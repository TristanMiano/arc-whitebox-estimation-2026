# T120B — bounded physical trace submission

## Current outcome

ALG028-V000 passed the predefined lean production comparison and all package
checks. The unchanged archive was accepted as official submission **329774**
at 2026-09-04T20:24:19.713Z. It graded successfully. **ALG028-V000 is the new official project best**, submission 329774: adjusted 1.42299664616985e-07, final-layer MSE 1.422996646169849e-06, 3.7974% below ALG026 submission 329690. The owner authorized upload and requested protocol
restructuring after this attempt. T121 and the parked R3 production work have
not resumed.

## Candidate and evidence

This is T120's R1P physical trace correction with unchanged ALG026 coefficients,
closure, seeded frame/child/partial construction and fallback. It reuses the
terminal propagated clouds and rebases the existing AS features on the trace
corrected carrier. There is no new fit, arm grid, or scientific-tier campaign.
Numerical operations remain within the allowed FlopScope API. Inherited
numerical modules are byte-identical to ALG026; provenance and licenses ship.

T120's 250-network result (3.5932% improvement, 203/250 wins) motivated this
choice. The actual production implementation was confirmed on 12 rows chosen
before execution, spread across those already-opened panels. Those rows are
reused development evidence, not fresh independent validation.

| Production comparison | Result |
|---|---:|
| Candidate adjusted score | 1.3518392250026865e-7 |
| Current parent adjusted score, identical networks | 1.3748933313646438e-7 |
| Ratio / improvement | .9832320764 / 1.676792% |
| Network wins | 7/12 |
| Paired network-bootstrap support for improvement | .9068 |
| 90% two-sided interval for adjusted mean change | [-5.240333212e-9, +5.473454714e-10] |
| Worst network ratio | 1.047891765 |

The .9068 bootstrap result exceeds the prospectively recorded .90 submission
threshold. It is a screening diagnostic, not a calibrated probability of an
official win or a scientific confidence claim. The two-sided interval includes
zero; no extra interval or scientific-tier gate was imposed. Actual predictions
were sealed before accessing the reused panel targets. Both candidate and
parent use the same inherited primitives; the exact unchanged parent AS
composition supplies the paired control, avoiding duplicate frame propagation.
Its previously measured exact cost remains 218,819,123,305 FLOPs.

## Production and package qualification

Actual integrated candidate cost is **218,985,062,607 FLOPs**, identical on all
12 networks, multiplier **.1**. This measured charge supersedes the old R1P
component estimate for this package. The parent closure is retained and fully
charged. Resource checks passed across the 12-network execution: residual
.3659–.3810 seconds, approximately 16 seconds wall time, .0012 seconds setup,
and peak process RSS 5,409,210,368 bytes. The zero-budget, diagonal and
unsupported-shape fallbacks are byte-identical to the parent.

The predeclared historical numerical-equivalence limits were maximum terminal
error <=1e-5 and numerical MSE <=1e-12. Observed maxima across the 12 rows were
3.33786e-6 and 3.51829e-13. Every actual repeated output was byte-identical.
No historical prediction, coefficient, or prior result was rewritten.

Whest contract and package-manifest checks pass. Clean temporary extraction
reproduced the current-source prediction hash and exact cost; residual times
were .3795 and .3752 seconds. Static import checks found no prohibited raw
numerical imports. WSL was used under the existing recovery allowance after
T118A/T120A had established Windows residual failures on these inherited kernels.
No additional platform campaign or consecutive-clean-run rule was added.

Archive: `packages/ALG028-V000.tar.gz`.
SHA-256: `0415448d568e81441919094cfc6f9374aa69e491a388096620ccb4b721c4f878`.
`PREUPLOAD_SEAL.json` binds the package, qualification and decision.

## Disposition and timing

N1 combination provenance is inherited from the T119/T120 derivation; no new
scientific tier is claimed. Production/competition screen PASS, all required
operational checks PASS, official grade PASS. **ALG028-V000 is the new official project best**, submission 329774: adjusted 1.42299664616985e-07, final-layer MSE 1.422996646169849e-06, 3.7974% below ALG026 submission 329690. R3's raw signal and corrected
4.11% conditional projection remain preserved, with its production blockers.
It was parked for speed, not scientifically rejected.

Start: 2026-09-04T20:13:08Z (13:13:08 PDT). Estimate: 60 active engineering
minutes, 75 minutes including grading. Upload accepted after 11m11.713s.
Official grade arrived on the first submission; no retry was created. End/checkoff: 2026-09-04T20:39:32.943093+00:00. Actual elapsed 26.42 minutes, 48.58 minutes earlier than the 75-minute estimate. Approximate allocation is recorded in RESULT.json. The bounded R1P attempt is complete. Next is the owner-requested TODO/protocol review; do not automatically run T121 or start a theory recurrence. T120A/R3 remains parked with its evidence preserved.

Owner wait extension at 20:38:01 UTC: wait **30 minutes per submission attempt**, including the current submission. Submission 329774 therefore has an absolute cutoff of 20:54:19.713 UTC. The 15-minute monitoring process was intentionally stopped and resumed against the same submission with that deadline; no submission was cancelled or duplicated. Original monitor source/status are preserved.
