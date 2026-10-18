# T151 — SCP-A implemented and tested; retain V29

**ALG044-V000 / H150-SCP-A loses the planned local comparison. No submission.**
Retain ALG043-V000 / submission330597, official adjusted score
**5.419051334510831e-9**. T149 remains **not tested and deferred**.

| Metric, same12 development networks | SCP-A | Incumbent V29 |
|---|---:|---:|
| Raw final-layer MSE |2.31745094686e-8|2.21745311085e-8|
| Mean adjusted score |6.10403666174e-9|5.63009302710e-9|
| Settled FLOPs |576,244,210,938|555,383,704,047|

SCP-A is **4.51% worse in raw error and 8.42% worse after compute adjustment**.
It loses both metrics on all 12 networks. Bootstrap support for a lower adjusted
mean is 0; the90% bootstrap mean-difference interval is
[4.2901e-10,5.2250e-10]. The worst network's adjusted ratio is 1.11745 and the
median is 1.08711. Each network uses its actual call multiplier, including the
first/settled lifecycle. This is reused development evidence, not a fresh blind
validation. [Full score and per-network results](attempts/screen-sealed/SCORE.json).

## What was implemented

The complete fixed SCP-A candidate changes the law used by finite cumulant
propagation to a fixed input radius while keeping an explicit physical mean
anchor. It includes the angular initial moments, radial initial third history,
oriented fourth slices, four additional native source terms, changed old-source
gate, complete birth repeated repair and physical calibration conversion.
The original public coefficients, ranks and compression objective remain fixed.
The input-radius identity preserves the exact expectation; it does not guarantee
that this finite propagation becomes more accurate.

The implementation adds one initial matrix and thin radial vectors, reusing
the existing transport and compression machinery. Actual extra settled cost is
20.86B FLOPs, within the20–30B theory forecast. Its raw error also rose, so the
loss is not just a compute penalty. [Implementation notes](IMPLEMENTATION_NOTES.md).

## What passed and what the result means

All15 full-shape calls (three lifecycle probes plus twelve comparison rows)
pass the resource checks. Residual time is 0.253–0.270s, maximum wall time 38.17s,
setup 0.030s and peak process memory5.51GiB. Repeated settled predictions are
byte-identical. Generated production source contractions agree with independent
literal tensors, including both compressed and uncompressed paths. The marginal
helper agrees with the parent's retained mean program to float32 precision;
the tested off-shape fallbacks are byte-identical at identical cost.

One generated fixture was corrected because it violated the parent's required
c1=lambda*d identity. Its failure is retained. The candidate itself required
no formula or numerical-realization repair; one frozen source was tested.
There was no fit, sweep, candidate combination or comparison extension.

This is a competitive loss for the specified approximation. It is not a failure
of the homogeneous expectation identity, nor evidence that every angular or
homogeneous closure is exhausted. We have not isolated a cause among omitted
mixed responses, changed calibration trajectories and source compression.
The modest, consistent loss supplies no reason for an ablation campaign or a
larger cohort before deciding against this unchanged candidate.

## Next recommendation

Propose **T152: H150-HGC6-A on the retained V29 parent**, the other complete
ambitious specification. It changes the layerwise cumulant representation and
adds a finite fifth/sixth response program; it does not reuse SCP-A's fixed
input-radius closure. Its calibration risk partly overlaps with SCP-A, so its
success is not independent or assured. The broad subjective T150 forecast
remains15–30% for a retained win, with10–40% adjusted gain if successful.

Revised elapsed estimate60–120 minutes uses T151's measured implementation
experience and reusable code/harness; initial60 active engineering minutes with
one concrete extension of up to30. This is a proposed task, not started.
T149/CMF2 and FAR-CT remain preserved inexpensive options.
[Proposal](NEXT_PROPOSAL.json), [current candidate status](CANDIDATE_STATUS.md).

Qualification/upload scripts were prepared while the probe ran, but no package
was created or qualified and no upload occurred. [Timing](TIMING.json) records
actual elapsed/engineering/compute time and the error against the original
120–180-minute estimate; that estimate was an allowance, not a minimum.

Measured through records: **24.03 elapsed minutes**, including
17.48 engineering/records and 6.55 unattended-compute minutes.

Through final verification: **27.13 elapsed minutes**, including
20.58 engineering/records and 6.55 unattended-compute minutes.
