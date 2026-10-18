# T143 — joint response, retained memory, and adjacent methods

**Recommendation: T144 should make one bounded attempt with H143-JSP, a
joint-source path update. H143-E1 is the separate second nominee.** Neither
has been run on the challenge. ALG038-V001 / submission330153 remains the
official best at adjusted1.46676758754e-8.

T143 used **120.02 derivation, 60.06 literature, and 30.21 candidate-selection minutes**: **210.29 useful minutes** over **250.43 elapsed minutes** through records. Setup and overhead are excluded from the three floors. [Actual timing](TIMING.json).

## The main finding

The incumbent carries a rich third-moment history, but each newly created
source is based on the Gaussian backbone. Its signed mean/covariance and
third-moment corrections affect current pair responses and the temporary
completion E; they do not fully enter the persistent new joint source.
That leaves a specific, inexpensive place to improve the recurrence.

JSP changes the source's existing B factor from F to F+H, where H contains
selected Gaussian and incoming third-response paths plus the variation of
the Gaussian source under the signed mean/covariance corrections. The number
of source/history columns is unchanged. Repairing the repeated entries still
preserves the current moment response. The intended benefit appears after
the changed joint source is transported through later layers.

This is a mechanism for testing, not a diagnosis that these terms dominate
the remaining leaderboard error. It is also not a complete augmented
cumulant algorithm: covariance triangles, general old-third gate loops, and
the fourth vertex remain absent. The finite factor update retains some
higher-order cross-products. Its precise definition is in the
[JSP handoff](JSP_MATHEMATICAL_HANDOFF.md).

## Selected candidates

| Candidate | Change | Projected full prediction cost | Raw-MSE gain needed to pay for cost | Subjective chance of a retained official gain |
|---|---|---:|---:|---:|
| **H143-JSP — first** | Improve the fresh joint source, retaining the incumbent history and factor count | **757.14–757.89B** (+0.03–0.13%) | **0.03–0.13%** | **45%**, broad range25–65% |
| **H143-E1 — second** | Retain one uncompressed completion block for one extra explicit hop | **828.52–831.52B** (+9.46–9.86%) | **8.65–8.97%** | **25%**, broad range10–40% |

These probabilities concern a future bounded attempt producing a retained
official improvement, including implementation risk. They are planning
judgments, not calibrated probabilities or the roughly90% support expected
after a local submission screen. Costs are static projections; no T143
candidate has been metered. The [cost record](COST_PROJECTIONS.json) includes
complete history/slice charges and conditional score scenarios.

For scale, a10% raw gain would give approximately9.9% adjusted improvement
for JSP at its upper forecast price, but only about1.2% for E1 at its central
price. A20% raw gain would give about19.9% and12.2%, respectively. These are
**if-then calculations**, not forecasts of the actual gain. Small gains would
still be acceptable if the normal screen supports them.

E1 preserves the full main history; it is not another rank64 compression
attempt. Its [handoff](E1_MATHEMATICAL_HANDOFF.md) specifies exactly which
extra block is transported and which old all-distinct contribution is then
discarded. Older effects can still persist through repeated moments, a,D,h
and later E. Full completion retention is a separate, more expensive reserve:
about1.27T FLOPs and a roughly40% raw-gain requirement. The mathematically
cleaner full construction does not yet have enough support to displace JSP.

## What the derivations established

**The selected source is affordable algebraically.** Its path tangent agrees
with explicit diagram enumeration; parameter differentiation, factor
cross-products, repeated-entry repair and scale conventions have independent
small generated checks. The checked local Gaussian and third-response
examples usually favor the path update over the simpler tree. No deep-network
or score conclusion follows from those examples.

**Discarded information does not disappear merely because weights mix it.**
An invertible linear map preserves a third tensor's norm in appropriately
whitened coordinates. Gaussian ReLU gate transport is nonexpansive, but it can
approach identity in highly active directions. The repeated-entry projection
is generally oblique in that metric. Therefore there is no general one-layer
forgetting theorem for the incumbent's completion. A dense four-step generated
reference verifies E1's bookkeeping, while leaving its accuracy unresolved.

**The relevant compression error depends on the future response.** The work
derived a random-next-ReLU discrepancy, its relation to an arc-cosine kernel,
and an exact next-cubic-query Gram equal to six times a third-order ANOVA
kernel. The latter preserves generated next-row queries to numerical precision.
It does not preserve all mixed queries needed for later covariance and fourth
responses. That makes it an interesting larger reserve, not a ready new
compressed estimator.

