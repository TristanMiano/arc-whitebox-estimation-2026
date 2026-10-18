# Research strategy and effort map through T128

**Latest update: T154/T155 (2026-09-11).** All four recent fixed candidates
are tested local losses. The [failure diagnosis](../experiments/diagnosis/t155/REPORT.md)
finds a partial HGC calibration repair and demonstrates CMF proxy/score
mismatch; SCP/FAR causes are less completely isolated. Incumbent remains
ALG043-V000 /330597. T153 is proposed, not running.

**Latest pointer, T149 executed after T152 (2026-09-11 UTC):** The owner selected
CMF2, superseding its deferral. ALG046-V000 loses0.347% raw and1.074% adjusted
mean;6/12 adjusted wins, support.09155. Resources pass; no upload. All three
recent fixed candidates now have actual negative feedback. Retain
ALG043-V000 /330597 at5.41905133451e-9. T153 remains proposed.
[Report](../experiments/submission_policy/t149/REPORT.md),
[current candidate status](../experiments/submission_policy/t149/CANDIDATE_STATUS.md).
The original census and dated snapshots remain historical.

**Historical pointer, T143 (2026-09-08/09 UTC):** the completed joint-response
recurrence is summarized in the dated addendum below. ALG038-V001 /330153
remains official best. [T143 result](../experiments/theory/t143/REPORT.md);
JSP/T144 is proposed, not started. Earlier snapshots remain historical.

**Historical pointer, T136 (2026-09-06/07 UTC):** ALG037/330101 is the retained
official best at1.285804677308988e-7. The [combined research result](../experiments/theory/t136/REPORT.md)
proposes CSK3-R/T137 with augmented K2 as a fallback. See the dated addendum
below; the original census and earlier snapshots remain historical.

**Later update, T132 (2026-09-06):** the owner authorized a literature-first
trial and explicitly prioritized better submissions regardless of academic
novelty. The [literature index](LITERATURE_INDEX.md) and
[route-status tracker](RESEARCH_ROUTE_STATUS.md) record its sources, saturation
estimates, reopening conditions and subsequent-return baseline. T132 recommends
a bounded public-estimator comparison next. The historical census below remains
unchanged; it does not include T129–T132.

Snapshot: 2026-09-05 Pacific / 2026-09-06 UTC. Retrospective task **T128A**.
Current retained algorithm: **ALG031-V000**, official submission **329989**, adjusted
score **1.3618567538742354e-7**. This is the recorded grade, not a live leaderboard
check. T129 has not started. Recommendations below are proposals for directing
attention, not additional protocol gates.

The project is best described as **empirical algorithm search guided by
mathematical deduction, with increasingly important small supervised fits**.
The theory has produced useful exact identities and eliminated false mechanisms.
The recent winning implementation line combines analytic approximation, structured
sampling and learned correction weights. Calling it either pure deduction or pure
parameter tuning would conceal something important.

## What a theory recurrence is for

The purpose is to find a change whose expected official improvement justifies
its entire remaining cost: derivation, implementation, execution, qualification
and grading. Producing another candidate is optional. A derivation that rules
out an expensive idea can be a successful recurrence.

The recurring process, and how I would make its priorities explicit, is:

1. **Identify a specific remaining error.** Start with the complete incumbent
   and retained results: which approximation bias, sampling fluctuation or
   interaction could still be reduced? Distinguish a useful coordinate signal
   from a reduction in final mean-squared error.
2. **Derive a mechanism.** Use homogeneity, symmetry, conditional expectation,
   covariance identities and the network's piecewise-linear structure. Write
   the estimator and its assumptions, not just a promising family name.
3. **Try to break the argument cheaply.** Look for a counterexample, a zero
   covariance identity, a work-normalized variance bound, or a dimensional
   scaling obstruction. Small symbolic/synthetic checks can catch a sign or
   projection mistake without another challenge campaign.
4. **Translate the mechanism into complete-estimator risk and cost.** For parent
   error `e = estimate − truth` and proposed output change `v`, at an unchanged
   score multiplier the exact MSE change is `2 E[e·v] + E[||v||²]` (with the
   same coordinate normalization throughout). An individually better moment
   estimate can worsen the final blend. If the multiplier changes, compare the
   two full adjusted risks as well.
5. **Choose zero to two cheap attempts.** State the remaining uncertainty and
   the smallest production comparison that would resolve it. Reuse existing
   features where useful, fit only a declared small model when justified, and
   take a supported candidate to official feedback promptly.

These are not five additional reports or gates. They can be five short entries
in the existing scratchpad. Current policy already permits a small local screen
and roughly 90% support; its bootstrap support is a practical decision aid, not
an exact probability of a private-suite win.

Concrete deductions already changed the search:

- **Exact radial integration:** positive homogeneity gives
  `E[f(RU)] = E[R] E[f(U)]`. Replacing random radius by its mean is exact for
  this setting; more radial quadrature cannot improve that already-integrated
  quantity. This predates the recent recurrences and is retained in the sampler.
- **T025/T028, affine residuals:** an exact kink decomposition is useful, but
  subtracting an affine part does not create a new antithetically evenized
  gradient-rotation mechanism. A renamed duplicate did not merit a new run.
- **T095, complementary frames:** conditional rotational symmetry makes the
  two normalized frame estimates have zero cross-covariance. The proposed
  negative-covariance advantage disappeared algebraically before implementation.
- **T122/T126, closure and projection limits:** finite moments do not determine
  the ReLU expectation; the recorded four-moment counterexample differs by
  2.6064%. A Gaussian-looking selected direction can also miss orthogonal shape.
  These are limits on universal claims, not evidence that typical challenge
  networks realize the counterexamples.
- **T126, the full step matters:** T125's correction had favorable initial
  error alignment, but its squared step was too large. The complete variant
  still lost. This points to a risk question without licensing tuning on the
  already-open comparison rows.

Sources: [prior sampler report](PRIOR_ATTEMPT_REPORT.md),
[T095 mathematics](../experiments/checkpoint3/t095/THEORY_NOTEBOOK.md),
[T122](../experiments/theory/t122/REPORT.md),
[T126](../experiments/theory/t126/REPORT.md). The task CSV below retains source
locations for earlier decomposition decisions.

## Approach tree

This is a **conceptual tree, not a genealogy**: the winning hybrids combine
ideas from several branches. Leaves are representative algorithms or tests,
not a claim that every historical variant is shown. The exhaustive task mapping
is in the CSV. Cross-family theory stays in its own effort bucket so the same
hour is not credited to both nominees.

