# Submission-focused research loop

**Effective:** 2026-09-04, T123, by the owner's direction after T120B.
**Research amendment:** 2026-09-11, T156; experiments during derivations and
increased active research floors.
**Policy mirror:** [competitive_research_policy.json](../state/competitive_research_policy.json).
**Current algorithm and route:** [current_state.json](../state/current_state.json)
and the active queue in [TODO.md](../TODO.md).

This is the governing prospective workflow. Earlier task specifications and
results remain historical evidence. They do not impose their scientific gates
on a new submission attempt. The owner's latest explicit instruction controls.

## Objective and priorities

Optimize expected improvement in the actual official adjusted score per
remaining hour. Official submissions are an intended source of feedback once
we have reasonable evidence that a lawful candidate will help. Roughly **90%
confidence of improvement is enough**; do not seek publication-level certainty
before submitting.

For each serious option, estimate the probability of a successful compliant
submission, plausible score improvement, and total remaining time: theory,
implementation, local runs, qualification, likely repairs, and grader waiting.
Use ranges and evidence, not a compulsory 100-point rubric or invented precise
priors. A useful ranking aid is:

`expected retained official score reduction / expected remaining hours`.

Retained reduction accounts for keeping the best submission if an attempt
loses. Consider a small, readily deployable improvement alongside a more
ambitious idea. Sunk work and a reserved position in a queue do not justify
continued investment. Re-rank after every meaningful result or cost discovery.
Academic novelty is recorded separately and does not bar a score submission.

**Standing larger-upside preference (owner direction, 2026-09-08):** during
research, if a cheap candidate worth testing appears alongside a credible
thread offering substantially greater score reduction, record the cheap option
and prefer developing the larger opportunity. Finding a ready candidate does
not itself end a recurrence. Balance plausible gain, success probability,
remaining work and information value; keep cheap candidates as fallbacks and
re-rank as evidence changes. Small improvements remain worthwhile choices.
This preference adds no minimum submission gain, extra evidence gate or
automatic budget extension. Once a submission task is selected, use the lean
screen and prompt official feedback below. The preference remains in force
until the owner revisits it; task-specific research durations remain separate.

**Owner correction after T148 (2026-09-11):** preserve the balance in the final
selection as well as during derivations. Do not repeatedly park an ambitious
route merely because the smaller candidate is easier to finish or more likely
to win. Use the uncertainty and possible size of the payoff; a speculative
midpoint calculation of gain per hour is not a veto on exploration. Prefer a
concrete, explicitly approximate test over indefinite completeness work when
the omitted terms need not prevent useful feedback. The roughly90% local
submission screen applies after implementation, not to the research prior.
When comparing an ambitious option and a fallback, state their untested status,
subjective success probabilities, conditional gains and expected retained gains.
These estimates guide judgment; they add no fixed risk quota or testing gate.

## One bounded task at a time

The default is one owner-authorized TODO task, then a result and a stop. A
candidate task may include implementation, lean screening, packaging and an
already-authorized upload. If upload is not yet authorized, finish the concrete
package and put its upload task next; asking to execute that task authorizes
upload and bounded monitoring. Do not ask again for authority already supplied.

A theory recurrence can nominate **zero, one or two** candidate decisions.
This limits final nominees, not hypotheses, exploratory variants or small
experiments within the recurrence. Those nominees are options, not mandatory
errands. Return to theory early whenever the
remaining slate looks less useful than another hour of mathematical work.
Parked tasks are outside the active queue and cannot block the next task.

Estimate runtime before starting. Default to a **60-active-minute engineering
budget per candidate attempt**, with a reassessment around 30 minutes. Count
coding, debugging, local execution that requires attention, and recordkeeping;
report unattended compute and grader waiting separately, but include both in
expected total time. This is a ceiling for planning, not time to fill. Before
extending, record a finite additional budget and a concrete likely payoff;
otherwise park the branch. A larger task explicitly authorized by the owner
uses its stated budget. Avoid multi-hour implementations on an old forecast.
Training-data generation, fitting and cache construction belong in the same
size/time estimate; a small comparison does not justify an unbounded training
corpus. Reuse existing primitives and generate only the additional data needed
for the proposed decision.

