# T149 — CMF2 implemented and tested; retain V29

**ALG046-V000 / H148-CMF2 does not support a submission.** Retain
ALG043-V000 / submission330597, official adjusted **5.419051334510831e-9**.
T149 is now **tested and complete**, superseding its earlier deferred status.

| Same12 development networks | CMF2 | Incumbent V29 |
|---|---:|---:|
| Raw final-layer MSE |2.22514668376e-08|2.21745311085e-08|
| Mean adjusted score |5.69057840876e-09|5.6300930271e-09|
| Settled FLOPs |559,472,491,965|555,383,704,047|

Raw mean error is **0.347% worse**, despite8/12 raw wins.
Adjusted mean error is **1.074% worse**, with
6/12 wins and **9.16%** bootstrap
support for an improvement. Median adjusted ratio is0.999151, but the larger
ordinary losses outweigh the small wins; worst ratio1.086760. The90% bootstrap
interval for the mean adjusted difference is[-1.1363e-11,1.4223e-10].
These are reused development rows, not independent blind validation or an
official grade. Each row uses its actual call cost, including first/settled
lifecycle. [Full score and per-network evidence](attempts/screen-sealed/SCORE.json).

## Implementation and verification

The complete fixed CMF2 specification uses a two-direction conditional metric,
float64 projection statistics and its frozen numerical guard, actual row-norm
fourth diagonals, oriented fourth moment slices, canonical single-fourth
source and two columns aligned with every A/P compression regime. Existing
public coefficients, physical ranks, source-basis objectives and arithmetic
settings remain fixed. No local fit, parameter sweep, HGC/CT combination or
candidate formula repair occurred. [Implementation notes](IMPLEMENTATION_NOTES.md).

All15 full-shape calls pass resource checks and the settled replay is
byte-identical. Actual extra settled cost **4.0888B FLOPs (0.736%)**
is within the2–5B theory estimate. Residual time ranges from
0.239 to0.262s; maximum wall time
38.31s, setup0.024s and peak process
memory5.53GiB. Focused production contractions,
geometry, fourth-slice and join/nested-helper checks agree with independent
generated references. Generic fallback outputs and costs match the parent.

The sole generation issue was a mechanical syntax typo, fixed before source
freezing or numerical execution. One frozen implementation was tested. No
extra cohort, ablation campaign, package qualification or upload was performed.

## Decision and next work

The screen is a modest competitive loss, not an implementation/resource
failure or proof that every conditional metric is unhelpful. Its raw mean
also loses, so eliminating only the added compute cannot make this observed
comparison favorable. At0.09155 adjusted-win support, another cohort is poor
value for deciding whether to submit this unchanged candidate. Keep the result
and move on rather than fitting or pruning against this panel.

Recommend the proposed **T153 focused recurrence**, now informed by all three
T149/T151/T152 results. Reassess a richer metric before giving it priority;
seek useful missing joint-core or future-response information, with a distinct
conditional/observable-state alternative if it offers more upside. FAR-CT
remains untested and does not start automatically. Preserve the balance between
small opportunities and credible larger improvements.
[Updated proposal](NEXT_PROPOSAL.json), [candidate status](CANDIDATE_STATUS.md).

Through records: **20.53 elapsed minutes**, including
13.88 engineering/records and6.65
unattended-compute minutes. The60–120-minute estimate included qualification
and grading allowances; it was not a minimum. [Timing](TIMING.json).

Through final verification: **21.94 elapsed minutes**, including
15.29 engineering/records and6.65 unattended-compute minutes.
