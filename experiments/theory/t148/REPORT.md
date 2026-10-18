# T148 — conditional fourth-metric recurrence on V29

T148 recovered after a system crash and continued from its saved scratchpad.
Final completion and exact phase durations are recorded in [TIMING.json](TIMING.json)
and [RESULT.json](RESULT.json). No candidate was executed or submitted.
The incumbent remains **ALG043-V000 / submission330597**, official adjusted
score **5.419051334510831e-9**.

**Recommend T149: one bounded attempt at H148-CMF2**, the conditional
fourth-metric correction. Save **H148-FAR-CT** as an optional cheaper fallback.
Neither has measured challenge accuracy. The
[selection](CANDIDATE_SELECTION.md), [fixed formula](CMF2_SPEC.md), and
[native implementation handoff](IMPLEMENTATION_HANDOFF.md) contain the concrete
next step; T149 is proposed, not started.

## What the preferred candidate changes

The incumbent approximates one part of its fourth-order state with a constant
metric2I. The exact object is the supplied weight Gram, W W^T. Computing that
matrix alone is manageable; carrying all its source effects would be costly.
The new proposal predicts a useful part of it from information the recurrence
already has: its covariance, the actual weight-row lengths, and two directions
formed from the preceding mean and covariance.

The prediction combines a covariance term with a correction in those two
directions. Its coefficient is derived analytically after conditioning on the
row lengths. In an isotropic background plus a captured spike it recovers the
metric exactly in real arithmetic. More generally it is an optimal *restricted
linear predictor* under the stated weight model, not the full conditional
expectation and not an optimum for the final challenge score.

The main engineering result is that the modeled single-fourth source can be
written using the incumbent's two dense A/P factor families plus only two
additional dynamic vectors. The current fourth slices and source use the same
metric. The estimated extra arithmetic is **2–5B FLOPs**, roughly **0.36–0.90%**
of settled V29; this needs about **0.36–0.89% lower raw error** to pay for itself
at the same call lifecycle. These are static estimates, not measured resources.

A substantial correctness issue appeared during the derivation: those two
vectors must undergo the same age-dependent projections as A/P. Keeping them
on the existing uncompressed thin-vector path can destroy an essential
cancellation. The final specification includes the aligned transport, the
correct asymmetric fourth-slice orientations, and consistent repeated-moment
repair. It keeps the published coefficients, ranks and age gates fixed.

## Why the forecast is cautious