```text
Estimate deep-ReLU expectations more accurately per unit of allowed work
├── Sampling geometry and active directions
│   ├── Low-discrepancy samples + exact radius + antithetic pairs
│   │   └── ALG003 / inherited Sobol: conservative baseline, officially graded
│   ├── Gradient-adapted coordinates
│   │   ├── Early top-64 / top-16 tests: typical gains, damaging fixed-design tails
│   │   └── T033, T070 / ALG011: layer-local successor; no official incumbent
│   └── Structured spherical frames
│       ├── T085: Haar-MUB residual sampling test
│       └── T091/T091A → ALG014: Haar-Stiefel; official improvement
├── Structure, residuals and unbiased controls
│   ├── Dead/on/kink classification and sparse propagation
│   │   └── T019–T024: integrated structural candidate; complete comparison lost
│   ├── Exact affine/kink decomposition and stochastic continuation
│   │   ├── T025/T026: exact identity; residual-only sampling had severe tails
│   │   └── T080/T083/T089/T092: multilevel / suffix / survival tests
│   └── Conditional expectation and control variates
│       ├── T034 / ALG012: deep-gradient control
│       ├── T076/T077: transported kink and transport-ridge controls
│       ├── T079: angular-orbit integration, tractability failure
│       ├── T082 / ALG013, T088/T094: hidden-state and subframe controls
│       └── T086: spherical Stein/JVP control test
├── Moment propagation and analytic closure
│   ├── Higher cumulants
│   │   ├── T017 / ALG007: shallow K3 positive; full-cost obstacle
│   │   └── T110 / ALG020: trace/diagonal Edgeworth; no competitive successor
│   ├── Transport of early exact moments
│   │   └── T117B / ALG025: causal story failed; weak composition hedge
│   └── Covariance completion
│       └── T125 / ALG030: unfitted trace change; local loss 1.0826%
├── Closure–sample fusion and fitted observers [winning continuation]
│   ├── Blend biased closure with structured sample estimates
│   │   ├── T096 / ALG015: fixed shrinkage; large official adjusted-score gain
│   │   ├── T097 / ALG016: adaptive cross-fitted shrinkage failed
│   │   └── T103/104 / ALG017–018: independent arms and fusion; ALG018 graded
│   ├── Conditional response and shape corrections
│   │   ├── T108 / ALG019: harmonic skew and conditional fusion; official gain
│   │   ├── T111/T114/T115: source-risk proxy, LPITF and audit-carrier tests
│   │   └── T119A / RVRC: Opus variance recalibration; complete proxy loss
│   ├── Fitted analytic observers and cheaper numerical propagation
│   │   ├── T117 / ALG024: fitted observer; official gain
│   │   ├── T118 / ALG026: independent frame + observer; official gain
│   │   └── T120 / ALG027: fitted R3 signal; production/cost contract parked
│   └── Cheap physical trace and response updates
│       ├── T120B / ALG028: no new fit; official gain 3.7974%
│       ├── T124 / ALG029: one 16-column fit; official gain 3.8961%
│       ├── T127 / ALG031: one 22-column fit; official gain 0.4167%
│       └── T128 / ALG032: two-column shape fit; local loss 0.7171%
├── Cross-family theory, scouting and external intake
│   ├── T073–T098: repeated mechanism slates and algebraic eliminations
│   ├── T107/T109/T113/T116/T119/T122/T126: longer written recurrences
│   └── T108B and T112: external intake / mixed theory and public reconstruction
└── Baselines, runtime, evidence and protocol
    ├── T001–T015: environment, baseline, accounting and evidence foundations
    ├── T054–T066, T071: host recovery, native runtime and evaluation funnel
    └── D001/D002, T074/T102/T106/T123: calibration, packaging and policy
```

Some label ranges above are shorthand for related work, not assertions that
every task in the numerical interval belongs to that branch. In particular,
T007/T013 are sampling tasks. Use the explicit task lists in the data for counts.
A failed leaf closes that tested realization; it does not falsify every possible
member of its parent family.

## Effort by approach

The census has **116 started work items: 113 completed T tasks, two completed D
calibration tasks, and the partially executed, parked T120A**. Unrun T072,
deferred TODOs, T129 and this audit are excluded. Seven pre-numbered P events
are acknowledged separately; their work is not assigned invented task IDs or
time. Grouped events T019–T021, T054–T056 and T062–T063 map to their individual
TODO tasks and are not counted again as extra tasks.

| Primary approach | Tasks | Tasks with some timing | Recorded session-hours, at least |
|---|---:|---:|---:|
| Sampling geometry and active directions | 12 | 10 | 4.76 |
| Structure, residuals and unbiased controls | 21 | 15 | 6.22 |
| Moment propagation and analytic closure | 6 | 3 | 1.43 |
| Closure–sample fusion and fitted observers | 27 | 27 | 19.75 |
| Cross-family theory, scouting and intake | 18 | 18 | 23.06 |
| Baselines, runtime, evidence and protocol | 32 | 7 | 4.03 |
| **Total** | **116** | **80** | **59.24** |

These are **wall-clock task-session durations**, including ordinary execution,
repair, documentation and waiting. They are not pure reasoning hours or machine
compute time. Thirty-six tasks have no usable timing in the inspected records;
two more have only partial intervals. Missing times are not zeros. In particular,
the infrastructure total substantially undercounts the older host work. Summing
sessions also does not measure end-to-end calendar duration or guarantee no
historical overlap.

An independent, additive classification by **primary activity** gives:

| Primary activity | Tasks | Timing coverage | Recorded session-hours, at least |
|---|---:|---:|---:|
| Theory, source review and research planning | 20 | 19/20 | 21.59 |
| Candidate construction, experiments and empirical selection | 52 | 42/52 | 29.67 |
| Baselines, operations, validation and protocol | 38 | 13/38 | 5.53 |
| Dedicated official qualification/upload tasks | 6 | 6/6 | 2.45 |

A mixed task receives one primary activity, not a fictional stopwatch split.
T112 includes 60 theory minutes but is primarily an empirical reconstruction
here; T107 includes exploratory replays as well as theory. T120B/T124/T127
include uploads inside their candidate tasks. Thus the final row is not all
submission time, and the theory row is not all mathematical work.

Eight longer tasks explicitly record **at least 16.02 active theory hours**:
T107, T109, T112, T113, T116, T119, T122 and T126. Earlier theory is additional.
T107's 3h08 task duration includes only a stated minimum of 2h active theory;
it must not be relabeled as three hours of deduction.

Timing exceptions are preserved per row: T026 contributes its known 17m29
completion segment, not its entire 98m49 interrupted span; T095 contributes
47m29 across two sessions; T105A contributes 45m12 excluding a 93m32 owner
pause; T113 contributes 3h10 excluding the restart gap, rather than its roughly
52-hour calendar span; T120A contributes only its 26m45 initial audit interval.
These conventions make the totals useful lower-bound effort records, not a
claim of precise historical accounting.

## How much is fitting, tuning or machine learning?

**We do not train or fine-tune the supplied challenge network's weights.** We
estimate its output expectation. But learning an estimator's readout weights
from public training targets is supervised machine learning, even when the
features came from a derivation and the model is a small ridge regression.

Four different practices should stay distinguishable:

| Practice | Examples | Character |
|---|---|---|
| Derive a formula or prove an obstruction | Radial identity; complementary-frame covariance; finite-moment counterexamples | Deduction; no target labels required |
| Select mechanisms, sample counts, ranks or regularization | Early sampler/rotation sweeps; T013; six T117 rungs × three ridge values | Empirical search / hyperparameter selection |
| Fit coefficients across networks using training targets | T117, T118, T120, T124, T127, T128 | Small supervised models; frozen before comparison |
| Estimate moments, pilots or surrogate risk from generated samples | Active-gradient pilots; T097; T111/T115/T117B pseudo-label fitting | Numerical adaptation or self-supervised estimation; no official reference labels in those fits |

