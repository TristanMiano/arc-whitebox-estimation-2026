# T152 — HGC6-A tested; retain the incumbent

**ALG045-V000 / H150-HGC6-A loses decisively. No submission.** Retain
ALG043-V000 / submission330597, official adjusted **5.419051334510831e-9**.
T149 remains **not tested and deferred**.

| Same12 development networks | HGC6-A | Incumbent V29 |
|---|---:|---:|
| Raw final-layer MSE |1.87101446722e-07|2.21745311085e-08|
| Mean adjusted score |4.82136971924e-08|5.6300930271e-09|
| Settled FLOPs |563,752,761,251|555,383,704,047|

Raw error is **8.438 times** the incumbent's and adjusted error is
**8.564 times**. All12 networks lose both metrics; bootstrap
support for a lower adjusted mean is0. Individual adjusted ratios range from
6.39 to10.16. The additional compute is only **1.51%**,
so this is principally an accuracy failure. The comparison uses actual call
costs, including the first/settled lifecycle, and reused development rows.
It is local evidence, not an official grade or fresh blind validation.
[Full score](attempts/screen-sealed/SCORE.json).

## What was implemented and checked

The fixed layerwise conversion includes the guarded variance/third/fourth
state, finite fifth/sixth moment terms, physical mean anchor, changed old-source
gate, original-state physical feedback plus known injected columns, oriented
source terms, and full birth repeated repair. Public coefficients, physical
ranks and compression settings remain fixed. The extra settled8.369B FLOPs
fits the6–12B theory forecast. No local fit or parameter sweep was performed.
[Implementation notes](IMPLEMENTATION_NOTES.md).

All15 full-shape calls pass: residual time0.248–0.263s,
maximum wall time39.93s, setup0.023s and peak
process memory5.50GiB. Settled replay is byte-identical.
Actual production source contractions agree with independent literal tensors
on compressed, uncompressed and terminal paths. The actual added moment
program agrees with explicit symmetric index sums; the conversion guards and
mean/fallback checks pass. One test script's unavailable SciPy import was
replaced with elementary reference formulas. The estimator required no repair.

## Interpretation and limits

The large loss triggered a bounded integration review. No obvious mismatch
with the frozen specification was found. Saved predictions are identical at
layer1 and differ by only4.97e-8 RMS at layer2, consistent with the physical
anchor on the first changed update. Differences then accumulate from5.39e-6
at layer3 to4.21e-4 at layer16. The final MSE increase decomposes into
1.7692e-7 from the squared prediction change and -1.1994e-8 from its cross
term with the parent's error. It is not simply a common output offset.
[Saved-prediction diagnostic](SAVED_PREDICTION_DIAGNOSTIC.json).

This describes an accumulating trajectory error; it does not isolate omitted
mixed responses, the regenerated fourth-core convention, changed calibration
or compression as its cause. Passing local algebra checks cannot prove the
entire approximation faithful. The fixed HGC6-A attempt is closed; the exact
homogeneous identities and every other homogeneous closure are not disproved.
No additional networks, ablations, damping fit, package or upload were run.

## Next recommendation

Both ambitious T150 nominees now have actual negative feedback. Recommend
**T153**, a focused literature/theory recurrence giving most attention to
joint fourth-core/metric state and affordable future-response contractions,
with a bounded alternative closure. Generic homogeneous identity searching
and tuning this failed finite conversion have low immediate priority.
Keep the cheap CMF2/FAR-CT candidates saved; neither becomes automatic.
[Proposed scope and time allocation](NEXT_PROPOSAL.json),
[current candidate status](CANDIDATE_STATUS.md).

Measured through records: **24.32 elapsed minutes**, including
17.64 engineering/records and
6.68 unattended-compute minutes. The60–120-minute
estimate included possible qualification/grading and was an allowance, not a
minimum. [Timing and estimate error](TIMING.json). No further task was started.

Through final verification: **26.07 elapsed minutes**, including
19.39 engineering/records and6.68 unattended-compute minutes.
