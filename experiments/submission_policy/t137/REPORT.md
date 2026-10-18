# T137 — CSK3-R implementation and submission

**New official best: ALG038-V000, adjusted 1.73692836098e-08; 86.4915% below ALG037.**

Submission **330141**; 1 official attempt(s).
The complete12-network local comparison gives **84.7202% lower adjusted score**,
**12/12 wins**, and bootstrap support **1.0**. No coefficient fit or sampling.
This is an end-to-end estimator result; no component ablation or new theorem is claimed.

| Local evidence | CSK3-R / ALG038 | ALG037 |
|---|---:|---:|
| Raw final-layer mean squared error | 4.53072293406e-08 | 1.20859182288e-06 |
| Adjusted arithmetic mean | 1.84669820565e-08 | 1.20859182288e-07 |
| Actual FLOPs | 896,310,006,000 | 218,987,857,755 |
| Multiplier | 0.407594600802 | .1 |

Raw error fell **96.2512%** despite
charging the full4.076× multiplier increase. Worst adjusted network ratio:
**0.19808395**. The90% bootstrap
mean-change interval is [-1.1056548336980395e-07, -9.410218947701756e-08].
These are reused development networks, not independent validation or a calibrated
private-grade probability. The final local blind block remains untouched.

## Implementation

The final T136 section22 source is implemented with coefficient-one physical
response around an uncalibrated Gaussian reference. Persistent paired factors
carry joint third-order structure; a repeated-index remainder and radial
fourth-order scalar complete the specified approximate recurrence. Modeled
repeated third entries are matched; the full true third/fourth tensors are not
claimed exact. The output is the nonnegative corrected physical mean.

Dense factor products use float32 and the retained licensed three-level matrix
kernel. Moment formulas and centralization use float64, stable positive-tail
cumulants, and physical rescaling. Rectangular products share flat workspace.
Small shapes exceeding that workspace use ordinary tracked products.
All numerical work uses permitted FlopScope APIs. No accounting changes,
untracked numerical computation, fitted assets, new training data or parameter search.

Reproduce a final-source production fixture from the repository root with
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 tmp/t128-runtime312/bin/python experiments/submission_policy/t137/run_candidate.py --source submissions/phase2_alg038_v000 --rows 0 --output tmp/t137-replay-001`.
The fixed comparison rows and bootstrap seed137001 are in START_AND_SPEC.json;
all actual invocations and source hashes are retained in attempt START records.

## Evidence and execution repair

The initial full-shape workspace-view mistake was corrected before any score.
The successful original core and cached-view implementation produced byte-identical
outputs at the same cost; caching reduced residual overhead. Independent small
pair checks match the derived equations within7.4e-9. Rectangular float32 products
match dense float64 to relative Frobenius error at most2.6e-6. The initial
unscaled absolute tolerance rejection is preserved, with its correction explained
in [REPAIRS.md](REPAIRS.md).

Four native crashes interrupted the comparison; one row exhausted its unchanged
retry. The five completed prescribed prefix rows were sealed and scored as an
**incomplete diagnostic**, giving adjusted ratio.15517. This justified bounded
repair and was never treated as the full submission screen. No equation or
coefficient changed after this interim look. An isolated CPython3.12.13 check
also crashed, so the original qualified runtime was retained.

A generated marginal-only reproducer localized the problem away from model
weights and matrix workspaces. An explicit-operator rewrite also failed.
Extracting the positive-tail arithmetic into a helper, with explicit returned
fields, then passed64 generated calls and a byte-exact full-shape fixture with
unchanged FLOPs. The remaining seven prescribed rows and clean archive replay
all passed first try. This demonstrates a usable repaired realization; the
crashes' root cause remains unproved. Original failures and source snapshots
are preserved. [Repair evidence](SOURCE_REPAIR_RESULT.json).

All12 prediction outputs were sealed before opening the remaining seven targets;
the earlier5-row look is disclosed in [the final score](attempts/screen-sealed/SCORE.json).
There was no24-row extension, new fit, or comparison-driven numerical tuning.

## Production and official feedback

Completed full-shape calls took **32.24–34.07s**;
residual range **0.302–0.368s**;
maximum observed RSS **5.611GiB**.
The final archive passes import, manifest, finite-shape, small-shape fallback,
resource, exact current-design replay and actual-cost checks. The first
single-file packaging command was rejected before creating an archive; folder
packaging succeeded and the rejected result is retained.

Archive: `experiments/submission_policy/t137/packages/ALG038-V000.tar.gz`. SHA256:
`e83da8bbea78b45be296edaea50a31083079bfdb497442b276ec9b2a31cd5745`.
Official adjusted score: **1.7369283609807433e-08**; raw score: **4.2613318385065216e-08**.
Official predecessor adjusted score: **1.285804677308988e-07**.
[Exact result](RESULT.json) · [Archive checks](PACKAGE_QUALIFICATION.json).

## Time and next action

Start **2026-09-07T01:07:11+00:00**; checkoff **2026-09-07T02:18:18.490512+00:00**.
Elapsed **71.12 minutes**, versus100 estimated
(error **-28.88 minutes**). Local work through upload:
**45.85 minutes**. 17 completed metered full-shape calls consumed
9.39 minutes; failed calls
and input loading are additional. Grader wait overlaps recordkeeping.
No engineering-budget extension or subagents. [Timing](TIMING.json).

Await owner selection. Recommend a focused recurrence on cheaper representations of the successful joint-cumulant state and its leading omitted correction. Keep removal of unused final-layer contractions and deeper equivalent matrix kernels as a cheap implementation option, while prioritizing a credible larger improvement. Re-rank A2LR as a reserve; do not run it automatically.
