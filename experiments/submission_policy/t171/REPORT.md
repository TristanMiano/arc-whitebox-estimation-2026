# T171 — quadratic mixed-cumulant covariance submission attempt

**New official best: ALG053-V000.** Official submission 335391: adjusted 4.15561726455e-09, 3.02% lower than ALG052-V000.

| Measure | ALG053-V000 | ALG052-V000 |
|---|---:|---:|
| Official adjusted score | 4.1556172645504615e-09 | 4.285182274373245e-09 |
| Official raw MSE | 2.0127173101514018e-08 | 2.0914763076973487e-08 |
| Local adjusted mean | 4.33558405482e-09 | 4.46262197884e-09 |
| Local raw mean | 2.09655880261e-08 | 2.17523119985e-08 |

The unchanged T170 P49 source adds 32 analytic covariance-defect fields with 96
fixed coefficients across 3 layer bins, using the already completed all 32 fit.
It changes the physical covariance trajectory and retains ALG052's learned
mean-source asset. No fitting or algorithm repairs occurred in T171. This is
our adaptation of the public 504aldo/V29 cumulant framework using standard
cumulant/Edgeworth/Hermite machinery, without an academic priority claim.

## Local decision and qualification

The fixed 12-network comparison used previously exposed development
inputs outside the 32 fitting networks. The exact ALG052 source/runtime/input
order/call-position prediction bank was reused from T167; its compute was not
repeated. Candidate predictions came from the clean actual archive and were
sealed before targets were read. These are reused development data, not fresh
validation. No comparison extension was needed.

Adjusted mean ratio **0.97153290**, raw ratio
**0.96383263**, **11/12 adjusted wins**.
Whole-network bootstrap support **1.00000**, 90% ratio
interval **[0.9619059979018771, 0.9806101761373159]**. Worst network ratio
**1.002523** on row 750.
Bootstrap support is a screening diagnostic, not private-suite probability.
The earlier forecast was 80–90% official-win probability and 1–4% conditional gain.
[Score and per-network records](SCORE.json).

All 13 new full-size calls pass resource limits, including one additional
settled byte replay. SDK validation, manifest/import checks, exact archive
identity and small-shape fallback checks pass. Maximum residual
**0.39595 s**, peak RSS
**6.314 GiB**, maximum prediction wall
**42.79 s**, setup **0.02152 s**.
The inherited width 2 off-contract limitation remains recorded. No forced
call-counter warmup. [Qualification](PACKAGE_QUALIFICATION.json).

The first packaging command omitted sibling assets in single-file mode. The
manifest check rejected it before full-size predictions. Folder packaging fixed
this without source changes; original archive/logs remain in
`failed-packaging-001/`. [Recovery](PACKAGING_RECOVERY.json).

Archive SHA256: `13f9dd52e24fde2987d16b004cd66d6049b31a3b2cb630a53c9652826c2ccc4e`.
Estimator SHA256: `f31d8c70733464b0ad1d60ba240442299165b8658df9d9aa95538139d32d0e50`.
Neural asset SHA256: `3bb8b66e7d1988ba9984ccf1dae366ba5127449bd0465c6dcd75416c03bb4dce`.

## Official outcome, time and next step

Submission **335391** graded successfully on the first attempt after **34.90 minutes**.
The official adjusted reduction of **3.02%** closely matches the local **2.85%**;
official raw MSE fell **3.77%**. No retry was needed. The standing allowance
was 60 minutes per attempt. No final designation,
agents or final-blind access. [Result](RESULT.json).

Elapsed **50.55 minutes**, versus 30–120 estimated. Exclusive categories:
**9.91 minutes engineering, 5.57 minutes local waiting, and 35.07 minutes grader waiting**. New full-size predictions used
**8.91 metered minutes**, overlapping
some engineering work. Historical incumbent compute is excluded from new task
time. [Timing and grader milestones](TIMING.json).

Proposed **T172: Broader empirical recurrence on covariance structure and information-preserving compression**. Develop pair-conditioned covariance corrections and a concrete joint covariance/third-moment compression idea, guided by the T170 diagnosis. Start with small actual-cost probes, retain cheap candidates as fallbacks, and prioritize credible larger score reductions. Re-rank against an adjacent-literature refresh; do not default to another coefficient or neural sweep. The small covariance gain is retained; larger gains need additional useful state information or compression that preserves it.
T172 has not started. [Proposal](NEXT_PROPOSAL.json).
