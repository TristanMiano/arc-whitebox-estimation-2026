# Route status and marginal value of more research

First snapshot: **T132, 2026-09-06**. This tracker implements the owner's request
to estimate when routes are becoming exhausted and adjust time accordingly.
It is a lightweight planning record, not another submission gate.

Two different questions are tracked: how thoroughly we have searched the
relevant literature, and whether a specific implementation remains promising.
**High search saturation does not mean a route has failed.** An untested
adaptation may be worth implementing even when more generic searching is poor
value. A negative test closes its tested spelling; a theorem closes only its
stated assumptions. Reopening triggers keep parked branches from disappearing.

The probability column estimates: **another 30 minutes of focused external
search, starting from this index, finds an actionable result that changes which
bounded implementation or theory question we would choose**. These are broad
subjective ranges, not calibrated probabilities of an official score gain.
Paper counts and repeated appearances of familiar ideas do not count as leads.
Recommended minutes are ceilings for the next authorized refresh, not promises
to spend that time on every row. The rows overlap; do not add their probabilities.

| Route | Search saturation / implementation status | Chance next 30 min changes action | Next search ceiling | Reopen or spend more when… |
|---|---|---:|---:|---|
| R01 Public Phase2 code and calibrated closure | T147 independently reproduces unchanged V29: official 5.42e-09, 54.20% better than JSP. Further unchanged generic searching has low value | 0–10% | 0 now;2–5 min for a changed release | New source or outcome evidence. The L85 publication met the earlier reopening condition; T147 completes its reproduction. Reopen on changed source or a named implementation gap. |
| R02 Small learned output corrections, including DS/KCAS | T158 fresh five-feature trajectory head yields about0.94% held-out raw gain and0.67% LOO; shipping head unbuilt, nominee has no new fit | 0–10% for generic regression; named new feature may reopen | 0 now | Information outside the current trajectory features or a changed physical state. Preserve the current fit as a small reserve; no automatic training campaign. |
| R03 Structured sampling geometry at unchanged counts | High for static positive frame/design route; scoped bounds and tested losses constrain it | 0–10% | 0–5 min | New adaptivity, useful extra samples, different weight restrictions, or a concrete scoring mechanism changes the T112/T129 assumptions. A new MUB citation alone does not. |
| R04 Learned exact controls / independent-source R4IF8-P | Medium-high; corrected specific reserve untested, related predecessors lost | 10–20% | 10 min | A low-dimensional control explains actual frame-estimation error cheaply, with fitting noise and head influence included. Use L05/L07/L09 and existing derivations. |
| R05 Multifidelity and uniform suffix continuation | High for basic variance/allocation formulas; current full-risk advantage unresolved | 5–15% | 5–10 min | A cheaper correlated surrogate or different sample overlap changes total risk after charging the source bank. Reuse L05/L06 instead of starting allocation algebra again. |
| R06 Marginal cumulant / terminal shape refinements | T158 final NIG gives0.36% adjusted gain; recurrent/joint alternatives are weak or adverse, with no major scalar-tail opportunity | 0–5% for standard identities | 0 now | A changed joint state supports a consistent, useful positive marginal law. A tiny terminal reserve does not justify a larger recurrence by itself. |
| R07 Conditional preintegration / exact line integration | Medium; reusable primitive exists, challenge integration cost not resolved | 10–25% | 15–20 min | A restricted direction/suffix permits cheap inner integration and enough residual variance reduction. L11 blocks an automatic smoothness claim, not the whole route. |
| R08 Non-Gaussian joint states / Gaussian splitting | T160positive QG32improves on Gaussian closure but loses91.5xraw versus incumbent; corrected Gaussian tail does not rescue it | 5–15% for a named distributed-state construction | 0 generic;10–20min on shared quadratic atoms | Fresh distributed quadratic directions and a finite cheap nonlinear response, not merely a larger scalar order or tiny latent rank. |
| R09 Output-aware recombination / kernel compression | Medium-high for basic balance/recombination machinery after T136; no qualified nonlinear residual feature/kernel or solver yet | 10–20% | 5–10 min | A feature explains whole-frame residual error beyond the already cancelled quadratic component and fits the fully charged bank/suffix budget. Generic balancing citations alone no longer change the next action. |
| R10 Tensor-train integration / amortized neural integrators | Low–medium for adjacent tensor environments/recursive chaos after T143; direct network integration feasibility still largely unknown | 10–25% | 10–20 min for a concrete rank question | A cheap relevant tensor environment, low approximation rank, or reusable training is demonstrated. The adjacent literature does not establish a width1024 joint-state representation. |
| R11 Extra radial quadrature for the current homogeneous Gaussian setup | Settled for this exact operation; radius already integrated analytically. This does not close R15's changed approximate propagation | 0–5% | 0 min | The input law, homogeneity or requested observable changes. Reuse the exact identity; distinguish adding quadrature from choosing a different finite closure. |
| R12 Persistent joint-tensor compression | T159trace/Winograd improves officially; T160partial-interface/gate nominee gives8.69%adjusted gain on8reused networks. Paired-state variants fail; harmonic-CP recurrence unbuilt | 0–5% for generic low-rank search | 0 before nominee feedback | Qualify the preserved source; reopen larger compression only with a new state/merge/trace-metric mechanism and actual response evidence. |
| R13 Homogeneous observable state on the positive cone | T148 extends angular moments and identifies the full T(.,.,1) matrix bottleneck; finite closure remains open | 10–25% for a narrowly specified finite closure | 0 now;10–20 min when that question is selected | An affordable response-preserving state or contraction exploits the weighted angular law. Exact law-invariance restrictions do not close useful approximations. |
| R14 Conditional fourth metric / matrix prediction | T160cheap patches weak; corrected3+2cup gains1.44%on pair; exact pair slices too costly. Missing cubic birth derived but standalone response poorly aligned | 10–20% for a named coherent finite update | 0 generic;10–20min on update/cost gap | Complete core/residual/covariance/cubic bookkeeping with an affordable history carrier. The complete method remains unbuilt, not rejected. |
| R15 Fixed-radius representative with angular cumulant closure | SCP-A raw+4.51%, adjusted+8.42%; T155 supports initial radial conversion and locates divergence after nonlinear closure, before old-source confinement | 5–15% for a named mixed-response gap | 0 generic;10–15 min for that gap | Isolate mixed radial third/fourth responses or a different finite closure. No core collapse observed on the completed trace; exact missing term unresolved. |

Status anchors: [T112 reconstruction](../experiments/checkpoint3/t112/REPORT.md),
[T129 reserves](../experiments/theory/t129/RESERVES.md),
[T130 loss](../experiments/submission_policy/t130/REPORT.md),
[T131 inconclusive lead](../experiments/submission_policy/t131/REPORT.md), and
[literature L01–L20](LITERATURE_INDEX.md). R09's particular Hayakawa method was
not found in the inspected T113/T119/T122/T126/T129 records; this is a scoped
search finding, not proof that nobody in the repository ever mentioned it.

## Effort baseline and diminishing returns

The [T128A census](../experiments/protocol/t128a/TASK_AUDIT.csv) remains the
historical timing source. It records 116 started work items and at least 59.24
task-session hours, with incomplete older timing. Its broad approach totals
are 12 sampling tasks / 4.76 hours, 21 structure-and-control tasks / 6.22 hours,
6 moment-closure tasks / 1.43 hours, 27 hybrid-fusion tasks / 19.75 hours,
18 cross-family theory/intake tasks / 23.06 hours, and 32 foundation tasks /
4.03 hours. These are pre-T129 parent-family totals, not times measured on
each narrower row above. Mixed theory time must not be credited to every route.

Later identifiable work: T129 used 209.32 minutes to checkoff, including at
least 181.15 active root research minutes; its agents contributed another
284.91 overlapping minutes. T130 and T131 used 20.08 and 28.89 minutes to
checkoff. T132's own timing and search phases live in its result/search log.
Agent minutes are separate from calendar time. Historical literature-only
minutes are unknown; do not infer them from the duration of a theory task.

