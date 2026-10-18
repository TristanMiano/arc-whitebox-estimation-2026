# T169 — complete native fourth-state constructor and transfer diagnosis

**The constructor is now implemented and affordable enough to test, but the
measured correction is not competitive. No submission nominee.** Keep
ALG052-V000/submission332641, official adjusted score4.285182274373245e-9.

The main practical result is a complete permitted-runtime implementation of a
cheaper late fourth-state update, including its observations, transported third
proxy, carried and born terms, repeated targets, covariance bases and shared
compression. The main scientific result is an explanation for its failed native
transfer: compression destroys a real broad fourth-moment component, and useful
small-network error cancellation does not survive the move to the incumbent's
actual regime. A concrete repair confirms much of that diagnosis, but does not
produce enough accuracy to pay for the additional state.

The recommended next task is a broader empirical research recurrence, preserving
these implementations and findings. The full proper nonlinear mean/covariance
feedback port remains unbuilt. It should not be the automatic next engineering
task. [Selection, forecasts and untested work](CANDIDATE_SELECTION.md).

## Complete construction and cost

The original T168 model is expensive when all previously unpaid terms are
included. Its complete1024 steady update costs1.573T FLOPs with straightforward
products, or578.487B after exact fusion/Strassen engineering. A negative
mixed-third211 completion dominates. Approximating its covariance edge retains
small-network accuracy, but still costs96.970B per update after further exact
engineering—too much for seven late updates.

P09 changes the approximation: omit the **whole output211 correction**, retaining
the born/carried211 values and ordinary scalar4/31/22 target corrections. Keep
the transported gate-derived third proxy, original physical third state, fixed
half mean/covariance sharing, Q128/common96/pair32 and middle64. This improves
the retained generated results and removes the expensive completion. The later
cost reductions preserve this selected mathematical model; floating-point order
changes are separately measured rather than called byte equivalence.

| Constructor stage | Scope | FLOPs |
|---|---|---:|
| Original complete model, straightforward | One steady1024 update |1,572.625B|
| Original complete model, fused | One steady1024 update |578.487B|
| Cross16 approximation, exact implementation savings | One steady1024 update |96.970B|
| P09 output211 omission | One steady1024 update |24.596B|
| P12 exact proxy reassociation | One steady / first-rich update |18.762B /26.084B|
| P36 shared-input, fused P09 | **Entire added high trajectory**, seven updates plus terminal/seed work |128.025B|
| P50 own-trace-protected state | Entire added high trajectory |155.941B|

These rows include a model change as well as exact engineering; they are not
one uninterrupted exact speedup. Standalone fixtures and actual native input
trajectories also have different bills. Complete whole-estimator calls below
are the relevant feasibility measurements.

The reusable exact work includes lazy repeated-proxy contractions, packed
symmetric pair coordinates, shared bank queries, fused scalar/pair observation
polynomials, pooled products, symmetric reconstruction and collected adjoints.
The latter combine contributions with the same large pair bank before applying
its transpose. Tiny independent identities check the operators and contractions;
float32 state comparisons record tolerance-level differences. The failed
implementation and runtime attempts remain preserved.

## What the actual estimator calls show

P41 is a deliberately limited native pilot: compute the complete rich state on
the incumbent's unchanged physical trajectory and propagate its fixed half
high-minus-low mean source through the Gaussian mean Jacobian. Add that readout
to the existing NN correction. It is not the full proper-dual feedback algorithm.
P42 is the cheap limiting correction that removes native scalar fourth/higher
mean terms fromlayer9 without constructing a rich state.

Both sources were fixed before T169 read their targets. The two networks are
previously exposed **F training rows0/499**, including incumbent training, so
these are adaptive mechanism tests—not held-out validation or90% confidence.
The actual unchanged ALG052 comparator uses the same call order.

| Actual call | Row0 FLOPs / residual | Row499 FLOPs / residual | Paired raw ratio | Paired adjusted ratio |
|---|---:|---:|---:|---:|
| Unchanged ALG052 |479.296B /0.303s |457.377B /0.342s |1|1|
| P41 rich frozen-mean readout |627.643B /0.370s |617.689B /0.390s |2.1561|2.8686|
| P42 cheap zero-rich limit |479.310B /0.298s |457.392B /0.339s |2.4317|2.4287|

The baseline residual values are recorded per call in the actual evidence;
see the machine-readable call files for full precision. P41's observed costs
require23.64%/25.95% raw reductions merely to break even. Both variants lose on
both rows. P41's warm peak memory isabout7.47GB, within the observed8GiB limit;
its residual headroom is narrow. These are successful measured calls, not full
archive qualification or a guarantee about every future input/lifecycle.

