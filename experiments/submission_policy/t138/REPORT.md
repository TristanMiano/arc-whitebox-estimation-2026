# T138 — CSK3-R cost reduction and submission

**New official best: ALG038-V001.**
ALG038-V001 submission **330153** graded at **1.46676758754e-08**,
**15.5539% lower** adjusted score than V000.
One mathematical recurrence, no fitting or state compression.

| Quantity | V001 | V000 |
|---|---:|---:|
| Local raw MSE | 4.53095008665e-08 | 4.53072293406e-08 |
| Local adjusted mean | 1.55952916773e-08 | 1.84669820565e-08 |
| Local prediction FLOPs | 756,892,228,334 | 896,310,006,000 |
| Local multiplier | 0.344194735741 | .407594600802 |
| Official adjusted score | 1.46676758754e-08 | 1.73692836098e-08 |

## What changed

The final layer computes only the marginal quantities its output mean needs.
For M=W.T, the diagonal of M C M.T is the row sum of (M C)*M;
the covariance response uses the same identity. For transformed paired factors
At=M A and Bt=M B, the marginal third is sum_r At_ir Bt_ir^2.
The repeated remainder contributes sum_j (M E)_ij M_ij^2. These replace
full matrices whose off-diagonals were never used by the last mean response.
All earlier state updates, factors, coefficients, cutoffs and moment formulas
are unchanged. The independent small dense-tensor oracle agrees within 2.85e-13.

The single deeper kernel uses four levels of the retained public product
identities and cached rectangular workspace. Its generated matrix products
agree with float64 dense references to relative Frobenius error below 4.6e-6.
Input-independent workspace allocation and view preparation moved into setup;
all network-dependent arithmetic remains in prediction. The before/after
setup fixture outputs are byte-identical. Setup did not establish a material
residual-time reduction on its one paired fixture; both passed. The setup
move also shifts allocation/view charges out of the prediction window, as
[the recorded comparison](SETUP_EQUIVALENCE.json) explicitly shows.

Final marginal work alone reduced prediction FLOPs to 845,501,381,358,
a 5.67% reduction. Depth 4 before setup preparation measured758,286,260,974.
The final implementation measures 756,892,228,334, a 15.5546%
reduction. These are actual local meters, not the earlier projections.

## Evidence and limits

The fixed 12 reused development networks give adjusted ratio **0.844495957**,
**12/12 wins**, bootstrap support **1.000000**,
and worst network ratio **0.844865948**.
The 90% bootstrap interval for mean adjusted change is
[-3.0418025044755008e-09, -2.7137830741855508e-09].
No interim score look, comparison extension, coefficient fit or new training
corpus. Bootstrap support is descriptive screening evidence, not a calibrated
private-win probability. The final local blind block remains untouched.

Across this panel, maximum all-layer RMS difference from V000 is
3.80509e-07, and maximum absolute difference is
2.38419e-06. The prospectively registered
bounds were 5e-6 RMS and 5e-5 maximum absolute; actual adjusted MSE also passes.
Different floating-point operation order is allowed under this new version;
historical V000 byte identity is not claimed. The final archive replays its
own fixture exactly, including actual prediction FLOPs.

Recorded completed calls span 31.87–43.08s
wall and 0.3278–0.3900s residual.
Peak process RSS is 6.338GiB; setup at most
0.006384s. Required limits pass. Small generated shapes
exercise a one-layer case and ordinary-product fallbacks. The unchanged
moment kernel retains T137's qualification; only affected checks were added.

The first depth3 fixture completed its prediction but failed afterward because
the copied harness pointed to the old T135 parent directory. Correcting that
path and rerunning saved its output; no estimator arithmetic changed.
The failure and meter remain in [the log](DIAGONAL_DEPTH3_PROBE.log).
[Operational notes](REPAIRS.md) preserve the setup decision.

## Official package and time

Archive: `experiments/submission_policy/t138/packages/ALG038-V001.tar.gz`. SHA256:
`b5cad63ef997dc0ead3dd17587b56340580119de8d460f95bcd5e9a9e5f6f367`.
The package passes manifest/import validation, relevant shape and numerical
checks, clean extraction and exact current-design replay. Official attempt
1 graded successfully. The initial monitor reached its 30-minute
endpoint without a result. One final status check observed the successful
grade at 31.01 minutes and avoided the permitted unchanged retry. The original
deadline remains in OFFICIAL_ATTEMPT.json; the latest status snapshot comes
from that zero-wait recheck. [Wait endpoint](WAIT_ENDPOINT.json). Official raw MSE is **4.26135243714e-08**.
[Receipt](SUBMISSION_330153_STATUS.json) · [full result](RESULT.json) ·
[qualification](PACKAGE_QUALIFICATION.json).

Start 2026-09-07T03:27:43Z; checkoff 2026-09-07T04:21:09.351407+00:00.
Elapsed **53.44 minutes**, versus75 estimated (-21.56).
Through upload: 21.35 minutes; official grading wait:
31.01 minutes. The 17 fully recorded
metered prediction calls total11.71 minutes;
the first harness-error prediction adds 31.88 seconds. These times overlap
elapsed work, and grader waiting overlaps records. No engineering extension
or subagents. [Timing](TIMING.json).

Await owner selection. Recommend a focused recurrence on compression of the persistent joint-cumulant history and a specifically motivated omitted correction. Preserve the successful full state as comparator; avoid extending T138 into a kernel tuning campaign.

Final evidence review and scoped commit preparation bring elapsed time to
**56.57 minutes** at2026-09-07T04:24:17.059306+00:00, versus75 estimated
(-18.43). The53.44-minute figure above is the decision checkoff.