There is a **warning of diminishing returns in the recent incremental slate**:
T124's retained official gain was 3.8961%, T127's was 0.4167%, and T128/T130/T131
did not yield another submission. The last of these still had a tiny local
positive mean. These selected, different tasks are not a fitted learning curve
or proof that hybrid estimators are exhausted. They support shortening generic
searches and trying the concrete cheaper comparator before another shape tweak.

For the new literature process, T132 is only the **first observation**. It
found one new execution-ready *lead* (L01, still requiring local checks), one
conditional transfer idea, and one concrete compression literature reserve.
The final breadth pass added background but did not change the recommendation.
That is a reason to stop this search, not an established long-run decline.

At the next relevant task, append one short dated row below. Track elapsed
search minutes, actionable leads, which lead actually reached a bounded test,
and any retained official gain. Leave outcomes pending until they occur. If a
route has two successive searches with no decision-changing lead and no new
reopening trigger, normally halve its next refresh budget or skip it. This is
a planning default for the trial, not a permanent protocol requirement.

| Round | Search effort | Decision-changing yield | Tests / retained official gain attributable to search |
|---|---|---|---|
| T132 → T133 | T132:21.34min search-task elapsed; T133:9.67min to checkoff, separately counted implementation/comparison | L01 reached one unchanged bounded test; conditional calibration transfer and compression remain untested | T133:12 rows, .7299% adverse mean, .4319 support;56.787B FLOPs. Zero retained official gain, no upload. Tested cheap baseline retained. |

For the next recurrence, suggest **20–30 minutes total refresh**, concentrating
on changed public code and the single route selected for that recurrence. A new
domain can justify more; an unchanged topic does not require another full survey.

## T133 update — 2026-09-06

[The first downstream test](../experiments/submission_policy/t133/REPORT.md)
completed in9.67 minutes to checkoff (40 estimated). Fourteen production
predictions used0.613 metered minutes; no new fitting, no
comparison extension, no submission. The unchanged public estimator is .7299%
worse on12 reused development networks, with .4319 bootstrap support. The
uncertainty is wide; neither equality nor private-suite inferiority is established.
Its56.787B actual FLOPs leave163.116B under the discount floor. This supports a
credible cheap starting point, not a claim that its features add independent
signal to ALG031. The original T132 forecasts and source report remain preserved.

**R01's direct unchanged-upload leaf is parked; the wider family is open.**
Reopen on changed source, convincing comparable evidence or a concrete use of
the saved compute. **R02's transfer remains untested**, and is proposed as T134
with one small fixed training fit. Keep the earlier15–30% official-gain planning
range for L132-B; T133 does not warrant raising it. R09's compression reserve
acquires neither positive nor negative implementation evidence from this test.

The trial has produced a new usable baseline in roughly31.01 combined minutes
to the two checkoffs, but no leaderboard gain. This is useful feasibility and
selection feedback, not demonstrated score return. One search/test pair is too
little to estimate a trend; lower R01's next generic search allocation and favor
the concrete transfer or a changed baseline mechanism. Do not repeat a broad
survey simply because the unchanged public candidate did not pass the screen.

T133 final verification/handoff records bring its measured elapsed subtotal to
14.11 minutes (4.44 beyond checkoff); use that fuller value for
future effort planning. The combined31.01-minute figure above is specifically
to the two checkoffs and excludes their later delivery overhead.

## T134 update — 2026-09-06

[T134](../experiments/submission_policy/t134/REPORT.md) used one 32-network
five-coefficient fit, keeping all existing ALG031 coefficients and sampling
unchanged. Training improved 4.3325%; local adjusted mean improved 2.9794% on12
reused development networks (11 wins, bootstrap support 1.0). The one qualified
submission **330097** graded at **1.32636576382e-07**,
**2.6061% below ALG031**. Additional cost is 1.627M FLOPs and the multiplier
remains .1. No feature grid, comparison extension, refit or retry occurred.

**R02's fixed five-column transfer is resolved as an official improvement.**
This supports the complete correction, not the necessity of every feature. It
does not close the wider learned-correction route or identify a best possible
head. R01 remains a cheaper alternative baseline and R09 remains untested.
The earlier T132/T133 forecasts and statements describe their dates; this
addendum supersedes their pending-transfer status.

| Follow-up | Elapsed to checkoff | Downstream return |
|---|---:|---|
| T134 /L132-B | 38.59min, including 14.63min grader wait overlapping record preparation | One accepted grade; retained official improvement 2.6061%;46 production calls, one five-coefficient fit |

The literature-first trial now has two bounded implementation observations,
and **2.6061% retained official improvement** attributable to its selected
transfer. That is actual submission feedback, beyond T133's useful feasibility
result. It is still too little evidence to fit a diminishing-return curve or
make literature-first a permanent requirement. Generic regression searching
remains low-value; reuse the indexed methods when selecting a specific next
algorithm. No automatic next task is authorized by this tracker.

T134 total through final verification/handoff is39.95 minutes, including
1.36 minutes after its checkoff. Use this fuller subtotal for effort planning.

## T135 update — 2026-09-06

One joint 27-column update reusing 32 cached networks gave 2.3234%
training improvement and +3.3367% local adjusted improvement
(12/12 wins; support 1.00000).
Submission **330101** graded at **1.28580467731e-07**, +3.0581% improvement versus ALG036. One accepted submission, no retry. Grader wait 13.00 minutes.
Elapsed 28.09 min to checkoff. [Result](../experiments/submission_policy/t135/REPORT.md).

The fixed one-step joint refit is resolved; the whole correction family remains
open. This supplies one more marginal-return observation, not a fitted saturation
curve. Generic regression searching and further same-feature coefficient tweaks
have low priority now. Reopen with a concrete new signal, a cheaper implementation,
or an identified fit failure that could plausibly matter. The next recommended
investment is focused literature refresh followed by theory on R01's cheap
Gaussian baseline and R09/L132-C output-aware compression. No automatic next task.

T135 total through final verification/handoff: 29.06 minutes.

## T136 update — 2026-09-06/07 UTC

Combined task: **138.79 elapsed / 120.09 useful minutes** to checkoff,
including83 active theory and16.5 literature minutes. Approximate active-theory
allocation:25 minutes to R09 balancing/exact controls,58 to R08 joint cumulants
and their costs; mixed work is assigned once. These are conservative estimates,
not a fine-grained activity log. [Timing](../experiments/theory/t136/TIMING.json).

Two prospective nominees, zero challenge candidate runs and zero new official
gain so far. R08's CSK3-R keeps persistent paired factors and exact repeated
entries with904.626B projected FLOPs; R01/R08's A2LR fallback projects136.853B.
The old K3 full-depth cost failure does not close these changed representations.
The public source has been rechecked and pinned; another broad cumulant survey
has low immediate value. Prefer one bounded implementation decision now.

R09 has improved construction/error theory but no qualified output-sensitive
residual feature. Conditional unbiasedness, capped weights and exact quadratic
balance are insufficient by themselves. Reopen on a useful nonlinear residual
feature plus its charged solver and bank cost. This is incomplete implementation
progress, not proof that network-adaptive compression fails. Keep related R04
controls and conditional-integration reserves separate; they were not tested.

For diminishing returns, T132's literature-led sequence ultimately produced
two official gains through T134/T135, together5.5844% versus ALG031. T136 instead
produced a larger-risk joint-state test and specific compression failure
conditions; its score return is pending. Two different rounds do not establish
a monotone return curve. Source counts are not a substitute for eventual grades.

Next refresh: normally5–10 minutes for changed public code or one diagnosed
gap, not another generic balancing/cumulant survey. A new failure mechanism or
unfamiliar route can justify more. These remain trial planning estimates, with
no permanent mandatory search or validation gate.

## T137 update — joint cumulants reach production

R08 CSK3-R / ALG038 achieves local adjusted ratio0.152798,12/12
wins with no fit, at896.310B actual FLOPs. Submission330141 is
graded with adjusted score1.7369283609807433e-08. RetainALG038-V000.
Elapsed71.12min;45.85min through qualified upload. The initial5-row
diagnostic and repaired native execution failures are disclosed in
[the result](../experiments/submission_policy/t137/REPORT.md).

