# T139 — Compress joint history and retain more of its modeled information

**Recommendation: T140 should implement and make one bounded submission attempt
with C64-E.** It combines a smaller third-cumulant history with persistence of
the old modeled remainder, which the incumbent currently uses for repeated
moments and then partly discards. The construction-inclusive forecast is
**427.998B FLOPs versus756.892B**, a43.45% reduction. Accuracy and actual runtime
are unmeasured; this is a candidate worth testing, not an established win.

T139 produces two prospective nominees, no production candidate evaluation,
no challenge-target access, no fitting, no uploads and no agents. ALG038-V001 /
330153 remains the official best at **1.46676758754e-8 adjusted**. Small generated
tensor checks and Gaussian-reference trajectories are mathematical evidence,
not challenge scores. [Actual timing](TIMING.json) records the approved120-useful
and90-active-theory-minute floors and the120–150-minute planning estimate.

## The two nominees

| Priority | Candidate | What changes | Projected cost / score condition | Planning chance of a retained official gain |
|---|---|---|---|---|
| 1 | **H139-C64E / C64-E** | Keep two recent CP source blocks; compress older history into a symmetric rank64 Tucker core; absorb the transported/gated old E into that core | **427.998B**, .5655× incumbent cost. At fixed raw MSE,43.45% lower adjusted score, around8.29e-9. Break-even raw MSE ratio1.768 | **55%**, broad35–70% range |
| 2 | **H139-Q4D / Q4D** | Replace the fourth scalar with per-coordinate fourth trace and marginal kurtosis, retaining the full incumbent third state | **814.932B**,7.67% added cost. Needs about7.12% lower raw MSE to break even | **30%**, broad15–45% range |

Under the C64-E cost projection, even a25% increase in raw MSE would still
give about29% lower adjusted score. That headroom helps justify testing the
riskier representation. It does not predict its actual raw error.

These probabilities are subjective planning judgments about a future bounded
attempt, including feasibility; they are not calibrated posteriors or submission
support. Neither candidate has reached the usual roughly90% evidence threshold.
The nominees are independent. Combining them would require a new registration.

The complete mathematical handoffs are [C64-E](C64E_MATHEMATICAL_HANDOFF.md) and
[Q4D](Q4D_MATHEMATICAL_HANDOFF.md). [Cost projections](COST_PROJECTIONS.json)
include core construction, refresh, repeated repair, sketches, SVD billing and
engineering reserves. They use direct core products and the existing public
matrix-kernel arithmetic; they are not production measurements or strict upper
bounds on every implementation's cost.

## What the recurrence found

**The old history is compressible, but the representation matters.** Small
generated histories had concentrated tensor-mode spectra. Replacing old history
while repairing its repeated entries can make the immediate tensor error small.
A single compression impulse changed the final signed mean correction by about
0.13–1.20% for the tested quarter-width Tucker projections. That denominator is
the incumbent's signed correction, not its error against truth. Repeated
compression, fixed rank64 at width1024, and the new E persistence were not tested
by those impulses. [Geometry](HISTORY_GEOMETRY_CHECKS.json),
[impulses](RESPONSE_IMPULSE_CHECKS.json).

**An affordable core also offers a specific accuracy extension.** The incumbent
already calculates M E. The gated old remainder is exactly represented by the
temporary paired factors `(diag(d) @ M @ E /s, diag(d) @ M /s)`, so it can be projected into the core
without an additional full transport product. The new E then restores the
candidate's current repeated response. This preserves more of the modeled
incoming third tensor; E itself remains an approximation and may carry harmful
error. The dense transport/projection/repair identity checks pass below3.5e-17.
[Check](REMAINDER_CORE_CHECKS.json).

**The scalar fourth state has a complete, inexpensive extension.** Existing K22
calculations already supply each coordinate's fourth trace and marginal
kurtosis. A two-vector minimum-norm completion preserves both, and its transport
needs three additional square products per nonfinal layer. It recovers the exact
fourth tensor for independent coordinates. It remains weak when the omitted
off-diagonal trace dominates: on the strongly correlated six-coordinate fixture,
relative quartic metric was .745 versus .853 for the scalar completion. This
does not establish a large high-width score gain. [Check](FOURTH_PROJECTION_CHECKS.json).

