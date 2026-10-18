# T145 — One extra completion hop loses on the JSP incumbent

**No submission. ALG041-V000 / JSP remains the official best**, submission
330392 at adjusted 1.18330815718e-8. The combined E1-on-JSP candidate
ALG042-V000 raises raw MSE by **2.709%** and adjusted score by
**12.527%**, losing both metrics in all 12 networks.

| Same 12 reused development networks | E1-on-JSP | JSP incumbent |
|---|---:|---:|
| Raw MSE | 3.65350805933e-08 | 3.55715049947e-08 |
| Adjusted arithmetic mean | 1.37847684266e-08 | 1.22501849244e-08 |
| Prediction FLOPs | 829,696,441,070 | 757,303,958,254 |
| Multiplier | 0.377302258617 | 0.344381968832 |

Bootstrap support for an adjusted improvement is 0.0; the 90% mean-change interval
is [1.40645e-09, 1.68238e-09]. The worst network ratio is 1.165734.
Cost rises 9.559%, requiring 8.725% lower raw error;
raw accuracy instead gets worse. This is a clear competitive loss after
resource repair, not an unresolved packaging or evaluator failure.
[Per-network score](attempts/screen-sealed/SCORE.json).

## What was tested

This newly registered combination retains JSP's full main history and fresh
source, plus one extra explicit completion pair. Its complete incoming third
slice feeds both the moment response and JSP source response. After each
activation it replaces the extra pair and repairs repeated entries against
main history, fresh JSP source and the new pair. The old pair's current moment
effects remain, although its explicit all-distinct history is dropped.
[Specification](MATHEMATICAL_SPEC.md) · [registration](START_AND_SPEC.json).

The original H143-E1 proposal was against ALG038. It remains unrun; T145 does
not relabel that earlier hypothesis or test a memory-age ladder. No fit,
new coefficients, damping, added fourth state or compression was introduced.
One comparison used the predetermined 12 reused development rows. Predictions
were sealed before opening targets, with one score look and no extension.
The final blind block remains untouched.

## Engineering and checks

The initial cached-kernel realization passed the full-size fixture at .395691s
residual, then failed the first comparison row at .407169s against the .4s cap.
The batch stopped before targets. A prospectively recorded 15-minute repair
bundles the active J columns with main history for existing chunked transforms,
then splits the owned outputs. This saves 22 separate products at depth 16.
It preserves the equations and separately computed main/J repeated slices.

The repaired fixture uses 829.696B FLOPs versus 829.892B initially, with .369952s
residual. Its output differs by 5.4394e-8 RMS and 4.7684e-7 maximum absolute,
within the recorded 5e-6/5e-5 numerical bounds. All 13 current-source full-size
calls pass: the fixture and 12 comparison networks. Runtime is
43.84–46.09s, residual
0.36995–0.39302s, maximum setup
0.00839s, and peak process RSS 6.406 GiB.
[Repair](REPAIRS.md) · [equivalence](REPAIR_EQUIVALENCE.json) ·
[resources](RESOURCE_SUMMARY.json). The initial failed source and row are retained.

A generated dense reference independently transports complete third tensors and
constructs the coupled JSP source. The initial float32-production versus
float64-reference absolute check failed at 3.90e-5 on a sensitive tiny-network
output near 6.15. With identical weights and both implementations in float64,
the recurrence agrees to 1.1e-14;
deliberately omitting old J changes the output by 1.25. The original failed
precision check is retained, with no tolerance relaxation or challenge-source
conversion to float64. Current generated width 1/2 repair invariants, boundary
shapes and first-two-row checks pass; all 12 full-size outputs retain the exact
first two JSP rows. Existing T142 kernel and T143 tensor checks were reused.
[Generated checks](TRANSLATION_CHECKS.json).

No package qualification, archive or upload followed the clear loss. The shipped
incumbent and its prior official evidence are unchanged. Fifteen total full-size
calls include two initial-source calls and 13 repaired-source calls; these are
not 15 distinct comparison networks.

## What this changes

The extra output correction has RMS 2.90005e-05.
Its squared-change contribution to MSE is 8.41029e-10;
twice its cross term with the incumbent error is
1.22547e-10. Both are adverse here. Most of the
raw loss comes from the size of a correction that does not align usefully with
the residual. This is a description of the same saved panel, not a fitted
coefficient or another experiment. [Diagnostic](RESIDUAL_DIAGNOSTIC.json).

Longer retention carries the information represented by the closure; it does
not add an independent measurement of the true joint moments. A more complete
recurrence of that modeled state need not be more accurate. This test does not
separate the effect of retention from its coupled change to the JSP source,
or prove a general impossibility for memory. It closes the fixed combined
spelling and demotes an automatic longer-memory ladder. Changing bookkeeping
again without a new accuracy mechanism is a weaker next step than improving
how the joint state is represented or generated.

The useful engineering result is the bundled-transform implementation. Preserve
it for future designs with extra factor columns; it is not a measured gain for
unchanged JSP. Q4D's earlier raw gain is also still against ALG038, with no
assumed transfer to JSP.

## Proposed next task and timing

**T146: a focused joint-response literature/theory recurrence.**
Preserve JSP as comparator; prioritize a better justified joint completion or a coherent
omitted source response over retaining more modeled memory. Investigate
response-oriented completion/gauge and coherent triangle/fourth-vertex constructions,
with response-preserving compression as a larger-upside reserve. Reuse T143 literature
and search only named missing ingredients. Keep cheap implementation ideas as fallbacks;
no automatic memory-age, rank or coefficient sweep.

Proposed floors: 120 minutes of derivation, 30 of focused literature, and 30 of
candidate selection—180 useful minutes, with productive continuation allowed;
estimate 180–220 elapsed. T143's 210 useful/250 elapsed minutes produced the
19.33% official JSP gain. Keep two hours of derivation while narrowing generic
literature work because the wider survey is already available. These are
proposed task allocations, not a new permanent protocol rule. No T146 work,
subagents or new candidate execution starts automatically.

Started 2026-09-10T21:16:25Z; score decision 2026-09-10T21:37:57.086018+00:00; main records
completed 2026-09-10T21:42:43.800000+00:00. **26.31 elapsed minutes**, against 35–75
estimated (-8.69 versus the lower estimate). All 15 prediction calls
total 11.24 metered minutes;
current-source calls total 9.74. These overlap work and
are not additive. No grader wait, budget extension, fitting or usage resets.
[Timing](TIMING.json).
