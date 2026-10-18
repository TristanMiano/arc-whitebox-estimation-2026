# T166 — Broader empirical research recurrence

**One small submission nominee, and a larger physical-model lead that remains
unfinished.** ALG051-V000, submission332018, remains the official incumbent at
adjusted score4.368514231311302e-9. This task made no official submission.
Measured active research time was **241.06 minutes**: 135.69 derivation,
59.36 empirical work, 30.26 literature, and
15.74 selection. Overlapping compute is counted once; administration and
seven conservative minutes of context recovery are excluded.
[Full timing](TIMING.json).

The practical nominee changes how we learn the missing mean correction. The
larger lead retains substantially more fourth-moment information late in the
network. The recurrence also tested stochastic compression, conditional
reconstruction, angular normalization, function controls and error attribution.
Several attractive capacity arguments failed when converted into recurrences.

## What is ready for a bounded attempt

[P45](sources/P45_final_source/estimator.py) replaces the incumbent's linear
terminal correction with a small nonlinear source model. It learns from the
same32 training networks, using their intermediate-layer mean labels in
addition to final labels. The source is propagated through the unchanged
physical trajectory. Training and its labels are absent from inference.

| Evidence | Result | What it establishes |
|---|---:|---|
| Four whole-network folds,24 fitting /8 held networks per fold |2.79% lower mean raw error than a matched old-head refit;27/32 wins | Promising adaptive research evidence for the fixed recipe |
| Individual fold ratios |0.9830,0.9826,0.9627,0.9601 | Improvement is not confined to one fold |
| Worst individual held-network ratio |1.02314 | A preserved2.31% loss, not universal improvement |
| Network bootstrap,50,000 resamples |90% ratio interval[0.96458,0.97969]; all resampled means favor the new recipe | Descriptive support on reused exploratory data, not private-suite odds |
| Native full-size implementation |479.295695B versus479.271895B FLOPs | Overhead is0.00497%, well below the CV effect |
| Native/offline prediction agreement |RMS2.40e-8; first15 outputs byte-identical to incumbent | The prepared implementation matches its intended inference closely |
| Native F0 comparison |1.19% worse raw error | A fitting-input loss; preserved without another fit to erase it |

The prepared full32-network asset is different from the24-network fold assets.
Its fitting error is only0.19% below a matched full-data linear-head refit.
The better CV result is consistent with local supervision reducing overfitting,
but adaptive family selection and different training-set sizes limit that
interpretation. No new paired submission panel or archive qualification was
performed. Those are the remaining checks for the shipped asset.

My subjective forecast is **80–90% probability of an official improvement**,
with **1–4% adjusted reduction conditional on success**. This is deliberately
less confident than the bootstrap result. The source, weights and identities
are saved; no algorithm ID has yet been assigned.

**Recommend T167:** freeze/register the exact P45 package, make the usual small
paired comparison with ALG051, qualify it and submit if supported. Keep this
bounded; a clear result does not need a larger local validation campaign. The
standing grading allowance is60 minutes per attempt, with one unchanged retry
for a generic evaluator failure. T167 is proposed only.

## What offers the larger possible gain

The proper dual-state model shares lower moments between two closure rules
while preserving separate harmonic and richer fourth states. A fixed late
switch activates this coupling at layer8. It is distinct from averaging two
final answers: the shared lower trajectory changes at each later layer.

| Generated width | AUG3 reference MSE | Late proper-dual MSE | Raw reduction | Sparse-birth raw reduction |
|---|---:|---:|---:|---:|
|256 |9.1554e-7 |5.3997e-7 |41.0% |32.5% |
|384 |4.0388e-7 |2.3217e-7 |42.5% |25.1% |

These are generated-network comparisons against AUG3, **not measurements
against native ALG051**. The late384 version also beats its full-history
counterpart by16.9%. This makes the information mechanism worth retaining.

A fixed sparse schedule generates new all-distinct fourth information only at
layers8,11,14. It still transports the state and repairs repeated fourth
moments on every layer. This retains79.1% and59.0% of the full late schedule's
raw improvement at256 and384. Fewer updates do not automatically mean a better
adjusted score: the saved work must outweigh the lost accuracy.

The measured projected fourth-birth component is34.89B FLOPs per call, down
from61.35B for the earlier larger projection. Seven useful late calls total
244.23B; three sparse calls total104.67B. **Neither is a complete bill.** The
component assumes a supplied compact third state, whereas the incumbent keeps
shared320/192-dimensional histories and additional thin feedback terms.
Transport, repeated repair, compression and extra lower-state updates remain.

The tested shortcut—replacing the entire third state by a128-dimensional
core—loses the benefit. Exact current repeated moments do not rescue it;
restoring the next layer's repeated moments also fails. A96-dimensional
third-only shortcut has2.67 times the reference raw error. Its cost saving
cannot offset that loss even at the optimistic multiplier floor if transferred.
These exact variants should stop receiving nearby rank or repair sweeps.

