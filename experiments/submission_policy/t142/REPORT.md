# T142 — Q4D improves accuracy but misses on adjusted score

**Q4D lowers raw MSE by 8.14%, but its resource-compliant implementation is
3.02% worse on adjusted score. No submission was made.** The official best
remains ALG038-V001 / submission 330153 at adjusted 1.46676758754e-8.

| Same 12 reused development networks | Q4D / ALG040-V000 | Incumbent |
|---|---:|---:|
| Raw MSE | 4.16196841904e-8 | 4.53095008665e-8 |
| Adjusted mean | 1.60655997042e-8 | 1.55952916773e-8 |
| Prediction FLOPs | 848,844,195,990 | 756,892,228,334 |
| Multiplier | .386009649442 | .344194735741 |

Q4D wins on raw MSE in **all 12 networks**, but on adjusted score in only **3/12**.
Actual adjusted ratio is **1.030157052**; bootstrap support for improvement is
**.0019**, with a 90% mean-change interval [1.974130302e-10,7.519254511e-10].
The worst network ratio is 1.08935. All predictions were sealed before opening
these targets. This is a single comparison on reused development data, not
fresh validation; no fitted coefficients, extension or final blind-block access.
[Full score](attempts/screen-sealed/SCORE.json).

## Implementation and operational tradeoff

The registered Q4D equations keep the full successful third-cumulant history and
replace the radial fourth scalar with each coordinate's fourth trace and marginal
cumulant. Fixed constraint equations reconstruct a fourth polynomial; its
transported marginal and pair entries feed every inherited analytic response.
Large products are float32; trace/marginal state and analytic responses are
float64. Small-width continuations are explicitly registered.
[Specification](START_AND_SPEC.json) · [final source identity](SOURCE_FREEZE.json).

The initially cheaper implementation exceeded the residual-time cap. Four
bounded engineering changes preserved the equations:

| Production realization | FLOPs | Recorded residual | Outcome |
|---|---:|---:|---|
| Initial, original depth 4 kernels | 812.091B | .43409s | Residual failure |
| Stacked response reduction | 813.318B | .43934s | No benefit; reverted |
| Cache outer kernel views | 813.565B | .40578s | Better, still over cap |
| Depth 2 for new fourth products | 828.297B | .39416s fixture; .400824s first screen row | Batch stopped before targets |
| Ordinary counted fourth products, cached depth 4 elsewhere | 848.844B | .36722–.39110s | All 13 current-source calls pass |

Cached views use counted input copies and return independently owned counted
output copies. The ordinary fourth products reduce Python overhead at a higher
charged FLOP cost. The final implementation differs from the initial fixture
by only 4.49e-8 RMS and 4.77e-7 maximum absolute output. No equation or coefficient
was changed after registration. All unsuccessful probes, the obsolete screen
row, source versions and numerical freezes are retained.
[Repair history](REPAIRS.md) · [equivalence](REPAIR_EQUIVALENCE.json).

The final version runs in 43.73–46.48s,
uses at most 6.356GiB process RSS and
0.00907s setup. All resource checks pass. Generated dense
checks verify fourth constraints/transport, including widths 1 and 2, and the
radial special case reproduces the incumbent pair response. Separate matrix
checks cover cached-view arithmetic, independent output ownership and capacity
fallbacks. The qualified Python 3.12 / NumPy 2.2.6 / FlopScope 0.12.0 /
WhestBench 0.16.0 environment was reused.
[Resources](RESOURCE_SUMMARY.json) · [fourth checks](FOURTH_CHECKS.json) ·
[kernel checks](KERNEL_CHECKS.json).

## What remains useful

This is a positive accuracy result for richer fourth information, unlike the
large raw-MSE losses of the two compression attempts. The current implementation
costs 12.15% more, requiring 10.83% lower raw MSE; its measured 8.14% gain falls short.
More networks are unlikely to change this submission decision.

Holding the **final predictions fixed**, point break-even cost is 823.995B FLOPs;
about **812.815B** gives 90% bootstrap support. At the initial 812.091B bill,
those same predictions would give a 1.44% adjusted improvement and .91375 support.
That is conditional arithmetic, **not a qualified result for the earlier source**:
its residual failure remains, and only a fixture establishes numerical equivalence.
[Cost envelope](COST_ENVELOPE.json).

Keep Q4D as a useful fallback requiring cheaper compliant execution or a cheaper
fourth completion. Reusing the decomposition of the same layer weight across
several matrix products is a concrete engineering question; it has not been
implemented or assigned a performance claim here. The raw-MSE gain does not
establish that Q4D captures all important fourth information. Its omitted
off-diagonal trace and the incumbent's incomplete persistent third-source
response remain possible larger opportunities.

## Recommended next task

Propose **T143: a focused literature/theory recurrence** with at least 120 useful
minutes, including at least 90 minutes of written theory; estimate 120–150 minutes,
with productive continuation allowed. Reuse the existing literature and spend
only about 10–15 minutes on a specific missing-response or implementation question.
Prioritize a credible larger improvement from missing third-source response or
another well-motivated joint correction. Retain the measured Q4D gain and the
concrete cost target as the inexpensive fallback. Compression should reopen
with a response-preserving mechanism, not a generic rank sweep.

This follows the standing balance between cheap gains and larger opportunities.
No recurrence, extra candidate, agents, package qualification or upload starts
automatically. T142 is complete; T143 awaits owner selection.

## Timing

Started 2026-09-08T19:39:41Z; score decision 2026-09-08T20:07:16Z; main records
completed 2026-09-08T20:16:24.324096+00:00. **36.72 elapsed minutes**, versus 45–75
estimated (-8.28 versus the lower estimate). All 18 full-size calls,
including failed earlier realizations, total 13.73 metered minutes; the 13 final-
source calls total 9.78. Those overlap other work. Rough exclusive allocation:
29.7 minutes implementation/analysis/records and 7.0 execution/I/O waiting.
The operational repair episode took about 12 elapsed minutes within its 20-active-
minute allocation; the 60-active-minute task engineering budget was not extended.
No official wait, agents or usage resets. [Timing](TIMING.json).

Final verification and commit preparation completed 2026-09-08T20:21:43.131387+00:00:
**42.04 elapsed minutes** through this point, 2.96 minutes below
the lower estimate. The earlier timing above ends at main-record completion.