This materially raises the return from the T136 R08 investment; it is not a
component ablation. Persistent joint cumulants remain an active productive
route. Generic literature search is still low marginal value; the next useful
work is specific compute reduction or the leading omitted correction. A2LR
remains untested and should be re-ranked against the improved joint-state
benchmark. R09 compression remains open, with no new evidence from T137.
No permanent protocol change or automatic second candidate task.

T136 plus T137 used **209.91 elapsed task-minutes (3.50 hours)**,
including literature, theory, implementation, records and grader waiting; the
owner gap between tasks is excluded. This sequence produced the86.49% official
adjusted-score reduction. It is a useful research-round return, not a marginal
causal estimate for each hour or a guarantee for the next recurrence.

## T137A update — explanation of the large gain

The [owner-requested postmortem](../experiments/analysis/t137a/REPORT.md)
reuses the sealed 12-row outputs and official receipts. Raw official MSE
improved 30.17-fold; the effective multiplier rose 4.076-fold, leaving a
7.40-fold adjusted gain. Cost was within 0.92% of forecast; accuracy exceeded
the T136 conditional upside range. Only 1.20% of ALG037's local MSE was a
common within-network offset, while the neuron-specific part fell 96.23%.
These describe the complete estimator; component contributions remain open.

Keep R08 the first route to consider. T017's positive shallow K3 evidence and
old cost obstruction should inform interpretation: the family was not
established ineffective. Test a component only when it changes a concrete
compression or extension decision. Reaching the discount floor at unchanged
accuracy would yield 4.2613e-9 adjusted, but that requires roughly fourfold
less compute and is not a demonstrated compression result. No new candidate,
fit, submission, or standing protocol requirement was introduced by T137A.

## T138 update — cheaper unchanged joint state

ALG038-V001 retains the CSK3-R state and achieves15.5539%
official adjusted improvement with756.892B prediction FLOPs.
The final contractions and single depth4 kernel attempt improve cost without
fitting or state compression. R08 remains productive; its next larger question
is compression or a specifically motivated omitted term, not a broad survey.
[Result](../experiments/submission_policy/t138/REPORT.md).


## T139 update — 2026-09-08

[This recurrence](../experiments/theory/t139/REPORT.md) nominates **C64-E first**
and **Q4D second**, with no production candidate evaluation or official gain yet.
C64-E keeps two recent sources and a rank64 symmetric core, including projected
transport of old E; its complete static forecast is427.998B. Q4D preserves the
coordinate fourth trace and marginal kurtosis at814.932B projected. Comparator
ALG038-V001 remains756.892B and1.46676758754e-8 official adjusted.

T139 used **121.02 elapsed / 120.05 useful minutes**, including **92.37 active theory**, 10.67 literature and 17.01 selection/handoff minutes. Setup (0.97 minutes) is excluded from useful time. [Actual timing](../experiments/theory/t139/TIMING.json).

The research allocation was approximately50 minutes on persistent compression
and old-E transport, and42 on omitted-source/fourth-response questions; these
are overlapping-topic editorial assignments counted once, not measured separate
clocks. Total written-theory time is measured. No fitting or target-directed
parameter search occurred. The fixed tensor-product sketch adapts to a tensor
computed from weights, not to challenge labels.

| Specific leaf | Current outlook / exhaustion estimate | Reopen or next action |
|---|---|---|
| C64-E / R12 plus R08 | Implementation-open; generic Tucker search now medium-high saturation | One bounded integrated test. Repeated compression and modeled-E persistence are the actual unknowns. |
| Q4D / R08 | Defined secondary nominee; no complete-estimator evidence | Meter and score only in a separately authorized task. Correlated off-diagonal fourth trace remains outside its state. |
| Rank256 dense core | This charged realization is cost-rejected, not the Tucker family | Changed core factorization or a materially cheaper construction. More generic low-rank papers alone do not change the count. |
| One-leg and two-leg states | Algebra/geometry established; wider-rank accumulation unresolved | Revisit if C64-E identifies a concrete lost component or construction bottleneck. No automatic rank grid. |
| One-next-trace repair | Low value on the tested residuals: about3–6% metric improvement | A trace-dominated error diagnosis. Do not repeat the same repair merely for extra rigor. |
| Conditional32 shared-mode source / R08 | Closed formula, limited covariance coverage; reserve | Evidence of an important common-mode response or a cheap way to include conditional residual correlations. The one-factor success is not a general accuracy result. |
| Full nonradial fourth-trace matrix | Partial source only; not an implementation-ready full-response nominee | Affordable off-diagonal source/response, or a different explicit approximation with enough upside. |

Recommended next refresh remains **5–10 minutes** for a diagnosed gap, and zero
for an unchanged generic re-survey. The trial has now produced another concrete
implementation decision in10.665 search minutes, but its score return is pending.
T136/T137's large gain and T138's15.55% follow-up establish that joint cumulants
are productive; they do not validate T139's compression or justify extrapolating
a research learning curve. R09's sample compression did not receive new tests
and must not inherit R12's positive geometry or its cost-rejected leaves.

T140 is proposed only. The subjective planning chances of a future retained
win are55% for C64-E and30% for Q4D, with broad ranges in the report. These are
not the roughly90% local support used to decide an actual submission.


## T140 update — 2026-09-08

[C64-E production attempt](../experiments/submission_policy/t140/REPORT.md) completed
in 17.50 elapsed minutes through records, against100–130 estimated. Thirteen
full-size calls total 5.48 metered minutes, overlapping other work. No new
literature/theory recurrence, fitting, agents or submission. The first production
implementation passed all resources:422.773B FLOPs,44.14% below the incumbent.
The 12 paired networks reject its accuracy: raw ratio 8.2575, adjusted ratio 4.6123,
0/12 wins. The earlier 55% planning chance did not turn into a useful submission.

**Exhaustion assessment:** the exact C64-E leaf is closed unchanged; further
network batches or unchanged submissions have negligible expected value here.
The generic Tucker literature search is already near diminishing returns for
this immediate question. The compression family remains materially unexplored:
T140 combines repeated projection with a new persistence rule for modeled E.
Neither contributor is separately measured. Do not transfer this loss to Q4D
or infer that old history is intrinsically incompressible.

Prefer proposed T141, the existing compression-only fallback, before spending
more research time. It reuses working core code and changes the failed joint
design to preserve the incumbent's ephemeral E. Earlier399.471B cost remains
unmetered. Subjective retained-win planning chance 40% (25–55%), 45–75 elapsed
minutes including possible grader wait; no authorization or execution yet.
If it also loses clearly, pause generic rank trials and choose Q4D or a focused
response-preserving representation diagnosis. Reopen this exact C64-E leaf only
for a concrete implementation defect or a materially changed mathematical state.


## T141 update — 2026-09-08

[Compression-only C64](../experiments/submission_policy/t141/REPORT.md) also loses:
394.359B FLOPs (47.90% reduction), raw-MSE ratio7.9846, adjusted ratio4.1602,
0/12 wins. Thirteen production calls pass all resources; small full-rank
trajectories agree with the incumbent within5.36e-7. No upload or fitting.
The task used11.90 elapsed minutes through records, versus45–75 estimated;
5.51 metered prediction minutes overlap other work. Final commit-preparation
timing is retained in the task record.

**Exhaustion assessment:** both exact rank64/recent2 leaves are closed unchanged.
Removing old-E persistence reduces raw MSE only3.31% relative to T140; it is
not sufficient to rescue this compression design. More batches, an unchanged
submission, generic Tucker surveys or an unmotivated rank grid have negligible
expected value for the current leaves. The family is not proved exhausted:
a response-preserving compression mechanism, changed representation, or concrete
implementation defect would be a valid reopening trigger. The original small
geometry/impulse checks did not settle full-width recurrent accuracy.

Prefer proposed T142, the already-derived Q4D fourth-state extension that retains
the incumbent third history. Forecast814.932B remains unmetered and needs about
7.12% raw-MSE improvement. Planning retained-win chance30% (15–45%), unchanged
by these compression tests;45–75 elapsed minutes including a possible grader
wait. Q4D has not run and T142 still requires owner selection. Further generic
literature search has no priority before this direct decision; reopen focused
research when it answers a specific missing-response or cost question.


