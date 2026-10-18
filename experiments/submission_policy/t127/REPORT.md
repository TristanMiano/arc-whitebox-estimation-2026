# T127 — parity-split response fit and official feedback

**ALG031-V000 is the new official best:** submission **329989**, adjusted **1.36185675387e-07**, **0.4167% below ALG029**.

One 22-column anchored fit reused all 500 Full-F training caches; six new
columns separate odd mean, even mean and variance responses and their global
means. The prescribed full training step was accepted and frozen before
production comparison. No new training propagation, grid, comparison refit,
extension, scientific funnel or final-blind evaluation was used.

| Evidence | ALG031 | ALG029 | Relative mean change |
|---|---:|---:|---:|
| Training final-layer MSE | 1.38147294544e-06 | 1.38875366883e-06 | 0.5243% lower |
| Production-screen raw MSE | 1.28870788486e-06 | 1.30728993478e-06 | 1.4214% lower |
| Production-screen adjusted mean | 1.28870788486e-07 | 1.30728993478e-07 | 1.4214% lower |
| Official adjusted score | 1.36185675387e-07 | 1.36755548851e-07 | -0.4167% |

The screen won **9/12** networks, with **.98205** whole-network bootstrap
support. The 90% adjusted mean-change interval was
[-3.26803e-9, -4.08695e-10]; maximum network ratio **1.02090962**.
These are predetermined reused development networks, not fresh independent
validation or a calibrated private-suite probability. The approximately .90
submission target was already met, so no further local comparison followed.
The complete fitted update earned the gain; no ablation isolates a mechanism.

## Production and package

The parent source realization, propagation, closure, trace, coefficients,
first fifteen outputs, cap and fallback remain intact. The new update sits
inside the same cap. Actual cost is **218,986,065,179 FLOPs**, only **319,532**
above ALG029, at multiplier **.1**. Screen residual time was
**0.3610–0.3783s**,
prediction wall time **15.84–16.40s**,
setup at most .00138s and peak RSS below 4.30 GiB. Eleven screen rows completed
on their first attempt. Row953 failed once in inherited FlopScope fast
propagation before the new head; only that missing row was retried, with
unchanged source, and completed before any comparison scoring.

Zero new coefficients reproduce current ALG029 byte-for-byte. The unchanged
parent's final outputs match the retained T124 outputs on every screen row.
The fitted fixture is deterministic; cached formula agreement has maximum
absolute error 3.33786e-6 and numerical MSE 3.27246e-13, inside the predeclared
1e-5 / 1e-12 tolerance. Actual production outputs decide the score.

Whest validation, allowed imports, archive manifest, clean extraction with
byte-exact production replay, unchanged exact cost, finite full-shape output,
and low-budget/unsupported-shape parent fallback all pass. The fitted asset
and archive hashes remain sealed. Archive SHA-256:
`b40b309a9fa3a353fa3f8d9163fa8bd1566299af87e3338558cefb8607c0f247`.

The first package command needed its output directory created. Later the
upload CLI exited139 without an ID or error text. A fresh server response's
public submission history showed no acceptance since that command began;
the unchanged archive was then accepted using the standard single-thread
runtime environment. The crash's root cause is unproved. The Windows browser
helper could not initialize in WSL; no Windows input occurred. This local
client recovery did not change the algorithm and was not an official retry.
One accepted submission received a grade; no evaluator retry was needed.

## Next action and time

Recommend **T128**, the already frozen one-direction functional shape option,
from retained official **ALG031-V000**. The lower-response fit's local gain
supports a small additional attempt, while the beyond-third-order shape
hypothesis remains untested. Its separate failure cases still apply. Bind the
actual parent, meter a nonzero head before any new training collection, then
collect only the 32 declared F feature rows if feasible. One two-coefficient
fit and the lean score screen suffice. Estimate **45–90 minutes total**, with
60 active engineering minutes initially and reassessment around thirty.
Do not extend a difficult special-function implementation on an old forecast;
record a finite concrete payoff or return to theory. **T128 has not started**.
R3 and CGMA stay parked; no scientific tier or final designation changes.

Start 2026-09-06T00:45:06+00:00; end/checkoff 2026-09-06T01:20:11.879968+00:00.
Total **35.10 minutes**, versus **45 estimated** (-9.90 minutes).
Acceptance occurred after **16.11 minutes**;
acceptance-to-checkoff was 18.99 minutes,
including overlapping record preparation and grading wait. Metered production
prediction time totaled 4.01 minutes; input loading and records
are additional. Final verification and scoped commit follow checkoff.

See [commands and failure records](README.md), [fit](FIT.json),
[source freeze](SOURCE_FREEZE.json), [local score](attempts/screen-sealed/SCORE.json),
[package qualification](PACKAGE_QUALIFICATION.json), [official status](SUBMISSION_329989_STATUS.json),
[verification](VERIFICATION.json), and [result](RESULT.json).