There was an unintended4.58-second upper-bound overlap between the end of the
baseline process and the next research launch. It is disclosed in
[P41_P42_SCHEDULING_NOTE](P41_P42_SCHEDULING_NOTE.json). Both completed; subsequent
launches checked the final guard. No clean-run campaign or host audit was added.

[Exact per-network comparison](P41_P42_ACTUAL_COMPARISON.json) and prediction-only
artifacts are retained. Private input-containing captures stay outside committed
evidence. No official upload, protected blind access, new model fit or agent work
was performed.

## Why the rich correction fails

The strongest diagnosis comes from reusing T166's existing million-sample
moment measurements on the same exposed F0 network. The input weights match
exactly. Replicate variation supplies a finite-sampling uncertainty estimate.
All standardized values below use the same native variance denominator.

| Incoming layer | Estimated actual fourth cumulant /variance² | Native lower state | Compressed rich state | Trace-protected rich state |
|---|---:|---:|---:|---:|
|8|0.04354 ±0.00032 SE|0.04192|0.04185|same initial seed|
|12|0.05583 ±0.00022 SE|0.05039|0.00462|0.04762|
|15|0.06366 ±0.00040 SE|0.05600|0.000959|0.05037|

The rich state's late fourth-moment discrepancy is much larger than sampling
uncertainty. Weighted by the actual ReLU mean sensitivity, its fourth-moment
error atlayers12/15 isabout15–16 times the native lower state's. Decomposing
the mean source confirms that the changed H4 accounts for almost all the bad
readout; omission of the native kappa3²/kappa3*kappa4 terms is much smaller.
Older13-feature ridge correction is disabled in ALG052. Its newer NN readout
is separate and does not feed back into the physical mean; the diagnosis uses
that actual source behavior.

The geometry explains a specific risk of common neuron-rank compression. An
isotropic fourth tensor Sym(I,I) needs one pair factor, but a full-rank matrix.
Projecting every leg into a rank-r neuron subspace retains only
r(r+2)/(n(n+2)) of its average scalar observation under isotropic queries.
For common96 at1024 this isabout0.9%. This illustrative identity is not a fit
to the non-isotropic native state, but distinguishes pair rank from neuron rank.

P49 evaluates the selected **uncompressed** next scalar fourth directly, with
an exact structured native contraction. The first next-layer standardized
moment is.04407, near the native.04484. Later one-step uncompressed observations
are already damaged by their compressed history (.00750 atterminal). The
all-neuron query adds132.282B across seven updates and substantial residual
time; merely applying an expensive terminal lookahead cannot restore history.

## Repairs and counterfactual checks

P43 preserves the high map's own diagonal trace after compression by adding a
separate harmonic pair. Its generated256/384 MSEs are11.93%/28.24% worse than
P09. P47 exactly preserves its own next-layer scalar fourth observations via a
well-conditioned Hadamard-square Gram solve; it is15.54% worse at256. These
identities work, but preserving an approximate model's moments is not sufficient
to improve its final answer. Earlier T162/T168 trace and residual failures were
explicitly reviewed rather than rediscovered under new names.

After actual moment evidence identified the native failure, P50 implemented
the bounded own-trace repair at1024. It restores most of the missing background
and changes the F0 frozen-mean error ratio fromabout2.082 to1.012. P51's coupled
Gaussian mean/covariance tangent makes that1.008. The added high trajectory
costs155.941B, so this is a useful mechanistic rescue, not a competitive algorithm.

The Gaussian tangent was independently checked against finite differences and
the zero-mean ReLU covariance formula. It includes full covariance transport and
local mean/variance responses, but omits changing higher-state dynamics and NN
derivatives. The unrepaired state gives2.386x raw error with this coupling;
separating mean and covariance sources does not reveal a winning endpoint.
Neither result proves that the full nonlinear port must fail. Missing
physical-third and rich-state feedback can enter at first order, not only
through large nonlinear effects (SCRATCHPAD§37).

Retrospective quadratic bounds show that damping the same directions is weak.
Even optimizing a P41 scalar on its already-seen pair cannot beat1.326x adjusted
score. The repaired mean and Gaussian joint directions have optimistic raw
ceilings of0.36%/1.05% improvement on F0, far below the computation premium.
These are diagnostic bounds, not coefficients selected for a submission. P57 also
checks combinations: the entire span of four saved directions can remove at
most2.67% of F0 raw error, even fitted retrospectively on that same network.

