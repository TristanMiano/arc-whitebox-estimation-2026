# Neglected and incompletely tested tracks

**Later update, T132 (2026-09-06):** [route status](RESEARCH_ROUTE_STATUS.md)
now distinguishes search saturation, tested leaves and unexecuted reserves.
The [literature trial](../experiments/literature/t132/REPORT.md) recommends a
cheap public-estimator comparison next and retains a specific kernel-recombination
reference for output-aware compression. Historical forecasts below are preserved.

**T128B, 2026-09-05 Pacific / 2026-09-06 UTC.** A one-off review requested
before T129; no agents, candidate experiments or theory recurrence were started.
This supplements the [strategy map](RESEARCH_STRATEGY_MAP.md). It does not change
the protocol or authorize the trials described below.

There is real unfinished territory. The clearest cases are **T117's unselected
DS/M observers**, **RCERC**, and **uniform fixed-count suffix continuation**.
The records distinguish them from unsuccessful implementations. Other entries
are technically difficult reserves that received substantial mathematical
attention but little implementation work. They should not all be called
forgotten or insufficiently researched.

## Meaning of the probabilities

The following are **new subjective planning judgments against current
ALG031-V000**, not measured frequencies, bootstrap confidence or the older
slates' probabilities. Current official adjusted score is
`1.3618567538742354e-7`; its recorded score is 43.25% below ALG019's. An old
win over ALG019 or direct sampling is therefore substantially weaker evidence
for a present win.

- **P(useful lead):** within at most two active hours of focused review and
  mathematical work on that track, we identify a specific, materially distinct
  successor whose error/cost argument justifies one small production attempt.
  Merely recovering an old name, producing interesting equations, or finding
  another reason to reject it does not count as this positive event.
- **P(official gain):** starting from today, that review followed by at most
  one bounded implementation attempt (up to two active engineering hours,
  including any explicitly justified extension) and normal grading yields a
  retained official improvement over ALG031. Failure to produce a viable
  implementation counts as no gain. This is an unconditional probability,
  not conditional on the first column succeeding.

The intervals in parentheses are subjective plausible ranges for those
judgments, not statistical confidence intervals. They convey how easily the
ranking could change. Two hours is a common forecasting horizon for this audit,
not a new entitlement to spend two hours on every candidate. Current protocol
still starts with a 60-minute engineering budget and reassessment.

| Review rank | Track | Why attention may have stopped too early | P(useful lead) | P(official gain) |
|---:|---|---|---:|---:|
| 1 | Depth and transported-innovation observer features: DS/M | Positive older point results were excluded by a minimum-gain/sequential rule | **60%** (45–75%) | **30%** (15–45%) |
| 2 | Exact first-layer controls on the independent child: RCERC | Developed and corrected, then displaced by the two-candidate cap; no empirical rejection | **50%** (35–65%) | **20%** (10–35%) |
| 3 | Uniform fixed-count suffix continuation | A failed adaptive proposal overshadowed its stronger uniform control; a distinct-family rule blocked follow-up | **40%** (25–55%) | **15%** (5–25%) |
| 4 | Smooth gate-conditioned correction weights: KCAS | Specified but not implemented; later fits cover some nearby territory | **45%** (30–60%) | **20%** (10–30%) |
| 5 | Output-aware particle compression: BLMFC | Related response-space tests were unstable; this different compression estimator was never built | **30%** (15–45%) | **10%** (3–20%) |
| 6 | Compressed non-Gaussian hidden-state propagation | Early K3 had a shallow signal; trace approximations progressed, but the richer joint-state route remains untested | **30%** (15–45%) | **10%** (3–20%) |
| 7 | Symmetry-aware covariance acceleration with an explicit use for savings | Particle propagation was accelerated; the identified covariance-kernel opportunity remains a cost sketch | **35%** (20–50%) | **15%** (5–25%) |
| 8 | Reference-residual ensemble anchoring: CAMA/NCFA descendants | Raw anchoring failed; the later residual-based correction is mathematically different and untested | **20%** (10–35%) | **5%** (1–15%) |

