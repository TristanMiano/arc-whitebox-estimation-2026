"""Frozen T118 DF0/DF1/DFFH and AS-composition family."""

from __future__ import annotations

import math

import flopscope.numpy as fnp
from whestbench import BaseEstimator, MLP, SetupContext

import base_family
import response_family
from fast_kernel import FastMultiplier


WIDTH = 1024
DEPTH = 16
MAIN_ROWS = 2048
RADIUS = 31.992188454829048
CHILD_XOR = 0xD118C411
EPS64 = 1e-30
CAP_FRACTION = 0.25
FRAME_SHARE = 0.260 / 0.285
PAIR = (5, 1536)


def _standardized(moment):
    safe = fnp.maximum(moment[1], EPS64)
    return moment[2] / (safe * fnp.sqrt(safe))


def _combine_moments(left, right, left_rows, right_rows):
    total = float(left_rows + right_rows)
    wl = float(left_rows) / total
    wr = float(right_rows) / total
    mean = wl * left[0] + wr * right[0]
    dl = left[0] - mean
    dr = right[0] - mean
    second = wl * (left[1] + dl * dl) + wr * (right[1] + dr * dr)
    third = wl * (left[2] + 3.0 * dl * left[1] + dl * dl * dl)
    third = third + wr * (right[2] + 3.0 * dr * right[1] + dr * dr * dr)
    return mean, second, third


