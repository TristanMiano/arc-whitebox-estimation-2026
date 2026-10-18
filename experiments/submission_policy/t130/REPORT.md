# T130 — bounded PF1760 attempt

**Close ALG033-V000 without submission.** Its twelve-network adjusted mean
was **1.0536% worse** than ALG031, with **4/12 wins** and **.30525** whole-network
bootstrap support for improvement. Keep official **ALG031-V000 /329989** at
**1.3618567538742354e-7**. No extension, refit or count search is justified.

| Metric | PF1760 / ALG033 | ALG031 |
|---|---:|---:|
| Raw terminal MSE | 1.30228597723e-06 | 1.28870788486e-06 |
| Adjusted mean | 1.30228597723e-07 | 1.28870788486e-07 |
| Actual FLOPs |216,450,782,331|218,986,065,179|
| Multiplier |.1|.1|

The worst network ratio was **1.119260467**.
The paired90% mean-change interval was
[-3.410341e-09, 5.96129931e-09].
These are predetermined reused development networks, not independent
validation. Predictions were sealed before targets were opened. The full
per-network record is in [SCORE.json](attempts/screen-sealed/SCORE.json).

## Implementation and useful results

Main2048 and partial332 directions, radius, random streams, gamma and all
fitted coefficients were retained. The child was regenerated as a complete
1760-row normalized QR frame; pooling, trace, source fit and reconstruction
use the new counts. Partial664 signed rows occupy672 work rows, with padding
reset before every fast multiply and excluded from all statistics. The child
terminal is copied before buffer reuse. Layer0 uses the direct repeated-weight
Gram; all later covariance congruences retain their original formula.

The integrated implementation saves **2,535,282,848 FLOPs** versus ALG031,
leaving **3,451,543,224** below the discount-floor boundary. This is an actual
metered whole-candidate saving. The isolated first-Gram saving remains its
source-level accounting claim; it was not independently scored as another arm.
The gross saving funded extra child propagation, but the resulting complete
fixed-coefficient estimator lost the score comparison. This does not disprove
the ideal-law harmonic variance theorem or larger sampling counts generally.

## Bounded repairs and numerical qualification

The initial incomplete fixture used indexed assignment to reset padding,
which FlopScope disallows. Replacing it with permitted `fnp.copyto` preserved
the intended operation. No target had been accessed.

The first complete fixture had residual **.411985s**, over the .4s cap. Its
unchanged replay produced identical output and FLOPs at **.397563s**, leaving
little margin. A bounded implementation repair caches data-free workspace
views during setup. It performs the same ordered tracked operations and copies
during prediction. The public licensed kernel file is unchanged. This reduced
F0 residual to **.311658s** with **identical output bytes and charged FLOPs**.
There was no accounting change or numerical work moved into setup.

Against the same1760-child dense-partial/general-Gram reference on F0, complete
output maximum difference was **2.623e-6**, whole-output numerical MSE
**8.957e-14**, and terminal numerical MSE **2.493e-13**. The original complete-
output tolerance passes. The standalone partial output exceeded the initial
diagnostic tolerance: max **1.788e-5**, MSE **4.195e-12**, against1e-5/1e-12.
That failed diagnostic remains recorded. Its small blend weight and the
passing actual complete-output comparison justify proceeding; no historical
failure was rewritten as a pass. At reference target MSE1e-6, Cauchy bounds
the terminal numerical contribution's relative MSE change by about **.10%**
on this fixture. This is a fixture comparison, not a uniform certificate.
See [numerical review](NUMERICAL_REVIEW.json).

The final twelve production rows all passed on their first attempt:
residual **0.3011–0.3140s**,
prediction wall **18.33–19.03s**,
peak RSS **4.487 GiB**,
setup at most **0.002469s**, and identical exact cost.
Finite nonnegative full-shape output, source/coefficient identity, child buffer
and moment preservation, imports and `whest validate` pass. Unchanged fallback
source/dispatch evidence is reused. No archive qualification or upload ran
after the local loss. Python3.12/Whest0.16/FlopScope0.12/NumPy2.2.6 were reused.

## Decision, next option and time

The subjective prior for a retained official gain was35%; this outcome is not
surprising under that planning judgment. The score loss is inconclusive about
the broader mechanism, but sufficient to stop this bounded submission attempt.
Do not automatically refit the coefficients or test another child count.

**T131 / FC4S remains the recommended next task, unstarted.** Bind official
ALG031 with its original1536-child count. Its all-output fourth-plus-skew-squared
field tests a different error source, and the direct first Gram independently
funds it. The T12925% subjective win estimate remains a planning judgment;
this sampling result supplies no new shape-efficacy measurement. Reuse the
workspace-view repair if actual runtime needs it. R4IF8-P remains a reserve.

Start **2026-09-06T18:49:45+00:00**; end/checkoff **2026-09-06T19:09:49.905340+00:00**.
Elapsed **20.08 minutes**, versus **75 estimated** (-54.92).
Completed prediction meters total **4.94 minutes**
across **16 calls**, including the numerical reference.
Input loading and one incomplete prediction are additional; work overlapped
some execution. No overall engineering-budget extension or grading wait.
Final record verification and scoped commit follow checkoff.

[Specification](START_AND_SPEC.json) · [source freeze](SOURCE_FREEZE.json) ·
[decision](DECISION.json) · [result](RESULT.json) · [verification](VERIFICATION.json).