This is a review priority balancing evidence, likely payoff, effort and breadth;
it is not sorted solely by either probability. In particular #3 gets priority
as a distinct, overlooked sampling mechanism. #1 and #4 are correlated local
fitting opportunities. The probabilities must not be added, or combined as
independent chances of success. These are chances of some improvement, not of
reaching the top of the leaderboard.

## 1. DS/M: the strongest concrete omission

**What happened.** T117 tested a nested observer ladder on 150 selection
networks. AS had raw MSE `1.766009462e-6`, DS `1.761641530e-6`, and M
`1.754334658e-6`. Relative to AS, DS was **0.2473% better** and M
**0.6611% better** in that selection comparison. DS missed the required
`2e-8` absolute incremental improvement. The sequential rule then made M
ineligible, even though M improved on DS on 132/150 networks. Only AS was
selected for the next panel and eventually shipped as ALG024.

The report explicitly calls DS favorable and strict-rule-limited. This is
selection evidence, not fresh confirmation for DS/M and not an official gain.
The old selected result remains valid; there is no need to rewrite its rules.

**Remaining territory.** DS contributes eight summaries of the frame/partial
error trajectory across depth. M adds four transported-innovation and two
bridge features. The current 22-column response design adds terminal physical
responses instead; it does not directly implement that omitted 14-column
history/transport block. Some predictive information may nevertheless overlap.

**Attention and assets.** One direct empirical task, T117, tested these rungs;
no complete DS/M successor on today's parent was found in the inspected record.
All **500 old training feature-cache files are still present**. This audit
checked filenames only. Their compatibility with current source semantics and
production numerics remains to be established; they are not automatically free
current-parent training data.

**Smallest useful revisit.** Reconcile the exact 14 omitted fields with the
current carrier and existing cache. If useful fields can be obtained cheaply,
nominate one anchored extension, fitted on declared training data and assessed
by the lean current submission rule. No six-rung/three-ridge repeat is needed.
Abandon the proposal if compatible feature generation dominates the likely gain
or the new fields are effectively redundant.

**Why only 30% for an official gain.** The original effect was small and
selected; the parent, coefficients and error distribution have improved since.
This is the best short-term cleanup opportunity, not the strongest structural
breakthrough hypothesis. **Flavor: small supervised fitting.**

