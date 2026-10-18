# T155 — why the recent candidates lost, and what can be repaired

**The largest failure has a specific, partly repairable mechanism.** HGC6-A
reused a calibration floor that is unsuitable for its transformed state.
Changing that floor removes most of its deterioration on two diagnostic
networks, but the repaired version still loses. CMF2 improves the intermediate
metric it was designed to predict, yet does not improve final mean accuracy.
The precise causes of SCP-A's and FAR-CT's smaller losses remain less certain.

Retain **ALG043-V000 / submission330597**, official adjusted score
**5.419051334510831e-9**. No new upload. The owner-authorized FAR-CT attempt
preceded this investigation and is complete as T154. T153 recurrence has not
started. This report does not add a standing protocol or extra submission gate.

## Results that required explanation

Each row below uses the same12 reused development networks and the frozen
production implementation. Positive changes are worse. Added compute is the
settled FLOP increase; adjusted scores use the actual cost of every call.

| Candidate / task | Raw error change | Added compute | Adjusted score change | Adjusted wins |
|---|---:|---:|---:|---:|
| SCP-A / T151 | +4.510% | +3.756% | +8.418% | 0/12 |
| HGC6-A / T152 | 8.438× parent | +1.507% | 8.564× parent | 0/12 |
| CMF2 / T149 | +0.347% | +0.736% | +1.074% | 6/12 |
| FAR-CT / T154 | +0.690% | +0.0159% | +0.708% | 3/12 |

FAR-CT passed its source/fallback checks and all15 full-size resource calls.
Its adjusted-win bootstrap support was.00005. No extra cohort or upload was
justified. [FAR-CT report](../../submission_policy/t154/REPORT.md).
All four original candidates passed their full-size resource checks; these
were competitive losses, not failed packages or nonfinite-output failures.

## Why more compute did not help

These algorithms spend extra arithmetic changing a biased approximation.
They are not increasing the number of independent samples of a fixed
estimator. A more complete tensor, or a closer approximation to one component,
can make the final answer worse if another approximation relied on its error
or if the new component changes the meaning of the propagated state.

For parent error e and candidate prediction change d, the exact decomposition is

    change in mean squared error = 2 mean(e*d) + mean(d*d).

The proposed change must point usefully against the parent's error, by enough
to outweigh its own size. The desired-correction cosine is−.090 for SCP-A,
+.096 for HGC6-A, +.081 for CMF2, and−.008 for FAR-CT. All are weak; HGC's
change is additionally enormous. Mean offsets account for less than1% of each
change's energy, so a simple common-bias subtraction would miss the problem.
Cold/steady numerical differences are much smaller than these changes,
particularly HGC's. [Full decomposition](SAVED_ERROR_GEOMETRY.json).

Even an optimally rescaled prediction change, chosen retrospectively on this
panel with free access to the parent output, yields only.917% raw gain for
HGC and.664% for CMF2. Those optimistic gains are smaller than their added
compute percentages. SCP and FAR prefer a negative scale, with FAR's best
possible gain along this observed direction only.0068%. These are descriptive
oracle calculations, not fitted submissions or forecasts. They make a generic
damping sweep a weak next step.

## HGC6-A: a calibration floor drives accumulated state distortion

HGC changes the covariance and higher cumulants to exploit a degree-one
homogeneity identity, then regenerates a fourth-order core from the changed
state. Its inherited adaptive rule was calibrated on the parent's physical
state and multiplies a positive table coefficient by a ratio clamped to
**[0.5, 2]**. That lower floor is consequential.

On both traced networks, the converted core rapidly shrinks and becomes
negative by layer5. On row750, its mean is.592 times the parent after the
first conversion, .326 after the next, .066 after the next, and−3.87 by
layer15. The positive lower clamp keeps further conversions running even as
the representation moves far from the one on which the rule was fitted.
By layer15, mean covariance variance is about6.5% below the parent's. Row976
shows the same pattern (core−3.69×, variance about5.8% lower).

Negative formal cumulants are not inherently illegal. The issue is the
combination of repeated conversion, regeneration and an inherited rule that
does not follow the transformed state. This behavior begins before old-source
confinement starts, and a direct confinement intervention leaves it intact.

The targeted tests give the following raw-error ratios:

