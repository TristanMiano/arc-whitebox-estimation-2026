# Fast-funnel decision: ALG011-V001

- Cycle: `FC001`
- Candidate task: `T070`
- Decision: `reject`
- Furthest completed tier: `F2`
- Fast-screen outcome tier: `U0-unclassified`
- Proposed canonical tier (monotone): `M1-mechanism-signal`
- F0 package projection: `pass` (`76c16daba592f1615d401b4c9a482f4dfa2dcd9857f28e933550956013118ceb`)
- Synthetic fixture: `false`
- Research application allowed: `true`
- Controller-scheduled rigorous evidence opened: **no**

| Cohort | Networks | Candidate/mechanism | Candidate/incumbent | Max paired ratio |
|---|---:|---:|---:|---:|
| F1 micro | 2 | 0.714611997 | 0.769131972 | 0.930031599 |
| F2 sentinel | 12 | 1.0701375 | 1.05829231 | 1.53842516 |
| F3 half A | 0 | 0 | 0 | 0 |
| F3 half B | 0 | 0 | 0 | 0 |
| F3 pooled | 0 | 0 | 0 | 0 |

The incumbent comparison is mandatory contest context and was not used as a P1 veto. Assessment: `candidate_worse_than_incumbent`; paired 90% bootstrap interval: [0.844780331, 1.30859044]; candidate-minus-incumbent compute delta fraction: -0.0238004112. The incumbent is a bounded-float32 native numerical control only; prediction-bit, Whest-runtime, and packaged-submission parity are not claimed.

The screening MDE uses the fixed T014-derived provisional floor (`41646c6d4e954bb090c53e62740c9867f82d197f8fa7e8a7bfa5d7dad951d8f3`); candidate-pair recomputation: `false`. T014 measures only routed_31232 versus routed_16384; this provisional screening floor is not a recomputed target-noise MDE for the declared candidate/control pair and does not establish universal conservatism.

Wall time is reported per route and arm in nanoseconds. Residual time: available=`false`, included=`false`; caveat: residual time is unavailable in the native fast funnel and remains excluded from this screening proxy. The native proxy `native modeled-FLOP screening proxy` uses `modeled_flops <= hard_budget_flops - reserve_flops` with budget 272000000000 and reserve 15554355200. This report makes no official-score claim.

Unexplained-tail evidence count: 3 (required: 0).

Protected-input boundary: the controller rejects protected paths and lanes before it opens or schedules them. The exact source/binary-bound project evaluator is a trusted audited boundary; no syscall sandbox, arbitrary-open/exec prevention, or technical Python-subprocess prevention is claimed.

Evaluator environment: `experiments/checkpoint3/fast_cycles/FC001/candidates/ALG011-V001/recovery_attempts/IR003/environment.json` (`7eb3aac9b7e05177e6c321d608c24a6a546cab9dc54e4cd02369c345e77b327a`). Cumulative active evaluator time: `resource_accounting/snapshots/attempt-E6cslN.tsv` (`4fe4c4b3ded419ac5d1a191c5b4a8f0ddcbc3fb207992a8b603c4bfb54581a0c`).

The immutable bundle contains separate proposed ALGORITHM_LEDGER and state/experiments.csv events; neither was applied. Canonical proposals: `experiments/checkpoint3/fast_cycles/FC001/candidates/ALG011-V001/recovery_attempts/IR003/algorithm_ledger_event_proposal.json` and `experiments/checkpoint3/fast_cycles/FC001/candidates/ALG011-V001/recovery_attempts/IR003/experiment_event_proposal.json`.

Reason codes:

- `mechanism_direction_contradiction`