Sources: [T117 results](../experiments/checkpoint3/t117/REPORT.md#s_o-nested-selection),
[26 feature definitions](../experiments/checkpoint3/t117/observer_family.py),
[T127 fit](../experiments/submission_policy/t127/fit.py),
[T122 intermediate-defect reserve](../experiments/theory/t122/SCRATCHPAD.md#17-transported-intermediate-mean-defects-cheap-arithmetic-missing-training-cache).

## 2. RCERC: a developed exact control that never got its turn

**What happened.** T119 developed low-rank combinations of first-layer
antipodal responses whose analytic mean and pair covariance are known. It
corrected an initially attractive symmetric learned construction after finding
an extra cross-leg variance term. The final learned version trains its response
on the main source and applies the centered control only to the independent
child; a deterministic analytic version can act on both sources. RCERC was
then displaced by COA-R and CGMA under the two-decision limit.

**Remaining territory.** This changes sampling error using an exactly centered
control, rather than learning another target-based terminal correction. The
child source is already paid for. Neither a failure of estimated-center
subframe controls nor T091's failed leverage weighting rejects this mechanism.

**Attention.** Substantial T119 derivation, including §§59–63 and the final
ranked slate; **zero dedicated empirical candidate tasks** found. This is
implementation-neglected, not theory-neglected.

**Smallest useful revisit.** Choose one rank-eight analytic or main-learned
control after checking its attainable reduction in the *complete* current
estimator and its actual dependencies. Preserve pair clustering, source
independence and the corrected insertion point. Do not implement all six old
arms. The historical symmetric learned draft is superseded; exact control
centering also does not prove variance reduction after the fitted head/clamp.

**Main risk.** The learned control affects only part of one sampling branch.
The old idealized 45.3% child variance share was a share of **frame variance**,
not of total estimator error. Deep gate decorrelation and today's fitted
corrections can leave little useful correlation. **Flavor: deduction and
within-input regression; an offline readout fit is optional, not intrinsic.**

Sources: [final T119 slate](../experiments/checkpoint3/t119/RANKED_SLATE.md#parked-reserve-1--rcerc),
[placement and variance ceiling](../experiments/checkpoint3/t119/THEORY_LEDGER.md#59-rcerc-placement-audit-preserve-the-exact-control-before-nonlinear-as),
[T119 disposition](../experiments/checkpoint3/t119/REPORT.md#parked-not-rejected).

## 3. Uniform continuation: a promising control buried under an adaptive loss

**What happened.** T083's optimistic continuation oracle gave a
variance-cost ratio of **0.8522** to direct sampling but missed a required
`<0.80` effect. T092 then tested adaptive fixed-count residual allocation.
The adaptive rule lost to uniform allocation at **1.0167×**. However, the
uniform control was **0.6197× equal-work direct** in the conditional
finite-population proxy. T093 explicitly declined to select uniform
continuation because it would repeat a family when a different-family attempt
was mandatory. That is a documented scheduling restriction, not a rejection
of uniform continuation.

**Remaining territory.** Evaluate a cheap affine suffix on every shared prefix
and calculate the exact nonlinear residual on a fixed uniform subset of paired
paths. This preserves the residual expectation when constructed correctly.
The uniform law avoids the untransferred adaptive risk predictor.

**Attention.** Two related support experiments, T083 and T092, totaling about **41
minutes of recorded task sessions**; no complete
current-shape uniform-continuation submission test found. Later failed
multilevel/survival constructions are relatives, not the same fixed-count rule.

**Smallest useful revisit.** Audit a single-cut, fixed-count construction,
including randomness of the original particle cloud, residual selection,
setup and the interaction with current source moments. Establish whether the
old conditional proxy omitted enough variance or cost to erase the apparent
saving. If it survives, nominate one current-shape attempt, rather than
repeating a cut/count grid.

**Main risk.** The old tests used width 64/depth 32, while the present task is
width 1024/depth 16. The proxy is not a complete score against ALG031; the
current structured sampler, fast propagation and closure blend create a much
harder baseline. The `0.6197` figure is **not** a forecast of 38% leaderboard
improvement. **Flavor: deduction and sampling design; no training-target fit
is essential.**

Sources: [T083](../experiments/checkpoint3/t083/REPORT.md),
[T092 retained uniform signal](../experiments/checkpoint3/t092/REPORT.md#retained-positive-evidence),
[T093's explicit scheduling exclusion](../experiments/checkpoint3/t093/REPORT.md#reconciliation-of-t091-through-t092).

## 4. KCAS: smooth coefficients on existing physical discrepancies

T119 specified bounded gate-polynomial interactions with four existing
physical discrepancy fields. The question was whether correction weights
should vary smoothly with signed distance to a ReLU gate, rather than rely
on constant coefficients and a few coarse masks. It was parked behind the
selected pair; no dedicated implementation/test was found.

This is not wholly untouched territory: ALG019 had conditional fusion, AS had
alpha contrasts, and T127 adds parity-sensitive responses. A current KCAS
proposal must identify an interaction genuinely outside that span. The old
24-column definition is a starting point for inspection, not a prescription
to append 24 columns blindly.

The smallest useful step is a formula/cache overlap check, then one fixed
anchored fit if meaningful capacity remains. No new neural model, learned
knots or polynomial-degree search is needed. The expected upside is modest
and shares failure risks with #1. **Flavor: supervised varying-coefficient
regression; the most explicitly ML-like track on this list.**

Source: [T119 §46](../experiments/checkpoint3/t119/THEORY_LEDGER.md#46-low-cost-observer-lane-kink-conditioned-analytic-synthesis).
The old instruction there to fit across all public networks is historical;
any new fit follows current declared training/data roles and preserves the
current final-blind policy.

## 5. BLMFC: spend particle work only where it affects the output

T116 proposed retaining hidden coordinates according to estimated final-output
sensitivity, folding omitted means into the next layer. A cheap backward
recursion estimates which activation fluctuations matter. Its illustrative
22% saving applied only to the affected particle-propagation subgraph, not
the whole estimator. This route was not implemented.

The adverse evidence is substantial but narrower than this proposal: T023/24
lost with their integrated activation classification, and T114 found
probe-unstable response subspaces. Neither tested this mean-folded,
output-weighted particle algorithm. Conversely, those failures are reasons
to distrust a convenient low-rank or diagonal approximation, not reasons to
assume an untested compression will work.

A useful review would produce one concrete late-layer compression rule and
an error-versus-saved-work argument that includes omitted covariance and gate
changes. Prefer a controlled late suffix to a whole-network rewrite. Savings
must fund a stated benefit, such as more useful independent samples, to lower
score while already on the .1 multiplier floor. A stable inexpensive response
proxy is the first uncertainty, not the optimal pruning percentage.

**Attention:** a T116 reserve/refinement and related T114 negative evidence;
zero complete BLMFC tests found. **Flavor: structural approximation and
numerical algorithms, with empirical allocation later.**

Sources: [T116 BLMFC](../experiments/checkpoint3/t116/THEORY_LEDGER.md#avenue-d--backward-leverage-mean-folded-compression-blmfc),
[T116 refinement](../experiments/checkpoint3/t116/THEORY_LEDGER.md#blmfc-refinement-a-floor-compatible-backward-leverage-recursion),
[T114 probe instability](../experiments/checkpoint3/t114/REPORT.md#qualification-and-implementation-risk-audit).

## 6. Joint non-Gaussian propagation beyond trace/diagonal corrections

This family has a long history: T017's shallow K3 signal, the unselected
compressed-suffix `H073-C`, T110's trace/diagonal work, T116's tensor sketch,
and T119's positive Gaussian-mixture assimilation (CGMA). It has received
considerable theory; calling the entire family forgotten would be false.
Trace-related descendants were tested, and part of their benefit already
reached ALG028/29/31. T120 also revisited late TD. Those are not unopened
opportunities merely because an older checkbox remains incomplete.

The remaining question is **whether a small joint non-Gaussian state can be
transported through a layer cheaply enough**, preserving output-relevant
shape that trace/diagonal closure misses. Possible representations include
an output-weighted compressed cubic or a small positive mixture. They are
alternatives within one broad track, not independent chances to add together.

A useful two-hour investigation would choose one representation and settle
its decisive approximation, Gaussian-null and charged-cost obstruction. It
would not start the old six-to-twelve-hour CGMA implementation. T122 corrected
two scalar claims in that specification; T126 showed that a naive norm-based
scale mixture creates spurious non-Gaussianity even from Gaussian input.
Any proposal must use the corrected analysis. Matching finitely many moments
also cannot universally guarantee the required ReLU mean.

**Attention:** shallow and restricted descendants tested; no complete richer
joint-state candidate demonstrated on the current parent. **Flavor:
mathematical approximation and tensor/mixture design; source-moment estimation
and a small optional fitted readout.** Its potential upside is larger than a
few extra observer columns, but implementation risk makes its bounded official
win probability low.

Sources: [H073-C](../experiments/checkpoint3/t073/NOVELTY_SLATE.json),
[T110's actual scope](../experiments/checkpoint3/t110/REPORT.md#what-happened-to-the-proposed-td-mechanism),
[T119 CGMA](../experiments/checkpoint3/t119/RANKED_SLATE.md#decision-2--cgma),
[T122 corrections and simplified assimilation](../experiments/theory/t122/SCRATCHPAD.md),
[T126 limitations](../experiments/theory/t126/REPORT.md).

## 7. Covariance acceleration that earns a score benefit

T118 successfully accelerated particle propagation. T126 identified a
separate opportunity in symmetric covariance congruences: combine one fast
product with only the required triangular output panels. No production
realization of that new kernel was found. Earlier generic compute-optimization
TODOs were deferred, but that does not mean the whole project lacks
optimization; much of it is already implemented.

This review must start from the current symmetry-aware cost, not compare
against two unnecessarily generic dense products. T126 showed that a simple
two-fast-product replacement does not automatically bring R3 under the floor.
It also identified residual-time and numerical-stability risks.

The next useful result is one fully charged operation plan **plus a specific
use for its savings**: fund an accuracy mechanism, or make a previously
useful but more expensive composition competitive. A faster estimator with
identical error and the same .1 multiplier has no direct score improvement.
The old R3 raw gain is not an available 14% margin after charging its real
cost, and its old contract stays parked.

**Flavor: numerical algorithm engineering and cost deduction; no coefficient
fit required for the kernel.** This may be a short engineering investigation
rather than the best use of every theory agent.

Source: [T126 covariance-cost audit](../experiments/theory/t126/SCRATCHPAD.md#13-covariance-acceleration-does-not-make-the-old-r3-cost-problem-disappear--2250-utc).

## 8. Residual ensemble anchors after the failed raw anchor

T116's unit norm anchor was badly harmful, with risk ratio 28.05; fitting its
strength made it nearly neutral. That is real negative evidence. An identity
averaged over fresh output weights is not an exact constraint on this
network's realized output columns. CAMA added a kernel-based second-moment
identity but remained an untested reserve with the same finite-column issue.

T126 described a materially different route: preserve a reference's realized
coordinate structure and anchor only its residual against an ensemble
reference. This can remove some of the unwanted variation that defeated the
raw anchor. The corrected residual route has not been tested. Required
penultimate norms and accurate reference norms are not already supplied by
the current terminal-only cache.

The useful first step is to determine whether the reference subtraction can
make finite-column noise smaller than the correctable residual error. If not,
stop without collecting the new statistics. If yes, nominate one heavily
shrunk residual control. Do not retry a unit population-moment snap.

**Flavor: deduction/empirical-Bayes reasoning plus a possible tiny fit.** The
prior stays low because the failed ancestor and the small remaining common
bias both argue against a large payoff.

Sources: [T116 anchor analysis](../experiments/checkpoint3/t116/THEORY_LEDGER.md#cama-population-truth-is-a-noisy-target-for-the-realized-columns),
[T126 residual reformulation](../experiments/theory/t126/SCRATCHPAD.md#15-a-corrected-ensemble-anchor-must-preserve-the-query-specific-reference--22532256-utc).

## Things that should not be mislabeled neglected wins

- **T035–T037's unchecked training/feature/correction tasks:** much of their
  substance was completed through T117 and later fits. A stale checkbox is
  not evidence of unexplored learning capacity.
- **Late TD and HTTS trace:** incomplete early disposition does not erase
  T120 and the shipped trace descendants. Only the remaining richer joint
  action is open; scalar K4 and the one-direction T128 shape variant have
  actual negative evidence.
- **Complementary-frame covariance cancellation and affine-residual
  rebranding:** algebraically closed mechanisms. A looser score rule cannot
  restore the claimed effect.
- **Learned adaptive suffix weights, inverse-survival telescopes, small
  subframe estimated-center controls and fixed active rotations:** actual
  negative results survive. The uniform-continuation entry does not reopen
  those variants.
- **RLCE exact line integration:** no empirical test, but an explicit
  breakpoint-growth cost obstruction. I put it below the top eight: roughly
  10% chance of a useful lead and 2% of a bounded official gain under the
  definitions above. A new compression/conditioning identity would be needed
  before enumeration is attractive.
- **Sign-Walsh sketches, kink-energy importance sampling, pilot-routed
  frame/Sobol mixtures:** named but lightly tested or untested reserves exist
  in the early slates. They lack the positive clue of #1/#3 or the developed
  current-parent construction of #2; their old priority closures were not
  scientific falsifications. They remain secondary leads, with directional
  transfer, density tails and pilot overhead unresolved.

## A possible one-time agent trial

I would give a first wave **three different mathematical questions**, rather
than ask every agent for a general list of better algorithms:

| Assignment | Track | Concrete deliverable within 60–90 active minutes |
|---|---|---|
| Agent A | #2 RCERC | One corrected rank-eight control, its insertion into ALG031, attainable complete-risk benefit and counted dependencies; reject it if the remaining correlation/cost is inadequate |
| Agent B | #3 uniform continuation | Reconcile the T092 proxy with full estimator variance and setup cost; derive one fixed-count, single-cut current-shape design or explain precisely why the old signal will not transfer |
| Agent C | #5 output-aware compression | A stable cheap response rule for one late compressed suffix, including omitted fluctuation/gate error and what useful work its savings buy; avoid a pruning grid |
| Main agent | #1 cleanup plus integration | Reconcile the retained DS/M cache and current features, check duplication across proposals, challenge the assumptions, and rank zero to two actual next attempts |

These are proposed briefs only; no agents were launched. #4 shares too much
with #1 to merit another agent in the first wave. #6 is the alternative third
assignment if the owner prefers a higher-risk joint-distribution investigation
over compression. That substitution should replace an assignment, not add an
unbounded second wave. #7 can be a focused engineering option if the preceding
cost arguments make it decisive.

All agents would start from the same incumbent and these corrected failure
boundaries, write separate scratchpads, and avoid candidate execution or shared
live-state edits. Their deliverables should make a decision possible without
requiring the main agent to redo each investigation. The main agent should
compare the strongest ideas; a unanimous vote is not a requirement.

Parallelism trades calendar time for more total model work. Three hour-long
investigations plus the main agent's own review/integration are several agent-
hours, not one hour of total effort. I would judge a single trial by whether it
produces a stronger, cheaper-to-test survivor than the ordinary recurrence.
Any choice to use Ultra can be evaluated as part of that trial; this audit
provides no evidence that a higher setting will necessarily repay its usage.
No exact token/usage multiplier is inferred from these wall-clock budgets.

This is a **one-time trial proposal**, not a standing process change. Keep the
existing small-test/official-feedback loop, and decide whether to repeat the
agent approach only after seeing the quality of its first results.

## Audit provenance

The review inspected the early novelty slates, later ranked reserves, decisive
negative/positive reports, current fit definitions, and relevant T122/T126
scratchpad passages. It searched for later dispositions rather than treating
the first rejection label as final family-wide evidence. It did not reread
every page of the chronological notebooks or establish absence of every
possible prototype file.

The [evidence inventory](../experiments/protocol/t128b/EVIDENCE_INVENTORY.json)
records source hashes, the metadata-only cache-presence check and arithmetic
from reported results. The [ranked data](../experiments/protocol/t128b/TRACKS.json)
preserves probability definitions, ranges and agent briefs for a future run.
The [task record](../experiments/protocol/t128b/REPORT.md) records scope and time.
All proposed probabilities and implementation choices are prospective; no new
performance evidence was generated.


## T129 follow-up — evidence scope and final priority, 2026-09-06 UTC

The original table above is preserved as a dated forecast. Its RCERC phrase
**“no empirical rejection” was too broad**: the exact T119 spelling was
unexecuted, but H107-L/M were materially relevant losing predecessors. T129
derived a specific harmonic repair and a separate fitting-noise repair rather
than treating the family as empirically untouched.

The three-agent trial is now complete. Root also reviewed DS/M, KCAS and
ensemble anchors. The final nominees are **PF1760 first, FC4S second if still
worthwhile**, with subjective unconditional official-win priors35% and25%.
The first-layer Gram shortcut made the full-output shape field quicker to try
than the more involved R4IF8-P control. That control is fully specified as a
reserve; it has not lost a new experiment. Historical DS positives remain,
while some simple transport information is already in the current head.

Uniform continuation's old conditional proxy omitted source-bank error; its
review uncovered a useful exact-compute offshoot without proving the original
uniform method wins. The all-output curvature proposal also still has genuine
approximation error. No track probabilities are empirically calibrated by
these theory results, and no new candidate was run. [Full findings, timing and
changed priorities](../experiments/theory/t129/REPORT.md) and
[reserve conditions](../experiments/theory/t129/RESERVES.md).

This trial does not enshrine a new protocol. The existing small-test and
official-feedback loop remains the prospective execution route.