## T142 update — 2026-09-08

[Q4D](../experiments/submission_policy/t142/REPORT.md) improves raw MSE by8.14%
on all12 reused networks, but the compliant848.844B implementation raises
adjusted score3.02% (3/12 wins, bootstrap support.0019). No upload. Cheaper
812.091–828.297B realizations have recorded residual failures. All13 final-source
full-size calls pass; all18 completed calls, including four earlier resource
failures, are preserved. No fit or equation change after registration.

**Exhaustion assessment:** the current compliant realization is closed for
unchanged submission. Q4D's mathematical direction remains open and now has
positive full-shape accuracy evidence. Holding the final predictions fixed,
approximately812.815B supports a local win at90%; the initial812.091B cost would
give1.44% improvement and.91375 support, but that source is operationally failed.
These conditional calculations do not qualify an earlier source. Further
networks on the current losing implementation add little decision value.

Specific reopening routes include cheaper compliant execution (for example,
reusing a weight operand's decomposition across several products) or a cheaper
completion that preserves the useful fourth information. Neither was executed
or assigned a score claim. The omitted off-diagonal fourth trace and incomplete
persistent third-source response remain research opportunities. More generic
Tucker/compression search is low value after T140/T141.

T142 used36.72 elapsed minutes through records, versus45–75
estimated;13.73 metered prediction minutes overlap useful work. The repair
episode was approximately12 elapsed minutes within its20-active-minute allocation.
No new literature recurrence, agents or official feedback. Final timing is in
the task record. Propose T143: at least120 useful minutes including90 written
theory, with a brief focused literature refresh. Retain Q4D as the inexpensive
fallback while developing a credible larger gain under the standing preference.
T143 is not started.

## T143 update — 2026-09-08/09 UTC

The owner expanded this recurrence to separate120-minute derivation,
60-minute literature and30-minute candidate-selection floors.
T143 used **120.02 derivation, 60.06 literature, and 30.21 candidate-selection minutes**: **210.29 useful minutes** over **250.43 elapsed minutes** through records. Setup and overhead are excluded from the three floors. [Actual timing](../experiments/theory/t143/TIMING.json).

[The result](../experiments/theory/t143/REPORT.md) nominates **H143-JSP** first
(fresh joint-source paths, no extra factor columns,757.14–757.89B static
cost) and **H143-E1** second (one extra uncompressed completion hop,
828.52–831.52B). Both preserve the successful full Gaussian/main third state.
No challenge candidate was run; retained official return is pending, not zero
measured effect. T144 is proposed for one bounded JSP attempt.

The50 new literature entries span ten adjacent areas, with reading depths
recorded. The wider search did not uncover a ready superior external estimator.
It did connect the work to memory projection, response-oriented reduction,
Gaussian residuals and observable kernels. Its useful output includes transfer
limits; paper count is not a measure of decision-changing yield.

The unchanged generic literature now has lower marginal value. Specific
mathematical reserves remain open: a stable coupled completion gauge, mixed
query-preserving compression, and a curvature-weighted triangle correction.
Their [reopening conditions](../experiments/theory/t143/RESERVES.md) prevent
an untested route from being mistaken for an exhausted one. Low-dimensional
conditional integration succeeded as an identity but lost accuracy when its
residual correlation was discarded; simple old-factor loop projection had
poor coverage and high repeated-slice cost. These findings demote precise
spellings, not the encompassing families.

This is one interleaved recurrence, not one new task per subbranch. Category
clocks are measured; per-route minutes are not, and the full duration is not
credited to every route. T139 and its three follow-ups still provide no new
retained official gain; whether the extra T143 research improves return must
be judged after its prospective implementation feedback. No new compulsory
search phase or permanent time quota is introduced.


## T144 — fixed JSP submission feedback

T144 implements one T143 deduction-led nominee without fitting or new columns.
Local adjusted score improves 21.45% on all 12 reused networks,
with 0.0544% extra cost. The first two layers remain exact; the growing later
correction aligns with the incumbent residual on the saved panel. Official
submission 330392 returns 1.18330815718e-08, a
19.33% gain versus ALG038-V001. Retain ALG041-V000.
[Report](../experiments/submission_policy/t144/REPORT.md).

This is one algorithm task, 45.27 elapsed minutes including
27.11 minutes to observed grading; 15 local calls
total 10.92 metered minutes. Durations overlap. No
new literature search, fitting, agents, repairs or extra comparison. This gives
T143 a measured submission return; it does not credit all preceding research
time to JSP or show which source term caused the gain.

R08's fixed JSP leaf now has actual feedback. More generic literature on these
same paths has low immediate value; other response sectors and memory remain
open. T145: prospectively register E1-on-JSP as a new combined candidate, then one
bounded production/submission attempt against ALG041-V000. Keep JSP fresh source and
full main history; add exactly one completion hop from H143-E1 with its prescribed
repeated-entry repair. This is an explicit new parent/formula decision, not execution of
unchanged H143-E1 against ALG038. No age/rank/coefficient sweep. Early full-size meter,
usual 12 paired reused networks, approximately 90% support; 60 active engineering
minutes, 30-minute reassessment; 35–75 elapsed estimate. Actual added cost must earn its
raw-error reduction; roughly 9% projected hurdle. No work on that proposal has started.
Original E1 and Q4D
forecasts were against ALG038, and no benefit transfer to JSP is assumed.


## T145 — one extra completion hop on JSP closes unchanged

One fixed combination was implemented and tested, with no fitting. Raw MSE
worsens 2.71%, adjusted score 12.53%, all 12 losses
on both metrics. Cost rises 9.56%. A bundled-transform repair resolves
residual overhead; the final 13 full-size calls pass. No upload or comparison
extension. Retain JSP's official 19.33% gain from T144.
[Result](../experiments/submission_policy/t145/REPORT.md).

The extra correction's squared magnitude supplies most of the raw loss and
its aggregate error cross term is adverse too. This describes the same saved
panel, not a new fit or an attribution separating retention from coupled JSP
feedback. The retained state is a modeled closure, so transporting more of it
does not establish more faithful true joint moments. Close this fixed spelling;
original E1 on ALG038 is untested and demoted against JSP. No general memory
impossibility or automatic longer-memory ladder follows.

This is one additional algorithm task, 26.31 elapsed minutes through
records, with no official wait. All 15 full-size calls total
11.24 metered minutes, overlapping other
work; only 12 networks enter the score. Reuse the bundled-transform engineering
where relevant. No new search was performed, so literature saturation is not
changed by this test. T143's 19.33% retained official gain survives its second
nominee's negative feedback. Do not assign that full research duration to each
leaf or treat the second nominee as an independent literature recurrence.

T146 is proposed for better justified joint completion/gauge or coherent omitted
source response, with response-preserving compression as a larger-upside reserve.
Reuse T143 literature; search named gaps instead of another generic survey.
Proposed floors 120 minutes derivation, 30 focused literature, 30 selection
(180 useful; 180–220 elapsed estimate), with productive continuation allowed.
No new permanent quota or automatic task execution. Q4D's raw gain remains
against ALG038; a transfer to JSP has not been measured.

## T146 — a changed public source and a conditional homogeneous-state route

The [T146 selection](../experiments/theory/t146/CANDIDATE_SELECTION.md) recommends
one nominee: unchanged public V29, H146-PUB29. The author's reported5.40e-9
adjusted score would improve the retained JSP score by about54.4%; this is
external evidence, not a local reproduction or a new retained official result.
The source was published after the previous broad review. This is R01's
explicit changed-source reopening condition being met, rather than evidence
that repeatedly searching unchanged material was worthwhile all along.

The new evidence also limits what should be called exhausted. Our rank64
compression failures do not cover its age-dependent shared bases at ranks384
and224. The public author's own negative catalogue is useful for concrete
spellings and costs; it does not prove a universal raw-error floor or identify
the algorithms used by leaderboard leaders.

T146's own work derives an O(n²) gated response metric, a finite connected
fourth-source projection program, and a homogeneous reduction of a modeled
fourth core into existing second/third responses plus a residual paired core.
That residual has an affordable fourth-to-third source term in the JSP factor.
The strongest own reserve, HGC, has a static728–731B cost estimate versus
JSP's757.304B, conditional on adopting the average fourth metric cI. Its actual
resource use and accuracy remain untested; the public fitted table's transfer
to the new trajectory is also uncertain.

Two negative findings narrow future work. Exactly preserving the immediate
mixed query did not preserve later generated histories; additional solver
accuracy did not repair the failure. An exact homogeneous observable
equivalence also did not order finite-moment closure errors: generated
examples include genuine reversals. The positive-cone weighted-law state is
therefore a separate, open R13 reserve with an explicit finite-state/cost gap.

One previously pessimistic assessment was revised within the recurrence.
Mixed trace-probe noise is4.80–5.75% relative to the sum of two source sectors
in two generated geometries, despite large relative error against the small
signed mixed term alone. That restores a conditional projection reserve; it
does not qualify its missing sectors or total implementation cost.

The round adds16 source entries and18 generated-check records. Paper and
check counts are not independent opportunities or leaderboard evidence.
Category clocks are measured; per-route clocks are not. Count the round once
as cross-family research, with no agent minutes, fitting, challenge runs or
uploads. Its actual return remains pending the proposed bounded reproduction.
The next useful action is implementation feedback, not another generic survey
or an automatic memory/rank ladder. [Reserves and reopening conditions](../experiments/theory/t146/RESERVES.md).

T146 timing: **120.11 derivation,30.24 literature,30.14 selection minutes**;
**180.49 useful minutes**, **219.87 elapsed minutes through records**.
[Exclusive timing](../experiments/theory/t146/TIMING.json). Per-route and
per-source stopwatches were not recorded.


## T147 — unchanged public V29 independently reproduced

One algorithm task adopts 504aldo's unchanged MIT source; no local fit or
algorithm adaptation. Official submission 330597 scores 5.41905133451e-09,
54.20% better than JSP. Local adjusted gain
54.04% on 12/12 reused networks. The public design
brings source feedback, structured fourth regeneration, age-dependent shared
bases and efficient arithmetic together; this task cannot attribute the gain
to an isolated component. [Report](../experiments/submission_policy/t147/REPORT.md).

Elapsed 64.35 minutes, including 42.93
minutes from acceptance to observed grade. Metered local prediction time
10.46 minutes overlaps other work. The original
loader memory failure is retained; corrected input loading passes with the
unchanged estimator. A brief owner-requested public-availability refresh during grading found no stronger released Phase2 implementation; no new saturation estimate or formal recurrence.

Focused literature/theory recurrence on the stronger V29 baseline. First identify which
joint-source and fourth-response terms its published equations already contain; then
derive one coherent omitted response without double counting. Prioritize a cheap
paired-fourth or conditional-source correction native to V29, keeping
response-equivalent homogeneous state as a larger-upside reserve. Re-rank HGC using the
actual cost hurdle; do not automatically port JSP, E1 or Q4D or sweep existing
ranks/coefficients. Proposed floors: 120 minutes written derivation, 30 focused adjacent
literature, 30 candidate selection; estimate 180–220 elapsed minutes, with productive
continuation allowed. A cheap candidate may be saved while a credible larger-gain thread
is developed. No new task, candidate execution or agents start automatically.

T148 is proposed only. HGC remains untested, and its cost/accuracy hurdle is
recomputed against this result in [the recommendation](../experiments/submission_policy/t147/NEXT_PROPOSAL.json).
JSP/E1/Q4D gains do not automatically transfer to the stronger public baseline.

## T148 — conditional fourth metric, with larger native reserves

[The completed recurrence](../experiments/theory/t148/REPORT.md) nominates
CMF2 first and FAR-CT as an optional cheap fallback. Both are untested on the
challenge. CMF2 has an analytic norm-conditioned coefficient and a two-column
source realization; static extra cost2–5B FLOPs. The public exact-metric
comment lowers expectations of a large isolated gain. The far-CT source is
not the same intervention as the public B2 loss.

Native HGC's fifth/sixth source vertices now reuse existing factors. This
removes a specific arithmetic obstacle but leaves a finite update/calibration
choice; no all-orders proof is required before testing a named approximation.
Joint core conditioning, low-degree core queries and a whole-matrix spectral
predictor were developed after the cheap leads appeared. Their
[reopening steps](../experiments/theory/t148/RESERVES.md) remain explicit.
No whole family was closed. The naive dense spectral realization is poor
value; a cheap source representation can reopen it.

Timing:121.19 derivation,30.10 literature,30.14 selection minutes;
181.43 useful minutes. Crash/recovery and records are excluded, with exact
elapsed accounting in [TIMING.json](../experiments/theory/t148/TIMING.json).
This is one interleaved task, not one task or the full duration per route.
No agents, fitting, candidate runs, targets or uploads. The15 newly indexed
unique sources plus an L38 revisit do not constitute16 new methods. The
round's retained official return is pending, not yet measured.

More unchanged generic literature has low immediate value. R08's useful next
question is the bounded CMF2 score test; R13 still needs an affordable finite
angular closure. A narrow R14 entry below separates conditional matrix
prediction from the broader joint-state family without adding a new process.
T149 is proposed only; FAR-CT is not an automatic second test.


## T150 — develop the larger change; distinguish a settled identity from an untested closure

The owner left T149 **not tested and deferred** after identifying drift toward
likely small gains. T150 completed60.10 active derivation and4.48 selection
minutes; no new external search. Two finite algorithms are now specified:
SCP-A (preferred) and HGC6-A (ambitious alternative). Both remain unimplemented
and untested. [Result](../experiments/theory/t150/REPORT.md),
[complete status/forecast inventory](../experiments/theory/t150/UNTESTED_INVENTORY.md).

R15 uses the known Gaussian-radius identity to choose a different law for
approximate internal propagation. It does not spend more compute on an already
integrated input radius. R11's narrow closure therefore never implied that
this approach was exhausted. The first-layer common-radius covariance gives
a mechanism; the changed closure, compression and public calibration may still
lose. Some mixed responses are deliberately omitted, including terms first
order in radial coefficients. More completeness work is not a prerequisite.

R08's generic HGC reserve now has an explicit finite update, source and anchor.
An implementation result is more valuable than another generic proof search.
R13 positive-cone closure and R14 spectral/joint-core extensions remain open
at named state/cost gaps. These are not failed algorithms. Older fixed forms
must be compared with today's V29 incumbent before reusing their forecasts.

No new score evidence changes route saturation. The gain-per-hour midpoint is
a judgment aid; it does not veto the larger potential payoff and information
value of SCP-A. T151 is proposed only, and no cheap fallback is automatic.


## T151 — actual SCP-A feedback, preserve the ambitious alternative

H150-SCP-A / ALG044-V000 loses raw and adjusted score on all12 development rows.
The loss is modest and consistent (4.51% raw,8.42% adjusted), with resource and
implementation checks passing. No unchanged retry, extra cohort or cost sweep.
This supplies actual evidence against the fixed R15 leaf, not a cause-isolating
result or a family-wide impossibility. [Report](../experiments/submission_policy/t151/REPORT.md).

H150-HGC6-A remains untested and is proposed as T152 on V29. It has a different
layerwise conversion and finite fifth/sixth program, though changed-calibration
risk overlaps. Reuse existing literature and native contractions; no generic
search restart is needed to try this specified reserve. T149/CMF2 remains not
tested and deferred. [Current candidate status](../experiments/submission_policy/t151/CANDIDATE_STATUS.md).


## T152 — the finite HGC6 closure loses; re-rank beyond this pair

H150-HGC6-A / ALG045-V000 has8.438x raw and8.564x adjusted error on the12
reused development rows,0/12 wins. Its8.37B extra FLOPs and passing resource
checks resolve the implementation-cost question. They do not rescue accuracy.
The saved trajectory difference accumulates through layers; no cause was
isolated among finite-response truncation, state/core convention, calibration
and compression. [Report](../experiments/submission_policy/t152/REPORT.md).

Both complete T150 nominees now have actual local losses and zero retained
official gain. No more unchanged tests are useful. This lowers the immediate
value of similar finite homogeneous conversions, without settling every
angular closure. Generic identity searches should get no new budget; reopen
on a concrete new approximation argument. This is two selected leaves, not
a statistical learning curve or proof of family exhaustion.

Proposed T153 gives more attention to R14's joint core/metric convention and
R12's affordable future-response queries, with a bounded R13 or conditional
Hermite alternative. These remain incomplete routes, not ready algorithms.
No new search or recurrence ran during T152. T149/CMF2 remains not tested and
deferred; FAR-CT remains untested. No cheap fallback begins automatically.
[Current candidate status](../experiments/submission_policy/t152/CANDIDATE_STATUS.md),
[proposal](../experiments/submission_policy/t152/NEXT_PROPOSAL.json),
[actual task timing](../experiments/submission_policy/t152/TIMING.json).


## T149 executed after T152 — CMF2 supplies modest negative feedback

The owner explicitly selected the formerly deferred CMF2 candidate.
ALG046-V000 passes all15 full-shape calls and settled byte replay; its
4.0888B extra FLOPs fall within the2–5B theory estimate. The12-row adjusted
mean loses1.074%,6/12 wins, support.09155. Raw mean loses0.347%, despite8/12
raw wins. No extension, fit, package or upload. [Report](../experiments/submission_policy/t149/REPORT.md).

This closes the fixed CMF2 spelling, not every conditional matrix predictor.
The modest loss does not identify which metric/core/source component mattered.
It weakens the case for simply adding more metric fidelity without a new
information argument. Joint-core conventions and future nonlinear queries
remain named gaps; their cost and impact must be addressed before nomination.
The public exact-metric comment already tempered this candidate's upside.

T153 remains a proposal, updated to re-rank those gaps using the three recent
implementation outcomes. FAR-CT stays untested and requires a separate owner
choice. T149 is now tested and complete; earlier deferral/untested labels in
historical snapshots are superseded by this dated result. No new literature
or theory recurrence occurred during this implementation task.
[Current candidate status](../experiments/submission_policy/t149/CANDIDATE_STATUS.md),
[actual task timing](../experiments/submission_policy/t149/TIMING.json).


## T154/T155 — final preserved test and targeted failure diagnosis

FAR-CT is now tested: raw+0.6904%, adjusted+0.7076%,3/12 wins; no upload.
Its correction has almost no useful projection onto parent error, so a
standalone coefficient sweep has very low apparent value. The specific leaf
is closed, without claiming all coupled CT/feedback approaches are exhausted.

The four candidates lost for different reasons. HGC has a demonstrated
calibration-floor/state interaction and a partial repair. CMF's metric proxy
works on actual states, but improving it is not sufficient for final score.
SCP's initial radial law conversion agrees with parent physical moments; its
later nonlinear closure is the open error source. FAR/SCP precise omitted-term
explanations remain hypotheses. See [T155 diagnosis](../experiments/diagnosis/t155/REPORT.md).

A better local tensor is not a reliable score surrogate. The next proposed
T153 should focus on joint core/future-response information and a compatible
state convention, with a distinct conditional/observable-state alternative
when more promising. Keep the HGC repair lead, but do not let its readiness
crowd out larger opportunities. This is a research-status update, not a new
universal testing protocol, search quota or confidence gate.

T154 is one implementation task; T155 is one diagnosis spanning several
routes, not an additional recurrence credited independently to each route.
[Implementation timing](../experiments/submission_policy/t154/TIMING.json),
[diagnosis timing](../experiments/diagnosis/t155/TIMING.json). Fourteen completed
diagnostic calls and three framework exceptions; no fitting, agents or new
literature search. Two counterfactual/trace analyses have one-network limits.
The larger family forecasts remain uncertain; only the fixed tested leaves
are closed by these scores.

## T153 update —2026-09-12: interleaved feedback changes the compression route

[Result](../experiments/theory/t153/REPORT.md):249.30 active research minutes,
including121.44 derivation,30.36 literature,67.46 empirical work and30.04
selection.28 numbered probes include30 completed full-size calls on two
repeatedly exposed networks. Their13.25 summed metered prediction minutes
overlap other work. No new fit, agent or submission; no official gain yet.
Per-route stopwatches were not recorded, so do not credit the whole round to
each row. Probe counts are not wallclock or independent success trials.

| Route | Updated implementation evidence | Marginal next action |
|---|---|---|
| R12 Persistent joint-tensor compression | T159trace/Winograd improves officially; T160partial-interface/gate nominee gives8.69%adjusted gain on8reused networks. Paired-state variants fail; harmonic-CP recurrence unbuilt | 0–5% for generic low-rank search | 0 before nominee feedback | Qualify the preserved source; reopen larger compression only with a new state/merge/trace-metric mechanism and actual response evidence. |
| R14 Conditional fourth metric / matrix prediction | T160cheap patches weak; corrected3+2cup gains1.44%on pair; exact pair slices too costly. Missing cubic birth derived but standalone response poorly aligned | 10–20% for a named coherent finite update | 0 generic;10–20min on update/cost gap | Complete core/residual/covariance/cubic bookkeeping with an affordable history carrier. The complete method remains unbuilt, not rejected. |
| R08 Non-Gaussian joint states / Gaussian splitting | T160positive QG32improves on Gaussian closure but loses91.5xraw versus incumbent; corrected Gaussian tail does not rescue it | 5–15% for a named distributed-state construction | 0 generic;10–20min on shared quadratic atoms | Fresh distributed quadratic directions and a finite cheap nonlinear response, not merely a larger scalar order or tiny latent rank. |
| R13 observable law / conditional state | Lagged radial and simple gradient closure do not supply the missing angular/mixed information. Exact positive-cone law and conditional primitives remain. | Preserve as larger-departure reserves with explicit finite closure/cost gaps; no universal failure claim. |
| R02 trajectory-matched learned correction | No new fit here. Public CORR_BETA is off and was trained on an earlier trajectory. | A small fresh current-trajectory head is a cheap reserve, not the primary recommendation or a new fit authorization. |

The current next30-minute search assessment for unchanged R12/R14 basics is
0–10%; spend0 now unless implementation exposes a named gap. For the specific
R08 transformed-state or R13 finite-closure question, retain roughly10–20%
subjective chance of a decision-changing targeted search, with10–20 minutes
only when that question is selected. These are search-value judgments, distinct
from the nominee's15–30% subjective chance of a retained official win.

The round shows diminishing returns for the nearby trace/core and simple
moment-preservation spellings, but it also produces a reopening result for
native future-response compression. It is premature to label the entire
analytic family exhausted or fit a learning curve from these adaptive probes.
The next actual candidate score, rather than the number of papers/proofs, will
measure whether this lead paid off. [Forecasts and untested inventory](../experiments/theory/t153/CANDIDATE_SELECTION.md).


## T157 update —2026-09-13: fixed NFC128 closes as a local loss

R12's H153-NFC128 / ALG048-V000 is now **tested**, with two exploratory
full-size calls. Raw+36.65%, adjusted+25.47%,0/2 wins; steady511.508B,8.41%
cheaper than the matched parent. Resources, generated projection/source
algebra and original generic fallback checks pass. No concrete code repair,
fit, parameter ladder, archive or upload. [Attempt](../experiments/submission_policy/t157/REPORT.md),
[actual measured timing](../experiments/submission_policy/t157/TIMING.json).
This is one implementation task, not an additional theory recurrence.

The prior500–530B cost estimate was accurate. The15–30% research-stage chance
of a retained win did not realize. The exact unchanged candidate has very low
remaining submission value after two large consistent losses. That does not
make the entire native compression family exhausted: the spectral saved-state
signal and the cheap combined sketch/range/feedback implementation differ in
several unisolated ways. No probability of a successful repair is established.

Avoid another unmotivated rank, ridge or seed trial. A single cheap saved-state
diagnostic could justify a named repair; otherwise the better research use is
one of the still-incomplete R08/R13 compatible-state alternatives. The
current-rank coupled metric and current-trajectory learned head remain untested
cheap reserves. No new fitting or recurrence is authorized by this update.
The T153 dated route table and forecasts remain historical evidence.


## T158 update —2026-09-13: broader pilots produce a stronger efficiency nominee

240.10 active research minutes (92.34 derivation,82.78
empirical,34.69 literature,30.29 selection).46 numbered probes,
91 full-size calls on8 reused networks,21 literature entries;52.34 summed
prediction minutes overlap research. No per-route clocks, agents or uploads.
One primary five-feature fit plus six diagnostic LOO fits; nominee has no new fit.
[Full route analysis and search-value revisions](../experiments/theory/t158/ROUTE_UPDATE.md).

Explicit lost-trace compensation plus classical Winograd/shared-arena arithmetic
lowers adjusted mean7.45%,8/8 wins, with4.65% higher raw error. This integrated
nominee has85–95% subjective retained-win probability,4–10% conditional gain;
its official return remains pending T159. Reuse the eight-network evidence.

More exact NFC, recurrent/joint NIG, transported cups and fourth-star response
have negative or weak feedback. Full-rank trace is not an impossibility result:
P43–P46 find a corrected low-rank fourth-chain source whose remaining gaps are
trace construction and full-state feedback. Compatible conditional laws remain
open. Do not count these as completed failed algorithms or inflate their priors.
Later kernel refinements have diminishing marginal return; no new sweep or full
screen is needed before the proposed attempt. The owner's broader empirical
allocation was round-specific and does not impose a new quota.
[Report](../experiments/theory/t158/REPORT.md),
[status/forecast inventory](../experiments/theory/t158/CANDIDATE_SELECTION.md),
[timing](../experiments/theory/t158/TIMING.json).


## T159 — official attempt for T158 trace/Winograd nominee

Official submission 330887: adjusted 5.01785974707e-09, 7.40% lower than ALG043-V000. Retain ALG049-V000. This is one implementation/qualification task,
not another recurrence. Reuse 8-network research evidence; 5 actual archived
full-size checks, no new comparison, fit, agents or blind access. Source
changes only encode the tested configuration. 53.45 elapsed minutes;
external waiting and overlapping prediction time are in the timing record.
The larger fourth-chain/conditional-state reserves are still unbuilt. T160 is
proposed only. [Result](../experiments/submission_policy/t159/REPORT.md),
[timing](../experiments/submission_policy/t159/TIMING.json).

## T160 update —2026-09-20: another efficiency nominee, larger gaps narrowed

240.22active minutes: 101.37derivation,
93.70empirical,31.97literature,
13.19selection.97completed full-size calls sum59.75prediction
minutes and49.372Tmetered FLOPs, overlapping research. No per-route time clock,
agents, new target coefficient fit or upload. Offline tensor fits and adaptive
threshold choices are disclosed. T161is proposed, not authorized/started.

[Report](../experiments/theory/t160/REPORT.md),
[route-specific update](../experiments/theory/t160/ROUTE_UPDATE.md),
[forecasts/status inventory](../experiments/theory/t160/CANDIDATE_SELECTION.md),
[repeatable continuation](../experiments/theory/t160/CONTINUATION.md),
[timing](../experiments/theory/t160/TIMING.json).


## T161 — official attempt for T160 interface/gate nominee

Official submission 331607: adjusted 4.54434242306e-09, 9.44% lower than ALG049-V000. Retain ALG050-V000. Exact T160source, reused8-network evidence,
5actual archive calls and no new fit/screen. 40.27session minutes;
external waiting and overlapping prediction time are separate in the timing
record. This is our algorithmic/implementation adaptation of publicV29 via
ALG049. Larger coupled states remain unbuilt; no family-exhaustion claim.
T162proposed only. [Result](../experiments/submission_policy/t161/REPORT.md),
[timing](../experiments/submission_policy/t161/TIMING.json).


## E158 / T162 completion — no nominee

240.00 active research minutes; 77.94 derivation,
117.69 empirical,31.39 literature,
12.98 selection. Interrupted gaps excluded.37 completed
full-size calls,19.744T metered FLOPs;57 generated recurrences. No upload,
agents or new challenge-label fit. ALG050/submission331607 unchanged.
P19six-network adjusted+0.96%is parked. Persistent fourth state gives a42.2%
generated256raw gain;384full-state result uncertain, compact inner state loses.
Half-response diagnostics justify a controlled coherent residual, not a
submission forecast. T163proposed only.
[Report](../experiments/theory/t162/REPORT.md), [route update](../experiments/theory/t162/ROUTE_UPDATE.md), [continuation](../experiments/theory/t162/CONTINUATION.md).

## T163 update — 2026-09-23: nominate P67; distinguish capacity from compression

240.18active minutes,119.71written derivation. Frozen marginal-and-pair learned
responseP67 improves12-network exposed-development adjusted score5.12%,12/12
wins;32-network CV raw gain3.89%, two actual compact calls verify0.07% added
FLOPs. Subjective90–95% official-win forecast with2–6% conditional gain.
Our learned adaptation of ALG050/public cumulant method. P41is a weaker reserve.
No upload, agents or blind access; proposedT164 only.

The larger route was pursued through the floor. Full fourth state at384 gives
35%raw gain, but shared128loses39.6% versus the publicaug3 control. Main-third
covariance-only bases fail; own-tensor bases and response queries work better.
Final jointP79retains13.4%raw gain at256 versus factoredaug3,7.2% versus denseaug3.
Neither capacity comparator is ALG050. Mixed loops are essential; complete
source construction and width transfer are the remaining obstacles. Forecast
15–30%official win in8–16 further hours,10–30% conditional gain.

Scoped saturation (chance nearby2–4h variants produce no useful new lead):
endpoint/covariance-square85–95%; more frozen-residual scalar/ridge tuning80–95%;
current shared fourth metric75–90%; source-aware fourth35–60%; own-tensor
main-third basis40–65%; new information for learned residual40–65%.
These are subjective local forecasts, not field-wide exhaustion claims.
Coordinatewise Stein's conditional-zero-mean restriction is an explicit
obstruction; general function-level integration remains low-information.

148completed full-shape calls/68.820Tmetered FLOPs;41generated recurrences,
40unique hashes. No precise route-hour clock; category and machine timings
remain separate. [Report](../experiments/theory/t163/REPORT.md),
[complete scoped saturation table](../experiments/theory/t163/ROUTE_UPDATE.md),
[selection](../experiments/theory/t163/CANDIDATE_SELECTION.md),
[runnable continuation](../experiments/theory/t163/CONTINUATION.md).


## T164 — official attempt for T163 learned residual

Official submission 332018: adjusted 4.36851423131e-09, 3.87% lower than ALG050-V000. Retain ALG051-V000. Exact P67source, reused12-network development
evidence,5actual archive calls; no new fit/cohort. 36.83session minutes,
with overlapping prediction and external wait milestones recorded separately.
Our supervised learned adaptation of ALG050/publicV29. Larger fourth-state
construction and transfer remain unresolved; no field-exhaustion claim.
T165proposed only. [Result](../experiments/submission_policy/t164/REPORT.md),
[timing](../experiments/submission_policy/t164/TIMING.json).

## T165 — 2026-09-27: capacity persists; current compression returns diminish

241.72 active minutes,146.05 written mathematics; no nominee. Generated
third/fourth endpoint mixtures reduce raw error51–68%, but the affordable
representation is still missing. Exact-young256 capacity improves56.8%; residual
thirdP47 retains46.6% mixture gain. Mixed-birth omission, quarter sources,
squared-third additions and coupled-half feedback lose. The sampled cubic
compressor cuts its component bill40%, yet15steps alone exceed the whole parent
and raw error rises44%. New neighbor/cycle/trace features lose16F matched CV.

Increase local saturation for shared fourth bases/refits to90–97%, generic
paired cubic compression80–95%, and source-aware residual60–80%. These are
subjective chances another2–4h of nearby variants yields no useful lead,
not family-wide impossibility. A genuinely different compatible conditional
state remains lower-information,25–55% saturation. The small unchanged-head
training reserve predicts~0.9%gain by extrapolation only; no64F run exists.

32full-size feature calls/14.504T FLOPs and38generated trajectory records;
all jobs finished. No upload/agents/blind. ALG051 retained. Broader T166proposed
only; no permanent protocol change. [Report](../experiments/theory/t165/REPORT.md),
[scoped route assessment](../experiments/theory/t165/ROUTE_UPDATE.md),
[untested algorithms/forecasts](../experiments/theory/t165/CANDIDATE_SELECTION.md).

## T166 update — 2026-09-27

One practical nominee: intermediate-supervised nonlinear source, prepared P45.
Adaptive32F whole-network CV raw-2.79%,27/32 wins; full-size overhead0.00497%.
Shipped full32 asset still needs the small paired comparison/qualification.
Forecast80–90% official win,1–4% conditional adjusted reduction; T167 proposed only.

Larger proper-dual late fourth-state route stays open. Whole-third96/128
compression failed, but compression only inside the fourth-birth query retains
41.4%/39.6% generated raw gains at256/384. Complete native cost is unresolved;
P52 records exact native-history query identities. Forecast15–25% official win
within8–16 further hours,5–20% conditional adjusted reduction; high end requires
substantial further cost progress. Avoid treating component bills as full cost.

Nearby stochastic32-source banks, selected-coordinate96/32 reconstruction,
finite inverse-radius formulas and whole-third repeated-repair variants are
closed in their tested forms. Additional informative supervised state remains
open; extra histories and terminal-only NN fitting did not help. Late source
label noise is small, so more precise labels alone is a weak repair hypothesis.
[Detailed status/probabilities](../experiments/theory/t166/CANDIDATE_SELECTION.md),
[report](../experiments/theory/t166/REPORT.md).

## T167 official update — 2026-09-27

The exact T166 P45 intermediate-supervised mean source is now **ALG052-V000**,
submission **332641**, official adjusted **4.285182274373245e-9**: **1.9076%**
better than ALG051. The fixed 24-network development comparison gave 1.8772%
adjusted improvement, 17/24 wins, and .99930 bootstrap support after one
predeclared extension. Both looks and prior exposure are retained; no refit.
[Submission report](../experiments/submission_policy/t167/REPORT.md).

This confirms one useful learned-source adaptation; it does not establish that
a nearby neural sweep is the best next use of time. The T166 source-only third
compression route still offers materially larger generated fourth-state gains,
but affordable complete construction remains unresolved. Proposed T168 targets
that cost gap and alternative new state information with a four-hour research
floor. This is a proposal, not authorization or a new permanent protocol.

## T169 update — 2026-10-09: constructor completed, native transfer rejected

240.04active research minutes. Complete P09 high trajectory128.025B; actual
rich readout2.156xraw/2.869xadjusted on exposedF0/499. Actual moment estimates
confirm lost broad fourth information; trace rescue restores most of it but
F0rawratio1.01209(and1.00800withGaussianmean/Cresponse) gives no competitive gain.
Small generated success includes error cancellation; NN overlap is not the
main native failure. Simple damping or combinations of retained directions
cannot repay the measured premium on the diagnostic cases.

Nearby unchanged-P09 engineering/damping/rank changes have low remaining value.
Proper feedback is unbuilt, including potentially important first-order
higher-state loops: subjective3–8% official-win forecast for the straight port,
5–15% for trace-protected feedback, conditional gains2–10%/2–12%. These are
planning priors, not calibrated probabilities or impossibility claims.
A genuinely different cheaper informative state, useful new learned input or
conditional law remains open. Keep the cheap extra-training reserve but the
standing larger-upside preference applies. No new protocol gate or automatic
T170 start. [Detailed forecasts/reopening conditions](../experiments/theory/t169/CANDIDATE_SELECTION.md),
[report](../experiments/theory/t169/REPORT.md).

## T170 update — 2026-10-11: physical covariance lead; compression diagnosed

A96coefficient analytic covariance-defect dictionary reaches .956049 reused32F
response CV; the fixed fold0 native source reaches .969975adjusted on8networks.
P49all32asset nominated, unexecuted/unqualified; subjective80–90%official win,
1–4%conditional gain. No upload. Mixed-cumulant covariance retains useful nearby
territory, but more endpoint neural capacity and two new memory inputs lost.

Exact trace/diagonal and mean-axis repairs do not rescue512source compression.
Variance plus cubic perturbations dominate its terminal loss; a covariance-only
oracle component removal still loses1.11949xadjusted. Single-source retained-span
reweighting, immediate-mean ranking and cheap higher-order scalar observers now
have strong diminishing returns. Pair-conditioned covariance, joint across-birth
compression and affordable matrix observations remain untested, with specific
capacity/cost questions. L7/min8 is a small untested engineering reserve.

[Scoped exhaustion probabilities and reopening conditions](../experiments/theory/t170/CANDIDATE_SELECTION.md),
[report](../experiments/theory/t170/REPORT.md),
[dominant-route time](../experiments/theory/t170/ROUTE_TIME_SUMMARY.json).
No new permanent protocol requirement or automatic T171 start.

## T171 submission update — 2026-10-11

Official submission 335391: adjusted 4.15561726455e-09, 3.02% lower than ALG052-V000. Retain ALG053-V000. The exact T170 P49 all32 fitted covariance
asset gave2.85% lower local adjusted error,
11/12 wins and1.00000 bootstrap
support on the fixed exposed development panel. Archive resource/replay checks
pass; no extension, refit or algorithm repair. Matching parent calls were reused.
[Official and local evidence](../experiments/submission_policy/t171/REPORT.md).

This tests the selected complete covariance variant; it does not isolate the
contributions of individual analytic fields. The larger pair-conditioned and
joint covariance/third-moment compression ideas remain untested. No new family
exhaustion claim or automatic nearby fitting sweep follows. T172 is proposed
only: Broader empirical recurrence on covariance structure and information-preserving compression.

## T172 update — 2026-10-17: cheaper engine and three official improvements

The credited public LordProcciuto engine supplied the largest cost reduction.
Our existing covariance correction transferred after exact kernel regrouping;
ALG054 graded at3.03329104712e-9. A newly fitted trace-informed mean source
then produced ALG055 at2.98282232784e-9,28.22% below the pre-task incumbent.
A fixed equal average of that source and the64-network contextual source
then produced ALG058-V001 /336809 at2.97110640613e-9: another0.3928%,
and28.50% below the starting score. These are official results, not extrapolated research scores.

The fuller fourth-core route remains scientifically open. Scale extraction,
collapsed third births, implicit tensor readers and a narrow-sketch producer
retain useful raw accuracy in two-network research prototypes. A complete
native implementation has not established an adjusted-score gain. The late
P80 kernel measurement projects roughly51% extra compute for a literal rank32
implementation against15% raw gain; pruning and structural reuse would need
to change that tradeoff substantially. This is a scoped cost projection, not
a family lower bound. Its key
remaining question is coupled trajectory accuracy per billed operation, not
another proof of the small algebraic identities. Rank8/16 and scalar-only
substitutes lose important information; diagonal-only transport loses relevant
off-diagonal covariance. Do not infer family exhaustion from those versions.

Nearby history-rank/age reallocations and unrestricted covariance refits lost
in their tested forms. A retained-basis repair made the late fourth-query
readout numerically sensible but did not make its learned prediction better.
The first full-inverse experiment had incorrectly treated masked slices as a
complete basis and is not clean evidence against full-information queries.

Richer learned context has diminishing returns on the current small training
set: original32-network context/graph models lost their CV advantage to the
simpler trace model on32 additional F networks. Expanded64-network fits and
native comparisons are documented in the task report. The half-physical
ALG056 variant failed its larger comparison and was not uploaded. These are
scoped empirical results, not calibrated probabilities for all learned methods.

[Report](../experiments/theory/t172/REPORT.md),
[derivations](../experiments/theory/t172/SCRATCHPAD.md),
[evidence inventory](../experiments/theory/t172/EVIDENCE_INVENTORY.json).
No automatic follow-on task or final nomination.
