# Optional scientific protocol reference

**Scope as of T123:** the following is the preserved pre-T123 scientific
protocol. It governs its historical evidence labels and provides methods for
a separately chosen scientific task. It is not the default candidate or
submission workflow. References to “every candidate,” mandatory F0--F3,
P1 pools, fresh blocks and native-only execution below are scoped to those
scientific contracts; they do not require a second implementation or extra
validation before ordinary official feedback.

Before new scientific work, specify the claim, relevant procedures, data
roles and finite budget. No full-rigor trigger is automatic. Follow the current
[submission policy](COMPETITIVE_RESEARCH_LOOP.md) for candidate selection,
upload eligibility and task ordering. Relative repository paths in the
preserved text below are interpreted from the repository root.

---

# Research protocol

This protocol exists because the first attempt found an apparently strong
average improvement that disappeared when evaluated with the exact fixed point
set. The campaign should make that class of error difficult to repeat.

## 1. Evaluation tiers

Use four disjoint tiers.

### A. Exploration

Cheap synthetic networks and small widths. Use to reject broken mechanisms and
debug implementations. Results here do not justify promotion.

### B. Selection

A fixed, predeclared set of width-256, depth-32 networks. Hyperparameters may be
chosen using this set. Once used for selection, it is never described as
validation.

### C. Frozen validation

At least three untouched blocks, ideally using official public-dataset ground
truth. Evaluate the exact candidate package with fixed points and routing. A
candidate that fails is not tuned against the same block; create a new version
and reserve a new block.

### D. Final blind

A final local holdout not inspected until the candidate slate and selection rule
are frozen. Use once per major checkpoint. The actual challenge private rerun
is stricter still.

Store block manifests under `state/splits/` and never edit an existing manifest.

### Continuing fast and rigorous cycles

The historical selection and validation 1–3 roles were opened in Checkpoint 2.
They are development evidence now and cannot confirm an adaptively created
candidate. `local_blind` remains sealed for the final predeclared slate.

Every new candidate follows TODO's nested process:

1. complete the applicable bounded novelty-generation task in
   `docs/ACADEMIC_NOVELTY_AND_SUBMISSION_POLICY.md`, assign a novelty label, and
   separate any score-only baseline from an academic-contribution claim;
2. register its semantic identity in `ALGORITHM_LEDGER.md` and reject exact
   duplicates;
3. run F0 static feasibility, F1 micro correctness, the reject-only F2
   sentinel, and two renewable F3 exploration cohorts;
4. enter a rigorous cycle only after the frozen `P1-promising` pool gate is
   nonempty and the required alternative mechanism attempts are complete;
5. freeze at most three candidates and three fresh rigorous blocks before any
   result is viewed; and
6. if no candidate survives, retire that slate/epoch and return to fast
   discovery with new candidate IDs and later fresh blocks.

Empirical tier and novelty are orthogonal. `N0-KNOWN-BASELINE` through
`N2-NOVEL-MECHANISM` come from the academic-novelty policy; a candidate may be
empirically strong but academically known, or academically novel but
empirically rejected. The score-track fallback lane does not open protected
scientific outcomes and must not be used to bypass the candidate funnel.

Use four distinct scientific states; do not collapse them into the word
"promotion":

- `M1-mechanism-signal`: a cheap local diagnostic or ablation moves in the
  predeclared direction. This is useful research evidence, even if the method is
  currently far from the incumbent, but it does not unlock rigorous testing.
- `P1-promising`: the complete fast funnel supports the candidate against its
  relevant paired nearest-grid/equal-compute mechanism control under the
  T065-frozen effect, uncertainty, and tail rules. The actual incumbent must be
  reported as contest context, but failure to match it is not a `P1` veto.
- `R1-mechanism-confirmed`: fresh rigorous blocks confirm the scientific gain
  against the frozen mechanism control. An `R1` result remains positive research
  when it is not contest-competitive; preserve it and return to the fast funnel
  for refinement.
- `P2-competitive`: an `R1` candidate also passes the separately frozen
  paired competitiveness rule against the actual incumbent, plus all applicable
  compute, tail, and reproducibility gates. P2 qualifies a strong scientific
  and native-competitiveness claim; it is not an Official-Rules submission
  prerequisite.

