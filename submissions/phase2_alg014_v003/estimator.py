"""ALG014-V003: Phase 2 equal-weight Haar-Stiefel realization.

The width-1024 implementation preserves ALG014-V000's equal-weight normalized
Haar-Stiefel rows, antithetic pairing, exact mean-chi radius, and exact first
layer.  It uses grader-seeded flopscope Gaussian QR and four (2048 x 1024)
frames, giving 8,192 positive pairs.  Shape, generator, and accumulation
changes give this submission realization a new identity and no transferred
scientific tier.
"""

from __future__ import annotations

import math

import flopscope as flops
import flopscope.numpy as fnp
from whestbench import MLP, BaseEstimator


_WIDTH = 1024
_DEPTH = 16
_FRAME_ROWS = 2048
_FRAME_BLOCKS = 4
_MIN_FULL_BUDGET = 550_000_000_000
_RADIUS = 31.992188454829048
_INV_SQRT_2PI = 1.0 / math.sqrt(2.0 * math.pi)


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

    def predict(self, mlp: MLP, budget: int) -> fnp.ndarray:
        if mlp.width != _WIDTH or mlp.depth != _DEPTH or budget < _MIN_FULL_BUDGET:
            return self._fallback(mlp, budget)

        weights = [fnp.asarray(weight, dtype=fnp.float32) for weight in mlp.weights]
        layer_sums = [fnp.zeros(_WIDTH, dtype=fnp.float32) for _ in range(_DEPTH)]

        # Keep all four statistically independent blocks in one stacked array.
        # Stacked QR performs one QR per leading-index block, while batching the
        # forward paths avoids hundreds of client/server round trips under the
        # grader-like subprocess runner.
        rng = fnp.random.default_rng(mlp.seed)
        gaussian = rng.standard_normal(
            (_FRAME_BLOCKS, _FRAME_ROWS, _WIDTH), dtype=fnp.float32
        )
        q, r = fnp.linalg.qr(gaussian, mode="reduced")
        leverage = fnp.sum(q * q, axis=2)
        directions = q * (_RADIUS / fnp.sqrt(leverage))[:, :, None]
        positive = fnp.reshape(directions, (_FRAME_BLOCKS * _FRAME_ROWS, _WIDTH))
        activations = fnp.concatenate((positive, -positive), axis=0)
        del gaussian, q, r, leverage, directions, positive

        for layer, weight in enumerate(weights):
            activations = fnp.maximum(activations @ weight, 0.0)
            layer_sums[layer] = fnp.mean(
                (
                    activations[: _FRAME_BLOCKS * _FRAME_ROWS]
                    + activations[_FRAME_BLOCKS * _FRAME_ROWS :]
                )
                * 0.5,
                axis=0,
                dtype=fnp.float32,
            )

        rows = layer_sums
        first_weight = weights[0]
        rows[0] = fnp.sqrt(fnp.sum(first_weight * first_weight, axis=0)) * _INV_SQRT_2PI
        return fnp.stack(rows, axis=0)
