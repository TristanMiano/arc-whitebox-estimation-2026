# Work recorded between official score improvements

Audit T159A, 2026-09-13. Through T159, the repository records **100.70 task-session hours** across **151 started tasks**. There are **41.81 explicitly recorded active research hours** within that sum, including **32.55 hours recorded as theory/derivation**. These are agent work records, not the owner's human hours or model inference-time telemetry.

The archive contains **17 successful, successively improving submissions**. The first two share one task, giving **16 time groups** below. Historical rank movements are not fully recorded, so the milestones are improvements in our official best adjusted score. The owner reports T159 reached rank 12, up five places, with the leader around 2.5e-9; those rank observations were not independently checked in this audit.

## Time to each achievement

Each row sums all recorded task sessions after the previous milestone through completion of the new submission task: theory, unsuccessful candidates, experiments, implementation, repairs, reviews, protocol work, packaging and grading waits. It does **not** subtract submission dates, include gaps between conversations, or charge all prior research to the winning algorithm's mechanism. Whole closing-task time includes final records after its grade.

| Milestone | Official adjusted score | Improvement | Tasks since previous | Recorded hours | Active research hours¹ | Cumulative hours | Local contribution/provenance |
|---|---:|---:|---:|---:|---:|---:|---|
| T075 · ALG014-V003 | 6.6072e-07 | Initial pair² | 73 | 16.39 | — | 16.39 | Local sampling combination |
| T096A · ALG015-V000 | 2.8435e-07 | 56.96% | 3 | 1.41 | — | 17.81 | Local closure/sample blend |
| T105A · ALG018-V000 | 2.6931e-07 | 5.29% | 7 | 3.79 | — | 21.60 | Local closure/fusion changes |
| T108A · ALG019-V000 | 2.3996e-07 | 10.90% | 7 | 6.32 | 2.00 | 27.92 | Local skew/fusion mechanism |
| T117A · ALG024-V000 | 1.7154e-07 | 28.51% | 11 | 14.71 | 8.00 | 42.62 | Local fitted observer |
| T118A · ALG026-V000 | 1.4792e-07 | 13.77% | 3 | 3.20 | — | 45.82 | Local composition + public kernel |
| T120B · ALG028-V000 | 1.423e-07 | 3.80% | 5 | 6.26 | 2.00 | 52.09 | Local trace correction |
| T124 · ALG029-V000 | 1.3676e-07 | 3.90% | 3 | 3.09 | 2.01 | 55.18 | Local response recalibration |
| T127 · ALG031-V000 | 1.3619e-07 | 0.42% | 3 | 3.22 | 2.01 | 58.40 | Local parity features + fit |
| T134 · ALG036-V000 | 1.3264e-07 | 2.61% | 9 | 7.17 | 3.02 | 65.57 | Adapted public features + fit |
| T135 · ALG037-V000 | 1.2858e-07 | 3.06% | 1 | 0.48 | — | 66.05 | Local refit only |
| T137 · ALG038-V000 | 1.7369e-08 | 86.49% | 2 | 3.50 | 2.00 | 69.55 | Adapted public cumulant method |
| T138 · ALG038-V001 | 1.4668e-08 | 15.55% | 2 | 1.15 | — | 70.70 | Local arithmetic changes only |
| T144 · ALG041-V000 | 1.1833e-08 | 19.33% | 7 | 8.30 | 5.51 | 79.00 | Local joint-source correction |
| T147 · ALG043-V000 | 5.4191e-09 | 54.20% | 3 | 5.25 | 3.01 | 84.26 | Unchanged public copy |
| T159 · ALG049-V000 | 5.0179e-09 | 7.40% | 12 | 16.45 | 12.26 | 100.70 | Modified public V29 |

¹ **Active research is a documented subset, not an extra amount to add.** Recent research records separate derivation, literature, empirical research and selection; older entries often record only a conservative theory minimum. A dash means no separately recorded active-research duration, not zero thinking. Ordinary engineering and diagnosis are included in the session column but are not silently relabeled active research. For example, T132's 21.34-minute literature task is in the session sum; it has no exclusive active-research stopwatch split.