The table's examples are not disjoint time allocations. The confirmed public-
target fitting set contains **six tasks totaling 8.40 recorded task-hours**;
this is time in tasks that included fitting, not time spent solving regressions,
and is not an exhaustive count of every historical scalar calibration.
T117 genuinely performed a model/regularization search: six nested feature
rungs and three ridge values, with five whole-network training folds. It would
be misleading to describe that as only deduction.

The current lean era is more transparent:

| Attempt | New fit and data | Total wall-clock task time | Outcome |
|---|---|---:|---|
| T124 / ALG029 | One 16-column anchored fit; 500 existing training caches | 33.82 min | Official gain 3.8961% |
| T125 / ALG030 | No new fit; analytic covariance-trace replacement | 14.08 min | Local loss 1.0826%; no upload |
| T127 / ALG031 | One 22-column anchored fit; 500 existing training caches | 35.10 min | Official gain 0.4167% |
| T128 / ALG032 | One two-column fit; 32 newly collected training feature rows | 50.73 min | Training gain 0.2021%, local loss 0.7171%; no upload |

So **3/4 recent attempts used supervised coefficient fitting**, but none
performed an automatic parameter grid. T124/T127 reused existing propagated
features. T128 had to collect new features and repair execution, making a
nominally tiny two-coefficient model the slowest of these four attempts.
Model dimension is not a good proxy for engineering cost.

The current algorithm inherits prior fitted corrections as well. T120B's
unfitted trace update was a useful analytic improvement, but it did not make
the whole estimator label-free. Conversely, the gains of T124/T127 belong to
the whole fitted update: without an ablation we cannot assign them exclusively
to either the derivation or the fit. Extra ablations are not needed merely to
make a submission decision.

The two recent cycles give an unusually well-recorded comparison:

- T122 theory + T124/T125: **3h06**, one official improvement.
- T126 theory + T127/T128: **3h50**, one official improvement.
- Together: **6h56** of task sessions, including **4h42** in theory-task sessions
  (**4h01 explicitly active theory**) and **2h14** in four attempts. This excludes
  the separate 13m39 T123 protocol edit and between-task gaps.
- Official adjusted score moved from **1.42299664617e-7 to 1.36185675387e-7**,
  a **4.2966%** reduction. Two successes out of four attempts is a description
  of this tiny sequence, not a calibrated future success rate.

For operational context, T127 reached accepted upload in **16.11 minutes**;
its next **18.99 minutes** included grading and overlapping record preparation.
T128's 48 completed prediction meters sum to **12.84 minutes** within its
50.73-minute task; loading, incomplete calls and repairs are additional. We
should track these separately instead of calling the entire task compute.

## What has actually reached the grader?

The graded sequence provides an outcome metric for the tree. Scores below come
from saved official receipts. Differences between entries are observed official
score changes, not causal ablations of individual ingredients.

| Algorithm | Main idea | Successful submission | Official adjusted score |
|---|---|---:|---:|
| ALG003-V009 | Conservative Sobol fallback | 328477 | 7.81113541080e-7 |
| ALG014-V003 | Haar-Stiefel sampling | 328479 | 6.60719950258e-7 |
| ALG015-V000 | Lower-cost fixed closure/frame shrinkage | 328500 | 2.843538175e-7 |
| ALG018-V000 | Refined closure and independent-arm fusion | 328686 | 2.69314724164e-7 |
| ALG019-V000 | Harmonic skew and conditional fusion | 328762 | 2.39959831788e-7 |
| ALG024-V000 | Fitted analytic observer | 329529 | 1.71538296854e-7 |
| ALG026-V000 | Faster independent-frame/observer composition | 329690 | 1.47916588048e-7 |
| ALG028-V000 | Simpler physical trace update | 329774 | 1.42299664617e-7 |
| ALG029-V000 | Anchored physical-response recalibration | 329806 | 1.36755548851e-7 |
| ALG031-V000 | Parity-split response fit | 329989 | 1.36185675387e-7 |

Ten distinct algorithms have successful grades in this recorded sequence.
The table omits failed upload attempts as separate algorithms; T105A retains
its generic failed attempt and retry, and T117A its rejected package and
compliance repair. Those remain part of the task histories and time.

## Where I would direct the next recurrence

The concern about drifting into local tuning is justified. The last two
recurrences derived real new information, yet both prioritized extending the
incumbent's feature readout. That is efficient for small gains but explores a
narrow neighborhood. The tree has many tested leaves under related correction
schemes, not equally deep coverage of all possible estimators.

My recommendation is to **preserve the cheap submission path while giving the
next theory recurrence a deliberate structural alternative**:

- First investigate a change to the underlying approximation or sampled
  quantity: a cheaper exact conditional reduction, a useful deep-network
  decomposition, or a tractable multivariate representation that preserves
  relevant shape. These families have antecedents in our failed tests, so a
  successor needs a specific answer to their variance/cost or projection
  obstruction. This is not permission to rebuild the old losing variants.
- Keep one inexpensive incumbent improvement as a competing option when the
  algebra exposes it. A single small fit is acceptable; automatically sweeping
  T128's direction, bins, loading or training size would not be my next move.
- Rank both by plausible **complete adjusted-score improvement per remaining
  hour**. Do not require a structural candidate to be implemented merely to
  balance the portfolio. Zero nominations remains an acceptable outcome.

A much larger learned surrogate is a separate strategic option, but this audit
finds no reason to make it the default: it introduces a different training and
transfer problem. Likewise, other entrants' score gaps do not identify their
algorithms. We should choose broader ideas for mathematical reasons, not infer
a hidden top-ranked method from the leaderboard alone.

For future recurrences, a single small scratchpad table would make this audit
easier: **branch; active minutes; result/counterexample; next decisive action**.
Reuse the task's existing execution, repair and grading timings. This would
expose concentration of effort without creating another validation process.

## Follow-up: where attention may have stopped too early

The owner's subsequent **T128B** review identified several incomplete tracks.
The [detailed neglected-track audit](NEGLECTED_RESEARCH_TRACKS.md) supplies
source evidence, failure boundaries, subjective probability ranges and possible
one-time agent briefs. The strongest concrete omissions are:

- **DS/M observer fields:** T117's depth/transport variants had favorable
  selection results, but an old minimum-gain/sequential rule excluded them.
  Their 500 old training feature files still exist; current compatibility
  remains to be checked.
- **RCERC exact first-layer controls:** a corrected, developed design was
  displaced by the two-candidate cap, with no empirical candidate rejection.
- **Uniform fixed-count continuation:** T092's adaptive rule failed while its
  simpler uniform control remained promising in a limited proxy. T093 then
  excluded follow-up because another mechanism family was required.

Other candidates are smooth gate-conditioned coefficients (KCAS), output-aware
particle compression (BLMFC), compressed joint non-Gaussian propagation,
symmetry-aware covariance acceleration, and reference-residual ensemble anchors.
Some received substantial theory but no implementation; some older effects
have already been partly absorbed by today's stronger incumbent. The review
does not relabel actual losing variants as winners.

