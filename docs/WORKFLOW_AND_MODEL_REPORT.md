# How this challenge was approached

**Author and participant: Tristan Miano** (`tristan_miano` on AIcrowd). This is a retrospective account of an extensively AI-assisted research project, through submission **336809 / ALG058-V001** and the October 18, 2026 writeup draft. It describes what happened, including unsuccessful work and changes of direction. It is not a claim that this workflow is optimal or that another run will reproduce the same discoveries.

The numerical problem was to estimate mean activations of known random ReLU networks under Gaussian inputs, using fewer charged operations than sampling at comparable accuracy. The project optimized the official adjusted error, including its compute multiplier. The best retained public grade is **2.971106406126817e−9**. Final private evaluation and prize review are distinct from this public result.

## Human and model roles

| Contributor | Recorded role | What the record supports |
|---|---|---|
| Tristan Miano | Set the objective, chose tasks, changed strategy and research budgets, authorized submissions, reviewed results and writeups | Human direction throughout; no complete log of human supervision hours |
| GPT-5.6 Sol | Principal earlier research/coding agent | Identified by the owner as carrying out most work before the September 4 Astra handoff; no reliable per-model time allocation |
| GPT-6 Astra, primarily extra-high effort | Later main research, coding, experiments, literature, analysis and drafting | Owner-confirmed description: primarily local work through the ChatGPT Desktop application. Exact backend build/version for each turn is not recorded |
| Fable / Fable 5.1 | External proposal contributions | All-layer Edgeworth mean-correction proposal entered at T108B; repair/derivation at T109 and test at T110. Early-anchor proposal led to T117B/ALG025 |
| Opus-5 | External variance-recalibration proposal | Repaired and tested in T119A; the tested form lost and was not submitted |
| T129 root plus three sub-agents, Ultra effort | One explicitly authorized parallel theory trial | Exact-control, uniform/compression/cost, and current-shape tracks; bounded follow-ups, at most three sub-agents at once |

The Sol/Astra attribution and the extra-high/local-desktop description come from the owner's account, confirmed on October 18. The Fable/Opus labels are the names in the retained intake records; this report does not infer vendor identities or undocumented model versions. A task date alone does not identify its model. There is no complete per-turn token, price, reasoning-effort, or model-build ledger.

LLM agents performed most code writing, derivation, literature inspection, experiment execution/interpretation and report drafting. The human did not personally write or independently prove every part. Explanations without isolated empirical support remain hypotheses. The participant is responsible for the final submission and report.

T129 is the one separately timed multi-agent trial documented here. Its root recorded **181.15 active theory minutes**; agents recorded **86.14**, **86.74**, and **112.03** minutes. The **284.91 agent person-minutes overlap** the root and one another. The combined **7.77 person-hours** are not 7.77 elapsed hours. Parallel critique repaired a control fit, identified a missing squared-third term and exposed a Gram-cost saving. There was no matched solo run or token-cost comparison showing that Ultra or delegation was more efficient. Most later recurrence records explicitly say no sub-agents were used.