² **T075 shared initial phase:** Sobol ALG003-V009 / 328477 scored 7.81113541080e-7, then Haar ALG014-V003 / 328479 scored 6.60719950258e-7, a 15.41% improvement. The shared preparation and submission phase totals 16.39 recorded hours. T075 itself records 14.81 minutes; no defensible per-submission split is available. Both grades and their shared phase are counted once in totals.

Times are rounded only for display; sums use the saved numeric records. All 36 wholly untimed tasks belong to the initial phase. T026 and T120A have partial durations. Missing time is never treated as observed zero. Because older records are incomplete and historical overlap cannot be completely ruled out, this is a sum of available sessions, not a complete reconstructed timesheet.

## What the latest interval contains

The interval from ALG043 to ALG049 is **16.45 recorded hours**, including **12.26 active research hours**, over 12 tasks. The final T158 recurrence plus T159 shipping task account for **4.98 hours**. The wider interval includes the prior recurrences, unsuccessful attempts and diagnosis that preceded the successful candidate.

| Task | Recorded session time | Recorded active research | Source |
|---|---:|---:|---|
| T148 | 3h 28m | 3h 01m | [t148](../experiments/theory/t148/REPORT.md) |
| T150 | 1h 19m | 1h 05m | [t150](../experiments/theory/t150/REPORT.md) |
| T151 | 0h 27m | — | [t151](../experiments/submission_policy/t151/REPORT.md) |
| T152 | 0h 26m | — | [t152](../experiments/submission_policy/t152/REPORT.md) |
| T149 | 0h 22m | — | [t149](../experiments/submission_policy/t149/REPORT.md) |
| T154 | 0h 12m | — | [t154](../experiments/submission_policy/t154/REPORT.md) |
| T155 | 0h 28m | — | [t155](../experiments/diagnosis/t155/REPORT.md) |
| T156 | 0h 10m | — | [t156](../experiments/protocol/t156/REPORT.md) |
| T153 | 4h 18m | 4h 09m | [t153](../experiments/theory/t153/REPORT.md) |
| T157 | 0h 18m | — | [t157](../experiments/submission_policy/t157/REPORT.md) |
| T158 | 4h 06m | 4h 00m | [t158](../experiments/theory/t158/REPORT.md) |
| T159 | 0h 53m | — | [t159](../experiments/submission_policy/t159/REPORT.md) |

T148's 27.36-minute crash/recovery exclusion is subtracted from its latest 235.28-minute verification endpoint, leaving 207.92 recorded session minutes. T149 and T153 appear in execution order: they were performed after their higher-numbered neighboring tasks.

The largest score breakthrough, T137's 86.49% improvement, followed 3.50 recorded hours since T135, including 2.00 active research hours. T147's 54.20% improvement followed 5.25 hours, including 3.01 active research hours. These contrasts show that returns have been uneven. They do not prove that earlier failed research had no value or that any given research duration predicts a gain.

## Coverage and accounting