**Representation choices can change future approximation without changing
today's tensor.** Adjusting the source diagonal q and repairing E leaves the
current tensor invariant. A quartic minimizes a local completion norm, but an
explicit small-perturbation counterexample shows that, to leading order, the
squared Frobenius norm can fall25% while cubic-query mean-square error rises25%. A coupled observable objective, gradient and positive
Gauss–Newton approximation are derived. This offers a cheap future direction
once its numerical update is specified; it is not parameter fitting on
challenge targets.

The [scratchpad](SCRATCHPAD.md) also develops conditional Hermite projections,
stable pair-leg integrals, coherent missing-diagram contractions, and a paired
representation of a low-rank Gaussian triangle. The
[mathematical evidence index](MATHEMATICAL_EVIDENCE.md) identifies what each
generated check does and does not establish.

## Where progress was weaker

More accurate pair information did not consistently improve the complete
third response. A resummed skewness pair leg underperformed the simpler path
in selected fixtures. An isolated fourth path worsened the approximation
unless its missing vertex was included. A cheap old-factor projection left
roughly96–98% relative tensor error in two generated examples, while requiring
about273B extra repeated-slice work. Those versions are poor immediate bets.

Conditional integration was accurate within its specified model, but dropping
residual cross-correlations produced substantial error. A single coherent
direction also captured little of some missing joint tensors. These results
do not close conditioning or coherent corrections as families; they identify
what a useful follow-up must retain.

There is still no mathematical prediction of the incumbent's exact remaining
error decomposition. T143 did not establish an order-of-magnitude successor,
and the larger reserves need additional work. The return from the longer
round is a better specified near-term test and several sharper alternatives,
not a demonstrated leaderboard gain.

## Literature outcome and attribution

The wider review covered moment closures, conservative kinetic reduction,
Mori–Zwanzig memory, Gaussian splitting, polynomial chaos, observable kernels,
Stein methods, randomized trace estimation, turbulence closure, and tensor
network truncation. The [reading notes](LITERATURE_NOTES.md) and
[registry](SEARCH_LOG.json) distinguish50 new entries plus the core source
refresh by actual reading depth; many are selected sections or limited
screening, not complete-paper readings.

Several useful primitives have established prior art: the arc-cosine kernel,
Bussgang decomposition, ANOVA identity, Gaussian trace cycles, and augmented
path factors. The latter are explicit in the
[public cumulant-propagation code](https://github.com/alignment-research-center/mlp_cumulant_propagation/blob/93d091a4c26c042bfffa28f2e76a81bc0aba94bb/src/mlp_kprop/factor_k3.py).
JSP adapts selected terms to this repository's paired source and retention
policy. Academic novelty is not a condition for trying it.

No ready external estimator clearly displaced the current plan. The most
useful adjacent principle is to preserve information according to its effect
on later responses, as detailed in [the transfer assessment](ADJACENT_METHODS.md).
Further generic searching now appears less valuable than one complete test.
That is a scoped planning judgment, not a claim that those fields are exhausted.

## Next action and stopping rule

Propose **T144: one bounded JSP implementation and submission attempt**.
Register the variant, reuse the qualified Python3.12/Whest path, and meter an
integrated1024-by16 fixture early. The incumbent's .3278–.3900s historical
residual range is close to the .4s cap; extra array overhead can defeat the
static cost advantage. Price the final compliant realization rather than an
earlier cheaper prototype.

If feasible, compare on the usual12 predetermined reused development
networks against ALG038-V001, using actual adjusted cost. Approximately90%
support is enough for package qualification and an authorized submission.
Do not add a broad ablation campaign, extra confidence threshold, or minimum
percentage gain. Use the existing single bounded extension only if it can
resolve a useful uncertain decision. A clear loss ends the candidate attempt.

Estimate35–75 elapsed minutes for a normal attempt, including possible grader
waiting; this is not a minimum. Keep the default60 active engineering minutes
with a30-minute reassessment. Allow30 minutes per submission try and one
unchanged-package retry for a generic evaluator failure. E1 is not automatic:
re-rank it and the [reserves](RESERVES.md) after the primary result.

Q4D remains the accuracy-positive engineering fallback, with its conditional
approximately812.815B cost target and earlier residual failures preserved.
T143 itself made no challenge predictions, opened no challenge targets, fit
no coefficients, created no submission package, used no subagents, and made
no permanent protocol change. T144 has not started.


Completed 2026-09-09T00:43:50.002370+00:00. Estimate235–265 elapsed minutes; error+15.43 versus the lower estimate and-14.57 versus the upper. Event E138. Final verification/commit follows this record endpoint.

Final record/source verification completed 2026-09-09T00:44:35.320081+00:00, **251.19 elapsed minutes** from task start. JSON, Python syntax, handoff hashes, local links, time floors and live-state/event consistency pass. No production code changes or repeated mathematics runs. [Verification](VERIFICATION.json).
