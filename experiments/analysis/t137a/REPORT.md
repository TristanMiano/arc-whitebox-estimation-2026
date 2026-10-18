# T137A — Why CSK3-R made such a large jump

**The strongest explanation is that CSK3-R corrected a large, neuron-specific
error left by our previous approximation to the activation distributions.**
It carries joint non-Gaussian information through the network and lets that
information correct later means and covariances. The observed gain is broad,
survives the official evaluation, and required no coefficient fitting.
The complete estimator is validated by that result; the contribution of each
part of its recurrence remains unmeasured.

The owner reports rank **32**, up **44 places**. That rank is owner-reported;
this analysis uses the retained official score receipts rather than a new
leaderboard snapshot. Rank movement depends on the other scores. Our measured
algorithmic improvement is **7.40-fold in adjusted score**.

## 1. Most of the surprise was accuracy

| Official quantity | ALG037 | ALG038 / CSK3-R | Change |
|---|---:|---:|---:|
| Raw final-layer MSE | 1.28580467731e-6 | 4.26133183851e-8 | **30.17-fold lower** |
| Root mean squared error | 0.001133933 | 0.000206430 | **5.49-fold lower** |
| Effective score multiplier | 0.100000 | 0.407602 | **4.076-fold higher** |
| Adjusted score | 1.28580467731e-7 | 1.73692836098e-8 | **7.40-fold lower; 86.49% reduction** |

The arithmetic is `30.17 / 4.076 = 7.40`. Squared-error scoring makes a
5.49-fold reduction in error amplitude a 30.17-fold raw-score improvement.
The extra computation consumed much of that advantage, but left a large net win.

T136 forecast **904.626 billion FLOPs**; the local production meter measured
**896.310 billion**, only **0.919% below forecast**. An unexpectedly cheap kernel
therefore explains very little of the surprise. We knowingly exceeded the
219.902-billion-FLOP discount boundary and bought much more accuracy.

For precision, the official adjusted/raw score ratio is **0.407602230196**,
whereas our prediction meter yields **0.407594600802**. This is a **0.001872%**
relative difference. The table uses the effective official ratio to make its
decomposition exact. We have no official per-network FLOP breakdown here and
do not assign a cause. This discrepancy has no material role in the jump.

Sources: [T137 official receipt](../../submission_policy/t137/SUBMISSION_330141_STATUS.json),
[incumbent receipt summary](../../submission_policy/t137/INCUMBENT_STATE.json),
[frozen forecast](../../theory/t136/DECISION_FREEZE.json).

## 2. What changed mathematically

ALG037 was a substantial hybrid: structured antithetic sample paths, Gaussian
covariance propagation, trace/Hermite response terms, and fitted output
corrections. T135's last change was a joint refit of 27 existing features.
It was already much more sophisticated than plain Monte Carlo or a Gaussian
mean-only approximation. Nevertheless, its richer corrections relied heavily
on sampled summaries and a restricted output-feature family.

CSK3-R instead maintains a deterministic distributional state at every layer:

- a Gaussian reference mean and covariance;
- separate first-order mean and covariance corrections;
- persistent factors representing joint third cumulants, plus a matrix
  completing the modeled entries with repeated neuron indices;
- one fourth-cumulant summary measuring a radial component of shape beyond
  a Gaussian distribution.

ReLU turns even a Gaussian input into an asymmetric activation distribution.
The next weighted layer mixes those activations. Its skew depends on their
**joint** third cumulants, not only the skew of each individual activation:

\[
\kappa_3\!\left(\sum_i w_iY_i\right)
=\sum_{i,j,k}w_iw_jw_k\,\kappa(Y_i,Y_j,Y_k).
\]

Knowing just means and covariances loses this information. Retaining only a
trace of the third tensor also loses many directions. The CSK3-R factors
preserve a richer approximation to it under later weight matrices and gates.
The response then changes subsequent means and covariances, so an earlier
distributional error need not simply flow to the output uncorrected.

For a single preactivation, write the Gaussian reference as
`N(mu, sigma^2)`, with `alpha = mu/sigma`. Its ReLU mean is
`mu Phi(alpha) + sigma phi(alpha)`. The implemented first-order correction is

\[
\delta m =
\Phi(\alpha)a
+\frac{\phi(\alpha)}{2\sigma}D_{ii}
-\frac{\alpha\phi(\alpha)}{6\sigma^2}\kappa_3
+\frac{(\alpha^2-1)\phi(\alpha)}{24\sigma^3}\kappa_4.
\]

Here `a` and `D` contain corrections propagated from earlier layers.
This gives a concrete reason why preserving distributional shape can improve
the requested mean: the ReLU threshold is sensitive to that shape.
The sign and importance of each term depend on the neuron. The direct skew
term even vanishes at `alpha=0`; this is not a universal one-sign correction.

The equation describes an approximate recurrence, not an exact expansion for
every possible activation distribution. CSK3-R drops some all-distinct third
information, most fourth-order structure, and products of perturbations.
Our inference is that the retained terms capture much of the important missing
error on these networks. We have not proved the remaining approximation order.

