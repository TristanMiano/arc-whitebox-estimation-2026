# T069 — rigorous Cycle 1 adjudication and route

## Decision

`ALG014-V000` earns neither `R1-mechanism-confirmed` nor `P2-competitive` in
rigorous Cycle 1. RC001 is frozen as a completed negative rigorous slate and
its three blocks become immutable historical evidence. The project returns to
Checkpoint 3B; T095 is the next task and opens the rejection-informed FC005
hypothesis cycle.

This decision has two importantly different parts:

- **R1 is strict-tail-limited despite strong positive mean mechanism
  evidence.** Candidate/iid is favorable on every block, `0.533290` pooled,
  has upper bound `0.707180`, and exceeds pair-specific MDE by
  `3.27851e-7`. Only the conjunctive p95 and maximum rules fail. The p95 miss
  is narrow (`2.521804` versus `<2.5`, adverse by `0.021804`); the maximum
  miss is large (`7.510423` versus `<4`, adverse by `3.510423`). Removing both
  tail gates would award R1, but they were prospectively frozen and cannot be
  waived after output. The mean effect is real evidence worth using; the tail
  is also a real scientific risk rather than administrative noise.
- **P2 is scientifically noncompetitive, not merely tail-gate-limited.** It
  already fails because R1 is absent, and independently fails B1, the pooled
  upper bound, target-noise MDE, p95, and maximum. Its pooled point ratio
  `0.993461` is an adjusted-score tie, not evidence of stable superiority.

No downstream Checkpoint 4--6 scientific candidate path opens. The separate
T074/T075 deadline-safe `ALG003-V008` fallback lane remains active and is not
blocked by this research return.

## R1 gate audit

| Frozen requirement | Observation | Margin | Status |
|---|---:|---:|---|
| each block candidate/mechanism `<1` | `0.625390 / 0.514844 / 0.454117` | favorable by `0.374610 / 0.485156 / 0.545883` | PASS |
| pooled ratio `<1` | `0.533290` | favorable by `0.466710` | PASS |
| 97.5% upper ratio `<1` | `0.707180` | favorable by `0.292820` | PASS |
| mean benefit `>6.27594e-8` MDE | `3.90611e-7` | favorable by `3.27851e-7` | PASS |
| p95 `<2.5` | `2.521804` | adverse by `0.021804` | **FAIL-STRICT-GATE** |
| maximum `<4` | `7.510423` | adverse by `3.510423` | **FAIL-STRICT-GATE** |
| identity, route parity, exact control, reserve, finite output, T064, replay, operations | all complete | no defect | PASS |

The maximum route is global 27 (`rc001-b2-003`). It is not explained away by
target noise: all eight reference banks were retained, the pair MDE was sealed
before scoring, and the full payload reproduced across the frozen replay
program. The mechanism result is therefore classified
`STRICT_GATE_LIMITED_TAIL_INSTABILITY`, with strict gates the sole formal R1
blocker.

The outcome is moderately surprising relative to the qualitative pre-result
belief. E0004 made the mean improvement expected and its maximum was
`2.312252`, already motivating the prospectively relaxed rigorous limit of
`4`. A new maximum of `7.510423` and p95 just outside `2.5` are worse than
that evidence suggested. T067 did not freeze a numeric R1 outcome prior, so no
post-hoc surprise-bit value is invented.

## P2 gate audit

| Frozen requirement | Observation | Margin | Status |
|---|---:|---:|---|
| R1 prerequisite | not awarded | sequential | FAIL |
| each block candidate/incumbent `<=1.05` | `1.495094 / 0.812056 / 0.874450` | B1 adverse by `0.445094` | **FAIL-SCIENTIFIC** |
| pooled ratio `<1` | `0.993461` | favorable by `0.006539` | PASS |
| 97.5% upper ratio `<1` | `1.360065` | adverse by `0.360065` | **FAIL-SCIENTIFIC** |
| mean benefit `>7.05578e-8` MDE | `2.93770e-9` | short by `6.76201e-8` | **FAIL-SCIENTIFIC** |
| p95 `<2.5` | `3.834159` | adverse by `1.334159` | **FAIL-SCIENTIFIC** |
| maximum `<4` | `9.998310` | adverse by `5.998310` | **FAIL-SCIENTIFIC** |
| reserve `>=11B` | `24.649052B` | favorable by `13.649052B` | PASS |

This result is not surprising. Fast evidence established a plausible
development candidate, not stable incumbent superiority. On the fresh blocks,
mean raw final-layer MSE is actually worse than the incumbent
(`4.90814e-7` versus `4.65445e-7`); lower modeled work brings the adjusted
pooled point estimate close to parity, but not above the uncertainty or noise
floor.

## Status of `ALG014-V000`

The algorithm keeps its historically valid `P1-promising` tier and remains
the current best-so-far project submission candidate because no directly
comparable project algorithm has beaten it. It does **not** keep eligibility
to re-enter another rigorous cycle unchanged. P1 means the fast screen passed;
RC001 now records that the exact candidate failed fresh rigorous promotion.
A descendant must have a new identity and traverse F0--F3 before entering a
future rigorous slate.

The academic label also remains N1/dimension 2. Strong arithmetic evidence for
collective Haar-Stiefel balance is preserved, but RC001's tail failure prevents
presenting this exact estimator as a rigorously confirmed contribution.

## Return route

T095 must run the mandatory post-no-P2 novelty recurrence before another
protected candidate opens. It must use RC001's two distinct signatures:

1. a large and block-consistent collective-balance mean benefit with rare
   severe losses; and
2. insufficient, heterogeneous incumbent competitiveness.

It will rerank parked H093-A/H093-B rather than inherit them, generate at
least two new mechanism-distinct alternatives, seek at least one novelty
dimension 3 or stronger candidate if defensible, and freeze numerical outcome
priors. It must explicitly compare tail-safe frame coupling, lawful
candidate/incumbent mixing or routing, and at least one family not derived
from Haar-Stiefel refinement. T096 and T097 execute the first two frozen
decisions to terminal P1/rejection. T098 is the mandatory FC005 checkpoint
and appends more candidate decisions if the rigorous-entry rule is not met.
Conditional T099--T101 freeze, run, and adjudicate RC002 only after a newly
eligible pool exists; RC002 must use new blocks and one-sided familywise alpha
`0.0125`.

No owner action is required and changing RC001's gates now would not be a
lawful unlock. The immediate high-impact action is agent-side hypothesis work
in T095. Independent reproduction on a stable VM remains desirable later but
is not a reason to stop research.

## Verification

```bash
bash experiments/checkpoint3/t069/verify_evidence.sh
```

## Task timing

- Start: `2026-08-25T19:53:52,505319010-07:00`
- Pre-task estimate: `30 minutes` (plausible range `20–50 minutes`)
- End/check-off: `2026-08-25T20:07:38,932917296-07:00`
- Actual wall-clock difference: `00:13:46.433218234`
