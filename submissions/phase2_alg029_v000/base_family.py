"""Frozen FC007 T108 family: H107-O/I/N/J/F as ALG019-V000..V004.

This module contains one shared implementation so the five variants differ
only through the prospectively sealed final-layer rules.  ``Estimator`` is the
V000/H107-O entry point; ``VARIANT_CLASSES`` exposes every nested arm to the
T108 runners without changing the production contract.
"""

from __future__ import annotations

import math

import flopscope as flops
import flopscope.numpy as fnp
from whestbench import BaseEstimator, MLP


_WIDTH = 1024
_DEPTH = 16
_FRAME_ROWS = 2048
_PARTIAL_BASE_ROWS = 288
_PARTIAL_EXTENSION_ROWS = 44
_PARTIAL_ROWS = _PARTIAL_BASE_ROWS + _PARTIAL_EXTENSION_ROWS
_RADIUS = 31.992188454829048
_HERMITE_ORDER = 12
_SATURATION = 12.0
_PARTIAL_BASE_STREAM_XOR = 0x5EED98A1
_PARTIAL_EXTENSION_STREAM_XOR = 0xA44D107E
_INV_SQRT_2PI = 1.0 / math.sqrt(2.0 * math.pi)
_COV_RESCALE_THRESHOLD = 1e30
_MIN_FULL_BUDGET = 220_000_000_000
_EPS64 = 1e-30

_EARLY_FRAME_WEIGHT = 0.260
_EARLY_PARTIAL_WEIGHT = 0.025
_EARLY_CLOSURE_WEIGHT = 0.715
_STOCHASTIC_WEIGHT_TOTAL = _EARLY_FRAME_WEIGHT + _EARLY_PARTIAL_WEIGHT
_FRAME_SHARE = _EARLY_FRAME_WEIGHT / _STOCHASTIC_WEIGHT_TOTAL
_PARTIAL_SHARE = _EARLY_PARTIAL_WEIGHT / _STOCHASTIC_WEIGHT_TOTAL


