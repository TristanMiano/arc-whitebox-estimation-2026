# Research and submission evidence

The default workflow is the [submission-focused research loop](docs/COMPETITIVE_RESEARCH_LOOP.md).
Its goal is enough evidence to make a good official submission decision,
normally around 90% support, with little local work. One small comparison and
the required production checks usually suffice. Official grading supplies the
next feedback; no scientific tier is required first.

## Data roles and identity

For a submission-facing test, record the candidate delta, fixed
coefficients/assets/seeds, data roles, comparator, scoring rule and budget.
Compare the actual shipped design with the current deployable incumbent on
identical networks. Seal predictions before the scoring pass and disclose
earlier exposure to the comparison targets.

- Training/development data may support fitting when that use is explicit.
- A frozen validation block is not a tuning set. After observing it, preserve
  the original result and use a new variant/data plan for adaptive changes.
- Reused panels can provide development or production-equivalence evidence.
  Do not call them fresh independent confirmation.
- Keep the final local blind block sealed until a separately authorized plan
  calls for it. It is not needed for routine official feedback.

During a research recurrence, numerous small experiments may be interleaved
with derivations. Declare an exploratory development role before using data
for iteration; targets may then be inspected repeatedly to revise hypotheses,
partial prototypes and targeted parameter comparisons. A concise scratchpad
or batch entry with a local probe ID, question, code/configuration, inputs and
comparator suffices before execution. Preserve the executed version and output,
then note what was learned. Adaptive changes receive new local labels; full
algorithm-registration paperwork is unnecessary for every micro-run. No fixed
number of probes or90% confidence threshold applies to exploration.

Search prior work before duplicating a material idea. Register and freeze the
selected ALG variant before its submission-facing comparison. Research
selection and repeated target use must be disclosed; do not call them fresh
validation or continue testing solely to cross a confidence threshold. Keep
historical source, sealed arrays and results intact. A changed production
realization gets its own recorded identity and equivalence assessment. Exact
current-package replay does not imply bit equality across older environments.
The [recurrence policy](docs/COMPETITIVE_RESEARCH_LOOP.md#theory-recurrence)
defines the increased time floors and cumulative experiment budgeting.

## Minimum useful report

Use arithmetic mean adjusted final-layer score, actual cost and multiplier.
Include the paired raw mean, network count, wins, an uncertainty summary,
worst-network behavior, operational failures and source/package identity.
Report known tails honestly and relate them to expected score. A usual losing
network or a two-sided interval crossing zero does not itself ban submission.

A whole-network bootstrap is one inexpensive diagnostic for the approximate
90% decision target. It is not a calibrated posterior probability of beating
the private suite. Disclose cohort reuse, candidate selection and repeat looks;
do not buy apparent certainty by testing repeatedly until a threshold passes.
Prior comparable evidence can reduce the need for new runs.

Keep the decision clear: submit, one bounded additional check, park, close the
unchanged competitive branch, or return to theory. Explain the actual blocker
and the smallest useful next action. An unresolved interval is not a scientific
rejection; a packaging failure is not an accuracy result. Preserve useful
mechanism evidence even when a particular implementation is uncompetitive.

## Optional scientific claims

M1, P1, R1 and P2 describe scientific evidence, separately from novelty and
submission readiness. They are not automatic steps of this workflow. A grade
does not establish a mechanism, and a missing tier does not prevent upload.

For a separately chosen scientific task, define the exact claim and only the
validation necessary to support it. The historical procedures, effect floors,
multiple-testing rules and native execution contracts remain available in
[SCIENTIFIC_RESEARCH_PROTOCOL.md](docs/SCIENTIFIC_RESEARCH_PROTOCOL.md). They
apply to their historical claims or a new explicit scientific plan, not by
inheritance to every future estimator. Full rigor has no automatic trigger.

## Durable records

A task normally needs one compact specification/result with linked raw output,
reproduction command, identity, decision and timing. Append the event to
`state/experiments.csv`; update the applicable algorithm entry, live state and
active TODO. Policy-only work needs no candidate ID, prediction run or new
scientific tier. Historical completed tasks and freezes remain available in
[the pre-T123 snapshot](experiments/protocol/t123/before/).