Sources: [strategy-map attribution](RESEARCH_STRATEGY_MAP.md#attribution-and-reproducibility), [Fable intake](../experiments/checkpoint3/t108b/INTAKE_ASSESSMENT.md), [T119A](../experiments/checkpoint3/t119a/REPORT.md), [T129](../experiments/theory/t129/REPORT.md).

## Task structure and persistent memory

The ordinary unit of work was **one owner-authorized TODO task**, rather than a continuously autonomous campaign. A task might be a research recurrence, a bounded candidate attempt, a failure diagnosis, a literature refresh, a strategy review or protocol maintenance. Task numbers reflect planning history and are not a reliable chronological sort: tasks could be deferred, resumed or carried out out of numeric order. The experiment-event sequence records execution order.

Each new session read the live state, active TODO queue, current protocol, relevant prior results and algorithm ledger. Persistent Markdown/JSON files carried context across fresh conversations, model changes and crashes. The September 4 handoff is a dated orientation artifact. Old instructions were preserved as history, not silently imposed on every later task.

Typical task artifacts were:

- A scope/specification with hypothesis, comparator, data role, source identity, start time and estimate.
- A mathematical scratchpad and/or short probe records while research was in progress.
- Executed source/configuration, outputs, input/asset identities and actual compute measurements.
- A report stating the decision and limits, structured result, timing record and event row.
- An update to the active TODO, live state and algorithm entry; a scoped local Git commit when practical.

These were conventions rather than a perfectly uniform schema. Some early timing records are missing, some task results have different names, and not every exploratory probe received a full registered algorithm ID. The public release preserves selected source records and explicitly records what was copied. It is a curated snapshot, not the entire original Git history or all tool conversations.

See the dated [TODO snapshot](../workflow/TODO.md), [agent instructions](../workflow/AGENTS.md), [handoff](../workflow/ASTRA_HANDOFF_2026-09-04.md), [event ledger](../state/experiments.csv), and [copied-file provenance](../evidence/export_origins.json). Snapshot instructions describe the original workspace; they are not instructions to automatically start its next task.

## How the strategy changed

| Period | Main practice | Why it changed |
|---|---|---|
| Initial sampling and closure work | Broad sampling comparisons, synthetic mechanisms, native scientific checks, strict freezes and tiers | Some promising small-network effects failed at full scale. This phase also accumulated expensive infrastructure and verification work |
| T123 submission-focused reset | Prefer small actual-package comparisons, reuse evidence, distinguish scientific proof from a submission decision | The owner wanted roughly 90% practical confidence, cheap official feedback and less unnecessary rigor |
| T129 parallel trial | Divide selected neglected tracks and the current track among three sub-agents | Explore breadth and cross-check derivations; evaluate once before making it permanent |
| T132 onward | Literature review before or alongside recurrence; track exhausted routes and reopening conditions | Avoid rediscovering published methods and spend time where new evidence could change a decision |
| T136/T139 onward | Preserve a cheap fallback while developing a credible larger-gain route | Avoid choosing every candidate solely for a high chance of a small win; the owner later corrected drift back toward risk aversion |
| T156/T153 onward | Interleave numerous small empirical probes with equations, then broaden the probes | Pure theory often ended with weakly supported nominees. Feedback during derivation could reject assumptions sooner |
| Later four-hour recurrences | Repeated derivation–prototype–measure–revise loops; allow no nominee and repeat a recurrence | Good improvements sometimes required several rounds. Finding a small candidate did not terminate more promising research |
| T172 final recurrence | Owner waived research time-allocation restrictions, retained a four-hour floor and challenge compliance | Use the remaining time for the best achievable adjusted score, combining public implementation progress with tested local adaptations |

Time floors were **minimum active-work commitments**, not a claim that spending a fixed number of hours guarantees a discovery. Different rounds had different subdivisions. For example, T143 specified two hours of derivations, one hour of literature and half an hour of selection. Later rounds commonly used a four-hour total floor with substantial empirical work. Current standing defaults in a protocol file do not retroactively replace task-specific instructions.

The owner also lengthened evaluator waits when the service was slow. The standing default eventually became **60 minutes per attempt**, with at most one unchanged-package retry for a generic evaluator problem; some individual rounds allowed longer waits. Waiting was useful operational patience, not counted as mathematical work.

The decision objective remained better submissions, regardless of academic novelty. Existing public methods could be reproduced or adapted with appropriate licensing and credit. The substantial-contribution requirement for final eligibility still applies; publication and successful grading are not advance eligibility approval.

## What a research recurrence actually did

1. **Reorient.** Confirm the current incumbent, exact runtime/cost model, unresolved failures, public developments and the current task's authority and time floor.
2. **State a hypothesis mathematically.** Write the proposed state, recurrence or correction; identify assumptions, omitted terms, scaling, invariances and the output observable that matters.
3. **Estimate charged cost early.** A more accurate raw predictor may be a worse challenge algorithm. Check the actual FlopScope path, required state size and residual-time overhead rather than extrapolating only from a native prototype.
4. **Probe while deriving.** Use generated identities, reduced-width calculations, captured geometry, small public development comparisons or partial implementations. Label exploratory/adaptive data honestly. Revise or abandon the equation when evidence disagrees.
5. **Compare routes.** Keep a cheap candidate as a fallback while pursuing larger credible gains. Record why an alternative failed: mathematical obstruction, missing information, numerical failure, resource cost, incomplete implementation or actual predictive loss.
6. **Nominate zero, one or two actionable candidates.** State a rough success probability, possible gain, missing engineering and cheapest informative next step. These forecasts were judgment calls, not calibrated Bayesian probabilities.
7. **Close the task.** Save derivations, scripts, results, failed paths, timing and a next-step recommendation. A no-nominee result was allowed and occurred repeatedly.

Early recurrences emphasized equations and deduction, but the later process was a hybrid of deduction, literature reuse, empirical search and supervised fitting. It would be misleading to describe the whole project as pure theorem-driven discovery. Feature families and local corrections were often motivated analytically, then selected, fitted or rejected on data. The final mean sources are small learned models, with training targets and architecture disclosed in the final report.

The route tracker estimates exhaustion of **particular tested recipes**, not exhaustion of a mathematical field. Larger fourth-state representations repeatedly showed raw capacity but failed cost or transfer constraints. Better preservation of one contraction did not reliably preserve subsequent nonlinear covariance feedback. This distinction prevented a cheap projection failure from being presented as a general impossibility theorem.

## Candidate attempts and official feedback

The later submission workflow froze a chosen algorithm variant before its submission-facing comparison, ordinarily used a small paired panel of about twelve predetermined public networks, and reused relevant earlier checks. It compared arithmetic mean adjusted final-layer error, actual costs, wins, uncertainty and resource failures against the deployable incumbent.

Approximately 90% support was a practical shipping screen, **not** a theorem, a required research-stage success probability or a ban on high-upside speculative work. Adaptive panel exposure was disclosed. Repeated tuning on an observed panel does not create fresh validation. A local bootstrap cannot by itself establish a 90% chance of beating the private leaderboard.

Before upload, the actual archive was checked for identity, allowed numerical operations, finite full-shape output, resource limits, natural call lifecycle and replay where appropriate. Passing checks were reused when unaffected by changes. Submission-task authorization covered upload and monitoring; final nomination and writeup delivery remained separate actions. Failed service attempts were distinguished from algorithmic losses.

The history includes a generic failed evaluator attempt and an actual compliance failure from raw-NumPy constant construction, repaired to charged FlopScope operations. The latter is disclosed rather than recast as a service error. Most unsuccessful algorithm ideas were stopped locally and therefore have no official submission ID.

## What drove the score improvements

The path moved from Sobol/Haar sampling, to sampling/closure combinations and fitted corrections, to factored joint-cumulant recurrences, public V29 reproduction and adaptations, then physical covariance correction and learned mean innovations on the lower-cost public e30_a engine.

Returns were uneven. T137's large improvement followed adoption and adaptation of the published cumulant framework. T147 was an **unchanged public-code reproduction**. T159's improvement followed about **16.45 recorded session hours** since that reproduction, including unsuccessful attempts and diagnosis. Later gains often required several four-hour recurrences. A successful submission list alone hides this selection process; the task chronology includes the failed and no-nominee work between successes.

For the final result, the **28.50% historical improvement** over ALG053 should not be credited wholly to this project's new mathematics: most was associated with adopting the public lower-cost engine. On four adaptively reused networks with the same current meter, the complete local adaptation improved adjusted error by **4.55%** relative to that public engine. The added mean sources improved the official score by **2.05%** relative to our covariance-only entry. These are different comparisons with different evidential strength.

The record does not isolate the causal effect of the owner's larger-gain policy, a particular model, Ultra effort, more time, or any one protocol change. Public research, implementation improvements, model/session changes and repeated experience were confounded. Successful outcomes do not validate every derivation proposed along the way.

## Reproducing the workflow

Use [REPRODUCTION.md](REPRODUCTION.md) for exact packages, report rebuilds and inference. To reproduce the *working process* on a new research question:

1. Create an incumbent record and a task queue. Preserve the actual objective, rules, data permissions and cost model in short entry documents. Keep credentials outside the repository.
2. Give the agent one concrete task with its time budget/floor and allowed actions. State whether public research, experiments, fitting, uploads and delegation are authorized.
3. Require equations and cheap falsifiable checks during research, with a scratchpad and persistent checkpoints. Let the agent return no nominee. Require accurate separation of fitting data, reused development data and protected evaluation.
4. For promising candidates, freeze source/assets, compare the actual charged implementation on a small paired panel and qualify the shipping archive. Do not require a large scientific campaign unless that is the objective.
5. Use official feedback when authorized, retain failed attempts and record the resulting score. Have the human review recommendations before a new task, final selection or formal publication/delivery.
6. At session boundaries, update live state, TODO, results and timing so another conversation can resume without restarting the work. Save intervals before long operations; recover from disk after interruption.

Example recurrence request:

> Work on the next authorized research task for at least four active hours. Optimize adjusted score, following the challenge rules. Combine literature, derivation and empirical probes. Preserve a cheap fallback while pursuing a credible larger gain. Record failures and data exposure; zero nominees is acceptable. Save checkpoints and report active time separately from waits and interruptions.

Example candidate request:

> Implement and qualify the selected fixed candidate. Reuse relevant evidence and use a small paired production comparison. If supported and compliant, submit the exact archive and monitor within the agreed wait/retry budget. Record the decision and stop after this task.

These prompts are reusable reconstructions of the approach, not a verbatim export of every conversation. The supplied snapshots show the project's evolved protocol, including obsolete historical context. A new run should explicitly choose its own rules and budget rather than inherit every historical gate.

The [full timing table](SUBMISSION_TIMELINE.md), machine-readable [task records](../evidence/task_times.json), [individual submitted-method writeups](../writeups/README.md), and [dated research strategy map](RESEARCH_STRATEGY_MAP.md) allow readers to inspect the workload and decisions. Timing is recorded session effort, **not model thinking-time telemetry**. Human hours, dollar cost, tokens, all external-model work and a complete per-turn model history are unavailable and are not estimated here.
