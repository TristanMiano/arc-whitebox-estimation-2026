# T095 — extended post-RC001 theory recurrence and FC005 freeze

Status: **complete prospective theory/prior-art decision; no selected outcome
opened**.

The initial 17-minute pass was reopened at the owner's request before T096.
The extension started at `2026-08-25T22:20:52,728895692-07:00`, ran for at
least thirty additional minutes, and produced the derivations in
`THEORY_NOTEBOOK.md`. This was not ceremonial extra time: it invalidated the
initial first choice and replaced both executable decisions.

Timing: original estimate `35 minutes`; original start
`2026-08-25T21:58:13,313210771-07:00`; final check-off
`2026-08-25T22:50:56,671256756-07:00`; full wall span
`00:52:43.358045985`. The owner-requested extension itself took
`00:30:03.942361064`; cumulative recorded work intervals were
`00:47:28.963644694`.

The public-source cutoff is `2026-08-25T22:46:13-07:00`. The historic P1 pool
still contains only `ALG014-V000`; the current official Phase-2 candidate is
`ALG014-V003`. No new ALG identity, protected FC005 result, scientific tier,
official grade, or submission succession is claimed by T095.

## Material result of the deeper analysis

The initially selected `H093-A` complementary-frame construction is a
theoretical null. Conditional on its first Stiefel block, the complementary
block equals a fixed complement basis times an independent Haar right
orientation. Averaging that orientation makes every row-normalized estimator
coordinate equal to the exact target. Therefore the covariance of the two
block estimates is exactly zero, not negative. Their equal average has the
same variance as two independent frames and likely greater construction cost.

`H093-A` is priority-closed before M1 without spending candidate compute. Its
target validity remains true; its claimed complement-induced cancellation does
not. This is a theoretical rejection of the proposed mechanism, not an
implementation failure, protected empirical outcome, or strict-gate miss.

The second major result is an exact shrinkage identity. For unbiased randomized
frame estimate `F`, deterministic covariance-propagation estimate `C`, target
`mu`, and closure weight `lambda`,

```
E ||(1-lambda)F + lambda C - mu||^2
  = (1-lambda)^2 E||F-mu||^2 + lambda^2 ||C-mu||^2.
```

The cross term vanishes exactly. This gives both a mechanism with a known
beneficial interval and a way to use the Phase-2 score floor deliberately.

## Current-shape projection, clearly not a result

Official T075 gives four-frame `ALG014-V003` raw final-layer MSE
`2.509378157355968e-6`, adjusted score `6.607199502584784e-7`, and multiplier
`0.2632926421574666`. A 2026-08-24 participant report attributes six tied
Phase-2 entries at adjusted `3.93e-7` / raw `3.93e-6` to plain covariance
propagation. The attribution is plausible but not organizer-certified.

Four independent frame blocks imply a one-block estimator variance four times
the four-block variance. Because an official MSE can also contain residual
finite-reference error, four times the reported MSE is used as a conservative
one-block upper projection rather than claimed as exact. Combining one block
at weight `1/4` with full covariance at weight `3/4` therefore projects:

| quantity | prospective value |
|---|---:|
| one-frame variance | `1.0037512629423872e-5` |
| blended raw MSE | `2.837969539338992e-6` |
| conservative combined charged FLOP upper projection | `197,455,901,579` |
| Phase-2 0.1 score-floor FLOPs | `219,902,325,555.2` |
| adjusted score if floor holds | `2.837969539338992e-7` |
| ratio to official `ALG014-V003` | `0.429527` |
| vs sampling approximation | `4.228x` |

This is not a candidate score: it combines two aggregate sources and has no
new-estimator outcome. Its useful feature is robustness. At closure/four-frame
raw-MSE ratio `r`, the blend risk in four-frame units is
`0.25 + 0.5625*r`; it remains an adjusted-score win over `ALG014-V003` while
`r < 4.2363`, versus the public working value `1.5661`. Exact combined package
cost and fresh outcomes remain mandatory.