- Reuse the earlier [T128A task census](../experiments/protocol/t128a/TASK_AUDIT.csv): 116 tasks, 80 with some duration, 59.24 recorded hours. Add 35 later tasks with recorded time. Final coverage is 115/151 tasks with some timing, including two partial records; 36 have none.
- Order by the saved experiment event sequence, checked against the task history where numbering diverges. For example, T102 preceded the first T075 submissions, while T099 followed T105A. Every task is assigned to one milestone group. Grouped historical events do not become extra tasks.
- Use the latest explicitly measured task endpoint where available. Later verification/commit-preparation durations replace earlier snapshots; they are not added as whole new sessions. This explains small differences from older summary tables that stopped at initial checkoff.
- Preserve prior pause adjustments: T026's known completion segment only; T095's two work sessions; T105A excluding the owner pause; T113 excluding the restart gap; T120A's initial audit only. Subtract T148's explicitly excluded crash/recovery interval. Unknown preliminary work, final delivery beyond the saved endpoint, and unrecorded conversation turns remain missing.
- T129 also records **4.75 overlapping sub-agent person-hours**, excluded from session and root-research totals. Adding them gives **46.56 recorded active research person-hours** across root and agents, not 46.56 elapsed hours. Fable/Opus and other imported contributions have no comparable complete duration record in this audit; no duration is invented for them.
- Seven pre-numbered P events have no recorded task-session duration. E120's visualization-repair follow-up also has no captured start/duration; it is flagged separately, not counted as a second T128A task.
- Grading and numerical execution occur inside task sessions and can overlap reading or recordkeeping. Prediction meters, wait windows and agent durations are never added on top of sessions. We cannot recover pure model thinking time by subtracting these overlapping fields.
- The current T159A audit is excluded: it happened after the latest achievement. The proposed T160 remains unstarted.

## Degree of copying versus local contribution

These are **provenance labels**, not a verdict that an idea is unpublished. A local implementation of Sobol, Haar sampling, Hermite closure or Winograd multiplication does not invent those methods. A fit-only successor is distinguished from a changed recurrence. Historical N1 labels are retained in their original records, but this audit does not elevate them into verified academic novelty.

**ALG043 is the clear unchanged-public-code case. ALG049 is a modified V29 derivative.** ALG038 was also based on a published cumulant method, but with a materially different local compressed recurrence. ALG036 borrowed a specific public feature vocabulary and refitted it in our estimator. The earlier lineage consists mainly of local implementations/combinations and subsequent corrections or calibration, using established/public ingredients.

Here “local” includes this repository's contributors, including Sol, Astra and relevant imported Fable/Opus ideas; it does not allocate authorship by model or claim every ingredient was ours. Those external contributions retain their attribution in the [strategy map](RESEARCH_STRATEGY_MAP.md#attribution-and-reproducibility). No new literature priority audit was performed.

