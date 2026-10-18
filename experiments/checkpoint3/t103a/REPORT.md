# T103A — Phase-2 ALG017 versus submission incumbent

## Answer

No: the faithful Phase-2 realization `ALG017-V002` is **not** better than the
current submission candidate `ALG015-V000` on adjusted score. On 12 fresh,
identical Phase-2 networks, its pooled adjusted-score ratio was `1.505849`,
with 0/12 wins. `ALG015-V000` remains the local and official project best.

This is not a failure of the scientific mechanism. `ALG017-V002` reduced raw
MSE by 57.34% relative to `ALG015-V000` and beat its own five-frame carrier on
all 12 networks. It loses only because preserving the parent's five independent
`2w x w` frames costs almost four times as much as the incumbent.

## Prospective construction and integrity

Before opening targets, T103A fixed a new U0 shape-specific identity,
`ALG017-V002`, without transferring `ALG017-V000`'s historical P1. It preserves
the parent mechanism exactly at Phase-2 dimensions:

- five independent 2048-by-1024 normalized Haar-Stiefel frames;
- antithetic propagation and exact first layer;
- order-12 density-weighted Price/Hermite full-covariance closure with the
  frozen `abs(alpha)>12` zero guard; and
- half-strength positive-part shrinkage only of the residual orthogonal to
  `span{constant, closure}`.

The source, exact cost probe, incumbent source, comparison program, shard hash,
rows 48--59, scoring rule, and `.10/.90` succession prior were sealed before
candidate accuracy. The next unopened Phase-2 shard was selected rather than
reusing T096 or T097 outcomes.

Windows-native contract validation passed. Two target-blind fixed-seed runs
were byte-, factor-, and FLOP-identical. A separate formula audit reproduced
the shrink factor and output from a NumPy reference, checked the parent
constants, exact saturated-tail zero, target independence, and finite output.

## Exact compute

| Arm | Exact FLOPs | Score multiplier |
|---|---:|---:|
| `ALG017-V002` | `776,207,157,195` | `0.352978` |
| five-frame carrier | `723,900,711,260` | `0.329192` |
| `ALG015-V000` | `196,459,652,235` | `0.1` |

All are inside the hard `2^41` budget. The candidate is well outside the
`0.1` score floor. To beat `ALG015-V000`, it prospectively needed raw MSE below
`0.283304` of the incumbent.

## Fresh direct comparison

| Metric | `ALG017-V002` | `ALG015-V000` | Candidate/incumbent |
|---|---:|---:|---:|
| pooled raw final-layer MSE | `1.136979385e-6` | `2.665134140e-6` | `0.426612` |
| pooled adjusted score | `4.013288781e-7` | `2.665134140e-7` | `1.505849` |
| adjusted wins | — | — | 0/12 |
| median paired adjusted ratio | — | — | `1.421632` |
| maximum paired adjusted ratio | — | — | `2.602969` |
| bootstrap upper 90% | — | — | `1.677822` |

The raw gain is large but misses the compute-adjusted break-even requirement:
`0.426612` observed versus `<0.283304` required. Equivalently, the candidate
uses a `3.52978x` multiplier but improves raw error by only `2.344x`.

Against the exact five-frame carrier, the candidate's raw ratio was `0.563025`
and adjusted ratio `0.603707`, with 12/12 wins, median `0.601124`, and maximum
`0.675744`. Every prospectively frozen current-shape mechanism gate passed.
This awards current-shape M1 to `ALG017-V002`; it does not transfer historical
P1, and it does not establish submission succession.

## Reproduction and defect audit

The complete 12-route WSL replay used identical source and data hashes. Exact
FLOPs matched on every arm. The candidate/incumbent ratio was `1.505849476`
versus Windows `1.505848701`, absolute difference `7.76e-7`; both environments
gave 0/12 adjusted wins, mechanism pass, and no succession. Maximum raw-MSE
relative platform difference was `1.69e-4`.

No plausible implementation defect was found: dimensionless sampling ratios,
five-block pooling, `width-4` positive-part coefficient, half damping,
closure projection, Hermite saturation, exact first layer, factor bounds,
contract, and charged operations all passed explicit checks. The 50.58%
adjusted-score loss is much larger than the platform numeric discrepancy.
Independent-machine/VM reproduction remains appropriate for the positive
mechanism claim.

The first post-outcome audit-harness invocation stopped before producing an
audit result because the script used JSON spelling `false` instead of Python
`False`. That isolated harness typo was corrected and the audit rerun; it did
not touch candidate source, cohort, scores, or frozen rules.

## Promotion, surprise, and route

- `ALG017-V000`: historical P1 remains preserved.
- `ALG017-V002`: current-shape M1 awarded; historical P1 not transferred.
- Submission succession: scientifically rejected on adjusted competitiveness,
  not blocked by an arbitrary strict gate. `ALG015-V000` remains best.
- Frozen no-succession probability `.90` gives only `0.152003` bits: the
  contest result was expected. The independently frozen `.45` mechanism-pass
  event gives `1.152003` bits and is positive evidence.
- The large raw and mechanism gain strengthens the rationale for T104, whose
  already-frozen H098-A/H098-B route tries to retain deeper Hermite benefit at
  score-floor-efficient compute. A smaller post-outcome ALG017 frame schedule
  would be a new variant requiring a new seal and fresh cohort; it cannot be
  substituted retroactively here.

No upload was authorized or performed. T104 remains next.

Timing: start `2026-08-27T10:41:56,951273555-07:00`; estimate `55 minutes`;
end/checkoff `2026-08-27T11:04:17,572844909-07:00`; elapsed
`00:22:20.621571354` (`1340621571354` ns).
