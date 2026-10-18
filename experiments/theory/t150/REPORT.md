# T150 — Develop the larger opportunity before returning to a cheap correction

**Recommend H150-SCP-A, fixed-radius cumulant propagation, for proposed T151.**
H150-HGC6-A is a second specified ambitious option. T149 / H148-CMF2 remains
**NOT TESTED and DEFERRED**. Its frozen specification, T148's other work and
the official incumbent are preserved. No challenge candidate ran in T150.

## What changed in the theory

The useful advance is a change in the distribution that our approximation
propagates. Write a Gaussian input as X=RU, with independent radius R and
uniform direction U. For a bias-free homogeneous network F,

    E[F(X)] = E[F((E R)U)].

The exact target is therefore unchanged when the input radius is fixed at its
mean. The approximate internal moments are different. In particular, random
input radius creates a shared covariance component after the first ReLU; a
fixed-radius state removes that component in the corresponding weight-average
calculation. This is a concrete structural mechanism, not a fitted coefficient
or an output rescaling. Deeper angular norm fluctuations still exist.

SCP-A now has a complete finite specification: initial raw moments, radial
third-order source, fourth-order slices, native source contractions, repeated
entry repair, transport/compression paths and terminal output. A virtual
Gaussian-radius state retains the interpretation of the public calibration
fields. Its marginal prediction provides an explicit mean anchor; the changed
central moments influence predictions at later layers. The mean anchor is a
chosen approximation convention, not an exact distributional theorem.

The extra state is one initial matrix, one initial vector and three vectors
per source. A dense extra matrix is not created at every layer. Static extra
cost is about 20–30B FLOPs, a 3.5–5.1% raw-error improvement hurdle at the
incumbent's settled cost. Actual first-call cost, residual time and accuracy
remain unmeasured. [Fixed specification](SCP_A_SPEC.md),
[implementation handoff](IMPLEMENTATION_HANDOFF.md).

Before developing SCP-A, this round also resolved the earlier homogeneous
conversion reserve into **HGC6-A**. It fixes a finite fifth/sixth-cumulant
response program, the injected feedback correction, mean anchor and native
transport. Projected extra cost is 6–12B FLOPs. It is cheaper to build, but
its altered fourth-core trajectory and truncation make accuracy uncertain.
[Alternative specification](HGC6_A_SPEC.md).

Neither algorithm requires another generic theory round merely to decide its
omitted-order convention. Both deliberately omit some mixed response terms.
In particular, SCP-A's checked single-fourth source is **not** a complete
first-order radial expansion; some omitted mixed terms are also first order
in the radial coefficient. The finite algorithm can be tested without a claim
that all such terms are negligible. [Derivations](SCRATCHPAD.md), especially
sections 24–27, state these limits.

## Selection and forecasts

These are subjective, uncalibrated planning ranges against ALG043-V000,
including implementation failure and failure to reach a supported submission.
They are distinct from the approximately 90% support used after a local screen.
Conditional gains are plausible judgment bands, not confidence intervals.

| Untested candidate | Chance of retained official win | Adjusted-score reduction if successful | Illustrative expected retained reduction |
|---|---:|---:|---:|
| **SCP-A — preferred T151** | **15–30%** | **15–45%** | **~6%** |
| HGC6-A — ambitious alternative | 15–30% | 10–40% | ~5% |
| CMF2 — T149 deferred | 25–45% | 2–15% | ~2.8% |
| FAR-CT — cheap fallback | 20–35% | 1–5% | ~0.7% |

Expected retained reduction uses an illustrative success probability times a
conditional mean gain, with zero retained gain on failure. It is not the
average score of every candidate tried. The scenarios are correlated and
should not be summed. The [full inventory](UNTESTED_INVENTORY.md) gives the
arithmetic, older untested specifications, open routes, and already tested
candidates that must not be mistaken for forgotten tests.

SCP-A is preferred for its larger possible gain and the information supplied
by testing a different propagated input law. HGC6-A and CMF2 can look better
under some gain-per-hour midpoint choices. Those uncertain arithmetic choices
do not settle the decision. The owner's requested balance warrants developing
and trying the credible larger change, while retaining the inexpensive work.
No fallback begins automatically if implementation proves difficult.

## Evidence and effort

Completed **60.10 active minutes of written mathematics** and **4.48 minutes
of candidate selection**, with intake, context recovery and records excluded.
No additional literature block was needed: the round reused the existing
literature and public-source analysis. [Exact timing](TIMING.json) records
elapsed time and estimate error separately: 77.97 minutes through records versus the 90-minute estimate. Time was not recorded per route;
do not invent a retrospective split between HGC6-A and SCP-A.

Three small generated algebra checks pass: homogeneous moment/source slices,
the injected CT term with oriented contractions, and radial-law cumulants plus
fourth-source/trace identities. The largest recorded error is 6.64e-15.
A separate high-precision scalar calculation supplies stable radial constants;
ordinary operation counts supply cost scenarios. These validate the stated
identities, not challenge accuracy, production implementation or resource use.

No challenge inputs or targets, fitting, estimator runs, packages, uploads or
subagents were used. Retain ALG043-V000 / submission 330597 at official
adjusted score **5.419051334510831e-9**. T151 is proposed only: one implementation
and lean decision on SCP-A, estimated 120–180 elapsed minutes, with explicit
engineering reassessment and no automatic second candidate.
