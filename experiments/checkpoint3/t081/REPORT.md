# T081 — literature- and rejection-informed novelty refresh

Status: **complete bounded theory/prior-art refresh and prospective slate; no
protected candidate outcome opened**.

Ledger event `E052` is a source/design decision, not an estimator-quality
result. The public-source cutoff is 2026-08-22 11:52:30 PDT. The
`P1-promising` pool remains empty.

## Decision

Run `H081-A`, the exact auxiliary-prefix-centered hidden-state control, in
T082. It attacks the public mid-network control's measured centering
bottleneck without using an approximate analytic center. If T082 produces no
P1 candidate, run `H081-B`, coupled affine-suffix stochastic continuation, in
T083. It is the covariance-preserving response to E051: a cheap baseline and
its exact nonlinear correction remain on the same input path, and the suffix
is skipped only by an explicitly reweighted Bernoulli decision.

If both terminate without P1, T084 performs the required two-decision novelty
recurrence and reranks `H081-C`, the exact spherical Stein/JVP control, against
new ideas. `H081-C` passes the score floor but is not silently scheduled beyond
the bounded two-candidate sequence. The old `H078-C` sign-Walsh sketch was
explicitly reranked as `H081-D`; its unchanged fingerprint remains below the
floor and it is not inherited merely because the preceding candidates failed.

No owner action is required. T074/T075 remain the independent deadline-safe
submission lane.

## What the evidence changed

| Evidence | Observation | Consequence for this slate | Surprise already recorded |
|---|---:|---|---|
| E047/T076 joint co-kink control | pooled joint/marginal ratio `1.02416786`; `1/12` wins | Do not fit another input-anchored kink feature; selected controls must use realized hidden/path state | Qualitatively moderately surprising; no numerical prior had been frozen |
| E048/T077 threshold control | ratio `0.99968796`; `7/12` wins | Downweight all small-spectrum retunes of transported input ridges | Not surprising under T073's qualitative prior |
| E050/T079 angular orbit | exact small integration, but 884/884 examined anchors exceeded the eight-forward work limit | Do not raise the cap; reject global cell enumeration and require a per-path operation bound | Expected under frozen probability `.72` (`0.473931` bits) |
| E051/T080 independent levels | optimistic oracle ratio `5.17211585`; `0/12` wins | Preserve common-path residual cancellation and shared work; independent level allocation is closed | Expected under frozen probability `.55` (`0.862496` bits) |
| Public mid-network controls | deployed `17.6%` final-MSE reduction; an essentially exact offline layer-24 center removed about `45%` raw MSE | Treat centering fidelity, rather than hidden-state correlation, as a testable bottleneck | Positive external mechanism evidence, not local promotion |
| Public fixed-rule and reweighting census | fixed nonnegative spherical rules are essentially saturated; target-aware basis reweighting has about `5.5x` oracle capacity but lawful observables have cosine `0.018` to it | Do not spend a candidate on another fixed positive carrier or an outcome-dependent signed rule without a target identity | O6/O8 remains high-value open theory, not a runnable candidate here |

The strongest public escape route is signed/network-adaptive angular
reweighting. It was screened but not admitted to this runnable slate. The
published oracle uses target information; using its weights on a deterministic
MUB cloud would not preserve the requested mean, while every disclosed lawful
observable has so far failed to identify the correction. A candidate needs an
exact zero-mean statistic, randomization identity, or prospective bias bound
before protected compute. Oracle headroom alone is not such an identity.

## Dated prior-art boundary

The Phase 1 close census and final rescore materially narrow the search:

- fixed nonnegative spherical cubature is theoretically near-saturated at the
  relevant support, leaving signed/adaptive designs as the public angular gap;
- mid-network state is the only publicly live control channel, while analytic
  centering fidelity is its limiting error;
- error is transported late in a low-dimensional output subspace, but all
  disclosed target-free frame selectors and lawful reweighting observables
  failed to transfer; and
- switching surfaces are dense, supporting per-path identities rather than a
  second global cell enumerator.

Sources:

