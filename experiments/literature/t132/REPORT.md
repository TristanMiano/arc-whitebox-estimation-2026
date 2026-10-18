# T132 — Literature reconnaissance and route saturation trial

The search changes the recommended next action: **compare an existing cheap
public calibrated estimator before committing to another theory recurrence**.
The objective is better submissions, regardless of academic novelty.

This was the owner's one-cycle literature trial. It used public internet
sources, source inspection and existing project reports. There was no candidate
execution, fitting, target-array access, submission, or new mathematical research
claim. ALG031-V000 / 329989 remains the recorded official best at
1.3618567538742354e-7 adjusted. Start: 2026-09-06 20:23:58 UTC; estimate 60
minutes, ceiling 90. Final timing is in [RESULT.json](RESULT.json).

## The strongest concrete finding

A [September 5 Phase 2 release](https://discourse.aicrowd.com/t/phase-2-write-up-exact-bivariate-relu-covariance-plus-per-layer-calibration-3x-over-the-kit-baseline-with-negative-results-submission-329951/18214)
reports adjusted score **1.32e-7** for submission 329951. Its
[cost/results log](https://github.com/agentaiventure-dot/arc-whest-estimator/blob/fb33bb5a66b4b0aed3022e6a70a9274d5957d61d/results/exact_cov_RESULTS.md)
reports **55,694,969,087 FLOPs**, about **25.4% of ALG031's compute**, and a
four-network local adjusted mean around 1.3695e-7. I inspected the complete
estimator, calibration constants, applicable license and relevant result
sections, and pinned the repository revision and hashes in
[PUBLIC_SOURCE_PIN.json](PUBLIC_SOURCE_PIN.json). Its official receipt did not
load in the browser; the external grade remains author-reported, not reproduced
or independently confirmed here. Its four-network panel differs from ours.

The source propagates Gaussian mean/covariance and applies a fixed correction
to the reported output only. Its predictors are output mean, preactivation
variance, standardized mean, mean absolute off-diagonal covariance, and an
intercept. No online model training is required. [Pinned implementation](https://github.com/agentaiventure-dot/arc-whest-estimator/blob/fb33bb5a66b4b0aed3022e6a70a9274d5957d61d/estimator/estimator.py).

This is **not evidence that Gaussian covariance correction is a missing idea
in our implementation**. ALG031 already uses a Hermite-series covariance
closure and several fitted corrections. Source inspection found that its
22-column design uses disagreement/response fields; it does not explicitly
include that public model's complete absolute-state feature vector. This does
not prove feature independence or incremental benefit. The useful question is
whether a much cheaper calibrated estimator is already competitive, and whether
its errors or features complement ours.

Both algorithms would sit at the same .1 multiplier if the external cost
reproduces. Therefore saving FLOPs alone would not improve its adjusted score.
The potential value is comparable accuracy with about 164.2B operations of
room below the discount floor, or a cheap additional signal. Simply adding
another full 55.7B closure to ALG031 would exceed that floor and require an
accuracy gain large enough to pay for it. None of those gains is assumed.

## Ranked handoff

| Rank | Next useful action | Remaining question and bounded scope |
|---|---|---|
| 1 — L132-A | Reproduce the pinned public calibrated estimator unchanged and compare it with ALG031. | Register its own identity before testing, use one production fixture then the usual 12 predetermined reused development networks. Freeze predictions before target access. No coefficient refit. Estimate 30–45 active minutes, ceiling 60; ordinary qualification/grading adds time only if supported. |
| 2 — L132-B, conditional | Transfer a small absolute-state output correction to our existing closure/head. | First use L132-A to see whether the source is credible and complementary. Reuse existing mean/variance/alpha states and add the covariance-row statistic only if needed. One declared small training fit, no feature grid. Allow 45–75 active minutes if selected, with an explicit finite extension beyond the default ceiling. |
| 3 — L132-C, theory reserve | Output-aware positive recombination of a prefix bank. | Reuse Hayakawa's empirical-measure quadrature construction. Find a cheap feature/kernel sensitive to final error, account for source-bank error, and identify a tracked solver. A 60–90-minute theory recurrence could decide whether any prototype is worth making; an implementation is not yet specified. |

Subjective planning ranges for an official retained gain from a route plus one
bounded implementation attempt: **A 20–40%, B 15–30%, C 5–15%**. These are
uncalibrated judgments, include implementation failure, are dependent, and are
not literature-derived confidence levels. A/B appear to offer modest gains
if they work (roughly 0.2–5% as a planning range); C has insufficient evidence
for a useful gain-size forecast and should not outrank A on speculative upside.
For A, budget roughly 60–100 elapsed minutes through a successful graded
attempt, plus at most 30 minutes for the permitted generic-error retry. B's
complete path is roughly 90–140 minutes, plus such a retry. C needs its theory
decision before any reliable full-path estimate. These budgets authorize no
execution beyond T132.

Suggested **T133** is L132-A, pending the owner's next request. If it reproduces
and the ordinary comparison supports improvement, that submission task should
allow the normal qualification/upload path. If it loses or does not reproduce,
preserve the result and decide whether B or the separate theory reserve offers
more value. Do not automatically run all three. Existing DS and R4IF8-P reserves
remain available and have not acquired new negative evidence here.

## What the broader literature changed

- **Use established controls and allocation formulas.** The generalized
  approximate-control-variate framework includes noisy control means and sample
  overlap. It is useful machinery for our partial paths; iid formulas cannot
  simply be assigned to our orthogonal frames. The paper was already in T113's
  references. [Gorodetsky et al., Section 3](https://www.alexgorodetsky.com/static/papers/gorodetsky_et_all_acv_2020.pdf).
- **Full spherical-harmonic regression is too large in its straightforward
  form.** The published dimension formula gives 524,799 degree-two nonconstant
  controls at input dimension 1024, already far beyond our few thousand
  directions. A selected low-dimensional control remains possible; this
  supports adapting the existing R4IF8-P reserve rather than starting with the
  full polynomial basis. [Leluc et al., Lemma 1](https://arxiv.org/pdf/2402.01493).
- **Conditional integration has a reusable implementation primitive but no free
  smoothness guarantee.** EXACTLINE supplies breakpoint composition; a separate
  preintegration paper explains the monotonicity limitation. Whole-line tail
  handling, number of intervals and saved error per unit work remain our
  application questions. [EXACTLINE](https://arxiv.org/pdf/1908.06214),
  [preintegration limitation](https://arxiv.org/pdf/2112.11621).
- **Gaussian splitting's practical dimension reduction mismatches our starting
  input.** WGMprop uses leading input-covariance eigendirections in its scalable
  implementation. Our input covariance is the identity, so choosing a small
  such subspace throws away most variance. This does not disqualify a method
  that retains the complement or uses a justified output-sensitive subspace.
  [Monchot et al., Section 3.4.4](https://proceedings.mlr.press/v202/monchot23a/monchot23a.pdf).
- **Compression has a concrete literature path worth retaining.** Positive
  kernel recombination can replace a large empirical measure with fewer weighted
  points, but the empirical bank is still approximate. Its construction needs
  a useful kernel, actual kernel-evaluation costs and a submission-compatible
  solver; the inspected public code depends on Gurobi. This addresses an old
  reserve without proving it works here. [Hayakawa et al., Section 5](https://proceedings.mlr.press/v202/hayakawa23a/hayakawa23a.pdf),
  [reference code](https://github.com/satoshi-hayakawa/kernel-quadrature).

No ready-made method explaining the top of the leaderboard was recovered.
Some broad searches were largely duplicative. That is useful for directing
future search time, but the recurrence records show we were not working without
literature. Their frequent emphasis on novelty/attribution checks also differs
from this task's emphasis on finding a usable baseline. The full index records
access depth so a future run need not reread every source or mistake an abstract
for an inspected implementation.

## Route exhaustion and return on search time

The [living tracker](../../../docs/RESEARCH_ROUTE_STATUS.md) has eleven scoped
routes, separate search-saturation and implementation states, a subjective
chance that another 30 minutes changes our action, next-search ceilings, and
reopening conditions. It preserves T131 as inconclusive positive and the
unexecuted reserves as untested. Only the unchanged exact radial operation is
treated as settled, not an entire family of algorithms.

T132 supplies the first baseline for the proposed search process: one new
concrete execution lead, a conditional transfer idea and a specific compression
reserve. The final three-query breadth pass added no new execution-ready lead
or change of priority. No score return can be attributed to this search yet;
that column stays pending until a downstream test or grade exists. The next
refresh should normally be 20–30 minutes total, focused on changed public code
and the chosen open question. This trial creates no permanent search gate and
does not count toward a future theory task's active-time minimum.
