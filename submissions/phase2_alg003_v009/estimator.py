"""ALG003-V009: Phase 2 fixed Sobol fallback realization.

This width-1024 realization preserves ALG003-V008's complete-block spherical
Sobol, antithetic, seed-reflection, exact-radius, and exact-first-layer rules.
The 50 MiB package cap requires one int8 bank instead of three float16 banks;
rows are restored and renormalized through flopscope at prediction time.  That
material change is why this has a new identity and inherits no scientific tier.
"""

from __future__ import annotations

import math
from pathlib import Path

import flopscope as flops
import flopscope.numpy as fnp
from whestbench import MLP, BaseEstimator, SetupContext


_WIDTH = 1024
_DEPTH = 16
_ALLOWED_PREFIXES = (8_192,)
_SAFETY_FRACTION = 0.97
_QUANTIZATION_SCALE = 20.0
_RADIUS = 31.992188454829048
_INV_SQRT_2PI = 1.0 / math.sqrt(2.0 * math.pi)
_ASSET = "sobol_sphere_bank_i8.npy"


class Estimator(BaseEstimator):
    def __init__(self) -> None:
        self._points = None
        self._submission_dir: str | None = None

    def setup(self, context: SetupContext) -> None:
        self._submission_dir = context.submission_dir
        self._load()

    def teardown(self) -> None:
        self._points = None

    def _load(self) -> None:
        base = (
            Path(self._submission_dir)
            if self._submission_dir is not None
            else Path(__file__).resolve().parent
        )
        path = base / _ASSET
        self._points = fnp.load(str(path)) if path.is_file() else None

    @staticmethod
    def _zero(mlp: MLP) -> fnp.ndarray:
        return fnp.zeros((mlp.depth, mlp.width), dtype=fnp.float32)

    @staticmethod
    def _fallback(mlp: MLP, budget: int) -> fnp.ndarray:
        # Validation supplies budget=100 outside a BudgetContext.  Return a
        # correctly shaped safe answer instead of executing a probe-only model.
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
    def _choose_count(budget: int, available: int) -> int:
        per_positive = _DEPTH * (4 * _WIDTH * _WIDTH + 2 * _WIDTH)
        cap = int(_SAFETY_FRACTION * budget) // per_positive
        chosen = 0
        for candidate in _ALLOWED_PREFIXES:
            if candidate <= cap and candidate <= available:
                chosen = candidate
        return chosen

    def predict(self, mlp: MLP, budget: int) -> fnp.ndarray:
        if self._points is None:
            self._load()
        if (
            self._points is None
            or mlp.width != _WIDTH
            or mlp.depth != _DEPTH
            or self._points.ndim != 2
            or self._points.shape[1] != _WIDTH
        ):
            return self._fallback(mlp, budget)

        count = self._choose_count(budget, int(self._points.shape[0]))
        if count < _ALLOWED_PREFIXES[0]:
            return self._fallback(mlp, budget)

        positive = fnp.asarray(self._points[:count], dtype=fnp.float32)
        positive = positive / _QUANTIZATION_SCALE
        norms = fnp.sqrt(fnp.sum(positive * positive, axis=1))
        positive = positive * (_RADIUS / norms)[:, None]

        rng = fnp.random.default_rng(mlp.seed)
        signs = fnp.asarray(
            fnp.where(rng.uniform(0.0, 1.0, size=mlp.width) < 0.5, -1.0, 1.0),
            dtype=fnp.float32,
        )
        positive = positive * signs
        activations = fnp.concatenate((positive, -positive), axis=0)
        rows = []
        for weight in mlp.weights:
            weight32 = fnp.asarray(weight, dtype=fnp.float32)
            activations = fnp.maximum(activations @ weight32, 0.0)
            rows.append(fnp.mean(activations, axis=0, dtype=fnp.float32))

        first_weight = fnp.asarray(mlp.weights[0], dtype=fnp.float32)
        rows[0] = fnp.sqrt(fnp.sum(first_weight * first_weight, axis=0)) * _INV_SQRT_2PI
        return fnp.stack(rows, axis=0)
