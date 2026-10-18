# T105A — qualify and officially evaluate ALG018-V000

## Result

**`ALG018-V000` is now the best officially graded project submission.** The
owner-authorized first upload, submission `328678`, eventually failed with only
the generic message `Evaluation could not complete; please retry`. The exact
unchanged archive revalidated, account/round eligibility passed, and the owner
authorized one sealed retry. Attempt 2, submission `328686`, graded
successfully at adjusted score `2.6931472416436013e-7`, final-layer MSE
`2.693147241643601e-6`, and `4.455753x` versus sampling approximation.

Against prior official best `ALG015-V000` submission `328500`, adjusted score
ratio is `0.947111337`: a **5.288866% official reduction**. Both entries use
the `.1` score multiplier, so the raw final-layer-MSE ratio is the same. The
official score was only `0.624372%` above T104's prospective public-cohort
estimate, closely confirming the predicted direction and scale.

## Hard-gate qualification

The immutable archive is
`experiments/submission_policy/t105a/packages/ALG018-V000.tar.gz`, SHA-256
`7dff1ba505a85e237fdfc0e7b5ab114bcb2df30910195b9129c27e6cdeff02d9`,
size 3,583 bytes. It binds estimator SHA-256
`7c1228792721deae9d99bcb9accbd0445bc4bbb1fd33d0e637d260c2e3c7eee0`
and the MIT license. The accepted manifest records Python 3.10.20,
WhestBench 0.16.0, flopscope 0.12.0, and NumPy 2.2.6.

Contract, package, and fresh-extraction validation passed. Two fixed-seed
fresh-extraction runs were byte-identical at exactly `216,711,677,067` FLOPs,
maximum wall time `2.6041s`, and residual time `0.04925s`. Peak working set was
`255,217,664` bytes and setup was `6.56us`. Local and isolated-subprocess runs
on public Phase-2 network `logan-fitzgerald` agreed exactly: adjusted score
`2.628418315e-7`, final-layer MSE `2.628418315e-6`, exact FLOPs, zero failures,
and maximum residual time `0.04290s`. All hard minimum limits passed.

The first valid package inherited Python 3.12 from a temporary tool runner.
This was detected before upload and self-repaired by rebuilding on Python
3.10.20 without changing estimator bytes, then repeating the full gate. An
initial fixed-seed harness invocation also stopped at import because its
isolated environment lacked `psutil`; adding that harness-only dependency and
rerunning the unchanged package passed. Neither incident reached AIcrowd or
constitutes candidate evidence.

## Official and scientific disposition

Submission `328686` replaces `ALG015-V000` submission `328500` as the best
officially graded project entry. Attempt `328678` is preserved as a generic
external operational failure; it is not algorithm evidence. `ALG018-V000`
retains current-shape M1 and local submission succession; no historical
P1/R1/P2 tier transfers from packaging or official grading. No final
designation was made. T099 is next.

Timing so far: start `2026-08-27T12:23:56,030409122-07:00`; estimate
`35 minutes`; owner-directed pause poll
`2026-08-27T13:01:31,928864452-07:00`; active elapsed to pause
`00:37:35.898455330` (`2255898455330` ns). Resumed
`2026-08-27T14:35:04,385766073-07:00` with a `20 minute` additional estimate.
Final checkoff: `2026-08-27T14:42:40,209000376-07:00`. Start-to-finish wall-clock difference:
`02:18:44.178591254` (`8324178591254` ns), including owner-directed pause
`01:33:32.456901621`. Cumulative active elapsed was `00:45:11.721689633`
(`2711721689633` ns); the resumed interval was `00:07:35.823234303`.
