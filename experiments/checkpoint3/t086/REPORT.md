# T086 — exact spherical Stein/JVP path-control adjudication

## Decision

Reject unchanged `H081-C` before M1 and proceed to T087's required novelty
recurrence. The held-out selected-control/direct work-normalized ratio was
`2.180344051022253` against the frozen strict `<0.90` gate. It missed by
`1.280344051022253` absolute (`142.2605%` of the threshold), lost all `12/12`
network comparisons, and reached a maximum network ratio of
`3.706704741462621` against `<1.25`.

This is a strong scientific rejection, not merely a cost-accounting or strict-
gate rejection. Before charging JVP work, the pooled corrected trace variance
was already `1.080673914930681` times direct antithetic variance, so the frozen
response worsened raw variance by `8.0674%`. Charging its still-optimistic
`528,896` operations per observation versus direct's `262,144` made the loss
larger. Direction selection did provide weak ablation evidence: the selected
control was `0.977509874189548` of the fixed-axis control, a `2.2490%`
improvement, but it missed the frozen `<0.95` mechanism gate by
`0.027509874189548` (`2.8958%` of that threshold).

M1, complete width256 registration and charging, FC004/F0--F3, and P1 were
correctly not run. No `ALG` identity, tier, competitive rank, protected fast
outcome, or official claim changed.

## Frozen estimator and identities

For each width64/depth32 deterministic bias-free ReLU network, T086 formed the
T025 expected-gate Jacobian and selected its leading left singular direction
by 64 fixed power iterations. The comparator direction was the first input
coordinate. At unit-sphere point `u`, direction `a`, and output vector `f`, the
zero-mean control was

```text
C_a(u) = D_a f(u) - 64*(a dot u)*f(u).
```

The executable propagated `D_a f` through the exact realized ReLU gates. A
512-pair pilot fold independently fit the frozen full 64-by-64 ridge response;
a disjoint 512-pair evaluation fold supplied every reported variance and gate.
Both output and control were multiplied by the exact mean chi radius. The
optimistic M1 screen charged the two signed forward paths, their tangents, the
dense response correction, and administration, while omitting direction
construction, all pilot sampling, covariance/Cholesky work, rounding, and
reserve. Those omissions favor H081-C and cannot rescue this rejection.

All six construction checks passed:

| Check | Maximum observation | Limit / disposition |
|---|---:|---:|
| selected-direction norm error | `3.33e-16` | `<=2e-14`, PASS |
| analytic linear spherical identity error | `0` | `<=2e-13`, PASS |
| radial homogeneity error | `1.24e-14` | `<=2e-11`, PASS |
| selected JVP finite-difference error | `5.26e-11` | `<=2e-7`, PASS |
| fixed JVP finite-difference error | `2.07e-10` | `<=2e-7`, PASS |
| response-system solve residual | `2.13e-14` | `<=2e-8`, PASS |

Finite-difference steps were bounded by every realized-gate margin; the
minimum used step was `1e-5`. The minimum Cholesky diagonal was
`0.000935148`, so the fit was not accepted through a singular solve.

## Held-out gates

| Gate | Frozen requirement | Observation | Status |
|---|---:|---:|---|
| construction/JVP/replay | all pass | all pass; byte-identical | PASS |
| pooled selected/direct variance-cost | `<0.90` | `2.1803440510` | FAIL-SCIENTIFIC |
| network wins | `>=9/12` | `0/12` | FAIL-SCIENTIFIC |
| maximum network ratio | `<1.25` | `3.7067047415` | FAIL-SCIENTIFIC-TAIL |
| selected/fixed-axis variance-cost | `<0.95` | `0.9775098742` | FAIL-STRICT-EFFECT |
| M1 / registration / F0--F3 / P1 | sequential | not run | NOT-RUN |

The median selected/direct work ratio was `2.1361445074`; the best network was
still `1.8501162216`. Expected-gate selection amplified the expected linear
image by `4.08x` to `40.50x` relative to the fixed axis, but that proxy did not
translate to useful held-out control correlation after the nonlinear realized
gates.

