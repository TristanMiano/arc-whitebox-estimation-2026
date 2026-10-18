# T128 — one-direction shape attempt

**Close ALG032-V000 without submission.** Its twelve-network adjusted mean was
**0.7171% worse** than ALG031, with **5/12 wins** and **.0484** bootstrap support
for improvement. Retain official **ALG031-V000**, submission **329989**, at
**1.3618567538742354e-7**. No comparison extension or refit is justified.

The frozen T126-B head uses one covariance direction and a radially integrated
26-bin functional statistic with Hermite orders zero through three removed.
Only its coordinate response and global mean receive new coefficients, inside
the unchanged parent cap. Every parent coefficient and earlier output is fixed.
Exactly 32 prescribed F feature rows were sealed before their targets were
used. One anchored two-column fit accepted the full step; coefficients are
[0.27012531404381174, -247.43953178803764]. Its training gain did not transfer to the comparison.

| Evidence | ALG032 | ALG031 | Candidate change |
|---|---:|---:|---:|
| Training terminal MSE, 32 F rows | 1.48641782259e-06 | 1.48942726794e-06 | 0.2021% lower |
| Production terminal MSE, 12 rows | 1.29794976008e-06 | 1.28870788486e-06 | 0.7171% higher |
| Production adjusted mean | 1.29794976008e-07 | 1.28870788486e-07 | 0.7171% higher |

The paired 90% mean-change interval is
[7.73328821e-12, 1.9057123e-09].
The worst network ratio is **1.043585207**.
These are predeclared reused development networks, not independent validation
or a calibrated private-suite probability. The result rejects this complete
fitted variant; it does not disprove higher-order functional corrections or
isolate which component failed. No ablation, direction/loading/bin/training-size
grid, scientific tier, final-blind evaluation, package or upload followed.

## Production and runtime evidence

Actual cost is **219,257,819,691 FLOPs**, **271,754,512** above ALG031, keeping
the multiplier at **.1**. The nonzero diagnostic F0 passed twice, reproduced
deterministically and returned the exact parent when its coefficients were
zero. The numerical scalar translation passed the bounded check; the frozen
radius rounding and two initial reference-check failures are explained in
[NUMERICAL_NOTE.md](NUMERICAL_NOTE.md), with all raw evidence retained.

Training under the inherited CPython3.10.20 environment incurred **eight
incomplete attempts**: four during inherited fast propagation, two during
inherited closure, one during imports, and one during an extra parent replay
after the candidate had already completed successfully. A bounded runner
repair removed that redundant replay and checkpoints output immediately after
the meter. It did not cure all interpreter failures. Row402 also completed
with residual **.40529988s**, above the .4s cap; that resource failure and its
valid features were retained, with no passing replacement chosen for the row.

One isolated runtime check then used existing system **CPython3.12.3**, keeping
WhestBench0.16.0, FlopScope0.12.0 and NumPy2.2.6. The diagnostic output, both
features, carrier, cap and parent matched the earlier fixture byte-for-byte,
with the same cost. The two remaining training rows, fitted fixture and all
twelve comparison rows completed on their first attempts in that environment.
The fitted cache agrees exactly. Every comparison parent matches T127's
sealed production output byte-for-byte. Comparison residual time was
**0.2924–0.3093s**,
wall time **15.25–15.97s**,
peak RSS **4.486 GiB**, and setup at most
0.001610s. Required imports and unchanged fallback
source/dispatch checks pass. No archive qualification is claimed.

The old environments were preserved. The runtime switch worked for these
checks; the earlier crashes' root cause is unproved. Use
`tmp/t128-runtime312/bin/python` and the recorded
[runtime pins](runtime312-requirements.txt) for a future local submission
attempt, reusing these checks where relevant. This is operational evidence,
separate from the negative algorithm result.

## Next action and time

Recommend **T129**, a new theory recurrence against retained ALG031. Both
T126 nominees have now been tested: T127 gave a small official gain, while
this single-direction shape fit lost locally. Seek a more transferable,
low-cost successor rather than automatically sweeping this variant. Preserve
the projection and finite-moment limitations; theory may nominate zero to two
candidates. The policy minimum is 60 active minutes unless the owner requests
longer. **T129 has not started.** R3/CGMA remain parked.

Start **2026-09-06T01:23:36+00:00**; end/checkoff **2026-09-06T02:14:19.588667+00:00**.
Elapsed **50.73 minutes**, versus **75 estimated**
(-24.27 minutes). Completed prediction meters total
12.84 minutes across
48 logged calls, including row209's successful call lost during later
bookkeeping. Input loading, failed calls and repairs are additional. No grader
wait or engineering-budget extension. Final verification and scoped commit
follow checkoff.

See [decision](DECISION.json), [feature seal](FEATURE_SEAL.json), [fit](FIT.json),
[source freeze](SOURCE_FREEZE.json), [score](attempts/screen-sealed/SCORE.json),
[runtime recovery](ISOLATED_RUNTIME_RESULT.json), [result](RESULT.json), and
[verification](VERIFICATION.json).
