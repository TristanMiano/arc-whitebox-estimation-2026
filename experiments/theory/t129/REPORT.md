# T129 — coordinated theory recurrence

**Final route: T130 / PF1760 first; T131 / FC4S second if still worthwhile.**
Both are prospective definitions. Official best remains ALG031-V000,
submission 329989, adjusted **1.3618567538742354e-7**. No new candidate was
implemented, trained, run on challenge inputs or submitted in this recurrence.

Completed in **209.32 minutes to record checkoff**, versus225 estimated
(-15.68 minutes). Timing is in TIMING.json and RESULT.json. The owner
requested at least three hours, with all work complete within four; root time
and overlapping agent time are accounted separately below.

## The practical result

| Order | One proposed attempt | Why it is worth trying | Subjective chance of a retained official gain | Forecast active work |
|---|---|---|---:|---:|
| T130 | **PF1760:** fast padded partial propagation,1760 child pairs, direct initial Gram | More samples with frozen coefficients and a lower projected cost | **35%** (20–55%) |45–75 min|
| T131, conditional | **FC4S:** full-covariance fourth-plus-skew-squared field on all outputs; one scalar fit | Tests persistent shape error with a small implementation, now affordable | **25%** (15–35%) |35–60 min|

These are uncalibrated planning probabilities including implementation and
qualification failure, not the roughly90% support used at submission time.
For either win, roughly.3–3% score reduction is a plausible planning range,
not a measured effect. PF forecasts60–105 elapsed minutes including a possible
grade; FC4S55–90 to a local decision, then up to30 per accepted official try.
Both start under the existing60-active-minute budget and reassessment near30;
estimates do not grant automatic extensions.

The useful late discovery was simple: the first closure covariance is I, but
the source still uses its general congruence. The public repeated-weight Gram
spelling saves **2.146B charged FLOPs on paper** with the same mathematical
matrix. It strengthens PF1760 and independently funds FC4S even if PF loses.

PF1760 projects216.408B FLOPs before its200M ancillary allowance. FC4S projects
219.340B on current counts with only the Gram saving, or219.108B on the PF
parent including its allowance. Both stay below the current219.902B discount
floor boundary in this calculation. **No actual package meter has confirmed
these projections.** Residual time and changed floating-point contractions
remain ordinary feasibility questions for the early integrated fixture.

The final definitions are [PF1760](CANDIDATE_A.md) and [FC4S](CANDIDATE_B.md),
with source hashes and predetermined data roles in DECISION_FREEZE.json.
One small paired twelve-network development screen, optional single extension
to24 only when useful, and prompt official feedback are sufficient. There is
no new scientific gate, minimum-effect threshold or experiment ladder.

## What the theory established

**We can now explain an important old control failure.** First-layer absolute
ridge features contain mostly quadratic marginal variation. The current QR
frames integrate that component unusually well, so pointwise regression can
learn the wrong coefficient for the error of a whole frame. Subtracting the
exact degree-two component produces a control whose remaining frame covariance
is tightly related to its analytic point covariance. For the1536-row child the
factor is between.9999937 and1.0019468 times the IID value. This is a proved
ideal-law harmonic bound, not just a fit to a few synthetic frames.

It also yields a local reason for PF1760: the degree-four-and-higher covariance
of both current main/child response channels falls by at least5.73% under the
stated equal-law, regular-mask linearization. This is not a whole-score theorem.
The complete head can change bias and masks, and degree-two leakage can rise.

**A small learned range does not automatically have small fitting noise.**
An exact Gaussian example shows that selecting and fitting a rank-one range
on the same observations can retain all1024-dimensional selection noise.
The repaired R4IF8-P uses main samples for its range/pilot, independent partial
samples for coefficients, and the child for application. Its full current-head
influence includes trace, source-fit, all22 columns, cap and scored pilot mask.
Remaining mixed fourth-moment and shared-partial risks are explicit.

**The current shape track has a more complete low-cost approximation.** Two
covariance products give the full leading fourth cumulant and leading third
cumulant for every realized output direction. The fourth response must be tied
to the squared-third response at the same perturbative order; a fourth-only
field can predict the wrong sign even when its fourth cumulant is correct.
The resulting FC4S avoids T128's single-direction coverage limitation.

The approximation is still limited: it can have70% relative cumulant error
even as width grows, and exact cubic moments can worsen it by omitting
same-order hidden Hermite4 contributions. One scalar fit may repair a common
scale/sign defect, but cannot repair every direction. These counterexamples
motivate a cheap score test, not a larger prerequisite study.