Historical width-256/depth-32 closure evidence is adverse. T096 must therefore
publish separate current-Phase-2 submission-facing and historical FFSP003
scientific dispositions. A historical P1 failure cannot be hidden, but under
the audited submission policy it also cannot ban a current-shape score winner.

## Theory-updated ranked hypothesis slate

The unchanged priority score is
`S=(35*N+30*E+15*C+20*R)/4`, with dimensions 0–4, floor 55, and at most two
selected decisions. Scores are theory priorities, not evidence.

| Rank | Hypothesis | family / provenance | novelty | N/E/C/R | score | frozen terminal prior: pre-M1 / M1-no-P1 / P1 | decision |
|---:|---|---|---|---|---:|---|---|
| 1 | `H095-C` one-frame + 3/4 covariance score-floor shrinkage | current-shape tail-safe collective/analytic blend; `OURS+PUBLIC` | `N1` | 2/4/4/4 | `82.50` | `.28 / .32 / .40` | T096 |
| 2 | `H095-D` cross-fitted positive-part Stein shrinkage | lawful adaptive mixer; `OURS+PUBLIC` | `N1` | 2/3/3/4 | `71.25` | `.50 / .25 / .25` | T097 |
| 3 | `H095-E` trace-orthogonal right-orbit Stiefel frame | collective orientation orbit; `OURS+PUBLIC` | provisional `N2` | 3/2/3/3 | `67.50` | `.66 / .20 / .14` | parked for theory screen |
| 4 | `H095-B` median scrambled spherical Sobol replicates | non-Haar robust RQMC; `OURS+PUBLIC` | `N1` | 2/2/4/4 | `67.50` | `.73 / .19 / .08` | parked |
| 5 | `H095-A` pilot-gated frame/Sobol allocation | lawful router; `OURS+PUBLIC` | `N1` | 2/2/3/3 | `58.75` | `.80 / .16 / .04` | parked |
| 6 | `H093-B` weight-fixed Haar involution | orientation antithetic; `OURS+PUBLIC` | `N1` | 2/1/4/3 | `55.00` | `.88 / .10 / .02` | parked at floor |
| 7 | `H093-A` complementary frames | proved covariance-null | construction provisional `N2`, mechanism null | 3/0/4/2 | `51.25` | `1 / 0 / 0` | theory-closed |

The first selected P1 prior rose from the initial `.14` to `.40`; the second
rose from `.06` to `.25`. The increase is not cosmetic. It is supported by the
exact bias/variance identity, the official score multiplier and frame MSE, the
public closure aggregate, and a broad prospective robustness interval. The
priors remain below 0.5 because the public attribution is inferred, one
realized frame can have a nonzero sample cross term, exact combined cost is not
yet measured, and historical-shape P1 transfer is uncertain.

Outcome surprise uses the frozen category probability `q` and
`I=-log2(q)`: `q>=.50` expected, `.25<=q<.50` mildly surprising,
`.10<=q<.25` strongly surprising, and `<.10` very surprising. Submission-facing
adjusted win probability for `H095-C` is separately frozen at `.62`; it is not
a P1 probability.

## Frozen decision 1 — H095-C / T096

Implement one exact 2048x1024 Haar-Stiefel frame block with the T074 antipodal,
mean-chi-radius, and exact-first-layer behavior. Independently compute bundled
float32 full covariance propagation. Return `0.25*frame + 0.75*closure` at every
layer. The weights are fixed before an outcome.

First requalify an outcome-blind current-shape FFSP003 adapter and measure exact
combined package FLOPs without opening candidate accuracy. A project P1 cannot
be awarded by an ad hoc Phase-2 score check.
The Phase-2 score-floor premise fails if cost exceeds `219,902,325,555.2`.
Current-shape M1 then requires candidate/best-fixed-endpoint adjusted ratio
`<=0.99`, at least `7/12` wins on the lawful mechanism cohort, and maximum
paired ratio `<4`. Pure one-frame and pure covariance are the frozen endpoints;
the official-four-frame arm is a mandatory succession ablation. A directly
comparable adjusted win over
`ALG014-V003` triggers the owner's **new submission candidate** rule even if
historical P1 fails.

