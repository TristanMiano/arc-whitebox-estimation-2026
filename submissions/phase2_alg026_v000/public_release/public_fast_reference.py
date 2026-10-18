"""Sentinel32 pre-prune, depth-2 Strassen absolute half-cloud, ReLU trapezoid.

About half of every post-ReLU activation cloud is exactly zero.  The layer loop
orders the surviving columns by their nonzero rate, contracts the dense tail of
the ordered block in a single Strassen call, and then repairs only the rows that
actually hold a nonzero inside a stripped segment.  The only products skipped
are products against exact zeros, so the result is the same sum with fewer
multiplies; rows are never permuted, so every probe mask and the coordinate
bookkeeping stay where they were.
"""
from __future__ import annotations

import math

import flopscope.numpy as fnp
from whestbench import BaseEstimator, SetupContext
from whestbench.domain import MLP

N_BASES = 129
SALT = 4
PRUNE_ALPHA = 2.0e-2
STRASSEN_MIN_INNER = 16
STRASSEN_MIN_OUTPUT = 1_000_000
PREPRUNE_START_LAYER = 12
PROBE_DIRECTIONS = 2
PROBE_BASIS_SLOPE = 73
PROBE_LAYER_SHIFT = 17
PROBE_DIRECTION_STRIDE = 29
DEAD_RMS_MARGIN = 0.05
SENTINEL_SIZE = 32
FLOAT32_UNIT_ROUNDOFF = 2.0**-24
PREFIX_LEVELS = 12
PREFIX_TAU = 0.15
PREFIX_SAMPLE = 2048
STRASSEN_KMIN = 128


def _mm(a: fnp.ndarray, b: fnp.ndarray, out: fnp.ndarray) -> fnp.ndarray:
    """matmul with vecmat's broadcasting convention.

    ``_mm(a, b)`` treats ``a``'s trailing axis as the contracted one and
    lets ``b`` carry an extra leading singleton for the batch.  ``fnp.matmul``
    wants matching stacks, so drop that singleton when it is present.  Both ops
    are priced identically by the cost model (8,640,135,168 FLOPs for the same
    66048x256 @ 256x256 contraction, verified); this is purely a faster
    implementation of the same charged arithmetic.
    """
    if b.ndim == a.ndim + 1:
        b = b[..., 0, :, :]
    return fnp.matmul(a, b, out=out)


def _gf128_mul(a: int, b: int) -> int:
    out = 0
    for _ in range(7):
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & 0x80:
            a ^= 0x83
    return out & 0x7F


def _kerdock_signs(count: int) -> list[list[float]]:
    multiply = [
        [_gf128_mul(a, b) for b in range(128)]
        for a in range(128)
    ]

    def powers(exponent: int) -> list[int]:
        table = []
        for value in range(128):
            out = 1
            base = value
            remaining = exponent
            while remaining:
                if remaining & 1:
                    out = multiply[out][base]
                base = multiply[base][base]
                remaining >>= 1
            table.append(out)
        return table

    trace = []
    for element in range(128):
        out = 0
        value = element
        for _ in range(7):
            out ^= value
            value = multiply[value][value]
        trace.append(out)

    p3, p5, p9 = (powers(exponent) for exponent in (3, 5, 9))
    signs = []
    for a in range(count):
        phase_row = []
        linear_row = []
        for x in range(128):
            ax = multiply[a][x]
            phase = trace[p3[ax] ^ p5[ax] ^ p9[ax]]
            linear = trace[ax]
            phase_row.append(1.0 if phase == 0 else -1.0)
            linear_row.append(1.0 if (phase ^ linear) == 0 else -1.0)
        signs.append(phase_row + linear_row)
    return signs


def _mub_preact(
    rotated_weight: fnp.ndarray,
    signs: fnp.ndarray,
    n: int,
    mean_radius: float,
    output_cube: fnp.ndarray,
    output_flat: fnp.ndarray,
    stage_views: tuple[
        tuple[fnp.ndarray, ...],
        tuple[fnp.ndarray, ...],
    ],
) -> fnp.ndarray:
    """Evaluate the MUB transform with setup-cached contiguous stage views."""
    fnp.copyto(output_cube[0], rotated_weight)
    values = output_cube[1:]
    fnp.multiply(signs[:, :, None], rotated_weight[None, :, :], out=values)

    source_slot = 0
    step = 1
    stage = 0
    while step < n:
        source = stage_views[source_slot][stage]
        target = stage_views[1 - source_slot][stage]
        low = source[:, :, :step, :]
        high = source[:, :, step:, :]
        fnp.add(low, high, out=target[:, :, :step, :])
        fnp.subtract(low, high, out=target[:, :, step:, :])
        source_slot = 1 - source_slot
        step *= 2
        stage += 1
    if source_slot != 0:
        raise AssertionError("width must have an even number of FWHT stages")
    fnp.divide(values, math.sqrt(n), out=values)
    fnp.multiply(output_flat, mean_radius, out=output_flat)
    return output_flat


def _probe_rowmask(n: int, layer: int, stage: int) -> fnp.ndarray:
    bases = fnp.arange(N_BASES)[:, None]
    directions = fnp.arange(n)[None, :, None]
    probe_numbers = (
        fnp.arange(PROBE_DIRECTIONS)[None, :]
        + stage * PROBE_DIRECTIONS
    )
    selected = (
        PROBE_BASIS_SLOPE * bases
        + PROBE_LAYER_SHIFT * layer
        + PROBE_DIRECTION_STRIDE * probe_numbers
    ) % n
    half = fnp.reshape(
        fnp.any(directions == selected[:, None, :], axis=2),
        (N_BASES * n,),
    )
    return fnp.concatenate([half, half], axis=0)


def _ordered_probe_rows(n: int, layer: int, stage: int) -> list[int]:
    rows: list[int] = []
    for half in range(2):
        half_offset = half * N_BASES * n
        for basis in range(N_BASES):
            for local_probe in range(PROBE_DIRECTIONS):
                probe = local_probe + stage * PROBE_DIRECTIONS
                direction = (
                    PROBE_BASIS_SLOPE * basis
                    + PROBE_LAYER_SHIFT * layer
                    + PROBE_DIRECTION_STRIDE * probe
                ) % n
                rows.append(half_offset + basis * n + direction)
    return rows


def _mask_from_coordinates(
    full_coordinates: fnp.ndarray,
    selected_coordinates: fnp.ndarray,
) -> fnp.ndarray:
    return fnp.any(
        full_coordinates[:, None] == selected_coordinates[None, :],
        axis=1,
    )


def _confirmed_keep_mask(
    source: fnp.ndarray,
    active_weight: fnp.ndarray,
    full_coordinates: fnp.ndarray,
    n: int,
    layer: int,
    sentinel_rows: fnp.ndarray,
    nomination_rows: fnp.ndarray,
    confirmation_rows: fnp.ndarray,
) -> fnp.ndarray:
    sentinel_source = fnp.take(source, sentinel_rows, axis=0)
    sentinel_pre = sentinel_source @ active_weight

    # A column passing the original rule has every nomination preactivation
    # <= -margin*RMS <= 0.  Therefore any provably positive sentinel value can
    # be rejected before the full probe without changing the final mask.  The
    # guard covers both float32 dot products using a deliberately conservative
    # forward-error bound.  Since source is a ReLU cloud, max(source_row) times
    # ||weight_column||_1 bounds sum(abs(source_i * weight_i)).
    row_scale = fnp.max(sentinel_source, axis=1)
    weight_l1 = fnp.sum(
        fnp.abs(active_weight), axis=0, dtype=fnp.float64
    )
    roundoff_factor = (
        8.0 * active_weight.shape[0] * FLOAT32_UNIT_ROUNDOFF
    ) / (
        1.0 - 8.0 * active_weight.shape[0] * FLOAT32_UNIT_ROUNDOFF
    )
    roundoff_guard = (
        row_scale[:, None] * weight_l1[None, :] * roundoff_factor
    )
    definitely_positive = fnp.max(
        sentinel_pre - roundoff_guard, axis=0
    ) > 0.0
    survivors = fnp.logical_not(definitely_positive)
    survivor_coordinates = fnp.compress(
        survivors,
        full_coordinates,
        axis=0,
    )
    survivor_weight = fnp.compress(
        survivors,
        active_weight,
        axis=1,
    )

    nomination_source = fnp.compress(
        nomination_rows,
        source,
        axis=0,
    )
    nomination_pre = nomination_source @ survivor_weight
    nomination_rms = fnp.sqrt(
        fnp.mean(fnp.square(nomination_pre), axis=0)
    )
    nominated = fnp.less_equal(
        fnp.max(nomination_pre, axis=0),
        -DEAD_RMS_MARGIN * nomination_rms,
    )

    nominated_coordinates = fnp.compress(
        nominated,
        survivor_coordinates,
        axis=0,
    )
    nominated_weight = fnp.compress(
        nominated,
        survivor_weight,
        axis=1,
    )
    confirmation_source = fnp.compress(
        confirmation_rows,
        source,
        axis=0,
    )
    confirmation_pre = confirmation_source @ nominated_weight
    confirmation_rms = fnp.sqrt(
        fnp.mean(fnp.square(confirmation_pre), axis=0)
    )
    confirmed = fnp.less_equal(
        fnp.max(confirmation_pre, axis=0),
        -DEAD_RMS_MARGIN * confirmation_rms,
    )
    pruned_coordinates = fnp.compress(
        confirmed,
        nominated_coordinates,
        axis=0,
    )
    pruned = _mask_from_coordinates(full_coordinates, pruned_coordinates)
    return fnp.logical_not(pruned)