The reference implementation's `use_avg_metric` description reports only a
small empirical MSE/FLOP effect from using the exact metric. Its inspected
scope supplies no paired V29/width1024 result, but this is adverse information
for expecting a large gain. [Pinned reference source](https://github.com/alignment-research-center/mlp_cumulant_propagation/blob/93d091a4c26c042bfffa28f2e76a81bc0aba94bb/src/mlp_kprop/kprop_harmonic.py).

Generated examples show that useful metric information can be recovered, but
better reconstruction of a modeled source need not reduce final error. Other
omissions, fixed calibration and compression may cancel part of the existing
error. One broad-spectrum example even slightly preferred one direction to
two on source error. These examples are mechanism evidence, not a local score
or a basis for claiming90% private-success probability.

My subjective planning range is **25–45%** for a useful compliant official
improvement from the bounded attempt, with **2–15% adjusted improvement if it
works**. The uncertainty is wide. The usual small screen must supply the
roughly90% local support before a submission; no2% minimum-gain gate is added.

## Other progress and its limits

| Route | Result of the round | Current disposition |
|---|---|---|
| Far-repeated CT feedback | The shipped simplification omits one leading feedback path; restoring it uses existing factors. The public B2 loss tested a different change. | Fixed cheap fallback, roughly20–35% subjective chance of useful official gain and1–5% conditional gain. No automatic second attempt. |
| Native homogeneous state | Derived cheap fifth-order gate/feedback terms and a sixth-order source using existing vectors. Small coefficient checks pass. | Best larger-upside reserve. A finite update and core-calibration convention still need selection; no completed native algorithm or resource result. |
| Joint core and metric | Derived a small conditional correction for the core as well as the metric. | Reserve: the public coefficient was fitted at the preactivation, so an added covariance component could be counted twice. |
| Fourth-core vector queries | Derived and checked affordable queries through the specified low-degree terms. | Higher mixed sectors still produce expensive row-dependent queries. |
| Whole-matrix spectral metric | Related multiplicative-noise literature led to a degree-two matrix predictor. One limiting example reduces linear Gram residual risk9.09%. | Its naive source realization adds about225B FLOPs. That closes this implementation choice, not the spectral family. |
| Positive-cone state | Extended centered angular moments and identified the next required contraction. | Exact homogeneous equivalence still lacks an affordable finite closure; the broad exact-invariance theorem does not rule out useful approximations. |

The larger-upside preference was applied after the cheap ideas were available.
The HGC and whole-matrix developments are real progress, but neither became
a better near-term complete candidate during this round. The disappointing
part is that these promising identities still do not amount to a demonstrated
new algorithm. Their remaining gaps are listed concretely in
[RESERVES.md](RESERVES.md), so the next recurrence can resume there instead of
repeating a broad search or assuming the routes failed.

## Literature, checks and research style

The [focused reading](LITERATURE_NOTES.md) covers Gaussian/spherical quadratic
conditioning, conditional cumulants, finite closure and matrix estimation.
The16 local new labels contain **15 newly indexed unique sources and one revisit**:
L110 duplicates existing L38 and is marked as an alias. Existing paper/code
and other relevant sources were also revisited. These are selected-section
readings, not16 full-paper proof audits. General EP and covariance-shrinkage
results do not directly solve the present forward-estimation problem.

The published framework supplies the cumulant/Edgeworth and L211 structures.
The conditional approximation and its cheap source realization are our proposed
adaptation. The fallback restores a published lean-source term; academic
novelty is not required. [ARC paper](https://arxiv.org/html/2605.05179v2),
[public V29 source](https://github.com/504aldo/whest-p2-cumulant-k3/tree/18c17e2d7a9aeacd399cfc2c6b571e4e16dbfb45).

This round was deduction and implementation reasoning, supported by15 small
generated algebra/geometry check records. It involved no challenge inputs,
target access, new predictions, training, candidate coefficient/rank sweep,
package or upload. An analytic online least-squares coefficient is used in
the proposal; no dataset is used to fit it. Existing author-fitted V29
parameters remain part of the parent. The [evidence map](EVIDENCE_MAP.md)
distinguishes checked identities, illustrative geometry, corrected draft
formulas and untested claims; it is not an extra submission test suite.

Actual useful time: **121.19 minutes derivation,30.10 literature,30.14 selection**,
**181.43 minutes total**. Elapsed through records: **233.77 minutes**,
versus180–220 estimated; the **27.36-minute** crash/recovery exclusion
accounts for the overrun beyond the upper estimate. Removing only that interval
gives206.40 elapsed minutes.

Category clocks are measured separately. Crash/recovery, intake and final
bookkeeping are excluded from the research floors. Per-route time was not
measured and this single round must not be counted in full for every branch.
No agents or idle waits were used. Retained official return is pending a future
test, not the sum of the mathematical proxy improvements.

## Next task

[Proposed T149](NEXT_PROPOSAL.json) implements one fixed CMF2 variant in the
qualified Python/Whest path, meters it early, and compares against the reused
12-network T147 panel. Initial engineering budget60 active minutes,
reassessment30; one concrete finite extension of at most30 minutes if warranted.
Normal elapsed estimate60–120 minutes including grading. Use the ordinary
roughly90% support rule and at most one useful extension to24 networks. A
qualified supported win can be submitted under that task's owner authority.
No ablation campaign, refit or rank ladder is planned. Normal grading allowance
is30 minutes per attempt with at most one unchanged generic-error retry.
