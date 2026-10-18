# T167 — intermediate-supervised source submission attempt

**New official best: ALG052-V000.** Official submission 332641: adjusted 4.28518227437e-09, 1.91% lower than ALG051-V000.

| Measure | ALG052-V000 | ALG051-V000 |
|---|---:|---:|
| Official adjusted score | 4.285182274373245e-09 | 4.368514231311302e-09 |
| Official raw MSE | 2.0914763076973487e-08 | 2.1323075287682514e-08 |
| Local development adjusted mean | 4.50628182675e-09 | 4.59249151752e-09 |
| Local development raw mean | 2.19870977459e-08 | 2.24114793857e-08 |

The exact T166 P45 source and JSON weights replace the old 124-coefficient
correction with a 644-parameter nonlinear local mean source. The physical
trajectory and first 15 outputs remain byte-identical in the paired comparison.
No estimator changes, new fits or configuration overrides were made in T167.
This is our learned adaptation of the public 504aldo/V29 cumulant framework
through ALG050/051, not a pure copy or an academic novelty claim.

## Local decision and qualification

The predetermined initial 12 and one predeclared 12-network extension used
previously exposed development inputs outside the 32 fitting networks.
Both algorithms used actual metered calls in the same input order. Both prediction banks were sealed before targets were read.
Adjusted mean ratio **0.98122812**; raw ratio
**0.98106410**; **17/24 wins**. Whole-network
bootstrap support **0.99930**, 90% ratio interval
**[0.971613963005005, 0.9908272921237302]**. Worst ratio **1.032041**
on row 750. These reused data and bootstrap support are
not a calibrated private-suite probability. [Score](SCORE.json).

Initial 12 adjusted ratio 0.99564098, support 0.71332. The one predeclared 12-network extension used a fresh matched lifecycle and gave adjusted ratio 0.96749154. Both looks are retained; no further extension or refit. [Initial result](SCORE_INITIAL_12.json).

The prospective T166 forecast was 80–90% official-win probability and 1–4%
conditional adjusted gain. Its 2.79% fourfold CV gain and F0 fitting-input 1.19%
loss remain preserved; the shipped asset was tested without refitting.
The official gain closely matches the 24-network local gain; the weaker first
12 result was not reproduced by the extension. The initial baseline audit
found matching feature family and ridge settings. [Audit](TRANSFER_AUDIT.json).

The candidate was loaded from the actual clean archive. Its 24 comparison calls
also supplied resource checks; one additional row 999 call checked settled byte
replay. SDK validation, manifest/import checks and small-shape fallbacks pass.
Maximum residual **0.32522s**, peak RSS
**6.495GiB**, maximum prediction wall
**40.93s**, setup **0.02446s**.
No call-counter manipulation or uncharged full-size warmup. The inherited
width 2 off-contract limitation remains recorded; no universal-shape claim.
The extension input loader needed one cached-path repair before predictions;
its original failure is preserved. No algorithm repair was required.
[Package qualification](PACKAGE_QUALIFICATION.json).

Archive SHA256: `827a2ff81a318eb655013b7766df194b851d0bad4be34669db87d0121066d547`.
Estimator SHA256: `b094bb97c90e42d91b0552f80ed9f8817922afb99706f761a235cb49f86ae7b1`.
Weights SHA256: `3bb8b66e7d1988ba9984ccf1dae366ba5127449bd0465c6dcd75416c03bb4dce`.

## Official outcome and handoff

1 accepted attempt(s): [332641]. Standing 60-minute
allowance per attempt; at most one unchanged retry for a generic evaluator
problem. Valid unfavorable grades are not retried unchanged. No final-submission
designation, agents or final-blind access. [Result](RESULT.json).

Elapsed **73.69 minutes** through records against 20–85 initially estimated.
The one local extension was budgeted for at most 25 additional wall minutes
and 15 active minutes within the 60-active-minute task budget.
Exclusive timing: **19.54 minutes active engineering**, **22.00 minutes local
waiting**, and **32.15 minutes grader waiting**. Actual local predictions
used 31.26 metered minutes, overlapping some
preparation; these durations are not additive. Official acceptance/wait
milestones are retained in [TIMING.json](TIMING.json).

Proposed **T168: Empirical recurrence on affordable fourth-birth queries and new state information**. Prioritize T166 source-only third compression for fourth births: preserve the lower state, test a concrete approximate affordable constructor, and measure complete cost early. Explore materially new state information if that constructor is weak. Keep the learned incumbent as comparator; no automatic nearby NN sweep.
The small learned improvement is retained; the larger 39.6–41.4% generated raw capacity still needs an affordable complete implementation. The proposed active research floor is **240 minutes**. T168 has not started. [Proposal](NEXT_PROPOSAL.json).
