# T085 — Haar-MUB coherent affine-residual Hansen–Hurwitz adjudication

## Decision

Reject unchanged `H084-A` before M1 and move to `H081-C`/T086. The frozen
optimistic target-aware oracle produced a pooled candidate/full-Haar-MUB
variance-cost ratio of `0.905089151661011` against the strict `<0.75`
requirement. That misses by `0.155089151661011` absolute, or `20.6786%` of the
threshold. Because this oracle knows the true coherent basis residual norms
and omits several candidate overheads, the later lawful affine-proxy stage
cannot establish the prospectively claimed route after this failure.

There is weaker positive evidence worth retaining: the idealized allocation
improved pooled variance-cost by `9.4911%`, favored the candidate on `10/12`
networks, and had no severe network tail (range `0.618927–1.092443`, median
approximately `0.914131`). This is therefore not a direction reversal. It is
a scientific rejection of H084-A's claimed *effect magnitude* and a strict
sequential-gate stop, not evidence that coherent basis allocation has exactly
zero value.

The independent 32-rotation lawful-proxy fold, uniform ablation, M1,
registration, FC004/F0–F3, and P1 were correctly not run. No `ALG` identity or
empirical tier was created. The provisional novelty-dimension-3 assessment is
an idea/provenance judgment and remains separate from the negative promotion
result.

## Exact construction and checks

The native fixture constructed the complete width-64 real MUB from the
standard basis and 32 Kerdock/Walsh bases in the frozen
`GF(2^5) + GF(2)` model. All 496 pairwise alternating-matrix differences had
binary rank six. Within-basis and cross-basis errors were exactly zero in the
dyadic representation, certifying 33 orthonormal mutually unbiased bases and
4,224 antipodal endpoints per Haar replication.

For one Haar rotation `Q`, one-based cut `j`, exact basis mean `Y_b`, and
collapsed T025 affine mean `A_b`, the tested correction was

```text
Abar + (1/m) sum_s (Y_b_s-A_b_s)/(33*q_b_s).
```

The oracle used the frozen `1/4` uniform probability mixture and true
`||Y_b-A_b||` scores. Fixed-count categorical sampling used equal inverse-CDF
strata; the executable integrated each stratum exactly to obtain conditional
trace variance. Maximum conditional recovery error was
`3.33066907387547e-16`.

The Haar generator's maximum orthogonality error was
`1.33226762955019e-15`; rotated-norm error was `1.11022302462516e-15`;
complete-carrier angular mean error was zero and second-moment error was
`9.02056207507940e-17`. Radial positive-homogeneity error was
`3.99680288865056e-15`. Raw normal mean/variance across the pilot matrices were
`-0.000762506` and `1.00036012`. The accepted result and replay are
byte-identical.

## Frozen oracle result

The fixture used 12 deterministic width64/depth32 networks and 32 independent
pilot Haar rotations per network. It selected separately per network among
cuts `{4,8,12,16,20,24}` and draw counts `{4,6,8,12,16,20,24,28}`. The most
common choice was cut 4 (`7/12` networks) and 12 draws (`5/12`).

| Gate or diagnostic | Frozen requirement | Observation | Status |
|---|---:|---:|---|
| Kerdock/MUB, Haar, target identities, replay | all pass | all pass; byte-identical | PASS |
| Optimistic target-aware pooled oracle | `<0.75` | `0.905089151661011` | FAIL-SCIENTIFIC (effect magnitude) |
| Oracle network wins | diagnostic | `10/12` | favorable support |
| Oracle median / maximum | diagnostic | `~0.914131 / 1.092443` | modest gain; no severe tail |
| Lawful held-out/full Haar-MUB | `<0.90` | not run | NOT-RUN |
| Held-out wins / maximum | `>=9/12 / <1.25` | not run | NOT-RUN |
| Adaptive/uniform allocation | `<0.95` | not run | NOT-RUN |
| M1 / registration / F0–F3 / P1 | sequential | not run | NOT-RUN |

