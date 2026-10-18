# T084 — rejection-informed novelty recurrence

Status: **complete bounded theory/prior-art refresh; no protected candidate
outcome opened**.

Ledger event `E055` is a source/design decision, not estimator-quality
evidence. The public-source cutoff is `2026-08-22T13:31:26-07:00`. The
`P1-promising` pool remains empty.

## Decision

Run `H084-A`, the Haar-randomized MUB coherent-residual Hansen–Hurwitz
estimator, in
T085. It is the first project hypothesis to receive novelty dimension `N=3`
and the provisional academic label `N2-NOVEL-MECHANISM`: conditional
Hansen–Hurwitz correction exactly recovers a complete randomly oriented MUB rule,
while Haar averaging exactly recovers the spherical target. Its same-
orientation prefix proxy can guide which *basis residuals* receive nonlinear
suffix work without making the weights target-dependent.

If T085 produces no P1 candidate, run the already parked `H081-C` spherical
Stein/JVP path control in T086 under its unchanged fingerprint and original
`.70/.20/.10` prior. `H084-B`, symmetric kink-energy vMF importance sampling,
is a new exact mechanism but ranks third because public importance-sampling
prior art and the project's input-anchored negatives limit its expected gain.
It remains above the score floor for the next recurrence rather than
displacing H081-C automatically.

If T085 and T086 both terminate without P1, T087 performs the next mandatory
two-decision novelty recurrence. No owner action is required. T074/T075 remain
the independent deadline-safe submission lane.

## Why the slate changed

| Evidence | Observation | Consequence |
|---|---:|---|
| E053/T082 | width64 exact-center M1 `0.642904`, then width256 F1 `1.569200`, `0/2` | Do not fit another high-dimensional full response; use a scalar/basis allocation rule whose exactness does not depend on fit transfer |
| E054/T083 | optimistic shared-prefix continuation `0.852166`, `11/12`, max `1.027672`, but short of `<0.80` | Preserve same-path residual cancellation, aggregate residuals coherently before roulette, and reduce the number of nonlinear suffixes rather than retuning the gate |
| Public fixed-rule census | complete MUB/Kerdock nearly saturates fixed nonnegative rules; signed per-network oracle about `5.5x` | Keep MUB as a carrier and move adaptivity into an exactly corrected sampling design, not an outcome-dependent deterministic rule |
| Public lawful-weight negative | fixed learned weights collapse toward uniform after Haar rotation | Let the proxy observe the *same orientation* and use inverse-probability correction; do not transfer an index weight across independent rotations |
| E047/E048 and prior active rotations | input-anchored controls were adverse/near-null and fixed orientations had catastrophic tails | Downrank vMF importance sampling and require a uniform proposal floor and an exact uniform ablation |

The first row of the new slate is not a relaxed T083 continuation. T083 made
an independent continuation decision per antithetic path. H084-A evaluates a
complete cheap surrogate over a Haar-randomized finite MUB population, forms
coherent vector residual means at the *basis* level, and uses a fixed-count
design-unbiased estimator of that finite-population residual total. Both its
random object and its variance mechanism are different.

## Dated prior-art and duplicate boundary

The audit covered the current official challenge/census, all local semantic
fingerprints and negative-result families, the public fixed MUB/Kerdock
theorems and reweighting oracle, the public Haar-learned-weight negative,
classical Haar-randomized spherical rules, Hansen–Hurwitz/design-unbiased
finite-population estimation, multifidelity/control-variate residual
correction, spherical vMF importance sampling, and Stein gradient controls.

Those ingredients separately are public. The bounded search found no public
description of the complete H084-A interaction: a complete real-MUB finite
population under one Haar orientation, an all-basis same-orientation affine
surrogate, proxy-adaptive fixed-count basis draws, and exact inverse-
probability correction of coherent nonlinear basis residuals. Exact-phrase
and mechanism searches also found no local fingerprint collision.

That supports novelty dimension `3`—a plausible new estimator mechanism
pending broader review—and the provisional `N2-NOVEL-MECHANISM` label. It does
**not** support dimension `4`: randomized cubature, MUB carriers, survey
sampling, and multifidelity residual correction are established separately;
the prior-art search was bounded; and the surviving public #1 is evidence that
an undisclosed lawful adaptive angular method may exist. An N4 claim would be
unnecessarily strong before empirical isolation and external review.

