# T101 — rigorous Cycle 2 adjudication and route

## Decision

`ALG017-V000` earns neither `R1-mechanism-confirmed` nor `P2-competitive` in
rigorous Cycle 2. RC002 is frozen as a completed negative slate. Its three
blocks are immutable historical evidence, and no unchanged ALG017 realization
may receive more expensive evaluation.

The decision has two distinct parts:

- **R1 is not awarded solely because of the frozen every-block rule.** The
  candidate/carrier pooled ratio is `0.962267`, familywise upper is `0.985252`,
  benefit exceeds MDE by `1.70991e-8`, 52/72 routes win, p95 is `1.156528`,
  and maximum is `1.217949`. B1 and B2 pass at `0.961582` and `0.917224`, but
  B3 is `1.003198`, adverse by `0.003198`. All other frozen R1 gates pass.
  This is `STRICT_GATE_LIMITED_BLOCK_HETEROGENEITY`, not a scientific
  reversal of the pooled mechanism evidence.
- **P2 is scientifically rejected.** Candidate/incumbent is adverse in B1
  and B3 (`1.418156` and `1.421474`), pooled at `1.136546`, and has upper
  `1.406062`, negative mean benefit, p95 `4.019953`, and maximum `5.270800`.
  These are broad competitiveness failures independent of the R1 prerequisite.

The historically valid P1 tier is preserved. It means ALG017 passed its fast
mechanism funnel; it does not imply native incumbent competitiveness or
submission priority.

## R1 gate audit

| Frozen requirement | Observation | Margin | Status |
|---|---:|---:|---|
| each block candidate/carrier `<1` | `0.961582 / 0.917224 / 1.003198` | B1 `+0.038418`; B2 `+0.082776`; B3 `-0.003198` | **FAIL-STRICT-GATE** |
| pooled ratio `<1` | `0.962267` | favorable by `0.037733` | PASS |
| 98.75% upper ratio `<1` | `0.985252` | favorable by `0.014748` | PASS |
| mean benefit `>1.49674e-9` MDE | `1.85958e-8` | favorable by `1.70991e-8` | PASS |
| p95 `<2.5` | `1.156528` | favorable by `1.343472` | PASS |
| maximum `<4` | `1.217949` | favorable by `2.782051` | PASS |
| identity, invariants, budget, mechanism ablation, T064, replay, operations | all complete | no defect | PASS |

Removing or relaxing only the every-block rule would award R1. It cannot be
changed after outcome access. The miss is small enough that the result remains
positive academic mechanism evidence, and the exact threshold effect is
explicit for the owner.

The pooled mechanism win was expected from T103. The single B3 reversal is
mildly surprising because the larger prospective run retained the direction
overall but exposed a small block dependence. T099 froze no numeric R1 prior,
so no post-hoc surprise bits are assigned.

## P2 gate audit

| Frozen requirement | Observation | Margin | Status |
|---|---:|---:|---|
| R1 prerequisite | not awarded | sequential | FAIL |
| each block candidate/incumbent `<=1.05` | `1.418156 / 0.753330 / 1.421474` | B1 `-0.368156`; B2 `+0.296670`; B3 `-0.371474` | **FAIL-SCIENTIFIC** |
| pooled ratio `<1` | `1.136546` | adverse by `0.136546` | **FAIL-SCIENTIFIC** |
| 98.75% upper ratio `<1` | `1.406062` | adverse by `0.406062` | **FAIL-SCIENTIFIC** |
| mean benefit `>2.62396e-8` MDE | `-5.69748e-8` | adverse by `8.32144e-8` | **FAIL-SCIENTIFIC** |
| p95 `<2.5` | `4.019953` | adverse by `1.519953` | **FAIL-SCIENTIFIC** |
| maximum `<4` | `5.270800` | adverse by `1.270800` | **FAIL-SCIENTIFIC** |
| reserve `>=11B` | `248.159B` | favorable by `237.159B` | PASS |

This reversal is moderately surprising relative to T103's context-only
candidate/incumbent ratio `0.726672`, but that earlier comparison was neither
prospective rigorous evidence nor a frozen P2 prior. The new result is much
larger, stricter evidence and updates the competitive belief downward.

## Submission and route

T101 does not change the submission candidate. This historical lane is not
directly comparable to Phase 2, and faithful Phase-2 `ALG017-V002` had already
lost to then-incumbent `ALG015-V000` at adjusted ratio `1.505849`.
`ALG018-V000` remains the local and officially graded best.

The prior pipeline would now return to a novelty recurrence. The owner has
requested a leverage correction first: T106 will make fixed-duration deep
theoretical hypothesis generation the dominant recurring activity and will
forbid expensive rigorous work on an already noncompetitive family unless a
specific academic deliverable justifies it. T107 will be the first new FC007
hypothesis-generation task. No owner action is required.

## Verification

```bash
bash experiments/checkpoint3/t101/verify_evidence.sh
```

## Task timing

- Start: `2026-08-27T16:01:34,238893594-07:00`
- Pre-task estimate: `25 minutes` (plausible range `15–40 minutes`)
- End/check-off: `2026-08-27T16:06:26,068351108-07:00`
- Actual wall-clock difference: `00:04:51.829457514`
