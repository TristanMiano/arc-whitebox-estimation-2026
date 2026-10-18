# T135 — one joint correction refit

**New official best: ALG037, adjusted 1.28580467731e-07, 3.0581% below ALG036.**

The single 27-column fit improved training MSE **2.3234%**.
On the 12 fixed reused development networks, adjusted mean changed by
**+3.3367% improvement**, with **12/12 wins**
and **1.00000** paired bootstrap support.
Submission **330101** graded at **1.28580467731e-07**, +3.0581% improvement versus ALG036. One accepted submission, no retry. Grader wait 13.00 minutes.

| Evidence | ALG037 | ALG036 |
|---|---:|---:|
| Training terminal MSE,32 networks | 1.39179231797e-06 | 1.42489803686e-06 |
| Local terminal MSE,12 networks | 1.20859182288e-06 | 1.25031153442e-06 |
| Local adjusted mean | 1.20859182288e-07 | 1.25031153442e-07 |
| Official adjusted mean | 1.28580467731e-7 | 1.32636576382e-7 |
| Full-shape FLOPs | 218,987,857,755 | 218,987,691,813 |
| Score multiplier | .1 | .1 |

Worst local ratio **0.99524271**;
90% bootstrap mean-change interval **[-5.215088851612891e-09, -3.1464859259158357e-09]**.
These are adaptively reused development networks. Bootstrap support is a local
screening statistic, not a calibrated probability of improving the private grade.
All comparison predictions were sealed before their targets were accessed.
No final local blind data was opened.

## Change and bounded work

This is a joint regularized update over the existing 22 response columns and
five absolute-state columns. The current ALG036 coefficients remain as an
arithmetic anchor, with one added linear update inside the same cap. This is
equivalent to refitting their combined coefficients, while preserving byte-exact
zero-update behavior. Original 12 theta columns are already included in the 22;
no feature is omitted from the joint correction span. Sampling, propagation,
early-layer outputs, covariance calculation, and fallback dispatch are unchanged.

The fit uses 32 declared training networks, RMS column scaling, the active
Jacobian of the clipped head, and ridge .01 times its Gram diagonal. One linear
system was solved. The first prescribed step, **1**, lowered the
penalized objective. There was no hyperparameter grid, feature search, alternate
fit, or comparison-driven coefficient adjustment. The tiny extra cost is
**165,942 FLOPs**. Existing source licenses are retained.

## Cache compatibility and production

All 32 training rows reuse hashed T118/T120/T134 caches. An initial cache-builder
import failed because the production environment lacks SciPy; reconstruction
used the already-installed system SciPy, without changing production dependencies.
The first diagnostic completed but failed a newly imposed near-exact feature
check. That result is preserved, not relabeled as passing. Inspection found
that T127 had already documented approximate historical caches and accepted
max output error 1e-5 / numerical MSE 1e-12. Before target access, T135 recorded a
[contract correction](CACHE_COMPATIBILITY.json) to reuse that tolerance.
No candidate source or mathematical feature was changed in this correction.

Current carrier, raw ALG036 correction, cap and all five absolute columns are
byte exact against the new cache; the old 22 columns have maximum relative RMS
difference **0.6453%** on the fixture. The fitted cached-head output differs from
production by maximum **3.57627868652e-07** and numerical MSE
**3.61851878906e-15**, negligible against terminal MSE
around 1e-6. Actual production outputs decide the score. Fitted cache equality
is approximate; zero-update historical ALG036 equality is exact.

All **15 production calls** completed first try. The original diagnostic
checker rejection is separate from runtime/resource failure. Residual time was
**0.2096–0.2226s**;
prediction wall **14.75–15.57s**;
peak process RSS **4.491 GiB**, setup at most
**0.002155s**. Allowed imports and unchanged fallback checks pass.
The qualified archive passes manifest/import checks, CLI validation, clean extraction and a byte-exact current-design replay.

Archive: `experiments/submission_policy/t135/packages/ALG037-V000.tar.gz`.

SHA256: `5d6ddf7461fe7322c592bddfd420c8e5e5068797a47f34bd7f005e61e74748d5`.

## Decision and time

T135 closes this one fixed joint-refit attempt. It does not establish the best
possible coefficients or exhaust learned correction as a family. The next
recommended investment is a focused literature refresh and then theory on the
cheap Gaussian baseline and output-aware compression. Avoid an open-ended chain
of small coefficient tweaks. No next task starts automatically.

Start **2026-09-06T21:51:33+00:00**; checkoff **2026-09-06T22:19:38.180445+00:00**.
Elapsed **28.09 minutes**, versus 30 local /45 including grading estimated.
Local completion through upload took **14.95 minutes**, versus 30 estimated. Total estimate error **-16.91 minutes**. Production calls total
**3.79 metered minutes**;
grading wait **13.00 minutes** overlaps
bookkeeping. No engineering-budget extension. Final verification follows.

[Specification](START_AND_SPEC.json) · [cache amendment](CACHE_COMPATIBILITY.json) ·
[feature seal](FEATURE_SEAL.json) · [fit](FIT.json) · [source freeze](SOURCE_FREEZE.json) ·
[paired score](attempts/screen-sealed/SCORE.json) · [result](RESULT.json).

Final verification/handoff time: **29.06 minutes**, at **2026-09-06T22:20:36.564970+00:00**,
versus45 estimated (-15.94). The scoped commit follows.