- [Official challenge and Phase 2 prize/timeline page](https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026)
- [Phase 1 close technique census and August 18 addenda](https://discourse.aicrowd.com/t/a-technique-census-of-phase-1-what-the-mathematics-is-doing-what-walls-it-hit-and-whats-still-open/18157)
- [Public exact-center diagnostic and layer-22 control](https://discourse.aicrowd.com/t/phase-1-write-up-bias-variance-tradeo-across-control-layers-submission-327723/18170)
- [Public intra-network control-variate write-up](https://discourse.aicrowd.com/t/phase-1-write-up-monetizing-the-approach-to-the-moment-propagation-frontier-an-intra-network-control-variate-and-a-measured-map-of-the-wall-behind-it-submission-326024/18154)
- [Generalized approximate control variates for unknown low-fidelity means](https://doi.org/10.1016/j.jcp.2020.109257)
- [Unbiased randomized truncation / multilevel correction](https://arxiv.org/abs/1207.2452)
- [Stein-gradient control functionals](https://doi.org/10.1111/rssb.12185)

These sources make all three new mechanisms conservative
`N1-NOVEL-COMBINATION` hypotheses. ACV, randomized continuation, and Stein
control variates exist academically; the possible contribution is their
specific exact interaction with deep white-box ReLU state, not invention of
the general tool. Bounded ARC exact-phrase/mechanism searches found no public
duplicate of the complete H081-A/B/C specifications. Absence from that corpus
is not proof of worldwide novelty.

## Frozen ranking and surprise rules

The T078 rule is reused unchanged and was fixed before numerical ranking. Each
dimension is an integer from 0 to 4:

`S = (35*N + 30*E + 15*C + 20*R) / 4`.

- `N`, academic novelty: 0 known/duplicate; 1 crowded refinement; 2 plausible
  non-obvious N1 combination; 3 plausible new N2 mechanism pending broader
  review; 4 isolated N2 after broad review.
- `E`, expected effect after all negatives: 0 contraindicated or below 1%; 1
  expected 1–3%; 2 expected 3–10%; 3 expected 10–25%; 4 expected above 25%.
- `C`, falsification/deployment economy: 0 no bounded route; 1 expensive or
  near-budget; 2 bounded diagnostic; 3 cheap kill and credible complete route;
  4 algebraic/static oracle or ample-reserve direct route.
- `R`, robustness: 0 uncontrolled target error; 1 severe open bias/tail risk;
  2 prospectively bounded risk; 3 exact target plus independent fit/fallback;
  4 exact target with a pointwise or conditional identity.

The selection floor is `55`; ties break on N, R, E, then C. At most two
candidates are scheduled before the mandatory recurrence. Passing the score
still requires a unique semantic fingerprint (or explicit same-hypothesis
lineage), exact target or prospective bound, nearest ablation, cheap kill, and
complete estimator route.

For the mutually exclusive outcome that later occurs, record
`I=-log2(q)` using the frozen probability `q`: `q>=.50` expected,
`.25<=q<.50` mildly surprising, `.10<=q<.25` strongly surprising, and
`q<.10` very surprising.

## Ranked hypothesis slate

| Rank | Hypothesis | Project provenance | Academic novelty | N/E/C/R | Score | Frozen final-outcome probabilities | Decision |
|---:|---|---|---|---|---:|---|---|
| 1 | `H081-A` auxiliary-prefix-centered hidden-state ACV | `OURS+PUBLIC` | `N1-NOVEL-COMBINATION` | 2/3/3/4 | `71.25` | pre-M1 reject `.55`; M1 then no P1 `.27`; P1 `.18` | Selected first; T082 |
| 2 | `H081-B` coupled affine-suffix stochastic continuation | `OURS` | `N1-NOVEL-COMBINATION` | 2/2/4/4 | `67.50` | pre-M1 reject `.66`; M1 then no P1 `.24`; P1 `.10` | Selected conditionally; T083 |
| 3 | `H081-C` spherical Stein/JVP path control | `OURS+PUBLIC` | `N1-NOVEL-COMBINATION` | 2/2/3/4 | `63.75` | pre-M1 reject `.70`; M1 then no P1 `.20`; P1 `.10` | Parked above floor for T084 reranking |
| 4 | `H081-D` reranked H078-C sign-Walsh path sketch | `OURS` | `N1-NOVEL-COMBINATION` | 2/0/3/3 | `43.75` | pre-M1 reject `.83`; M1 then no P1 `.15`; P1 `.02` | Parked below floor; unchanged lineage |

The priors are subjective design priors, not empirical evidence. They sum to
one within each row and exist to make later surprise reporting auditable.

## H081-A — exact auxiliary-prefix-centered hidden-state control

### Identity and mechanism

For one antithetic evaluation pair, let `Y` be the final-output pair mean and
`H_j` the post-ReLU hidden-state pair mean at cut `j` from the same paths. Let
`H'_j` have the same law but come from an independent prefix-only stream. For
`N` full pairs, `M` auxiliary prefix pairs, and a response matrix `B` frozen
from data independent of both evaluation means, define

`mu_hat = mean_N(Y) - B (mean_N(H_j) - mean_M(H'_j))`.

Because both hidden means target the same `E[H_j]`, `E[mu_hat]=E[Y]` exactly
for every fixed `B`. Its covariance is

`Cov(Y-B H_j)/N + B Cov(H_j) B^T/M`.

The work is `N*C_full + M*C_prefix(j) + C_pilot`; the pilot jointly optimizes
`B`, `N`, `M`, and the cut under the trace-variance/work objective. This keeps
the valuable `Y,H_j` common-path covariance. Only the unknown center is
estimated independently, unlike E051's independent estimation of every
telescope increment.

Semantic fingerprint:
`008c2391e75ca4e87c8e843a918fae987427b9c16c4672990734f516d4ab98ca`.
No ledger collision was found. The closest academic method is approximate
control variates with an unknown low-fidelity mean; the closest ARC work is
the analytically centered mid-network control. The proposed N1 delta is to use
the network prefix itself as an exactly centered cheap fidelity and optimize
the auxiliary/full split under the contest cost.

### Predicted failure, ablation, kill, and complete route

Most likely failure: the auxiliary-center sampling term and per-network pilot
cost erase the public hidden-state oracle correlation at equal work, or the
best cut varies too much across networks. E047/E048 predict that a shallow cut
will decorrelate; the public center diagnostics predict that a deep cut will
be too expensive.

The nearest mechanism ablation applies a frozen permutation to `H_j` relative
to `Y` in the independent pilot *before fitting `B`*, while preserving pilot
marginals, evaluation streams, auxiliary center, and operation count. (A
permutation after fitting would leave `mean(H_j)` unchanged and would not be
an ablation.) This removes the pilot's common-path covariance signal. `B=0`
equal-work direct antithetic sampling is the target comparator. The known-
center oracle is reported diagnostically to price the centering tax and cannot
earn M1.

T082 freezes cuts, sample domains, pilot folds, costs, ridge rule, and rounding
before output. On 12 width-64/depth-32 networks with 512 full antithetic pairs
per covariance fold and independent prefix streams, reject immediately unless:

1. construction, expectation, source, and replay checks pass;
2. the optimistic continuous ACV trace-variance/work oracle is `<0.82` of
   direct sampling;
3. the held-out rounded allocation is `<0.90` of equal-work direct sampling,
   wins at least `9/12`, and has maximum network ratio `<1.25`; and
4. the candidate/permuted-pair ablation ratio is `<0.90`.

On a pass, award M1 only, register a new candidate/control, charge independent
pilot full paths, auxiliary prefix paths, response fitting, mean correction,
and the selected full paths inside a `261B` working envelope with at least
`11B` reserve, then continue F0–F3 without an intermediate stop until P1 or
rejection. Coefficients remain independent of every evaluation fold.

Pre-result plausible work-normalized ratio range: `0.65–1.05`, center `0.84`.

## H081-B — coupled affine-suffix stochastic continuation

### Identity and mechanism

At cut `j`, compute the exact prefix state `H_j` and a cheap deterministic
affine-suffix baseline `A_j(H_j)` using T025's frozen affine coefficients. Let
`Y` be the exact nonlinear suffix output on that same state. Draw a Bernoulli
continuation `I` with frozen probability `p(H_j)>0`, using one decision for an
antithetic pair, and return

`Z = A_j + I (Y-A_j)/p(H_j)`.

Pointwise, `E_I[Z | H_j]=Y`; hence the estimator preserves the exact target.
For trace variance,

`Var(Z) = Var(Y) + E[((1-p)/p) ||Y-A_j||^2]`,

while expected path work is
`C_prefix + C_affine + E[p*C_nonlinear_suffix]`. The frozen continuous oracle
therefore decides the family before Bernoulli noise or rounding is deployed.
Unlike H078-B, there is one coupled correction on the same input and shared
prefix; no cross-level covariance is discarded and no prefix is repeated.

Semantic fingerprint:
`df514e456fab7727066e2174032766bb3d4651eefb6266393c1ad03df651c421`.
No ledger collision was found. Randomized truncation and occasional
high-fidelity correction are known; the N1 claim is the white-box affine
suffix plus exact same-path continuation interaction.

### Predicted failure, ablation, kill, and complete route

Most likely failure: `Y-A_j` is too large at early cuts while late cuts save too
little work, so roulette variance dominates. E051 raises this probability, but
its `5.17x` loss does not decide this mechanism because that test separately
sampled 32 increments and destroyed their cancellation.

The nearest ablation sets `p=1` at the same cut, baseline, and path, which
reduces exactly to ordinary full antithetic sampling. A constant-probability
rule is mandatory in the first test; any later prefix-adaptive probability
must beat it on an independent fold and receives a new fingerprint if it
changes the deployed behavior.

T083 freezes cuts and constant probabilities before output. Using 12
width-64/depth-32 networks and 512 antithetic pairs per oracle fold, reject
unless the exact continuous variance/work oracle is `<0.80` of direct. If it
passes, execute an independent Bernoulli fold and require work-normalized ratio
`<0.90`, at least `9/12` wins, maximum ratio `<1.25`, exact empirical
continuation frequency, and byte-identical replay.

On M1, register the complete estimator, precompute/charge affine suffix maps,
select a rounded prefix count and continuation probability under `261B` with
at least `11B` reserve, and run F0–F3 to P1 or rejection. Every skipped suffix
has positive frozen continuation probability; no target-dependent stopping is
allowed.

Pre-result plausible work-normalized ratio range: `0.85–1.25`, center `1.02`.

## H081-C — exact spherical Stein/JVP path control

### Identity and route

For a scalar component `f` of the degree-one homogeneous ReLU network and a
constant network-selected direction `a`, surface integration by parts on
`S^(d-1)` with tangent field `f(u)(a-(a dot u)u)` gives

`E[D_a f(U) - d (a dot U) f(U)] = 0`.

The weak identity remains valid for the Lipschitz piecewise-linear network;
activation boundaries have surface measure zero. A forward-mode JVP computes
`D_a f` along the realized gate path. Subtract a pilot-frozen linear
combination of these vector controls from the ordinary spherical-antithetic
mean. No analytic or sampled center is needed.

Semantic fingerprint:
`51daacb8b7a4799d6bd9e69761de151a7df9d4b01b30c889327eba6b03ed28d4`.
No ledger collision was found. Stein gradient controls are known generally;
the provisional N1 delta is the exact spherical homogeneous identity coupled
to a white-box deep-path JVP.

Most likely failure: a JVP costs nearly another prefix/full propagation and
the two large Stein terms add noisy cancellation; the expected-gate direction
may also fail exactly as earlier transported input selectors did. The nearest
ablation replaces the selected direction by the first coordinate while keeping
the exact operator and cost. A bounded 12-network/512-pair kill would require
identity/finite-difference checks, held-out work-normalized ratio `<0.90` to
direct, `9/12` wins, max `<1.25`, and selected/fixed-axis ratio `<0.95`.
The complete route charges the pilot, one tangent propagation per sampled
path, fitting, and correction under `261B`, followed by ordinary registration
and F0–F3. It is parked for T084 reranking, not rejected.

Pre-result plausible work-normalized ratio range: `0.85–1.20`, center `1.02`.

## H081-D — reranked sign-Walsh path sketch

This is exactly `H078-C`, not a renamed invention. For three frozen input axes,
evaluate a cheap path sketch on all eight conditional sign flips. Nonconstant
Walsh components have exact conditional mean zero. Pair/triple components are
the proposed controls; singleton components are the nearest ablation. The
fingerprint is deliberately preserved:
`077c69a0d801305052070cea377fc6c7f14d977ebb75f80d4a8b7bab0d6ff9b7`.

The cheap kill would require an eight-sign construction/replay check and
held-out work-normalized ratio `<0.90`, `9/12` wins, max `<1.25`, and
pair/triple-to-singleton ratio `<0.95`; a pass would batch the eight sketches
under the `261B` envelope and enter F0–F3. E047/E048 plus the public finding
that lawful low-order controls are spent by good carriers now put expected
effect below 1%. Its plausible ratio range is `0.97–1.10`, center `1.01`.
It remains a valid but low-priority N1 hypothesis, not a scientific rejection.

## Duplicate and human-promotion disposition

- Subject/evidence class: E052/T081 bounded source/design audit (`N`); four
  ranked hypotheses, no estimator outcome.
- Provenance/novelty: H081-A/C are `OURS+PUBLIC`, H081-B/D are `OURS`; all are
  conservative N1 combinations. Project provenance is not an invention claim.
- Duplicate audit: H081-A/B/C hashes are new and globally absent; H081-D
  deliberately preserves H078-C lineage and makes no new semantic claim.
- Current/highest/next tier: no new empirical tier; P1 remains empty; next
  considered tier is M1 for H081-A in T082.
- Positive evidence: each route has an exact target identity, explicit
  ablation, decisive cheap kill, full cost path, and frozen outcome prior.
- Gate status: novelty recurrence `PASS`; four distinct hypotheses `PASS`;
  ranking/priors `PASS`; protected outcomes, M1, F0–F3, and P1 `NOT-RUN`.
- Primary blocker: `EVIDENCE_INCOMPLETE`, not scientific rejection or a strict
  gate miss. Scores and public results are priors, not local evidence.
- Strict gate sole blocker: no; no candidate gate has opened.
- Immediate high-impact unlock: agent executes T082's predeclared exact ACV
  oracle and held-out kill. No owner action or threshold change is required.

## Reproduction

```bash
bash experiments/checkpoint3/t081/verify_evidence.sh
```

## Task timing

- Start: `2026-08-22T11:42:33,904110229-07:00`
- Pre-task estimate: `50 minutes`
- End/check-off: `2026-08-22T12:02:10,655299240-07:00`
- Actual wall-clock difference: `00:19:36.751189011`
  (`1176751189011` ns)
