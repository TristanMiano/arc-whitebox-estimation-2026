# T172 — final broad, score-focused recurrence

Completed **252.69 active work minutes** (296.74 elapsed), with **3 official improvements**. Retain **ALG058-V001 / 336809**, adjusted **2.97110640613e-09**, **28.50% below the starting score**.

The owner authorized unrestricted research allocation within ARC rules and a
four-hour work floor. Timing includes experimental and submission work; it is
not four hours of exclusive derivation. No final nomination was made.

## Official results

| Algorithm | Official submission | Adjusted score | Raw final MSE | Outcome |
|---|---:|---:|---:|---|
| Starting ALG053 | 335391 | 4.15561726455e-09 | 2.01271731015e-08 | Starting incumbent |
| ALG054-V000 | 336778 | 3.03329104712e-09 | 1.98937605589e-08 | 27.01% better than previous best |
| ALG055-V000 | 336785 | 2.98282232784e-09 | 1.95308695794e-08 | 1.66% better than previous best |
| ALG058-V001 | 336809 | 2.97110640613e-09 | 1.94467643766e-08 | 0.39% better than previous best |

**ALG058-V001 remains best, 28.50% below the starting adjusted score.** Most of the gain came from reducing arithmetic while preserving accuracy.

The lower-cost physical engine is the public LordProcciuto/504aldo work.
ALG054 combines it with our previously developed 32-field, 96-coefficient
covariance correction and a new exact regrouping of that correction's
arithmetic. ALG055 adds our newly fitted, trace-informed local mean source. ALG058-V001
then averages that source equally with the 64-network contextual source, using
a single batched evaluation that preserves both models' normalization.
On the same four development networks under the current runtime, the public
engine alone scores 3.22335e-9; our covariance version scores 3.10976e-9,
and the added mean source scores 3.08614e-9. Those are development comparisons,
not additional official grades.

![Same-input cost and accuracy comparison](NATIVE_FRONTIER.png)

All three submitted archives passed the package, fallback, full-shape resource
and repeated-input byte-replay checks. The official records and exact archive
identities are in [ALG054](candidates/ALG054-V000/OFFICIAL_RESULT.json),
[ALG055](candidates/ALG055-V000/OFFICIAL_RESULT.json), and
[ALG058-V001](candidates/ALG058-V001/OFFICIAL_RESULT.json). No final designation has
been made.

## What the larger physics work established

The fuller third/fourth-cumulant equations with coordinated scale extraction
have real accuracy capacity. In the initial two-network research comparison,
raw error falls from 1.665e-8 without extraction to 1.148e-8 with it when third
history is retained. Cheap substitutes repeatedly lose important information.
Cutting history to three, five or seven layers fails; matching the scale
counterterm's age does not repair that loss. Reserving a third-trace component
helps, but remains far behind the fuller model.

Several derivations reduce the implementation gap:

- Three current third-birth pairs collapse into one algebraic pair. Only its
  extra factor requires compression. Small-chain agreement is about 1e-15.
  Folding the scale counterterm into the birth and repeated-index residual
  preserves nearly the same two-network accuracy.
- Existing third-tensor factors can answer a directional matrix query without
  materializing a cubic tensor. A rank-96 reader retained the full reader's
  raw accuracy within about 3% in its initial two-network comparison.
- With a purely repeated-index approximation for old third moments, the old
  reader's terms in fourth-core production cancel exactly. The newborn
  contribution remains. This corrects an earlier age-slicing experiment that
  did not faithfully reproduce the public newborn-only approximation.
- Except for one covariance-triangle term, fourth-core production can be
  represented by elementwise matrices and factored products, and queried on a
  narrow sketch. Independent identities agree at about 1e-15. The full old
  third action can also be included directly in that sketch.

The compact research prototypes are **not qualified submissions**. On F rows
0 and 499, the rank-32 version with the cheap old reader gives 1.508e-8 raw;
including the full old-third action gives 1.431e-8. The native fast parent is
about 1.78e-8 on those rows. Added arithmetic and native history-compression
error can consume those 15–20% raw gains. Rank-8/16 versions lose much of the
benefit. No complete native implementation was shown to beat adjusted score.