P54/P55 check two further explanations on the same saved F0 evidence. The rich
mean response still loses against the physical estimator without its learned
head (1.903x raw error), so the NN does not explain the original transfer loss.
The trace-repaired response improves physical error only0.41%, which disappears
against the learned incumbent. Transporting the error already present atlayer7
through fixed Gaussian mean Jacobians gives an oracle-prefix-removal gain of
5.94% against the final learned-corrected error or7.66% against physical-only
final error. The intermediate returned means are physical in both cases. This is an algebraic
diagnostic, not a causal intervention or a bound on inherited covariance errors;
it does not support prefix mean error as the dominant problem.

## Why small-network capacity looked better

| Generated256/384 experiment | Final MSE256 | Final MSE384 |
|---|---:|---:|
| Dense AUG3 controls |9.15537e-7|4.03880e-7|
| P09 proper mean/C sharing |7.01824e-7|2.90074e-7|
| Forced-native physical baseline |9.69411e-7|4.02120e-7|
| Forced-native plus frozen high mean response |7.95350e-7|3.46722e-7|
| P43 own diagonal trace, dense proper feedback |7.85565e-7|3.71997e-7|
| P47 next scalar preservation, dense proper feedback |8.10894e-7|not run|

P46's forced-native bridge is a research adaptation at small width, not the
incumbent's production fallback. It retains native approximation laws and the
rich constructor, and compares the physical mean separately from the NN readout.
The gains survive this change of lower machinery, but shrink to17.96%/13.78%.
The lower approximation alone therefore does not explain the actual failure.

P53 adds an independent small-network moment check: on the same256 network,
terminal standardizedH4 is.25998 ±.00348 SE, versus native.22461 and high.15002.
The high scalar moment is worse, despite its better final mean prediction.
Its correction has useful alignment with other approximation errors there
(cosine-.447), which falls toabout-.059 on the actual P41 pair. Error
cancellation can produce a good submission if it transfers; it did not here.
The small positive results remain valid, with their interpretation narrowed.

The retained intermediate labels also let P56 compare the proposed local
sources with the correction needed by an algebraic fixed-Jacobian decomposition.
Atlayers9–15 their magnitudes are similar, but local alignment is weak. Their
summed terminal cosine is0.048 and falls essentially to zero after accounting
for the existing late NN sources. Thus the added error is mainly a wrong
direction, rather than a correct direction that merely needs a smaller weight.
These are exposed-data diagnostics, not fresh validation or an impossibility
result for richer feedback.

## Scope, incomplete work and next step

No proper native mean/C feedback port or submission-facing comparison panel was
completed or claimed. The port's interface semantics are worked out in
SCRATCHPAD§25: shared covariance must enter the trace-third refit and next
covariance transport consistently; overwriting it at the end would be wrong.
The native harmonic regeneration is also an explicit approximation relative
to the dense dual history. Tiny negative postactivation variance entries occur
in the formal shadow closure; the existing next-preactivation variance floor
must not be confused with a validated positive joint distribution.

The most useful next direction is a cheaper informative state or response law
that preserves the broad information the incumbent already has. Repeating
nearby ranks, damping or generic trace repairs has diminishing value. Keep
room for a different conditional/distributional approach and retain the small
learned-source reserve; neither automatically becomes the next task.

This is our adaptation and engineering of the public cumulant/Wick framework,
not an unchanged published submission. Standard harmonic and Gaussian identities
are credited as such; there is no academic-priority claim. A short final
[primary-source cross-check](LITERATURE.md) found no ready replacement and
records the limits of transferring ICA sketches, harmonic factorization and
conservative low-rank schemes to this problem. Full forecasts and scoped reopening triggers
are in [CANDIDATE_SELECTION](CANDIDATE_SELECTION.md).

Completed **240.04 active research minutes**: 70.46 written
mathematics, 154.31 empirical work, 2.31 focused literature
and 12.96 selection. Elapsed through record closure: 324.30 minutes,
including 56.39 interruption minutes and 27.87 administrative
minutes, both excluded from the floor. The original estimate was255–330 elapsed
minutes. Final verification/commit after the recorded endpoint is also excluded.

The inventory retains 20 full-shape calls on two exposed networks (six scored
calls included), 18 generated trajectory/bridge/capture records, and
36 completed native constructor bills among 42 attempted-result records.
P01–P57 include algebra, engineering and diagnostic probes, not57 independent
algorithm tests. New moment sampling used262144 points on one generated network;
actual F0 moment evidence was reused. No new challenge targets or fits.

[Timing](TIMING.json), [machine-readable result](RESULT.json), and
[evidence inventory](EVIDENCE_INVENTORY.json) retain the detailed accounting.
Failed/interrupted runs, corrected interpretation labels, source hashes and
strongest positive generated capacity results are preserved.