class _FamilyEstimator(BaseEstimator):
    variant = "V000"

    @staticmethod
    def _zero(mlp: MLP) -> fnp.ndarray:
        return fnp.zeros((mlp.depth, mlp.width), dtype=fnp.float32)

    @staticmethod
    def _fallback(mlp: MLP, budget: int) -> fnp.ndarray:
        if budget < 100_000_000:
            return _FamilyEstimator._zero(mlp)
        mu = fnp.zeros(mlp.width, dtype=fnp.float32)
        var = fnp.ones(mlp.width, dtype=fnp.float32)
        rows = []
        for raw_weight in mlp.weights:
            weight = fnp.asarray(raw_weight, dtype=fnp.float32)
            mu_pre = mu @ weight
            var_pre = fnp.maximum(var @ (weight * weight), 1e-12)
            sigma = fnp.sqrt(var_pre)
            alpha = mu_pre / sigma
            pdf = flops.stats.norm.pdf(alpha).astype(fnp.float32)
            cdf = flops.stats.norm.cdf(alpha).astype(fnp.float32)
            mu = mu_pre * cdf + sigma * pdf
            second = (mu_pre * mu_pre + var_pre) * cdf + mu_pre * sigma * pdf
            var = fnp.maximum(second - mu * mu, 0.0)
            rows.append(fnp.asarray(mu, dtype=fnp.float32))
        return fnp.stack(rows, axis=0)

    @staticmethod
    def _exact_first(weight: fnp.ndarray) -> fnp.ndarray:
        return fnp.sqrt(fnp.sum(weight * weight, axis=0)) * _INV_SQRT_2PI

    @staticmethod
    def _weighted_hermite(alpha, pdf, maximum_degree):
        safe_alpha = fnp.minimum(fnp.maximum(alpha, -_SATURATION), _SATURATION)
        valid = fnp.abs(alpha) <= _SATURATION
        previous = fnp.where(
            valid, pdf, fnp.zeros(alpha.shape, dtype=fnp.float32)
        )
        values = [previous]
        if maximum_degree == 0:
            return values
        current = safe_alpha * previous
        values.append(current)
        for degree in range(2, maximum_degree + 1):
            following = safe_alpha * current - float(degree - 1) * previous
            previous, current = current, following
            values.append(current)
        return values

    @classmethod
    def _propagate_positive(cls, positive, weights):
        rows = positive.shape[0]
        activations = fnp.concatenate((positive, -positive), axis=0)
        outputs = []
        final_preactivation = None
        for layer, weight in enumerate(weights):
            preactivation = activations @ weight
            if layer == len(weights) - 1:
                final_preactivation = preactivation
            activations = fnp.maximum(preactivation, 0.0)
            outputs.append(
                fnp.mean(
                    (activations[:rows] + activations[rows:]) * 0.5,
                    axis=0,
                    dtype=fnp.float32,
                )
            )
        exact_first = cls._exact_first(weights[0])
        assert final_preactivation is not None
        return fnp.stack([exact_first] + outputs[1:], axis=0), final_preactivation

    @classmethod
    def _frame_predict_with_final_pre(cls, mlp: MLP):
        weights = [fnp.asarray(weight, dtype=fnp.float32) for weight in mlp.weights]
        rng = fnp.random.default_rng(mlp.seed)
        gaussian = rng.standard_normal((_FRAME_ROWS, _WIDTH), dtype=fnp.float32)
        q, r = fnp.linalg.qr(gaussian, mode="reduced")
        leverage = fnp.sum(q * q, axis=1)
        positive = q * (_RADIUS / fnp.sqrt(leverage))[:, None]
        result = cls._propagate_positive(positive, weights)
        del gaussian, q, r, leverage, positive
        return result

    @classmethod
    def _partial_positive(cls, mlp: MLP):
        base_rng = fnp.random.default_rng(
            int(mlp.seed) ^ _PARTIAL_BASE_STREAM_XOR
        )
        base_gaussian = base_rng.standard_normal(
            (_WIDTH, _PARTIAL_BASE_ROWS), dtype=fnp.float32
        )
        q0, r0 = fnp.linalg.qr(base_gaussian, mode="reduced")

        extension_rng = fnp.random.default_rng(
            int(mlp.seed) ^ _PARTIAL_EXTENSION_STREAM_XOR
        )
        extension_gaussian = extension_rng.standard_normal(
            (_WIDTH, _PARTIAL_EXTENSION_ROWS), dtype=fnp.float32
        )
        projection = q0 @ (q0.T @ extension_gaussian)
        extension_residual = extension_gaussian - projection
        q1, r1 = fnp.linalg.qr(extension_residual, mode="reduced")
        q = fnp.concatenate((q0, q1), axis=1)
        positive = q.T * _RADIUS
        del base_gaussian, extension_gaussian, projection, extension_residual
        del r0, r1, q
        return positive, q0.T * _RADIUS

    @classmethod
    def _partial_predict(cls, mlp: MLP):
        weights = [fnp.asarray(weight, dtype=fnp.float32) for weight in mlp.weights]
        positive, _ = cls._partial_positive(mlp)
        prediction, _ = cls._propagate_positive(positive, weights)
        return prediction

    @classmethod
    def _partial_base_predict(cls, mlp: MLP):
        weights = [fnp.asarray(weight, dtype=fnp.float32) for weight in mlp.weights]
        base_rng = fnp.random.default_rng(
            int(mlp.seed) ^ _PARTIAL_BASE_STREAM_XOR
        )
        base_gaussian = base_rng.standard_normal(
            (_WIDTH, _PARTIAL_BASE_ROWS), dtype=fnp.float32
        )
        q0, r0 = fnp.linalg.qr(base_gaussian, mode="reduced")
        positive = q0.T * _RADIUS
        prediction, _ = cls._propagate_positive(positive, weights)
        del base_gaussian, q0, r0, positive
        return prediction

    @classmethod
    def _partial_prefix_predict(cls, mlp: MLP):
        weights = [fnp.asarray(weight, dtype=fnp.float32) for weight in mlp.weights]
        _, base_positive = cls._partial_positive(mlp)
        prediction, _ = cls._propagate_positive(base_positive, weights)
        return prediction

    @classmethod
    def _closure_predict_with_final_state(cls, mlp: MLP):
        width = mlp.width
        mu = fnp.zeros(width, dtype=fnp.float32)
        cov = flops.as_symmetric(
            fnp.eye(width, dtype=fnp.float32), symmetry=(0, 1)
        )
        log_scale = 0.0
        outputs = []
        final_alpha = None
        final_sigma_physical = None
        final_pdf = None
        for layer, raw_weight in enumerate(mlp.weights):
            weight = fnp.asarray(raw_weight, dtype=fnp.float32)
            max_var = float(fnp.max(fnp.diag(cov)))
            if max_var > _COV_RESCALE_THRESHOLD:
                scale = float(fnp.sqrt(max_var))
                mu = mu / scale
                cov = cov / (scale * scale)
                log_scale += float(fnp.log(scale))

            mu_pre = weight.T @ mu
            cov_pre = fnp.einsum("ij,ia,jb->ab", cov, weight, weight)
            var_pre = fnp.maximum(fnp.diag(cov_pre), 1e-12)
            sigma = fnp.sqrt(var_pre)
            alpha = mu_pre / sigma
            pdf = flops.stats.norm.pdf(alpha).astype(fnp.float32)
            cdf = flops.stats.norm.cdf(alpha).astype(fnp.float32)
            mu = mu_pre * cdf + sigma * pdf
            second = (mu_pre * mu_pre + var_pre) * cdf + mu_pre * sigma * pdf
            var_post = fnp.maximum(second - mu * mu, 0.0)

            cov = fnp.multiply(fnp.outer(cdf, cdf), cov_pre)
            sigma_outer = fnp.outer(sigma, sigma)
            correlation = cov_pre / fnp.maximum(sigma_outer, 1e-30)
            correlation = fnp.minimum(fnp.maximum(correlation, -1.0), 1.0)
            weighted = cls._weighted_hermite(alpha, pdf, _HERMITE_ORDER - 2)
            rho_power = correlation * correlation
            factorial = 2.0
            cov = cov + sigma_outer * rho_power * fnp.outer(
                weighted[0], weighted[0]
            ) / factorial
            for degree in range(3, _HERMITE_ORDER + 1):
                rho_power = rho_power * correlation
                factorial *= float(degree)
                coefficient = weighted[degree - 2]
                cov = cov + sigma_outer * rho_power * fnp.outer(
                    coefficient, coefficient
                ) / factorial
            fnp.fill_diagonal(cov, var_post)
            cov = flops.as_symmetric(cov, symmetry=(0, 1))
            physical_scale = float(fnp.exp(log_scale))
            outputs.append(mu * physical_scale)
            if layer == len(mlp.weights) - 1:
                final_alpha = alpha
                final_sigma_physical = sigma * physical_scale
                final_pdf = pdf

        exact_first = cls._exact_first(
            fnp.asarray(mlp.weights[0], dtype=fnp.float32)
        )
        assert final_alpha is not None
        assert final_sigma_physical is not None
        assert final_pdf is not None
        return (
            fnp.stack([exact_first] + outputs[1:], axis=0),
            final_alpha,
            final_sigma_physical,
            final_pdf,
        )

    @staticmethod
    def _block_moments(block):
        mean = fnp.mean(block, axis=0, dtype=fnp.float64)
        centered = block - mean
        squared = centered * centered
        second = fnp.mean(squared, axis=0, dtype=fnp.float64)
        third = fnp.mean(squared * centered, axis=0, dtype=fnp.float64)
        return mean, second, third

    @staticmethod
    def _combine_equal_moments(left, right):
        left_mean, left_second, left_third = left
        right_mean, right_second, right_third = right
        delta = right_mean - left_mean
        mean = (left_mean + right_mean) * 0.5
        second = (
            (left_second + right_second) * 0.5
            + delta * delta * 0.25
        )
        third = (
            (left_third + right_third) * 0.5
            + delta * (right_second - left_second) * 0.75
        )
        return mean, second, third

    @classmethod
    def _skew_statistics(cls, final_preactivation, alpha, sigma, pdf):
        z = fnp.asarray(final_preactivation, dtype=fnp.float64)
        a_positive = cls._block_moments(z[0:1024])
        b_positive = cls._block_moments(z[1024:2048])
        a_negative = cls._block_moments(z[2048:3072])
        b_negative = cls._block_moments(z[3072:4096])
        half_a = cls._combine_equal_moments(a_positive, a_negative)
        half_b = cls._combine_equal_moments(b_positive, b_negative)
        full = cls._combine_equal_moments(half_a, half_b)

        def standardized(moment):
            safe_second = fnp.maximum(moment[1], _EPS64)
            return moment[2] / (safe_second * fnp.sqrt(safe_second))

        half_a_skew = standardized(half_a)
        half_b_skew = standardized(half_b)
        full_skew = standardized(full)
        alpha64 = fnp.asarray(alpha, dtype=fnp.float64)
        sigma64 = fnp.asarray(sigma, dtype=fnp.float64)
        pdf64 = fnp.asarray(pdf, dtype=fnp.float64)
        influence = sigma64 * alpha64 * pdf64 / 6.0
        influence_sq = influence * influence
        influence_total = fnp.sum(influence_sq)
        beta_denominator = fnp.sum(influence_sq * alpha64 * alpha64)
        beta = fnp.sum(influence_sq * alpha64 * full_skew) / fnp.maximum(
            beta_denominator, _EPS64
        )
        residual = full_skew - beta * alpha64
        noise = 0.25 * fnp.sum(
            influence_sq * (half_a_skew - half_b_skew)
            * (half_a_skew - half_b_skew)
        ) / fnp.maximum(influence_total, _EPS64)
        observed = fnp.sum(influence_sq * residual * residual) / fnp.maximum(
            influence_total, _EPS64
        )
        rho_raw = 1.0 - noise / fnp.maximum(observed, _EPS64)
        rho = fnp.where(
            observed <= _EPS64,
            fnp.zeros(observed.shape, dtype=fnp.float64),
            fnp.minimum(fnp.maximum(rho_raw, 0.0), 1.0),
        )
        harmonic_skew = fnp.minimum(
            fnp.maximum(beta * alpha64 + rho * residual, -1.0), 1.0
        )
        clipped_full_skew = fnp.minimum(fnp.maximum(full_skew, -1.0), 1.0)
        return {
            "half_a_skew": half_a_skew,
            "half_b_skew": half_b_skew,
            "full_skew": full_skew,
            "clipped_full_skew": clipped_full_skew,
            "harmonic_skew": harmonic_skew,
            "beta": beta,
            "rho": rho,
            "noise": noise,
            "observed": observed,
            "alpha64": alpha64,
            "sigma64": sigma64,
            "pdf64": pdf64,
        }

    @staticmethod
    def _final_closure_weight(variant, alpha):
        absolute = fnp.abs(alpha)
        if variant == "V001":
            return fnp.where(absolute <= 3.0, 0.800, 0.610)
        if variant in ("V000", "V002", "V003"):
            return fnp.where(
                absolute <= 1.0,
                0.840,
                fnp.where(absolute <= 3.0, 0.795, 0.610),
            )
        return fnp.full(alpha.shape, _EARLY_CLOSURE_WEIGHT, dtype=fnp.float32)

    @staticmethod
    def _blend(frame, partial, closure, final_closure_weight, exact_first):
        early = (
            _EARLY_FRAME_WEIGHT * frame
            + _EARLY_PARTIAL_WEIGHT * partial
            + _EARLY_CLOSURE_WEIGHT * closure
        )
        remaining = 1.0 - final_closure_weight
        final = (
            remaining * _FRAME_SHARE * frame[-1]
            + remaining * _PARTIAL_SHARE * partial[-1]
            + final_closure_weight * closure[-1]
        )
        return fnp.asarray(
            fnp.concatenate(
                (exact_first[None, :], early[1:-1], final[None, :]), axis=0
            ),
            dtype=fnp.float32,
        )

    @classmethod
    def _predict_variant_with_diagnostics(cls, mlp: MLP, variant: str):
        frame, final_pre = cls._frame_predict_with_final_pre(mlp)
        partial = cls._partial_predict(mlp)
        closure, alpha, sigma, pdf = cls._closure_predict_with_final_state(mlp)
        final_closure = closure
        statistics = None
        if variant in ("V000", "V002"):
            statistics = cls._skew_statistics(final_pre, alpha, sigma, pdf)
            skew = (
                statistics["harmonic_skew"]
                if variant == "V000"
                else statistics["clipped_full_skew"]
            )
            delta = (
                -statistics["sigma64"]
                * skew
                * statistics["alpha64"]
                * statistics["pdf64"]
                / 6.0
            )
            corrected_final = fnp.asarray(
                fnp.asarray(closure[-1], dtype=fnp.float64) + delta,
                dtype=fnp.float32,
            )
            final_closure = fnp.concatenate(
                (closure[:-1], corrected_final[None, :]), axis=0
            )
        closure_weight = cls._final_closure_weight(variant, alpha)
        exact_first = cls._exact_first(
            fnp.asarray(mlp.weights[0], dtype=fnp.float32)
        )
        prediction = cls._blend(
            frame, partial, final_closure, closure_weight, exact_first
        )
        return prediction, {
            "frame": frame,
            "partial": partial,
            "closure": closure,
            "corrected_closure": final_closure,
            "alpha": alpha,
            "sigma": sigma,
            "pdf": pdf,
            "final_preactivation": final_pre,
            "final_closure_weight": closure_weight,
            "skew_statistics": statistics,
        }

    @classmethod
    def _predict_variant(cls, mlp: MLP, variant: str):
        prediction, _ = cls._predict_variant_with_diagnostics(mlp, variant)
        return prediction

    def predict(self, mlp: MLP, budget: int) -> fnp.ndarray:
        if mlp.width != _WIDTH or mlp.depth != _DEPTH or budget < _MIN_FULL_BUDGET:
            return self._fallback(mlp, budget)
        return self._predict_variant(mlp, self.variant)


class EstimatorV000(_FamilyEstimator):
    variant = "V000"


class EstimatorV001(_FamilyEstimator):
    variant = "V001"


class EstimatorV002(_FamilyEstimator):
    variant = "V002"


class EstimatorV003(_FamilyEstimator):
    variant = "V003"


class EstimatorV004(_FamilyEstimator):
    variant = "V004"


Estimator = EstimatorV000

VARIANT_CLASSES = {
    "ALG019-V000": EstimatorV000,
    "ALG019-V001": EstimatorV001,
    "ALG019-V002": EstimatorV002,
    "ALG019-V003": EstimatorV003,
    "ALG019-V004": EstimatorV004,
}

VARIANT_HYPOTHESES = {
    "ALG019-V000": "H107-O",
    "ALG019-V001": "H107-I",
    "ALG019-V002": "H107-N",
    "ALG019-V003": "H107-J",
    "ALG019-V004": "H107-F",
}