| Algorithm | Degree/type of local contribution | What was inherited and what we changed | Evidence |
|---|---|---|---|
| ALG003-V009 | Known baseline | Standard Sobol sampling, stored point bank, radial normalization and current-shape/API translation. Local implementation/packaging; no new estimator principle claimed. | [Source 1](../state/algorithm_specs/ALG003-V009.json) |
| ALG014-V003 | Local sampling combination | Haar-Stiefel/QR frames, antipodal pairing, mean-chi radius, exact first layer and budget-sized frame schedule. Established tools combined and implemented here; not an unchanged public challenge submission. | [Source 1](../state/algorithm_specs/ALG014-V003.json) [Source 2](../submissions/phase2_alg014_v003/README.md) |
| ALG015-V000 | Local closure/sample blend | One Haar frame blended 0.25/0.75 with the bundled full-covariance closure. The project contribution is the concrete cost-aware composition; shrinkage and Gaussian closure are known. | [Source 1](../state/algorithm_specs/ALG015-V000.json) [Source 2](../submissions/phase2_alg015_v000/README.md) |
| ALG018-V000 | Local closure/fusion changes | Order-12 Price/Hermite closure plus an independent partial-Haar arm and fixed fusion weights. A locally developed allocation and combination of known tools. | [Source 1](../state/algorithm_specs/ALG018-V000.json) [Source 2](../submissions/phase2_alg018_v000/README.md) |
| ALG019-V000 | Local skew/fusion mechanism | Harmonic-shrunk terminal skew/Edgeworth correction, alpha-stratified fusion and nested partial extension. The source registry calls this OURS, while its sampling and closure lineage uses established ingredients. | [Source 1](../state/algorithm_specs/ALG019-V000.json) |
| ALG024-V000 | Local fitted observer | A 12-feature analytic-synthesis observer, locally fitted coefficients, correction cap and output projection over ALG019. Public/known numerical ingredients remain inherited. | [Source 1](../state/algorithm_specs/ALG024-V000.json) [Source 2](../submissions/phase2_alg024_v000/README.md) |
| ALG026-V000 | Local composition + public kernel | Combines a public MIT fast multiplication kernel with an independent child frame, cross-frame harmonic reliability and the fitted analytic observer. Substantive local composition; multiplication algorithm is public. | [Source 1](../state/algorithm_specs/ALG026-V000.json) [Source 2](../submissions/phase2_alg026_v000/README.md) |
| ALG028-V000 | Local trace correction | Replaces the terminal harmonic-skew correction with a radial-law-corrected physical third-cumulant trace projection; retains the existing observer coefficients. A local mathematical adaptation, not a new fit. | [Source 1](../state/algorithm_specs/ALG028-V000.json) [Source 2](../experiments/submission_policy/t120b/REPORT.md) |
| ALG029-V000 | Local response recalibration | Cap-aware anchored physical-response recalibration with a fixed Hermite remainder, followed by a local coefficient fit. Incremental response/calibration work on ALG028. | [Source 1](../state/algorithm_specs/ALG029-V000.json) [Source 2](../experiments/submission_policy/t124/REPORT.md) |
| ALG031-V000 | Local parity features + fit | Parity-split physical response features and a fitted correction on ALG029. A local extension and recalibration of the inherited estimator. | [Source 1](../state/algorithm_specs/ALG031-V000.json) [Source 2](../experiments/submission_policy/t127/REPORT.md) |
| ALG036-V000 | Adapted public features + fit | Transfers the five absolute-state calibration features from venture_agent_ai public work into our own ALG031 state, with our coefficients fitted locally. Neither a wholly local feature invention nor a copied complete estimator. | [Source 1](../state/algorithm_specs/ALG036-V000.json) [Source 2](../experiments/submission_policy/t134/REPORT.md) |
| ALG037-V000 | Local refit only | One joint regularized refit of the existing 27 correction columns. No new feature vocabulary, sampling rule or recurrence; inherits the local/public mixture of ALG036. | [Source 1](../state/algorithm_specs/ALG037-V000.json) [Source 2](../experiments/submission_policy/t135/REPORT.md) |
| ALG038-V000 | Adapted public cumulant method | Public joint-cumulant framework rebuilt as our paired compressed full-history recurrence, with repeated-index completion, radial fourth scalar and signed mean/covariance response. Reuses public fast multiplication. No local fit; not an exact implementation of the full published method. | [Source 1](../experiments/theory/t136/REPORT.md) [Source 2](../experiments/theory/t136/CANDIDATE_A.md) [Source 3](../submissions/phase2_alg038_v000/README.md) |
| ALG038-V001 | Local arithmetic changes only | Retains ALG038-V000 state and recurrence; uses final marginal contractions and a four-level multiplication schedule. The fresh contribution is lower cost, not a new statistical mechanism. | [Source 1](../state/algorithm_specs/ALG038-V001.json) [Source 2](../experiments/submission_policy/t138/REPORT.md) |
| ALG041-V000 | Local joint-source correction | Adds the locally derived/implemented JSP fresh-source joint response to ALG038-V001 and recomputes repeated-entry completion. No local fit. Related cumulant-response ideas are published; this record does not establish academic priority. | [Source 1](../state/algorithm_specs/ALG041-V000.json) [Source 2](../experiments/submission_policy/t144/REPORT.md) [Source 3](../experiments/theory/t143/JSP_MATHEMATICAL_HANDOFF.md) |
| ALG043-V000 | Unchanged public copy | 504aldo public V29 at commit18c17e2d7a9aeacd399cfc2c6b571e4e16dbfb45, numerical source byte-identical. Published terms, fitted tables, defaults and schedules unchanged. Only packaging, qualification and harness work were ours. | [Source 1](../state/algorithm_specs/ALG043-V000.json) [Source 2](../experiments/submission_policy/t147/REPORT.md) [Source 3](../experiments/submission_policy/t147/ATTRIBUTION.md) |
| ALG049-V000 | Modified public V29 | Starts from public V29 and adds the coupled native history basis, covariance-cup compensation for lost third-tensor trace, ranks320/192 and Winograd/shared-arena arithmetic. Inherits V29 calibration and core machinery; no new fit. The Winograd algorithm itself is established. | [Source 1](../state/algorithm_specs/ALG049-V000.json) [Source 2](../submissions/phase2_alg049_v000/README.md) [Source 3](../experiments/submission_policy/t159/REPORT.md) |

