# T083 — coupled affine-suffix stochastic continuation

## Decision

Reject H081-B before M1 under the frozen continuous oracle, while retaining a
meaningful favorable strict-gate-limited signal. The optimistic pooled
candidate/direct variance-cost ratio was `0.8521661838586021` against the
strict `<0.80` requirement: an absolute miss of `0.0521661838586021`, despite
a `14.7834%` improvement over direct sampling. Eleven of 12 network oracles
favored the mechanism, the median ratio was `0.8554224601792284`, and the
maximum was only `1.0276719747510001`.

Thus this is not a scientific reversal or a near-null result. The strict oracle
gate is the sole completed-stage blocker, but the oracle is deliberately
optimistic and still misses the prospectively required effect. The independent
Bernoulli fold, empirical frequency gate, held-out win/tail gates, M1,
candidate registration, FC004/F0-F3, and P1 are correctly not run. T084's
required rejection-informed novelty recurrence is next.

## Frozen exact estimator

At one-based cut `j`, H081-B computes the exact shared prefix `H_j`, applies
T025's deterministic class-aware affine suffix `A_j(H_j)` as one collapsed
dense map, and occasionally computes the exact nonlinear suffix `Y`. With one
Bernoulli decision shared by the antithetic pair,

```text
Z = A_j(H_j) + I [Y - A_j(H_j)] / p.
```

For every prefix state and every frozen positive `p`,
`E_I[Z | H_j]=Y`. The nearest ablation `p=1` reduces pointwise to direct full
antithetic sampling. The source verified that identity to
`4.440892098500626e-16`, the `p=1` reduction to
`5.551115123125783e-17`, and the collapsed-versus-sequential affine suffix to
`4.884981308350689e-15`. All six construction checks passed, 1,800 frozen
Bernoulli domains were unique, and the accepted run replayed byte-identically.

## Oracle design and result

The fixture used 12 deterministic width64/depth32 networks and 512
fixed-radius spherical antithetic pairs. Candidate cuts were
`{2,4,6,8,10,12,16,20,24,28}`; the prospective implementation grid was
`p in {1/16,...,15/16}`. For paired direct variance `V`, paired affine-suffix
residual second moment `D`, base cost `C0`, and nonlinear suffix cost `Cs`, the
frozen continuous screen minimized

```text
[V + (1-p)D/p] [C0 + p Cs]
```

over `0<p<=1` at each cut, then selected the best cut per network. It charged
the exact prefix, collapsed affine map, and expected nonlinear suffix, but
excluded one-time map construction, production rounding, reserve, and stream
administration. These omissions favor the candidate and therefore cannot
rescue its failure.

| Gate or diagnostic | Frozen requirement | Observation | Status |
|---|---:|---:|---|
| Exact construction and replay | all pass | six checks; byte-identical | PASS |
| Pooled continuous oracle | `<0.80` | `0.8521661838586021` | FAIL-STRICT-GATE |
| Oracle network wins | diagnostic | `11/12` | favorable support |
| Median network oracle ratio | diagnostic | `0.8554224601792284` | favorable support |
| Maximum network oracle ratio | diagnostic | `1.0276719747510001` | no severe oracle tail |
| Held-out candidate/direct | `<0.90` | not run | NOT-RUN |
| Held-out wins | `>=9/12` | not run | NOT-RUN |
| Held-out maximum | `<1.25` | not run | NOT-RUN |
| Exact continuation frequency | exact | not run | NOT-RUN |
| M1 / registration / F0-F3 / P1 | sequential | not run | NOT-RUN |

The best continuous cuts ranged from 4 to 20 and probabilities from about
`0.286` to `0.856`. Individual oracle ratios ranged from `0.713035` to
`1.027672`. This breadth makes the favorable direction credible as a local
mechanism clue, but it is selection/pilot evidence rather than held-out or
complete-candidate evidence.

## Human promotion disposition

- Subject/evidence: H081-B width64 continuous variance-cost oracle; no `ALG`
  candidate was registered.
- Current/highest supported tier: no new empirical tier; retain exact T025
  support plus favorable strict-gate-limited oracle evidence. Next considered
  tier was M1.
- Strongest positive evidence: pooled ratio `0.852166` (14.78% better),
  `11/12` oracle wins, median `0.855422`, maximum `1.027672`.
- Gate status: construction/replay PASS; oracle FAIL-STRICT-GATE; held-out,
  frequency, M1, registration, F0-F3, and P1 NOT-RUN.
- Exact strict miss: `0.8521661838586021` versus `<0.80`, adverse by
  `0.0521661838586021` absolute or `6.5208%` of the threshold.
- Primary blocker: `STRICT_GATE_LIMITED_EFFECT_SIZE`.
- Strict gate sole completed-stage blocker: **Yes.** There is no scientific
  direction contradiction, near-null aggregate, or severe oracle tail.
- Why not promoted: even before omitted production costs, the expected gain is
  smaller than the prospectively frozen M1 effect requirement; no independent
  Bernoulli-fold evidence exists.
- High-impact unlock: the agent should use T084 to compare H081-C with new
  hypotheses informed by this favorable-but-insufficient signal. A future
  continuation successor needs a new fingerprint and a prospective mechanism
  that reduces residual energy or base cost (for example lawful prefix-adaptive
  continuation or a better affine/nonlinear baseline), not a post-outcome
  threshold relaxation. No owner action is required. Any owner-requested gate
  change must be prospective and cannot retroactively award M1 or P1 here.

## Academic and surprise disposition

H081-B remains an `OURS`, `N1-NOVEL-COMBINATION` hypothesis/support result:
randomized continuation is known, while the project-specific same-prefix T025
affine suffix interaction is distinct. Because it did not reach M1 or a
complete registered algorithm, it is not a promoted academic contribution or
submission candidate.

T081 froze probability `.66` for rejection before M1, `.24` for M1 then
rejection, and `.10` for P1. The observed pre-M1 rejection is therefore
**expected** at `-log2(.66) = 0.5994620704162712` bits. The favorable severity
within that category does not change the frozen category probability.

## Operational record

The first Windows-native attempt compiled cleanly but stopped before any JSON,
CSV, or scientific outcome was published because the collapsed-versus-
sequential affine equivalence incorrectly required bit-exact equality. The
attempt is preserved under
`attempts/collapsed_affine_bitexact_failure_001/`. Before opening an outcome,
amendment 001 changed only that validation condition to the established
`2e-10` floating-point identity tolerance and rebound the source hash; the
estimator, streams, grid, cost model, gates, prior, and semantic fingerprint
did not change.

The accepted Windows-native run used MSVC 19.43 and Windows SDK 10.0.22621.0
from `2026-08-22T13:00:23.7436360-07:00` to
`2026-08-22T13:01:05.7419667-07:00`. It completed ordinary frozen validation,
recorded empty stderr, and needed no owner action, reboot, or platform switch.

## Verification

```bash
bash experiments/checkpoint3/t083/verify_evidence.sh
```

## Task timing

- Start: `2026-08-22T12:52:24,716333070-07:00`
- Pre-task estimate: `60 minutes`
- End/check-off: `2026-08-22T13:09:04,173497337-07:00`
- Actual wall-clock difference: `00:16:39.457164267` (`999457164267` ns)