T096 must also run or explicitly adjudicate the historical FFSP003 scientific
route with its nearest valid four-frame carrier and `ALG003-V008` context.
Current-shape score viability and historical P1 are separate fields; neither
may silently substitute for the other.

Fingerprint SHA-256:
`5e55139a1862af5d42f7e73ee8ab87574033f14bd0ae31f5006c906290e015d0`.

## Frozen decision 2 — H095-D / T097

Use four independent frame blocks in two pairs. Each pair difference estimates
single-block average coordinate noise for the opposite pair mean; divide that
variance by two for the pair mean. Shrink each pair mean toward deterministic
covariance propagation using the positive-part James-Stein form, clip to
`[0,1]`, then average the cross-fitted estimates. Cross-fitting makes the
applied carrier and scalar noise estimate independent.

Classical James-Stein dominance is not transferred: it assumes Gaussian,
isotropic, known-variance errors, while deep frame errors are anisotropic and
the variance is estimated. FC005 M1 requires pooled candidate/four-frame ratio
`<=0.99`, at least `7/12` wins, maximum `<2`, finite unit-interval shrink
factors, and exact opposite-pair cross-fitting. The target-aware oracle is
report-only. On M1, register and fully charge every frame, covariance pass,
noise calculation, blend, path, rounding operation, administration, and
reserve before F0–F3.

Fingerprint SHA-256:
`f47a04ff3ebcd75bf166645a43d370da10b4eb54afd25beb5845e5209a7bac30`.

## Required family coverage and parked reserve

- `H095-C` is the tail-safe collective/current-shape analytic blend.
- `H095-D` is the lawful adaptive mixer.
- non-Haar `H095-B` remains parked and independently falsifiable.
- novelty-dimension-3 `H095-E` directly couples right orientation, unlike the
  proved-null complementary subspaces. It must first pass an outcome-blind
  arc-cosine/NNGP harmonic screen predicting ratio `<0.98`.

The exact candidate definitions, controls, incumbents, kill rules, charged
routes, provenance, priors, and fingerprints are machine-readable in
`NOVELTY_SLATE.json`. Absence from the bounded scan is not worldwide novelty
proof.

## FC005 initialization and routing

FC005 remains frozen empty on fresh epoch E0005; no protected route was read.
The historical T065 v2.1 checker still reaches its expected post-seal
registration-projection failure. Before complete F0 output, T096 must extend
and requalify the current adapter using T091's bounded precedent. It must not
mutate the historical seal, silently ignore the failure, or ask the owner to
repair an agent-side adapter.

T096 now executes `H095-C`; T097 follows with `H095-D`; T098 adjudicates and
reranks. Stop at scientific rejection, but preserve current-shape
submission-facing evidence separately as required by the audited rules.

Sources added by the extension:

- [AIcrowd participant covariance-propagation attribution](https://discourse.aicrowd.com/t/covariance-propagation-baseline-scores-3-93e-7-3-93e-6/18198)
- [Phase-1 variance/bias hybrid write-up](https://discourse.aicrowd.com/t/phase-1-write-up-a-variance-bias-budget-for-deep-white-box-mean-estimation-submission-317660/18085)
- [Phase-1 analytic/Monte-Carlo fusion write-up](https://discourse.aicrowd.com/t/phase-1-write-up-monetizing-the-approach-to-the-moment-propagation-frontier-an-intra-network-control-variate-and-a-measured-map-of-the-wall-behind-it-submission-326024/18154)
- [Antithetic variates in higher dimensions](https://arxiv.org/abs/0902.4211)
- [Quasi-Monte Carlo Methods for Simulation](https://informs-sim.org/wsc03papers/011.pdf)
- [The James-Stein Estimator](https://stat210a.berkeley.edu/fall-2024/reader/jamesstein.html)

See `THEORY_NOTEBOOK.md` for the full complement proof, angular-lattice bound,
right-orbit argument, shrinkage derivation, score-floor calculation, and
assumption audit.
