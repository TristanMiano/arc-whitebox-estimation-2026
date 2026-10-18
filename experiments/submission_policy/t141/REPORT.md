# T141 — compression-only C64 result

**C64 is a clear local loss; no submission was made.** ALG039-V001 reduces
compute by 47.90%, but raw MSE rises 7.98-fold and adjusted score is 4.16 times
worse. It loses all 12 comparisons. ALG038-V001 / submission 330153 remains the
official best at adjusted 1.46676758754e-8.

| Same 12 reused development networks | Incumbent | T140: C64-E | T141: C64 |
|---|---:|---:|---:|
| Raw MSE | 4.53095008665e-8 | 3.74143616657e-7 | 3.61776768946e-7 |
| Adjusted mean | 1.55952916773e-8 | 7.19308832782e-8 | 6.48787883565e-8 |
| Prediction FLOPs | 756.892B | 422.773B | 394.359B |
| Adjusted ratio to incumbent | 1 | 4.61235 | 4.16015 |

## What was tested

The registered change removes old-E persistence from T140. Rank 64, two recent
CP source blocks and 128 probe pairs per refresh from seed 139064001 remain fixed.
The core now projects only aged CP sources plus the gated old core. E contributes
to the current moment response and is then replaced by the repeated-index repair,
as in the incumbent. No coefficients, rank, seeds or source construction were
fitted or searched. [Specification](START_AND_SPEC.json) · [source identity](SOURCE_FREEZE.json).

The first integrated width 1024/depth 16 fixture passed. All 13 full-size calls
(one feasibility fixture plus 12 development rows) completed on their first
attempt, with exactly **394,359,109,358 FLOPs**, multiplier **.179333760278**.
Observed cost is 1.28% below the 399.471B forecast. Wall time was
24.81–25.87s,
residual 0.3348–0.3523s,
peak process RSS 4.854GiB and setup at most
0.03773s. Required resource checks pass. The qualified
Python 3.12 / NumPy 2.2.6 / FlopScope 0.12.0 / WhestBench 0.16.0 runtime was reused.
[Resource summary](RESOURCE_SUMMARY.json).

The unchanged core primitives have identical ASTs to T140's tested implementation.
A new complete-trajectory check compares C64 with the incumbent when rank equals
width, so compression discards no directions. Width 4 cases (depths 1,2,6) match
exactly; width 32/depth 6 differs by at most 5.36e-7. This supports the implemented
no-truncation recurrence and exercises both ordinary and fast products. It does
not establish accuracy after rank 64 truncation at width 1024. No production or
checker repair was needed. [Full-rank checks](FULL_RANK_CHECK.json) ·
[reused identities](CORE_IDENTITIES.json).

All 12 outputs were sealed before opening their targets. The single arithmetic-
mean adjusted comparison gives ratio **4.160152288**, **0/12 wins** and
bootstrap support **0.0000** over 20,000 whole-network resamples. Network ratios
span 3.3209–4.8546; median
4.2078. The 90% bootstrap interval for
mean adjusted increase is [4.691056280e-8,5.169390725e-8]. These are reused
development data, not fresh validation or a calibrated private-score probability.
No comparison extension, final blind-block access, package, upload or grader
wait followed the clear loss. [Full score](attempts/screen-sealed/SCORE.json).

## What we learned

Removing E persistence improves raw MSE by 3.31% and adjusted score by 9.80%
relative to T140, but leaves almost all of the large accuracy deficit. E
persistence is therefore **not necessary for this failure**. The compression-only
design itself fails against the incumbent. Cost feasibility and the small
no-truncation trajectory checks both pass; an unchanged rank 64 retry or nearby
parameter sweep has poor expected value.

On this panel the first three output layers match exactly, then RMS differences
grow from 8.76e-5 at layer 4 to 5.82e-4 at the final layer. The mean final change is
only -9.72e-6, so the main difference is neuron-specific rather than a uniform
mean shift. The cost savings tolerate a raw-MSE ratio of 1.9193, far short of the
observed 7.9846. [Residual description](RESIDUAL_DIAGNOSTIC.json) ·
[three-way comparison](COMPRESSION_COMPARISON.json).

T139's construction-cost estimates transferred well; its small geometry and
single-compression checks did not establish that repeated rank 64 projection at
width 1024 would preserve prediction accuracy. Those earlier tests used different
relative ranks and questions. The failed leaf is this representation and fixed
design, not every possible way to compress the history. A reopening should have
a concrete response-preserving mechanism or a diagnosed defect, not another
unmotivated rank grid or generic Tucker literature survey.

## Next recommendation

Propose **T142: one bounded Q4D implementation and submission attempt** using the
existing [mathematical handoff](../../theory/t139/Q4D_MATHEMATICAL_HANDOFF.md).
It keeps the full successful third history and extends the scalar fourth state
to coordinate trace and marginal vectors. Earlier projected cost is 814.932B,
7.67% above the incumbent, requiring about 7.12% lower raw MSE to pay for itself.
Its full recurrence and actual resource cost remain untested.

Estimate 45–75 elapsed minutes including a possible 30-minute grader wait; no
minimum. The earlier subjective planning chance remains 30% (roughly 15–45%).
This independent, already-specified option is preferable to a further generic
compression sweep. A future compression recurrence should target the moments
needed by later predictions. T142 is proposed only; no other candidate ran.

## Timing

Started 2026-09-08T19:09:27Z; decision 2026-09-08T19:18:14Z; records completed
2026-09-08T19:21:21.279027+00:00. **11.90 elapsed minutes**, versus 45–75 estimated
(-33.10 versus the lower estimate). The 13 full-size predictions total
5.51 metered minutes and overlap
other work. Rough allocation: 9.4 active implementation, analysis
and records; 2.5 minutes execution/I/O wait. No engineering extension, agents,
usage resets or official waiting. [Timing](TIMING.json).

Final verification and scoped commit preparation bring elapsed time to **13.53 minutes** at 2026-09-08T19:22:58.945900+00:00. The earlier 11.90-minute figure measures completion of the main records.