def _segment_cuts(
    cumulative: fnp.ndarray,
    width: int,
    budget: float,
) -> list[int]:
    """Greedy leading segments whose union bound on the hot rows stays low.

    `cumulative` is the running sum of the sampled per-column nonzero counts of
    the ordered active columns, so it is nondecreasing and every comparison
    against a threshold selects a prefix.  Growing a segment while that running
    sum stays under `budget` bounds the fraction of rows that need a repair by
    PREFIX_TAU.  Only the length of a compressed mask is read back, never a
    value, which is the same metadata read the column filter already performs.
    A badly placed cut costs speed and never correctness: exactness comes from
    the per-segment maximum taken in the layer loop.
    """
    limit = width - STRASSEN_KMIN
    if limit < 4:
        return []
    cuts: list[int] = []
    start = 0
    while len(cuts) < PREFIX_LEVELS and start < limit:
        if start:
            relative = cumulative - cumulative[start - 1]
        else:
            relative = cumulative
        within = fnp.less_equal(relative, budget)
        end = min(fnp.compress(within, within, axis=0).shape[0], limit)
        if end <= start:
            break
        cuts.append(end)
        start = end
    if not cuts or cuts[-1] < 4:
        return []
    return cuts


def _direct_flops(m: int, k: int, n: int) -> int:
    return 2 * m * k * n - m * n if n else 0


def _strassen_one_level_flops(m: int, k: int, n: int) -> int:
    even_k = k - (k & 1)
    half_m = m // 2
    half_k = even_k // 2
    half_n = n // 2
    block_product = 2 * half_m * half_k * half_n - half_m * half_n
    operand_sums = 5 * half_m * half_k + 5 * half_k * half_n
    output_sums = (12 if k & 1 else 8) * half_m * half_n
    odd_tail_product = m * n if k & 1 else 0
    return (
        7 * block_product
        + operand_sums
        + output_sums
        + odd_tail_product
    )


def _strassen_profitable(m: int, k: int, n: int) -> bool:
    even_k = k - (k & 1)
    if (
        m % 2
        or n % 2
        or even_k < STRASSEN_MIN_INNER
        or m * n < STRASSEN_MIN_OUTPUT
    ):
        return False
    return _strassen_one_level_flops(m, k, n) < _direct_flops(m, k, n)


def _strassen_two_level_core_flops(m: int, k: int, n: int) -> int:
    main_k = k - k % 4
    tail_k = k - main_k
    half_m = m // 2
    half_k = main_k // 2
    half_n = n // 2
    quarter_m = m // 4
    quarter_k = main_k // 4
    quarter_n = n // 4
    leaf_product = 2 * quarter_m * quarter_k * quarter_n - quarter_m * quarter_n
    outer_operands = 5 * half_m * half_k + 5 * half_k * half_n
    inner_operands = 7 * (
        5 * quarter_m * quarter_k + 5 * quarter_k * quarter_n
    )
    inner_outputs = 7 * 8 * quarter_m * quarter_n
    outer_outputs = 8 * half_m * half_n
    tail_product_and_add = 2 * m * tail_k * n
    return (
        49 * leaf_product
        + outer_operands
        + inner_operands
        + inner_outputs
        + outer_outputs
        + tail_product_and_add
    )


def _strassen_two_level_core_profitable(m: int, k: int, n: int) -> bool:
    main_k = k - k % 4
    if (
        m % 4
        or n % 4
        or main_k < 2 * STRASSEN_MIN_INNER
        or m * n < STRASSEN_MIN_OUTPUT
    ):
        return False
    return _strassen_two_level_core_flops(
        m,
        k,
        n,
    ) < _strassen_one_level_flops(m, k, n)


def _strassen_one_level_output_flops(m: int, k: int, n: int) -> int:
    even_n = n - (n & 1)
    total = 0
    if even_n:
        if _strassen_profitable(m, k, even_n):
            total += _strassen_one_level_flops(m, k, even_n)
        else:
            total += _direct_flops(m, k, even_n)
    return total + _direct_flops(m, k, n - even_n)


def _strassen_two_level_output_flops(m: int, k: int, n: int) -> int:
    core_n = n - n % 4
    return _strassen_two_level_core_flops(
        m,
        k,
        core_n,
    ) + _direct_flops(m, k, n - core_n)


def _strassen_two_level_output_profitable(m: int, k: int, n: int) -> bool:
    core_n = n - n % 4
    if not core_n or not _strassen_two_level_core_profitable(m, k, core_n):
        return False
    return _strassen_two_level_output_flops(
        m,
        k,
        n,
    ) < _strassen_one_level_output_flops(m, k, n)


def _strassen_even_output(
    a: fnp.ndarray,
    b: fnp.ndarray,
    result: fnp.ndarray,
    left_workspace: fnp.ndarray,
    right_workspace: fnp.ndarray,
    product_workspace: fnp.ndarray,
) -> fnp.ndarray:
    m, k = a.shape
    n = b.shape[1]
    if not _strassen_profitable(m, k, n):
        _mm(a, b, out=result)
        return result

    even_k = k - (k & 1)
    half_m = m // 2
    half_k = even_k // 2
    half_n = n // 2
    a11 = a[:half_m, :half_k]
    a12 = a[:half_m, half_k:even_k]
    a21 = a[half_m:, :half_k]
    a22 = a[half_m:, half_k:even_k]
    b11 = b[:half_k, :half_n]
    b12 = b[:half_k, half_n:]
    b21 = b[half_k:even_k, :half_n]
    b22 = b[half_k:even_k, half_n:]
    c11 = result[:half_m, :half_n]
    c12 = result[:half_m, half_n:]
    c21 = result[half_m:, :half_n]
    c22 = result[half_m:, half_n:]
    left = left_workspace[:, :half_k]
    right = right_workspace[:half_k, :half_n]
    product = product_workspace[:, :half_n]

    fnp.add(a11, a22, out=left)
    fnp.add(b11, b22, out=right)
    _mm(left, right, out=product)
    fnp.copyto(c11, product)
    fnp.copyto(c22, product)
    fnp.add(a21, a22, out=left)
    _mm(left, b11, out=product)
    fnp.copyto(c21, product)
    fnp.subtract(c22, product, out=c22)
    fnp.subtract(b12, b22, out=right)
    _mm(a11, right, out=product)
    fnp.copyto(c12, product)
    fnp.add(c22, product, out=c22)
    fnp.subtract(b21, b11, out=right)
    _mm(a22, right, out=product)
    fnp.add(c11, product, out=c11)
    fnp.add(c21, product, out=c21)
    fnp.add(a11, a12, out=left)
    _mm(left, b22, out=product)
    fnp.subtract(c11, product, out=c11)
    fnp.add(c12, product, out=c12)
    fnp.subtract(a21, a11, out=left)
    fnp.add(b11, b12, out=right)
    _mm(left, right, out=product)
    fnp.add(c22, product, out=c22)
    fnp.subtract(a12, a22, out=left)
    fnp.add(b21, b22, out=right)
    _mm(left, right, out=product)
    fnp.add(c11, product, out=c11)

    if k & 1:
        tail_top = a[:half_m, even_k]
        tail_bottom = a[half_m:, even_k]
        tail_left = b[even_k, :half_n]
        tail_right = b[even_k, half_n:]
        fnp.multiply(tail_top[:, None], tail_left[None, :], out=product)
        fnp.add(c11, product, out=c11)
        fnp.multiply(tail_top[:, None], tail_right[None, :], out=product)
        fnp.add(c12, product, out=c12)
        fnp.multiply(tail_bottom[:, None], tail_left[None, :], out=product)
        fnp.add(c21, product, out=c21)
        fnp.multiply(tail_bottom[:, None], tail_right[None, :], out=product)
        fnp.add(c22, product, out=c22)
    return result


