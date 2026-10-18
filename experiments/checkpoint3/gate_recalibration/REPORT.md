# D002 — leaderboard-informed screening-gate recalibration

## Decision

Qualify prospective screening policy `FFSP003`. The exact disclosed Phase-1
rank-15 method passes the complete new F0--F3 screen and is awarded an
**external calibration P1**. It remains public and does not enter the
project-authored P1 pool.

The policy intentionally makes `P1-promising` a broad development-screen
status rather than a mini confirmatory result. It still requires a complete,
lawful, deterministic, finite, under-budget candidate; M1; paired
mechanism-control evidence; no operational failures; and a pooled 32-network
benefit. It no longer requires every half to beat parity, a bootstrap interval
to exclude parity, the unrelated T014 absolute MDE, or zero ratios above
`1.25`.

## Official score and project scoreability

The official Phase-1 ranking quantity is the mean over MLPs of

`final_layer_mse_m * max(0.1, effective_compute_m / 272e9)`.

`effective_compute` includes metered FLOPs plus residual-time charging. Final
layer MSE is an unadjusted diagnostic. The displayed `vs sampling` number is
approximately the `6.5e-7` Phase-1 sampling-reference score divided by the
adjusted score; it is not a separate scoring term.

Among tested project candidates labeled at least N1, only `H081-A` /
`ALG013-V001` reached a complete challenge-width scoring route. Its local
two-network F1 proxy is `1.3413263408521997e-6`, approximately `0.4846x` the
sampling reference, but it is not an official or cohort-comparable leaderboard
score and lost to its paired mechanism control by `1.5692002441x`.

The other tested N1/N2 mechanisms stopped at width-64 trace-variance,
variance-cost, tractability, or oracle gates. Those metrics cannot be
converted into final-layer MSE without inventing a scale. The complete audit
is in `SCORE_TABLE.md`.

Board context read on 2026-08-22 was:

| Phase-1 position | Adjusted score |
|---:|---:|
| rank 15, selected disclosed control | `9.69e-8` (exact retained receipt: `9.686489982715155e-8`) |
| rank 50 | `1.55e-7` |
| rank 100 | `2.548e-7` |
| sampling approximation | approximately `6.5e-7` |

Sources:

- [Official Phase-1 leaderboard](https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/leaderboards?round=phase-1)
- [Official scoring model](https://github.com/AIcrowd/whest-starterkit/blob/main/docs/concepts/scoring-model.md)
- [Selected rank-15 release](https://github.com/kaileh57/whitebox-phase1-327786/releases/tag/phase1-327786)

Adjusted scores are evaluator-configuration dependent, and local project
cohorts differ from the board. Consequently the table does not pretend that a
two-network local proxy has an official rank.

## Frozen prospective policy

`POLICY_V3.json` was frozen at `2026-08-22T18:54:06.845885232-07:00`, before
any F3B output was opened. Its SHA-256 is
`25e8ce01149dbf064b675b4ed432c548a7fd6d021fee6fa344dadfc42789955b`.

| Stage | Old default | `FFSP003` prospective default | Reason |
|---|---:|---:|---|
| lawful width-64 M1 admission, 12 routes | task-specific effect floors as low as `<0.75` | pooled `<=0.99`, `>=7/12` wins, max `<2`; oracle alone only authorizes lawful test | M1 should establish direction, not demand contest-size effect |
| F2 aggregate reject | `>1.05` | `>1.10` | reject-only sentinel should tolerate sampling noise |
| F2/P1 duplicated tail veto | zero ratios `>=1.25`, plus max `<1.5` | no separate tail-count veto; catastrophic max `<4` | rank-15 positive control proves the conjunction can false-reject |
| each F3 half | `<1.0` | `<=1.05` | tolerate bounded half-cohort noise |
| pooled F3 | `<=0.99` | `<1.0` | still require aggregate benefit |
| bootstrap | 90% upper `<1.0` | 90% upper `<1.10` | rule out meaningful aggregate harm, not demand significance in a screen |
| absolute T014 MDE | P1 veto | report-only | it is not pair-specific and was never a universal MDE |
| integrity/compute/package/operations | strict | unchanged | these are validity requirements, not statistical conservatism |

The policy is calibrated to require the disclosed rank-15 method to pass. Its
thresholds are designed to be compatible with a modest repeatable benefit of
the sort a top-100 candidate might have, but top-100 coverage is not claimed:
we have not yet reproduced an exact disclosed method near rank 100.

Historical decisions are not rewritten. Any old strict-gate-limited mechanism
that is reconsidered must be prospectively reranked and continued under a new
or explicitly amended frozen identity. Direction reversals, infeasibility, and
strong optimistic-oracle losses remain decisive.

## Positive-control completion

F3B used the D001-precommitted 16 networks, materialized rows 76--91. All
three arms used dataset metadata SHA-256
`4d7f4fa8a54957037661ce54516ebf2902dad758ceedefee8caf37187a3a5bb2`;
the Parquet SHA-256 remained
`adce8b6c6ba1dfeb5df2993aaf3d9fb6846eefd474ee1d2070dd5fef185c71ba`.
No route failed.

All adjusted scores below use the same conservative fixed modeled-compute
translation predeclared by D001, not each local run's host-dependent residual
time.

| Evidence | Candidate/control | Wins | Maximum | Candidate/incumbent |
|---|---:|---:|---:|---:|
| F3A retained | `0.36004803` | `15/16` | `1.41090209` | `0.35300190` |
| F3B new | `0.43198056` | `13/16` | `1.34118864` | `0.33312237` |
| pooled F3 | `0.39607700` | `28/32` | `1.41090209` | `0.34185745` |

The pooled one-sided 90% network-bootstrap upper ratio is `0.45282910`, and
the absolute adjusted-score advantage over the mechanism control is
`1.8845146892e-7`. Every `FFSP003` gate passes with wide margins. The old v2
rules still reject the same complete result solely because two of 32 ratios
are at least `1.25`; retaining that counterfactual confirms the recalibration
changed the intended false-negative mode rather than the scientific data.

## Human promotion disposition

- Subject / evidence class: `LB001-V001`, exact public Phase-1 submission
  327786, positive-control calibration on 32 public exploration networks.
- Current / highest / next tier: external `P1-promising` calibration pass;
  excluded from the project pool; a private or rigorous claim is not made.
- Positive evidence: pooled candidate/control `0.396077`, `28/32` wins,
  bootstrap upper `0.452829`, max `1.410902`, candidate/incumbent `0.341857`.
- Gate results: F0, determinism, M1, F2, both F3 halves, pooled benefit,
  bootstrap-harm, max-tail, compute, and operations all `PASS` under FFSP003.
- Primary blocker class: `PROMOTED` for external calibration; no project pool
  membership because provenance is public.
- Why not project-promoted: provenance/role only, not a failed numerical gate.
- Immediate high-impact unlock: agent requalifies the T066 policy adapter
  before the next complete project F0--F3 run; T090 reranks historical
  strict-gate-limited evidence and new hypotheses under FFSP003. A second
  disclosed near-rank-100 control is needed before claiming top-100 coverage.

## Runner boundary

T066 remains qualified for the immutable v2 contract, not for `FFSP003`.
T090 is a novelty/design task and may proceed, but before another complete
project candidate opens F0--F3 evidence the decision adapter and positive,
reject, stop, resume, and mutation fixtures must be requalified against the
new policy. This is an agent-side prerequisite, not an owner action.

## Task timing

- Start: `2026-08-22T18:50:13,429174165-07:00`
- Pre-task estimate: `45 minutes`
- End/check-off: `2026-08-22T19:11:13,908392717-07:00`
- Actual wall-clock difference: `00:21:00.479218552`
  (`1260479218552` ns)
