# T090 — rejection-informed novelty recurrence under FFSP003

Status: **complete bounded theory/prior-art refresh; no protected candidate
outcome opened**.

Ledger event `E063` is a source/design decision. The public-source cutoff is
`2026-08-22T19:51:32-07:00`. The project `P1-promising` pool remains empty.

## Decision

Run new `H090-B`, the leverage-exact Haar-Stiefel antithetic tight-frame
estimator, in T091. If it terminates without a project P1, run new `H090-A`,
balanced gate-risk affine-suffix continuation, in T092. If both terminate
without P1, T093 repeats novelty generation and reranks parked `H090-C`.

`H084-B` was reranked for the third time, not inherited. It now scores `51.25`,
below the unchanged `55` floor, and is priority-closed without an empirical
scientific test. Its exact estimator remains lawful and untested; the closure
means that the expected value of testing it is lower than the new alternatives,
not that its mechanism has been falsified.

`H090-B` receives provisional `N2-NOVEL-MECHANISM`, novelty dimension `3`.
Whitening, Haar-Stiefel frames, random positive quadrature and spherical
designs are public. The bounded audit found no exact description of the full
interaction: normalize the rows of a Haar-Stiefel frame, use their leverage
scores as positive quadrature weights, analytically integrate the Gaussian
radius by homogeneity, and antipodally evaluate the deep network. The result is
unbiased and exactly balanced through angular degree three for every frame.
That is a plausible academic mechanism, not proof of global novelty.

No owner action is required. `FFSP003` applies prospectively. An oracle may
authorize a lawful test but cannot award M1. Before either selected candidate
opens a complete F0--F3 outcome after lawful M1, the T066 decision adapter must
be requalified for `FFSP003`.

## Failure and policy reconciliation

| Evidence | Observation | Surprise from frozen prior | Consequence |
|---|---:|---|---|
| T088 / H087-A | lawful candidate/direct `0.997123`, `1/12`; selected/fixed `0.974014` | pre-M1 rejection had probability `.55`: **expected**, `0.862496` bits | Close the exact rank-six hidden-response fingerprint; collective estimator balancing must replace another hidden basis retune |
| T089 / H087-B | optimistic variance-cost `1.608477`, `0/12`, range `1.254406–1.996889` | pre-M1 rejection had probability `.63`: **expected**, `0.666576` bits | Close inverse-survival depth telescopes; one fixed-size residual decision may remain testable |
| T083 / H081-B | optimistic `0.852166`, `11/12`, max `1.027672` | historical strict-gate-limited support | These numbers clear the new FFSP003 M1 thresholds, but omitted-cost oracle evidence cannot award M1; H090-A materially changes allocation and must earn lawful evidence |
| T085 / H084-A | target-aware `0.905089`, `10/12`, max `1.092443` | historical modest favorable direction | These numbers also clear the new numerical thresholds, but target-aware evidence cannot award M1 and the rejected fingerprint is not reopened |
| D002 / LB001 | complete pooled F3 `0.396077`; external calibration P1 | not a project outcome | Confirms the prospective funnel can admit a rank-15 public estimator; it does not promote any project candidate |

The rejection *categories* for T088 and T089 were unsurprising. T089's severe
loss is scientifically stronger than T088's near-null, but its exact magnitude
was not a separately frozen outcome category; no post-outcome probability is
invented.

## Dated prior-art and duplicate boundary

The refresh covered the official challenge and contribution guidance, the
updated Phase 1 census/frontier, public whitening and antithetic measurements,
complete MUB/Kerdock estimators, mid-network controls, randomized QMC,
Haar-Stiefel distributions, random positive spherical quadrature, fixed-size
PPS/Horvitz-Thompson sampling, generalized approximate control variates, and
every local semantic fingerprint through the cutoff.

Public Phase 1 evidence reports batch whitening at about `2.0x–2.34x`, and
`2.86x` with antipodal pairing. It also reports that low-discrepancy sampling
adds no resolved gain once whitening is present. Those are external design
measurements, not H090-B results. The public construction is described as
forcing the realized batch covariance and is not, for a nonlinear integrand,
the exact leverage-weighted sphere identity frozen here.