Submission readiness is a separate axis. Per
`docs/SUBMISSION_RIGOR_AUDIT_2026-08-25.md`, a current best or at-least-`N1`
candidate may enter Phase 2 translation, packaging, and official public
evaluation at any empirical tier after passing the hard rules/compliance and
operational gate. Scientific failures remain disclosed and inform final
designation, but they do not ban a lawful package. The normal two-entry final
strategy preserves a reliable/best-score entry and a materially distinct
strongest novel entry where possible.

### Promotion transparency contract

Apply `docs/OWNER_OPERATING_DIRECTIVES.md` to every candidate decision and
decision-relevant support result. The candidate report and durable ledger
summary must show the current and highest supported tier, strongest favorable
evidence, next tier considered, and every relevant gate as `PASS`,
`FAIL-SCIENTIFIC`, `FAIL-STRICT-GATE`, `NOT-RUN`, `NOT-APPLICABLE`, or
`BLOCKED-OPERATIONAL`. For each strict-gate miss, report the frozen threshold,
observed value, direction, and margin.

The conclusion must separately answer whether the primary blocker is a
scientific negative, strict-gate limitation, incomplete evidence, operational
block, incumbent-only competitiveness gap, or support-only scope; whether a
strict gate is the sole blocker; and the smallest credible high-impact unlock
with its actor. A later failure never erases a valid lower tier. `NOT-RUN`
means not yet known, and incumbent-only failure can block `P2` but not valid
`M1`, `P1`, or `R1` evidence. A frozen gate may be flagged for prospective
owner review but may not be relaxed retroactively after outcomes are opened.

Fast confidence intervals are screening diagnostics, not confirmatory claims.
FFC002 v2.1 fixes the fast absolute-effect gate at no less than the
`4.365727137273773e-10` T014-derived provisional screening floor.
`candidate_pair_recomputed=false`: this value was derived for routed 31,232
versus routed 16,384 and is neither a target-noise MDE recomputed for arbitrary
candidate pairs nor proof of universal conservatism. A candidate may predeclare
a larger value before outcomes, but P1 requires an absolute effect at least the
effective frozen floor. M1 requires a core-derived mechanism signal of at least
`0.01` on two routes, and a candidate/mechanism ratio of at least `1.25` is an
inclusive unexplained-tail boundary.

Repeated rigorous cycles use a predeclared familywise one-sided error allowance
such as `0.05 / 2^j` for cycle `j`, with Holm adjustment within its slate, or an
equally conservative frozen anytime-valid rule. This prevents an indefinite
feedback loop from manufacturing a false positive through repeated 5% tests.

Each fast batch and rigorous cycle is a bounded checkpoint. A negative result
completes and checks its experiment tasks but does not clear a positive phase
gate. Only an explicit owner request terminates the continuing project.

Within a batch, candidate turnover is immediate. As soon as a candidate is
scientifically negated or proven duplicate, stop its unchanged descendants,
mark their gates `NOT-APPLICABLE`, and advance to the next materially distinct
candidate. Do not consume compute on a failed premise or retain dependent
stages as unchecked TODO blockers. Preserve any valid lower-tier mechanism
signal, and keep strict-gate-only near misses visible for owner review.

Artifact-producing discovery, validation, correction, and optimization use the
audited standalone C++20/native path through Checkpoint 5. A separate
submission-evaluation lane may translate and package the current best and
strongest at-least-`N1` candidate earlier under T074; this never transfers a
native scientific tier or turns an official score into mechanism evidence.
Final scientific-slate translation remains in Checkpoint 6. Native proxy
results are never reported as official Whest scores.

## 2. Primary and diagnostic metrics

Scientific primary comparison through `R1` uses the frozen native modeled-score
proxy, never an official Whest score:

- arithmetic mean per-MLP adjusted final-layer score versus the predeclared
  nearest-grid/equal-compute mechanism control;
- paired candidate/control ratio on that arithmetic mean.

Contest comparison:

- the same paired arithmetic metrics versus the actual deployable incumbent;
- mandatory context at F2/F3 and rigorous evaluation, but a pass/fail gate only
  for `P2-competitive` and scientific/native final-selection claims. It informs
  submission choice but is not a hard upload-eligibility gate. If a faithful
  comparison is impossible, predeclare the closest valid comparator and
  limitation before viewing results.

Always also record:

- raw final-layer MSE;
- all-layer MSE;
- analytical FLOPs;
- residual wall time and effective compute;
- score multiplier;
- failures, zeroed MLPs, non-finite outputs, and budget exhaustion;
- median per-network ratio;
- 75th, 90th, 95th, and maximum per-network ratio;
- network win rate;
- layerwise MSE curve;
- wall-clock and peak memory.

Geometric means may reveal typical multiplicative behavior but never replace
the arithmetic objective.

## 3. Scientific qualification and submission gates

A cheap directional result may earn `M1-mechanism-signal`; it should be
reported and retained without being described as `P1-promising`,
`R1-mechanism-confirmed`, or `P2-competitive`. A method earns `P1-promising`
only through the complete frozen fast rule against its relevant paired
mechanism/equal-compute control. Incumbent results are mandatory context at this
stage and may motivate refinement, but they do not erase a valid mechanism
result or block `P1-promising`.

Every gate assessment below must be included in the human promotion
disposition even when the first failed gate stops later work. Unrun later gates
are `NOT-RUN`, not silent failures or evidence against the mechanism.

Rigorous scientific qualification (`R1-mechanism-confirmed`) requires all
applicable scientific gates:

1. deterministic native contract, exact identity, and finite outputs;
2. no budget-projection or operational failures;
3. exact fixed shipped assets and routing tested where applicable;
4. improvement over the frozen mechanism control on at least three independent
   fresh blocks;
5. aggregate arithmetic adjusted-score improvement large enough to survive
   reference noise and compute uncertainty;
6. no unexplained catastrophic tail; as a default, maximum per-network ratio
   should be below 1.5 unless the aggregate gain is overwhelming and the tail is
   understood;
7. bootstrap or randomization interval reported at the network level;
8. mechanism-specific ablation supports the claimed cause.

`P2-competitive` additionally requires the separately frozen paired
competitiveness rule against the actual incumbent. Package size, grader API,
Python determinism, subprocess, and rules-compliance gates remain mandatory for
the affected submission package, whether exercised early through T074 or for a
later final scientific slate. Passing native scientific gates is not a claim
that a Python/Whest submission is ready; conversely, lacking P2 does not make a
validated lawful package ineligible for official evaluation.

These thresholds are defaults, not laws. Change them only before viewing the
relevant validation block and record the reason.

## 4. Paired experiment design

For candidate A versus baseline B:

- use identical MLPs and ground truth;
- use identical sample counts where the scientific question is variance
  reduction at fixed sampling compute;
- separately compare under equal effective compute when the challenge score is
  the question;
- preserve per-network records;
- use network-cluster bootstrap, not independent-neuron bootstrap;
- report the ratio of arithmetic means and the arithmetic mean of paired score
  differences;
- inspect outliers before summarizing.

## 5. QMC-specific safeguards

- Distinguish fresh-scramble studies from fixed shipped-design tests.
- Quantize points exactly as shipped before final comparisons.
- Evaluate every bank and seed-routing branch.
- Test coordinate permutations, reflections, and rotations for worst-case
  behavior, not only their scramble-averaged mean.
- If a learned or pilot selector chooses among point systems, cross-fit the
  selector and evaluate selection regret.
- Prefer mixtures that reserve some unrotated points when a rotated component
  has uncertain tails.

## 6. Reference quality

Official baked ground truth is preferred. For synthetic references:

- use independent point sets from every candidate;
- use enough samples that reference uncertainty is small relative to the
  candidate difference;
- repeat references or estimate their standard error;
- do not select a method based on one noisy reference realization;
- record reference method, sample count, seeds, and convergence checks.

## 7. Compute accounting

For every `P1-promising`/`R1-mechanism-confirmed` candidate, project the intended
supported-operation cost and measure the native scientific proxy. For every
`P2-competitive` candidate translated at the final boundary:

- measure flopscope's actual `flops_used`;
- measure residual wall time and effective compute;
- test the slowest/worst MLP, not only the mean;
- keep a meaningful reserve below the hard cap;
- inspect dtype billing and hidden float64 conversions;
- profile large allocations and array lifetime;
- run the grader-like subprocess and docker modes;
- avoid internal time cutoffs calibrated to one machine.

The score may reward using substantially less compute. Optimize raw MSE and
adjusted score separately rather than assuming the full budget is optimal.

## 8. Experiment record

Each experiment gets:

- immutable ID (`E###`);
- associated task ID (`T###`);
- hypothesis stated before results;
- candidate and baseline hashes;
- command line and environment versions;
- split manifest;
- raw machine-readable report;
- short result and decision;
- follow-up hypothesis.

Through Checkpoint 5, use the native/shell event and provenance transaction
qualified by T066 (eight source-keyed CPU1 Clang 17 steps, qualification key
`cc2cdd34f655a87414285cfe0e8d46e747e0cb15f4f29fa5f56c0bbe407bbeb4`). It must bind the
canonical algorithm specification, native source/build/binary and dependency
hashes, exact argv, immutable manifest, T064 shard identities, raw report, and
ledger event before publishing the result. T025/FC001 is its first scientific
use; do not improvise a Python recorder for current artifact-producing work.

The pre-F0 production evaluator is a trusted audited boundary. T065 binds its
exact source/build/binary bytes, rejects direct and closure `libpython`, and
replays a five-second `env -i` interface smoke, but it does not install a
syscall sandbox or technically prevent evaluator-initiated open, exec, or
Python subprocess activity. T066 F1, not that pre-F0 seal, supplies scientific
qualification.

`scripts/record_experiment.py` is retained for historical Whest campaigns and
final Checkpoint 6 Python translations. There it must be used with
`--candidate-path`, exact `--command-argv-json`, and the named
`--split-manifest`; it writes an immutable `provenance.json` that hashes the
exact Whest-packaged files, environment locks, command arguments, and split.
Store large run outputs under `runs/E###/`.

### Crash-resumable long runs

Every multi-network fast-funnel or rigorous run, regardless of expected
duration, and every other empirical command expected to exceed 10 minutes must
use the T064-qualified shard-first execution path. The independent unit should
normally be one exact network/route/configuration tuple. Each unit must:

- bind its exact dataset/manifest member, input hashes, controller source and
  binary hashes, configuration, seed/route identity, numerical dependencies,
  and canonical order before computation;
- write to a unique temporary path, validate schema/cardinality/finiteness, and
  atomically rename a content-addressed payload plus completion record only
  after the unit is complete;
- leave interrupted temporary data distinguishable from completed evidence;
- refuse duplicate identities with unequal payloads and any hash, schema,
  order, or route mismatch.

On resume, verify every completion record from bytes and skip only fully valid
units. Merge verified shards in a declared deterministic order, reject missing
or duplicate units, and bind the final aggregate to the ordered shard hashes.
T064's qualification included bounded normal and ASan/UBSan fault-injection
tests in which interrupted-and-resumed fixtures were byte-identical to their
uninterrupted references under the canonical representation. Preserve each
future interruption record and resume audit with the result.

T064 makes this gate mandatory before any such run and before another protected
role is opened. Completed scientific legs may remain the coarsest reusable unit
only when each leg itself meets the same atomic, hash-bound, and equivalence
requirements.

The T065 incumbent realization (canonical report SHA-256
`a5db21da5a723a4f3fb7cc1d9fb45a40eb202fb0506ea880dc5a7e2e26ce5e15`) is a
numerical control for the frozen contract, not a second algorithm or a
submission artifact. Never transfer its native proxy to Python/Whest,
flopscope billing, residual time, package behavior, or official-grader claims.

## 9. Honest stopping rules

Stop or demote a branch when:

- its core mechanism fails a clean falsification test;
- gains require repeated tuning on frozen blocks;
- fixed-design tails erase the mean improvement;
- effective compute or residual time makes it noncompetitive;
- a simpler estimator matches it;
- its apparent gain is below reference noise.

Preserve the branch and write down why. Negative results are part of the final
technical contribution.