Sources:

- [Official challenge and Phase 2 page](https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026)
- [Phase 1 technique census and August 18 addenda](https://discourse.aicrowd.com/t/a-technique-census-of-phase-1-what-the-mathematics-is-doing-what-walls-it-hit-and-whats-still-open/18157)
- [Complete MUB/Kerdock public build](https://discourse.aicrowd.com/t/phase-1-write-up-metered-dead-compacted-kerdock-cubature-with-exact-compiler-reductions-submission-326680/18149)
- [MUB optimality and missing-basis study](https://discourse.aicrowd.com/t/phase-1-write-up-the-missing-basis-was-not-the-mechanism-submission-327749/18176)
- [Public signed-reweighting oracle report](https://discourse.aicrowd.com/t/phase-1-report-submission-327801/18183)
- [Haar-learned-weight negative, lines 283–290](https://discourse.aicrowd.com/t/phase-1-write-up-a-variance-bias-budget-for-deep-white-box-mean-estimation-submission-317660/18085)
- [Classical randomized spherical-rule precedent](https://doi.org/10.1016/S0377-0427(99)00214-9)
- [Stable randomized cubature](https://doi.org/10.1016/j.jat.2022.105706)
- [Adaptive importance sampling and control variates](https://arxiv.org/abs/2212.00568)
- [Repulsive spherical Monte Carlo and vMF importance baseline](https://openreview.net/forum?id=JSiTmB6Ehu)
- [Stein-gradient control functionals](https://doi.org/10.1111/rssb.12185)

Absence from these sources is not proof of worldwide novelty. The novelty
label must be revisited after T085 derives and tests the exact deployed rule.

## Frozen ranking and surprise rule

The T078/T081 rule is reused unchanged and fixed before numerical ranking:

`S = (35*N + 30*E + 15*C + 20*R) / 4`,

with integer dimensions from 0 to 4, selection floor `55`, ties broken by N,
R, E, then C, and at most two candidates before another recurrence. `N=3`
means a plausible new N2 mechanism pending broader review; `N=4` requires an
isolated N2 mechanism after broad review.

For the mutually exclusive result later observed, report
`I=-log2(q)`: `q>=.50` expected, `.25<=q<.50` mildly surprising,
`.10<=q<.25` strongly surprising, and `q<.10` very surprising.

## Ranked hypothesis slate

| Rank | Hypothesis | Project provenance | Academic novelty | N/E/C/R | Score | Frozen final-outcome probabilities | Decision |
|---:|---|---|---|---|---:|---|---|
| 1 | `H084-A` Haar-MUB coherent affine-residual Hansen–Hurwitz estimator | `OURS+PUBLIC` | provisional `N2-NOVEL-MECHANISM` | 3/3/3/4 | `80.00` | pre-M1 reject `.58`; M1 then no P1 `.27`; P1 `.15` | Selected first; T085 |
| 2 | `H081-C` exact spherical Stein/JVP path control | `OURS+PUBLIC` | `N1-NOVEL-COMBINATION` | 2/2/3/4 | `63.75` | pre-M1 reject `.70`; M1 then no P1 `.20`; P1 `.10` | Selected conditionally; T086 |
| 3 | `H084-B` symmetric kink-energy vMF importance sampler | `OURS+PUBLIC` | `N1-NOVEL-COMBINATION` | 2/1/4/4 | `60.00` | pre-M1 reject `.80`; M1 then no P1 `.16`; P1 `.04` | Parked above floor for T087 reranking |

The probabilities are subjective prospective design priors, not empirical
evidence. H081-C's existing probabilities and fingerprint are deliberately
unchanged because no H081-C outcome has been opened.

## H084-A — Haar-MUB coherent affine-residual Hansen–Hurwitz estimator

### Exact two-stage target identity

Let `B` be the number of bases in the complete real MUB construction and let
each basis contain its antipodal endpoints `v_bk`. Draw one Haar orthogonal
matrix `Q` per replication. For the exact network output `f`, define the
antipodal basis mean `Y_b(Q)`. At frozen cut `j`, compute T025's same-path
collapsed affine-suffix output on every endpoint and define its basis mean
`A_b(Q)`. The cheap population mean is

```text
Abar(Q) = (1/B) sum_b A_b(Q).
```

From the all-basis prefix information, compute strictly positive probabilities
`q_b(Q)` with a frozen uniform floor and `sum_b q_b=1`. Draw exactly `m` basis
indices using stratified random uniforms whose individual marginals are
categorical `q`. For each draw `s`, finish the nonlinear suffix for basis
`b_s` and return

```text
Z(Q) = Abar(Q)
       + (1/m) sum_s [Y_{b_s}(Q)-A_{b_s}(Q)] / [B q_{b_s}(Q)].
```

Conditional on `Q` and every prefix-derived probability,

```text
E_draw[Z(Q) | Q,prefix] = (1/B) sum_b Y_b(Q).
```

Every `Q v_bk` is marginally uniform on the sphere, so expectation over Haar
`Q` is the desired spherical mean. Positive homogeneity supplies the exact
Gaussian-radius factor. The estimator therefore remains exact even if the
proxy is useless; proxy quality affects variance only.

### Novel delta and falsifiable prediction

The new claim is that same-orientation, coherent *basis residuals* are a
lawful adaptive unit for deep ReLU cubature. Unlike fixed learned frame
weights, the allocation sees the current orientation. Unlike target-aware
deterministic reweighting, the inverse-probability correction preserves the
complete rotated rule conditionally. Unlike T083, roulette occurs after
antipodal and within-basis cancellation and all prefixes share the MUB
population structure.

Falsifiable prediction: after charging all-basis prefix work, a target-aware
continuous basis-residual oracle is `<0.75` of full Haar-MUB variance-cost, and
a lawful prefix proxy retains enough of that gain to achieve `<0.90`, at
least `9/12` network wins, maximum ratio `<1.25`, and candidate/uniform-
allocation ratio `<0.95` on an independent fold.

### Duplicate audit, ablation, cheap kill, and complete route

Semantic fingerprint:
`20f626b99b9c5a1dd0f551513e11ea623f9de0e5c3b60db158ef349270b23e18`.
No local collision exists. The closest public components are Haar-randomized
spherical rules, fixed MUB cubature, Hansen–Hurwitz residual totals, and multifidelity
correction; none located has this complete same-orientation basis mechanism.

The nearest ablation uses uniform `q_b=1/B` with the identical Haar matrix,
cut, affine surrogate, fixed draw count, streams, and charged work. It keeps
the exact carrier and coherent residual correction while removing only
network-adaptive allocation. Report T083's pathwise oracle as historical
context, not as a route-matched comparator.

T085 first uses 12 deterministic width64/depth32 networks, the complete 33-
basis real MUB (`4,224` antipodal endpoints per Haar replication), 32 pilot
and 32 independent held-out Haar rotations, cuts `{4,8,12,16,20,24}`, and
fixed basis-draw counts `{4,6,8,12,16,20,24,28}`. It must freeze the prefix
proxy, uniform floor, stratified categorical domains, costs, folds, and source
hash before output. Reject immediately unless construction checks, conditional
identity, Haar marginal checks, and deterministic replay pass and the
optimistic oracle is `<0.75`. Only on that pass open the lawful proxy fold and
apply the `<0.90`, `>=9/12`, `<1.25`, and `<0.95` gates above.

On M1, register one complete width256 rule using the 129-basis real MUB,
charge Haar generation/rotation, all prefixes, affine maps, categorical
administration, every nonlinear suffix, output accumulation, and fixed
reserve inside `261B` with at least `11B` reserve, then run F0–F3 to P1 or
rejection without pausing.

Most likely failure: all-basis prefix cost plus categorical residual noise
exceeds the saving, or the legal prefix proxy cannot predict residual basis
energy. The public `0.018` proxy/oracle cosine and T082's width-scaling
reversal make proxy-transfer failure a serious risk. Pre-result plausible
work-normalized ratio range: `0.62–1.15`, center `0.86`.

## H081-C — exact spherical Stein/JVP path control

This is the unchanged T081 hypothesis, not a renamed invention. Its semantic
fingerprint remains
`51daacb8b7a4799d6bd9e69761de151a7df9d4b01b30c889327eba6b03ed28d4`.
For degree-one ReLU output `f`, the spherical divergence identity makes
`D_a f(U)-d(a dot U)f(U)` exactly zero mean. One realized-gate forward JVP
computes the path derivative; a coefficient and network direction are frozen
on an independent pilot.

The nearest ablation is the first coordinate under the same operator/JVP cost.
T086 retains the 12-network/512-pair kill: identity and finite-difference
checks, held-out work-normalized ratio `<0.90`, `>=9/12` wins, maximum `<1.25`,
and selected/fixed-axis ratio `<0.95`. On M1 it charges pilot, tangent
propagation, fitting, and correction inside `261B`/`>=11B`, then enters F0–F3.
The most likely failure remains tangent cost plus noisy cancellation. Its
original plausible range `0.85–1.20`, center `1.02`, and `.70/.20/.10` prior
remain frozen.

## H084-B — symmetric kink-energy vMF importance sampling

Construct network-only antipodal directions from late, path-compatible kink-
influence summaries and define a symmetric proposal density relative to the
uniform sphere:

```text
q(u) = lambda
       + (1-lambda) sum_r alpha_r
         [vMF(u; a_r,kappa)+vMF(u;-a_r,kappa)] / 2,
```

with `lambda>=0.5`, nonnegative `alpha` summing to one, and all parameters
frozen before evaluation. Sampling `U~q` and returning the antithetic output
pair divided by the exactly evaluated `q(U)` is unbiased. The uniform floor
bounds likelihood ratios by `1/lambda` and supplies the tail safeguard.

Semantic fingerprint:
`ce4f4c2fe7ceb7bb19d4b240435da2b41e5c2de1dd1c0d3d8979b536a9357900`.
No local collision exists, but spherical/vMF importance sampling is explicit
public prior art. The project delta is only the late kink-energy construction,
so the conservative label is `N1-NOVEL-COMBINATION`, novelty dimension 2.

The nearest ablation is `lambda=1` under identical antithetic IID work. A
future cheap kill would first require a target-aware vMF-family oracle `<0.82`
of uniform, then a lawful held-out ratio `<0.90`, `>=9/12` wins, maximum
`<1.25`, and legal-proxy/oracle retention `<1/0.95`. A complete route charges
center construction, normalized-density evaluation, exact vMF sampling, and
full paths under `261B`/`>=11B` before F0–F3.

Most likely failure: deep He-ReLU angular energy is too isotropic for a small
mixture, while concentrations strong enough to help create likelihood-ratio
tails. The project's input-feature negatives and the public vMF baseline make
that expected. Plausible ratio range: `0.88–1.18`, center `1.03`.

## Human promotion disposition

- Subject/evidence class: E055/T084 source/design audit; three ranked
  hypotheses, no candidate result.
- Current/highest/next tier: no new empirical tier; P1 remains empty; H084-A
  next considers M1 in T085.
- Positive evidence: H084-A has a two-stage exact target proof, an isolated
  adaptive-allocation ablation, a bounded cheap kill, and a complete-cost
  route. Its novelty dimension is provisionally `3`.
- Gate results: novelty recurrence `PASS`; three mechanisms `PASS`; at least
  two new mechanisms `PASS`; exact/bounded admission `PASS`; duplicate audit
  `PASS`; ranking/priors `PASS`; protected outcomes, M1, F0–F3, and P1
  `NOT-RUN`.
- Strict-gate margin: not applicable; no empirical promotion gate opened.
- Primary blocker class: `EVIDENCE_INCOMPLETE`.
- Why not promoted: no strict gate or scientific result blocked it; H084-A is
  a prospective hypothesis and must earn M1/P1 empirically before receiving an
  `ALG` identity or contribution claim.
- Immediate high-impact unlock: agent executes T085's exact construction,
  continuous oracle, and—only after an oracle pass—lawful held-out proxy
  allocation. No owner action is required.

## Task timing

- Start: `2026-08-22T13:15:16,106274113-07:00`
- Pre-task estimate: `55 minutes`
- End/check-off: `2026-08-22T13:32:04,138887976-07:00`
- Actual wall-clock difference: `00:16:48.032613863` (`1008032613863` ns)