## Implementation-defect audit

The evidence substantially reduces, but cannot make literally zero, the risk
of a hard-to-spot implementation defect. The strongest defenses are:

- two independent point domains and pilot-only fitting;
- analytic spherical and homogeneity checks;
- central finite differences bounded by realized-gate margins for both JVPs;
- deterministic Cholesky residual checks, source hashes, and byte-identical
  Windows verification/replay;
- a post-outcome independent GCC 13.3/Linux build of the exact sealed C++
  source (`7aa2384f...`). It reproduced the same decision, every gate, `0/12`
  wins, and the four main ratios within `2.20e-11` absolute (the pooled direct
  ratio differed by `8.87e-13`).

The GCC low-order floating-point checksum differs from MSVC as expected, while
the scientific disposition is far from every promotion boundary. A hidden
defect would therefore need to survive two compilers, the exact-identity and
finite-difference checks, cross-fitting, and replay while reversing a raw-
variance loss and a `2.18x` work result. That is possible in principle but not
a credible reason to continue unchanged H081-C.

## Human promotion disposition

- Subject / evidence class: H081-C width64 exact spherical Stein/JVP path
  control; synthetic held-out variance-cost evidence; no `ALG` registered.
- Current / highest supported / next considered tier: no new empirical tier;
  exact-control implementation support only; M1 was considered and rejected.
- Strongest favorable evidence: selected direction beat fixed axis by `2.249%`
  pooled and on `9/12` networks. This is weak direction-selection support, not
  estimator promise.
- Failed margins: direct `2.180344` versus `<0.90` (adverse `1.280344`);
  wins `0/12` versus `>=9/12`; maximum `3.706705` versus `<1.25` (adverse
  `2.456705`); fixed axis `0.977510` versus `<0.95` (adverse `0.027510`).
- Primary blocker: `SCIENTIFIC_NEGATIVE_VARIANCE_COST_AND_TAIL`; the strict
  gates are not the sole blocker because raw variance was adverse before cost.
- Why not promoted: realized-gate Stein controls did not reduce held-out
  variance, their JVP path approximately doubled observation cost, and the
  expected-gate direction supplied only a small advantage over an arbitrary
  fixed direction.
- Immediate high-impact unlock: none for unchanged H081-C and no owner action.
  T087 must use this failure signature to rerank H084-B against at least two
  materially distinct new hypotheses under new fingerprints.

## Novelty and surprise

H081-C remains an `OURS+PUBLIC`, `N1-NOVEL-COMBINATION` research hypothesis;
it did not become an algorithm candidate or academic submission claim. Its
exact fingerprint is closed. A successor must change the cost/correlation
mechanism, not the direction seed, ridge, folds, or gate.

T081 froze `.70` probability for rejection before M1. The result is therefore
**expected** at `-log2(.70) = 0.514573172829758` bits. The failure strength is
not surprising relative to the prior prediction that JVP cost and noisy Stein
terms would dominate.

## Operational record

Three controller-only failures were preserved before the accepted run. The
first exposed PowerShell `Start-Process -Wait` hanging after MSVC had exited;
the second established that the returned Windows `Process.ExitCode` property
was empty; the third produced the frozen rejection but was refused because an
inherited UNC-directory startup notice made stderr nonempty before replay.
Amendments 001--003 added bounded exact-process polling, batch-written exit
status, and an explicit Windows-local initial working directory. No estimator,
source, executable flags, outcome, cost, gate, fingerprint, or prior changed.
No owner action or reboot was needed.

The accepted Windows-native MSVC run began
`2026-08-22T14:45:36.7836593-07:00` and ended
`2026-08-22T14:45:46.6931858-07:00`, including verification and byte-identical
replay.

## Verification

```bash
bash experiments/checkpoint3/t086/verify_evidence.sh
```

## Task timing

- Start: `2026-08-22T14:25:14,199085012-07:00`
- Pre-task estimate: `60 minutes`
- End/check-off: `2026-08-22T14:52:26,536490818-07:00`
- Actual wall-clock difference: `00:27:12.337405806`
  (`1632337405806` ns)
