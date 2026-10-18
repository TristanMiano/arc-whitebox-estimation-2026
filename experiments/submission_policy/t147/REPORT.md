# T147 — unchanged public V29 reproduction and submission

**New official best: ALG043-V000, unchanged 504aldo public V29.**
Submission **330597** returned adjusted **5.41905133451e-09**, a
**54.204% reduction** versus JSP / ALG041-V000.

| Measure | Public V29 reproduction | JSP incumbent |
|---|---:|---:|
| Official adjusted score | 5.41905133451e-09 | 1.18330815718e-08 |
| Official raw MSE | 2.13274181249e-08 | 3.43595788976e-08 |
| Local adjusted mean | 5.6300930271e-09 | 1.22501849244e-08 |
| Local raw MSE | 2.21745311085e-08 | 3.55715049947e-08 |
| Local first-call FLOPs | 587,262,754,287 | 757,303,958,254 |
| Local second-call FLOPs (first depth-5 call) | 558,473,140,719 | 757,303,958,254 |
| Local later-call FLOPs | 555,383,704,047 | 757,303,958,254 |

## What changed

The submission source is byte-for-byte public `estimator_v29.py` at commit
`18c17e2d7a9aeacd399cfc2c6b571e4e16dbfb45`, renamed for the submission API.
All mathematical terms, author-fitted tables, defaults, source compression
and multiplication schedules are inherited. **We added no algorithmic
adaptations and did no local fitting.** The MIT license is included.
[Attribution](ATTRIBUTION.md) · [Registration](START_AND_SPEC.json).

V29 brings structured fourth-cumulant regeneration, richer source feedback,
age-dependent shared source bases and cheaper batched matrix products together.
The comparison measures their combined effect; it does not isolate any one
mechanism. Official raw MSE improves 37.93%, while the effective
ratio of adjusted to raw score is 0.25408848, versus
0.34438960 for JSP. That aggregate
ratio is descriptive, not a claim of constant per-network official FLOPs.

## Local evidence and resource checks

The single predetermined comparison uses 12 reused development networks,
with predictions sealed before target access. V29 wins adjusted score on
12/12; the adjusted mean improves 54.04%,
and raw MSE improves 37.66%. Whole-network bootstrap support is
1.0000. The 90% mean-change
interval is [-7.144658561722497e-09, -6.09027508989613e-09]. This is development
evidence, not an independent scientific validation or a calibrated leaderboard
success probability. No extension, coefficient selection or blind-block access.
[Per-network scores](attempts/screen-sealed/SCORE.json).

A fresh estimator serves the comparison sequentially. Its first call uses the
published depth-4 schedule; later calls use depth 5. Actual row-specific costs
are used in scoring, including pool allocation on the first depth-5 call. First versus steady float32 outputs differ slightly;
repeated steady outputs and clean-package matching lifecycles are bit-identical.
No private call-counter edits or uncharged full-size warmup are used.

The first harness exceeded 8 GiB while rereading whole parquet shards beside
persistent estimator pools. Separate target-free input extraction removes that
loader overhead. First and second predictions and FLOP counts remain identical;
no estimator source repair was necessary. The failed run is retained.
[Memory review](HARNESS_MEMORY_REVIEW.json).

All 18 calls with the corrected loader pass: wall time
25.12–34.20s, residual
0.18615–0.20987s, peak RSS
5.475 GiB, setup at most 0.02243s.
There are 20 completed calls including
the two original-loader calls. Generated small/odd shapes, import/API audit,
archive manifest and exact lifecycle replay pass. The source's standard-library
uses are named configuration reads and garbage-collection control; all numerical
work uses permitted tracked APIs. [Resources](RESOURCE_SUMMARY.json) ·
[Package qualification](PACKAGE_QUALIFICATION.json).

An extra width-2 check found a division-by-zero in the public `_statics`
coefficient. This known limitation is outside the fixed 1024×16 competition
shape. It is retained and documented; we claim only the actual competition
and representative passing fallback checks, not universal shape support.
The unchanged source was not patched for this unrelated case.
[Width-2 limitation](WIDTH2_LIMITATION.json).

## Official result, timing and next decision

Archive SHA-256: `fdf4b3bf4f0cf0a0cabeefb42fca39985123a0ad636eb750ad7bafa963a7717f`.
Accepted 2026-09-11T01:55:05.162Z; terminal grade observed
2026-09-11T02:38:01Z. There was one submission
attempt. The owner extended this round's allowance from 30 to
60 minutes per attempt, retaining the original
acceptance time. The monitor resumed with the same ID and preserved event history.
[Wait extension](OWNER_WAIT_EXTENSION.json).
[Official status](SUBMISSION_330597_STATUS.json). No final-submission designation.

The owner also asked whether this was the strongest published method we had
found. A brief current-source and leaderboard check found no stronger released
Phase 2 implementation; stronger leaderboard entries do exist. This is a scoped
search result, not a universal claim. [Availability check](PUBLIC_AVAILABILITY_CHECK.md).

Focused literature/theory recurrence on the stronger V29 baseline. First identify which
joint-source and fourth-response terms its published equations already contain; then
derive one coherent omitted response without double counting. Prioritize a cheap
paired-fourth or conditional-source correction native to V29, keeping
response-equivalent homogeneous state as a larger-upside reserve. Re-rank HGC using the
actual cost hurdle; do not automatically port JSP, E1 or Q4D or sweep existing
ranks/coefficients. Proposed floors: 120 minutes written derivation, 30 focused adjacent
literature, 30 candidate selection; estimate 180–220 elapsed minutes, with productive
continuation allowed. A cheap candidate may be saved while a credible larger-gain thread
is developed. No new task, candidate execution or agents start automatically.

[Reserve re-ranking and proposed T148](NEXT_PROPOSAL.json). T148 has not started.

Started 2026-09-11T01:33:49Z; records completed 2026-09-11T02:38:09.926331+00:00.
Elapsed **64.35 minutes** against 45–90 estimated. Upload after
21.27 minutes; grading wait until observed
42.93 minutes. Prediction calls total
10.46 metered minutes, overlapping other work.
No engineering-budget extension, subagents or usage resets. [Timing](TIMING.json).

Final source, archive, prediction seals and live-state verification completed
2026-09-11T02:40:46.283533+00:00, **66.95 elapsed minutes**
from start. [Verification](FINAL_VERIFICATION.json).
