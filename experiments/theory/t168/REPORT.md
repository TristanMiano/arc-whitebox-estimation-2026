# T168 — affordable fourth-state recurrence

**Completed 241.91 active research minutes. No submission-ready nominee;
one concrete larger development lead.** ALG052-V000/submission 332641 remains
the official best at 4.285182274373245e-9. No upload, agents or final-blind access.

The main advance is a cheaper way to supply third-moment information to a richer
fourth-moment state. A gate-derived analytic proxy is transported through the
actual layer, while the ordinary physical third recurrence stays intact. Sharing
only mean/covariance avoids an extra physical cubic state. Reusing old pair
directions and using small covariance eigenspaces then reduce construction cost.

The most useful late finding was that an expensive mixed-interaction family can
be omitted from the rich repeated-moment target with only 0.8–1.8% raw deterioration
relative to the C1 version on the two generated cases. This potentially removes
an 11.22B-FLOP standalone component per update. The final combined design retains
**21.31%/22.23% raw improvement**.
These are gains over generated AUG3 controls, **not measured gains over ALG052**.

## Capacity and cost

| Retained exploratory design | Raw reduction, width 256 | Raw reduction, width 384 |
|---|---:|---:|
| Expensive source-only reference + C64 | 36.55% | 44.32% |
| Gate-derived proxy, full previous-repeat repair | 32.90% | 31.68% |
| One proxy family | 31.11% | 26.20% |
| Mean/covariance sharing + warm compression | 24.08% | 25.34% |
| C1 hard interactions | 25.18% | 23.21% |
| Omit hard interaction family | 23.81% | 22.58% |
| Final combination: omission + cheap covariance bases | 21.31% | 22.23% |

These are two heavily reused generated networks with fixed reference caches.
They demonstrate capacity and diagnose mechanisms; they are not fresh validation.
P23/P26/P28 initially used the older noisy384 reference. Their original outputs
are preserved, and MATCHED_REFERENCE_RESULT.json records the corrected scores.
The initial loss interpretation of those runs was withdrawn.

Native accounting now includes an exact packed one-family birth operator at
**10.826B FLOPs** per steady update. The final branch's needed middle/output
covariance sketches add **1.418B**. The cheaper current-star reserve has a4.466B
birth component but different capacity evidence. These are component bills:
carried-fourth terms, remaining repeated targets, high lower observations,
transport and the complete recurrence are still unpaid. The first rich update
has 2 old + 38 fresh directions rather than the 32 old + 8 fresh steady fixture. Final-layer
state construction can be skipped, but its mean/covariance observations cannot.

The [scratchpad](SCRATCHPAD.md) derives exact pair operators, centered-Wick
coefficient fusion, weighted hard-graph masks, compact carried-fourth slices,
and a shared bank for direct-third targets and mixed births. Tiny independent
identities support the implemented components. A full implementation should
combine these banks before one compression; adding separately compressed bills
would also overstate some work. [Cost sensitivity](COST_DECISION.json).

## What failed or remains incomplete

An earlier transported proxy fitted its coefficients from postactivation
variances. Those finite-closure variances could be negative or nearly zero,
producing coefficients up to 7.47e8 and a67% wider error increase. Replacing the
fit with preactivation gate formulas repaired the failure on both generated cases.
This was an approximation/conditioning failure, despite a correct transport identity.

The broader alternatives did not produce a cheap nominee. A transported
mean/variance observer lost 1.20%; quartic response jets lost 0.53%; covariance
rays gained only 0.015%,15/32 wins, in fixed four-fold comparisons on the existing
32 training networks. The positive neuron-gauge wrapper had 6.06x adjusted error
on its first actual 1024 development row and was stopped. Nearby fitting sweeps
were not pursued. Carried cubic cores and harmonic/residual alternatives either
cost too much or lost capacity; their positive and negative records remain intact.

The remaining disappointment is practical: the round did not finish a complete
native fourth update or produce a package worth submitting. Its larger-gain
lead is more concrete and cheaper, but not yet established as competitive.

## Recommendation and forecasts

Recommend proposed **T169: a complete native late-layer update**, initially 3–5
active hours, to resolve the remaining cost question before a whole-network port
or local comparison panel. Include all remaining target/observation work and
first/steady behavior. This is research implementation, not a submission attempt.
T169 has not started and requires the owner's next instruction.

My subjective chance of this route producing an official improvement after 6–12h
further development is **25–40%**, with **3–15% adjusted reduction conditional on
success**. That is not a calibrated probability. The
[candidate inventory](CANDIDATE_SELECTION.md) lists untested work, alternative
routes, forecasts, novelty and scoped exhaustion estimates. Zero ready nominees
is an acceptable outcome; a small neural tweak is not substituted for the larger
research objective.

This is our adaptation of the public cumulant framework, using established
low-rank and moment techniques. It is not a pure copy of a published ARC
submission, and no academic novelty claim is made. The
[literature notes](LITERATURE.md) cover 19 primary-source entries and their limits.

## Effort and evidence

| Exclusive category | Minutes |
|---|---:|
| Written derivations | 111.13 |
| Empirical design/prototypes/interpretation | 85.01 |
| Literature | 29.84 |
| Candidate selection | 15.92 |
| **Active research** | **241.91** |
| Administration/context recovery | 25.61 |

Elapsed through records **267.52 minutes**, versus 255–315 estimated
(midpoint error −17.48min). Overlapping compute is counted once;
records/context/idle time do not supply research credit. There are
**45 completed generated trajectory/diagnostic records**, three
observer recipes with 12 fold fits, **1 new actual 1024 estimator call**,
and **19 native component meter records**. Counts do not mean that
many independent algorithms or networks. Guards peaked at
10.27GB under 13.25GB; failed attempts are retained.
[Timing](TIMING.json), [evidence inventory](EVIDENCE_INVENTORY.json),
[chronological probes](PROBES.md), [result](RESULT.json).
