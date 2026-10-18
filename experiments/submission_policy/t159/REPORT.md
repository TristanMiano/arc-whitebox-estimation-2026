# T159 — trace compensation and Winograd submission attempt

**New official best: ALG049-V000.**
Submission **330887** returned adjusted **5.01785974707e-09**,
**7.403% lower** than ALG043-V000 / 330597.
The official gain closely matches the local 7.45% estimate. Official raw MSE
is 4.60% higher; the lower computation cost makes the adjusted score better.

| Measure | ALG049-V000 | ALG043-V000 |
|---|---:|---:|
| Official adjusted score | 5.01785974707e-09 | 5.41905133451e-09 |
| Official raw MSE | 2.23092068197e-08 | 2.13274181249e-08 |
| Reused development adjusted mean | 4.95490832475e-9 | 5.35358521402e-9 |
| Reused development raw mean | 2.18060020615e-8 | 2.08373676492e-8 |
| Settled local FLOPs | 480,530,585,472 | 555,383,704,047 |

## Change and evidence

This ships the integrated T158 P26 algorithm: a coupled native A/P basis,
explicit covariance-cup compensation of the principal third tensor's lost
trace, ranks 320/192, and 15-addition Winograd with shared scratch arenas.
It builds on 504aldo's MIT public V29 and retains the author's ages, calibration,
source machinery and first-call safeguard. The only change from the tested
research source encodes four configuration settings in five default literals,
including the nested covariance-depth fallback. No new fit or tuning.

T158's eight reused development networks provide 7.45% adjusted improvement,
8/8 wins, despite 4.65% higher raw error. That is an efficiency improvement.
The data were exposed and selected adaptively; the bootstrap support 1.0 was
never private-suite certainty. The prior subjective retained-win forecast was
85–95%, with 4–10% conditional gain. This task made **no new comparison panel**.
[Reused evidence](../../theory/t158/SELECTED_EVIDENCE.json),
[research specification](../../theory/t158/CANDIDATE_SPEC.md).

## Actual package checks

Five full-size calls on 750/772/817/885/885 all pass. The first four archived
predictions and per-call FLOPs exactly match T158; fourth/fifth predictions
are byte-identical. Counted work settles at 480.531B after the fourth call.
No private counter changes or uncharged full-size warmup were used.
SDK validation, allowed imports, manifest, clean extraction, and generated
1×1/5×3/32×6 fallback checks pass. The inherited off-contract width 2 limitation
is preserved in T147's record; no claim of universal shape support is made.

Maximum residual 0.30411s, outer wall
58.71s, RSS 7.129GiB,
setup 0.02227s. The numerical diagnostic arithmetic in P26
was retained and charged. [Package qualification](PACKAGE_QUALIFICATION.json),
[resource summary](RESOURCE_SUMMARY.json), [preupload seal](PREUPLOAD_SEAL.json).

Archive SHA256: `f61fc6eb9e0525f6d40c8c856a46becb88a360d116d036d36a1e4024512f001e`. The included license and README
preserve attribution. The incumbent source and all prior evidence are intact.

## Official feedback and timing

Submission **330887** was accepted at 14:48:47.840 UTC. The first observed
successful grade was at 15:32:13 UTC, about **43.42 minutes** later. One
attempt; no retry. The owner extended this round’s allowance to 120 minutes
from acceptance. The grade arrived before that deadline. Both monitor logs
retain the same grade; their local restart overlap is explained in
[the wait extension record](OWNER_WAIT_EXTENSION.json).
[Official state and decision](RESULT.json). No final-submission designation.

Elapsed **53.45 minutes** through records, against 45–90 estimated.
First acceptance after 8.06 minutes.
The five predictions total 4.30 metered minutes,
overlapping other work. External status timings are recorded separately;
these intervals must not be added or mislabeled as active research time.
No engineering-budget extension, new fit, agents or blind-block access.
[Timing](TIMING.json).

Proposed **T160: Focused empirical theory for a coherent fourth-history successor**. Use the T158 diagonal-repaired fourth-chain range and retained harmonic-star factors to choose an affordable trace projection and finite coupled response. Probe an integrated approximation early; retain a compatible conditional joint law as a distinct larger-upside route if the fourth-history cost/response remains weak. Avoid another scalar fit or rank ladder by default.
The measured efficiency gain is now retained. T158 found no convincing large accuracy breakthrough, but its repaired fourth-chain primitive provides a concrete next question. [Next proposal](NEXT_PROPOSAL.json). T160 has not started.
