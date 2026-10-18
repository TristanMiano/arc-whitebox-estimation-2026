# T098 — one-hour deep hypothesis recurrence and FC005 adjudication

## Decision

FC005 is closed empty: both frozen decisions were scientifically rejected
before registration/F0, so there is no new rigorous-entry pool and T099 is not
activated.  The owner-directed one-hour return to hypothesis generation opens
FC006 on unused fast epoch `E0006` with two executable decisions:

1. **T103 / H098-D:** half-strength affine-subspace James--Stein residual
   shrinkage, the P1-facing candidate.  On reused historical evidence it is
   `0.904417` of the five-frame carrier, wins `10/12`, and has maximum `1.08445`.
   Its fresh P1 prior is frozen at `.45`, the highest assigned to a new
   internal candidate in the recent recurrences.
2. **T104 / H098-A with nested H098-B:** Phase-2 order-12 Price/Hermite closure
   plus a 288-row partial Haar headroom arm.  On reused Phase-2 evidence it is
   `0.943597` of exact `ALG015-V000`, wins `11/12`, and has maximum `1.01755`.
   The Hermite-only nested candidate is `0.963054`, wins `12/12`, and must be
   retained if the auxiliary arm does not replicate.  Official succession
   prior is `.60` for H098-A and `.55` for H098-B.

No new cohort, protected fast result, ALG identity, M1/P1 tier, official
submission, or submission-candidate succession occurred in T098.
`ALG015-V000` remains the official submission candidate.

## FC005 complete ledger

| Decision | Positive evidence | Terminal evidence | Why no registration/P1 |
|---|---|---|---|
| T096 / H095-C / ALG015-V000 | Current Phase-2 M1 `0.742026`, `12/12`, max `0.884449`; official adjusted `2.843538175e-7`, a 56.963% improvement over ALG014-V003 | Historical M1 `1.619843`, `2/12`, max `4.927358` | Scientific direction, breadth, and tail rejection before F0; current-shape submission succession remains valid and separate |
| T097 / H095-D / ALG016-V000 | Phase-2 raw MSE `0.594627` of ALG015; target-aware historical oracle `0.928454` of carrier | Phase-2 adjusted `1.705803` of ALG015; historical carrier ratio `1.407245`, `3/12`, max `2.215272` | Scientific aggregate/breadth rejection; cross-fitting gave independence but not a valid scalar bias/anisotropy model |

Both failures were scientific, not merely strict-gate mismatches.  FC005 has
zero registered candidates and therefore cannot feed rigorous Cycle 2.

## What the hour changed

The analysis did not begin from a list of cosmetic variants.  It reconstructed
the exact adjusted objective, derived break-even inequalities, killed two
apparently attractive compute reallocations, derived a higher-order covariance
closure, and then used T097's failure to construct a different shrinkage
theorem.

### 1. Falsified cheap-closure route

Replacing the `51.7B` full covariance closure with a cheap target would permit
roughly 50% more angular paths.  The derived requirement was cheap-closure MSE
below about `4.92e-6`.  Reused evidence gave diagonal MSE `2.21991e-4`
(`55.29x` full covariance).  A rank-`r` covariance-state sketch followed an
empirical `~0.045/r` error law and would need about 9,150 probes and `~307B`
dense FLOPs just to reach break-even.  Both routes are priority-closed.

### 2. Price/Hermite covariance correction

The current Gaussian closure uses only the first Price-series term

```text
sigma_x sigma_y rho Phi(a)Phi(b).
```

The notebook derives the exact series terms through arbitrary order using
Hermite coefficients.  An independent 150-case formula check reduced worst
absolute covariance error from `2.03e-2` at order 1 to `1.46e-8` at order 12;
the separate zero-mean arc-cosine formula matched within `5.56e-17`.

On six target-blind Phase-2 network diagnostics, median absolute correlations
grow from about `.021` at layer 1 to roughly `.075–.082` at layer 16, with
maxima about `.5–.59`.  The per-entry quadratic term is small but coherent
over about one million covariance entries.  This explains why adding only
`596.8M` closure FLOPs can lower closure MSE `4.61%` and the full blend `3.69%`.

### 3. Score-floor headroom

A reduced QR of a `1024 x 288` Gaussian matrix directly generates 288
orthonormal Haar directions.  The complete projected candidate costs
`216.710B`, leaving `3.193B` FLOPs for residual-time/implementation headroom.
The theory weight `1/17` follows from T091's approximately `2.25x` frame
efficiency and the relative path counts; the old-row fitted optimum `.09565`
was deliberately not adopted.

### 4. Correcting T097's bad-target assumption

H098-D projects the five-frame estimate onto `span{1,C}` and applies
half-strength positive-part James--Stein shrinkage only to the orthogonal
residual.  Under isotropic Gaussian carrier error, subspace shrinkage dominates
the carrier for every true mean; closure need not itself be accurate.  Half
strength remains inside the classical dominance interval and sharply improves
the old tail compared with full strength (`1.084` versus `1.308` maximum).

