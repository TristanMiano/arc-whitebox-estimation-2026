# T131 — full-covariance fourth and skew-squared response

**Park ALG034-V000 as an inconclusive small positive lead; no submission.**
The twelve-network adjusted mean is **0.0185% lower** than ALG031, with
**5/12 wins** and **.6348** whole-network bootstrap support. This is not enough
support for a submission, and an extension has low expected decision value.
Retain official **ALG031-V000 /329989**, adjusted **1.3618567538742354e-7**.

| Evidence | FC4S / ALG034 | ALG031 numerical training parent / official comparison parent |
|---|---:|---:|
| Training MSE,32 F networks |1.48870773306e-06|1.48940840763e-06|
| Production terminal MSE,12 networks |1.28846928895e-06|1.28870788486e-06|
| Production adjusted mean |1.28846928895e-07|1.28870788486e-07|

Training improved **0.0470%** with one scalar **2.61579629719448**, accepting
the full prescribed step. No parent coefficient was refitted. The worst
comparison ratio was **1.002488654**.
The paired90% mean-change interval is
[-1.36458379e-10, 8.92246358e-11].
The data are predetermined reused development networks, not independent
validation. All32 feature records were sealed before training targets;
all12 fitted predictions were sealed before comparison targets.

## What was implemented and checked

FC4S retains native layer14 Gaussian covariance, floored marginal variance,
alpha/pdf/cdf and physical scale. Two depth5 covariance products provide the
leading third/fourth cumulants in all1024 actual final-weight directions.
One tied fourth-plus-squared-skew response is added inside the existing cap.
Native final-layer sigma/alpha supply the physical normalization. All ALG031
source counts, random streams, radius and fitted coefficients remain fixed.
Layer0 uses the direct identity-covariance Gram. T130's cached workspace views
are reused with identical ordered tracked arithmetic during prediction.

Actual integrated cost is **219,333,252,379 FLOPs**, **347,187,200** more than
ALG031, retaining multiplier **.1** and about**569.1M** floor headroom.
The field/state/head costs2,493,622,272 when reconciled with the source-accounted
2,146,435,072 Gram saving. No isolated Gram or field ablation was scored.

The first nonzero fixture passed. Against direct float64 contractions on the
same saved native state, field relative RMS error was **1.752e-5**. At the final
fitted scalar, output maximum difference was **5.960e-8**, terminal numerical
MSE **4.136e-18**. The zero-update head equals its numerical parent byte-for-byte;
the fitted output and field equal the sealed cache byte-for-byte. Child moment
preservation passes. The initial Gram's zero-update output differs from the
historical ALG031 fixture by at most**2.861e-6**, numerical MSE**8.430e-14**,
within the registered tolerance. Historical byte identity is not claimed.

All32 training rows, the fitted fixture and all12 comparison rows passed
on their first attempts. Comparison residual time was
**0.2247–0.2420s**,
wall time **15.25–15.93s**,
peak RSS **4.486 GiB**, and setup at most
**0.002626s**. Finite nonnegative full-shape outputs, imports,
`whest validate`, unchanged source coefficients and inherited fallback checks
pass. No production repair, retry, archive qualification or upload was needed.
The runner gained a cheap zero-update composition check before the fitted
fixture; it changed no production arithmetic or collected feature.

## Interpretation and stopping decision

This result preserves a small favorable point estimate. It is neither a
demonstrated mechanism gain nor a scientific rejection of higher-order shape
methods. It does not tell us whether the limited effect comes from approximation
error, redundancy with the incumbent, or another source; no ablation was run.

The observed mean advantage is only.335 estimated standard errors. Doubling
the sample size at the same effect/dispersion would give about.473 standard
errors, still far from roughly90% support. That planning calculation is not a
new statistical gate or a prediction of the unseen rows. It supports stopping
instead of spending another comparison block on this weak lead. There is no
minimum-gain threshold, additional fit, coefficient/rank/output/count sweep,
final-blind access, scientific tier or automatic reserve experiment.

**Stop for the owner's strategy discussion.** Both T129 nominees are now
resolved as bounded attempts: PF1760 lost locally; FC4S has a small inconclusive
positive result. No new recurrence or candidate task has started.

Start **2026-09-06T19:26:17+00:00**; end/checkoff **2026-09-06T19:55:10.635872+00:00**.
Elapsed **28.89 minutes**, versus75 estimated (-46.11).
The **45** completed prediction calls total
**11.77 metered minutes**;
input loading, monitoring and records are additional, with some overlap.
No overall engineering-budget extension or grading wait. Verification and
scoped commit follow checkoff.

[Specification](START_AND_SPEC.json) · [feature seal](FEATURE_SEAL.json) ·
[fit](FIT.json) · [source freeze](SOURCE_FREEZE.json) ·
[score](attempts/screen-sealed/SCORE.json) · [decision](DECISION.json) ·
[result](RESULT.json) · [verification](VERIFICATION.json).