| Diagnostic intervention | Networks | Raw MSE / matched parent |
|---|---:|---:|
| Original HGC6-A | 2 | 8.585× |
| Remove the mean anchor | 2 | 9.063× |
| Change adaptive lower floor from0.5 to0 | 2 | **1.105×** |
| Remove old-source confinement in HGC and parent | 1 | 8.737× |
| Replay the parent's fourth core and coefficient into HGC | 1 completed | 579.770× |

The floor change keeps the core positive on both networks and greatly reduces
the covariance drift. It cuts about87.1% of the original diagnostic MSE,
removing about98.6% of its excess over the parent. However, the individual raw
ratios are1.010 and1.209: **a substantial partial repair, not a competitive
algorithm or a submission-ready result**. It was selected from the internal
trace, registered before execution, and tested once; there was no coefficient
grid or target fit.

Removing the anchor does not repair the problem. Removing shared-basis
confinement also fails to repair it; residual/feedback rank16 approximations
remain in that intervention, so this does not exonerate every compression.
Replaying only the parent's core is a deliberately incompatible diagnostic
and makes matters much worse: a physical core cannot simply be inserted into
the transformed covariance/third state. That result argues for a **consistent
state convention**, rather than replacing one array or refitting one number.

There is also strong cancellation between channels. On row750, terminal
variance, third-cumulant and fourth-cumulant changes individually move the
prediction by RMS0.00103, 0.000946 and0.000854, while the net prediction change
is only0.000415. A decomposition of all16 substitutions into the terminal
formula reproduces the shipped predictions to about5e-8 RMS. This explains
why isolated state replacement can be disastrous. It attributes terminal
effects; it does not identify an upstream true moment error.
[Terminal attribution](TERMINAL_ATTRIBUTION.json).

**Confidence:** high that the lower clamp causes much of this implementation's
large deterioration on the examined networks. The exact cause of the remaining
10.5% mean raw loss is unresolved. A generated scalar check confirms the
implemented first-order local conversion against an independent Euler/Stein
derivation, so no simple local sign or derivative error was found.
[Check](LOCAL_HGC_IDENTITY_CHECK.json), [derivation](MECHANISM_NOTES.md).

**Credible repair direction:** carry a calibration/state representation that
remains consistent through the transformation, or propagate a controlled
perturbation around V29 with the leading omitted mixed responses. The finite
HGC program adds single fifth/sixth vertices but omits mixed terms such as
third×fifth that can already matter at first order in the conversion strength.
Those are a specific remaining hypothesis, not a demonstrated cure. More rank,
reinstating the parent core alone, and ordinary output damping are not supported
repairs by this evidence.

## CMF2: the predictor works, but the intermediate objective is insufficient

An added observer computed the exact supplied-weight Gram W W^T at each
nonterminal metric update. The conditional predictor reduced squared metric
error at **all28 inspected updates** across two networks. Its error ratios
relative to the isotropic metric range from.349 to.917: improvements of
about8–65%.

Holding the candidate's approximate fourth core fixed, its modeled3+1 fourth
slices are also closer to the exact-metric version at every update, and its
modeled2+2 slices improve even more. These comparisons are **not true
fourth-cumulant targets**; they isolate the quality of the metric within the
same approximate core model. The instrumented estimator reproduces the
original predictions byte for byte.

Thus the conditional metric predictor is not simply broken. On the full12,
CMF2 achieves8 raw wins, but larger losses on other networks outweigh them;
compute adds another penalty. The desired final correction is only weakly
aligned with the metric-induced prediction change.

**Best hypotheses:** the remaining approximate core, its correlations with
the metric, omitted response terms, or source compression dominate the useful
metric signal. In particular, better separate core/metric estimates need not
give the right product when both depend on the same weights. Reusing a fitted
core coefficient can also preserve compensation for the old metric. The
current evidence does not isolate which of these dominates.

**Repair direction:** develop a joint core/metric or future-response correction
that targets the final observable, while preserving or explicitly replacing
the fitted covariance component. Merely increasing the metric predictor's
rank is poorly motivated: it already improves its intended proxy, including
on the network with the largest CMF2 loss.

## SCP-A: correct initial conversion, then a different finite closure

On the one completed trace, the first angular-to-physical variance and third
cumulant agree with the parent to roughly5.2e-7 and3.8e-7 relative RMS. The
first regenerated physical core is also essentially identical. This supports
the initial radial conversion and source bookkeeping.

The next nonlinear update introduces a roughly.93% relative change in the
virtual physical third cumulant; subsequent means diverge. This occurs before
old-source confinement starts. The core remains close to the parent throughout
(about1% higher at the end), unlike HGC's collapse. The final mean change is
about2.1e-5 RMS, and its direction is slightly harmful across the full12.

