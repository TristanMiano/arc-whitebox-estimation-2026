# Fast-funnel decision: ALG013-V001

- Cycle: `FC003`
- Candidate task: `T082`
- Decision: `reject`
- Furthest completed tier: `F1`
- Fast-screen outcome tier: `U0-unclassified`
- Proposed canonical tier (monotone): `M1-mechanism-signal`
- F0 package projection: `pass` (`2891b861552265a46e3be770e1d50f63894c0d4f59e6ef302418697ac213460c`)
- Synthetic fixture: `false`
- Research application allowed: `true`
- Controller-scheduled rigorous evidence opened: **no**

| Cohort | Networks | Candidate/mechanism | Candidate/incumbent | Max paired ratio |
|---|---:|---:|---:|---:|
| F1 micro | 2 | 1.56920024 | 1.68060391 | 2.34494692 |
| F2 sentinel | 0 | 0 | 0 | 0 |
| F3 half A | 0 | 0 | 0 | 0 |
| F3 half B | 0 | 0 | 0 | 0 |
| F3 pooled | 0 | 0 | 0 | 0 |

The incumbent comparison is mandatory contest context and was not used as a P1 veto. Assessment: `candidate_worse_than_incumbent`; paired 90% bootstrap interval: [1.15025967, 2.47034769]; candidate-minus-incumbent compute delta fraction: -0.00595015232. The incumbent is a bounded-float32 native numerical control only; prediction-bit, Whest-runtime, and packaged-submission parity are not claimed.

The screening MDE uses the fixed T014-derived provisional floor (`41646c6d4e954bb090c53e62740c9867f82d197f8fa7e8a7bfa5d7dad951d8f3`); candidate-pair recomputation: `false`. T014 measures only routed_31232 versus routed_16384; this provisional screening floor is not a recomputed target-noise MDE for the declared candidate/control pair and does not establish universal conservatism.

Wall time is reported per route and arm in nanoseconds. Residual time: available=`false`, included=`false`; caveat: residual time is unavailable in the native fast funnel and remains excluded from this screening proxy. The native proxy `native modeled-FLOP screening proxy` uses `modeled_flops <= hard_budget_flops - reserve_flops` with budget 272000000000 and reserve 11003810475. This report makes no official-score claim.

Unexplained-tail evidence count: 1 (required: 0).

Protected-input boundary: the controller rejects protected paths and lanes before it opens or schedules them. The exact source/binary-bound project evaluator is a trusted audited boundary; no syscall sandbox, arbitrary-open/exec prevention, or technical Python-subprocess prevention is claimed.

Evaluator environment: `experiments/checkpoint3/fast_cycles/FC003/candidates/ALG013-V001/environment.json` (`18458d54b8eedae441504b3f683e2e2b67dcb39caded6e86e52c9e763a0ff4a9`). Cumulative active evaluator time: `resource_accounting/snapshots/attempt-r6bdCv.tsv` (`42c53388ae7be6029a088e585accda2180f50436b0433a624dd4d4a40dae6f7d`).

The immutable bundle contains separate proposed ALGORITHM_LEDGER and state/experiments.csv events; neither was applied. Canonical proposals: `experiments/checkpoint3/fast_cycles/FC003/candidates/ALG013-V001/algorithm_ledger_event_proposal.json` and `experiments/checkpoint3/fast_cycles/FC003/candidates/ALG013-V001/experiment_event_proposal.json`.

Reason codes:

- `f1_unexplained_tail_count_nonzero`
