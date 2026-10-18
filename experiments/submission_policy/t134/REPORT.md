# T134 — absolute-state calibration transfer

**ALG036-V000 is the new official best: adjusted 1.32636576382e-07, 2.6061% below ALG031.**
Submission **330097** graded successfully. One five-coefficient fit
on 32 training networks produced a **2.9794% local improvement**, 11/12 wins,
and bootstrap support 1.0 across 20,000 resamples. The private grade is separate
feedback; the bootstrap statistic was never treated as certainty of an official win.

| Evidence | ALG036 | ALG031 |
|---|---:|---:|
| Training terminal MSE, 32 F networks | 1.42489803686e-06 | 1.48942726794e-06 |
| Paired local terminal MSE,12 networks | 1.25031153442e-06 | 1.28870788486e-06 |
| Paired local adjusted mean | 1.25031153442e-07 | 1.28870788486e-07 |
| Official adjusted mean | 1.32636576382e-07 | 1.36185675387e-07 |
| Full-shape FLOPs | 218,987,691,813 | 218,986,065,179 |
| Multiplier | .1 | .1 |

Worst local ratio **1.004322**; median **.971104**. Paired90% bootstrap
mean-change interval: **[-5.339784e-9, -2.357585e-9]** adjusted-score units.
The 12 networks are predetermined reused development data, not fresh independent
validation. Predictions were sealed before comparison target access. The final
local blind block remains untouched.

## What changed

The fixed feature vocabulary comes from the public calibrated Gaussian estimator
found in T132 and reproduced in T133. ALG036 uses **ALG031's own terminal closure
state**: ReLU mean, pre-activation variance, normalized pre-activation mean
(alpha), mean absolute off-diagonal covariance mass, and an intercept. Physical
scaling is preserved. It adds their fitted linear combination inside the
existing capped correction; all earlier-layer outputs, existing coefficients,
sampling counts/streams, first Gram and covariance approximation remain fixed.
The public code/coefficient tuple is not inserted into this candidate. This is
an adaptation of known calibration ideas, with no academic-novelty claim.

The additional cost is **1,626,634 FLOPs**, roughly **.000743%** of ALG031.
The inexpensive covariance-row reduction reuses the already-computed matrix.
T130/T131's audited FastMultiplier workspace views are prepared in setup; all
numerical arithmetic stays in prediction. That change preserves parent bytes.

The one fit RMS-normalizes all five columns, forms the active Jacobian of the
existing cap/nonnegative output, and solves one ridge system anchored at zero
new coefficients. Ridge is .01 times the Gram diagonal. The first prescribed
step improves the penalized training objective, so no backtracking or refitting
is needed. Training MSE improves **4.3325%**.
New coefficients, in the feature order above:

```text
[-0.0004192398052785608, 7.995031271408047e-05, -2.799146938256936e-05, -0.009626244115040865, 0.0002789094629530628]
```

No individual-feature ablation was run: the result supports this complete
five-column correction, not a claim that each column is necessary or that one
particular statistic causes the gain. The original T133 cheap estimator remains
a separate useful baseline; this test does not establish a winning blend with it.

## Production and official feedback

All **46 full-shape prediction calls** completed on their first tries.
The nonzero diagnostic and fitted fixture match a direct feature/head reference
exactly. Zero new coefficients reproduce the historical ALG031 fixture exactly;
uncorrected predictions on every comparison row also match the sealed incumbent.
Fitted production matches the cached feature prediction byte-for-byte. Clean
archive extraction and a separate replay reproduce the final prediction exactly.

Across completed calls, residual time was
**0.2050–0.2309s**,
wall time **14.56–15.85s**,
peak RSS **4.491 GiB**, setup at most
**0.002119s**. Finite full-shape outputs, allowed imports,
`whest validate`, archive manifest and unchanged fallback review pass. Reuse of
fallback evidence is justified by the identical fallback implementation and
dispatch. No new scientific tier or final-submission designation is inferred.

Archive: `experiments/submission_policy/t134/packages/ALG036-V000.tar.gz`

SHA256: `0fdfa15c36c94def66692f8b8003b837d954b3c8189e1596b79d1607befcbb25`.
Accepted **2026-09-06T21:29:15.838Z**; first 30-minute deadline
**2026-09-06T21:59:15.838000+00:00**. One accepted submission, no retry.
[Official status and events](SUBMISSION_330097_STATUS.json).

## Research return and stopping point

The T132 literature trial led to T133's near-parity cheap baseline, then this
small feature transfer. Its measured retained official gain is now
**2.6061%**. Reusing a known calibration idea produced
useful submission evidence without a new theory recurrence or a feature search.
The [route tracker](../../../docs/RESEARCH_ROUTE_STATUS.md) keeps this as a
specific result; one successful transfer is not a diminishing-return curve or
proof about the whole learned-correction family.

T134 is complete. **Stop for owner selection of the next task.** The cheap
public-base successor and output-aware compression reserve remain available;
no further fitting, candidate execution or theory recurrence starts automatically.

## Time and reproduction

Start **2026-09-06T21:05:31+00:00**; checkoff **2026-09-06T21:44:06.401168+00:00**.
Elapsed **38.59 minutes**, versus50 estimated (-11.41).
Full-shape predictions total **11.72 metered
minutes**. Grader wait **14.63 minutes**
overlaps some final record preparation. These overlapping subtotals should not
be added as disjoint activity times. Verification and commit follow checkoff.
The 60-active-minute engineering budget was not extended.

For a target-free reproduction, use a fresh output directory:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
 tmp/t128-runtime312/bin/python experiments/submission_policy/t134/run_candidate.py \
 --source submissions/phase2_alg036_v000 --rows 0 --reference \
 --output /tmp/arc-t134-new-replay
```

[Specification](START_AND_SPEC.json) · [fit plan](FIT_PLAN_FREEZE.json) ·
[feature seal](FEATURE_SEAL.json) · [fit](FIT.json) · [source freeze](SOURCE_FREEZE.json) ·
[paired score](attempts/screen-sealed/SCORE.json) · [package checks](PACKAGE_QUALIFICATION.json) ·
[result](RESULT.json) · [verification](VERIFICATION.json).

Final verification and handoff records bring elapsed time to **39.95 minutes**
at **2026-09-06T21:45:28.236315+00:00**, versus50 estimated (-10.05). The scoped commit
follows. This includes1.36 minutes after checkoff.
