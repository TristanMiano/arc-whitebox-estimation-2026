# T075 — initial graded Phase 2 fallback and N1 candidate

T075 is complete. The owner explicitly authorized upload after configuring the
credential outside the repository. The exact two T074 archives were submitted,
both reached the terminal `graded` state, and neither was designated for the
final private rerun.

| realization | submission | adjusted score | final-layer MSE | vs sampling approx. | result |
|---|---:|---:|---:|---:|---|
| `ALG003-V009` N0 fallback | `328477` | `7.811135410795243e-7` | `3.122393313788052e-6` | `1.5363x` (`1.5x` display) | graded successfully |
| `ALG014-V003` N1 candidate | `328479` | `6.607199502584784e-7` | `2.509378157355968e-6` | `1.8162x` (`1.8x` display) | graded successfully |

The Phase 2 leaderboard code defines `vs Sampling` as its fixed Monte Carlo
reference `1.2e-6` divided by adjusted score. The submission API reports
adjusted score as `score` and final-layer MSE as `score_secondary`.

**`ALG014-V003` is the better of the two directly comparable project Phase 2
submissions: adjusted score is 15.413% lower and final-layer MSE is 19.633%
lower than `ALG003-V009`. It remains the current official submission
candidate.** This is official contest evidence, but submission does not itself
transfer the Phase 1 parent's P1 or create a new scientific tier. `ALG014-V003`
remains U0/N1 and `ALG003-V009` remains U0/N0.

The complete fields exposed by the participant API are preserved in the two
submission JSON files: submission/challenge/round IDs, creation timestamp,
terminal status and message, adjusted score, and final-layer MSE. The API does
not expose per-MLP grader internals. The exact artifact hashes match T074.

This task consumed two of the ten Phase 2 submissions permitted per UTC day.
No final designation was made. T095 remains the next independent scientific
task.