def _strassen_one_level_output(
    a: fnp.ndarray,
    b: fnp.ndarray,
    result: fnp.ndarray,
    left_workspace: fnp.ndarray,
    right_workspace: fnp.ndarray,
    product_workspace: fnp.ndarray,
) -> fnp.ndarray:
    n = b.shape[1]
    even_n = n - (n & 1)
    if even_n:
        _strassen_even_output(
            a,
            b[:, :even_n],
            result[:, :even_n],
            left_workspace,
            right_workspace,
            product_workspace,
        )
    if n & 1:
        _mm(a, b[:, even_n:], out=result[:, even_n:])
    return result


def _fill_inner_operand_batches(
    a: fnp.ndarray,
    b: fnp.ndarray,
    left_stack: fnp.ndarray,
    right_stack: fnp.ndarray,
) -> None:
    half_m = a.shape[1] // 2
    half_k = a.shape[2] // 2
    half_n = b.shape[2] // 2
    a11 = a[:, :half_m, :half_k]
    a12 = a[:, :half_m, half_k:]
    a21 = a[:, half_m:, :half_k]
    a22 = a[:, half_m:, half_k:]
    b11 = b[:, :half_k, :half_n]
    b12 = b[:, :half_k, half_n:]
    b21 = b[:, half_k:, :half_n]
    b22 = b[:, half_k:, half_n:]
    left = fnp.reshape(
        left_stack,
        (7, 7, half_m, left_stack.shape[2]),
    )[:, :, :, :half_k]
    right = fnp.reshape(
        right_stack,
        (7, 7, right_stack.shape[2], right_stack.shape[3]),
    )[:, :, :half_k, :half_n]

    fnp.add(a11, a22, out=left[:, 0])
    fnp.add(b11, b22, out=right[:, 0])
    fnp.add(a21, a22, out=left[:, 1])
    fnp.copyto(right[:, 1], b11)
    fnp.copyto(left[:, 2], a11)
    fnp.subtract(b12, b22, out=right[:, 2])
    fnp.copyto(left[:, 3], a22)
    fnp.subtract(b21, b11, out=right[:, 3])
    fnp.add(a11, a12, out=left[:, 4])
    fnp.copyto(right[:, 4], b22)
    fnp.subtract(a21, a11, out=left[:, 5])
    fnp.add(b11, b12, out=right[:, 5])
    fnp.subtract(a12, a22, out=left[:, 6])
    fnp.add(b21, b22, out=right[:, 6])


def _combine_inner_product_batches(
    leaves: fnp.ndarray,
    products: fnp.ndarray,
) -> None:
    half_m = products.shape[1] // 2
    half_n = products.shape[2] // 2
    c11 = products[:, :half_m, :half_n]
    c12 = products[:, :half_m, half_n:]
    c21 = products[:, half_m:, :half_n]
    c22 = products[:, half_m:, half_n:]
    fnp.copyto(c11, leaves[:, 0])
    fnp.copyto(c22, leaves[:, 0])
    fnp.copyto(c21, leaves[:, 1])
    fnp.subtract(c22, leaves[:, 1], out=c22)
    fnp.copyto(c12, leaves[:, 2])
    fnp.add(c22, leaves[:, 2], out=c22)
    fnp.add(c11, leaves[:, 3], out=c11)
    fnp.add(c21, leaves[:, 3], out=c21)
    fnp.subtract(c11, leaves[:, 4], out=c11)
    fnp.add(c12, leaves[:, 4], out=c12)
    fnp.add(c22, leaves[:, 5], out=c22)
    fnp.add(c11, leaves[:, 6], out=c11)


