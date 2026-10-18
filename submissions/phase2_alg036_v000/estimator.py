"""ALG036-V000: absolute-state correction anchored at ALG031."""

from __future__ import annotations

import flopscope.numpy as fnp
from whestbench import BaseEstimator, MLP, SetupContext

import r1p_family
from coefficients import DELTA
from parity_coefficients import PARITY_DELTA
from absolute_coefficients import ABSOLUTE_DELTA


_WIDTH = 1024
_DEPTH = 16
_MIN_FULL_BUDGET = 220_000_000_000
_GAMMA = 0.021207293228815507
_COEFFICIENTS = (
    0.022335018705144927,
    -0.006717104161326076,
    -0.21431959342309018,
    -0.12569592752155787,
    -0.012815033441494608,
    3.795660733390352,
    0.7946249845342089,
    -0.30101750662565674,
    -11.214672161671643,
    1.0994254620447101,
    -6.476506757123343,
    3.0965098650043585,
)


class Estimator(BaseEstimator):
    """Return the fixed T134 absolute-state response fit."""

    def __init__(self) -> None:
        self.family = r1p_family.Family(depth=5, child_rows=1536, use_fast=True)

    def setup(self, context: SetupContext) -> None:
        self.family.setup(context)

    def predict(self, mlp: MLP, budget: int) -> fnp.ndarray:
        if mlp.width != _WIDTH or mlp.depth != _DEPTH or budget < _MIN_FULL_BUDGET:
            return fnp.maximum(self.family._fallback(mlp, budget), 0.0)
        return self.family.r1p_predict(
            mlp,
            gamma=_GAMMA,
            coefficients=_COEFFICIENTS,
            delta=DELTA,
            delta127=PARITY_DELTA,
            absolute_delta=ABSOLUTE_DELTA,
        )