My current subjective chances that at most two focused theory/review hours
yield a candidate worth one small production attempt are respectively
**60%, 50%, 40%, 45%, 30%, 30%, 35% and 20%** in that review order. These are
planning judgments, not score confidence or independent probabilities; the
detailed audit separately gives lower chances of an actual official gain.

For a first agent trial, I would assign RCERC, uniform continuation and
output-aware compression to three separate investigations while the main
agent checks the DS/M opportunity and integrates the findings. The proposal
is bounded and optional. No agents or T129 were started, and no permanent
protocol change was made. Evaluate one trial before deciding whether to repeat it.

## Attribution and reproducibility

The owner identifies GPT-5.6 Sol as the principal contributor before the Astra
handoff. The repository records the mathematical and experimental artifacts,
but it is not a reliable per-model time ledger. This report does not allocate
hours or individual gains to models from task dates alone.

External contributions remain attributable: Fable's all-layer EMC proposal was
intaken in T108B, repaired into trace/diagonal theory in T109 and tested in
T110; Fable 5.1's early-anchor proposal led to T117B/ALG025; Opus-5's variance
recalibration was repaired and tested in T119A. These inputs helped direct
questions; their tests did not independently create the current official best.
See [Fable intake](../experiments/checkpoint3/t108b/INTAKE_ASSESSMENT.md),
[early-anchor screen](../experiments/checkpoint3/t117b/REPORT.md), and
[Opus screen](../experiments/checkpoint3/t119a/REPORT.md).

Auditable artifacts:

- [Task-level CSV](../experiments/protocol/t128a/TASK_AUDIT.csv): all 116 rows,
  primary family/activity, recorded minutes, timing exceptions, events and sources.
- [Structured data](../experiments/protocol/t128a/STRATEGY_DATA.json): aggregates
  and the same task records.
- [Source inventory](../experiments/protocol/t128a/INVENTORY_RAW.json): preserved
  TODO blocks and event records as read for this audit.
- [Classification/rebuild script](../experiments/protocol/t128a/build_audit.py):
  explicit family membership and timing conventions; rerun against the preserved
  inventory to reproduce the task table and aggregates.
- [Historical TODO](../experiments/protocol/t123/before/TODO.md),
  [event ledger](../state/experiments.csv), [algorithm ledger](../ALGORITHM_LEDGER.md),
  and the individual reports linked in each task row supply the evidence.

The classification is an editorial aid, not a unique mathematical taxonomy.
Timing precision in raw records does not make the category boundaries precise.
No new candidate, target access, fit, propagation, upload or theory recurrence
was performed for this audit.


## T129 addendum — completed coordinated recurrence, 2026-09-06 UTC

This is a dated addition to the historical116-task census, not a rewrite of
its totals or earlier task classifications. T129 adds one cross-family theory
task: **181.15 active root minutes**, **209.32 elapsed to
record checkoff**, and **284.91 overlapping agent
person-minutes. [Result and timing](../experiments/theory/t129/REPORT.md).
Agent time is not added to wall time. No new candidate experiment ran.

```text
T129 theory recurrence
├── Sampling/compute: uniform continuation review + partial/covariance algebra
│   └── PF1760: prospective T130, no coefficient fit
├── Current shape: full leading K4 + matching K3-squared response
│   └── FC4S: prospective T131, one scalar fit on32 fixed F inputs
├── Exact controls: remove quadratic harmonics + repair learned fitting noise
│   └── R4IF8-P: fully specified reserve after a cost/time re-ranking
├── Observer histories: DS partly distinct; simple transport partly absorbed
│   └── DS-only small-fit reserve; old favorable evidence preserved
└── Limits: fixed-frame geometry, conditional mixtures, norm/H3-product noise
    └── Concrete reopening conditions; no automatic experiment queue
```

The most practical late finding was the initial identity-covariance Gram
specialization:2.146B projected FLOPs saved. It makes the all-output structural
field affordable, removing the earlier128-output coverage compromise. Both
nominees still require actual production metering and a small score comparison.
Their35%/25% official-win priors are subjective, not new outcome evidence.

This run was mostly deduction and mathematical source/cost work, plus fixed
input-only feature geometry and synthetic regression examples. It did not fit
a candidate or access challenge targets. PF1760 has no planned fit; FC4S has
one scalar supervised readout. The current learned-control alternative remains
a reserve. See [the final slate](../experiments/theory/t129/DECISION_FREEZE.json)
and [retained options](../experiments/theory/t129/RESERVES.md).

The trial produced useful independent corrections and a cheaper final route.
There is no matched solo run or token-cost comparison establishing an optimal
effort setting. Three agents were the maximum concurrency; bounded follow-ups
reused them. No reset or permanent multi-agent protocol change occurred.

## T136 addendum — persistent joint states reopened

```text
Joint distribution / cumulant propagation (R08)
├── Old full K3: T016 cost failure; T017 shallow positive evidence
├── Persistent paired K3 + full repeated remainder: CSK3-R → proposed T137
└── Third trace vector + fourth scalar: A2LR → cheap fallback, unexecuted
Output-aware sample compression (R09)
├── Known balance/recombination machinery + explicit finite-bank risk
├── Exact spherical quadratic controls; existing QR cancellation accounted for
└── Nonlinear residual feature and charged solver → unresolved, no nominee
Existing readout corrections (R02)
├── T134 absolute-state transfer → official improvement
├── T135 joint27-column update → further official improvement
└── More same-feature coefficient searching → lower priority now
```

T136 adds one combined research task: 138.79 elapsed minutes,83 active
theory and16.5 literature, with selection/handoff recorded separately. A rough
25/58 active-theory split assigns balance/control work to R09 and joint-state/
cost work to R08. It adds no trained model, fitted coefficient or challenge
algorithm test. Small fixed mathematical cases changed the representation;
this was primarily deduction and adaptation of known work. The proposed larger
test may fail and is not being counted as a submission gain in this map.


## T139 addendum — compress the successful joint state

```text
Joint cumulants / R08
├── CSK3-R: T136 theory → T137 official86.49% gain
│   ├── Equivalent final contractions / depth4: T138 official15.55% gain
│   └── Persistent state compression / R12: T139
│       ├── C64-E: two recent sources + rank64 core + old modeled E → proposed T140
│       ├── Compression-only C64 → simpler unexecuted fallback
│       ├── One-leg / two-leg projections → valid alternatives, not selected
│       └── One-future-trace repair → parked on low observed metric benefit
├── Fourth response: coordinate trace + marginal kurtosis → Q4D secondary nominee
├── Conditional32 source: one-factor identity passes → covariance coverage reserve
└── Full nonradial fourth trace → off-diagonal response remains incomplete
Sample-bank compression / R09
└── Unchanged by T139; this is a different object from persistent tensor history
```

T139 used **121.02 elapsed / 120.05 useful minutes**, including **92.37 active theory**, 10.67 literature and 17.01 selection/handoff minutes. Setup (0.97 minutes) is excluded from useful time. [Actual timing](../experiments/theory/t139/TIMING.json).

This adds one combined research task, with no candidate training, challenge
comparison, upload or agents. It is deduction and numerical representation
work: fixed synthetic checks expose algebra, cost and coverage limits. The SVD
selects an instance-specific tensor basis; it does not fit labels. The complete
[report and handoffs](../experiments/theory/t139/REPORT.md) retain the selected
path and the alternatives without adding permanent protocol gates.