A narrower final probe, P53, compresses the third state only inside the
fourth-birth query while preserving it for lower updates. It retains41.40% raw
improvement at256 and39.61% at384 (P54), retaining93.17% of the wider
full-birth benefit. This identifies a better approximation target than replacing
the whole third state; obtaining that compact query cheaply remains unresolved.
The whole-state failures therefore do not close this narrower route.

The [cost frontier](COST_FRONTIER.json) explains the remaining difficulty.
Hypothetically transferring the measured raw gains to the native479B base
leaves about89–110B for all missing full-schedule operations after its birth
subtotal. Sparse leaves56–126B. These are sensitivity calculations, not actual
budgets or native forecasts. They identify a concrete next question: can the
actual native third-history query and complete late fourth update fit together?

I estimate **15–25% probability** that this route produces an official win
within another8–16 hours, with **5–20% adjusted reduction if successful**. The upper end requires a
further substantial cost reduction, beyond the measured components.
A short complete-construction investigation should come before a full port.
The cheaper nominee should not displace this larger lead from future research.

## Why several other approaches failed

- **Unbiased fourth-source sampling:** favorable noise diagnostics on a fixed
  trajectory did not survive actual recurrent use. Three fixed random-source
  recurrences lost; averaging them still lagged the deterministic control.
  Conditional unbiasedness does not remove nonlinear propagation bias or
  accumulating variance. Nearby small-bank variants now have low value.
- **Selected-coordinate reconstruction:** a useful local restriction identity
  did not yield a stable global recurrence. Direct interpolation diverged.
  A covariance-based reconstruction with a metric-only positive shift completed
  but lost43.5% in raw error. Local exactness and a bounded reconstruction metric
  were insufficient to preserve the interactions needed downstream.
- **Angular normalization:** exact weighted angular information had small-width
  capacity. Finite inverse-radius expansions and a support-preserving radial
  ansatz failed. The actual-width oracle comparison was too noisy to establish
  a useful advantage. This family remains open only with a materially different
  tractable joint law; the tested scalar approximations are closed.
- **Function controls and single-site integration:** the measured variance or
  model-error reductions were too small relative to their cost. Some corrections
  improved a Gaussian baseline but worsened the stronger cumulant baseline.
  A useful identity alone did not produce a competitive estimator.
- **Extra local/history features:** final-only neural fitting, fixed causal
  histories and coherent-path features did not add a meaningful gain. The
  successful supervised-source change used additional intermediate labels;
  it was not a larger parameter sweep over the same terminal objective.

One failure classification required repair. Initial negative-variance guards
also rejected a successful matched control. Those stops were inconclusive.
After correcting the overstrict guard, one candidate genuinely diverged and
another completed with an accuracy loss. The original failures and corrected
runs are both preserved; numerical rejection is not substituted for evidence
of an algorithmic loss.

## What the error diagnosis says

Using known intermediate means to define exact local error sources creates an
algebraic decomposition of the terminal error. The mean-only oracle removes
about80% of the physical parent's error on the32 fitting networks. This does
**not** mean80% is recoverable from the current features: the oracle supplies
information unavailable to an estimator.

Intermediate labels are Monte Carlo estimates, so their noise matters. A
separate simulation, using the published sampling budget and the same response
operator, estimates that noise explains about one-third of the earliest source
error but less than1% after the early layers, and about0.065% at the final
source on F0. The unexplained late error is largely missing information or
model bias, rather than inaccurate labels. More informative joint-state
observables are a stronger research direction than simply obtaining more
precise labels or tuning the present small network.

## Research balance, provenance and reproducibility

The work remained primarily deduction and model design, interleaved with
empirical tests. The small nominee is explicitly a learned method: a644-parameter
network trained with local and terminal-response losses. Most physical-state
probes used fixed mathematical changes, fixed ranks/schedules and recorded
controls. There was no broad hyperparameter search or new-data expansion.

The [scratchpad](SCRATCHPAD.md) contains the equations and interpretation;
[probe ledger](PROBES.md) records prospective questions and outcomes. The
[literature notes](LITERATURE.md) record26 task-local sources with their actual
reading scope and limitations. Not all sources were read as complete papers.
Relevant learned-closure and reduced-state literature informed the supervision
and memory questions without supplying an ARC-ready implementation.

P45 is **our learned adaptation of the public504aldo/V29 cumulant framework
and our ALG050/ALG051 changes**. It is not a pure copy of a published submission.
Learned closures and local/trajectory losses are established ideas; no academic
priority claim is made. The dual-state and sparse-birth combinations are
likewise project adaptations within published cumulant machinery.

[Candidate selection](CANDIDATE_SELECTION.md) lists untested work, probability
and gain ranges, and diminishing-return estimates. [Evidence inventory](EVIDENCE_INVENTORY.json)
distinguishes full-size calls, generated response/trajectory records, component
bills and failures. Raw training labels and label-derived source arrays are
kept out of Git. No protected blind data, agents or official uploads were used.