This general approach comes from the existing
[cumulant-propagation literature](https://arxiv.org/html/2605.05179v2), which
propagates approximate activation distributions without sampling. Its
theoretical guarantees have assumptions and do not automatically transfer to
our compressed ReLU closure. The specific recurrence and omissions are in
[T136's final candidate](../../theory/t136/CANDIDATE_A.md); the deployed mean
response is in [moments.py](../../../submissions/phase2_alg038_v000/moments.py).

## 3. The saved outputs support a broad change in the error

This analysis reused the same 12 development networks and their 12,288
final-layer outputs. It generated **no new estimator predictions or fits**.

| Descriptive check | Finding |
|---|---:|
| Networks with lower adjusted error | **12/12** |
| Smallest adjusted improvement among those networks | **80.19%** |
| Individual outputs with lower raw squared error | **82.02%** |
| Old MSE attributable to a common offset within each network | **1.20%** |
| Reduction in the remaining, neuron-specific MSE | **96.23%** |
| 99th-percentile absolute error | **0.003574 → 0.000663** |

The offset decomposition is exact: within each network, mean squared error
equals squared mean error plus the mean square of the centered errors.
Almost all the old error was in the second term. Thus the observed advantage
cannot be explained by correcting one common additive offset per network.
This does not exclude more expressive neuron-dependent calibration in general.

Sorting outputs into four equally sized groups by their target mean, the new
raw-MSE ratios are **0.0162, 0.0590, 0.0478 and 0.0288**, from smallest to
largest means. The effect extends across the output range.

The calibrated Gaussian comparator ALG035 and the hybrid ALG037 had
substantially aligned neuron-specific error patterns: centered error cosine
**0.695**. ALG037's and ALG038's centered residuals have cosine **−0.012**.
This is consistent with moving past a shared error component into a different
residual pattern. It does **not** prove an orthogonal-error theorem, optimality,
or that the remaining error is reference noise. We have not established a
target-noise floor.

The official adjusted reduction, **86.49%**, is close to and slightly larger
than the local **84.72%**. Together with a single unfitted candidate and broad
local gains, this supports a transferable improvement. The 12 reused networks
are still development evidence, and 12,288 outputs are not 12,288 independent
network-level trials.

Reproduce these descriptive calculations with
`python3 experiments/analysis/t137a/analyze.py`.
[ANALYSIS.json](ANALYSIS.json) records input hashes, formulas' outputs and
per-network statistics. The source arrays are the sealed T133/T135/T137
predictions and previously used T118 targets, with only these 12 rows analyzed.

## 4. Why our forecast underestimated the upside

Before implementation, T136 gave a **15–30% subjective chance of a retained
official improvement**, including operational failure, and a **10–50% score
reduction if successful**. Those were planning judgments, not confidence
intervals. The actual **86.49%** reduction exceeded that upside range by a lot.
One successful attempt cannot calibrate the probability estimate; the clear
forecast miss is how large the win could be.

There were legitimate reasons for caution: the closure was approximate,
untested at the full challenge shape, and needed more than a fourfold raw-MSE
gain to pay for its compute. T137 also encountered real execution failures
before an equivalent refactor made the implementation usable.

But the history contained more positive evidence than a label such as
"old K3 did not work" would suggest. In [T017](../../checkpoint2/t017/REPORT.md),
a restricted factorized third-cumulant implementation achieved a final-layer
raw-MSE ratio of **0.169** against covariance propagation, winning on all
12 synthetic width-12, depth-3 networks. Full-depth work was parked because
its projected cost exceeded the older budget. This was positive shallow
accuracy evidence plus a deployment obstruction, not a full-shape accuracy
failure. The small-network result could not predict the present gain, but it
was a reason to keep the family open.

The current attempt combined that mechanistic foundation with a changed
representation, a cheaper Gaussian kernel, analytic pair responses, fast
matrix products, and the current challenge budget. The paired factors and
separate repeated-index remainder made the richer state practical. We cannot
infer that the same submission was available earlier without that work.

My planning diagnosis is that recent small improvements to sampled/fitted
output corrections anchored the expected gain too closely to that regime.
Adding missing propagated information can remove a large error component in
one step. The cheap calibrated public baseline's near-parity with ALG037 was
also a clue that much of our previous complexity had limited marginal value;
it did not establish which components were redundant.

## 5. What this should change in the next decision

**Prioritize this successful distributional-state family.** We now have
direct official evidence for its value, so the next task can start from a
working mechanism. There are two worthwhile directions: preserve its accuracy
at lower cost, or retain a specifically motivated missing correction.

At the present raw score, reaching the .1 multiplier floor with unchanged
accuracy would give an adjusted score of **4.2613e-9**, about another **4.08-fold**
improvement. That is a conditional arithmetic ceiling for cost reduction,
not a forecast that we can shrink this implementation that far. It requires
roughly fourfold less computation. Smaller equivalent optimizations can be
assessed first without making them a lengthy prerequisite to ambitious theory.

We should also avoid assuming every ingredient is indispensable. The current
comparison cannot divide the win among persistent third factors, the repeated
remainder, covariance feedback, the fourth scalar, or the readout change.
A small targeted removal test could be useful when it decides which state to
compress or extend. A comprehensive ablation suite is unnecessary for another
well-supported submission.

The former A2LR fallback must be re-ranked against ALG038. Cheapness or a
possible small win against ALG037 no longer makes it competitive. Broader
sampling/control routes remain available, but this result gives a strong
reason to spend the next focused effort on the working cumulant recurrence.
Nothing here establishes what other leaderboard participants use.

This is an analysis task, not a new theory recurrence or authorization to
execute the next candidate. T136 plus T137 took **3.50 elapsed task-hours**,
including grading and records, and inherited substantial earlier research
and public work. That return is encouraging but should not be extrapolated
as a guaranteed improvement rate. See [RESULT.json](RESULT.json) for this
postmortem's own measured duration and disposition.
