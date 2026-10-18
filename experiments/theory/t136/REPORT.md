# T136 — literature refresh and theory recurrence

**Recommend T137: one bounded CSK3-R implementation and submission attempt.**
This revisits joint third-cumulant propagation with a concrete cheaper
representation. It has greater plausible upside than another fitted output
correction, but a substantial chance of failure. Keep augmented K2 as a cheap
fallback. The final specifications are [candidate A](CANDIDATE_A.md) and
[candidate B](CANDIDATE_B.md); neither has been run on challenge inputs.

The incumbent is still **ALG037-V000**, submission **330101**, official adjusted
score **1.285804677308988e-7**. This task used public sources, written derivations
and small generated mathematical checks. There was no challenge target access,
full candidate prediction, fit, upload or subagent work. Final measured timing
and the conservative useful-work breakdown are in [TIMING.json](TIMING.json)
and [RESULT.json](RESULT.json). The task's floor is120 useful minutes including
80 active theory minutes;150 minutes was an estimate, not a ceiling.

## The main result

Older full-K3 work had promising shallow evidence but an unaffordable original
implementation. Its mathematical representation carries a growing collection
of tensor factors. Two of the three factors in the basic source can be equal,
so they need only one shared transformation. Existing fast matrix primitives
make that observation useful under the current1024-wide,16-layer budget.
The framework comes from the [public cumulant method](https://arxiv.org/html/2605.05179v2);
our compressed recurrence is an adaptation with its own approximation error.

The proposed state keeps one paired factor block from every layer, plus a
single matrix that corrects all third-cumulant entries with a repeated neuron
index. It also keeps a fourth-cumulant scalar and a signed mean/covariance
response around the Gaussian reference. The fresh source matches the Gaussian
tree and exact repeated Gaussian entries. This preserves much more historical
joint information than a terminal scalar shape correction. It avoids a dense
1024-by1024-by1024 tensor and halves the growing-source count relative to the
two-block construction considered first.

The later refinement mattered: keeping only the remainder's trace and diagonal
lost leading repeated-entry response even in a weakly correlated synthetic
case. Retaining its entire repeated matrix reduced that particular transmission
error by orders of magnitude for about5% more total computation. It also removed
the need to compromise the fresh tree curvature. The final source formula is
in scratchpad section22; earlier formulas are preserved as derivation history.

| Option | Projected FLOPs / multiplier | Accuracy requirement and planning outlook |
|---|---:|---|
| **CSK3-R — preferred** | **904.626B / .411376** | Needs raw error below24.31% of ALG037's to win adjusted score. Subjective15–30% chance of a retained official improvement; approximately10–50% reduction if successful. |
| **A2LR — cheap fallback** | **136.853B / .1** | Adds only a third trace vector and fourth scalar. Subjective20–35% chance of a retained improvement; approximately3–15% reduction if successful. |

These probability/gain ranges are uncalibrated judgments including engineering
failure. They are not forecasts from synthetic errors or the .90 support sought
after a useful paired comparison. The upside/time ranges overlap. I prefer
CSK3-R because it tests a larger missing information source with a now concrete
cost plan, consistent with the owner's preference to pursue plausible larger
gains after recording the cheap option.

## What was checked, and what remains uncertain

The mathematical checks resolve specific implementation and selection questions:

- Gaussian pair moment formulas agree with independent conditional integration
  to1.78e-15. Third/fourth derivatives agree with finite differences to about
  7.84e-7 scaled error. The unrolled implementation table agrees with the generic
  derivative formula to2.78e-17 across126 checked entries.
- A small dense tensor verifies persistent two-leg factor propagation through
  four linear/gated steps to4.44e-15. This is algebraic parity, not a depth16
  distribution-closure test.
- In a one-factor Gaussian stress case, the final fresh source matches the
  Gaussian-tree-plus-repeated reference to8.33e-17. Its relative next-cubic
  squared error against the actual Gaussian third tensor was2.15e-8 at
  correlation .05 and .00186 at .65.
- An independent formal non-Gaussian perturbation check exposed the limitation
  of gate-only historical transmission. Full repeated completion reduces its
  next-cubic squared error to .00000403, .000377 and .02990 at correlations
  .005,.05,.65. The last case remains a meaningful weakness.
- High-precision scalar checks found an actual tail problem: naive float64
  arithmetic gives zero third cumulant at standardized mean8. Stable formulas
  recover its small positive value. Rectangular contraction chunking reduces
  peak incremental kernel workspace from2.42GiB to about692MiB.

These are generated mathematical fixtures, not challenge networks, performance
ablation runs or a trained search. Their values do **not** transfer to whole
estimator MSE. The full repeated remainder's all-distinct history is still
discarded after its next nonlinear step. Some correlated nonlinear terms,
non-radial fourth information and products of perturbations are omitted.
Deep accumulated bias, actual FLOPs, residual time and process memory remain
unmeasured. In particular, a roughly fourfold raw-error reduction is a demanding
requirement. This could still produce a clean negative result.

The [pinned public source](PUBLIC_SOURCE_PIN.json), matching remote HEAD at
inspection, warns that cached K>=2 results/counts are stale after changed
diagram truncation. Its factorized AUGMENT is also a different term set from
dense AUGMENT. Old figures and our shallow ALG007-V005 result therefore supply
motivation, not current-shape quality or runtime guarantees. See the
[upstream status](https://github.com/alignment-research-center/mlp_kprop/blob/93d091a4c26c042bfffa28f2e76a81bc0aba94bb/TODO.md).

## What happened to output-aware sample compression

This was a serious initial branch, not a forgotten option. Established
[kernel recombination](https://proceedings.mlr.press/v202/hayakawa23a/hayakawa23a.pdf),
[cube sampling](https://doi.org/10.1093/biomet/asaf058) and
[Gram–Schmidt Walk balancing](https://arxiv.org/html/1911.03071v4) supply useful
construction machinery. The remaining challenge is choosing features that
predict the network's **integration error**, within the bank and suffix costs.

The useful deductions are now explicit: conditionally unbiased compression
adds its residual variance to the bank's existing error; a cap on positive
weights does not by itself give an iid1/m variance bound; and exact feature
balance cancels only the represented component. First-layer quadratic controls
can be centered exactly under the spherical source law, but an attractive
pointwise quadratic fit can target variation the existing QR frame already
cancels. Removing points can bring that error back. One paper-budget bank/
suffix allocation fits at207.387B operations, but has neither a qualified
feature map nor a demonstrated whole-estimator advantage.

Consequently, there is **no sample-compression nominee** from this round.
That is incomplete progress toward an algorithm, alongside useful negative
deductions. Further generic balance/recombination searching now looks less
valuable; reopen with a concrete nonlinear residual feature and a charged
solver. The [route tracker](../../../docs/RESEARCH_ROUTE_STATUS.md) records
this narrower condition and preserves unrelated reserves.

## Next decision and effort

T137 should begin under the usual60-active-minute engineering budget, reassess
at30, and use at most one additional30-minute block only with a recorded
concrete payoff. Expected elapsed time through a supported grade is75–120
minutes, with the existing30-minute unchanged-error retry allowance if needed.
The first integrated full-shape fixture decides whether the new state fits the
real runtime and memory limits. Then use one predetermined twelve-network
paired comparison against ALG037. Approximately .90 support is enough to
qualify and submit; no larger scientific campaign or minimum-gain gate.

Both first attempts are defined without a learned fit. The handoff contains
the [unrolled moment equations](ANALYTIC_MOMENT_KERNEL.md), source orientation,
numerical pitfalls and charged operation plan, so the next task can implement
the algorithm without repeating this derivation. This recurrence was primarily
deduction and source adaptation, with fixed small checks and no parameter
fitting or machine-learning training. A2LR is a fallback to re-rank after the
next result, not an automatic second experiment.

Final timing: **138.79 elapsed minutes**, **120.09 conservatively credited
useful minutes**:83.00 active theory,16.50 literature and
20.59 selection/handoff. The150-minute estimate was
11.21 minutes above observed checkoff time. No idle waiting counted.
The baseline20/80/20 allocation shifted slightly toward theory; both explicit
floors were met. Final record verification and commit follow this checkoff.