class Family(response_family._LPITFFamily):
    """Compute all frozen candidates once from shared physical components."""

    def __init__(
        self,
        depth: int = PAIR[0],
        child_rows: int = PAIR[1],
        use_fast: bool = True,
    ):
        self.fast_depth = int(depth)
        self.child_rows = int(child_rows)
        self.use_fast = bool(use_fast)
        self.multiplier = None
        self.buffer_a = None
        self.buffer_b = None

    def setup(self, context: SetupContext) -> None:
        if context.width != WIDTH or context.depth != DEPTH:
            return
        if not self.use_fast:
            return
        maximum_rows = 2 * max(MAIN_ROWS, self.child_rows)
        self.multiplier = FastMultiplier(maximum_rows, WIDTH, self.fast_depth)
        self.buffer_a = fnp.empty((maximum_rows, WIDTH), dtype=fnp.float32)
        self.buffer_b = fnp.empty((maximum_rows, WIDTH), dtype=fnp.float32)

    @property
    def setup_workspace_bytes(self):
        if self.multiplier is None:
            return 0
        return (
            self.multiplier.workspace_bytes
            + int(self.buffer_a.nbytes)
            + int(self.buffer_b.nbytes)
        )

    @classmethod
    def _child_positive(cls, mlp, rows):
        rng = fnp.random.default_rng(int(mlp.seed) ^ CHILD_XOR)
        if rows >= WIDTH:
            gaussian = rng.standard_normal((rows, WIDTH), dtype=fnp.float32)
            q, ignored_r = fnp.linalg.qr(gaussian, mode="reduced")
            leverage = fnp.sum(q * q, axis=1)
            positive = q * (RADIUS / fnp.sqrt(leverage))[:, None]
            del gaussian, ignored_r, leverage
            return positive
        gaussian = rng.standard_normal((rows, WIDTH), dtype=fnp.float32)
        q, ignored_r = fnp.linalg.qr(gaussian.T, mode="reduced")
        positive = q.T * RADIUS
        del gaussian, q, ignored_r
        return positive

    @staticmethod
    def _moments(block):
        mean = fnp.mean(block, axis=0, dtype=fnp.float64)
        centered = fnp.asarray(block, dtype=fnp.float64) - mean
        squared = centered * centered
        return (
            mean,
            fnp.mean(squared, axis=0, dtype=fnp.float64),
            fnp.mean(squared * centered, axis=0, dtype=fnp.float64),
        )

    def _fast_propagate(self, positive, weights, main=False):
        if self.multiplier is None or self.buffer_a is None or self.buffer_b is None:
            raise RuntimeError("Family.setup must be called before prediction")
        rows = positive.shape[0]
        count = 2 * rows
        active = self.buffer_a[:count]
        preactivation = self.buffer_b[:count]
        fnp.copyto(active[:rows], positive)
        fnp.negative(positive, out=active[rows:])
        outputs = []
        source_moment = None
        half_a = None
        half_b = None
        for layer, weight in enumerate(weights):
            self.multiplier.multiply(active, weight, out=preactivation)
            if layer == len(weights) - 1:
                source_moment = self._moments(preactivation)
                if main:
                    a_positive = self._moments(preactivation[:1024])
                    b_positive = self._moments(preactivation[1024:2048])
                    a_negative = self._moments(preactivation[2048:3072])
                    b_negative = self._moments(preactivation[3072:4096])
                    half_a = _combine_moments(a_positive, a_negative, 1024, 1024)
                    half_b = _combine_moments(b_positive, b_negative, 1024, 1024)
            fnp.maximum(preactivation, 0.0, out=active)
            outputs.append(
                fnp.mean(
                    (active[:rows] + active[rows:]) * 0.5,
                    axis=0,
                    dtype=fnp.float32,
                )
            )
        exact_first = self._exact_first(weights[0])
        if source_moment is None:
            raise RuntimeError("empty propagation")
        return (
            fnp.stack([exact_first] + outputs[1:], axis=0),
            source_moment,
            half_a,
            half_b,
        )

    def _dense_propagate(self, positive, weights, main=False):
        prediction, final_pre = response_family._LPITFFamily._propagate_positive(
            positive, weights
        )
        source_moment = self._moments(final_pre)
        half_a = None
        half_b = None
        if main:
            a_positive = self._moments(final_pre[:1024])
            b_positive = self._moments(final_pre[1024:2048])
            a_negative = self._moments(final_pre[2048:3072])
            b_negative = self._moments(final_pre[3072:4096])
            half_a = _combine_moments(a_positive, a_negative, 1024, 1024)
            half_b = _combine_moments(b_positive, b_negative, 1024, 1024)
        return prediction, source_moment, half_a, half_b

    def _propagate_frame(self, positive, weights, main=False):
        if self.use_fast:
            return self._fast_propagate(positive, weights, main=main)
        return self._dense_propagate(positive, weights, main=main)

    @staticmethod
    def _harmonic_statistics(full_moment, source_a, source_b, noise_factor, alpha, sigma, pdf):
        full_skew = _standardized(full_moment)
        skew_a = _standardized(source_a)
        skew_b = _standardized(source_b)
        alpha64 = fnp.asarray(alpha, dtype=fnp.float64)
        sigma64 = fnp.asarray(sigma, dtype=fnp.float64)
        pdf64 = fnp.asarray(pdf, dtype=fnp.float64)
        influence = sigma64 * alpha64 * pdf64 / 6.0
        influence_sq = influence * influence
        total = fnp.sum(influence_sq)
        beta = fnp.sum(influence_sq * alpha64 * full_skew) / fnp.maximum(
            fnp.sum(influence_sq * alpha64 * alpha64), EPS64
        )
        residual = full_skew - beta * alpha64
        noise = float(noise_factor) * fnp.sum(
            influence_sq * (skew_a - skew_b) * (skew_a - skew_b)
        ) / fnp.maximum(total, EPS64)
        observed = fnp.sum(influence_sq * residual * residual) / fnp.maximum(total, EPS64)
        rho_raw = 1.0 - noise / fnp.maximum(observed, EPS64)
        rho = fnp.where(
            observed <= EPS64,
            fnp.zeros(observed.shape, dtype=fnp.float64),
            fnp.minimum(fnp.maximum(rho_raw, 0.0), 1.0),
        )
        harmonic = fnp.minimum(fnp.maximum(beta * alpha64 + rho * residual, -1.0), 1.0)
        return {
            "full_skew": full_skew,
            "source_a_skew": skew_a,
            "source_b_skew": skew_b,
            "harmonic_skew": harmonic,
            "beta": beta,
            "rho": rho,
            "noise": noise,
            "observed": observed,
            "alpha64": alpha64,
            "sigma64": sigma64,
            "pdf64": pdf64,
        }

    @staticmethod
    def _with_delta(closure, statistics):
        delta = (
            -statistics["sigma64"]
            * statistics["harmonic_skew"]
            * statistics["alpha64"]
            * statistics["pdf64"]
            / 6.0
        )
        corrected = fnp.asarray(
            fnp.asarray(closure[-1], dtype=fnp.float64) + delta,
            dtype=fnp.float32,
        )
        return fnp.concatenate((closure[:-1], corrected[None, :]), axis=0), delta

    @staticmethod
    def _frame_direction(main, child, support, closure_weight):
        early = base_family._EARLY_FRAME_WEIGHT * (child - support)
        final = (
            (1.0 - fnp.asarray(closure_weight, dtype=fnp.float64))
            * FRAME_SHARE
            * fnp.asarray(child[-1] - support[-1], dtype=fnp.float64)
        )
        return fnp.asarray(
            fnp.concatenate(
                (
                    fnp.zeros((1, WIDTH), dtype=fnp.float64),
                    fnp.asarray(early[1:-1], dtype=fnp.float64),
                    final[None, :],
                ),
                axis=0,
            ),
            dtype=fnp.float64,
        )

    @staticmethod
    def _sf_feature(source_a, source_b, corrected_closure, dffh_support, closure_weight, statistics, m0, m1):
        alpha = statistics["alpha64"]
        sigma = statistics["sigma64"]
        pdf = statistics["pdf64"]
        actions = fnp.stack(
            (
                -sigma * alpha * pdf / 6.0,
                sigma * (alpha * alpha - 1.0) * pdf / 24.0,
                -sigma * (alpha * alpha * alpha - 3.0 * alpha) * pdf / 120.0,
            ),
            axis=1,
        )
        rms = fnp.sqrt(fnp.mean(actions * actions, axis=0))
        q, ignored_r = fnp.linalg.qr(actions / fnp.maximum(rms, EPS64), mode="reduced")
        del ignored_r
        reference = fnp.asarray(corrected_closure[-1], dtype=fnp.float64)
        beta_a = q.T @ (fnp.asarray(source_a[-1], dtype=fnp.float64) - reference)
        beta_b = q.T @ (fnp.asarray(source_b[-1], dtype=fnp.float64) - reference)
        total = float(m0 + m1)
        pooled = (float(m0) * beta_a + float(m1) * beta_b) / total
        signal = fnp.maximum(beta_a * beta_b, 0.0)
        omega = float(m0 * m1) / float((m0 + m1) ** 2)
        noise = omega * (beta_a - beta_b) * (beta_a - beta_b)
        reliability = signal / fnp.maximum(signal + noise, EPS64)
        correction = q @ (reliability * pooled)
        candidate = fnp.maximum(
            fnp.asarray(dffh_support[-1], dtype=fnp.float64)
            + fnp.asarray(closure_weight, dtype=fnp.float64) * correction,
            0.0,
        )
        return candidate - fnp.asarray(dffh_support[-1], dtype=fnp.float64), reliability

    def primitive_bundle(self, mlp):
        weights = [fnp.asarray(weight, dtype=fnp.float32) for weight in mlp.weights]
        rng = fnp.random.default_rng(mlp.seed)
        gaussian = rng.standard_normal((MAIN_ROWS, WIDTH), dtype=fnp.float32)
        q, ignored_r = fnp.linalg.qr(gaussian, mode="reduced")
        leverage = fnp.sum(q * q, axis=1)
        main_positive = q * (RADIUS / fnp.sqrt(leverage))[:, None]
        del gaussian, q, ignored_r, leverage
        main, main_moment, main_half_a, main_half_b = self._propagate_frame(
            main_positive, weights, main=True
        )
        del main_positive

        child_positive = self._child_positive(mlp, self.child_rows)
        child, child_moment, ignored_a, ignored_b = self._propagate_frame(
            child_positive, weights, main=False
        )
        del child_positive, ignored_a, ignored_b

        partial_positive, ignored_base = self._partial_positive(mlp)
        partial, ignored_pre = response_family._LPITFFamily._propagate_positive(
            partial_positive, weights
        )
        del partial_positive, ignored_base, ignored_pre
        closure, alpha, sigma, pdf, cdf_path = self._closure_predict_with_transport(mlp)

        main_statistics = self._harmonic_statistics(
            main_moment, main_half_a, main_half_b, 0.25, alpha, sigma, pdf
        )
        pooled_moment = _combine_moments(
            main_moment, child_moment, MAIN_ROWS, self.child_rows
        )
        omega = float(MAIN_ROWS * self.child_rows) / float((MAIN_ROWS + self.child_rows) ** 2)
        dffh_statistics = self._harmonic_statistics(
            pooled_moment, main_moment, child_moment, omega, alpha, sigma, pdf
        )
        main_corrected, main_delta = self._with_delta(closure, main_statistics)
        dffh_corrected, dffh_delta = self._with_delta(closure, dffh_statistics)

        total = float(MAIN_ROWS + self.child_rows)
        support = (float(MAIN_ROWS) * main + float(self.child_rows) * child) / total
        closure_weight = self._final_closure_weight("V000", alpha)
        exact_first = self._exact_first(weights[0])
        df1_support = self._blend(support, partial, main_corrected, closure_weight, exact_first)
        dffh_support = self._blend(support, partial, dffh_corrected, closure_weight, exact_first)
        deterministic_support = self._blend(
            support, partial, closure, closure_weight, exact_first
        )
        direction = self._frame_direction(main, child, support, closure_weight)
        sf_feature, sf_reliability = self._sf_feature(
            main,
            child,
            dffh_corrected,
            dffh_support,
            closure_weight,
            dffh_statistics,
            MAIN_ROWS,
            self.child_rows,
        )
        radii = fnp.sqrt(fnp.sum(fnp.asarray(weights[-1], dtype=fnp.float64) ** 2, axis=0))
        return {
            "main": main,
            "child": child,
            "support": support,
            "partial": partial,
            "closure": closure,
            "main_corrected": main_corrected,
            "dffh_corrected": dffh_corrected,
            "df1_support": df1_support,
            "dffh_support": dffh_support,
            "deterministic_support": deterministic_support,
            "frame_direction": direction,
            "closure_weight": closure_weight,
            "alpha": alpha,
            "radii": radii,
            "sf_feature": sf_feature,
            "sf_reliability": sf_reliability,
            "main_delta": main_delta,
            "dffh_delta": dffh_delta,
            "main_rho": main_statistics["rho"],
            "dffh_rho": dffh_statistics["rho"],
            "cdf_path": cdf_path,
        }

    @staticmethod
    def as_bundle(primitive, gamma):
        scalar_frame = fnp.asarray(primitive["support"], dtype=fnp.float64) + float(gamma) * fnp.asarray(
            primitive["child"] - primitive["support"], dtype=fnp.float64
        )
        incumbent = fnp.asarray(primitive["dffh_support"], dtype=fnp.float64) + float(gamma) * fnp.asarray(
            primitive["frame_direction"], dtype=fnp.float64
        )
        deterministic = fnp.asarray(
            primitive["deterministic_support"], dtype=fnp.float64
        ) + float(gamma) * fnp.asarray(primitive["frame_direction"], dtype=fnp.float64)
        corrected = fnp.asarray(primitive["dffh_corrected"][-1], dtype=fnp.float64)
        x1 = scalar_frame[-1] - corrected
        x2 = fnp.asarray(primitive["partial"][-1], dtype=fnp.float64) - corrected
        x3 = incumbent[-1] - deterministic[-1]
        m1 = fnp.mean(x1)
        m2 = fnp.mean(x2)
        m3 = fnp.mean(x3)
        ones = fnp.ones((WIDTH,), dtype=fnp.float64)
        columns = [x1, x2, x3, ones * m1, ones * m2, ones * m3, primitive["sf_feature"]]
        absolute = fnp.abs(fnp.asarray(primitive["alpha"], dtype=fnp.float64))
        middle = (absolute > 1.0) & (absolute <= 3.0)
        tail = absolute > 3.0
        centered = x3 - m3
        for mask in (middle, tail):
            masked = fnp.asarray(mask, dtype=fnp.float64) * centered
            columns.append(masked - fnp.mean(masked))
        for mask in (middle, tail):
            mask64 = fnp.asarray(mask, dtype=fnp.float64)
            columns.append(m3 * (mask64 - fnp.mean(mask64)))
        radii = fnp.asarray(primitive["radii"], dtype=fnp.float64)
        columns.append(m3 * (radii / fnp.maximum(fnp.mean(radii), EPS64) - 1.0))
        physical = fnp.stack((x1, x2, x3), axis=1)
        return {
            "incumbent": incumbent,
            "deterministic": deterministic,
            "features": fnp.stack(columns, axis=1),
            "cap_scale": fnp.sqrt(fnp.mean(physical * physical)),
        }

    @classmethod
    def candidate_prediction(cls, primitive, gamma, coefficients=None):
        bundle = cls.as_bundle(primitive, gamma)
        if coefficients is None:
            final = fnp.maximum(bundle["incumbent"][-1], 0.0)
        else:
            theta = fnp.asarray(coefficients, dtype=fnp.float64)
            raw = bundle["features"] @ theta
            limit = CAP_FRACTION * bundle["cap_scale"]
            correction = fnp.minimum(fnp.maximum(raw, -limit), limit)
            final = fnp.maximum(bundle["incumbent"][-1] + correction, 0.0)
        return fnp.maximum(
            fnp.concatenate(
                (
                    fnp.asarray(bundle["incumbent"][:-1], dtype=fnp.float32),
                    fnp.asarray(final, dtype=fnp.float32)[None, :],
                ),
                axis=0,
            ),
            0.0,
        )


class Estimator(BaseEstimator):
    """Template estimator; sealing replaces coefficients after Full F fit."""

    gamma = 0.0
    coefficients = None

    def __init__(self):
        self.family = Family()

    def setup(self, context: SetupContext) -> None:
        self.family.setup(context)

    def predict(self, mlp: MLP, budget: int):
        if mlp.width != WIDTH or mlp.depth != DEPTH or budget < 220_000_000_000:
            return fnp.maximum(self.family._fallback(mlp, budget), 0.0)
        primitive = self.family.primitive_bundle(mlp)
        return self.family.candidate_prediction(primitive, self.gamma, self.coefficients)
