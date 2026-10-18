# T144 — JSP implementation and official submission

**New official best: ALG041-V000 / JSP.**
Submission **330392** returned adjusted **1.18330815718e-08**, a
**19.325% reduction** versus ALG038-V001.
The local result was a **21.449% adjusted reduction**
on all 12 predetermined reused development networks.

| Measure | JSP / ALG041-V000 | ALG038-V001 |
|---|---:|---:|
| Official adjusted score | 1.18330815718e-08 | 1.46676758754e-08 |
| Official raw MSE | 3.43595788976e-08 | 4.26135243714e-08 |
| Local adjusted mean | 1.22501849244e-08 | 1.55952916773e-08 |
| Local raw MSE | 3.55715049947e-08 | 4.53095008665e-08 |
| Actual prediction FLOPs | 757,303,958,254 | 756,892,228,334 |
| Multiplier | 0.344381968832 | 0.344194735741 |

## Change and evidence

JSP retains the full successful third-cumulant history, Gaussian covariance,
analytic signed corrections and radial fourth state. It changes the fresh
paired third source using the fixed Gaussian path, incoming third, and
mean/covariance response terms derived in T143. Repeated entries are repaired
after that source change. This adds no factor columns, new dense products,
fit, random probes, damping coefficients or extra completion hop.
[Mathematical handoff](../../theory/t143/JSP_MATHEMATICAL_HANDOFF.md) ·
[Registered specification](START_AND_SPEC.json) ·
[Implementation](../../../submissions/phase2_alg041_v000/joint_source.py).

The source uses pre-activation moments in float64, before the inherited
float32 factor storage. It preserves the diagonal/tail convention and skips
the exactly zero correction at the first centered Gaussian layer. The finite
paired update includes its prescribed quadratic response terms; this result
does not establish a complete next-order approximation or identify which
individual added term drives the gain.

The source translation agrees with the direct formula to 4.44e-16. Widths 1/2
obey the full-repair invariant within 7.46e-9; the first two activation rows
match the incumbent exactly in all 12 full-size comparisons. Existing T143
mathematical and incumbent kernel checks were reused. No broad ablation suite.
[Translation/fallback checks](TRANSLATION_CHECKS.json).

Raw MSE improves 21.4922%, against only
0.05440% extra arithmetic. Adjusted bootstrap support
is 1.0000; the 90% interval for
mean score change is [-3.74827e-09,
-2.92716e-09]. Worst network ratio is
0.900093. These are reused development
networks, not fresh independent validation or a calibrated private-score
probability. Predictions were sealed before targets, with one score look,
no extension, and the final blind block untouched.
[Score and per-network records](attempts/screen-sealed/SCORE.json).

A descriptive decomposition on those same saved outputs gives squared change
8.43558e-09 and twice error/change cross term
-1.81736e-08, net raw-MSE change
-9.738e-09. The correction aligns with the prior
error; no post-score coefficient selection or additional inference run was
performed. [Saved-output diagnostic](RESIDUAL_DIAGNOSTIC.json).

## Qualification and grading

All 15 full-size calls pass, including the integrated fixture,
12 comparison networks, and two clean-extracted package replays. Runtime is
42.99–44.41s; residual time
0.37355–0.39112s; peak RSS
6.354 GiB; maximum setup 0.00691s.
One numerical realization, no repairs. The resource margin remains narrow,
but every recorded current-package check passes.

Archive `25de10fad808b8f66b11bcd363841c34a6daf518f24c040ea589aa174c98ad70` is 18,673 bytes. Manifest,
allowed imports, clean extraction, exact current-source identity, counted cost,
deterministic repeated use and affected fallback checks pass. No environment
change. [Qualification](PACKAGE_QUALIFICATION.json) · [Resources](RESOURCE_SUMMARY.json).

Submission accepted 2026-09-09T01:06:02.638Z; terminal grade observed
2026-09-09T01:33:09Z. There was one submission attempt. The owner extended this first attempt from 30 to 60 minutes
before retrying; its final deadline is 2026-09-09T02:06:02.638000+00:00. The original
deadline and monitor restart are retained in [the extension record](OWNER_WAIT_EXTENSION.json).
A valid grade receives no unchanged retry. This is an ordinary
submission, with no final-submission designation.
[Official status](SUBMISSION_330392_STATUS.json).

## Next decision and timing

T145: prospectively register E1-on-JSP as a new combined candidate, then one bounded
production/submission attempt against ALG041-V000. Keep JSP fresh source and full main
history; add exactly one completion hop from H143-E1 with its prescribed repeated-entry
repair. This is an explicit new parent/formula decision, not execution of unchanged
H143-E1 against ALG038. No age/rank/coefficient sweep. Early full-size meter, usual 12
paired reused networks, approximately 90% support; 60 active engineering minutes,
30-minute reassessment; 35–75 elapsed estimate. Actual added cost must earn its
raw-error reduction; roughly 9% projected hurdle.

This proposal follows the specific remaining memory mechanism. The original
H143-E1 hypothesis and its old-parent forecast remain historical; no E1 result
or Q4D gain is transferred to JSP. Further generic literature search currently
looks lower value than testing a concrete remaining mechanism. The broader
conditional, gauge, triangle and response-preserving compression routes stay
open for a future recurrence. T145 has not started.

Started 2026-09-09T00:48:16Z; main records completed 2026-09-09T01:33:32.243912+00:00.
**45.27 elapsed minutes**, against the 35–75-minute estimate
(+10.27 versus the lower estimate). Upload occurred after
17.78 minutes; official wait until observed
was 27.11 minutes. All local prediction
calls total 10.92 metered minutes, overlapping
preparation/recordkeeping. No exact exclusive active-time total was measured;
the 60-active-minute engineering allocation was not extended. No agents,
usage resets, fit or unrelated task execution. [Timing](TIMING.json).
