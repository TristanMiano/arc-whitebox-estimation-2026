# T087 — rejection-informed novelty recurrence

Status: **complete bounded theory/prior-art refresh; no protected candidate
outcome opened**.

Ledger event `E058` is a source/design decision, not estimator-quality
evidence. The public-source cutoff is `2026-08-22T15:01:02-07:00`. The
`P1-promising` pool remains empty.

## Decision

Run new `H087-A`, the Lyapunov-subspace projected auxiliary-prefix control, in
T088. If it terminates without P1, run new `H087-B`, the coupled-survival
affine-hybrid randomized telescope, in T089. If both terminate without P1,
T090 performs the next recurrence.

Parked `H084-B` was genuinely reranked, not inherited. It remains barely above
the floor at `56.25`, but the combined evidence says that another
input-direction proposal is much less likely to help than a dimension-
controlled exact hidden control or a covariance-preserving continuation rule.
No gate from T085 or T086 was weakened.

`H087-A` receives novelty dimension `3` and the provisional label
`N2-NOVEL-MECHANISM`. Low-rank controls and Lyapunov subspaces are public; the
bounded audit found no description of this exact interaction: a deterministic
weight-only six-dimensional forward/backward basis, an independent exact
prefix center, and a two-sided rank-six correction whose complement remains
direct. That supports a plausible academic mechanism claim, not proof of
worldwide novelty. Dimension `4` is withheld.

No owner action is required. T074/T075 remain the independent deadline-safe
submission lane.

## Failure reconciliation

| Evidence | Observation | Design consequence |
|---|---:|---|
| E056/T085 | optimistic coherent-allocation oracle `0.905089`, `10/12` wins, max `1.092443`; required `<0.75` | Retain the idea that structure can predict some residual energy, but stop paying an all-basis prefix population and stop expecting allocation alone to produce a 25% gain |
| E057/T086 | raw variance `1.080674`; work ratio `2.180344`; `0/12`; max `3.706705` | Do not propagate another full tangent or search another nearby direction; a successor must be cheap and dimension-controlled |
| E053/T082 | width64 exact-center ratio `0.642904`, `12/12`; width256 full response F1 `1.569200`, `0/2` | Preserve the exact independent prefix center, replace the width-dimensional response with fixed rank six, and test width scaling before registration |
| E054/T083 | same-prefix oracle `0.852166`, `11/12`, max `1.027672` | Preserve cross-increment covariance and shared paths; use a nested survival sum rather than an independent telescope or a post-outcome single-cut retune |
| Public Phase 1 structure | about 68% of reported closure error lies in a weight-computable six-dimensional Lyapunov subspace; low effective output rank is also reported | Test that six-dimensional structure as a lawful estimator component rather than treating it as an oracle score |

This reconciliation matters. `H087-A` is a prospectively frozen reduced-
dimension descendant of T082, not a rerun with more ridge. `H087-B` uses the
exact T025 affine-hybrid telescoping identity, but one common path and nested
survival event preserve the covariance that T080's independent levels lost.
Neither changes the meaning of a prior rejection.

## Dated prior-art and duplicate boundary

The refresh covered the official challenge and updated Phase 1 technique
census/frontier, the public estimator-class ceiling analysis, every local
semantic fingerprint, low-rank and multifidelity control variates, approximate
control variates with estimated means, active/Lyapunov subspaces, unbiased
randomized telescoping, Russian-roulette estimators, neural pruning/coarsening,
and spherical/vMF importance sampling.

Public literature establishes the broad ingredients:

- low-rank multifidelity control variates use correlations with reduced models;
- generalized approximate control-variate estimators allow estimated auxiliary
  means;
- randomized telescoping/Russian roulette can unbiasedly sum a finite or
  infinite difference sequence; and
- vMF importance sampling is not new.

The bounded search found no exact public or local collision for either new
semantic fingerprint. That absence is not proof of global novelty. H087-A's
dimension `3` rests on the complete exact-target interaction, not on claiming
low rank, subspaces, or control variates as inventions. H087-B remains
`N1-NOVEL-COMBINATION`, dimension `2`, because its identity is a close finite
application of public randomized telescoping. H084-B remains N1.

Sources:

