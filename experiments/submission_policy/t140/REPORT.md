# T140 — C64-E production result

**C64-E is a clear local loss; no submission was made.** The fixed candidate
ALG039-V000 uses 44.14% fewer FLOPs, but its raw MSE is 8.26 times the incumbent's.
Its adjusted score is 4.61 times worse, with 0/12 network wins. The official best
remains ALG038-V001, submission 330153, adjusted 1.46676758754e-8.

| Measured quantity | C64-E / ALG039-V000 | Incumbent / ALG038-V001 |
|---|---:|---:|
| Paired local raw MSE | 3.74143616657e-7 | 4.53095008665e-8 |
| Paired local adjusted mean | 7.19308832782e-8 | 1.55952916773e-8 |
| Prediction FLOPs | 422,772,641,518 | 756,892,228,334 |
| Adjusted multiplier | .192254738758 | .344194735741 |

## Implementation and evidence

Implemented the frozen T139 handoff: two recent CP source blocks, a symmetric
rank 64 core,128 bilinear Gaussian probe pairs per refresh from fixed seed 139064001,
and projected transport of the old modeled E. The first two source steps and
Gaussian/fourth-scalar responses retain the incumbent design. The final layer
uses marginal contractions. Core operations use counted direct products; the
large matrix products reuse the qualified public kernel. There was no fitting,
seed search, rank sweep, formula revision or production repair.

The first integrated width1024/depth16 fixture passed all resource checks,
with cost 1.22% below the 427.998B forecast. Thirteen full-size predictions
(one feasibility fixture plus the 12 fixed development networks) used 24.75–25.87s
wall, .3369–.3616s residual, at most 4.840GiB process RSS and .03683s setup.
All completed on the first attempt. The runtime is the qualified Python 3.12,
NumPy 2.2.6, FlopScope 0.12.0 and WhestBench 0.16.0 environment.
[Resources](RESOURCE_SUMMARY.json) · [source freeze](SOURCE_FREEZE.json).

Seven small generated-reference checks cover packed repeated/marginal
contractions, both sketches, both projections and full-rank compression with
old E. Their scaled errors are below 1.76e-6. One checker initially attempted
unsupported indexed assignment; its failed version/log are retained and its
synthetic-input preparation was repaired. Candidate code was unaffected.
These checks support implementation correctness; they do not establish accuracy
against challenge targets. [Identities](CORE_IDENTITIES.json) · [repair note](REPAIRS.md).

All 12 candidate predictions were saved and sealed before reading their targets.
They reuse the declared development cohort and saved incumbent predictions;
this is not independent validation. Actual arithmetic-mean adjusted ratio is
**4.612346134**, with bootstrap support for improvement **0.0000** over 20,000
whole-network resamples. Network ratios range 3.7547–5.2605; the median is 4.7620.
The 90% bootstrap interval for the adjusted mean increase is
[5.383870948e-8,5.899533543e-8]. There was one score look, no extension, and no
final blind-block access. [Score and per-network results](attempts/screen-sealed/SCORE.json).

## What this rules out, and what it leaves open

The combined C64-E design is not worth submitting unchanged. Cost was not the
problem: its savings could tolerate a raw-MSE ratio of 1.7903, far below the
observed 8.2575. Resource feasibility is now measured, not just forecast.

Outputs match the incumbent exactly through the first three layers on all 12
networks. The RMS difference then grows from 8.78e-5 at layer 4 to 5.84e-4 at the
final layer. The average final difference is only 5.70e-6 and about 47.6% of
coordinates move upward, so this is mostly neuron-specific error, not a uniform
mean offset. The exact MSE decomposition attributes 3.4161e-7 to the squared
output change, offset by a small favorable cross term of -1.2772e-8 with the
incumbent residual. [Descriptive diagnostic](RESIDUAL_DIAGNOSTIC.json).

This result does **not** separate repeated compression from persisting the old
modeled remainder. The latter was an accuracy hypothesis, not a known true
cumulant. The earlier small single-compression checks did not exercise this
combined recurrent mechanism. Possible explanations include harmful E
persistence, lost components under recurring projection, or incomplete
cancellation between retained recent sources and projected E. None is isolated
by this screen. A rank sweep or an unchanged official upload would be poor value.

## Recommended next task

Propose **T141: one bounded compression-only C64 attempt**, the fallback already
recorded in T139. Keep rank 64/recent 2, but project only aged CP sources and the
old core; retain the incumbent's ephemeral E treatment. Reuse this implementation,
contracts and dense checks where applicable. Register it as a separate variant,
remeasure the full-size cost, and use the same lean score decision before an
otherwise-authorized upload. Its earlier 399.471B cost forecast remains a
projection; its full recurrent accuracy is untested.

Estimate **45–75 elapsed minutes**, including a possible 30-minute grader wait;
no minimum. A rough planning win chance is **40% (25–55%)**, an explicitly
subjective prioritization estimate, not a private-score probability or a new
submission threshold. This cheaper, more incumbent-like variant is preferable
as the next task to a generic literature re-survey. Q4D remains a separate
accuracy option; it has not run. T141 is proposed only.

No archive was created, no qualification replay or upload was performed, and
there is no grader wait. Conditional qualification scripts were prepared but
never executed after the negative score. Source hashes and the prediction seal
identify the tested design. The bounded attempt is complete. No agents or
usage resets were used. Timing and the scoped commit complete the record below.


## Timing

Started 2026-09-08T18:49:14Z; score decision 2026-09-08T19:03:54Z; records completed 2026-09-08T19:06:44.020826+00:00. **17.50 elapsed minutes**, versus 100–130 estimated (-82.50 versus the lower estimate). The 13 prediction calls total 5.48 metered minutes and overlap other work. Rough allocation: 14.5 active implementation/analysis/records, 3.0 unattended execution/I/O wait; no official wait. No engineering-budget extension was needed. [Timing](TIMING.json).

Final verification and scoped commit preparation bring elapsed time to **19.48 minutes** at 2026-09-08T19:08:42.853925+00:00. The17.50-minute figure above is the earlier record completion.
