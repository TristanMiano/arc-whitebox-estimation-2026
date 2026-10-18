"""Frozen T117 H116-A target-blind observer feature family.

The numerical parent is the immutable T108 ALG019-V000 implementation reached
through T114's response-state graph.  This module implements only the prospectively
frozen BO -> GL -> SF -> AS -> DS -> M feature ladder from T116.  It never
loads an audit or released target.
"""

from __future__ import annotations

import math

import flopscope as flops
import flopscope.numpy as fnp
import response_family as parent



WIDTH = 1024
DEPTH = 16
XI = 1.000488400401617
EPS64 = 1e-30
CAP_FRACTION = 0.25
RIDGE_GRID = (1e-4, 1e-3, 1e-2)
RUNG_ORDER = ("BO", "GL", "SF", "AS", "DS", "M")
RUNG_FEATURE_COUNT = {"BO": 1, "GL": 6, "SF": 7, "AS": 12, "DS": 20, "M": 26}
FEATURE_NAMES = (
    "x1_frame_minus_corrected_closure",
    "x2_partial_minus_corrected_closure",
    "x3_incumbent_minus_deterministic",
    "m1_frame_gap_mean",
    "m2_partial_gap_mean",
    "m3_skew_increment_mean",
    "sf_three_action_complete_correction",
    "local_mid_alpha_contrast",
    "local_tail_alpha_contrast",
    "global_mid_alpha_contrast",
    "global_tail_alpha_contrast",
    "final_weight_norm_contrast",
    "frame_depth_dct0",
    "frame_depth_dct1",
    "frame_depth_dct2",
    "frame_depth_dct3",
    "partial_depth_dct0",
    "partial_depth_dct1",
    "partial_depth_dct2",
    "partial_depth_dct3",
    "transported_frame_linear",
    "transported_partial_linear",
    "transported_frame_quadratic",
    "transported_partial_quadratic",
    "thmb_frame",
    "thmb_partial",
)


def _repeat(scalar):
    # ``fnp.full`` currently trips a FlopScope internal copyto defect when its
    # fill value is itself a tracked scalar.  This spelling is mathematically
    # identical, visible to accounting, and works in the pinned runtime.
    return fnp.ones((WIDTH,), dtype=fnp.float64) * scalar


def _physical_components(mlp):
    """Return the parent state without recomputing any stochastic source."""
    family = parent._LPITFFamily
    weights = [fnp.asarray(weight, dtype=fnp.float32) for weight in mlp.weights]
    frame, frame_final_pre = family._frame_predict_with_final_pre(mlp)
    partial_positive, ignored_base = family._partial_positive(mlp)
    partial, partial_final_pre = family._propagate_positive(partial_positive, weights)
    del partial_positive, ignored_base
    closure, alpha, sigma, pdf, cdf_path = family._closure_predict_with_transport(mlp)
    components = {
        "frame": frame,
        "partial": partial,
        "closure": closure,
        "alpha": alpha,
        "sigma": sigma,
        "pdf": pdf,
        "cdf_path": cdf_path,
        "final_preactivation": frame_final_pre,
        "partial_final_preactivation": partial_final_pre,
        "weights": mlp.weights,
    }
    incumbent, closure_weight, statistics = family._base_and_weight(
        components, "retained", True
    )
    deterministic, _, _ = family._base_and_weight(components, "retained", False)
    return incumbent, deterministic, components, closure_weight, statistics


def _split_frame_feature(incumbent, components, closure_weight, statistics):
    z = fnp.asarray(components["final_preactivation"], dtype=fnp.float64)
    rows = z.shape[0] // 2
    pair = 0.5 * (fnp.maximum(z[:rows], 0.0) + fnp.maximum(z[rows:], 0.0))
    half = rows // 2
    frame_a = fnp.mean(pair[:half], axis=0, dtype=fnp.float64)
    frame_b = fnp.mean(pair[half:], axis=0, dtype=fnp.float64)

    alpha = fnp.asarray(components["alpha"], dtype=fnp.float64)
    sigma = fnp.asarray(components["sigma"], dtype=fnp.float64)
    pdf = fnp.asarray(components["pdf"], dtype=fnp.float64)
    actions = fnp.stack(
        (
            -sigma * alpha * pdf / 6.0,
            sigma * (alpha * alpha - 1.0) * pdf / 24.0,
            -sigma * (alpha * alpha * alpha - 3.0 * alpha) * pdf / 120.0,
        ),
        axis=1,
    )
    action_rms = fnp.sqrt(fnp.mean(actions * actions, axis=0))
    q, ignored_r = fnp.linalg.qr(actions / fnp.maximum(action_rms, EPS64), mode="reduced")
    del ignored_r
    delta = (
        -statistics["sigma64"]
        * statistics["harmonic_skew"]
        * statistics["alpha64"]
        * statistics["pdf64"]
        / 6.0
    )
    corrected_closure = fnp.asarray(components["closure"][-1], dtype=fnp.float64) + delta
    beta_a = q.T @ (frame_a - corrected_closure)
    beta_b = q.T @ (frame_b - corrected_closure)
    signal = fnp.maximum(beta_a * beta_b, 0.0)
    noise = 0.25 * (beta_a - beta_b) * (beta_a - beta_b)
    reliability = signal / fnp.maximum(signal + noise, EPS64)
    correction = q @ (reliability * 0.5 * (beta_a + beta_b))
    candidate = fnp.maximum(
        fnp.asarray(incumbent[-1], dtype=fnp.float64)
        + fnp.asarray(closure_weight, dtype=fnp.float64) * correction,
        0.0,
    )
    return candidate - fnp.asarray(incumbent[-1], dtype=fnp.float64), reliability