## All official receipts

| Task | Algorithm | Submission | Adjusted score | Saved evidence |
|---|---|---:|---:|---|
| T075 | ALG003-V009 | 328477 | 7.8111354108e-07 | [Receipt/result](../experiments/submission_policy/t075/RESULT.json) |
| T075 | ALG014-V003 | 328479 | 6.60719950258e-07 | [Receipt/result](../experiments/submission_policy/t075/RESULT.json) |
| T096A | ALG015-V000 | 328500 | 2.84353817506e-07 | [Receipt/result](../experiments/submission_policy/t096a/RESULT.json) |
| T105A | ALG018-V000 | 328686 | 2.69314724164e-07 | [Receipt/result](../experiments/submission_policy/t105a/RESULT.json) |
| T108A | ALG019-V000 | 328762 | 2.39959831788e-07 | [Receipt/result](../experiments/submission_policy/t108a/RESULT.json) |
| T117A | ALG024-V000 | 329529 | 1.71538296854e-07 | [Receipt/result](../experiments/submission_policy/t117a/RESULT.json) |
| T118A | ALG026-V000 | 329690 | 1.47916588048e-07 | [Receipt/result](../experiments/submission_policy/t118a/RESULT.json) |
| T120B | ALG028-V000 | 329774 | 1.42299664617e-07 | [Receipt/result](../experiments/submission_policy/t120b/RESULT.json) |
| T124 | ALG029-V000 | 329806 | 1.36755548851e-07 | [Receipt/result](../experiments/submission_policy/t124/RESULT.json) |
| T127 | ALG031-V000 | 329989 | 1.36185675387e-07 | [Receipt/result](../experiments/submission_policy/t127/RESULT.json) |
| T134 | ALG036-V000 | 330097 | 1.32636576382e-07 | [Receipt/result](../experiments/submission_policy/t134/RESULT.json) |
| T135 | ALG037-V000 | 330101 | 1.28580467731e-07 | [Receipt/result](../experiments/submission_policy/t135/RESULT.json) |
| T137 | ALG038-V000 | 330141 | 1.73692836098e-08 | [Receipt/result](../experiments/submission_policy/t137/RESULT.json) |
| T138 | ALG038-V001 | 330153 | 1.46676758754e-08 | [Receipt/result](../experiments/submission_policy/t138/RESULT.json) |
| T144 | ALG041-V000 | 330392 | 1.18330815718e-08 | [Receipt/result](../experiments/submission_policy/t144/RESULT.json) |
| T147 | ALG043-V000 | 330597 | 5.41905133451e-09 | [Receipt/result](../experiments/submission_policy/t147/RESULT.json) |
| T159 | ALG049-V000 | 330887 | 5.01785974707e-09 | [Receipt/result](../experiments/submission_policy/t159/RESULT.json) |

## Reproducible data

[Task-level CSV](../experiments/analysis/t159a/TASKS.csv) lists every included task, time field/source, timing limitations and milestone assignment. [Milestone CSV](../experiments/analysis/t159a/MILESTONES.csv) and [structured milestones](../experiments/analysis/t159a/MILESTONES.json) contain unrounded sums. [Source hashes](../experiments/analysis/t159a/SOURCE_MANIFEST.json) identify the read inputs, including the frozen event metadata used for ordering. [Build script](../experiments/analysis/t159a/build_audit.py) reproduces the aggregation from those records; [report script](../experiments/analysis/t159a/build_report.py) renders this document. No estimator, target arrays, external service or new experiment was used.