def _strassen_two_level_core(
    a: fnp.ndarray,
    b: fnp.ndarray,
    result: fnp.ndarray,
    product: fnp.ndarray,
    outer_left_workspace: fnp.ndarray,
    outer_right_workspace: fnp.ndarray,
    leaf_left: fnp.ndarray,
    leaf_right: fnp.ndarray,
    leaf_products: fnp.ndarray,
) -> fnp.ndarray:
    m, k = a.shape
    n = b.shape[1]
    main_k = k - k % 4
    half_m = m // 2
    half_k = main_k // 2
    half_n = n // 2
    quarter_k = main_k // 4
    quarter_n = n // 4
    a11 = a[:half_m, :half_k]
    a12 = a[:half_m, half_k:main_k]
    a21 = a[half_m:, :half_k]
    a22 = a[half_m:, half_k:main_k]
    b11 = b[:half_k, :half_n]
    b12 = b[:half_k, half_n:]
    b21 = b[half_k:main_k, :half_n]
    b22 = b[half_k:main_k, half_n:]
    c11 = result[:half_m, :half_n]
    c12 = result[:half_m, half_n:]
    c21 = result[half_m:, :half_n]
    c22 = result[half_m:, half_n:]
    outer_left = outer_left_workspace[:, :, :half_k]
    outer_right = outer_right_workspace[:, :half_k, :half_n]

    fnp.add(a11, a22, out=outer_left[0])
    fnp.add(b11, b22, out=outer_right[0])
    fnp.add(a21, a22, out=outer_left[1])
    fnp.copyto(outer_right[1], b11)
    fnp.copyto(outer_left[2], a11)
    fnp.subtract(b12, b22, out=outer_right[2])
    fnp.copyto(outer_left[3], a22)
    fnp.subtract(b21, b11, out=outer_right[3])
    fnp.add(a11, a12, out=outer_left[4])
    fnp.copyto(outer_right[4], b22)
    fnp.subtract(a21, a11, out=outer_left[5])
    fnp.add(b11, b12, out=outer_right[5])
    fnp.subtract(a12, a22, out=outer_left[6])
    fnp.add(b21, b22, out=outer_right[6])

    _fill_inner_operand_batches(
        outer_left,
        outer_right,
        leaf_left,
        leaf_right,
    )
    leaf_output = leaf_products[:, :, :quarter_n]
    _mm(
        leaf_left[:, :, :quarter_k],
        leaf_right[:, :, :quarter_k, :quarter_n],
        out=leaf_output,
    )
    grouped_leaves = fnp.reshape(
        leaf_products,
        (7, 7, m // 4, leaf_products.shape[2]),
    )[:, :, :, :quarter_n]
    outer_products = outer_left_workspace[:, :, :half_n]
    _combine_inner_product_batches(grouped_leaves, outer_products)

    fnp.copyto(c11, outer_products[0])
    fnp.copyto(c22, outer_products[0])
    fnp.copyto(c21, outer_products[1])
    fnp.subtract(c22, outer_products[1], out=c22)
    fnp.copyto(c12, outer_products[2])
    fnp.add(c22, outer_products[2], out=c22)
    fnp.add(c11, outer_products[3], out=c11)
    fnp.add(c21, outer_products[3], out=c21)
    fnp.subtract(c11, outer_products[4], out=c11)
    fnp.add(c12, outer_products[4], out=c12)
    fnp.add(c22, outer_products[5], out=c22)
    fnp.add(c11, outer_products[6], out=c11)

    if main_k < k:
        tail_top = a[:half_m, main_k:k]
        tail_bottom = a[half_m:, main_k:k]
        tail_left = b[main_k:k, :half_n]
        tail_right = b[main_k:k, half_n:]
        tail_product = product[:, :half_n]
        _mm(tail_top, tail_left, out=tail_product)
        fnp.add(c11, tail_product, out=c11)
        _mm(tail_top, tail_right, out=tail_product)
        fnp.add(c12, tail_product, out=c12)
        _mm(tail_bottom, tail_left, out=tail_product)
        fnp.add(c21, tail_product, out=c21)
        _mm(tail_bottom, tail_right, out=tail_product)
        fnp.add(c22, tail_product, out=c22)
    return result


def _strassen_two_level_output(
    a: fnp.ndarray,
    b: fnp.ndarray,
    result: fnp.ndarray,
    left_workspace: fnp.ndarray,
    right_workspace: fnp.ndarray,
    product_workspace: fnp.ndarray,
    outer_left_workspace: fnp.ndarray,
    outer_right_workspace: fnp.ndarray,
    leaf_left_workspace: fnp.ndarray,
    leaf_right_workspace: fnp.ndarray,
    leaf_product_workspace: fnp.ndarray,
) -> fnp.ndarray:
    m, k = a.shape
    n = b.shape[1]
    if not _strassen_two_level_output_profitable(m, k, n):
        return _strassen_one_level_output(
            a,
            b,
            result,
            left_workspace,
            right_workspace,
            product_workspace,
        )
    core_n = n - n % 4
    _strassen_two_level_core(
        a,
        b[:, :core_n],
        result[:, :core_n],
        product_workspace,
        outer_left_workspace,
        outer_right_workspace,
        leaf_left_workspace,
        leaf_right_workspace,
        leaf_product_workspace,
    )
    if core_n < n:
        _mm(a, b[:, core_n:], out=result[:, core_n:])
    return result


def _strassen_three_level_core_flops(m: int, k: int, n: int) -> int:
    main_k = k - k % 8
    tail_k = k - main_k
    half_m = m // 2
    half_k = main_k // 2
    half_n = n // 2
    quarter_m = m // 4
    quarter_k = main_k // 4
    quarter_n = n // 4
    eighth_m = m // 8
    eighth_k = main_k // 8
    eighth_n = n // 8
    leaf_product = (
        2 * eighth_m * eighth_k * eighth_n - eighth_m * eighth_n
    )
    outer_operands = 4 * half_m * half_k + 4 * half_k * half_n
    middle_operands = 7 * (
        4 * quarter_m * quarter_k + 4 * quarter_k * quarter_n
    )
    inner_operands = 49 * (
        4 * eighth_m * eighth_k + 4 * eighth_k * eighth_n
    )
    inner_outputs = 49 * 7 * eighth_m * eighth_n
    middle_outputs = 7 * 7 * quarter_m * quarter_n
    outer_outputs = 7 * half_m * half_n
    tail_product_and_add = 2 * m * tail_k * n
    return (
        343 * leaf_product
        + outer_operands
        + middle_operands
        + inner_operands
        + inner_outputs
        + middle_outputs
        + outer_outputs
        + tail_product_and_add
    )


def _strassen_three_level_core_profitable(m: int, k: int, n: int) -> bool:
    main_k = k - k % 8
    if (
        m % 8
        or n % 8
        or main_k < 4 * STRASSEN_MIN_INNER
        or m * n < STRASSEN_MIN_OUTPUT
    ):
        return False
    return _strassen_three_level_core_flops(
        m,
        k,
        n,
    ) < _strassen_two_level_core_flops(m, k, n)


def _strassen_three_level_output_flops(m: int, k: int, n: int) -> int:
    core_n = n - n % 8
    return _strassen_three_level_core_flops(
        m,
        k,
        core_n,
    ) + _direct_flops(m, k, n - core_n)


def _strassen_three_level_output_profitable(m: int, k: int, n: int) -> bool:
    core_n = n - n % 8
    if not core_n or not _strassen_three_level_core_profitable(m, k, core_n):
        return False
    return _strassen_three_level_output_flops(
        m,
        k,
        n,
    ) < _strassen_two_level_output_flops(m, k, n)


def _fill_batched_operands_d3(
    a: fnp.ndarray,
    b: fnp.ndarray,
    left_stack: fnp.ndarray,
    right_stack: fnp.ndarray,
) -> None:
    half_m = a.shape[-2] // 2
    half_k = a.shape[-1] // 2
    half_n = b.shape[-1] // 2
    a11 = a[..., :half_m, :half_k]
    a12 = a[..., :half_m, half_k:]
    a21 = a[..., half_m:, :half_k]
    a22 = a[..., half_m:, half_k:]
    b11 = b[..., :half_k, :half_n]
    b12 = b[..., :half_k, half_n:]
    b21 = b[..., half_k:, :half_n]
    b22 = b[..., half_k:, half_n:]
    left = left_stack[..., :half_m, :half_k]
    right = right_stack[..., :half_k, :half_n]

    # Store the seven products in physical order (P3,P0,P1,P2,P4,P5,P6).
    # This makes all three direct A blocks and all three direct B blocks each
    # contiguous, so two concatenate calls replace six independent copies at
    # exactly the same metered movement cost.
    fnp.concatenate(
        (
            a22[..., None, :, :],
            a11[..., None, :, :],
            a12[..., None, :, :],
        ),
        axis=-3,
        out=left[..., :3, :, :],
    )
    fnp.concatenate(
        (
            b11[..., None, :, :],
            b21[..., None, :, :],
            b22[..., None, :, :],
        ),
        axis=-3,
        out=right[..., 1:4, :, :],
    )
    fnp.add(a21, a22, out=left[..., 4, :, :])
    fnp.subtract(left[..., 4, :, :], a11, out=left[..., 5, :, :])
    fnp.subtract(a11, a21, out=left[..., 6, :, :])
    fnp.subtract(a12, left[..., 5, :, :], out=left[..., 3, :, :])
    fnp.subtract(b12, b11, out=right[..., 4, :, :])
    fnp.subtract(b22, right[..., 4, :, :], out=right[..., 5, :, :])
    fnp.subtract(b22, b12, out=right[..., 6, :, :])
    fnp.subtract(
        right[..., 5, :, :],
        b21,
        out=right[..., 0, :, :],
    )


def _combine_seven_products_d3(
    products: fnp.ndarray,
    result: fnp.ndarray,
) -> None:
    half_m = result.shape[0] // 2
    half_n = result.shape[1] // 2
    c11 = result[:half_m, :half_n]
    c12 = result[:half_m, half_n:]
    c21 = result[half_m:, :half_n]
    c22 = result[half_m:, half_n:]
    fnp.add(products[1], products[2], out=c11)
    fnp.add(products[1], products[5], out=c12)
    fnp.add(c12, products[6], out=c21)
    fnp.add(c21, products[4], out=c22)
    fnp.add(c12, products[4], out=c12)
    fnp.add(c12, products[3], out=c12)
    fnp.subtract(c21, products[0], out=c21)


def _combine_batched_products_d3(
    leaves: fnp.ndarray,
    products: fnp.ndarray,
) -> None:
    half_m = products.shape[-2] // 2
    half_n = products.shape[-1] // 2
    c11 = products[..., :half_m, :half_n]
    c12 = products[..., :half_m, half_n:]
    c21 = products[..., half_m:, :half_n]
    c22 = products[..., half_m:, half_n:]
    fnp.add(leaves[..., 1, :, :], leaves[..., 2, :, :], out=c11)
    fnp.add(leaves[..., 1, :, :], leaves[..., 5, :, :], out=c12)
    fnp.add(c12, leaves[..., 6, :, :], out=c21)
    fnp.add(c21, leaves[..., 4, :, :], out=c22)
    fnp.add(c12, leaves[..., 4, :, :], out=c12)
    fnp.add(c12, leaves[..., 3, :, :], out=c12)
    fnp.subtract(c21, leaves[..., 0, :, :], out=c21)


def _strassen_three_level_core(
    a: fnp.ndarray,
    b: fnp.ndarray,
    result: fnp.ndarray,
    outer_left_workspace: fnp.ndarray,
    outer_right_workspace: fnp.ndarray,
    middle_left_workspace: fnp.ndarray,
    middle_right_workspace: fnp.ndarray,
    leaf_left_workspace: fnp.ndarray,
    leaf_right_workspace: fnp.ndarray,
    leaf_product_workspace: fnp.ndarray,
    middle_product_workspace: fnp.ndarray,
    outer_product_workspace: fnp.ndarray,
) -> fnp.ndarray:
    m, k = a.shape
    n = b.shape[1]
    main_k = k - k % 8
    half_m = m // 2
    half_k = main_k // 2
    half_n = n // 2
    quarter_m = m // 4
    quarter_k = main_k // 4
    quarter_n = n // 4
    eighth_m = m // 8
    eighth_k = main_k // 8
    eighth_n = n // 8
    core_a = a[:, :main_k]
    core_b = b[:main_k, :]

    outer_left = outer_left_workspace[:, :, :half_m, :half_k]
    outer_right = outer_right_workspace[:, :, :half_k, :half_n]
    middle_left = middle_left_workspace[:, :, :quarter_m, :quarter_k]
    middle_right = middle_right_workspace[:, :, :quarter_k, :quarter_n]

    _fill_batched_operands_d3(
        core_a[None, :, :],
        core_b[None, :, :],
        outer_left,
        outer_right,
    )
    _fill_batched_operands_d3(
        outer_left[0],
        outer_right[0],
        middle_left,
        middle_right,
    )
    leaf_left = leaf_left_workspace[:, :, :, :eighth_m, :eighth_k]
    leaf_right = leaf_right_workspace[
        :, :, :, :, :eighth_k, :eighth_n
    ]
    _fill_batched_operands_d3(
        middle_left,
        middle_right,
        leaf_left,
        leaf_right[:, :, :, 0],
    )
    leaf_products = leaf_product_workspace[
        :, :, :, :eighth_m, :eighth_n
    ]
    _mm(leaf_left, leaf_right, out=leaf_products)

    middle_products = middle_product_workspace[
        :, :, :quarter_m, :quarter_n
    ]
    outer_products = outer_product_workspace[:, :half_m, :half_n]
    _combine_batched_products_d3(leaf_products, middle_products)
    _combine_batched_products_d3(middle_products, outer_products)
    _combine_seven_products_d3(outer_products, result)

    if main_k < k:
        tail_product = outer_product_workspace[0, :half_m, :half_n]
        tail_top = a[:half_m, main_k:k]
        tail_bottom = a[half_m:, main_k:k]
        tail_left = b[main_k:k, :half_n]
        tail_right = b[main_k:k, half_n:]
        c11 = result[:half_m, :half_n]
        c12 = result[:half_m, half_n:]
        c21 = result[half_m:, :half_n]
        c22 = result[half_m:, half_n:]
        _mm(tail_top, tail_left, out=tail_product)
        fnp.add(c11, tail_product, out=c11)
        _mm(tail_top, tail_right, out=tail_product)
        fnp.add(c12, tail_product, out=c12)
        _mm(tail_bottom, tail_left, out=tail_product)
        fnp.add(c21, tail_product, out=c21)
        _mm(tail_bottom, tail_right, out=tail_product)
        fnp.add(c22, tail_product, out=c22)
    return result


def _strassen_three_level_output(
    a: fnp.ndarray,
    b: fnp.ndarray,
    result: fnp.ndarray,
    outer_left_workspace: fnp.ndarray,
    outer_right_workspace: fnp.ndarray,
    middle_left_workspace: fnp.ndarray,
    middle_right_workspace: fnp.ndarray,
    leaf_left_workspace: fnp.ndarray,
    leaf_right_workspace: fnp.ndarray,
    leaf_product_workspace: fnp.ndarray,
    middle_product_workspace: fnp.ndarray,
    outer_product_workspace: fnp.ndarray,
) -> fnp.ndarray:
    m, k = a.shape
    n = b.shape[1]
    if not _strassen_three_level_output_profitable(m, k, n):
        _mm(a, b, out=result)
        return result
    core_n = n - n % 8
    _strassen_three_level_core(
        a,
        b[:, :core_n],
        result[:, :core_n],
        outer_left_workspace,
        outer_right_workspace,
        middle_left_workspace,
        middle_right_workspace,
        leaf_left_workspace,
        leaf_right_workspace,
        leaf_product_workspace,
        middle_product_workspace,
        outer_product_workspace,
    )
    if core_n < n:
        _mm(a, b[:, core_n:], out=result[:, core_n:])
    return result


def _strassen_four_level_core_flops(m: int, k: int, n: int) -> int:
    main_k = k - k % 16
    tail_k = k - main_k
    half_m = m // 2
    half_k = main_k // 2
    half_n = n // 2
    outer_operands = 4 * half_m * half_k + 4 * half_k * half_n
    outer_outputs = 7 * half_m * half_n
    tail_product_and_add = 2 * m * tail_k * n
    return (
        7 * _strassen_three_level_core_flops(
            half_m,
            half_k,
            half_n,
        )
        + outer_operands
        + outer_outputs
        + tail_product_and_add
    )


def _strassen_four_level_output_flops(m: int, k: int, n: int) -> int:
    core_n = n - n % 16
    if not core_n:
        return _direct_flops(m, k, n)
    return _strassen_four_level_core_flops(
        m,
        k,
        core_n,
    ) + _direct_flops(m, k, n - core_n)


def _strassen_four_level_output_profitable(
    m: int,
    k: int,
    n: int,
) -> bool:
    main_k = k - k % 16
    core_n = n - n % 16
    return bool(
        core_n
        and m % 16 == 0
        and main_k >= 8 * STRASSEN_MIN_INNER
        and m * core_n >= STRASSEN_MIN_OUTPUT
        and _strassen_four_level_output_flops(m, k, n)
        < _strassen_three_level_output_flops(m, k, n)
    )


def _fill_outer_group_d4(
    group: int,
    a: fnp.ndarray,
    b: fnp.ndarray,
    left: fnp.ndarray,
    right: fnp.ndarray,
) -> None:
    half_m = a.shape[0] // 2
    half_k = a.shape[1] // 2
    half_n = b.shape[1] // 2
    a11 = a[:half_m, :half_k]
    a12 = a[:half_m, half_k:]
    a21 = a[half_m:, :half_k]
    a22 = a[half_m:, half_k:]
    b11 = b[:half_k, :half_n]
    b12 = b[:half_k, half_n:]
    b21 = b[half_k:, :half_n]
    b22 = b[half_k:, half_n:]
    if group == 0:
        fnp.copyto(left[0], a11)
        fnp.copyto(right[0], b11)
        fnp.copyto(left[1], a12)
        fnp.copyto(right[1], b21)
        fnp.subtract(a11, a21, out=left[2])
        fnp.subtract(b22, b12, out=right[2])
    else:
        fnp.add(a21, a22, out=left[2])
        fnp.subtract(left[2], a11, out=left[3])
        fnp.subtract(a12, left[3], out=left[0])
        fnp.copyto(left[1], a22)
        fnp.subtract(b12, b11, out=right[2])
        fnp.subtract(b22, right[2], out=right[3])
        fnp.subtract(right[3], b21, out=right[1])
        fnp.copyto(right[0], b22)


def _combine_grouped_outer_products_d4(
    products: fnp.ndarray,
    result: fnp.ndarray,
) -> None:
    half_m = result.shape[0] // 2
    half_n = result.shape[1] // 2
    c11 = result[:half_m, :half_n]
    c12 = result[:half_m, half_n:]
    c21 = result[half_m:, :half_n]
    c22 = result[half_m:, half_n:]
    # The two memory-bounded groups are stored as
    # (p0, p1, p6, p2, p3, p4, p5).  Recombine directly in that order.
    fnp.add(products[0], products[1], out=c11)
    fnp.add(products[0], products[6], out=c12)
    fnp.add(c12, products[2], out=c21)
    fnp.add(c21, products[5], out=c22)
    fnp.add(c12, products[5], out=c12)
    fnp.add(c12, products[3], out=c12)
    fnp.subtract(c21, products[4], out=c21)


def _strassen_four_level_core(
    a: fnp.ndarray,
    b: fnp.ndarray,
    result: fnp.ndarray,
    outer_left_workspace: fnp.ndarray,
    outer_right_workspace: fnp.ndarray,
    middle_left_workspace: fnp.ndarray,
    middle_right_workspace: fnp.ndarray,
    leaf_left_workspace: fnp.ndarray,
    leaf_right_workspace: fnp.ndarray,
    leaf_product_workspace: fnp.ndarray,
    middle_product_workspace: fnp.ndarray,
    outer_product_workspace: fnp.ndarray,
    d4_leaf_left_workspace: fnp.ndarray,
    d4_leaf_right_workspace: fnp.ndarray,
    d4_leaf_product_workspace: fnp.ndarray,
) -> fnp.ndarray:
    m, k = a.shape
    n = b.shape[1]
    main_k = k - k % 16
    half_m = m // 2
    half_k = main_k // 2
    half_n = n // 2
    quarter_m = m // 4
    quarter_k = main_k // 4
    quarter_n = n // 4
    eighth_m = m // 8
    eighth_k = main_k // 8
    eighth_n = n // 8
    sixteenth_m = m // 16
    sixteenth_k = main_k // 16
    sixteenth_n = n // 16
    core_a = a[:, :main_k]
    core_b = b[:main_k, :]

    # Materialize all seven outer products together.  The leaf arrays remain
    # below the evaluator's per-array cap, while one vecmat call removes the
    # second D4 dispatch that dominated the two-group implementation's wall.
    batch = 7
    input_left = outer_left_workspace[0, :batch, :half_m, :half_k]
    input_right = outer_right_workspace[0, :batch, :half_k, :half_n]
    # Use the same packed physical product order as every inner D3 level.
    # The direct A blocks (P3,P0,P1) and direct B blocks (P0,P1,P2) are each
    # contiguous, so two concatenate calls replace the outer level's six
    # independent copies without changing any product or arithmetic order.
    _fill_batched_operands_d3(
        core_a,
        core_b,
        input_left,
        input_right,
    )

    level2_left = middle_left_workspace[:batch, :, :quarter_m, :quarter_k]
    level2_right = middle_right_workspace[:batch, :, :quarter_k, :quarter_n]
    _fill_batched_operands_d3(
        input_left,
        input_right,
        level2_left,
        level2_right,
    )

    level3_left = leaf_left_workspace[
        :batch, :, :, :eighth_m, :eighth_k
    ]
    level3_right = leaf_right_workspace[
        :batch, :, :, :, :eighth_k, :eighth_n
    ]
    _fill_batched_operands_d3(
        level2_left,
        level2_right,
        level3_left,
        level3_right[:, :, :, 0],
    )

    level4_left = d4_leaf_left_workspace[
        :batch, :, :, :, :sixteenth_m, :sixteenth_k
    ]
    level4_right = d4_leaf_right_workspace[
        :batch, :, :, :, :, :sixteenth_k, :sixteenth_n
    ]
    _fill_batched_operands_d3(
        level3_left,
        level3_right[:, :, :, 0],
        level4_left,
        level4_right[:, :, :, :, 0],
    )
    level4_products = d4_leaf_product_workspace[
        :batch, :, :, :, :sixteenth_m, :sixteenth_n
    ]
    _mm(level4_left, level4_right, out=level4_products)

    level3_products = leaf_product_workspace[
        :batch, :, :, :eighth_m, :eighth_n
    ]
    level2_products = middle_product_workspace[
        :batch, :, :quarter_m, :quarter_n
    ]
    level1_products = outer_product_workspace[:batch, :half_m, :half_n]
    _combine_batched_products_d3(level4_products, level3_products)
    _combine_batched_products_d3(level3_products, level2_products)
    _combine_batched_products_d3(level2_products, level1_products)
    _combine_seven_products_d3(
        outer_product_workspace[:, :half_m, :half_n],
        result,
    )

    if main_k < k:
        tail_product = outer_product_workspace[0, :half_m, :half_n]
        tail_top = a[:half_m, main_k:k]
        tail_bottom = a[half_m:, main_k:k]
        tail_left = b[main_k:k, :half_n]
        tail_right = b[main_k:k, half_n:]
        c11 = result[:half_m, :half_n]
        c12 = result[:half_m, half_n:]
        c21 = result[half_m:, :half_n]
        c22 = result[half_m:, half_n:]
        _mm(tail_top, tail_left, out=tail_product)
        fnp.add(c11, tail_product, out=c11)
        _mm(tail_top, tail_right, out=tail_product)
        fnp.add(c12, tail_product, out=c12)
        _mm(tail_bottom, tail_left, out=tail_product)
        fnp.add(c21, tail_product, out=c21)
        _mm(tail_bottom, tail_right, out=tail_product)
        fnp.add(c22, tail_product, out=c22)
    return result


def _strassen_four_level_output(
    a: fnp.ndarray,
    b: fnp.ndarray,
    result: fnp.ndarray,
    outer_left_workspace: fnp.ndarray,
    outer_right_workspace: fnp.ndarray,
    middle_left_workspace: fnp.ndarray,
    middle_right_workspace: fnp.ndarray,
    leaf_left_workspace: fnp.ndarray,
    leaf_right_workspace: fnp.ndarray,
    leaf_product_workspace: fnp.ndarray,
    middle_product_workspace: fnp.ndarray,
    outer_product_workspace: fnp.ndarray,
    d4_leaf_left_workspace: fnp.ndarray,
    d4_leaf_right_workspace: fnp.ndarray,
    d4_leaf_product_workspace: fnp.ndarray,
) -> fnp.ndarray:
    m, k = a.shape
    n = b.shape[1]
    if not _strassen_four_level_output_profitable(m, k, n):
        return _strassen_three_level_output(
            a,
            b,
            result,
            outer_left_workspace,
            outer_right_workspace,
            middle_left_workspace,
            middle_right_workspace,
            leaf_left_workspace,
            leaf_right_workspace,
            leaf_product_workspace,
            middle_product_workspace,
            outer_product_workspace,
        )
    core_n = n - n % 16
    _strassen_four_level_core(
        a,
        b[:, :core_n],
        result[:, :core_n],
        outer_left_workspace,
        outer_right_workspace,
        middle_left_workspace,
        middle_right_workspace,
        leaf_left_workspace,
        leaf_right_workspace,
        leaf_product_workspace,
        middle_product_workspace,
        outer_product_workspace,
        d4_leaf_left_workspace,
        d4_leaf_right_workspace,
        d4_leaf_product_workspace,
    )
    if core_n < n:
        _mm(a, b[:, core_n:], out=result[:, core_n:])
    return result


class Estimator(BaseEstimator):
    def __init__(self) -> None:
        self._signs = None
        self._mean_radius = None
        self._full_coordinates = None
        self._full_coordinate_mask = None
        self._probe_masks: dict[tuple[int, int], fnp.ndarray] = {}
        self._sentinel_rows: dict[int, fnp.ndarray] = {}
        self._activation_buffer = None
        self._initial_cloud_buffer = None
        self._outer_left_workspace = None
        self._outer_right_workspace = None
        self._middle_left_workspace = None
        self._middle_right_workspace = None
        self._leaf_left_workspace = None
        self._leaf_right_workspace = None
        self._leaf_product_workspace = None
        self._middle_product_workspace = None
        self._outer_product_workspace = None
        self._d4_leaf_left_workspace = None
        self._d4_leaf_right_workspace = None
        self._d4_leaf_product_workspace = None
        self._absolute_d2_workspaces = None
        self._mub_output_cube = None
        self._mub_output_flat = None
        self._mub_scratch_cube = None
        self._mub_stage_views: tuple[
            tuple[fnp.ndarray, ...],
            tuple[fnp.ndarray, ...],
        ] | None = None
        self._workspace_allocated_bytes = 0

    def setup(self, ctx: SetupContext) -> None:
        self._signs = None
        self._mean_radius = None
        self._full_coordinates = None
        self._full_coordinate_mask = None
        self._probe_masks.clear()
        self._sentinel_rows.clear()
        if ctx.width == 256:
            self._signs = fnp.asarray(
                _kerdock_signs(N_BASES - 1),
                dtype=fnp.float32,
            )
            self._mean_radius = math.exp(
                0.5 * math.log(2.0)
                + math.lgamma((ctx.width + 1) / 2.0)
                - math.lgamma(ctx.width / 2.0)
            )
            self._ensure_mub_workspaces(ctx.width, fnp.float32)
            self._full_coordinates = fnp.arange(ctx.width)
            self._full_coordinate_mask = fnp.ones(ctx.width, dtype=bool)
            for layer in range(PREPRUNE_START_LAYER, ctx.depth):
                ordered = _ordered_probe_rows(
                    ctx.width,
                    layer,
                    stage=0,
                )
                probe_count = len(ordered)
                self._sentinel_rows[layer] = fnp.asarray(
                    [
                        ordered[index * probe_count // SENTINEL_SIZE]
                        for index in range(SENTINEL_SIZE)
                    ]
                )
                self._probe_masks[(layer, 0)] = _probe_rowmask(
                    ctx.width,
                    layer,
                    stage=0,
                )
                self._probe_masks[(layer, 1)] = _probe_rowmask(
                    ctx.width,
                    layer,
                    stage=1,
                )
            if ctx.depth >= 3:
                self._ensure_workspaces_shape(
                    (2 * N_BASES * ctx.width, ctx.width),
                    fnp.float32,
                    ctx.width,
                )
                self._cache_absolute_d2_workspaces(
                    N_BASES * ctx.width,
                    ctx.width,
                    ctx.width,
                )

    def _ensure_mub_workspaces(self, n: int, dtype) -> None:
        if (
            self._mub_output_cube is not None
            and self._mub_output_cube.shape == (N_BASES, n, n)
        ):
            return
        output_cube = fnp.empty((N_BASES, n, n), dtype=dtype)
        scratch_cube = fnp.empty((N_BASES - 1, n, n), dtype=dtype)
        output_flat = fnp.reshape(output_cube, (N_BASES * n, n))
        stage_views: list[list[fnp.ndarray]] = [[], []]
        step = 1
        while step < n:
            shape = (N_BASES - 1, n // (2 * step), 2 * step, n)
            stage_views[0].append(fnp.reshape(output_cube[1:], shape))
            stage_views[1].append(fnp.reshape(scratch_cube, shape))
            step *= 2
        self._mub_output_cube = output_cube
        self._mub_output_flat = output_flat
        self._mub_scratch_cube = scratch_cube
        self._mub_stage_views = (
            tuple(stage_views[0]),
            tuple(stage_views[1]),
        )

    def _ensure_workspaces(self, h: fnp.ndarray, n: int) -> None:
        self._ensure_workspaces_shape(h.shape, h.dtype, n)

    def _ensure_workspaces_shape(
        self,
        shape: tuple[int, ...],
        dtype,
        n: int,
    ) -> None:
        if (
            self._activation_buffer is not None
            and self._initial_cloud_buffer is not None
            and self._activation_buffer.shape == shape
        ):
            return
        half_rows = shape[0] // 2
        quarter_rows = shape[0] // 4
        eighth_rows = shape[0] // 8
        sixteenth_rows = shape[0] // 16
        half_width = n // 2
        quarter_width = n // 4
        eighth_width = n // 8
        sixteenth_width = n // 16
        self._activation_buffer = fnp.empty(shape, dtype=dtype)
        self._initial_cloud_buffer = fnp.empty(shape, dtype=dtype)
        self._outer_left_workspace = fnp.empty(
            (1, 7, half_rows, half_width),
            dtype=dtype,
        )
        self._outer_right_workspace = fnp.empty(
            (1, 7, half_width, half_width),
            dtype=dtype,
        )
        self._middle_left_workspace = fnp.empty(
            (7, 7, quarter_rows, quarter_width),
            dtype=dtype,
        )
        self._middle_right_workspace = fnp.empty(
            (7, 7, quarter_width, quarter_width),
            dtype=dtype,
        )
        self._leaf_left_workspace = fnp.empty(
            (7, 7, 7, eighth_rows, eighth_width),
            dtype=dtype,
        )
        self._leaf_right_workspace = fnp.empty(
            (7, 7, 7, 1, eighth_width, eighth_width),
            dtype=dtype,
        )
        self._leaf_product_workspace = fnp.empty(
            (7, 7, 7, eighth_rows, eighth_width),
            dtype=dtype,
        )
        self._middle_product_workspace = fnp.empty(
            (7, 7, quarter_rows, quarter_width),
            dtype=dtype,
        )
        self._outer_product_workspace = fnp.empty(
            (7, half_rows, half_width),
            dtype=dtype,
        )
        self._d4_leaf_left_workspace = fnp.empty(
            (7, 7, 7, 7, sixteenth_rows, sixteenth_width),
            dtype=dtype,
        )
        self._d4_leaf_right_workspace = fnp.empty(
            (7, 7, 7, 7, 1, sixteenth_width, sixteenth_width),
            dtype=dtype,
        )
        self._d4_leaf_product_workspace = fnp.empty(
            (7, 7, 7, 7, sixteenth_rows, sixteenth_width),
            dtype=dtype,
        )
        self._absolute_d2_workspaces = None
        self._workspace_allocated_bytes = sum(
            int(value.nbytes)
            for value in (
                self._activation_buffer,
                self._initial_cloud_buffer,
                self._outer_left_workspace,
                self._outer_right_workspace,
                self._middle_left_workspace,
                self._middle_right_workspace,
                self._leaf_left_workspace,
                self._leaf_right_workspace,
                self._leaf_product_workspace,
                self._middle_product_workspace,
                self._outer_product_workspace,
                self._d4_leaf_left_workspace,
                self._d4_leaf_right_workspace,
                self._d4_leaf_product_workspace,
                self._mub_output_cube,
                self._mub_scratch_cube,
            )
        )

    def _cache_absolute_d2_workspaces(self, m: int, k: int, n: int) -> None:
        half_m = m // 2
        half_k = k // 2
        half_n = n // 2
        quarter_m = m // 4
        quarter_k = k // 4
        quarter_n = n // 4
        assert self._leaf_left_workspace is not None
        assert self._leaf_right_workspace is not None
        assert self._leaf_product_workspace is not None

        left_flat = fnp.reshape(self._leaf_left_workspace, (-1,))
        left_size = half_m * half_k
        outer_left_size = 7 * half_m * half_k
        leaf_left_size = 49 * quarter_m * quarter_k
        left_workspace = fnp.reshape(
            left_flat[:left_size],
            (half_m, half_k),
        )
        outer_left_workspace = fnp.reshape(
            left_flat[left_size : left_size + outer_left_size],
            (7, half_m, half_k),
        )
        leaf_left_workspace = fnp.reshape(
            left_flat[
                left_size + outer_left_size :
                left_size + outer_left_size + leaf_left_size
            ],
            (49, quarter_m, quarter_k),
        )

        right_flat = fnp.reshape(self._leaf_right_workspace, (-1,))
        right_size = half_k * half_n
        outer_right_size = 7 * half_k * half_n
        leaf_right_size = 49 * quarter_k * quarter_n
        right_workspace = fnp.reshape(
            right_flat[:right_size],
            (half_k, half_n),
        )
        outer_right_workspace = fnp.reshape(
            right_flat[right_size : right_size + outer_right_size],
            (7, half_k, half_n),
        )
        leaf_right_workspace = fnp.reshape(
            right_flat[
                right_size + outer_right_size :
                right_size + outer_right_size + leaf_right_size
            ],
            (49, 1, quarter_k, quarter_n),
        )

        product_flat = fnp.reshape(self._leaf_product_workspace, (-1,))
        product_size = half_m * half_n
        leaf_product_size = 49 * quarter_m * quarter_n
        product_workspace = fnp.reshape(
            product_flat[:product_size],
            (half_m, half_n),
        )
        leaf_product_workspace = fnp.reshape(
            product_flat[
                product_size : product_size + leaf_product_size
            ],
            (49, quarter_m, quarter_n),
        )
        self._absolute_d2_workspaces = (
            left_workspace,
            right_workspace,
            product_workspace,
            outer_left_workspace,
            outer_right_workspace,
            leaf_left_workspace,
            leaf_right_workspace,
            leaf_product_workspace,
        )

    def _absolute_depth2(
        self,
        source: fnp.ndarray,
        weight: fnp.ndarray,
        result: fnp.ndarray,
    ) -> fnp.ndarray:
        return _strassen_four_level_output(
            source,
            weight,
            result,
            self._outer_left_workspace,
            self._outer_right_workspace,
            self._middle_left_workspace,
            self._middle_right_workspace,
            self._leaf_left_workspace,
            self._leaf_right_workspace,
            self._leaf_product_workspace,
            self._middle_product_workspace,
            self._outer_product_workspace,
            self._d4_leaf_left_workspace,
            self._d4_leaf_right_workspace,
            self._d4_leaf_product_workspace,
        )

    def _multiply(
        self,
        source: fnp.ndarray,
        weight: fnp.ndarray,
        destination: fnp.ndarray,
    ) -> None:
        """Dispatch one contraction on the shipped depth-4 or depth-3 path."""
        if _strassen_four_level_output_profitable(
            source.shape[0],
            source.shape[1],
            destination.shape[1],
        ):
            _strassen_four_level_output(
                source,
                weight,
                destination,
                self._outer_left_workspace,
                self._outer_right_workspace,
                self._middle_left_workspace,
                self._middle_right_workspace,
                self._leaf_left_workspace,
                self._leaf_right_workspace,
                self._leaf_product_workspace,
                self._middle_product_workspace,
                self._outer_product_workspace,
                self._d4_leaf_left_workspace,
                self._d4_leaf_right_workspace,
                self._d4_leaf_product_workspace,
            )
        else:
            _strassen_three_level_output(
                source,
                weight,
                destination,
                self._outer_left_workspace,
                self._outer_right_workspace,
                self._middle_left_workspace,
                self._middle_right_workspace,
                self._leaf_left_workspace,
                self._leaf_right_workspace,
                self._leaf_product_workspace,
                self._middle_product_workspace,
                self._outer_product_workspace,
            )

    def predict(self, mlp: MLP, budget: int) -> fnp.ndarray:
        _ = budget
        n = mlp.width
        rng = fnp.random.default_rng(mlp.seed + 1_000_003 * SALT)
        gaussian = rng.standard_normal((n, n)).astype(fnp.float32)
        q, r = fnp.linalg.qr(gaussian)
        q = q * fnp.sign(fnp.diag(r))
        mean_radius = self._mean_radius
        if mean_radius is None:
            mean_radius = math.exp(
                0.5 * math.log(2.0)
                + math.lgamma((n + 1) / 2.0)
                - math.lgamma(n / 2.0)
            )

        if self._signs is None:
            positive = mean_radius * fnp.transpose(q)
            pre1 = positive @ mlp.weights[0]
            h = fnp.concatenate(
                [
                    fnp.maximum(pre1, 0.0),
                    fnp.maximum(-pre1, 0.0),
                ],
                axis=0,
            )
            for w in mlp.weights[1:]:
                h = fnp.maximum(h @ w, 0.0)
            final = fnp.mean(h, axis=0)
        else:
            signs = self._signs
            assert self._mub_output_cube is not None
            assert self._mub_output_flat is not None
            assert self._mub_stage_views is not None
            rotated_w0 = (q @ mlp.weights[0]).astype(fnp.float32)
            pre1 = _mub_preact(
                rotated_w0,
                signs,
                n,
                mean_radius,
                self._mub_output_cube,
                self._mub_output_flat,
                self._mub_stage_views,
            )
            if self._initial_cloud_buffer is None:
                negative = -pre1
            else:
                negative = self._initial_cloud_buffer[: pre1.shape[0], :]
                fnp.negative(pre1, out=negative)
            fnp.maximum(pre1, 0.0, out=pre1)
            fnp.maximum(negative, 0.0, out=negative)

            if len(mlp.weights) == 1:
                final = (
                    fnp.sum(pre1, axis=0, dtype=fnp.float64)
                    + fnp.sum(negative, axis=0, dtype=fnp.float64)
                ) / (2 * N_BASES * n)
            else:
                first_hidden_weight = mlp.weights[1]
                fnp.add(pre1, negative, out=pre1)
                remaining_weights = mlp.weights[2:]
                if remaining_weights:
                    self._ensure_workspaces_shape(
                        (2 * pre1.shape[0], n),
                        pre1.dtype,
                        n,
                    )
                    assert self._activation_buffer is not None
                    absolute_term = self._activation_buffer[
                        : pre1.shape[0],
                        :,
                    ]
                    self._absolute_depth2(
                        pre1,
                        first_hidden_weight,
                        absolute_term,
                    )
                else:
                    absolute_term = pre1 @ first_hidden_weight
                composed_weight = rotated_w0 @ first_hidden_weight
                linear_term = _mub_preact(
                    composed_weight,
                    signs,
                    n,
                    mean_radius,
                    self._mub_output_cube,
                    self._mub_output_flat,
                    self._mub_stage_views,
                )
                if self._initial_cloud_buffer is None:
                    positive = fnp.add(absolute_term, linear_term)
                    negative = fnp.subtract(absolute_term, linear_term)
                else:
                    cloud_rows = absolute_term.shape[0]
                    h = self._initial_cloud_buffer[: 2 * cloud_rows, :]
                    positive = h[:cloud_rows, :]
                    negative = h[cloud_rows:, :]
                    fnp.add(absolute_term, linear_term, out=positive)
                    fnp.subtract(absolute_term, linear_term, out=negative)
                fnp.multiply(positive, 0.5, out=positive)
                fnp.multiply(negative, 0.5, out=negative)
                fnp.maximum(positive, 0.0, out=positive)
                fnp.maximum(negative, 0.0, out=negative)
                if self._initial_cloud_buffer is None:
                    h = fnp.concatenate([positive, negative], axis=0)
                del pre1, absolute_term, linear_term, positive, negative

                if remaining_weights:
                    self._ensure_workspaces(h, n)

                full_coordinates = self._full_coordinates
                full_coordinate_mask = self._full_coordinate_mask
                assert full_coordinates is not None
                assert full_coordinate_mask is not None
                coordinate_mask = full_coordinate_mask
                source_buffer = h
                source_width = n
                destination_buffer = self._activation_buffer
                final_layer = len(mlp.weights)

                for layer, w in enumerate(remaining_weights, start=3):
                    current = source_buffer[:, :source_width]
                    current_coordinates = fnp.compress(
                        coordinate_mask,
                        full_coordinates,
                        axis=0,
                    )
                    _colmax = fnp.max(current, axis=0)
                    locally_active = _colmax > (
                        PRUNE_ALPHA * fnp.max(_colmax)
                    )

                    # Order the surviving columns by their sampled nonzero
                    # rate.  The permutation rides along inside the gather that
                    # replaces the original compress, so the ordering itself
                    # costs nothing beyond one count and one length-256 sort.
                    local_index = fnp.compress(
                        locally_active,
                        full_coordinates[:source_width],
                        axis=0,
                    )
                    width = local_index.shape[0]
                    sampled = fnp.count_nonzero(
                        current[:PREFIX_SAMPLE],
                        axis=0,
                    )
                    active_counts = fnp.take(sampled, local_index)
                    order = fnp.argsort(active_counts)
                    positions = fnp.take(local_index, order)
                    source = fnp.take(current, positions, axis=1)
                    active_coordinates = fnp.take(
                        current_coordinates,
                        positions,
                    )
                    active_weight = fnp.take(w, active_coordinates, axis=0)

                    if layer == final_layer:
                        output_weight = active_weight
                        output_width = n
                    elif layer >= PREPRUNE_START_LAYER:
                        coordinate_mask = _confirmed_keep_mask(
                            source,
                            active_weight,
                            full_coordinates,
                            n,
                            layer,
                            self._sentinel_rows[layer],
                            self._probe_masks[(layer, 0)],
                            self._probe_masks[(layer, 1)],
                        )
                        output_weight = fnp.compress(
                            coordinate_mask,
                            active_weight,
                            axis=1,
                        )
                        output_width = output_weight.shape[1]
                    else:
                        output_weight = active_weight
                        output_width = n
                        coordinate_mask = full_coordinate_mask

                    destination = destination_buffer[:, :output_width]
                    cuts = _segment_cuts(
                        fnp.cumsum(fnp.take(active_counts, order)),
                        width,
                        PREFIX_TAU * min(PREFIX_SAMPLE, source.shape[0]),
                    )
                    if not cuts:
                        self._multiply(source, output_weight, destination)
                    else:
                        # One contraction over the dense tail, for every row.
                        tail = cuts[-1]
                        self._multiply(
                            source[:, tail:],
                            output_weight[tail:, :],
                            destination,
                        )
                        # Then repair, segment by segment, only the rows that
                        # actually carry a nonzero there.  Post-ReLU values are
                        # non-negative, so a zero segment maximum proves every
                        # product over that segment is exactly zero.
                        bounds = [0] + cuts
                        for level in range(1, len(bounds)):
                            low = bounds[level - 1]
                            high = bounds[level]
                            segment = source[:, low:high]
                            if high - low > 1:
                                peak = fnp.max(segment, axis=1)
                            else:
                                peak = source[:, low]
                            hot = fnp.nonzero(peak)[0]
                            if not hot.shape[0]:
                                continue
                            gathered = fnp.take(segment, hot, axis=0)
                            partial = gathered @ output_weight[low:high, :]
                            accumulated = fnp.take(destination, hot, axis=0)
                            fnp.add(accumulated, partial, out=accumulated)
                            # put_along_axis is the one scatter fnp offers that
                            # mutates in place; applied one segment at a time it
                            # is an exact accumulating scatter.
                            fnp.put_along_axis(
                                destination,
                                hot[:, None],
                                accumulated,
                                axis=0,
                            )
                    fnp.maximum(destination, 0.0, out=destination)
                    source_buffer, destination_buffer = (
                        destination_buffer,
                        source_buffer,
                    )
                    source_width = output_width

                if remaining_weights:
                    self._activation_buffer = destination_buffer
                    self._initial_cloud_buffer = source_buffer
                    h = source_buffer[:, :source_width]
                final = fnp.sum(h, axis=0, dtype=fnp.float64) / (
                    2 * N_BASES * n
                )
        rows = [
            fnp.zeros(n, dtype=final.dtype)
            for _ in range(max(0, mlp.depth - 1))
        ]
        rows.append(final)
        return fnp.stack(rows, axis=0)