## T140 measured follow-up — 2026-09-08

The T139 compression branch now has one full production test:
`joint cumulants → compressed third history → rank 64/recent 2 plus persistent old E
→ ALG039-V000 (C64-E) → local rejection`. It used17.50 elapsed minutes through
records (13 full-size calls,5.48 metered minutes overlapping work), not the
100–130 minutes initially estimated. Cost passed at 422.773B; the 12-network
adjusted ratio was4.6123,0 wins. No fitting, parameter search, new theory
recurrence or official submission. The task reused the qualified production
harness and stopped on the first clear score decision.

The sibling `compression-only, incumbent ephemeral E` remains untested and is
proposed as T141. This negative leaf combines two changes and does not establish
that either the whole compression family or persistent cumulants are exhausted.
[Result and next-step reasoning](../experiments/submission_policy/t140/REPORT.md).


## T141 measured follow-up — 2026-09-08

The sibling branch is now tested:
`joint cumulants → compressed third history → rank64/recent2, ephemeral E
→ ALG039-V001 (C64) → local rejection`. Cost394.359B, adjusted ratio4.1602,
0/12 wins. Full-rank generated trajectories match the incumbent within5.36e-7.
No fitting or parameter search. Removing E persistence leaves the large deficit,
so both fixed compression leaves are now closed unchanged.

T140 and T141 together contribute two production tasks,26 full-size candidate
calls, and24 paired network evaluations on the same12-network development
cohort (not24 distinct networks). Metered predictions total10.99 minutes,
overlapping implementation and analysis. T140 used19.48 elapsed minutes through
commit preparation; T141 used11.90 through records, with final elapsed recorded
in its [timing artifact](../experiments/submission_policy/t141/TIMING.json).
There was no new theory recurrence or official submission in these tasks.

The next proposed branch is Q4D: full third history plus a richer fourth state.
Compression should reopen around preserving later moment responses, rather than
more generic tensor-norm compression or a rank grid.
[Result](../experiments/submission_policy/t141/REPORT.md).


## T142 measured follow-up — 2026-09-08

The second T139 nominee now has a production outcome:
`joint cumulants → richer fourth state → coordinate trace + marginal Q4D
→ ALG040-V000 → raw-accuracy gain, adjusted-score loss`. Raw MSE falls8.14%
on all12 networks; compliant cost848.844B produces adjusted ratio1.03016.
Cheaper numerical realizations fail the residual cap. This is a useful
accuracy result with an unresolved cost problem, not an exhausted fourth-state
family. No fitting, parameter search or equation tuning was performed.

T142 used36.72 elapsed minutes through records and18 full-size
prediction calls totaling13.73 metered minutes, overlapping work. It required
operational repairs, unlike T140/T141. The three T139 implementation follow-ups
now cover three mathematical candidates,44 completed full-size calls and36
paired candidate/network evaluations on the same12-network cohort. They produced
no new official submission. T139 research plus these follow-ups took about3.2
hours; exact stage-specific clocks are in their task records. No new theory
recurrence or sub-agents ran in the three follow-ups.

Preserve Q4D and its concrete cost envelope as a small-gain fallback. Proposed
T143 should pursue a credible larger joint-response improvement, with missing
persistent third-source terms a primary question and response-preserving
compression a conditional reserve.
[Q4D report](../experiments/submission_policy/t142/REPORT.md).

## T143 addendum — broader sources, explicit joint-response candidates

[The recurrence](../experiments/theory/t143/REPORT.md) extends the successful
analytic joint-state branch. The current incumbent is ALG038-V001 /330153,
adjusted1.46676758754e-8; this later addendum supersedes earlier live pointers.
No T143 production score or new submission exists.

```text
Analytic joint-state propagation / R08
├── Improve newly created third source: T143
│   ├── JSP: selected first; existing factors, changed joint response
│   ├── Exact pair/resummed leg: identities work; whole response not uniformly better
│   ├── Added covariance triangle:18 live rank4 columns; useful modes unresolved
│   └── Coherent joint contraction: precise scalar formulas; coverage unresolved
├── Retain discarded completion: T143
│   ├── E1: selected second; one extra n-column hop, full main history retained
│   ├── Full E: modeled bookkeeping derived; roughly40% raw-gain cost hurdle
│   └── Source diagonal gauge: current tensor invariant; future metric/update open
├── Conditional nonlinear response: T139 → T143
│   └── Two-mode-leg projection: exact identities; residual correlations matter
└── Reduce persistent state / R12
    ├── Rank64 C64-E and C64: measured failures T140/T141, unchanged leaves closed
    └── T143 actual-next-query Gram: exact cubic queries; mixed response unresolved

Q4D / T142: retained accuracy-positive engineering fallback; no automatic rerun
```

T143 used **120.02 derivation, 60.06 literature, and 30.21 candidate-selection minutes**: **210.29 useful minutes** over **250.43 elapsed minutes** through records. Setup and overhead are excluded from the three floors. [Actual timing](../experiments/theory/t143/TIMING.json).

This is **deduction-led algorithm design with generated numerical checks**.
Twelve check records test tensor identities and expose approximation failures;
they are not twelve challenge tasks or a parameter-fitting campaign. No
challenge predictions/targets, learned coefficients, rank/seed selection on
scores, or subagents were used. The gauge optimization is an analytic
per-state objective, not training; its complete numerical update remains a
reserve. The two selected candidates have fixed formulas and no fit.

The wider review registered50 additional sources across ten adjacent areas,
with explicit differences in access depth. The strongest reusable connections
are response-oriented reduction, projected-state memory, conditional Gaussian
chaos and observable kernels. No source supplied a ready superior full-width
estimator. This does not justify treating unexplored integration families as
failed; it does reduce the value of another immediate generic survey.

Relative to T139, this round spent more time challenging the attractive first
candidate and investigating alternatives. Some larger proposals became less
promising after their missing terms or repeated-slice costs were exposed.
The outcome is two costed nominees plus explicit reserves, not a proven larger
score gain. The standing larger-upside preference was used to keep exploring
after the cheap source update appeared; it did not require choosing the most
expensive implementation at the end.

Per-route stopwatch totals were not recorded within this interleaved round.
Count its measured duration once, in cross-family research, rather than
crediting all of it to each leaf. The [route tracker](RESEARCH_ROUTE_STATUS.md)
updates search saturation separately from implementation promise. Subsequent
bounded tests and official results will determine the actual return on T143.


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

## T146 — public reproduction first; homogeneous response retained as a reserve

The next recommendation is **H146-PUB29**, an unchanged reproduction of a newly
public Phase2 implementation. Its author reports5.40e-9 adjusted, about54.4%
below our retained1.1833e-8. This is a newly found external result, not a score
we achieved. [Selection and proposed T147](../experiments/theory/t146/CANDIDATE_SELECTION.md).

