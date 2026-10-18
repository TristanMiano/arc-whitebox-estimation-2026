# T122 — Theory recurrence after the ALG028 official win

The recommended next task is **T124: one inexpensive recalibration of ALG028,
using a fixed physical shape residual and the existing training cache**. A
source-standardized covariance trace correction is the second, conditional
option. R3 and CGMA remain parked. The recurrence produced prospective designs
and mathematical evidence; it did not fit a candidate, generate new challenge
predictions, open challenge targets or submit an algorithm.

The incumbent remains **ALG028-V000**, submission **329774**, official adjusted
score **1.4229966461698496e-7**. The owner's observation about nearby leaderboard
scores is recorded as owner-provided context, without inferring competitors'
algorithms or changing the task's direction.

## The two decisions

| Priority | Proposed change | Why it earns a bounded attempt | Main uncertainty |
|---|---|---|---|
| **1: T124** | One 16-column anchored, cap-aware fit; retain the trace carrier and add the old DFFH discrepancy plus a physical Hermite residual | Existing 500-network F cache; under one million added inference FLOPs; old coefficients were never recalibrated for R1P | Training improvement may not transfer; the cap and existing fitted corrections can absorb or reverse a moment-level benefit |
| **2: conditional** | Replace raw trace with source-standardized covariance completion, using five matrix–vector actions | Uses existing terminal rows; no second closure or new training corpus; exact rank-one recovery and a limited Gaussian-noise theorem | Actual correlated frames and fitted composition are outside that theorem; residual-time headroom is narrow |

The first option has the stronger expected improvement per remaining hour.
Judgment ranges are about 55–75% chance of a retained official win, 4–12%
conditional gain and 45–90 minutes total for the first attempt; about 25–45%,
1–8% and 60–105 minutes for the second. These are uncertain planning priors,
not score forecasts or substitutes for the roughly 90% submission screen.
There is no requirement to build the second option after the first.

The exact designs and decision cohort are in [candidate A](CANDIDATE_A.md),
[candidate B](CANDIDATE_B.md) and [the prospective freeze](DECISION_FREEZE.json).
T124 has a 60-active-minute initial engineering budget, with a reassessment
around 30 minutes. It uses the actual Python/Whest path and an early integrated
resource check, then the declared twelve reused development networks. One
useful extension to 24 is allowed. A supported adjusted-score win should lead
promptly to packaging and official feedback, under the existing 30-minute
wait and one generic-error retry rule. No scientific funnel, arm grid or
additional large cache is prescribed.

## What the mathematics changed

The new shape feature has an exact radial construction. Subtracting the first
three Gaussian/Hermite responses from the observed ReLU mean leaves an affine
functional of already-computed raw source moments. This avoids the naive
angular standardization error in the older SRR idea and keeps the incumbent's
Gaussian closure variance. The shape coefficient may legitimately be negative:
it can remove noise already present in the frame mixture.

A target-free check on twelve predeclared F training-source rows found the two
new shape columns finite and distinct from the old fourteen-column span:
about **77.8%** and **30.2%** of their respective second moments remained after
projection. That justifies including them in one fixed fit; it is **not a score
result**. The complete design and ridge were selected before any fit.

For covariance completion, the shifted system has condition number at most
three for a PSD covariance. A fixed polynomial uses five covariance actions
with relative inverse error at most **1/1351**. The Gaussian-null variance
comparison is coordinatewise, not a dominance theorem for the complete fitted
estimator. A source variance-dispersion proxy near effective rank 53 also
weakened the earlier pre-mixing trace idea's isotropic noise argument.

The CGMA scalar seal has two counterexamples: its lower-radius transition is
wrong, and its upper-radius check can reject a feasible mixture. A corrected
constrained scalar optimum and an analytic covariance endpoint are derived.
The historical seal is preserved. Separately, an exactly ReLU-realizable
Gaussian-input example has zero skew and excess kurtosis **-.56058**: the NIG
variance–mean model cannot represent every relevant symmetric shape. General
Gaussian mixtures are more flexible. Exact
cubic matching alone therefore cannot justify the larger mixture pipeline.

## Evidence, limits and stopping point

[The scratchpad](SCRATCHPAD.md) records equations, revisions, counterexamples,
failed alternatives and cost arguments. Deterministic symbolic/synthetic checks
cover Wick covariance, radial moments, projection order, the inverse polynomial
and scalar-mixture constraints. The saved training-source geometry reads have
predeclared plans and source hashes. [The prior-work review](SOURCES.md) separates
public methods from task-specific derivations; no new academic tier is claimed.

The original R3 comparison retains useful raw evidence, but after its actual
cost is charged, its historical local projection is only about half a percent
better than historical R1P. That is not an official grade. T119A's variance
replacement and T116's marginal K4 correction remain meaningful negative
results. The new slate is designed around those findings rather than requiring
new experiments to revisit them.

Timing: **120.71 active theory minutes** after a conservative ten-minute
allowance within the 130.71-minute theory interval. Total task time to checkoff
was **138.01 minutes**, versus 135 estimated (3.01 minutes over).
Completion checks are recorded in [RESULT.json](RESULT.json).
The owner-authorized minimum is **120 active theory minutes**; idle time and
ordinary state/commit work do not count. This task stops after the theory
record and queue update. T124 is the next task, not an executed continuation.