A late actual-meter kernel check sharpened that cost concern. The literal
rank 32, power-one compression costs9.16B FLOPs per full-width layer, and its
exact diagonal-remainder transport costs2.29B. Fifteen steady stages would
add171.7B, about50.8% of the current parent's whole-model compute, against an
approximately 15.2% two-network raw gain (only18.0% extra compute can break
even). Rank 16/no-power and rank 8/power versions project about20% extra compute
for smaller raw gains. These are shape-cost projections, **not integrated
scores or lower bounds**: first/final stages, pruning and shared algebra can
save work; producer formation and extra feedback would add work. A direct
port is therefore poorly justified without another substantial cost reduction.
[Measured kernel costs](P80_G_COST.json), [interpretation](P80_COST_INTERPRETATION.json).

A useful negative result is that a diagonal fourth-core residual cannot simply
be transported to its next diagonal: the off-diagonal part of
`W diag(d) W^T` matters. A cheap 18-field regression explains roughly two-thirds
of the teacher core's matrix variation but loses most of its final-mean gain.
Scalar-only fourth-core feedback fails more severely.

## Direct empirical improvements and losses

Earlier mean corrections did not transfer cleanly to the cheaper physical
trajectory. Directly attaching the older fitted mean/neural corrections gave
four-network adjusted scores around3.40–3.53e-9, versus 3.22e-9 for the public
engine alone. The physical covariance dictionary transferred successfully,
but the useful mean source had to be fitted on the new trajectory. Some early
versions also exceeded the local residual-time cap; those failures remain
recorded separately from their accuracy losses.

All ratios below are conditional or adaptive research evidence. They are not
private-suite probabilities.

| Experiment | Evidence | Outcome |
|---|---|---|
| Refit all 96 physical covariance coefficients on the new trajectory | 32-network conditional response CV | Loses: ratios 1.0154 / 1.0194 for the two fixed objectives |
| Refit 108 coefficients, including global radial/trace fields | Same conditional response model | Loses: 1.0104 / 1.0145 |
| Freeze the existing 96 and fit only 12 global additions | CV ratio 0.99238; then actual estimator pilot | Small screening signal, but actual version loses to context alone |
| Increase learned source width from 32 to 128 | CV ratio 0.97056 versus 0.97486 for trace24 | Small benefit; context was more informative |
| Add network means of the 24 local features | CV ratio 0.96272, 31/32 wins | Promising pilot; half-physical variant loses the larger comparison below |
| Add eight signed correlation messages | CV 0.96263; actual four-network adjusted ratio 1.00064 versus ALG055 | No native gain |
| Warm-start context model with terminal-error training | CV 0.96921; actual adjusted ratio 1.00781 | Better training fit did not generalize |
| Four structural history reallocations | Four actual networks each | All lose; stronger oldest-history compression is especially damaging |

The structural tests changed early/late compression, the oldest basis and a
feedback/residual allocation. Their failures support retaining the current
history representation, not a universal claim that compression is exhausted.

ALG056, the contextual source with half of its correction fed into the physical
mean, improved the four-network pilot by 1.08%. Its full twelve-network result
was **0.53% worse than ALG055**, with only 5/12 wins and bootstrap support
0.17136. Archive/resource/replay checks passed. It was **not uploaded**.
The exact result is preserved in [ALG056](candidates/ALG056-V000/RESULT.json).
The shadow-only context32 model was not given a twelve-network package comparison.
Nearby physical-sharing variants were too similar to justify another package
comparison after this reversal.

## A late fourth-moment query, and its repaired limitation

For a fixed symmetric third tensor, two-equal slices in an invertible query
basis recover a third-leg query by a linear solve. This exact identity does
not recover general all-distinct tensor entries.

The first application to the fast engine was flawed: its moment capture had
already zeroed pruned-neuron rows and columns, but the reconstruction treated
it as a complete basis. Large sensitivity to weak singular directions exposed
the problem. A matched-filter inverse approximation did not improve the score.

A subsequent retained-basis projection uses only the available moment entries
and stabilizes the query. Independent small tests verify both that projection
identity and the leading mixed-third/Gaussian fourth-birth polynomial. The
actual native tensor contains additional terms, and projection discards part
of the requested direction; this remains an approximate readout.

The repaired three- and seven-layer versions still lose to the simpler context
model before charging their additional dense products. These versions are
closed for this round. The [scratchpad](SCRATCHPAD.md) preserves the equations,
interface correction and conditions that a future version would need to meet.

## Expanded-data check

