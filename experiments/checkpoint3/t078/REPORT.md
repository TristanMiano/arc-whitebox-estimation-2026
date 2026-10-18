# T078 — rejection-informed novelty refresh

Status: **complete bounded theory/prior-art refresh and prospective slate; no
protected candidate outcome opened**.

Ledger event `E049` records a source/design decision, not an estimator-quality
result. The public-source cutoff is 2026-08-22 10:50 PDT. The
`P1-promising` pool remains empty.

## Decision

Run `H078-A`, exact angular-orbit Rao–Blackwellization, in T079. T079 must
either carry the complete design through to `P1-promising` or close it at the
first failed frozen gate. If it produces no P1 candidate, run `H078-B`, exact
multilevel kink-telescope allocation, in T080 under the same stop-at-P1-or-
rejection rule. If T079 does produce P1, T080 becomes not applicable and the
route enters T067 instead.

The slate deliberately does **not** select another fitted input-ridge feature.
E047 found the joint co-kink version directionally adverse, and E048 found the
thresholded version practically null. The new selected mechanisms change the
estimator operation: one computes an exact conditional expectation; the other
uses an exact layerwise expectation telescope with independent cost-optimal
allocation.

No owner action is required. T074/T075 remain the independent deadline-safe
submission lane.

## What the prior results changed

| Evidence | Observation | Update applied to this slate | Surprise assessment |
|---|---:|---|---|
| E047/T076 joint co-kink control | pooled joint/marginal ratio `1.02416786`; `1/12` wins; 11/12 adverse | Large downward update for fitted input-anchored joint features; no H073-A retune | **Moderately surprising, retrospectively and qualitatively.** T073 assigned expected-effect score 3/4 and ranked it first, but no numerical probability was frozen, so none is invented now. |
| E048/T077 threshold control | ratio `0.99968796`; `7/12` wins; only `0.0312%` favorable | Large downward update for changing the spectrum of the same transported ridge template | **Not surprising.** T073 gave only 2/4 expected effect, and the public record already warned that exact-mean low-order input controls decorrelate after depth and overlap RQMC. |
| E044/T071 lifted Householder | F1 `0.714612`, then F2 `1.0701375` with three tails | A strong local hidden-state signal may not be turned into an input-carrier rotation; selected routes must preserve the target without rotating the carrier | The reversal was scientifically informative; there was no prospectively frozen probability, so it is not assigned surprise bits. |
| E039/T026 residual telescope support | pooled residual/full IID variance `0.708098`, but maximum per-network ratio `413.877` | Exact telescoping remains usable, but covariance destruction and per-network tails must be explicit kill gates | Positive pooled direction with catastrophic heterogeneity supports only a cautious multilevel prior. |
| T024 integrated structure replacement | protected pooled ratio about `1.034` against dense | Approximate replacement is disfavored; analytic structure may enter only through an exact identity or bounded fallback | Consistent with selecting exact conditional/telescoping constructions rather than another replacement. |

These are calibration statements, not rewritten pre-result beliefs. Only the
probabilities in the prospective table below may be used to judge surprise in
T079/T080.

## Public-census delta through the cutoff

The refreshed public record makes the spectral fallback much less attractive
than it appeared from local reasoning alone:

