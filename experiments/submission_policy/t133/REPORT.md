# T133 — unchanged public calibrated Gaussian estimator

**No submission: the unchanged candidate has no supported advantage over ALG031.**
ALG035's adjusted mean is **0.7299% worse**, with **5/12 wins** and **.4319**
whole-network bootstrap support for improvement. The result is close and uncertain;
it does not establish that the public estimator is inferior on the private suite.
Official best remains **ALG031-V000 /329989**, adjusted **1.3618567538742354e-7**.

| Paired development evidence | Public ALG035 | Incumbent ALG031 |
|---|---:|---:|
| Raw final-layer MSE | 1.29811352689e-06 | 1.28870788486e-06 |
| Adjusted arithmetic mean | 1.29811352689e-07 | 1.28870788486e-07 |
| Actual FLOPs | 56,786,552,287 | 218,986,065,179 |
| Multiplier | .1 | .1 |

Worst paired ratio **1.212154**; median **1.031022**. The paired90% bootstrap
mean-change interval is **[-8.28325383e-09,
9.98628014e-09]** in adjusted-score units.
These are twelve predetermined **reused development networks**, not fresh
independent validation. Every candidate prediction was sealed before comparison
targets were opened. ALG031's existing sealed predictions were reused.

## What was reproduced

The [MIT public repository](https://github.com/agentaiventure-dot/arc-whest-estimator/tree/fb33bb5a66b4b0aed3022e6a70a9274d5957d61d),
Copyright(c)2026 venture_agent_ai, supplies the literal estimator source and
embedded16x5 calibration tuple. Source SHA256:
`0a22f57ce5670d1acac0b9bc9d15651fd49e04f1cae7210e2068369e3685c37c`.
The estimator and license match T132's pins byte-for-byte. No external NPZ was
included and no coefficients were refitted. The public author reports six
locally generated calibration-training MLPs and two holdouts, using400,000
Monte Carlo samples each; that training was not rerun or independently audited.
See [pinned results](public_reference/exact_cov_RESULTS.md#6-calibration-refit-at-higher-n-task-d).

The design propagates a Gaussian mean/full covariance through each layer.
Eight fixed quadrature nodes approximate the exact bivariate-Gaussian ReLU
covariance correction. A fixed affine correction uses mean, pre-activation
variance, alpha, mean absolute off-diagonal covariance mass and an intercept.
Only output estimates are calibrated; the uncorrected mean propagates forward.
The Gaussian-state assumption and finite quadrature are approximations, despite
upstream comments calling the underlying covariance identity exact.

Our measured cost is **1,091,583,200 FLOPs /1.96% above** the author's older
55,694,969,087 report. We preserve that discrepancy without inferring a cause;
it has no multiplier or feasibility consequence. Their reported submission329951
score1.32e-7 remains external evidence, not an independently verified receipt or
a paired score reproduced by this task. Our result uses a different panel.

## Production checks and checker correction

All14 full-shape predictions completed, including two fixture0 replays.
The fixture outputs and costs repeat exactly. The12 comparison runs pass first
try: residual **0.0455–0.0517s**,
wall **2.51–2.80s**,
peak process RSS **4.486 GiB** including input
loading, and setup at most **0.002312s** in that panel.
`whest validate` passes its2x4 smoke input, exercising the source's calibration
skip at other shapes. There is no claimed budget-adaptive fallback in this source;
the full production budget is the tested contract.

The first inherited runner returned a false failure because it required
nonnegative predictions. Fixture0 contains841 negative estimates, minimum
-0.0003342426. WhestBench0.16.0's `scoring.validate_predictions` requires finite
values and the right shape, and accepts this output. The original failed checker
result is preserved; [contract review](FIXTURE_CONTRACT_REVIEW.json) records the
successful official validation on its sealed output. Subsequent runs use that
contract and record negative counts. This correction changes no estimator code
or predictions and is not an operational failure or a relaxed official rule.
Negative estimates enter the reported squared error normally.

The source was imported successfully and its prediction arithmetic inspected:
FlopScope NumPy/statistics operations carry the numerical work. The optional
`__main__` local-engine entry remains upstream and is never executed on import.
Because the comparison did not support upload, no archive was created or
qualified; package-specific import review and clean extraction remain work for
any future submission of this source. No package-readiness claim is made.

## Decision and value of the literature lead

Stop after12 rows. A near-parity point estimate with a slightly adverse mean
and wide paired dispersion gives little reason to expect one extra block to
produce roughly90% support. Spend the next task on a changed hypothesis rather
than another look at this fixed algorithm. No minimum gain or extra confidence
gate was used. No fit, comparison extension, new ensemble, upload or final-blind
access occurred. The broader Gaussian/calibration route stays open.

The useful discovery is **near-parity observed accuracy at25.93% of ALG031's
FLOPs**, leaving **163.116B FLOPs below the discount floor**. The literature
trial has produced a tested cheap baseline, but **zero retained official gain**
so far. It does not yet demonstrate redundant incumbent components or a winning
combination; those require separate tests.

Propose **T134 /L132-B**, one small absolute-state correction on the existing
incumbent using available states and one frozen training fit. This is the
lowest-change transfer to try next. Preserve rebuilding from the cheap public
base and L132-C output-aware compression as alternatives. These are proposals,
not automatic execution or a permanent strategy change. The
[route tracker](../../../docs/RESEARCH_ROUTE_STATUS.md) records the scoped update.

## Time and reproduction

Start **2026-09-06T20:49:50+00:00**; checkoff **2026-09-06T20:59:30.249035+00:00**.
Elapsed **9.67 minutes**, versus40 estimated (-30.33);
default60-active-minute ceiling not extended. The14 metered calls total
**0.613 minutes**.
Shard loading, source/runner review and recordkeeping supply the rest, with
some overlap; grader wait was zero. Verification/commit follow checkoff.

Registered acquisition and runner preparation: `python3 experiments/submission_policy/t133/prepare.py`.
This script intentionally refuses to overwrite the completed registration.
For a target-free replay, use a fresh output directory:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  tmp/t128-runtime312/bin/python experiments/submission_policy/t133/run_candidate.py \
  --source submissions/phase2_alg035_v000 --rows 0 --repeats 2 \
  --output /tmp/arc-t133-new-replay
```

[Specification](START_AND_SPEC.json) · [source seal](SOURCE_FREEZE.json) ·
[paired score](attempts/screen-sealed/SCORE.json) · [decision](DECISION.json) ·
[result](RESULT.json) · [verification](VERIFICATION.json).

Final evidence verification and handoff records bring total elapsed time to
**14.11 minutes** at **2026-09-06T21:03:56.760522+00:00**, versus40 estimated
(-25.89). This includes **4.44 minutes** after
the decision checkoff; the scoped commit follows.
