# T124 — one recalibration and official submission

**ALG029-V000 is the new official best:** submission 329806, adjusted **1.36755548851e-07**, 3.8961% below ALG028.

The single T122-A design was implemented, fit once on the existing 500 Full-F
training caches, frozen, and compared on the twelve predeclared reused
development networks. No new training propagation, comparison extension,
coefficient/gate grid, scientific funnel, or final blind evaluation was used.

| Evidence | ALG029 | ALG028 | Change |
|---|---:|---:|---:|
| Training final MSE | 1.388753669e-06 | 1.441467552e-06 | 3.6570% lower |
| Production-screen raw final MSE | 1.307289935e-06 | 1.351839225e-06 | 3.2955% lower |
| Production-screen adjusted mean | 1.307289935e-07 | 1.351839225e-07 | 3.2955% lower |
| Official adjusted score | 1.36755548851e-07 | 1.42299664617e-07 | 3.8961% lower |

The screen won **10/12** networks. All 20,000 paired whole-network bootstrap
draws improved the mean; the 90% interval for adjusted mean change was
[-6.6712e-9, -2.4927e-9]. The maximum network ratio was 1.00560422. This is
reused adaptive development evidence, not independent confirmation or a
calibrated probability of beating the private suite. The official grade is
separate feedback. The full sixteen-column recalibration earned the measured
gain; no ablation isolates the two new physical-shape columns.

## Implementation and qualification

The shipped parent carrier, twelve original features and raw parent correction
are retained. A normalized cap-aware anchored ridge fit adds four columns,
including the old correction discrepancy and the fixed physical Hermite
remainder, then applies the existing single cap and nonnegative projection.
The prescribed first training step was accepted; all coefficients were sealed
before comparison predictions. The inherited propagation, closure, source
seeds, early outputs and fallbacks are unchanged.

Actual cost is **218,985,745,647 FLOPs**, only **683,040** above the parent,
at multiplier **.1**. All twelve measured residual times were .3577–.3756s.
The successful clean extraction measured .3710s residual, roughly 16s prediction
wall time, .0013s setup and 4.30 GiB peak RSS. Finite full-shape output, allowed
imports, archive manifest, current-source deterministic replay and exact
fallback parity passed. Source and extracted package predictions matched
byte-for-byte. Cached numerical equivalence is separately recorded: fixture
maximum absolute difference 2.7419e-6, numerical MSE 2.9551e-13, within the
prospective 1e-5 / 1e-12 limits. Actual production outputs determined the score.

Three local processes failed in inherited numerical/runtime paths: the first
probe, the long screen after nine complete saved rows, and a second extraction
replay. Exact retries/recovery passed. Only the three missing screen rows were
regenerated; no outcome-based selection or refit occurred. The offline SciPy
environment and folder-packaging invocation also required routine corrections.
All failures are retained. The archive then uploaded once; no official retry.

Archive SHA-256: `c8e6e9286bc5c6e9ad5be8c5bb693e810162e7775bd0e0b69668038afef295cb`.
Raw records, source/fit seals, commands and checks are linked from [README](README.md),
[FIT.json](FIT.json), [production score](attempts/screen-sealed/SCORE.json),
[qualification](PACKAGE_QUALIFICATION.json), [official status](SUBMISSION_329806_STATUS.json),
and [RESULT.json](RESULT.json). No new scientific tier is claimed.

## Decision and timing

The local 3.30% gain is modest, near the low end of T122's planning range,
and the tiny inference cost prediction held. The next recommended bounded
task is **T125: early feasibility of T122-B covariance trace completion**,
starting from retained official **ALG029-V000**, without another fit. Existing
production tooling, the observed 15.56-minute time to upload, and preserved
source moments make a short attempt useful (roughly 30–60 minutes total);
the roughly .025s residual margin remains its main practical risk. Meter it
first and park promptly if the cap cannot be met cheaply. The covariance
hypothesis remains untested; T124 does not validate it. R3/CGMA remain parked.
T125 is nominated, **not started or authorized by this task**.

Start 2026-09-04T23:57:01+00:00; end/checkoff 2026-09-05T00:30:49.974234+00:00.
Elapsed **33.82 minutes**, versus 75
estimated (-41.18 minutes).
Upload occurred after **15.56 minutes**.
Approximate allocation is 2 minutes analysis, 9 implementation/repair/records,
6 local execution/recovery, and the remaining time waiting for the grader.
The task stops here; no additional experiment runs after its grade.
