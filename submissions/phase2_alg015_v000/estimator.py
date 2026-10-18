"""ALG015-V000: fixed one-frame / full-covariance Phase 2 shrinkage.

The stochastic endpoint is one 2048-row mean-chi-radius Haar-Stiefel frame
with antithetic evaluation.  The deterministic endpoint is float32 full
covariance propagation.  The returned estimate was fixed prospectively as
one quarter frame plus three quarters covariance at every layer, with the
first layer replaced by its exact Gaussian value.
"""

from __future__ import annotations

import math

import flopscope as flops
import flopscope.numpy as fnp
from whestbench import MLP, BaseEstimator


_WIDTH = 1024
_DEPTH = 16
_FRAME_ROWS = 2048
_MIN_FULL_BUDGET = 190_000_000_000
_RADIUS = 31.992188454829048
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
        for weight in mlp.weights:
            weight32 = fnp.asarray(weight, dtype=fnp.float32)
            mu_pre = mu @ weight32
            var_pre = fnp.maximum(var @ (weight32 * weight32), 1e-12)
            sigma = fnp.sqrt(var_pre)
            alpha = mu_pre / sigma
            pdf = flops.stats.norm.pdf(alpha)
            cdf = flops.stats.norm.cdf(alpha)
            mu = mu_pre * cdf + sigma * pdf
            second = (mu_pre * mu_pre + var_pre) * cdf + mu_pre * sigma * pdf
            var = fnp.maximum(second - mu * mu, 0.0)
            rows.append(fnp.asarray(mu, dtype=fnp.float32))
        return fnp.stack(rows, axis=0)

    @staticmethod
    def _exact_first(weight: fnp.ndarray) -> fnp.ndarray:
        return fnp.sqrt(fnp.sum(weight * weight, axis=0)) * _INV_SQRT_2PI

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

        rows = []
        for weight in weights:
            activations = fnp.maximum(activations @ weight, 0.0)
            rows.append(
                fnp.mean(
                    (activations[:_FRAME_ROWS] + activations[_FRAME_ROWS:]) * 0.5,
                    axis=0,
                    dtype=fnp.float32,
                )
            )
        rows[0] = Estimator._exact_first(weights[0])
        return fnp.stack(rows, axis=0)

    @staticmethod
    def _covariance_predict(mlp: MLP) -> fnp.ndarray:
        width = mlp.width
        mu = fnp.zeros(width, dtype=fnp.float32)
        cov = flops.as_symmetric(
            fnp.eye(width, dtype=fnp.float32), symmetry=(0, 1)
        )
        log_scale = 0.0
        rows = []

        for raw_weight in mlp.weights:
            weight = fnp.asarray(raw_weight, dtype=fnp.float32)
            cov_diag = fnp.diag(cov)
            max_var = float(fnp.max(cov_diag))
            if max_var > _COV_RESCALE_THRESHOLD:
                scale = float(fnp.sqrt(max_var))
                mu = mu / scale
                cov = cov / (scale * scale)
                log_scale += float(fnp.log(scale))

            mu_pre = weight.T @ mu
            cov_pre = fnp.einsum("ij,ia,jb->ab", cov, weight, weight)
            var_pre = fnp.maximum(fnp.diag(cov_pre), 1e-12)
            sigma_pre = fnp.sqrt(var_pre)
            alpha = mu_pre / sigma_pre
            pdf = flops.stats.norm.pdf(alpha).astype(fnp.float32)
            cdf = flops.stats.norm.cdf(alpha).astype(fnp.float32)
            mu = mu_pre * cdf + sigma_pre * pdf
            second = (
                (mu_pre * mu_pre + var_pre) * cdf
                + mu_pre * sigma_pre * pdf
            )
            var_post = fnp.maximum(second - mu * mu, 0.0)
            zero32 = fnp.zeros((), dtype=fnp.float32)
            gain = fnp.where(sigma_pre > 1e-12, cdf, zero32)
            cov = fnp.multiply(fnp.outer(gain, gain), cov_pre)
            fnp.fill_diagonal(cov, var_post)
            cov = flops.as_symmetric(cov, symmetry=(0, 1))
            rows.append(mu * float(fnp.exp(log_scale)))

        rows[0] = Estimator._exact_first(
            fnp.asarray(mlp.weights[0], dtype=fnp.float32)
        )
        return fnp.stack(rows, axis=0)

    def predict(self, mlp: MLP, budget: int) -> fnp.ndarray:
        if mlp.width != _WIDTH or mlp.depth != _DEPTH or budget < _MIN_FULL_BUDGET:
            return self._fallback(mlp, budget)

        frame = self._frame_predict(mlp)
        closure = self._covariance_predict(mlp)
        estimate = frame * 0.25 + closure * 0.75
        exact_first = self._exact_first(
            fnp.asarray(mlp.weights[0], dtype=fnp.float32)
        )
        return fnp.asarray(
            fnp.concatenate((exact_first[None, :], estimate[1:]), axis=0),
            dtype=fnp.float32,
        )
