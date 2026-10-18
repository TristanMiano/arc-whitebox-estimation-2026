"""T118 exact Strassen/Winograd contraction wrapper.

The depth-2 through depth-4 kernels are the unmodified MIT-licensed public
Phase-1 release copied into ``public_release/public_fast_reference.py``.  This
module supplies only stable workspace ownership and the frozen memory-bounded
depth-5 outer wrapper.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import flopscope.numpy as fnp


def _fill_plan(a, b, left_stack, right_stack):
    """Bind public-kernel views without doing arithmetic or reading data."""
    hm, hk, hn = a.shape[-2] // 2, a.shape[-1] // 2, b.shape[-1] // 2
    a11, a12 = a[..., :hm, :hk], a[..., :hm, hk:]
    a21, a22 = a[..., hm:, :hk], a[..., hm:, hk:]
    b11, b12 = b[..., :hk, :hn], b[..., :hk, hn:]
    b21, b22 = b[..., hk:, :hn], b[..., hk:, hn:]
    left, right = left_stack[..., :hm, :hk], right_stack[..., :hk, :hn]
    l = tuple(left[..., i, :, :] for i in range(7))
    r = tuple(right[..., i, :, :] for i in range(7))
    return [
        (fnp.concatenate, ((a22[..., None, :, :], a11[..., None, :, :], a12[..., None, :, :]),), {'axis': -3, 'out': left[..., :3, :, :]}),
        (fnp.concatenate, ((b11[..., None, :, :], b21[..., None, :, :], b22[..., None, :, :]),), {'axis': -3, 'out': right[..., 1:4, :, :]}),
        (fnp.add, (a21, a22), {'out': l[4]}),
        (fnp.subtract, (l[4], a11), {'out': l[5]}),
        (fnp.subtract, (a11, a21), {'out': l[6]}),
        (fnp.subtract, (a12, l[5]), {'out': l[3]}),
        (fnp.subtract, (b12, b11), {'out': r[4]}),
        (fnp.subtract, (b22, r[4]), {'out': r[5]}),
        (fnp.subtract, (b22, b12), {'out': r[6]}),
        (fnp.subtract, (r[5], b21), {'out': r[0]}),
    ]


def _combine_plan(leaves, result):
    hm, hn = result.shape[-2] // 2, result.shape[-1] // 2
    c11, c12 = result[..., :hm, :hn], result[..., :hm, hn:]
    c21, c22 = result[..., hm:, :hn], result[..., hm:, hn:]
    p = tuple(leaves[..., i, :, :] for i in range(7))
    return [(fnp.add, (p[1], p[2]), {'out': c11}),
            (fnp.add, (p[1], p[5]), {'out': c12}),
            (fnp.add, (c12, p[6]), {'out': c21}),
            (fnp.add, (c21, p[4]), {'out': c22}),
            (fnp.add, (c12, p[4]), {'out': c12}),
            (fnp.add, (c12, p[3]), {'out': c12}),
            (fnp.subtract, (c21, p[0]), {'out': c21})]


def _load_public_reference():
    path = Path(__file__).resolve().parent / "public_release" / "public_fast_reference.py"
    spec = importlib.util.spec_from_file_location("t118_public_fast_reference", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


public = _load_public_reference()


class FastMultiplier:
    """Own exact-kernel workspaces for one frozen recursion depth."""

    def __init__(self, maximum_rows: int, width: int, depth: int, dtype=fnp.float32):
        if depth not in (2, 3, 4, 5):
            raise ValueError(depth)
        divisor = 1 << depth
        if maximum_rows % divisor or width % divisor:
            raise ValueError((maximum_rows, width, depth))
        self.maximum_rows = maximum_rows
        self.width = width
        self.depth = depth
        self.dtype = dtype
        self.reference = public.Estimator()
        # The released allocator normally initializes these unrelated MUB
        # buffers first in ``setup``.  T118 uses only its matrix kernel, so
        # explicit zero-length sentinels keep the release's byte accounting
        # intact without allocating the unused Phase-1 transform.
        self.reference._mub_output_cube = fnp.empty((0,), dtype=dtype)
        self.reference._mub_scratch_cube = fnp.empty((0,), dtype=dtype)
        inner_rows = maximum_rows // 2 if depth == 5 else maximum_rows
        self.reference._ensure_workspaces_shape((inner_rows, width), dtype, width)
        if depth == 2:
            self.reference._cache_absolute_d2_workspaces(inner_rows, width, width)
        if depth == 5:
            half_rows = maximum_rows // 2
            half_width = width // 2
            self.outer_left = fnp.empty((7, half_rows, half_width), dtype=dtype)
            self.outer_right = fnp.empty((7, half_width, half_width), dtype=dtype)
            self.outer_products = fnp.empty((7, half_rows, half_width), dtype=dtype)
        else:
            self.outer_left = None
            self.outer_right = None
            self.outer_products = None
        self._prepared = {}

    def prepare_rows(self, rows):
        """Cache only workspace views; all numerical work stays in multiply."""
        if self.depth != 5 or self.width % 32 or rows % 32:
            raise ValueError((rows, self.width, self.depth))
        m, k, n = rows // 2, self.width // 2, self.width // 2
        r = self.reference
        left = self.outer_left[:, :m, :k]
        right = self.outer_right[:, :k, :n]
        products = self.outer_products[:, :m, :n]
        l1 = r._outer_left_workspace[0, :7, :m//2, :k//2]
        r1 = r._outer_right_workspace[0, :7, :k//2, :n//2]
        l2 = r._middle_left_workspace[:7, :, :m//4, :k//4]
        r2 = r._middle_right_workspace[:7, :, :k//4, :n//4]
        l3 = r._leaf_left_workspace[:7, :, :, :m//8, :k//8]
        r3 = r._leaf_right_workspace[:7, :, :, :, :k//8, :n//8]
        l4 = r._d4_leaf_left_workspace[:7, :, :, :, :m//16, :k//16]
        r4 = r._d4_leaf_right_workspace[:7, :, :, :, :, :k//16, :n//16]
        p4 = r._d4_leaf_product_workspace[:7, :, :, :, :m//16, :n//16]
        p3 = r._leaf_product_workspace[:7, :, :, :m//8, :n//8]
        p2 = r._middle_product_workspace[:7, :, :m//4, :n//4]
        p1 = r._outer_product_workspace[:7, :m//2, :n//2]
        inner = (_fill_plan(l1, r1, l2, r2)
                 + _fill_plan(l2, r2, l3, r3[:, :, :, 0])
                 + _fill_plan(l3, r3[:, :, :, 0], l4, r4[:, :, :, :, 0])
                 + [(public._mm, (l4, r4), {'out': p4})]
                 + _combine_plan(p4, p3) + _combine_plan(p3, p2) + _combine_plan(p2, p1))
        steps = []
        for group in range(7):
            steps.extend(_fill_plan(left[group], right[group], l1, r1))
            steps.extend(inner)
            steps.extend(_combine_plan(p1, products[group]))
        self._prepared[rows] = (left, right, products, tuple(steps))

    @property
    def workspace_bytes(self) -> int:
        total = int(self.reference._workspace_allocated_bytes)
        for value in (self.outer_left, self.outer_right, self.outer_products):
            if value is not None:
                total += int(value.nbytes)
        return total

    def _depth4(self, a, b, result):
        r = self.reference
        return public._strassen_four_level_core(
            a,
            b,
            result,
            r._outer_left_workspace,
            r._outer_right_workspace,
            r._middle_left_workspace,
            r._middle_right_workspace,
            r._leaf_left_workspace,
            r._leaf_right_workspace,
            r._leaf_product_workspace,
            r._middle_product_workspace,
            r._outer_product_workspace,
            r._d4_leaf_left_workspace,
            r._d4_leaf_right_workspace,
            r._d4_leaf_product_workspace,
        )

    def multiply(self, a, b, out=None):
        rows, inner = a.shape
        if inner != self.width or b.shape != (self.width, self.width):
            raise ValueError((a.shape, b.shape))
        if rows > self.maximum_rows or rows % (1 << self.depth):
            raise ValueError((rows, self.maximum_rows, self.depth))
        result = out if out is not None else fnp.empty((rows, self.width), dtype=a.dtype)
        r = self.reference
        if self.depth == 2:
            work = r._absolute_d2_workspaces
            if work is None:
                raise RuntimeError("depth-2 workspace missing")
            return public._strassen_two_level_core(
                a,
                b,
                result,
                work[2],
                work[3],
                work[4],
                work[5],
                work[6],
                work[7],
            )
        if self.depth == 3:
            return public._strassen_three_level_core(
                a,
                b,
                result,
                r._outer_left_workspace,
                r._outer_right_workspace,
                r._middle_left_workspace,
                r._middle_right_workspace,
                r._leaf_left_workspace,
                r._leaf_right_workspace,
                r._leaf_product_workspace,
                r._middle_product_workspace,
                r._outer_product_workspace,
            )
        if self.depth == 4:
            return self._depth4(a, b, result)

        if rows in self._prepared:
            left, right, products, steps = self._prepared[rows]
            public._fill_batched_operands_d3(a, b, left, right)
            for operation, args, kwargs in steps:
                operation(*args, **kwargs)
            public._combine_seven_products_d3(products, result)
            return result

        half_rows = rows // 2
        half_width = self.width // 2
        left = self.outer_left[:, :half_rows, :half_width]
        right = self.outer_right[:, :half_width, :half_width]
        products = self.outer_products[:, :half_rows, :half_width]
        public._fill_batched_operands_d3(a, b, left, right)
        for group in range(7):
            self._depth4(left[group], right[group], products[group])
        public._combine_seven_products_d3(products, result)
        return result