## Minimum useful submission evidence

1. **Freeze the candidate and question.** Briefly record the estimator delta,
   fixed coefficients/assets/seeds, comparator, cohort, actual scoring rule,
   initial work budget and decision rule. Register a material variant before
   running it. Read relevant prior failures; do not recreate a negated identity.
2. **Check production feasibility early.** Prefer the actual Python/Whest
   estimator path for submission work. Meter an integrated full-shape fixture
   before generating a large cache. Reuse audited primitives and existing
   qualification. Run a separate mechanism test only if it can cheaply change
   the decision; ablations and native reimplementations are not routine gates.
3. **Run one small paired comparison.** For a new candidate, normally start
   with **12 predetermined current-shape networks**. Compare arithmetic mean
   adjusted final-layer score against the deployable incumbent on the same
   networks. This is a default, not a mandatory minimum when existing sealed
   evidence already answers the question. A packaging-only change may need
   only a numerical/contract replay. Do not repeat a 250-network experiment to
   requalify an unchanged formula.
4. **Decide with roughly 90% support.** A lower adjusted mean and about `.90`
   whole-network bootstrap support normally justify submission, after the
   operational checks below. Report raw and adjusted means, actual cost and
   multiplier, sample count, wins, an uncertainty summary and the worst tail.
   Bootstrap support is a screening diagnostic, not a calibrated probability
   of winning the private evaluation. Previously comparable evidence can
   inform the decision; explain any judgment around the approximate threshold.
   A point win alone is a lead, not proof that the candidate should be shipped.
5. **Stop spending once the decision is clear.** No additional 95%/99%
   confidence threshold, minimum percentage gain, two-sided interval excluding
   zero, universal tail-ratio cutoff, mechanism separation, or M1/P1/R1/P2 gate
   is added to the score screen. Account for observed tails in expected score;
   investigate a concrete unexplained catastrophic failure, not every ordinary
   losing network. If evidence is unclear, use at most one decision-relevant
   extension, normally to **24 total networks**, preferably planned before the
   first look. Disclose repeat looks. If the extra run is unlikely to change
   the action, park or return to theory instead. Larger studies require a
   separately justified task; never keep extending until the screen passes.
6. **Package and obtain official feedback promptly.** A supported improvement
   becomes the submission candidate. Announce that result in bold and qualify
   the concrete archive. Submit within existing authority; otherwise make its
   authorized-upload task the immediate next action. A local screen, an
   official score and a scientific mechanism claim remain distinct evidence.

Use public inputs and permitted development targets. For the submission-facing
comparison, freeze the selected candidate and seal predictions before the
scoring pass; disclose any earlier target exposure. Exploratory research may
inspect and reuse declared development targets during iteration as described
below. Do not fit on a block labeled frozen validation or describe
reused/adaptively selected data as fresh confirmation.
New fits belong to declared training/development data. Cheap production checks
may reuse existing panels if that role is explicit. Keep the final local blind
block sealed unless its separately planned use is authorized.

## Operational checks that remain required

Use the current official contract and scoring implementation. Currently the
adjusted multiplier is `max(.1, FLOPs / 2**41)`; `.1` is a discount floor,
not an eligibility limit. Score additional compute honestly. The actual caps
are FLOPs `<=2**41`, residual time below `.4s`, prediction wall time below
`120s`, setup below `5s`, and memory below `8 GiB`, with valid finite full-shape
outputs and the candidate's declared fallback behavior. Recheck official
requirements when versions or rules change; see
[the rules audit](SUBMISSION_RIGOR_AUDIT_2026-08-25.md).

