# Start here

Read these in order:

1. [Live state](state/current_state.json): current official best and next task.
2. [TODO active queue](TODO.md): execute one owner-authorized task; parked and
   historical tasks are not next merely because their boxes are unchecked.
3. [Submission-focused workflow](docs/COMPETITIVE_RESEARCH_LOOP.md): roughly
   90% support is sufficient to try a compliant candidate; keep local work small.
4. The relevant candidate's specification and result, and the needed portion
   of [the algorithm ledger](ALGORITHM_LEDGER.md).

Consult [owner directives](docs/OWNER_OPERATING_DIRECTIVES.md) for authority,
theory duration and the 60-minute wait per submission attempt. Use
[RESEARCH_PROTOCOL.md](RESEARCH_PROTOCOL.md) for data/identity rules. The
[scientific reference](docs/SCIENTIFIC_RESEARCH_PROTOCOL.md) is optional and
cannot impose its historical funnel on ordinary submission work.

The official best is **ALG058-V001**, submission **336809**,
adjusted **2.97110640613e-09** (28.50% below the pre-T172 ALG053).

**T173 is complete:** final selection recommends **336809 / ALG058-V001**
and **336785 / ALG055-V000**. Current grades and exact accepted archives
were verified. The complete writeup draft for336809 is ready for Tristan
Miano's review: [PDF](experiments/finalization/t173/writeup/arc-whestbench-phase2-336809-draft.pdf),
[editable source](experiments/finalization/t173/writeup/main.tex),
[selection](experiments/finalization/t173/FINAL_SELECTION.md),
[task report](experiments/finalization/t173/REPORT.md).
No final nominations or writeup delivery have been performed. Proposed T174
is author review, final nominations and delivery; do not start automatically.

**T172 is complete:** 252.69 active work minutes, 296.74 elapsed, and
three official improvements. The retained score is 28.50% below the
starting ALG053 score.
[Report](experiments/theory/t172/REPORT.md),
[timing](experiments/theory/t172/TIMING.json).

The [T170 recurrence](experiments/theory/t170/REPORT.md) completed240.17 active
minutes. Larger compression repairs and conditional heads failed their tested
forms; untested routes and scoped forecasts remain in its
[candidate inventory](experiments/theory/t170/CANDIDATE_SELECTION.md).

The final recurrence combined the credited public lower-cost engine with our
physical covariance and trace-informed mean corrections. Later refinements and
larger-physics cost checks are preserved in the report.
No automatic next task. The T159A milestone audit remains historical through T159.

**T156 is complete.** The [amended recurrence policy](docs/COMPETITIVE_RESEARCH_LOOP.md#theory-recurrence)
allows numerous small experiments during derivations, including partial
prototypes and targeted parameter comparisons. Keep brief reproducible records
and use feedback to revise the theory. The default recurrence floor is now120
active research minutes, including60 written mathematics. Extra empirical time
can become further derivation when more probes would teach little. Preserve
larger task-specific floors and the preference for credible larger gains.
[Change record](experiments/protocol/t156/REPORT.md).

The [T147 public V29 reproduction](experiments/submission_policy/t147/REPORT.md)
was the previous official best:54.20% better adjusted score than JSP, with unchanged
MIT source/defaults and no local fit or algorithm adaptation. Reuse its
corrected loader, actual call lifecycle and relevant qualification evidence.
The ordinary grading allowance is60 minutes per attempt under the owner's
standing T161 amendment; earlier round-specific wait records are historical. T172 is complete; its unrestricted protocol waiver was task-specific.

The [T137A postmortem](experiments/analysis/t137a/REPORT.md) explains the
preceding7.40-fold adjusted-score breakthrough and its forecast miss.
The [literature index](docs/LITERATURE_INDEX.md) and
[route tracker](docs/RESEARCH_ROUTE_STATUS.md) retain alternative routes and
reopening conditions. A2LR remains untested and requires re-ranking against
the current best.

Earlier strategy reviews remain available for planning.
[T128A strategy map](docs/RESEARCH_STRATEGY_MAP.md) records the approach tree,
task/time census, fitting versus deduction, and suggested areas of focus.
These suggestions add no execution or validation gate.
The [T128B neglected-track review](docs/NEGLECTED_RESEARCH_TRACKS.md) adds
eight ranked opportunities and the original one-time agent briefs. Dated
T129 addenda record what the completed trial changed; the earlier review itself
did not authorize execution or a new standing process.

For current T172 comparisons, use `tmp/t172-runtime312/bin/python` with
FlopScope0.12.3 and WhestBench0.16.2, as announced by the organizer on October17.
Preserve historical runtime evidence. The prior
qualified system-Python3.12 environment `tmp/t128-runtime312/bin/python`, with
WhestBench0.16.0/FlopScope0.12.0/NumPy2.2.6 and
[recorded pins](experiments/submission_policy/t128/runtime312-requirements.txt).
It reproduced the old fixture and features byte-for-byte and completed the
fitted comparison within caps. Preserve the older environment's runtime
failures; no root cause was established and no existing environment changed.
Reuse relevant passing checks. Never commit credentials or private data.

The original [Astra handoff](ASTRA_HANDOFF_2026-09-04.md) predates T120A/T120B
and is historical. Full earlier entry-point/status documents and TODO history
are preserved under [T123/before](experiments/protocol/t123/before/).