- [Official ARC challenge page](https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026)
- [Updated Phase 1 technique census and open questions](https://discourse.aicrowd.com/t/a-technique-census-of-phase-1-what-the-mathematics-is-doing-what-walls-it-hit-and-whats-still-open/18157)
- [Phase 1 combined solution ideas and public frontier](https://discourse.aicrowd.com/t/phase-1-solution-ideas-for-phase-2-and-the-honest-public-frontier-all-methods-combined-and-explained/18193)
- [Public estimator-class ceiling study](https://discourse.aicrowd.com/t/write-up-submission-326725-measuring-the-ceiling-of-a-method-class-how-we-closed-54-families-of-estimators-without-building-them/18182)
- [Fixed positive MUB saturation theorem](https://discourse.aicrowd.com/t/phase-1-writeup-fixed-positive-sampling-is-nearly-saturated-submission-327786/18171)
- [Low-rank multifidelity control variates](https://arxiv.org/abs/1611.02213)
- [Generalized approximate control-variate framework](https://www.sciencedirect.com/science/article/abs/pii/S0021999120300310)
- [Randomized telescoping sums](https://proceedings.mlr.press/v97/beatson19a.html)
- [Unbiased estimators and multilevel Monte Carlo](https://pubsonline.informs.org/doi/10.1287/opre.2017.1670)
- [Repulsive spherical Monte Carlo and vMF baseline](https://openreview.net/forum?id=JSiTmB6Ehu)

## Frozen ranking and surprise rule

The unchanged scoring rule is

`S = (35*N + 30*E + 15*C + 20*R) / 4`,

with integer dimensions 0--4, floor `55`, ties broken by N, R, E, then C,
and at most two scheduled candidates before recurrence. For the mutually
exclusive eventual result report `I=-log2(q)`: `q>=.50` expected,
`.25<=q<.50` mildly surprising, `.10<=q<.25` strongly surprising, and
`q<.10` very surprising.

| Rank | Hypothesis | Provenance | Novelty | N/E/C/R | Score | Frozen final-outcome probabilities | Decision |
|---:|---|---|---|---|---:|---|---|
| 1 | `H087-A` Lyapunov-subspace projected auxiliary-prefix control | `OURS+PUBLIC` | provisional `N2-NOVEL-MECHANISM` | 3/3/3/4 | `80.00` | pre-M1 reject `.55`; M1 then no P1 `.30`; P1 `.15` | T088 |
| 2 | `H087-B` coupled-survival affine-hybrid randomized telescope | `OURS+PUBLIC` | `N1-NOVEL-COMBINATION` | 2/3/3/4 | `71.25` | pre-M1 reject `.63`; M1 then no P1 `.25`; P1 `.12` | T089 if no T088 P1 |
| 3 | `H084-B` symmetric kink-energy vMF importance | `OURS+PUBLIC` | `N1-NOVEL-COMBINATION` | 2/1/3/4 | `56.25` | pre-M1 reject `.85`; M1 then no P1 `.12`; P1 `.03` | parked for T090 reranking |

The priors are subjective prospective design probabilities, not evidence.
H084-B's fingerprint and mechanism remain unchanged, but its still-prospective
prior is updated before any H084-B outcome using T085/T086 and the refreshed
public structure evidence.

## H087-A — Lyapunov-subspace projected auxiliary-prefix control

For full-path antithetic output `Y`, post-ReLU hidden state `H_j`, and an
independent same-law prefix-only state `H'_j`, construct six-column orthonormal
bases `P_j` and `Q_j` deterministically from the frozen network weights and
expected-gate forward/backward products. They must not use candidate outputs.
Fit only a pilot-separated `6 x 6` response `B`, then estimate

```text
Z = mean(Y) - Q_j B [mean(P_j^T H_j) - mean(P_j^T H'_j)].
```

Because the two projected hidden means have exactly the same expectation,
`E[Z]=E[Y]` for every pilot-frozen `P_j`, `Q_j`, and `B`. The component
orthogonal to `Q_j` remains the direct mean. Relative to T082, the response
dimension is fixed at six rather than scaling with width; projection and
aggregate correction cost scale as `O(6w)`, not a fitted `w x w` response.

The nearest ablation replaces `P_j,Q_j` by the first six coordinate axes with
identical centering, response size, streams, and charged work. T088 uses a
prospectively frozen width ladder: 12 width64 and 12 width128 depth32 networks,
512 pilot and 512 evaluation antithetic pairs per network. At each width it
requires candidate/equal-work direct `<0.88`, at least `9/12` wins, maximum
ratio `<1.25`, and candidate/fixed-coordinate `<0.95`; width128 may exceed the
width64 aggregate by less than `0.10`. Correctness, exact center, source, and
replay must also pass. Stop at the first scientific rejection.

On M1, register a complete width256 rank-six candidate inside `261B` with at
least `11B` reserve and continue F0--F3 to P1 or rejection. Most likely
failure: the public deterministic closure-error subspace does not align with
the stochastic final/hidden covariance, or independent-center noise and prefix
work still dominate. Plausible work-normalized ratio range `0.60--1.25`,
center `0.86`.

Semantic fingerprint:
`484671664a62f7c226cca4869f9298a87b03feb7eeb024befd5121a534191682`.

## H087-B — coupled-survival affine-hybrid randomized telescope

For one antithetic input/path, define nested T025 hybrids `F_0,...,F_L` by
progressively replacing affine-suffix layers with exact ReLU layers, with
`F_L=f`. Let `Delta_k=F_k-F_{k-1}`. Draw one truncation `K` with frozen
positive survival probabilities `p_k=P(K>=k)` and return

```text
Z = F_0 + sum_{k <= K} Delta_k / p_k.
```

Conditionally on the input, `E_K[Z]=F_0+sum_k Delta_k=f` pointwise. Unlike
T080's independent level streams, all increments share the input, prefix,
and nested survival event, retaining cross-increment covariance. Unlike T083,
the rule can allocate survival across multiple frozen levels rather than one
cut.

The nearest ablation is T083's best frozen single-cut Bernoulli continuation
at matched expected work. T089 freezes levels `{0,4,8,12,16,20,24,28,32}`,
positive monotone survival schedules, antithetic domains, costs, folds, and
rounding before output. On 12 width64/depth32 networks with 512 pairs per fold,
reject unless an optimistic tail-sum covariance oracle is `<0.80` of direct.
Only on a pass open the held-out route and require `<0.90`, `>=9/12` wins,
maximum `<1.25`, and candidate/single-cut `<0.95`, plus exact continuation
frequencies and replay.

On M1, register a fully charged width256 route inside `261B`/`>=11B` and run
F0--F3. Most likely failure: inverse-survival tails and repeated suffix work
erase covariance gains. Plausible ratio range `0.72--1.20`, center `0.91`.

Semantic fingerprint:
`d527bb5e36d0299f19d0f67ee6b71e43f952d06739338dae7e22418cf9f84071`.

## H084-B — reranked, not inherited

The exact T084 mechanism and fingerprint are unchanged:
`ce4f4c2fe7ceb7bb19d4b240435da2b41e5c2de1dd1c0d3d8979b536a9357900`.
It samples from a uniformly floored symmetric vMF mixture centered on late
kink-energy directions and divides the antithetic output by the exact proposal
density.

It remains lawful and above floor, but ranks third. T086 found only a `2.25%`
selected-direction advantage over fixed axis while losing raw variance and
more than doubling work-normalized variance; T085's target-aware coherent
allocation produced only `9.49%` gain before legal proxy costs; and the public
census reports a severe lawful-observable/oracle gap. These do not directly
test H084-B, so it is parked rather than scientifically rejected, but its new
prospective P1 probability is only `.03`. Its nearest ablation remains the
uniform proposal. Do not run it automatically after T088/T089; T090 must
rerank it again.

## Human promotion disposition

- Subject/evidence class: E058/T087 source/design audit; three hypotheses, no
  protected candidate result.
- Current/highest/next tier: no new empirical tier; P1 remains empty; H087-A
  next considers M1 in T088.
- Strongest positive evidence: T082's exact independent-center mechanism was
  `0.642904` with `12/12` width64 wins, and public analysis identifies a
  weight-computable six-dimensional error subspace. These are inputs, not an
  H087-A result.
- Gate status: recurrence, two-new-mechanism admission, exact identities,
  duplicate audit, ranking, ablations, complete routes, and priors `PASS`;
  candidate M1, registration, F0--F3, and P1 `NOT-RUN`.
- Strict-gate margin: not applicable; no empirical promotion gate opened.
- Primary blocker: `EVIDENCE_INCOMPLETE`.
- Strict gate sole blocker: no; there is no candidate outcome yet.
- Why not promoted: H087-A is a prospective hypothesis. Novelty dimension `3`
  is not efficacy, M1, an `ALG` identity, P1, or a submission claim.
- Immediate high-impact unlock: the agent executes T088's exact width ladder
  and continues a pass through the complete fast funnel. No owner action is
  required.

## Verification

```bash
bash experiments/checkpoint3/t087/verify_evidence.sh
```

## Task timing

- Start: `2026-08-22T14:54:44,588089248-07:00`
- Pre-task estimate: `55 minutes`
- End/check-off: `2026-08-22T15:09:01,163423946-07:00`
- Actual wall-clock difference: `00:14:16.575334698`
  (`856575334698` ns)