Submission numerical work must use allowed accounting APIs. No raw-array escape,
hidden grader state, timing-based evasion or unaccounted numerical computation.
Retain the immutable archive hash, allowed-import/manifest validation, a clean
extraction, deterministic replay of the current shipped design, and the
relevant fallback checks. Reuse earlier checks when the affected behavior and
environment are unchanged. Do not add a consecutive-clean-run streak or a
fresh multi-platform campaign. Use the environment with relevant passing
evidence; the current submission path has qualified on WSL/Linux.

Historical cross-environment byte equality is separate from current-package
determinism. Preserve historical seals and record a production version, the
source of numerical differences, and a justified equivalence tolerance before
its comparison. Bound the error relative to the expected score gain and check
the actual executable score. A materially changed formula or coefficient fit
needs a newly frozen variant. Never call a failed old byte/cost contract passed
by silently rewriting it; a prospective submission contract can be different.

## Official feedback and recovery

Allow **60 minutes per submission attempt**, measured from acceptance, and at
most **one unchanged-package retry** for a generic evaluator failure or timeout.
Record the submission ID immediately. Preserve the first result, recheck the
exact archive, cancel a timed-out job if a supported action permits it, and
avoid an unbounded duplicate queue. The60-minute default was set by the owner
during T161 (2026-09-20UTC), replacing30 minutes for current and future attempts.
A diagnosed candidate defect gets a bounded
repair with a new package identity and affected checks; a poor valid score
gets a research decision, not an unchanged resubmission.

A successful better grade replaces the official best and is announced in bold.
A worse grade preserves the incumbent and informs the next hypothesis. A
failure or timeout is an operational result, not proof against the mechanism.
At the bounded endpoint, document the exact state and next action. An explicitly
bounded attempt can be complete even if it fails; never claim an unperformed
upload, missing grade, or unfinished deliverable succeeded. No final submission
designation is inferred from an ordinary upload.

## Theory recurrence

When the queue is unpromising or its next implementation is poor value, choose
a dedicated research task. **Numerous small experiments are authorized during
the derivations**, under the owner's T156 change. Work in repeated cycles of
derivation, experiment, interpretation and revision. Seek feedback early and
whenever it can resolve an uncertainty; a complete specification or high
probability of a win is not needed to test a research hypothesis.

Useful probes include generated counterexamples, toy or reduced-shape systems,
saved-output analysis, internal-state traces, partial prototypes, targeted
ablations, parameter/rank sensitivities and small full-shape development runs.
Use a few networks when that answers the question (often1–4); this is an
example, not a minimum or maximum. A few minutes per probe is a useful starting
scale, not a hard timeout. Do not impose a fixed probe-count limit, a compulsory
12-network panel, a two-variant limit or the roughly90% submission threshold.
The default60-minute implementation budget belongs to a submission attempt,
not a fresh allowance or approval gate for each research micro-experiment.

Manage the task's cumulative compute and elapsed time, not just each run's
size. Reuse inputs and passing machinery, batch cheap related probes, and work
on derivations while runs execute. After feedback, choose the next probe for
what it could teach. Discard an uninformative implementation without declaring
its entire family exhausted. Large sweeps, corpus generation or an expanding
training campaign require a deliberate finite rescope; a collection of small
runs should not silently become one. Targeted adaptive comparisons and changes
are ordinary authorized research, including for ambitious low-probability ideas.

Keep one scratchpad and a lightweight experiment log. Before a run or small
batch, record its question, local ID, code/version, chosen inputs/seeds and
comparator; preserve enough executed source/configuration and raw output to
reproduce it. A batch entry can cover multiple declared variants. Afterward,
record the observation and how it changes the derivation or next action.
New adaptive variants receive new local labels. A full ALG registry, polished
candidate specification, package, formal gate or separate owner approval is
not required per exploratory probe. Register/freeze a selected candidate in
the usual way before its submission-facing comparison.