```text
Better official adjusted score
├── Public joint-cumulant implementations / R01
│   ├── T112 partial reconstruction: historical source-unavailable limitation
│   └── T146 L85: complete pinned V29 source → sole reproduction nominee
│       ├── Regenerated fourth core + matched third-source feedback
│       ├── Moderate age-dependent shared bases / R12
│       └── Batched matrix arithmetic and persistent buffer pools
├── Improve modeled joint response / R08
│   ├── JSP → T144 retained official gain19.33%
│   ├── Fixed E1-on-JSP → T145 loss; unchanged leaf closed
│   ├── Gated completion metric → T146 exact surrogate; accuracy target uncertain
│   ├── Homogeneous fourth conversion → T146 HGC reserve
│   │   ├── Existing pair interface: generated identity checks pass
│   │   ├── Residual paired-fourth source: affordable factor correction derived
│   │   └── Finite closure: favorable cases and counterexamples; no ARC test
│   └── Source projection → finite connected program; cost/noise gaps remain
├── Preserve compressed history / R12
│   ├── Fixed rank64 C64/C64-E → T140/T141 losses
│   └── T146 mixed-query solve → immediate query works; later history fails
└── Change observable-state representation / new R13
    ├── Weighted positive-cone law → exact degree-one observable equivalence
    ├── Two-atom and Gamma/Beta checks → naive closures can be worse
    └── Affordable positive finite-state transition → unresolved larger reserve

Separate Gaussian triangle source: still open, with explicit contraction costs
Q4D: preserve its earlier raw gain on ALG038; no automatic transfer or rerun
```

T146's own design work is deduction-led: response identities, source diagrams,
cost calculations and generated examples. The18 check records are mathematical
diagnostics, not challenge experiments or a fitted parameter search. Optimizing
an explicit per-state gauge objective would be a deterministic numerical
optimization, not training; it remains unselected here.

The sole nominee does include **the public author's fitting and empirical
selection**: its fourth-core tables, adaptation normalization and age/rank
choices. T146 did not refit them. The proposal is to use the published values
unchanged because useful submissions take precedence over originality or a
preference for wholly unfitted formulas.

The public lead appeared early, and the larger research threads were developed
before the final comparison. Their theory is materially more complete, but
none currently offers stronger evidence per remaining hour than reproduction.
The homogeneous conversion is exact for Gaussian first-order responses; finite
closure can still reverse the accuracy ordering. A new source formula can be
cheap while its usefulness remains untested. These boundaries are part of the
result, not reasons to demand an extensive new scientific campaign.

Count this as one interleaved research task. Exclusive category timing is in
[the time log](../experiments/theory/t146/TIME_BLOCKS.json); per-route time was
not separately recorded and must not be multiplied across the tree. There are
no agent minutes, challenge predictions, target access, fits or uploads in
T146. The public source review adds16 entries to the literature index, with
reading depth distinguished. No return on a T146 submission has yet been
measured. [Detailed reserves](../experiments/theory/t146/RESERVES.md) and
[route status](RESEARCH_ROUTE_STATUS.md) state what would reopen each branch.

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

## T148 update — conditional source geometry on the public V29 parent

The incumbent remains ALG043-V000, official5.41905133451e-9. One completed
recurrence adds the following branch, with no new challenge result:

```text
Public V29 joint-cumulant state
├── Conditional fourth metric → H148-CMF2: first bounded-test nominee
│   ├── Analytic row-norm / mean-subspace predictor
│   └── Two additional vectors sharing the A/P age projections
├── Leading CT feedback → H148-FAR-CT: optional cheap fallback
├── Joint fourth-core and metric prediction → calibration reserve
├── Homogeneous conversion → cheap fifth/sixth vertices; finite update open
├── Fourth-core vector queries → higher mixed-query cost open
└── Whole-matrix spectral metric → information gain; cheap source carrier open
Homogeneous observable state on the positive cone
└── Centered angular moments → finite closure and full contraction open
```

The work was deduction and implementation reasoning supported by generated
algebra/geometry checks. No new fit or candidate parameter sweep was performed.
CMF2's online regression coefficient is analytic under a stated weight model;
it is not learned from challenge targets. Existing public fitted coefficients
remain in the parent. A cheap lead did not terminate research: the larger
HGC/core/spectral routes received further derivation before selection.

Actual categories:121.19 derivation,30.10 literature,30.14 selection minutes,
181.43 useful total. Per-route minutes were not measured; count this as one
cross-family recurrence and do not allocate its full time to every branch.
A system crash/recovery interval is excluded from active time. No agents or
new submissions. [Report](../experiments/theory/t148/REPORT.md),
[selection](../experiments/theory/t148/CANDIDATE_SELECTION.md),
[reserves](../experiments/theory/t148/RESERVES.md),
[timing](../experiments/theory/t148/TIMING.json).


## T150 update — larger changes in the propagated law

```text
Analytic joint-state propagation on V29
├── Change the law used by the finite closure
│   ├── Fixed input radius: H150-SCP-A — specified, UNTESTED; preferred T151
│   ├── Layerwise homogeneous conversion: H150-HGC6-A — specified, UNTESTED
│   └── Positive-cone observable state — exact law known; affordable closure open
└── Refine existing source geometry
    ├── H148-CMF2 / T149 — specified, NOT TESTED, owner-deferred
    ├── H148-FAR-CT — specified, UNTESTED cheap fallback
    └── Joint-core and spectral metrics — named finite-source/cost gaps remain
```

One task added60.10 active written-theory and4.48 selection minutes to this
branch; time was not separately metered per leaf. No new literature block,
challenge inputs/targets, fit, candidate execution, package, upload or agents.
Three generated algebra records plus scalar constants and static cost arithmetic
support implementation identities, not performance. This round is deduction
and finite-model design, with inherited public calibration held fixed.

The owner corrected selection drift toward likely small gains. SCP-A has a
subjective15–30% chance of a retained official win, with a plausible15–45%
adjusted reduction conditional on success; CMF2 remains25–45% for2–15%.
Those are uncertain forecasts, not a new screen or a reason to discard cheap
work. The [full inventory](../experiments/theory/t150/UNTESTED_INVENTORY.md)
distinguishes recent algorithms, older untested forms, open routes and tested
leaves. The [report](../experiments/theory/t150/REPORT.md) explains the choice
and its limitations. T151 requires owner selection; no fallback starts itself.


## T151 update — one ambitious leaf tested

The fixed-radius leaf H150-SCP-A is now **tested: local competitive loss**,
not forgotten or unimplemented. It loses all12 raw/adjusted comparisons while
passing15 full-shape resource calls. One fixed source, no fitting or parameter
search. Generated source/mean/fallback checks pass; no algorithm repair.
This is analytic implementation and empirical feedback, with no trained change.
[Actual task timing](../experiments/submission_policy/t151/TIMING.json).

The sibling H150-HGC6-A remains **specified and untested**, proposed as T152.
Its different finite conversion still warrants direct feedback before assuming
this broader route is exhausted. T149/CMF2 remains **not tested and deferred**;
FAR-CT remains an untested cheap reserve. No fallback was started automatically.


## T152 update — both ambitious leaves have measured outcomes

```text
Joint-state propagation on retained V29
├── Change the law/representation used by the finite closure
│   ├── Fixed input radius: SCP-A — tested T151; adjusted loss8.42%
│   ├── Layerwise conversion: HGC6-A — tested T152; adjusted error8.564x
│   └── Positive-cone observable state — incomplete finite closure; open
└── Preserve different joint information
    ├── Joint fourth core / future-response queries — proposed T153 theory
    ├── CMF2 / T149 — NOT TESTED, owner-deferred
    └── FAR-CT — UNTESTED cheap reserve
```

