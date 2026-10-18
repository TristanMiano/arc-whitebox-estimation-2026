"""ALG024-V000: T117 Full-selected AS audit-free observer."""

from __future__ import annotations

import flopscope.numpy as fnp
from whestbench import BaseEstimator, MLP
import observer_family as family



_WIDTH = 1024
_DEPTH = 16
_MIN_FULL_BUDGET = 220_000_000_000
_RUNG = "AS"
_COEFFICIENTS = (
    -0.07376151392341117,
    -0.003433525700266425,
    -0.4552882544157547,
    -0.10027985344232235,
    -0.013238231103130021,
    4.407986109910849,
    0.7656082669390457,
    -0.17618379020172156,
    -13.22034375345173,
    1.4398907052111742,
    -7.697168270070758,
    3.8782132603904436,
)


class Estimator(BaseEstimator):
    """Return ALG019 with the fixed 12-feature AS final-layer correction."""

    def predict(self, mlp: MLP, budget: int) -> fnp.ndarray:
        if mlp.width != _WIDTH or mlp.depth != _DEPTH or budget < _MIN_FULL_BUDGET:
            fallback = family.parent._LPITFFamily._fallback(mlp, budget)
            return fnp.maximum(fallback, 0.0)
        bundle = family.feature_bundle(mlp, _RUNG)
        final = family.apply_observer(bundle, _RUNG, _COEFFICIENTS)
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