Explicitly label data used for iteration as exploratory development. Targets
may be inspected repeatedly there and may guide hypotheses or targeted fits;
record that use and preserve earlier results. Frozen validation and the final
blind block keep their existing roles. Reused or adaptively selected outputs
do not become fresh confirmation. A promising probe is a research lead; use
the lean submission process to decide whether the selected complete estimator
merits official feedback. This permission adds no automatic upload authority.
Standalone mathematical/reference experiments may use ordinary research tools;
production resource claims require the actual metered Python/Whest path and
the shipped estimator must obey all numerical/accounting constraints.

### Increased floors and time accounting

The default recurrence floor rises from60 to **120 active research minutes**,
with **at least60 minutes of written equations and derivations** preserved.
Use the extra time for empirical design, small-prototype implementation,
active execution/debugging and interpretation, alongside literature and
selection. If additional probes cease to be informative, use the remaining
research time for substantive derivation/synthesis; there is no run-count quota
or requirement to manufacture experiments to fill time. Larger task-specific
mathematics/literature/selection floors remain in force.

For the next proposed **T153**, increase the active total from180 to
**240 minutes**: retain120 derivation,30 focused literature and30 selection,
and add60 for empirical research interleaved throughout. This added empirical
allocation can become further substantive derivation if that is more useful;
the240-minute total and existing component minima remain. Plan roughly
240–300 elapsed minutes, with longer productive work allowed. The owner
requested increased floors; these numerical allocations implement that request.
T153 still requires owner selection to start.

Track actual derivation, empirical work, literature, selection and passive
compute separately. Count overlapping wall-clock minutes only once. Writing
mathematics while a probe runs can satisfy the mathematics floor; the same
minutes cannot also be credited as empirical time. Passive compute/grader
waiting, ordinary packaging and routine administration satisfy no research
floor. Prototype coding and result interpretation count as empirical research,
not automatically as written mathematics. Continue longer when productive;
only the owner can shorten the applicable floor.

Develop distinct mechanisms without a quota of ideas or equations. Record why
each useful alternative could reduce final error, its charged cost, plausible
gain and uncertainty, and what the probes did or did not establish. Do a focused
duplicate/prior-art check. End with zero to two ranked nominees and a route
decision; no nominee is compulsory. If a cheap candidate emerges early, retain
it and develop a credible larger-upside thread with the remaining research
time. The minimum applies to theory recurrences, not every repair, protocol
edit, diagnosis or submission task.

## T132 literature-first trial, 2026-09-06

The owner authorized one bounded external literature task before choosing the
next recurrence, with internet access. Prioritize reusable algorithms and better
submissions regardless of academic novelty. The task's 90-minute ceiling is not
a minimum, and its time does not satisfy a future theory minimum. A directly
usable method can lead to a separately selected implementation task.

Reuse the [literature index](LITERATURE_INDEX.md) and update the
[route tracker](RESEARCH_ROUTE_STATUS.md) when evidence materially changes a
route: search saturation, implementation status, marginal value of more work,
and a concrete reopening condition. A failed leaf does not exhaust its family.
Record subsequent tests/grades so the search's return can eventually be judged.
This is a trial, not a permanent mandatory survey or an additional evidence gate.

## Optional science and concise records

Full scientific validation requires a separate, explicitly chosen task with a
specific theorem, mechanism, write-up or final-selection question and a finite
budget. It is not automatically triggered by a local win, official grade,
near-top score, novelty label or final-candidate status. The optional
[scientific reference](SCIENTIFIC_RESEARCH_PROTOCOL.md) preserves the old
procedures and labels. Apply only the procedures needed for the stated claim.

Normally produce one task record with source/package identity, command and
cohort, compact result and failure explanation, decision, timing and next step.
Append one experiment event and update the candidate's ledger entry when
applicable. Keep live state in `state/current_state.json` and the active TODO;
other entry points link to them. Historical freezes, raw evidence and completed
results are immutable. Do not duplicate a full narrative across every policy
file or run old scientific verification suites for a documentation change.