T152 implemented one fixed analytic algorithm, with no local fit, parameter
search, candidate repair or agents. It used15 full-shape calls: three lifecycle
probes and twelve paired development networks. All resource checks pass;
extra settled compute1.51%. Generated checks support the changed formulas,
while actual score feedback rejects this finite algorithm. The descriptive
follow-up reused saved predictions and ran no further estimator.

The last recurrence's two implementation tasks produced no submission. Their
losses differ greatly in size; treating them as one universal failure would
hide information. A new recurrence should revisit specific state/response
choices and other routes, without turning into an automatic cheap-correction
queue. [Timing](../experiments/submission_policy/t152/TIMING.json) separates
engineering from compute waiting; this is one implementation task, not another
block of literature or theory time credited to every branch.


## T149 update, executed after T152 — the cheap conditional metric tested

The CMF2 leaf is now **tested: modest local competitive loss**, rather than
forgotten or deferred. One fixed analytic implementation, no local fitting,
rank/coefficient sweep or agents. It uses conditional regression with a
closed-form coefficient from current state/weights; this is not training on
challenge targets. Parent public fits are inherited unchanged.

Three lifecycle probes and twelve paired networks all pass resources;
extra compute0.736%. Raw error rises0.347% and adjusted error1.074%, with6/12
adjusted wins. This supplied the intended cheap empirical feedback and did
not trigger more expensive experiments. FAR-CT remains untested. The larger
joint-core, future-response and alternative-state branches remain research
options, with no ready replacement or demonstrated gain claimed.

T149 used one implementation task; no new theory/literature minutes should be
credited to it. [Timing](../experiments/submission_policy/t149/TIMING.json)
separates engineering and compute waiting. The updated T153 proposal balances
larger opportunities and cheap reserves using all three recent outcomes.


## T154/T155 — what the negative tests actually taught us

| Approach leaf | New evidence | Next useful question |
|---|---|---|
| HGC6-A homogeneous conversion | Inherited positive lower clamp keeps converting a changed state; core flips sign by layer5. Zero-floor diagnostic reduces raw8.585x->1.105x on two inputs, still a loss. More old-source fidelity does not fix it. | Can a consistent transformed calibration or finite perturbation preserve the useful response without cumulative drift? |
| CMF2 conditional metric | Intended metric proxy improves at all28 diagnostic updates, while final score loses. | What joint core/response information, absent from a metric-only predictor, matters to the final observable? |
| SCP-A fixed-radius closure | Initial physical moments agree to rounding; third response diverges after the next nonlinear update. No HGC-like core collapse on the completed trace. | Which mixed radial response or residual-source approximation prevents useful law-equivalence transfer? |
| FAR-CT coefficient completion | Correct specified contractions; almost no helpful final-error projection; tiny cost but raw loss. | Is it useful only alongside a coupled source/feedback correction? No standalone coefficient sweep is justified. |

T154 adds one fixed analytic implementation task. T155 adds one cross-route
diagnosis:14 completed full-size calls, three operation-accounting exceptions,
no agents, no trained coefficients, no target-driven parameter search and no
new literature search. The descriptive best scalar in the error analysis is
an oracle calculation, not a fitted algorithm. These are empirical tests guided
by deduction; no new theory recurrence time is claimed. Use the linked
[T154](../experiments/submission_policy/t154/TIMING.json) and
[T155](../experiments/diagnosis/t155/TIMING.json) clocks once when counting effort,
not once per route.

The next proposal preserves ambitious joint/response alternatives. A partial
repair of a losing candidate is useful evidence, not an automatic low-risk
replacement for those alternatives. [Updated T153 proposal](../experiments/diagnosis/t155/NEXT_PROPOSAL.json).

## T153 update — empirical checks during the derivations

```text
Retained public V29 native joint state
├── Better local core/metric precision
│   ├── P01/P05b/P11 joint-core variants — tested adjusted losses
│   └── P23 transverse fourth source → P24 one-hop closure — tested loss
├── Replace or compress native third history
│   ├── P07 one-vector/matrix closure — large loss
│   ├── P09 protected current moments — large loss
│   ├── P14/P15 coupled local basis — same-rank improvement; still overall loss
│   ├── P19 moderate ranks — close losing reserve
│   └── P25–P28 future-weighted native basis — positive saved-state geometry
│       └── H153-NFC128 — ONE finite nominee; full algorithm UNTESTED
└── Change the finite law/state
    ├── HGC signed clamp — same as zero-floor control
    ├── Finite homogeneous boundary — derived; too small to explain most drift
    └── Complete compatible gauge / positive-cone / conditional state — OPEN
Cheap reserves: current-rank coupled metric; actual-trajectory residual head;
small-gate history packing. None is an automatic fallback task.
```

The round has121.44 active derivation,30.36 literature,67.46 empirical design/
prototype/interpretation and30.04 selection minutes,249.30 research minutes
in total. Final elapsed time/estimate error are in the [timing record](../experiments/theory/t153/TIMING.json).
No per-route stopwatch was used. Assign this once as a cross-family recurrence;
do not multiply its hours across branches. Of28 numbered probes,17 primarily
concern native/history compression,7 fourth-core/source geometry,3 homogeneous
state and1 radial/observable-state geometry. These are work counts, not equal
durations or28 independent algorithm trials.30 full-shape calls consumed13.25
summed metered minutes, overlapping active work.

This was deduction with adaptive empirical feedback. Two reduced-rank settings
and several fixed structural sensitivities were tested. No new challenge-target
coefficient fit or trained model was made. Spectral bases optimize a specified
state proxy; retrospective output-alignment scalars remain diagnostics. The
parent's public calibration is inherited, and its old CORR_BETA rider is off.
No agents were used.

The preference for credible larger gains remained active. Several small-gain
core possibilities were recorded and rejected on actual cost. A late stronger
native-response signal received further probes before selection. Its complete
NFC128 implementation is still untested, with a15–30% subjective chance of a
retained official win and5–20% plausible gain conditional on success. No tested
integrated T153 realization beat the adjusted objective. [Report](../experiments/theory/t153/REPORT.md),
[selection/inventory](../experiments/theory/t153/CANDIDATE_SELECTION.md),
[finite specification](../experiments/theory/t153/NFC128_SPEC.md).


## T158 update — broader exploration with integrated evidence

T157 has since tested and rejected the historical H153-NFC128 nominee. T158
completes240.10 active minutes, with46 probe entries and91 full-size calls
on eight exposed networks;52.34 summed prediction minutes overlap other work.
There are no per-route clocks; count this as one cross-family recurrence.
No agents/upload. One separate five-feature primary fit plus six LOO diagnostic
fits; the nominee has no new fit. The method remains mainly equation-driven
with adaptive experiments, rather than a large coefficient/rank search.