def _depth_features(components):
    frame = fnp.asarray(components["frame"], dtype=fnp.float64)
    partial = fnp.asarray(components["partial"], dtype=fnp.float64)
    closure = fnp.asarray(components["closure"], dtype=fnp.float64)
    final_scale = fnp.sqrt(fnp.mean(closure[-1] * closure[-1]))
    frame_gaps = []
    partial_gaps = []
    minimum_scale = None
    for layer in range(1, DEPTH - 1):
        scale = fnp.sqrt(fnp.mean(closure[layer] * closure[layer]))
        minimum_scale = scale if minimum_scale is None else fnp.minimum(minimum_scale, scale)
        safe = fnp.maximum(scale, 1e-12)
        frame_gaps.append(final_scale * fnp.mean(frame[layer] - closure[layer]) / safe)
        partial_gaps.append(final_scale * fnp.mean(partial[layer] - closure[layer]) / safe)
    q_rows = []
    count = DEPTH - 2
    for degree in range(4):
        if degree == 0:
            q_rows.append([1.0 / math.sqrt(count)] * count)
        else:
            q_rows.append(
                [
                    math.sqrt(2.0 / count)
                    * math.cos(math.pi * degree * ((index + 1) - 0.5) / count)
                    for index in range(count)
                ]
            )
    q = fnp.asarray(q_rows, dtype=fnp.float64)
    z_frame = q @ fnp.stack(frame_gaps)
    z_partial = q @ fnp.stack(partial_gaps)
    repeated = [_repeat(z_frame[index]) for index in range(4)]
    repeated.extend(_repeat(z_partial[index]) for index in range(4))
    return repeated, minimum_scale


def _m_features(components):
    frame = fnp.asarray(components["frame"], dtype=fnp.float64)
    partial = fnp.asarray(components["partial"], dtype=fnp.float64)
    closure = fnp.asarray(components["closure"], dtype=fnp.float64)
    final_weight = fnp.asarray(components["weights"][-1], dtype=fnp.float64)
    alpha = fnp.asarray(components["alpha"], dtype=fnp.float64)
    sigma = fnp.maximum(fnp.asarray(components["sigma"], dtype=fnp.float64), EPS64)
    pdf = fnp.asarray(components["pdf"], dtype=fnp.float64)
    cdf = fnp.asarray(components["cdf_path"][-1], dtype=fnp.float64)
    r_frame = frame[-2] - closure[-2]
    r_partial = partial[-2] - closure[-2]
    u_frame = r_frame @ final_weight
    u_partial = r_partial @ final_weight
    transported = [
        cdf * u_frame,
        cdf * u_partial,
        pdf * u_frame * u_frame / (2.0 * sigma),
        pdf * u_partial * u_partial / (2.0 * sigma),
    ]

    mean_pre = alpha * sigma
    frame_pre = fnp.asarray(components["final_preactivation"], dtype=fnp.float64)
    partial_pre = fnp.asarray(
        components["partial_final_preactivation"], dtype=fnp.float64
    )

    def bridge(preactivation):
        moment1 = fnp.mean(preactivation, axis=0, dtype=fnp.float64)
        moment2 = XI * fnp.mean(
            preactivation * preactivation, axis=0, dtype=fnp.float64
        )
        return (
            cdf * (moment1 - mean_pre)
            + pdf
            / (2.0 * sigma)
            * (moment2 - 2.0 * mean_pre * moment1 + mean_pre * mean_pre - sigma * sigma)
        )

    return transported + [bridge(frame_pre), bridge(partial_pre)]