The Gaussian/isotropic theorem is not silently transferred to the contest.
Frame errors can be anisotropic and non-Gaussian, and the block-pooled variance
is estimated.  Those are the fresh-test risks behind the `.45` P1 prior.

The notebook now derives the unknown-variance result rather than borrowing the
known-variance theorem.  With `K=5`, `p=256`, the pooled variance has
`nu=1024`; the shrinkage coefficient remains risk-improving for
`0<c<2/(1+2/nu)=1.99610`.  The selected `c=.5` is comfortably inside that
interval.  An 840,000-trial synthetic audit (42 cases x 20,000) first found
improvement under Gaussian/Student-`t_5` noise and ordinary anisotropy, then
found the actual failure boundary under adversarial covariance spikes.  If
one signal-aligned direction carries more than 37.5% of covariance trace,
half-strength shrinkage can lose; a 90%-of-trace spike produced `1.13572x`
risk.  Reused block deviations reject isotropy: their leading sample mode
carries `0.348`--`0.566` of trace versus an isotropic-null 99.9th percentile
of `0.341`.  A top-noise-mode protection ablation trims the reused maximum
from `1.084` to `1.074` but weakens aggregate gain from `0.904` to `0.937`.
A conservative trace guard, derived from the generalized Stein risk bound,
further limits the maximum to `1.008` while retaining ratio `0.975` and `9/12`
wins.  In all synthetic cases its risk ratio was `0.646995`--`1.000011`; in
the six deliberate spike cases it remained essentially neutral
(`0.998959`--`1.000011`) while the primary reached `1.135717`.  T103 must
report the primary and both covariance ablations.  This audit is theory/
implementation evidence only, not candidate evidence, and does not alter the
prospectively frozen prior.

Fresh implementations must use the notebook's density-weighted Hermite
recurrence and frozen `|alpha|>12` zero-tail guard.  This prevents the hidden
`inf*0 -> NaN` risk of forming a high-order polynomial before multiplying by
an underflowed Gaussian density.  T103/T104 must charge and replay-validate
the guard before opening outcomes.

## Rejections and surprises during generation

| Route | Result on reused evidence | Prior expectation | Update |
|---|---|---|---|
| Diagonal closure plus 3 bases | `~45x` above break-even | Plausible but lower confidence | Severity surprising; correlations are indispensable |
| Rank covariance sketch | exact `1/r` error, thousands of probes needed | Moderate chance low-rank structure would help | Negative and stronger than expected |
| Square bases replacing tall frames | historical `1.564845`, `3/12`, max `3.636` | Small possible degree-two gain | Severity surprising; closes exact-degree-two carrier route |
| Fixed small historical Hermite shrinkage | lambda `.01` ratio `1.00301`, `4/12` | Expected weak | Confirms Phase-2 closure is shape-specific |
| Order-12 Hermite Phase-2 blend | `0.963054`, `12/12` | Expected sign, uncertain magnitude | Favorable magnitude; broadly consistent |
| Partial-Haar headroom arm | `0.979797` of Hermite control, `9/12` | About `~1.2%` total gain | Favorable and somewhat larger than projected |
| Half-strength affine-subspace shrinkage | `0.904417`, `10/12`, max `1.084` | Theorem suggested positive direction; contest assumptions uncertain | Favorable magnitude and breadth; raises P1 prior to `.45` |

These are hypothesis-generation updates on already-opened evidence, not formal
fresh scientific promotions.  T103/T104 freeze exact implementations and open
new evidence.

## Novelty boundary

The selected mechanisms are academically plausible but not claimed as new
statistical principles.  Price's theorem, Hermite covariance expansions,
Gaussian assumed-density propagation, orthogonal Monte Carlo, and
James--Stein shrinkage toward a subspace are public.  H098-D and H098-A are
`N1-NOVEL-COMBINATION`, novelty dimension 3: their exact interactions and ARC
cost/risk compositions were not found in the bounded local/public census.
Worldwide novelty is not proven.  H098-D is more suitable for a scientific
contribution claim because it is a direct, falsifiable correction of ALG016's
identified assumption failure; H098-A is primarily a contest-score mechanism.

## Human promotion disposition

- Current best: `ALG015-V000`, official adjusted `2.843538175e-7`; unchanged.
- FC005: empty and closed; no strict-only blocker and no rigorous entry.
- H098-D: selected but unregistered; M1/P1 not run.  Why not promoted: all
  favorable numbers reuse opened rows and Gaussian/isotropic assumptions are
  not established.  Immediate unlock: execute T103 on fresh evidence.
- H098-A/H098-B: selected but unregistered; current-shape M1/succession not
  run.  Why not promoted: cost is a component preflight and accuracy is reused
  evidence.  Immediate unlock: execute nested T104 after T103.
- Owner action: none.

## Timing

- Start: `2026-08-26T17:06:59.816301010-07:00`
- Pre-task estimate: `65 minutes`
- Minimum-work constraint: one full wall-clock hour before check-off
- End/check-off: `2026-08-26T18:08:19,058276152-07:00`
- Elapsed: `01:01:19.241975142` (`3679241975142` ns)

## Verification

```bash
bash experiments/checkpoint3/t098/verify_evidence.sh
```