**Several apparently broad avenues are narrower than they looked.**
Depth innovations with equal transport weights telescope to existing terminal
features. A naive Gaussian conditional mixture omits conditional third/fourth
cumulants and can get the fourth-cumulant sign wrong even with exact conditional
mean and positive variance. At fixed counts, preserving current quadratic
balance leaves less than.1% possible fourth-harmonic variance improvement for
the2048-row main frame through another positive function-independent geometry.
That bound leaves room for more samples, adaptive controls and better closure.

## What changed in the neglected-track map

T117's favorable DS/M selection evidence is preserved. Its depth-history
features retain some information beyond the current22 columns, but much of
the simple transported mean reached the current parity head already. It is a
credible small-fit reserve rather than fourteen wholly new mechanisms.

The earlier audit's phrase “no empirical rejection” for RCERC was too broad:
the exact T119 spelling was untested, but H107-L/M supplied relevant adverse
family evidence. The harmonic repair responds to that evidence specifically.
R4IF8-P was the tentative second nominee, then moved to reserve when the Gram
saving made FC4S quicker to implement. Its final specification is preserved;
the re-ranking is not a control experiment loss.

The uniform-continuation review recovered a cheaper exact vector-average
surrogate identity. It also showed why T092's.6197 conditional finite-bank
proxy cannot be read as a38% leaderboard gain. The immediate useful offshoot
was exact compute reinvestment. Output-aware compression, quadratic partial
controls, hidden norm cumulants and independent H3 products retain explicit
formulas and reopening conditions in [RESERVES.md](RESERVES.md).

## Work style, evidence and the one-time agent trial

This recurrence was predominantly deduction: equations, cost algebra,
counterexamples, source review and small synthetic mathematical checks. It
included fixed input-only feature-span and source-disagreement calculations
on64 previously cached F rows. Those projections and synthetic regressions
were not candidate training. No challenge-target arrays or final-blind data
were opened, and no new challenge propagation occurred.

PF1760 requires no coefficient fit. FC4S proposes one supervised scalar fit on
32 prescribed training networks. The more statistically learned R4IF8-P is a
reserve. No rank, count, ridge, output-selection or training-size sweep ran.

Three agents covered exact controls, uniform/compression/cost, and the current
shape track. Root covered observer history, synthesis and independent
derivations. Finished agents received bounded follow-ups when a concrete
question became useful; at most three sub-agents ran simultaneously. Cross-
review materially changed the result: it repaired the control fit, identified
the missing squared-third term, and exposed the Gram saving that changed the
final ranking.

This shows useful parallel contributions in this task. It does not establish
that Ultra or this allocation is cost-optimal: there is no matched solo run or
token-cost comparison. No reset was used, no model/effort setting was changed,
and no permanent multi-agent protocol was added.

## Timing and verification

Root completed **181.15 active theory minutes**:
03:49:53–07:11:02 UTC, less a conservative20-minute overhead allowance.
Final record/verification/commit work is excluded from that minimum.

| Contributor | Active theory/source-analysis minutes | Main work |
|---|---:|---|
| Root |181.15|Observer history, independent mathematics, synthesis and candidate comparison|
| Exact-control agent |86.14|Kernel, QR theorem, influence and coefficient risk|
| Uniform/cost agent |86.74|Continuation, partial control and compute reinvestment|
| Current-shape agent |112.03|Conditional/cumulant models, full field and re-ranking|

Agents total **284.91 overlapping person-minutes**;
root plus agents total **7.77 person-hours**.
These do not multiply wall-clock credit. All agent research ended by06:50:09 UTC.
Activity categories are approximate, based on verified intervals and stated
overhead deductions; they are not a second-by-second profiler. Task elapsed
time and its225-minute estimate error are recorded at final checkoff.

The mathematical checks cover harmonic kernels, trace/full-head calculus,
Wick contractions, conditional-cumulance counterexamples and the stated cost
identities. Already-passing checks were not rerun as a new validation suite.
Initial analysis/script errors and their repairs are preserved and explained
in [SOURCES.md](SOURCES.md); final record/hash/link checks are in VERIFICATION.json.
No production qualification is claimed by these theory checks.

Root mathematics: [SCRATCHPAD.md](SCRATCHPAD.md). Agent work:
[controls](agents/rcerc/LEARNED_RANGE_RISK.md),
[sampling/cost](agents/uniform/DECISION_DRAFT.md),
[current shape and final re-ranking](agents/current_shape/LATE_BUDGET_RERANK.md).
The durable strategy documents receive dated addenda; their historical task
census and earlier probabilities are not rewritten as if T129 were known then.