**The richer conditional source is mathematically viable but less compelling
as the next test.** A32-node shared-mode correction recovers Gaussian terms and
the He1–4 projected response missed by the current source, including proper
centering. At correlation.65 it corrects a gate-only skew-response error of about
43%; the formula's quadrature error is below2.74e-8 in those fixed cases. But a
generated width1024 covariance trajectory puts only about6% of late-layer
variance in its selected common mode, leaving substantial conditional residual
dependence. Its5% cost increase is not yet justified by expected coverage.
Keep the derivation as a reserve, rather than making the favorable one-factor
example a leaderboard forecast. [Source checks](CONDITIONAL_SOURCE_CHECKS.json),
[cap/sign checks](CONDITIONAL_SOURCE_BOUNDARY_CHECKS.json),
[covariance geometry](COVARIANCE_GEOMETRY_CHECKS.json).

## Where progress was limited

- Large Tucker cores are expensive. The rank256 direct-core construction exceeds
  the eligibility cap; rank128 retains less cost headroom than a transport-only
  estimate suggests. Symmetric packing helps, but does not make construction free.
- One-leg and two-leg projections are valid alternatives. Their accuracy/cost
  tradeoffs did not displace C64-E in this round. Cheap mean/trace directions
  did not consistently match tensor-mode directions. [One-leg](ONE_LEG_CHECKS.json),
  [two-leg/sketch](TWO_LEG_CHECKS.json).
- An exact repair of one future trace reduced the tested residual metric by only
  about3–6%. Its extra products are not justified now. Reopen when the relevant
  error is demonstrably trace-dominated. [Check](OBSERVABLE_TRACE_CHECKS.json).
- A full nonradial fourth-trace matrix has a tractable representation and a
  partial Gaussian source, but its affordable complete response remains
  unresolved. Q4D deliberately uses constraints whose full response is already
  available; it is a distinct approximation.

Two errors were caught and retained: the initial static sketch count omitted
two output products, and a fourth-moment reference used a truncated probability
where a zeroth raw moment needed1. Both were corrected before nomination. The
initial fourth-check output is preserved and clearly marked invalid. The long
[scratchpad](SCRATCHPAD.md) records derivations, failed routes and qualifications.

## Literature and research style

The refresh reused the ARC factorized-cumulant source and added focused Tucker
and observable-aware reduction references. Symmetric Tucker and streaming
sketch methods are established; their construction and approximation limits
informed the handoff. A structured bilinear sketch's unbiased mode Gram does
not automatically inherit an unstructured Gaussian sketch's error theorem.
[Symmetric Tucker](https://arxiv.org/pdf/2204.10824),
[streaming Tucker](https://tropp.caltech.edu/papers/SGLTU20-Low-Rank-Tucker.pdf),
[state/gradient reduction](https://arxiv.org/html/2207.14387v4).

The work was deduction and algorithm construction, with small fixed mathematical
checks. No coefficients, ranks or seeds were fitted to challenge targets.
The SVD chooses a basis for a tensor derived from supplied weights; that is
adaptive numerical compression, not supervised training. Search access limits
and normalized query topics are in [SEARCH_LOG.json](SEARCH_LOG.json).

## Proposed T140, requiring the next owner instruction

Register **C64-E** as one material variant, implement the specified recurrence
in the qualified Python3.12 runtime, and meter an integrated width1024 fixture
early. If feasible, compare the usual12 fixed networks against retained
ALG038-V001 outputs using actual adjusted costs. Roughly90% support is sufficient
for package qualification and an authorized upload; use the existing bounded
extension rule only if the decision remains usefully uncertain. Allow30 minutes
per submission attempt, with the existing one unchanged-package retry rule.

Plan roughly **100–130 elapsed minutes**, with no minimum-duration requirement
for that implementation task. Stop a clear scientific loss; repair routine
implementation faults within scope. Do not add a rank sweep, component ablation
campaign, a new fit, or a second automatic candidate task. Compression without
E persistence (~399.471B projected) remains the simpler fallback, and Q4D the
separate accuracy nominee. Neither substitutes silently for C64-E.


## Completion

T139 used **121.02 elapsed / 120.05 useful minutes**, including **92.37 active theory**, 10.67 literature and 17.01 selection/handoff minutes. Setup (0.97 minutes) is excluded from useful time. [Actual timing](TIMING.json).
Ended 2026-09-08T18:46:33.983719+00:00. Elapsed estimate error: +1.02 minutes versus the120-minute lower estimate, -28.98 versus150. Both approved floors met. Event E134; T140 remains proposed only.
