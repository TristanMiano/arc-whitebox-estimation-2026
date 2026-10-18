# T068 — rigorous Cycle 1 execution

## Outcome boundary

Rigorous Cycle 1 (`RC001`) is empirically complete. All 72 frozen routes—24
in each of B1, B2, and B3—were evaluated against `ALG014-V002` and
`ALG003-V008` with the exact T067-bound assets and routing. Every admitted
route is a verified T064 shard containing the three arm predictions and all
eight independent reference-bank predictions. There are no missing routes,
nonfinite values, admitted-run operational failures, or comparator
substitutions.

T068 does **not** award or reject `R1-mechanism-confirmed` or
`P2-competitive`. `RESULT.json` deliberately says
`complete_evidence_not_adjudicated` and contains no formal tier decision.
T069 owns that decision and route.

## Descriptive evidence

| Comparison | B1 | B2 | B3 | Pooled | Upper 97.5% | Mean benefit | Pair MDE | Wins | p95 | Max |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| candidate / iid mechanism | 0.625390 | 0.514844 | 0.454117 | 0.533290 | 0.707180 | 3.90611e-7 | 6.27594e-8 | 51/72 | 2.521804 | 7.510423 |
| candidate / incumbent | 1.495094 | 0.812056 | 0.874450 | 0.993461 | 1.360065 | 2.93770e-9 | 7.05578e-8 | 35/72 | 3.834159 | 9.998310 |

The mechanism-control mean result is strong and consistent by block. Its
arithmetic primary, interval, and target-noise comparisons are all favorable.
The tail is not: the observed p95 is `0.021804` above the frozen `2.5` limit,
and the maximum is `3.510423` above the frozen `4.0` limit. The maximum comes
from global route 27 (`rc001-b2-003`), where the raw candidate/control ratio
is `7.510423`.

The incumbent comparison is not a stable competitive win. Although its pooled
point ratio is just below one, B1 is `1.495094`, the bootstrap upper bound is
`1.360065`, the mean benefit is much smaller than target-noise MDE, and both
tail limits are exceeded. Mean final-layer raw MSE is `4.90814e-7` for the
candidate, `9.20361e-7` for the mechanism control, and `4.65445e-7` for the
incumbent. The candidate's lower modeled work moves the adjusted pooled point
comparison close to parity.

This pattern is partly expected and partly surprising. The large mean
mechanism benefit is consistent with E0004 and therefore unsurprising. The
frozen `4.0` maximum had already been relaxed prospectively from the generic
`1.5` rule because E0004 reached `2.312252`; observing `7.510423`, plus a p95
that narrowly exceeds `2.5`, is a moderately surprising worsening of the
tail. The weak and heterogeneous incumbent comparison is less surprising:
the fast evidence suggested competitiveness, not a high-confidence uniform
win on fresh blocks.

## MDE, determinism, and resources

The controller first merged prediction/reference bytes, then published
`MDE_SEAL.json`, and only afterward published `ROUTES.tsv` and `RESULT.json`.
The seal uses the prospectively frozen eight-bank leave-one-out jackknife,
three-sigma construction and binds merged payload SHA-256
`7a6dd4f1...`. It contains no score, ratio, win, or gate outcome.

Before opening RC001 output, both Clang and GCC builds byte-reproduced both
frozen T091A F1 records, covering all three arms. After all blocks completed,
full payload replays of routes 0, 24, and 48 were byte exact. A GCC rebuild of
route 0 was also byte exact to the Clang payload, including all three arm and
eight reference predictions.

Per-route analytical work is `247,350,948,181` FLOPs for the candidate,
`247,347,893,760` for the control, and `262,549,156,608` for the incumbent.
The candidate retains `24,649,051,819` FLOPs of modeled reserve. Effective
trajectory counts are 57,344, 58,852, and 62,464 respectively; each target
uses 1,048,576 effective trajectories. Summed steady-clock arm times were
223.85 s candidate, 331.75 s control, 334.66 s incumbent, and 5,927.98 s for
the eight-bank references. (The JSON field names say `cpu_wall`; the measured
clock is `std::chrono::steady_clock`, so these are wall durations summed over
routes.) Maximum per-worker process peak RSS was 333,701,120 bytes.

## Recovery and containment

Three controller attempts were excluded before the admitted run:

1. Attempt 001 passed pre-outcome parity but supplied xargs arguments in the
   wrong order. It computed no RC001 prediction and published no shard.
2. Attempt 002 computed four finite payloads, but a newline-handling defect in
   the validation adapter rejected them before publication. No score or MDE
   was computed. The adapter-only parser defect was corrected and directly
   regression-tested; estimator behavior did not change.
3. The prior xargs process had continued launching excluded workers after the
   validation failure. When the recovery reused the canonical path, T064 made
   the resulting mixed evaluator hashes visible. All scoped old/current
   workers were terminated, the mixed run was quarantined, and none of its
   shards entered the admitted merge.

The repaired controller now holds an exclusive run lock, converts any worker
failure to xargs' immediate-abort status, and verifies every retained T064
identity field. The final run identity is `ccd8e9a7...`, has 72/72 clean
shards, zero partials, and merged aggregate `621c3b41...`.

Two Clang compiler invocations also reproduced the known transient native
compiler crash. Each succeeded on the immediate bounded retry; no owner action
or reboot was requested. The build script records the approved maximum of
three attempts before it would stop.

## Human promotion disposition before T069

- Subject: `ALG014-V000`, rigorous RC001 evidence.
- Current/highest tier: `P1-promising` / `P1-promising`.
- Next possible tiers: `R1-mechanism-confirmed`, then `P2-competitive`.
- Evidence status: complete, reproducible, and ready for formal adjudication.
- Why no R1/P2 was awarded here: T068 is an execution task and T069 is the
  prospectively frozen adjudication owner—not because the evidence is absent.
- Immediate high-impact action: execute T069. Its report must make the strict
  tail-gate effect explicit rather than hiding the strong mean mechanism
  evidence.

Reproduce the retained integrity checks with:

```bash
bash experiments/checkpoint3/t068/verify_evidence.sh
```