```text
T158 broader recurrence
├── Native history / compression
│   ├── Exact spectral NFC — still loses
│   ├── Coupled basis only — tiny pilot reserve
│   ├── Lost-trace compensation320/192 — six-network adjusted gain2.96%
│   │   └── +15-addition Winograd/shared arenas — H158-TRACE-WINOGRAD
│   │       └── Eight-network pilot: adjusted−7.45%,8/8 wins; UNsubmitted
│   └── Cross-source Grams / sketches / pruning — weak or narrow reserves
├── Positive and compatible laws
│   ├── Final NIG — tiny pilot gain; recurrent/joint forms weak/adverse
│   ├── One-common-mixer joint NIG — inspected moment match incompatible
│   └── Conditional/multi-mixer/positive-cone finite state — still unbuilt
├── Higher moments and full response
│   ├── Scalar/fifth/radial response — small or weak
│   ├── Persistent harmonic fourth-star — cheap, but pair loses
│   └── Diagonal-repaired fourth-chain range — useful saved-state signal
│       └── Affordable trace projection + full feedback — still unbuilt
├── Hybrid analytic/sampling — measured remainder variance/bias bill too high
└── Small fitted trajectory head — ~1% held-out gain, shipping head unbuilt
```

The larger-change branches continued after the cheap positive lead appeared.
They did not yield a convincing large raw-accuracy improvement. The main nominee
has much stronger empirical evidence and85–95% subjective chance of a retained
official gain, with4–10% conditional adjusted reduction. The current larger
reserves retain uncertain planning forecasts, not the nominee's probability.
Proposed T159 uses ordinary affected package checks and the existing pilot;
it must not automatically repeat a full comparison or expand into a rank ladder.
[Research report](../experiments/theory/t158/REPORT.md),
[route priorities and effort/returns](../experiments/theory/t158/ROUTE_UPDATE.md),
[complete status and forecast inventory](../experiments/theory/t158/CANDIDATE_SELECTION.md),
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


## E155 / T159A — time and provenance audit through T159

[Milestone audit](SUBMISSION_MILESTONE_TIME_AUDIT.md) sums 100.70 recorded task-session hours across
151 started tasks, with 115 timed (including two partial) and 36 untimed.
The explicit active-research subset is 41.81 hours, including 32.55 recorded
as theory/derivation. T129's 4.75 overlapping agent person-hours are separate.
All 17 successful algorithms receive copying/adaptation labels. ALG043 was
unchanged public V29; ALG049 adds local trace and arithmetic adaptations.
No new academic priority claim, estimator change, experiment or submission.
This audit updates the dated census; it does not rewrite historical evidence.
T160 remains proposed and unstarted.


## T160 update — empirical theory with a retained efficiency nominee

240.22active research minutes,97completed full-size predictions plus
small/generated/saved-state tests. No new challenge-target coefficient fits;
adaptive thresholds and offline tensor coefficient fits are explicit. No agents
or upload. The method remains predominantly equation-driven, with empirical
feedback used during derivation and selection.

```text
T160 recurrence
├── Native history efficiency
│   ├── Partial nonlinear interface + exact semilinear trace action
│   │   └── +young-source gate packing → eight-network nominee, adjusted−8.69%
│   ├── Aggressive/randomized/response-ranked interfaces → weaker or failed
│   └── Paired states / young bridges → tested large accuracy losses
├── Fourth-order structure
│   ├── Cheap source histories → mostly weak; corrected3+2cup modest reserve
│   ├── Exact pair slices → too costly; complete feedback still missing
│   └── H4-to-T3birth derived and checked → full coherent algorithm unbuilt
├── Positive quadratic-Gaussian law
│   ├── Generated small networks → useful gains over Gaussian closure
│   ├── Actual-width32latent state → far worse than incumbent
│   └── Distributed quadratic-atom representation → finite response/cost gap
├── Arithmetic → primitive savings fail to become a strong integrated gain
└── Harmonic-CP / weighted traces → diagnostic progress, recurrent route unbuilt
```

The larger branches continued for over two hours after the combined reserve's
first positive pair. No forced second nominee. [Report](../experiments/theory/t160/REPORT.md),
[forecasts](../experiments/theory/t160/CANDIDATE_SELECTION.md),
[continuation](../experiments/theory/t160/CONTINUATION.md).


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

## T163 update — 2026-09-23: a learned residual and continued larger-state research

**240.18 active research minutes**:119.71 derivation,83.64 empirical,
23.22 literature,13.61 selection. Category time is measured; exact route-hours
were not separately clocked. One task, no agents. Machine durations overlap
research and are not additional thinking time.

```text
ALG050 successor research (T163 / E159)
├── Learned physical-state response
│   ├── 52 marginal features → P41 reserve,2.91% development adjusted gain
│   ├── +72 pair features → P67 nominee,5.12% gain,12/12 wins
│   │   └── 32-network whole-network CV →3.89% raw gain; compact inference checked
│   └── Coupled/conditional/nonlinear families → inferior CV; no further tuning
├── Coherent fourth-state propagation
│   ├── Full state at width384 →35.0% raw gain vs public aug3 capacity control
│   ├── Shared128 at width384 →39.6% raw loss; transfer is a real gap
│   ├── Essential mixed loops / protected repeated slices → useful causal probes
│   └── Joint third/fourth representation
│       ├── Covariance-only / direct old-state queries → losses
│       └── Own-state basis + cheap response + one refinement → P79
│           └── width256 gain13.4% vs factored,7.2% vs dense third control
├── Cheap endpoint / covariance-square / NIG reserves → weak or cost-negative
└── Function-level / conditional controls → literature and cost constraints;
    no new end-to-end nominee
```

P67 is explicitly **our supervised learned adaptation**, with124 shared
coefficients and four ridge choices selected using whole-network folds. The
feature architecture and one-vector transport come from derivation. It is
neither a pure copy nor a proved new closure. Larger-state work was chiefly
algebra and cost derivation with adaptive basis/rank/omission experiments.
The 148 full-shape calls include120 feature-collection calls and28
prototype/candidate calls;41 generated recurrences have40 distinct source
hashes. Failed work and duplicateP53 remain recorded.

P67's subjective official-win forecast is90–95%, conditional gain2–6%.
The larger shared/source-aware route is15–30% within8–16 additional hours,
conditional gain10–30%; width transfer and complete constructor cost remain
unresolved. A small nominee did not terminate the larger investigation.
Proposed T164 reuses P67 evidence for an ordinary bounded submission attempt;
no upload occurred in T163. ALG050/submission331607 remains incumbent.
[Report](../experiments/theory/t163/REPORT.md),
[forecasts](../experiments/theory/t163/CANDIDATE_SELECTION.md),
[continuation](../experiments/theory/t163/CONTINUATION.md),
[timing](../experiments/theory/t163/TIMING.json).


## T164 — official attempt for T163 learned residual

Official submission 332018: adjusted 4.36851423131e-09, 3.87% lower than ALG050-V000. Retain ALG051-V000. Exact P67source, reused12-network development
evidence,5actual archive calls; no new fit/cohort. 36.83session minutes,
with overlapping prediction and external wait milestones recorded separately.
Our supervised learned adaptation of ALG050/publicV29. Larger fourth-state
construction and transfer remain unresolved; no field-exhaustion claim.
T165proposed only. [Result](../experiments/submission_policy/t164/REPORT.md),
[timing](../experiments/submission_policy/t164/TIMING.json).
