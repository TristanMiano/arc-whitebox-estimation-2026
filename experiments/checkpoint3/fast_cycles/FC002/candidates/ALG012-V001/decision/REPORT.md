# Fast-funnel decision: ALG012-V001

- Cycle: `FC002`
- Candidate task: `T034`
- Decision: `reject`
- Furthest completed tier: `F2`
- Fast-screen outcome tier: `U0-unclassified`
- Proposed canonical tier (monotone): `U0-unclassified`
- F0 package projection: `pass` (`4d93d1e893f8169bf7d3ffc6db57a062aa733b934fad7ff04b63ea1607142e5d`)
- Synthetic fixture: `false`
- Research application allowed: `true`
- Controller-scheduled rigorous evidence opened: **no**

| Cohort | Networks | Candidate/mechanism | Candidate/incumbent | Max paired ratio |
|---|---:|---:|---:|---:|
| F1 micro | 2 | 0.901654901 | 0.951251097 | 0.987508289 |
| F2 sentinel | 12 | 0.988879987 | 0.996697465 | 1.41709625 |
| F3 half A | 0 | 0 | 0 | 0 |
| F3 half B | 0 | 0 | 0 | 0 |
| F3 pooled | 0 | 0 | 0 | 0 |

The incumbent comparison is mandatory contest context and was not used as a P1 veto. Assessment: `candidate_better_than_incumbent`; paired 90% bootstrap interval: [0.906918563, 1.09441876]; candidate-minus-incumbent compute delta fraction: -0.0205465293. The incumbent is a bounded-float32 native numerical control only; prediction-bit, Whest-runtime, and packaged-submission parity are not claimed.

The screening MDE uses the fixed T014-derived provisional floor (`41646c6d4e954bb090c53e62740c9867f82d197f8fa7e8a7bfa5d7dad951d8f3`); candidate-pair recomputation: `false`. T014 measures only routed_31232 versus routed_16384; this provisional screening floor is not a recomputed target-noise MDE for the declared candidate/control pair and does not establish universal conservatism.

Wall time is reported per route and arm in nanoseconds. Residual time: available=`false`, included=`false`; caveat: residual time is unavailable in the native fast funnel and remains excluded from this screening proxy. The native proxy `native modeled-FLOP screening proxy` uses `modeled_flops <= hard_budget_flops - reserve_flops` with budget 272000000000 and reserve 14736711104. This report makes no official-score claim.

Unexplained-tail evidence count: 1 (required: 0).

Protected-input boundary: the controller rejects protected paths and lanes before it opens or schedules them. The exact source/binary-bound project evaluator is a trusted audited boundary; no syscall sandbox, arbitrary-open/exec prevention, or technical Python-subprocess prevention is claimed.

Evaluator environment: `experiments/checkpoint3/fast_cycles/FC002/candidates/ALG012-V001/environment.json` (`b6dbcec709e484f6b5a410fb73e6502627fc6ad7400964b7dc891882fbb8b1ab`). Cumulative active evaluator time: `resource_accounting/snapshots/attempt-A6QMCg.tsv` (`b6d080bc22aba301d5f0fef07ee49fbcf2746bd1f22b25b37d20964d197573c3`).

The immutable bundle contains separate proposed ALGORITHM_LEDGER and state/experiments.csv events; neither was applied. Canonical proposals: `experiments/checkpoint3/fast_cycles/FC002/candidates/ALG012-V001/algorithm_ledger_event_proposal.json` and `experiments/checkpoint3/fast_cycles/FC002/candidates/ALG012-V001/experiment_event_proposal.json`.

Reason codes:

- `mechanism_direction_contradiction`
