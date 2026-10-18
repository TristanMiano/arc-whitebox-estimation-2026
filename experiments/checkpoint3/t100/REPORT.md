# T100 report — rigorous Cycle 2 execution

## Outcome boundary

Rigorous Cycle 2 (`RC002`) is empirically complete. All 72 T099-frozen routes,
24 in each of B1, B2, and B3, were evaluated for historical-P1
`ALG017-V000`, exact shared-frame carrier `ALG017-V001`, and native incumbent
`ALG003-V008`. Every admitted route is a validated T064 shard with all three
scored predictions and eight independent reference-bank predictions. There
are no missing routes, nonfinite predictions, operational failures,
substitutions, or post-freeze tuning decisions.

T100 deliberately does **not** award or deny `R1-mechanism-confirmed` or
`P2-competitive`. The machine-readable result is
`complete_evidence_not_adjudicated` and contains no formal tier decision.
T101 is the prospectively frozen adjudication owner.

## Descriptive evidence

| Comparison | B1 | B2 | B3 | Pooled | Upper 98.75% | Mean benefit | Pair MDE | Wins | p95 | Max |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| candidate / mechanism carrier | 0.961582 | 0.917224 | 1.003198 | 0.962267 | 0.985252 | 1.85958e-8 | 1.49674e-9 | 52/72 | 1.156528 | 1.217949 |
| candidate / incumbent | 1.418156 | 0.753330 | 1.421474 | 1.136546 | 1.406062 | -5.69748e-8 | 2.62396e-8 | 30/72 | 4.019953 | 5.270800 |

The mechanism comparison retains a real, well-resolved pooled benefit: the
point ratio and familywise upper bound are below one, the mean benefit is
`12.42x` its target-noise MDE, 52/72 routes win, and both frozen tail limits
have wide margin. B3 is narrowly adverse at `1.003198`, however, missing the
frozen every-block `<1` condition by `0.003198`. The largest route ratio is
`1.217949` at global route 21 (`rc002-b1-021`). This is not a reversal of the
mechanism direction; it is a heterogeneous-block result with one marginal
strict block miss.

The incumbent comparison is scientifically adverse on these fresh blocks.
The candidate is worse in B1 and B3, pooled ratio is `1.136546`, the upper
bound is `1.406062`, the measured benefit is negative, and both frozen tail
limits are exceeded. Its B2 ratio `0.753330` and enormous `248.159B` FLOP
reserve do not make the result broadly competitive. The largest route ratio
is `5.270800` at global route 49 (`rc002-b3-001`). Mean final-layer raw MSE is
`4.742332e-6` candidate, `4.928290e-6` mechanism, and `4.322782e-7`
incumbent. After the exact compute multipliers, the corresponding means are
`4.742332e-7`, `4.928290e-7`, and `4.172584e-7`.

These descriptions expose how the frozen gates line up but do not substitute
for T101's formal application. Relative to T103, the pooled mechanism gain is
expected and somewhat smaller (`0.962267` here versus `0.944459` there); the
tiny B3 reversal is mildly surprising but not a scientific mechanism
reversal. The fresh incumbent loss is a more meaningful adverse update from
T103's context-only `0.726672` comparison, although T099 froze no numeric R1
or P2 outcome prior from which to compute surprisal bits.

## Integrity, budget, and reproducibility

The controller rebuilt independent Clang 17 and GCC 13 evaluators. Both
byte-reproduced the T099-bound candidate and carrier on two already-open T103
F1 inputs before any RC002 outcome was accessed. All six frozen sentinel
routes (0, 23, 24, 47, 48, and 71) then reproduced the entire payload—three
scored arms and eight reference banks—byte-exactly.

The T064 run contains 72/72 complete hash-bound shards and zero partials. Its
run identity is `d0384a9e...`, merged payload hash `6805e88b...`, and aggregate
hash `bec605e7...`. `MDE_SEAL.json` was published before `RESULT.json`, binds
the merged payload/aggregate, and contains no score, ratio, win, or gate
field. Candidate/control/incumbent modeled FLOPs per route are
`23,840,966,267`, `22,133,260,412`, and `262,549,156,608`; both ALG017 arms
are inside the exact `0.1` score floor. Summed steady-clock arm durations were
21.81 s candidate, 20.02 s carrier, 312.11 s incumbent, and 5,501.09 s for
the reference banks. Maximum per-worker peak RSS was 336,121,856 bytes.

Maximum Haar orthogonality and leverage-sum errors were `6.65544e-7` and
`1.28529e-5`, within their frozen `2e-5` and `2e-4` limits. All exact-first-
layer, reference-count, finite, and shared-frame identity checks passed. No
failure fallback was invoked and no controller attempt needed exclusion or
repair.

## Human promotion disposition before T101

- Subject / evidence class: `ALG017-V000`, complete native rigorous RC002.
- Current / highest awarded tier: historical `P1-promising`.
- Next tiers considered: `R1-mechanism-confirmed`, then `P2-competitive`.
- Submission succession: not comparable on this historical width-256/depth-32
  lane. `ALG018-V000` remains the local and officially graded Phase-2 best;
  T100 supplies no evidence that a challenger beat it.
- Strongest positive evidence: candidate/carrier pooled `0.962267`, upper
  `0.985252`, benefit `12.42x` MDE, 52/72 wins, p95 `1.156528`, maximum
  `1.217949`.
- Gate alignment, not yet a formal decision: the mechanism comparison passes
  pooled, interval, MDE, p95, maximum, integrity, and budget conditions but
  B3 `1.003198` misses the every-block `<1` condition by `0.003198`. The
  incumbent comparison has several scientific competitiveness failures.
- Why not yet promoted or formally denied: evidence is complete, but T101 is
  the prospectively frozen adjudication owner. This process boundary—not an
  absent run or owner action—is the immediate blocker.
- Strict-gate transparency: for the mechanism/R1 comparison, the marginal B3
  block condition appears to be the sole arithmetic gate miss. For P2, strict
  gating is not the sole issue; the incumbent comparison is scientifically
  adverse on pooled, interval, breadth, and tails.
- Immediate high-impact action: the agent should execute T101 now. No owner
  action or gate waiver is required.

Reproduce the retained integrity checks with:

```bash
bash experiments/checkpoint3/t100/verify_evidence.sh
```

## Task timing

- Start: `2026-08-27T15:07:48,806459865-07:00`
- Pre-task estimate: `65 minutes` (plausible range `45–100 minutes`)
- End/check-off: `2026-08-27T15:56:29,832476019-07:00`
- Actual wall-clock difference: `00:48:41.026016154`