**Best hypothesis, with moderate confidence:** changing the input-law
representative changes the bias of the finite nonlinear closure. The exact
radial identity survives; the approximation does not commute with that law
change. Mixed radial responses omitted by the candidate and the residual
third-source approximation are plausible contributors. The initial conversion,
a large calibration collapse, and old-source confinement alone are weaker
explanations. I have not isolated one erroneous or missing term.

**Repair direction:** examine the first nonlinear angular update's mixed
third/fourth responses before investing in more radial parameters or a rank
sweep. A representation-consistent tangent correction may be cheaper to
understand than another complete angular propagator. The broader angular
approach remains open; this fixed spelling lost.

## FAR-CT: a valid missing term is almost orthogonal to the needed correction

The fixed candidate adds exactly the specified covariance–third source term.
Dense reference contractions, its birth repeated slice, transported slices
and fallback checks pass. Its predictions first change at layer3 and then
drift gradually. Its final correction is almost orthogonal to the parent's
error, so the added squared change is nearly all downside in the MSE identity.

**Best hypothesis, with lower confidence:** completing this coefficient in
isolation disturbs cancellation with the other omitted terms or the retained
rank16 feedback/source approximation. The tensor derivation is not an
end-to-end optimality argument. No integration bug was found in the affected
contractions, but the present diagnosis does not prove which remaining
approximation makes the correction unhelpful.

**Repair direction:** only reopen this term as part of a motivated coupled
response change or better feedback representation. Its almost-zero useful
projection makes a standalone coefficient adjustment a low-value next task.

## What this changes about the research strategy

The disappointing part is the bridge from a correct local derivation to the
final score. We overestimated how reliably improving a surrogate tensor or
changing to an equivalent exact law would improve a calibrated, truncated,
iterated estimator. CMF provides direct evidence of that gap. HGC exposes a
specific dynamical incompatibility that the original formula checks did not
address. Those checks did what they claimed, but answered a narrower question.

This does not justify abandoning ambitious algorithms or adding a large
validation battery. The lean tests supplied the intended feedback. The useful
adjustment is to make the next substantial hypothesis address a measured error
channel and its state convention. A cheap trace or one selective intervention
can then distinguish causes if it fails. Preserve larger-upside options;
the partial HGC repair should not automatically take priority just because
it is easy to implement.

Recommend the proposed **T153** with its existing time proposal, updated to
focus on joint core/future-response information and a distinct observable-state
alternative. Keep transform-consistent HGC repair as a specific research lead.
No untouched submission-ready candidate remains among SCP-A, HGC6-A, CMF2
and FAR-CT. The zero-floor HGC variant was tested diagnostically and still
lost; broader repairs are unimplemented. [Updated proposal](NEXT_PROPOSAL.json).

## Evidence limits and reproduction

This task reused the four sealed12-network comparisons, performed14 completed
full-size diagnostic calls and three failed diagnostic attempts, and added a
small generated local identity check. The diagnostic rows750 and976 were
selected after seeing the old results; no confidence level or private-score
claim is inferred from them. No fits, parameter sweeps, agents, uploads or
final-blind access occurred. Observer-only parent/HGC/CMF and the completed
SCP replay match original predictions exactly.

The core-replay test's second row hit a flopscope operation-accounting
SystemError twice, including one unchanged-source fresh-process recovery.
The instrumented SCP replay also failed on its second row. Both completed
first rows and all failure logs are preserved. Those two analyses therefore
have a one-network limitation; the successful clamp repair has two networks.
These exceptions arose in new diagnostic work and did not cause the earlier
production score losses. [Execution record](EXECUTION_SUMMARY.json).

Run analyze_saved.py, analyze_interventions.py and terminal_attribution.py
with tmp/t128-runtime312/bin/python from the repository root to reproduce
the analyses. INTERVENTIONS.json and its dated addition freeze every source
and question before execution. Run run_intervention.py with a registered
variant name only in a new output directory; preserve existing results.
[Interventions](INTERVENTIONS.json), [results](INTERVENTION_RESULTS.json),
[timing](TIMING.json). No further experiment is running.

Completed in **27.60 elapsed minutes** versus the45–75-minute estimate, including24.95 minutes of investigation/overlapping execution and2.65 of final records/verification. No minimum applied. Reusing sealed predictions and established execution code made this shorter than anticipated.
