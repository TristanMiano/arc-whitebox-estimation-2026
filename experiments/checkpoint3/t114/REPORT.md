# T114 — H113-L LPITF terminal competition decision

## Outcome

T114 closes the exact H113-L LPITF spelling **before protected-target access**.
No frozen N1 arm passed competition rule (212), so there was no direct Mini
comparison, algorithm ID, package, upload, tier change, or succession.
`ALG019-V000` remains the local and official best submission candidate,
official submission `328762`.

The nearest arm was `full-r16-retained-gap`:

| Quantity | Frozen result |
|---|---:|
| expected adjusted score | `2.575645581229e-7` |
| local ALG019 adjusted reference | `2.438182936200e-7` |
| candidate / local incumbent | `1.056379135` |
| bootstrap `P(adjusted win)` | `0.000000` |
| cross-fitted mean raw change | `-3.895813117e-8` |
| positive-`S` networks | `59/100` |
| gap-qualified networks | `36/100` |
| fitted `(h0,h1,h_rest)` | `(.0308214,.165083,0)` |

The correction reduced the retained deterministic-alpha base's raw-risk
proxy, but not enough to offset that base's distance from ALG019 and the
candidate's measured compute. Its point forecast is 5.64% above the local
incumbent, so this is a competition-negative result at the point estimate,
not a rejection caused solely by a strict confidence gate.

## What ran

The implementation imports the immutable T108 `ALG019` family and builds the
exact mean-transport factors

```text
A_l = diag(Phi(alpha_l)) W_l^T,          M = A_L ... A_2.
```

For ranks `{8,16,32}` with oversampling four, it applies the frozen stable
randomized left-Ritz construction: QR after each forward factor, one common
rescaling in the adjoint pass, and the top eigenvectors of `Z^T Z`. Random-rank
and terminal-local controls use the same count of dense products and QR calls,
with identity factors replacing excluded transport factors.

The 100-network weights-only pass used only `mlp_id`, `mlp_name`, `mlp_seed`,
and `weights`. Five whole-network folds fitted clean/retained scalar and
gap-qualified leading/rest shrink from the independent `F/P/C` cross-products.
The analyzer charged each arm's exact Windows-native FlopScope cost and used
50,000 network-block bootstrap draws. Hidden `final_means` were never loaded.

The best arm cost `221,015,444,377` FLOPs, multiplier
`.10050618783543541`; rank-8 and rank-32 full routes cost
`220,495,058,527` and `222,081,095,791` FLOPs. Every supported route remained
under `2^41`, finite, deterministic, and shape-correct.

## Qualification and implementation-risk audit

Windows-native Python 3.10.20, NumPy 2.2.6, FlopScope 0.12.0, and WhestBench
0.16.0 passed the full L0 seal. The nonsymmetric fixture selected the left
space (`.000258` projector distance) rather than the right (`.999996`). Common
layer rescaling changed the projector by only `.000340`; the deliberately
forbidden columnwise scaling changed it by `.892248`. The rank-deficient test
reported effective rank four, and the independent/shared source diagnostic
was `-.002460/1.001193`.

The imported parent `F/P/C/alpha` states and both zero-correction retained
parents were byte-identical. All 100 rows were finite; maximum projector
orthonormality error was `8.64e-8`, and every `(rank+4)` container retained
its declared effective rank. A fresh Python compilation and the read-only
`verify_t114.py` artifact audit passed.

One diagnostic remains scientifically important: alternate frozen probes
produced median full-chain projector distances of `.998313`, `.999587`, and
`.999574` at ranks 8, 16, and 32. This is not an implementation failure—the
synthetic orientation/invariance tests pass and the main probe is exactly
reproducible—but it says the finite-probe Ritz subspace is poorly identified.
It weakens a broad scientific rejection of full-chain response structure.

## Controls and strength of rejection

The best full-chain arm beat both matched controls in expected adjusted score:

| Arm | Expected adjusted score |
|---|---:|
| full rank-16 retained gap | `2.575645581229e-7` |
| random rank-8 retained scalar | `2.608664636183e-7` |
| local rank-8 retained scalar | `2.608811232194e-7` |

Full-chain was lower by `3.302e-9` versus random and `3.317e-9` versus local.
That supports the declared response mechanism direction. It does not create a
submission path because even the favorable full-chain forecast is still well
above ALG019.

The correct disposition is therefore:

- **strong competition rejection of this exact partial-observation spelling**:
  the point estimate itself loses and bootstrap `P(win)=0`, so no relaxed
  scientific-confidence threshold would open it;
- **positive but too-small mechanism evidence**: full-chain beats both matched
  controls and 59 networks have positive signal;
- **weak-to-moderate broader scientific negative evidence**: probe instability
  and the surviving control separation prevent treating this as proof that
  full-chain low-rank response structure is absent;
- not infrastructure-limited, not strict-gate-only, and no owner action needed.

The exact unchanged H113-L spelling is closed. A future descendant would need
a materially different/stabler subspace estimator, truth observation, or
score-paying base rather than another seed/rank retry on opened evidence.

## Prior surprise

The prospectively frozen probability that LPITF would have a
competition-opening target-free proxy was `.62`. It did not, an event with
prior probability `.38` and `-log2(.38)=1.396` bits: **moderately surprising
negative evidence**. Separately, the full-chain signal did beat random/local
controls, the `.65`-prior event (`.621` bits), so the failure is more about
effect size and the incumbent hurdle than a total absence of directional
signal. The `.48` direct-incumbent-win event was never observed because no
arm opened the protected comparison; no direct-score surprise is assigned.

## Next work

T115 is now actionable and rebases to unchanged `ALG019-V000`. It tests the
second and final FC010 decision: replicate-held audit-carrier selection with
DALT primary and NASES/NAAR fallbacks. T114's adverse capacity result should
lower confidence in the shared full-chain DALT subspace, but it does not close
T115 because DALT uses a different dual-audit truth observation and the
fallbacks are mechanism-distinct.

## Timing and work allocation

- Start: `2026-08-31T14:18:12,181968142-07:00`
- Pre-task estimate: **about 4 hours active wall-clock** (planning range
  `2.5--5 hours`)
- End/checkoff: `2026-08-31T15:20:56,246188762-07:00`
- Actual wall time: `01:02:44.064220620` (`3764064220620` ns)
- Estimate difference: completed `02:57:15.935779380` earlier than the
  four-hour point estimate.

Approximate allocation was 16 minutes of theory/specification/provenance
review, 34 minutes of implementation, operational repair, analysis, and
durable documentation, and 13 minutes of program execution/waiting. The last
category includes the fresh Windows environment, L0 metering, and the
100-network pass (whose recorded row-outer time was `320.152s`). Categories
are rounded and sum to the measured wall time only approximately.