Public literature already establishes the broad ingredients:

- Gaussian QR produces a Haar-Stiefel frame and its distribution is
  orthogonally invariant;
- optimized positive random quadrature on spheres/manifolds and spherical
  polynomial exactness are established topics;
- fixed-size unequal-probability sampling and Horvitz-Thompson correction are
  established and can dominate with-replacement allocation; and
- approximate control variates with independently estimated means are public.

The local duplicate scan found only broader frame/subframe coverage and no
prior occurrence of any new canonical string or SHA-256. H090-A is not H081-B:
the latter's unopened implementation branch already used a *uniform* fixed
count. H090-A freezes positive, path-dependent inclusion probabilities from a
lawful affine margin-risk statistic and an exact systematic PPS residual
correction. It is also not H087-B: there is one selection and no depth-survival
inverse tail. H090-B is not ordinary whitening: it replaces transformed
non-Gaussian rows by uniform row directions, analytic radius, and leverage
weights whose frame identity is exact. H090-C controls complete-MUB rotation
error rather than reallocating basis residuals as H084-A did.

Absence from this bounded search is not proof of worldwide novelty. Dimension
`4` is withheld because each ingredient has close prior art, the public
whitening descriptions may contain unpublished implementation overlap, and no
external review has isolated the claimed interaction.

Sources:

- [Official ARC challenge page](https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026)
- [ARC algorithmic-contribution guidance](https://discourse.aicrowd.com/t/algorithmic-contribution-prize-guidelines-how-arc-judges-these-prizes-discretion-technical-writeups-llm-usage/18041)
- [Updated Phase 1 technique census](https://discourse.aicrowd.com/t/a-technique-census-of-phase-1-what-the-mathematics-is-doing-what-walls-it-hit-and-whats-still-open/18157)
- [Current Phase 1 frontier and Phase 2 lever synthesis](https://discourse.aicrowd.com/t/phase-1-solution-ideas-for-phase-2-and-the-honest-public-frontier-all-methods-combined-and-explained/18193)
- [Primary Phase 1 research atlas](https://discourse.aicrowd.com/t/phase-1-research-atlas-how-i-reached-public-16-and-why-the-next-56-experiments-failed/18159)
- [Public unbiased RQMC result](https://discourse.aicrowd.com/t/unbiased-randomized-qmc-rao-blackwell-for-post-relu-activation-means-method-unbiasedness-proof-and-where-the-frontier-is/18053)
- [Public intra-network control result](https://discourse.aicrowd.com/t/phase-1-write-up-monetizing-the-approach-to-the-moment-propagation-frontier-an-intra-network-control-variate-and-a-measured-map-of-the-wall-behind-it-submission-326024/18154)
- [Haar-Stiefel row empirical-measure analysis](https://arxiv.org/abs/2105.04685)
- [Positive random quadrature on closed manifolds](https://link.springer.com/article/10.1007/s11222-019-09894-w)
- [Fixed-size conditional-Poisson versus with-replacement sampling](https://www.sciencedirect.com/science/article/pii/S0378375807002728)
- [Generalized approximate control variates](https://www.sciencedirect.com/science/article/pii/S0021999120300310)

## Frozen ranked hypothesis slate

The unchanged score is

`S = (35*N + 30*E + 15*C + 20*R) / 4`,

with integer dimensions `0–4`, floor `55`, ties broken by N/R/E/C, and at
most two scheduled candidates before recurrence. The final-outcome surprise
rule remains `I=-log2(q)`: `q>=.50` expected, `.25<=q<.50` mildly surprising,
`.10<=q<.25` strongly surprising, and `q<.10` very surprising.

| Rank | Hypothesis | Provenance | Novelty | N/E/C/R | Score | Frozen final-outcome probabilities | Decision |
|---:|---|---|---|---|---:|---|---|
| 1 | `H090-B` leverage-exact Haar-Stiefel antithetic tight frame | `OURS+PUBLIC` | provisional `N2-NOVEL-MECHANISM` | 3/3/4/4 | `83.75` | reject pre-M1 `.57`; M1 then no P1 `.25`; P1 `.18` | T091 |
| 2 | `H090-A` balanced gate-risk affine-suffix continuation | `OURS+PUBLIC` | `N1-NOVEL-COMBINATION` | 2/3/4/4 | `75.00` | reject pre-M1 `.61`; M1 then no P1 `.24`; P1 `.15` | T092 if no T091 P1 |
| 3 | `H090-C` rotation-level subframe ACV for complete MUB | `OURS+PUBLIC` | `N1-NOVEL-COMBINATION` | 2/2/3/4 | `63.75` | reject pre-M1 `.72`; M1 then no P1 `.20`; P1 `.08` | parked for T093 |
| 4 | `H084-B` symmetric kink-energy vMF importance | `OURS+PUBLIC` | `N1-NOVEL-COMBINATION` | 2/1/3/3 | `51.25` | reject pre-M1 `.89`; M1 then no P1 `.09`; P1 `.02` | below-floor priority closure |

These priors are prospective subjective design probabilities, not empirical
evidence. The selected-pair chance of at least one P1 under independence would
be `1-(1-.18)(1-.15)=.303`; dependence and shared benchmark assumptions make
that arithmetic descriptive, not a calibrated guarantee.

## H090-B — leverage-exact Haar-Stiefel antithetic tight frame

Let `Q` be Haar on the Stiefel manifold `V_d(R^n)`, with `Q^T Q=I`. For row
`q_i`, define leverage `ell_i=||q_i||^2` and direction
`u_i=q_i/sqrt(ell_i)`. Orthogonal invariance makes `u_i` uniform on the sphere
and independent of `ell_i`, with `E ell_i=d/n`. For the exact mean Gaussian
radius

```text
rho_d = sqrt(2) Gamma((d+1)/2) / Gamma(d/2)
```

and the degree-one homogeneous network `f`, freeze

```text
Z = (rho_d/d) sum_i ell_i [f(u_i)+f(-u_i)]/2.
```

Then `E Z=E f(G)` exactly. For every realized frame,
`sum_i ell_i u_i u_i^T=I`; normalized positive weights integrate every
angular quadratic exactly, and antipodes cancel every odd polynomial. Thus the
rule is a positive randomized spherical degree-three rule, not a biased
whitened Gaussian batch.

T091 first validates QR/Haar invariance, leverage sums, angular moments,
homogeneity, exact-target Monte Carlo, source identity and replay. Its lawful
12-network width64 screen uses 128 independent `128 x 64` Stiefel blocks per
network and compares equal full-path work to iid spherical antithetic sampling.
The FFSP003 M1 default is pooled ratio `<=.99`, at least `7/12` wins, and
maximum `<2`. Equal-weight row-normalized Stiefel is the mechanism isolation
ablation; candidate/ablation `<=.99` is required to retain provisional N2,
but its disposition must be reported separately from the primary scientific
comparison.

On lawful M1, requalify the T066 adapter for FFSP003 before opening any
complete candidate outcome, then charge QR/frame construction, normalization,
weights, full paths, rounding and reserve inside `261B` and run F0–F3 without
a pause. Most likely failure: the public gain comes from row normalization
rather than leverage weighting, or degree-three balance cannot compete with
the public complete-MUB carrier.

Semantic fingerprint:
`2ad2aca8f8b91115269fc77f972a2b3bf0c2a7a7152796f4683c266df7803204`.

## H090-A — balanced gate-risk affine-suffix continuation

For a batch of `N` antithetic prefixes, compute T025's collapsed affine suffix
pair means `A_i`. Before any exact suffix outcome is known, compute a frozen
nonnegative risk score from the affine suffix's propagated signed margins and
gate-leakage bounds. Deterministic capped water filling creates positive
inclusion probabilities `pi_i`, with a uniform floor and integer sum `m`.
A randomized cyclic systematic-PPS draw selects exactly `m` pairs and gives
each pair its declared first-order inclusion probability. For nonlinear
residual `R_i=Y_i-A_i`, freeze

```text
Z = mean_i A_i + (1/N) sum_{i selected} R_i/pi_i.
```

Conditional on every prefix and residual, `E[Z]=mean_i Y_i`. This is one
fixed-size selection, not H087-B's inverse-survival telescope. It materially
changes H081-B: that fingerprint's unopened lawful branch selected a uniform
fixed count, whereas H090-A uses a target-free pathwise statistic and unequal
exact inclusion correction.

T092 uses pilot/evaluation-separated folds on 12 width64 networks. It must
verify exact inclusion marginals and count, conditional target recovery,
uniform-limit reduction, T025 equivalence and replay. Under FFSP003, lawful
candidate/uniform-fixed-count must be `<=.99`, with at least `7/12` wins and
maximum `<2`; equal-work direct is mandatory context. An oracle can choose a
frozen score/cut family but cannot award M1.

On M1, requalify the T066 adapter if T091 has not already done so, then charge
scores, selection, affine maps, selected exact suffixes, rounding and reserve
inside `261B` and run F0–F3. Most likely failure: affine margin risk is a poor
proxy for nonlinear residual energy, or unequal weights and administration
consume H081-B's `14.8%` optimistic signal.

Semantic fingerprint:
`68e36d74fe438390cff63d1dc7cbe58a418415ac6890b6262d583b52e932dd01`.

## H090-C and H084-B dispositions

`H090-C` uses one complete Haar-rotated MUB output `Q(R)`, a fixed subframe
output `A(R)` already contained in it, and independent cheap Haar subframe
outputs to estimate `E A`. A pilot-frozen diagonal response gives

```text
Q(R0) - B [A(R0) - mean_j A(Rj)].
```

The bracket has exactly zero expectation. This controls randomized cubature
orientation error at the final output, unlike H084-A's within-orientation
basis allocation or the rejected hidden controls. It stays parked because
the complete-MUB carrier already has external P1; a future test must isolate
the correction and cannot misattribute the public carrier's success.
Fingerprint:
`31373be9160b677759032b8f93e6cb8d463a8e454c40572d4a475fd044ae9496`.

H084-B keeps fingerprint
`ce4f4c2fe7ceb7bb19d4b240435da2b41e5c2de1dd1c0d3d8979b536a9357900`.
It falls below the floor after three explicit rerankings because local
direction selection has repeatedly been null/adverse, public target-free
selection has failed to transfer, and collective exact balancing now has
stronger external evidence. It is not scientifically rejected; it is closed
as a research priority unless genuinely new evidence changes the slate.

## Human promotion disposition

- Subject/evidence: E063/T090 source/design audit; three new exact hypotheses,
  one parked hypothesis reranked, no protected candidate outcome.
- Current/highest/next tier: project P1 remains empty; H090-B next considers
  lawful M1 in T091 under FFSP003.
- Strongest positive evidence: external public whitening reports `2.0x–2.34x`
  and project H081-B oracle `0.852166`, `11/12`; neither is an H090 outcome.
- Gate status: recurrence, failure reconciliation, two-new-hypothesis
  admission, exact identities, duplicate audit, ranking, complete routes and
  priors `PASS`; candidate M1, registration, F0–F3 and project P1 `NOT-RUN`.
- Strict-gate margin: not applicable to a source/design task. Historical
  H081-B/H084-A signals are explicitly not promoted by the new policy.
- Primary blocker: `EVIDENCE_INCOMPLETE`.
- Why not promoted: novelty is not efficacy, and no selected estimator has yet
  produced lawful heldout evidence.
- Immediate high-impact unlock: the agent executes H090-B/T091. No machine
  owner action is required.

## Verification

```bash
bash experiments/checkpoint3/t090/verify_evidence.sh
```

## Task timing

- Start: `2026-08-22T19:41:33,182049897-07:00`
- Pre-task estimate: `45 minutes`
- End/check-off: `2026-08-22T20:00:15,191528740-07:00`
- Actual wall-clock difference: `00:18:42.010861757`
  (`1122010861757` ns)
