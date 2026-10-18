"""ALG018-V000: order-12 Hermite blend plus partial-Haar headroom.

H098-B / ALG018-V001 is the nested mechanism control: one 2048-row
mean-chi-radius Haar-Stiefel frame blended one-quarter with an order-12
density-weighted Price/Hermite covariance closure at weight three-quarters.

H098-A / ALG018-V000 adds an independent 288-row Haar partial basis with
within-stochastic weight 1/17 before the same final one-quarter/three-quarter
blend.  All coefficients and random streams are prospective and target-free.
"""

from __future__ import annotations

import math

import flopscope as flops
import flopscope.numpy as fnp
from whestbench import BaseEstimator, MLP


_WIDTH = 1024
_DEPTH = 16
_FRAME_ROWS = 2048
_PARTIAL_ROWS = 288
_PARTIAL_WEIGHT = 1.0 / 17.0
_CLOSURE_WEIGHT = 0.75
_MIN_FULL_BUDGET = 220_000_000_000
_RADIUS = 31.992188454829048
_HERMITE_ORDER = 12
_SATURATION = 12.0
_PARTIAL_STREAM_XOR = 0x5EED98A1
_INV_SQRT_2PI = 1.0 / math.sqrt(2.0 * math.pi)
_COV_RESCALE_THRESHOLD = 1e30


class Estimator(BaseEstimator):
    @staticmethod
    def _zero(mlp: MLP) -> fnp.ndarray:
        return fnp.zeros((mlp.depth, mlp.width), dtype=fnp.float32)

    @staticmethod
    def _fallback(mlp: MLP, budget: int) -> fnp.ndarray:
        if budget < 100_000_000:
            return Estimator._zero(mlp)
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

    @staticmethod
    def _frame_predict(mlp: MLP) -> fnp.ndarray:
        weights = [fnp.asarray(weight, dtype=fnp.float32) for weight in mlp.weights]
        rng = fnp.random.default_rng(mlp.seed)
        gaussian = rng.standard_normal((_FRAME_ROWS, _WIDTH), dtype=fnp.float32)
        q, r = fnp.linalg.qr(gaussian, mode="reduced")
        leverage = fnp.sum(q * q, axis=1)
        positive = q * (_RADIUS / fnp.sqrt(leverage))[:, None]
        activations = fnp.concatenate((positive, -positive), axis=0)
        del gaussian, q, r, leverage, positive

        outputs = []
        for weight in weights:
            activations = fnp.maximum(activations @ weight, 0.0)
            outputs.append(
                fnp.mean(
                    (activations[:_FRAME_ROWS] + activations[_FRAME_ROWS:]) * 0.5,
                    axis=0,
                    dtype=fnp.float32,
                )
            )
        exact_first = Estimator._exact_first(weights[0])
        return fnp.stack([exact_first] + outputs[1:], axis=0)

    @staticmethod
    def _partial_predict(mlp: MLP) -> fnp.ndarray:
        weights = [fnp.asarray(weight, dtype=fnp.float32) for weight in mlp.weights]
        rng = fnp.random.default_rng(int(mlp.seed) ^ _PARTIAL_STREAM_XOR)
        gaussian = rng.standard_normal(
            (_WIDTH, _PARTIAL_ROWS), dtype=fnp.float32
        )
        q, r = fnp.linalg.qr(gaussian, mode="reduced")
        positive = q.T * _RADIUS
        activations = fnp.concatenate((positive, -positive), axis=0)
        del gaussian, q, r, positive

        outputs = []
        for weight in weights:
            activations = fnp.maximum(activations @ weight, 0.0)
            outputs.append(
                fnp.mean(
                    (
                        activations[:_PARTIAL_ROWS]
                        + activations[_PARTIAL_ROWS:]
                    )
                    * 0.5,
                    axis=0,
                    dtype=fnp.float32,
                )
            )
        exact_first = Estimator._exact_first(weights[0])
        return fnp.stack([exact_first] + outputs[1:], axis=0)

    @staticmethod
    def _closure_predict(mlp: MLP) -> fnp.ndarray:
        width = mlp.width
        mu = fnp.zeros(width, dtype=fnp.float32)
        cov = flops.as_symmetric(
            fnp.eye(width, dtype=fnp.float32), symmetry=(0, 1)
        )
        log_scale = 0.0
        outputs = []
        for raw_weight in mlp.weights:
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
            rho = cov_pre / fnp.maximum(sigma_outer, 1e-30)
            rho = fnp.minimum(fnp.maximum(rho, -1.0), 1.0)
            weighted = Estimator._weighted_hermite(
                alpha, pdf, _HERMITE_ORDER - 2
            )
            rho_power = rho * rho
            factorial = 2.0
            cov = cov + sigma_outer * rho_power * fnp.outer(
                weighted[0], weighted[0]
            ) / factorial
            for degree in range(3, _HERMITE_ORDER + 1):
                rho_power = rho_power * rho
                factorial *= float(degree)
                coefficient = weighted[degree - 2]
                cov = cov + sigma_outer * rho_power * fnp.outer(
                    coefficient, coefficient
                ) / factorial
            fnp.fill_diagonal(cov, var_post)
            cov = flops.as_symmetric(cov, symmetry=(0, 1))
            outputs.append(mu * float(fnp.exp(log_scale)))

        exact_first = Estimator._exact_first(
            fnp.asarray(mlp.weights[0], dtype=fnp.float32)
        )
        return fnp.stack([exact_first] + outputs[1:], axis=0)

    @staticmethod
    def _control_predict(mlp: MLP) -> fnp.ndarray:
        frame = Estimator._frame_predict(mlp)
        closure = Estimator._closure_predict(mlp)
        return fnp.asarray(
            frame * (1.0 - _CLOSURE_WEIGHT) + closure * _CLOSURE_WEIGHT,
            dtype=fnp.float32,
        )

    @staticmethod
    def _candidate_predict(mlp: MLP) -> fnp.ndarray:
        frame = Estimator._frame_predict(mlp)
        partial = Estimator._partial_predict(mlp)
        closure = Estimator._closure_predict(mlp)
        stochastic = frame * (1.0 - _PARTIAL_WEIGHT) + partial * _PARTIAL_WEIGHT
        return fnp.asarray(
            stochastic * (1.0 - _CLOSURE_WEIGHT) + closure * _CLOSURE_WEIGHT,
            dtype=fnp.float32,
        )

    def predict(self, mlp: MLP, budget: int) -> fnp.ndarray:
        if mlp.width != _WIDTH or mlp.depth != _DEPTH or budget < _MIN_FULL_BUDGET:
            return self._fallback(mlp, budget)
        return self._candidate_predict(mlp)