P65 acquired32 additional public training trajectories and refitted four fixed
source families on 64 networks. The original32-network models were first tested
on the additional trajectories: trace24 had raw ratio0.96352 versus P09,
context48 had0.97856, and graph64 had0.97751. The original context advantage
did not generalize to those inputs. Network-wide conditioning has fewer
independent examples than the large neuron count might suggest; that is a
plausible explanation, not a demonstrated causal attribution.

|64-network recipe | Conditional cross-validation raw ratio to P09 | Wins |
|---|---:|---:|
| trace24, four depth heads |0.971506 |55/64 |
| context48 |0.967520 |56/64 |
| graph64 |0.981118 |46/64 |
| trace24, fifteen depth heads |0.971607 |58/64 |
| Equal trace/context average |0.966506 | — |
| Equal trace/context/graph average |0.964234 | — |

The fixed three-source average was selected for one native check. Its hidden
units can be merged algebraically into a single 96-unit model without fitted
mixture weights. A synthetic float32 check agrees with separate source
averaging within 5.96e-7. These screening results required actual estimator comparisons;
the offline average also clips at a different point.

The actual four-network results are:

| Late native variant | Adjusted change versus ALG055 | Wins |
|---|---:|---:|
| Rank 384 oldest basis |1.43% worse |0/4 |
| trace24,64 training networks |0.57% worse |0/4 |
| context48,64 training networks |0.28% better |2/4 |
| graph64,64 training networks |1.82% worse |0/4 |
| Separate depth heads |2.06% worse |1/4 |
| Equal three-source average |0.52% worse |1/4 |

All passed the pilot resource caps. Context64 was frozen as ALG057. Its twelve-network package comparison was
essentially tied:0.014% better,6/12 wins, bootstrap support 0.5212. It was not
uploaded. Archive, resources and byte replay passed. The richer-model CV gains
were unreliable guides to actual development improvement in this round.

The P81 fixed equal average of the incumbent and context64 was initially kept
as a screen-only reserve. After the full twelve-network contextual comparison,
its cached adjusted gain is 0.191% (including a provisional second-source cost),
8/12 wins and bootstrap support 0.91766. ALG058-V000 confirmed a0.325% native pilot gain, but its first archive
call missed the residual-time cap (0.401164s versus 0.4s). That failed package
is preserved. ALG058-V001 batches the same two models into one 72-coordinate,
64-hidden-unit evaluation, preserving their distinct normalizers and clipping.
Its synthetic float32 merge error is at most7.16e-7 in source-output units.
The revised package passed all checks, with maximum residual0.387661s and
exact repeated-input replay. Its twelve-network adjusted gain is 0.1702%,
8/12 wins, bootstrap support 0.89306. The extra billed arithmetic from batching
accounts for most of the difference from the cached estimate. The automatic
0.90 screen marked it for reassessment; under the owner's explicit protocol
waiver, approximately 89% support and positive mean were sufficient for one
bounded official attempt. This is descriptive local support, not a calibrated
private-suite probability. Submission 336809 graded successfully at **2.97110640613e-09 adjusted**,
**0.3928% better than ALG055**, with raw MSE
1.94467643766e-08. Retain **ALG058-V001** as the final best for this recurrence.
No mixture weight or new model was fitted. The original screen-only decision,
reopening, failed V000 package and pre-judgment screen are all preserved.

## Evidence, attribution and accounting

The original fits use 32 previously exposed F training networks. The physical
covariance coefficients already used those networks, so whole-network CV is
conditional and adaptive. The additional 32 rows are public F rows below 500;
they do not consume the protected blind block. Submission comparisons use
previously exposed development inputs under FlopScope 0.12.3. Bootstrap support
is descriptive. Official feedback decides the retained best.

Private weights, geometry and Monte Carlo labels stay under `tmp/` and are not
committed. Research capture timings with concurrent numerical work are explicitly
marked as unsuitable for shipping resource qualification. Candidate resource
checks run in isolation. Overlapping work is counted once in the saved timing record.

Public base: [LordProcciuto repository](https://github.com/siming767-creator/whestbench-lordprocciuto),
commit `3d038e9f48a97671878ee7bbef02e193f128b61c`, MIT, derived from 504aldo's
MIT V29. The research vehicle uses the credited lean implementation and current
ARC equations at reference commit `93d091a4c26c042bfffa28f2e76a81bc0aba94bb`.
The public scale-extraction proposal informed the fuller-model experiments.
Licenses are retained. Our additions are adaptations and independently derived
corrections; no academic-priority or advance eligibility approval is claimed.