The candidate cost charged all 4,224 prefixes and collapsed affine suffixes,
plus `m` exact nonlinear basis suffixes. The optimistic screen excluded suffix
construction, Haar generation and rotation, categorical administration,
output accumulation, reserve, and production rounding. Those omissions favor
the candidate and cannot rescue the failed effect-size prediction.

## Human promotion disposition

- Subject / evidence class: H084-A width64 target-aware Haar-MUB basis-residual
  variance-cost oracle; no `ALG` candidate registered.
- Current tier / highest supported / next considered: no new empirical tier;
  retain exact-construction and modest oracle support only; M1 was the next
  tier considered.
- Positive evidence: pooled `0.905089` (9.49% favorable), `10/12` network
  wins, median `~0.914131`, maximum `1.092443`, with exact identities and
  replay.
- Gate results: construction/replay PASS; frozen `<0.75` oracle
  FAIL-SCIENTIFIC on claimed magnitude; lawful held-out, uniform ablation,
  M1, registration, F0–F3, and P1 NOT-RUN.
- Exact failed-gate margin: observed `0.905089151661011` versus `<0.75`,
  adverse by `0.155089151661011` absolute (`20.6786%` of threshold).
- Primary blocker class: `SCIENTIFIC_NEGATIVE_EFFECT_MAGNITUDE` and
  `STRICT_GATE_LIMITED`; the aggregate direction itself remained favorable.
- Why not promoted (strict gate partial): the strict sequential gate is the
  immediate procedural stop, but it encodes H084-A's explicit falsifiable
  magnitude claim, and even an overhead-omitting target-aware oracle delivered
  only a modest gain. This is more than a merely bureaucratic miss.
- Immediate high-impact unlock: none for unchanged H084-A; a materially new
  fingerprint must reduce all-basis prefix cost or coherent residual noise.
  The agent proceeds now to the already frozen mechanism-distinct H081-C/T086.
  No owner action or retroactive gate change is recommended.

## Academic novelty and surprise

H084-A remains a project `OURS+PUBLIC` hypothesis with provisional
`N2-NOVEL-MECHANISM`, novelty dimension 3, because novelty is not erased by a
negative efficacy result. It is not a promoted academic contribution or
submission route. A future reuse must cite this negative and materially alter
the cost/residual mechanism; changing only the gate, probability floor, cut,
or draw grid is not a new candidate.

T084 froze probability `.58` for rejection before M1. The observed category
is therefore **expected** at `-log2(.58) = 0.785875194647153` bits. The modest
positive direction does not alter that predeclared category.

## Operational record

Five pre-outcome Windows-native attempts were preserved. Attempts 1–2 exposed
translation-unit composition and `/W4 /WX` conversion defects; attempts 3–4
exposed a stale-vector antipode diagnostic and then a launcher that reused the
old executable; attempt 5 showed `cmd.exe` defaulting a UNC working directory
to `C:\Windows`. Amendments 001–005 changed only source composition,
warning-cleanliness, diagnostics, and launcher process/working-directory
handling. No estimator choice, seed, cost, gate, prior, or fingerprint changed,
and no scientific JSON/CSV existed before the accepted run.

The accepted Windows-native MSVC run began
`2026-08-22T13:55:33.1521361-07:00` and ended
`2026-08-22T13:57:22.6190636-07:00`, including byte-identical verification and
replay. No reboot, platform switch, or owner action was needed.

## Verification

```bash
bash experiments/checkpoint3/t085/verify_evidence.sh
```

## Task timing

- Start: `2026-08-22T13:35:26,398673681-07:00`
- Pre-task estimate: `60 minutes`
- End/check-off: `2026-08-22T14:02:16,870773271-07:00`
- Actual wall-clock difference: `00:26:50.472099590`
  (`1610472099590` ns)