def feature_bundle(mlp, maximum_rung: str = "M"):
    """Return final parent states and the frozen feature prefix.

    ``maximum_rung`` only suppresses unnecessary post-parent feature work; it
    never changes a retained earlier column.
    """
    if maximum_rung not in RUNG_ORDER:
        raise ValueError(maximum_rung)
    incumbent, deterministic, components, closure_weight, statistics = _physical_components(mlp)
    frame = fnp.asarray(components["frame"][-1], dtype=fnp.float64)
    partial = fnp.asarray(components["partial"][-1], dtype=fnp.float64)
    delta = (
        -statistics["sigma64"]
        * statistics["harmonic_skew"]
        * statistics["alpha64"]
        * statistics["pdf64"]
        / 6.0
    )
    corrected_closure = fnp.asarray(components["closure"][-1], dtype=fnp.float64) + delta
    incumbent_final = fnp.asarray(incumbent[-1], dtype=fnp.float64)
    deterministic_final = fnp.asarray(deterministic[-1], dtype=fnp.float64)
    x1 = frame - corrected_closure
    x2 = partial - corrected_closure
    x3 = incumbent_final - deterministic_final
    m1 = fnp.mean(x1)
    m2 = fnp.mean(x2)
    m3 = fnp.mean(x3)
    physical = fnp.stack((x1, x2, x3), axis=1)
    cap_scale = fnp.sqrt(fnp.mean(physical * physical))

    if maximum_rung == "BO":
        return {
            "incumbent": incumbent,
            "deterministic": deterministic,
            "features": _repeat(m3)[:, None],
            "cap_scale": cap_scale,
            "alpha": components["alpha"],
            "sf_reliability": fnp.zeros((3,), dtype=fnp.float64),
            "minimum_depth_scale": fnp.asarray(math.nan, dtype=fnp.float64),
        }

    columns = [
        x1,
        x2,
        x3,
        _repeat(m1),
        _repeat(m2),
        _repeat(m3),
    ]
    if maximum_rung == "GL":
        return _bundle(incumbent, deterministic, columns, cap_scale, components, None, None)

    sf_feature, sf_reliability = _split_frame_feature(
        incumbent, components, closure_weight, statistics
    )
    columns.append(sf_feature)
    if maximum_rung == "SF":
        return _bundle(
            incumbent, deterministic, columns, cap_scale, components, sf_reliability, None
        )

    absolute_alpha = fnp.abs(fnp.asarray(components["alpha"], dtype=fnp.float64))
    middle = (absolute_alpha > 1.0) & (absolute_alpha <= 3.0)
    tail = absolute_alpha > 3.0
    centered_x3 = x3 - m3
    for mask in (middle, tail):
        masked = fnp.asarray(mask, dtype=fnp.float64) * centered_x3
        columns.append(masked - fnp.mean(masked))
    for mask in (middle, tail):
        mask64 = fnp.asarray(mask, dtype=fnp.float64)
        columns.append(m3 * (mask64 - fnp.mean(mask64)))
    final_weight = fnp.asarray(components["weights"][-1], dtype=fnp.float64)
    radii = fnp.sqrt(fnp.sum(final_weight * final_weight, axis=0))
    columns.append(m3 * (radii / fnp.maximum(fnp.mean(radii), EPS64) - 1.0))
    if maximum_rung == "AS":
        return _bundle(
            incumbent, deterministic, columns, cap_scale, components, sf_reliability, None
        )

    depth_columns, minimum_depth_scale = _depth_features(components)
    columns.extend(depth_columns)
    if maximum_rung == "DS":
        return _bundle(
            incumbent,
            deterministic,
            columns,
            cap_scale,
            components,
            sf_reliability,
            minimum_depth_scale,
        )

    columns.extend(_m_features(components))
    return _bundle(
        incumbent,
        deterministic,
        columns,
        cap_scale,
        components,
        sf_reliability,
        minimum_depth_scale,
    )


def _bundle(
    incumbent,
    deterministic,
    columns,
    cap_scale,
    components,
    sf_reliability,
    minimum_depth_scale,
):
    return {
        "incumbent": incumbent,
        "deterministic": deterministic,
        "features": fnp.stack(columns, axis=1),
        "cap_scale": cap_scale,
        "alpha": components["alpha"],
        "sf_reliability": (
            sf_reliability
            if sf_reliability is not None
            else fnp.zeros((3,), dtype=fnp.float64)
        ),
        "minimum_depth_scale": (
            minimum_depth_scale
            if minimum_depth_scale is not None
            else fnp.asarray(math.nan, dtype=fnp.float64)
        ),
    }


def apply_observer(bundle, rung: str, coefficients):
    """Apply one F-fitted rung with the frozen cap and nonnegative clamp."""
    if rung not in RUNG_ORDER:
        raise ValueError(rung)
    features = fnp.asarray(bundle["features"], dtype=fnp.float64)
    theta = fnp.asarray(coefficients, dtype=fnp.float64)
    if features.shape[1] != theta.shape[0]:
        raise ValueError((features.shape, theta.shape))
    if rung == "BO":
        base = fnp.asarray(bundle["deterministic"][-1], dtype=fnp.float64)
    else:
        base = fnp.asarray(bundle["incumbent"][-1], dtype=fnp.float64)
    correction = features @ theta
    limit = CAP_FRACTION * fnp.asarray(bundle["cap_scale"], dtype=fnp.float64)
    correction = fnp.minimum(fnp.maximum(correction, -limit), limit)
    return fnp.maximum(base + correction, 0.0)
