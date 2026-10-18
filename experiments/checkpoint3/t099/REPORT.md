# T099 report — rigorous Cycle 2 frozen prospectively

## Result

T099 is complete. RC002 is frozen before any RC002 candidate, control,
incumbent, reference, score, ratio, win, bootstrap, or formal gate outcome was
opened. The singleton slate is historical-P1 `ALG017-V000`, with exact shared-
frame carrier `ALG017-V001` as mechanism control and `ALG003-V008` as native
contest comparator.

The standalone C++20 implementation reproduces the frozen T103 candidate and
control semantics without loading CPython. On both already-open T103 F1 routes,
candidate/control maximum absolute differences were at most `1.90735e-6`,
prediction-scale normalized maximum differences at most `3.65579e-7`,
normalized RMSE at most `2.09530e-7`, and correlation at least
`0.9999999999999659`; all prospectively required translation tolerances pass.
Its internal deterministic replay is byte-exact. Maximum Haar orthogonality
and leverage-sum errors were `4.38203e-7` and `7.61780e-6` in the bound smoke.

Three new 24-network manifests contain 72 unique network seeds and 72 unique
reference seeds. None collide with any prior fast or rigorous manifest. No
RC001 route is reused. The protected T100 directory was absent during the
unopened-boundary verification.

## Frozen decision contract

- Candidate/control modeled costs are `23,840,966,267` and `22,133,260,412`
  FLOPs; both receive the exact `0.1` score-floor multiplier. The incumbent
  retains `262,549,156,608` FLOPs.
- Each route uses eight 65,536-positive antithetic reference banks.
- Candidate/control and candidate/incumbent each receive a separately sealed
  eight-bank leave-one-out jackknife three-sigma MDE, floor `1.1e-12`, before
  any score or ratio is exposed.
- Each comparison uses 200,000 stratified network bootstraps and the one-sided
  98.75% nearest-rank upper bound at zero-based index `197499`, implementing
  Cycle-2 familywise alpha `0.0125` for the singleton slate.
- Orders 0 and 23 in every block must replay byte-exactly for all three scored
  arms before score access.
- A failed scored arm remains in all aggregates as an all-zero prediction with
  its full frozen compute charge, and any failure blocks R1/P2. Reference
  failure blocks a valid target/MDE and cannot be hidden by route removal or a
  replacement seed.
- All R1 and P2 mean, block, interval, MDE, p95, maximum-tail, integrity,
  reserve, and mechanism-ablation gates are frozen in the predeclaration and
  seal.

`ALG014-V000` is excluded because unchanged RC001 re-entry is forbidden.
Current-shape-only `ALG017-V002`, `ALG018-V000`, and `ALG018-V001` are excluded
because their historical P1 evidence is not established; no tier is silently
transferred.

## Human promotion disposition

- Subject / evidence class: `ALG017-V000`, prospective native rigorous RC002.
- Current tier / highest supported / next considered: historical
  `P1-promising` / `P1-promising` / `R1-mechanism-confirmed`, then
  `P2-competitive`.
- Positive evidence: T103 F3 candidate/control `0.944459`, bootstrap upper90
  `0.966411`, 24/32 wins, p95 `1.090611`, maximum `1.158732`; constant-only was
  neutral at `1.000051`, supporting the closure-guided direction.
- Gate results: freeze, native binding, translation parity, source/dependency
  binding, fresh blocks/seeds, RC001 exclusion, MDE order, replay, failure
  policy, and R1/P2 rules `PASS`; empirical R1/P2 gates `NOT-RUN`.
- Primary blocker class: `EVIDENCE_INCOMPLETE`.
- Why not promoted: no strict or scientific gate has failed; the newly frozen
  72-network program has not yet executed.
- Immediate high-impact unlock: agent executes T100, then applies the frozen
  rules in T101. No owner action is required.

## Verification

```bash
research/native_checkpoint3/rigorous_cycle2/build.sh
T099_REQUIRE_UNOPENED=1 experiments/checkpoint3/t099/verify_freeze.sh
```

Both commands passed. T100 is now the next task.

## Task timing

- Start: `2026-08-27T14:46:11,618366160-07:00`
- Pre-task estimate: `45 minutes`
- End/check-off: `2026-08-27T15:05:22,071435678-07:00`
- Actual wall-clock difference: `00:19:10.453069518`
