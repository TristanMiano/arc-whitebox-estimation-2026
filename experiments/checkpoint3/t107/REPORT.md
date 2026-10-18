# T107 — two-hour FC007 competitive theory recurrence

## Outcome

T107 completed the owner-overridden minimum of **120 active minutes of written
theory**. It opened no protected candidate outcome, created no algorithm ID,
changed no scientific tier, and changed no submission incumbent.
`ALG018-V000` remains the local and officially graded best at adjusted
`2.6931472416436013e-7` (submission `328686`).

The cycle selected two immutable hypotheses for T108:

1. **H107-O** — harmonic-shrunk terminal-skew Edgeworth closure, three-band
   alpha fusion, robust partial-arm extension/retune. It is the lower expected-
   score decision, provisionally V000 in the next available algorithm family.
2. **H107-I** — the same robust carriers with a simpler two-band final-alpha
   fusion and no sampled terminal moment. It is the model-risk/transfer hedge,
   provisionally V001.

H107-N, H107-J, and H107-F are exact nested report-only algorithms from the
same components. They do not authorize more target openings, but every valid
frozen variant is eligible for succession if it has the lowest adjusted score.

## Selected score hypotheses

| Rule | N1 novelty | Conservative central adjusted forecast at `.1` floor | Subjective fresh incumbent-win probability | T108 role |
|---|---:|---:|---:|---|
| H107-O | dimension 3 | `2.45e-7` (`~.910x`) | `.95` conditional on valid bytes | selected lower-score V000 |
| H107-N | dimension 2 | `2.49e-7` (`~.925x`) | `.93` | O ablation |
| H107-I | dimension 3 | `2.55e-7` (`~.945x`) | `.88` | selected simpler V001 |
| H107-J | dimension 4 | `2.54e-7` (`~.944x`) | `.86` | N ablation |
| H107-F | dimension 2 | `2.655e-7` (`~.986x`) | `.72` | shared control |

Forecasts are explicitly selection-shrunk and conditional on the `.1`
multiplier. T108 must recompute the pre-outcome adjusted forecast if measured
effective compute crosses that scoring boundary.

## Main theoretical results

- For a symmetric cubic tensor, the exact spherical decomposition is
  `T[w,w,w] = 3 t·w/(d+2) + H3(w)`. This motivates preserving the skew component
  aligned with final alpha and shrinking only the degree-three residual.
- The first terminal Edgeworth action is derived with sign and units:
  `delta=-sigma*kappa3*alpha*phi(alpha)/6`.
- Pair-preserving half disagreement yields a reliability proxy for the sampled
  harmonic residual. The main-frame halves are exchangeable but not independent
  because they share one Stiefel QR; this is an explicit limitation, not a
  hidden theorem assumption.
- The quartic trace hierarchy and fourth-order ReLU actions were derived, but
  width scaling makes H107-Q likely a basis-point reserve rather than T108's
  next high-leverage decision.
- Positive homogeneity proves that mean-chi radial replacement is already exact;
  extra radial quadrature is closed theoretically without a run.
- A new high-leverage FC008 reserve, **H107-U**, uses the independent partial arm
  as a noisy self-supervised closure-bias label and the main frame as an
  independent risk witness. Its held-source risk difference is unbiased for
  closure-bias-power change under the ideal independent-stream model. U0/U1,
  their exact low-rank operator form, four-column analytic basis, invariants,
  and incumbent-dependent 13–17% post-O hurdle are recorded.
- Other nonredundant reserves are H107-K (exact spherical affine-ReLU control),
  H107-R (hierarchical replicate fusion), and H107-S (low-rank Stein control).

The full derivations, counterexamples, numerical threat model, probability
heuristic, selection-debt audit, surprise table, and reserve calculus are in
`THEORY_LEDGER.md`. Dated prior-art/contest sources are in `SOURCES.md`.

## Already-open hypothesis-generation evidence

No row below is fresh candidate evidence or scientific promotion evidence.
Across four already-open 12-network cohorts, H107-O scored `.979696` of H107-N
and `.894316` of the incumbent pooled, beating N on `48/48` and the incumbent
on `46/48`. H107-N scored `.967468` of J and `.912850` of the incumbent;
H107-I scored `.944936` of incumbent; J scored `.943539`. These unusually
large, stable effects raised the T108 priors but also create selection debt,
which is why rows 76–87 remain sealed for one immutable comparison.

H107-P's deterministic width-law trace-only ablation lost its single declared
displacement check to O at `1.005327`, `0/12`; it closed without replay/tuning.
H107-L and H107-M were adverse after fusion and closed. The transient native
segmentation fault during one O replay completed on the identical first retry,
with later runs normal. It is recorded as intermittent infrastructure, not
algorithm evidence, and did not require owner action.

## T108 frozen experiment

T108 uses Phase-2 mini rows **76–87** from dataset revision
`ce926b7d1ced65faa668c01b94a43f8c4f43783d`. Before target access it must:

- resolve the next algorithm family and register/hash V000 O, V001 I, V002 N,
  V003 J, and V004 F;
- prove incumbent Q0-prefix parity for a provisional 288+44 nested partial
  extension and all frame/closure/layer invariants;
- validate stable float64 final-moment reductions against an independent
  reference and exercise O's permutation, scale, half-swap, endpoint, and
  fallback fixtures;
- measure whole-package FLOPs, residual time, effective compute, multiplier,
  hard limits, determinism, shape, and finite output twice; and
- seal predictions/hashes before reading `final_means`.

The `.1` boundary is a score floor, **not** the hard `2^41` budget. T108 should
prefer the largest even partial-row count whose frozen risk/cost law predicts
the best adjusted score, normally preserving at least 50M effective-compute
units below the floor. A lawful design above the floor remains valid and is
charged its actual multiplier. Only hard rule/contract, finite, parity,
determinism, or true-budget failures make bytes invalid.

On the single protected cohort, compute raw MSE, FLOPs/effective compute,
multiplier, adjusted score, paired wins, and diagnostics for all five frozen
variants. A pooled adjusted ratio below one beats the incumbent and must be
reported in **bold**. The lowest adjusted valid winner becomes the local
submission candidate, even when its role was called an ablation/control. A
ratio at least one closes that unchanged score branch. No historical F0–F3 or
rigorous campaign is triggered merely by a T108 win; package/official upload
still requires the existing hard gate and fresh explicit owner authorization.

## Timing

- Start: `2026-08-27T16:26:36,718665126-07:00`
- Pre-task estimate: `2 hours 20 minutes`
- Active written theory/review: **at least 2 hours**
- Probe implementation/runtime/web/admin before theory completion:
  approximately **52 minutes**
- Documentation/state/verification closeout after the theory floor:
  approximately **12.77 minutes**
- End/checkoff: `2026-08-27T19:34:35,085986528-07:00`
- Actual start-to-checkoff wall time: `03:07:58.367321402`
  (`11278367321402` ns)

## Verification

```bash
bash experiments/checkpoint3/t107/verify_evidence.sh
```