- A public ceiling study reports that the residual is a high-degree ReLU-kink
  tail, but also reports dense switching surfaces and an additive
  one-dimensional ceiling; it explicitly groups cells, Gegenbauer methods,
  poles, and switching-hyperplane targeting among the closed directions.
  [Public ceiling study](https://discourse.aicrowd.com/t/write-up-submission-326725-measuring-the-ceiling-of-a-method-class-how-we-closed-54-families-of-estimators-without-building-them/18182)
- A separate public RQMC/Rao–Blackwell report found input and first-layer
  exact-mean controls roughly null at depth and argues that RQMC and these
  controls remove overlapping smooth variation.
  [Public RQMC/Rao–Blackwell report](https://discourse.aicrowd.com/t/unbiased-randomized-qmc-rao-blackwell-for-post-relu-activation-means-method-unbiasedness-proof-and-where-the-frontier-is/18053)
- Public Kerdock/MUB work already provides a ReLU-kernel optimality theorem and
  a weight-independent structured-quadrature result, increasing the duplicate
  burden for a new carrier-only claim.
  [Public Kerdock/MUB theorem report](https://discourse.aicrowd.com/t/phase-1-write-up-the-missing-basis-was-not-the-mechanism-submission-327749/18176)

Bounded exact-phrase and mechanism searches found no public ARC report for
full-network exact angular-orbit conditional integration or for the exact
T025-hybrid multilevel estimator below. Absence in this bounded challenge
census is not proof of worldwide novelty. `H078-A` therefore remains
`NU-UNCERTAIN`, with a provisional N2-level semantic claim to resolve only if
it first survives empirically. `H078-B` is conservatively `N1` because
multilevel Monte Carlo is known even though this ReLU telescope appears locally
distinct.

## Frozen ranking rule

The rule was fixed before the numerical rankings were calculated. Each
dimension is an integer from 0 to 4 and

`S = (35*N + 30*E + 15*C + 20*R) / 4`.

- `N`, academic novelty: 0 known/duplicate; 1 crowded refinement; 2 plausible
  non-obvious N1 combination; 3 plausible new N2 mechanism pending broader
  review; 4 isolated N2 after broad literature review.
- `E`, expected effect after prior scientific results: 0 contraindicated or
  below 1%; 1 expected 1–3%; 2 expected 3–10%; 3 expected 10–25%; 4 expected
  above 25%.
- `C`, falsification/deployment economy: 0 no bounded route; 1 expensive or
  likely near-budget; 2 bounded diagnostic before a cycle; 3 cheap kill and
  credible complete route; 4 static kill or ample-reserve direct route.
- `R`, robustness: 0 uncontrolled target error; 1 severe open bias/tail risk;
  2 prospectively bounded risk; 3 exact target plus independent fit/fallback;
  4 exact target with a deterministic conditional identity or target-
  preserving fallback.

The selection floor is `55`; ties break on N, then R. Passing the score is not
enough: a selected route also needs a unique semantic fingerprint, exact or
prospectively bounded target, nearest-mechanism ablation, cheap falsification,
complete operation plan, and path to F0–F3.

## Ranked hypothesis slate

| Rank | Hypothesis | Novelty | N/E/C/R | Score | Prospective empirical prior | Decision |
|---:|---|---|---|---:|---|---|
| 1 | `H078-A` exact angular-orbit conditional Rao–Blackwellization | `NU-UNCERTAIN` (provisional N2 claim) | 3/3/2/4 | `76.25` | pre-M1 rejection `.72`; M1 then no P1 `.18`; P1 `.10` | Selected first; T079 |
| 2 | `H078-B` exact multilevel kink-telescope allocation | `N1-NOVEL-COMBINATION` | 2/2/3/4 | `63.75` | pre-M1 rejection `.55`; M1 then no P1 `.30`; P1 `.15` | Selected conditionally; T080 if T079 yields no P1 |
| 3 | `H078-C` conditionally centered sign-Walsh path-sketch control | `N1-NOVEL-COMBINATION` | 2/1/3/3 | `51.25` | P(M1) `.20`; P(P1) `.05` if later made complete | Parked below floor; compression/decorrelation risk |
| 4 | `H078-D` degree-6/8 zonal harmonic input control | `N0-KNOWN-BASELINE` | 0/0/4/4 | `35.00` | P(M1) `.10`; P(P1) `.02` if nevertheless tested | Closed as current priority, not empirically tested |

The numerical priors are subjective design priors, not evidence. Their purpose
is to make later surprise reporting auditable rather than vulnerable to
hindsight.

## Prospective surprise rule

For the mutually exclusive final outcome category actually observed, record
`I = -log2(q)` bits using its frozen probability `q` above:

- `q >= 0.50`: expected;
- `0.25 <= q < 0.50`: mildly surprising;
- `0.10 <= q < 0.25`: strongly surprising;
- `q < 0.10`: very surprising.

Thus an `H078-A` pre-M1 rejection is expected (`q=.72`, `0.474` bits), an M1
pass followed by P1 rejection is strongly surprising (`q=.18`, `2.474` bits),
and P1 is strongly surprising (`q=.10`, `3.322` bits). For `H078-B` those
categories are expected (`.55`, `0.862` bits), mildly surprising (`.30`,
`1.737` bits), and strongly surprising (`.15`, `2.737` bits). A task report
must quote the applicable frozen category before interpreting its result.

## H078-A — exact angular-orbit conditional Rao–Blackwellization

### Theory and target identity

Choose a two-dimensional plane `P` deterministically from the network, before
sampling. For `U` uniform on the sphere, write

`U = Z + rho (cos(theta)e1 + sin(theta)e2)`,

where `Z` is the projection onto `P-perp`. Conditional on `(Z,rho)`, `theta`
is uniform. Therefore

`A(Z,rho) = (1/(2*pi)) integral f(Z + rho e(theta)) dtheta`

is exactly `E[f(U) | Z,rho]`, so `E[A]=E[f]` and the law of total variance
guarantees non-increasing raw variance. The network-selected plane is the top
two right singular directions of the frozen expected-gate end-to-end
Jacobian, with canonical tie/sign handling sealed before the result. This uses
T033's low-rank transport evidence without rotating the input carrier as
T071 did.

Along one orbit, every preactivation is piecewise
`a + b cos(theta) + c sin(theta)`. On each current interval ReLU introduces at
most two roots, so breakpoints can be propagated and each final activation can
be integrated analytically. The obvious danger is exponential interval growth,
not target bias.

Use a deterministic `65,536`-interval cap. The cap decision is a function only
of the whole orbit state `(network,Z,rho)`, never of the sampled angle. If
enumeration exceeds the cap, return the ordinary single-angle network output
for that orbit. Conditional expectation is then correct on both branches, so
the hybrid remains target preserving.

Semantic fingerprint:
`0a5539beb9f7030f3e8d8edcd88986e12bca1bd3c46c8ab35f52cb63b8581d06`.
It is distinct from H073-A/B fitted controls, ALG011's Householder carrier, and
ordinary fixed spherical cubature because the defining operation is exact
network-conditioned conditional expectation with an orbit-invariant fallback.

### Cheap kill and complete route

T079 first seals the selector and arithmetic identities, then verifies exact
integration against dense angular quadrature on small networks. Its frozen
12-network, width-64/depth-32 study uses 256 orbit anchors per network. Reject
before M1 if any identity/replay check fails, fewer than `75%` of orbits finish
under the interval cap, p95 completed-orbit work exceeds eight dense-forward
equivalents, or the hybrid's work-normalized trace-variance ratio is not
`<0.85` versus equal-work antithetic sampling with at least `9/12` network wins
and maximum ratio `<1.25`.

The mandatory selector ablation uses the fixed first two coordinate axes with
the same integrator and cap. The selected plane must additionally give ratio
`<0.95` to that ablation on the pooled work-normalized metric; otherwise the
weight-dependent academic delta is rejected even if generic orbit averaging
is useful.

If M1 passes, register a new immutable candidate and control before F0. At
width 256, charge expected-gate/Jacobian construction, plane projection,
breakpoint propagation, analytic integration, and fallback forwards. Choose a
nested anchor count from measured p95 work while preserving at least `10B`
modeled operations of the `272B` ceiling. Compare against a route-matched dense
antithetic estimator at equal modeled work, report the unchanged incumbent as
contest context, and continue F0–F3 without stopping between stages until P1
or rejection.

Pre-result central expectation: the raw conditional variance will fall, but
interval growth will erase the benefit at equal work; plausible work-normalized
ratio range `0.95–1.40`, central value about `1.10`. The predicted failure mode
is the tractability/cost gate, not bias. A pass is therefore genuinely
informative rather than expected confirmation.

## H078-B — exact multilevel kink-telescope allocation

### Theory and target identity

Reuse T025's fixed affine hybrids `F^(k)`: exact ReLU layers `1..k`, frozen
affine layers `k+1..L`. Pointwise,

`f = F^(0) + sum_(k=1)^L Delta_k`,

where `Delta_k = F^(k)-F^(k-1) = r_k(z_k) B_k`. Consequently

`E[f] = E[F^(0)] + sum_k E[Delta_k]`

exactly for any frozen affine coefficients. Estimate the levels with
independent randomized streams and counts `N_k`. If `V_k` is the trace
variance and `C_k` the modeled cost, the continuous optimum at fixed total
cost has `N_k proportional sqrt(V_k/C_k)` and variance-cost product

`Q = (sum_k sqrt(V_k C_k))^2`.

This is a direct theoretical screen: if `Q` cannot beat direct sampling before
rounding and reserve, implementation cannot rescue the family. It also exposes
the cancellation risk seen in T026 rather than hiding it in a pooled average.

Semantic fingerprint:
`b49d215e0b1a27c44ec3aaddb68b53e1d7c1bc2e86ca732879c41a4193ffea37`.
It is not T026's one-stream full residual sum, a K3 predictor, or H073's fitted
input control. The academic delta is the exact ReLU-hybrid level telescope plus
cost/trace-variance allocation; MLMC itself remains known, hence N1.

### Cheap kill and complete route

T080 freezes deterministic diagonal-Gaussian affine coefficients, level costs,
two-fold pilot/evaluation separation, rounding, minimum level counts, and
independent randomized streams. On 12 width-64/depth-32 networks, reject before
M1 unless the held-out work-normalized ratio is `<0.90` versus the identical
uniform-cost level telescope, `<0.95` versus equal-work direct antithetic
sampling, wins at least `9/12`, and has maximum network ratio `<1.25`. The
continuous oracle must first be `<0.75` of direct sampling; failure stops the
implementation immediately because it is a mathematical upper-bound screen.

The mandatory mechanism ablation is uniform-cost allocation over the identical
`Delta_k` levels and streams. Direct full-output antithetic sampling is the
second scientific comparator. Both preserve the same target.

If M1 passes, compute all suffix matrices once, charge that preprocessing,
allocate independent randomized spherical-RQMC streams to levels inside a
`261B` working envelope with at least `11B` reserve, register the complete
candidate/control identities, and run F0–F3 to P1 or rejection. Cross-fitting
keeps allocation estimates independent of evaluation samples. The candidate
may fall back to direct sampling under a frozen per-network projected-efficiency
rule; since the rule uses pilot data independent of the evaluation streams, it
does not change the target.

Pre-result plausible work-normalized ratio range is `0.85–1.25`, central value
about `1.02`. The predicted failure is covariance loss across independently
sampled levels or severe per-network allocation heterogeneity. The `.15` P1
prior reflects the promising T026 pooled direction but its extreme tail and
the public evidence that kink error is distributed rather than localized.

## Parked hypotheses

`H078-C` evaluates a cheap nonlinear path sketch on all eight sign flips of
three deterministically selected axes. Conditional on magnitudes and the
orthogonal state, the signs are uniform. Every nonconstant Walsh component
therefore has exact conditional mean zero. Pair/triple Walsh terms would be
the candidate and singleton terms the same-work ablation. This is mathematically
clean, but public support-removal cliffs, T077's deep decorrelation, and the
need for an aggressively compressed path sketch give it low expected effect.
It remains a real N1 queue entry, not a duplicate, but scores below the floor.
Fingerprint:
`077c69a0d801305052070cea377fc6c7f14d977ebb75f80d4a8b7bab0d6ff9b7`.

`H078-D` uses exactly centered degree-6/8 zonal harmonics aligned to a deep
gradient direction, with degree-2/4 terms as the nearest ablation. It was
initially attractive as a direct response to a high-degree residual. The
public Gegenbauer/additive-class ceiling plus E048's near-null input control
changes that conclusion: this form is `N0`, predicted below 1%, and closed as
a current priority without a new empirical test. This does not claim that
every high-degree control is scientifically impossible. Fingerprint:
`bf19e4bce2b473d2470c94f42f11bc61ede7e9f9f0b5d509e7fee63cf60947e1`.

## Human promotion disposition

- Subject/evidence class: E049/T078 bounded source/design audit (`N`); four
  prospective hypotheses, no estimator outcome.
- Current/highest/next tier: no new empirical tier; P1 pool remains empty;
  next considered tier is M1 for H078-A in T079.
- Positive evidence: two selected hypotheses have exact target identities,
  deterministic fallbacks or independent allocation, explicit ablations,
  bounded cheap kills, complete operation routes, and unique fingerprints.
- Gate status: novelty recurrence `PASS`; at least three distinct hypotheses
  `PASS` (four); duplicate audit `PASS`; ranking frozen before selection
  `PASS`; protected outcomes `NOT-RUN`; M1/F0–F3/P1 `NOT-RUN`; incumbent
  competitiveness `NOT-APPLICABLE`.
- Primary blocker: `EVIDENCE_INCOMPLETE`, not a scientific loss or strict-gate
  miss. The selected mechanisms have not yet been executed.
- Strict gate sole blocker: no; there is no opened empirical result to promote.
- Immediate high-impact unlock: agent executes T079's exact conditional-orbit
  theorem/tractability/variance sequence. No owner action or threshold change
  is required.

## Reproduction

```bash
bash experiments/checkpoint3/t078/verify_evidence.sh
```

## Task timing

- Start: `2026-08-22T10:39:44,082837657-07:00`
- Pre-task estimate: `50 minutes`
- End/check-off: `2026-08-22T10:58:11,745318933-07:00`
- Actual wall-clock difference: `00:18:27.662481276`
  (`1107662481276` ns)
