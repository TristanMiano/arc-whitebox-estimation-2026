# T163 / E159 — a learned residual nominee and a clearer fourth-state bottleneck

Completed **240.18 active research minutes**, including **119.71 minutes of
written derivation**. One frozen candidate, **P67**, merits a bounded submission
attempt: its estimated adjusted score improves **5.12% on the 12 declared
development networks**, with **12/12 wins**. These are previously exposed public
development inputs, not hidden validation. No submission was made; official
incumbent **ALG050-V000 / 331607**, adjusted **4.544342423060378e-9**, is unchanged.

## The nominee

P67 learns a small correction from the incumbent's intermediate physical
states. Its 124 shared coefficients combine 52 marginal features and 72 pair
features, then transport their contributions through the network's linearized
mean response. Linearity collapses the training feature matrix into **one
propagated vector at inference**. The physical recurrence and first 15 outputs
are unchanged; the final mean receives the correction.

The coefficients were fitted on 32 fixed training networks using four
whole-network folds and four declared ridge choices. Cross-validation improves
raw MSE **3.89%**, winning on 30/32 networks. The frozen model subsequently gives
the 12-network development result above. Selecting architectures and ridge
strengths using development work can produce optimism; descriptive bootstrap
support of 1.0 is not a 100% probability of an official win. My subjective
forecast is **90–95% probability of official improvement**, with **2–6% adjusted
gain conditional on success**.

Two actual compact calls verify a fixed **311,953,468 extra FLOPs**, about
**0.07%** of the incumbent's prediction cost, residual times of **0.306/0.324 s**,
and peak RSS **6.62 GB**. The 12-network adjusted comparison uses saved feature
predictions and that verified overhead, with matching call histories; it is
not twelve compact implementation calls. Ordinary archive qualification and
deterministic replay remain for the submission task.

An initial absolute numerical-equivalence tolerance of 2e-7 failed on one call
at 2.325e-7. The failure is preserved. Algebra inspection and a roundoff-scaled
comparison support equivalence of the two float32 summation orders; the induced
MSE change is bounded by 0.038%, well below the observed gain. Neither source nor
coefficients were changed to obtain this conclusion. This is distinct from
byte-identical replay of a final archive.

P41, the marginal-only model, remains a frozen reserve: **2.91% development
adjusted gain**, 12/12 wins. P67 beats it on 11/12 networks. Larger coupled,
conditional, terminal nonlinear and nonlinear trajectory feature families did
not improve cross-validation enough to replace P67. A retrospective optimal
scalar adds only 0.047 percentage points of raw gain and was **not applied**.

**Novelty:** P67 is our supervised learned adaptation of ALG050 and the published
cumulant framework. It is neither a pure copied submission nor a proved new
moment closure. The architecture comes from physical features and response
derivations; fitting determines its coefficients. No academic priority claim
is needed. [Frozen development evidence](P46_DEVELOPMENT.json),
[candidate source](sources/P67_pair_residual/estimator.py),
[selection and probabilities](CANDIDATE_SELECTION.md).

## Larger gains: capacity exists, affordable representation remains unresolved

Research continued on the larger route after the cheap candidate emerged.
The following generated-network tests compare with the public augmented
third-order recurrence, **not ALG050**. Each width uses one fixed network;
different widths also have different seeds. These are capacity experiments,
not challenge-wide performance estimates.

| Generated case | Raw MSE | Interpretation |
|---|---:|---|
| Width 256, factored third-order control | 9.15537e-7 | Main capacity comparator |
| Width 256, dense third-order control | 8.54480e-7 | Controls additional lower-order map terms |
| Width 256, full fourth state, outer rank 32 | 5.28958e-7 | Strong capacity, expensive state |
| Width 256, shared fourth basis 96 | 6.70101e-7 | Retains some gain |
| Width 256, combined compact third/fourth recipe P79 | 7.92666e-7 | 13.4% below factored control; 7.2% below dense control |
| Width 384, third-order control | 4.03880e-7 | Stronger new reference estimates |
| Width 384, full fourth state, outer rank 64 | 2.62775e-7 | **35.0% lower MSE** |
| Width 384, shared fourth basis 128 | 5.63810e-7 | **39.6% higher MSE** |

The wider compression failure is consequential. Better reference estimates
separate it from reference noise. It lowers my forecast for an affordable
larger successor to **15–30% official-win probability within 8–16 additional
research/implementation hours**, with **10–30% conditional adjusted gain**.

The round identified useful structure: mixed covariance/third-cumulant loops
are essential; preserving young sources helps; a basis chosen for the actual
third tensor outperforms a covariance-only basis; direct cubic-response queries
can replace an expensive response Gram; and repairing lost fourth repeated
slices improves the width-256 shared control. The final P79 combines a compact
third state and fourth response with one old-state Gram refinement and retains
a positive capacity result. Exact factor/query identities are recorded and
numerically checked.

The missing step is a **complete economical constructor**, including nonlinear
newborn sources, mixed loops, basis construction and projection. Cheap transport
alone does not establish an affordable algorithm. Wider transfer also remains
unresolved. More rank tuning is not the recommended next research action;
source-aware basis reuse or protected newborn/repeated components are concrete
alternatives. [Continuation](CONTINUATION.md), [route saturation](ROUTE_UPDATE.md),
[43-section scratchpad](SCRATCHPAD.md).

Adjacent literature broadened the review to tensor actions, basis augmentation,
Stein controls and conditional integration. Coordinatewise controls, 2D
geometric integration and exponential-dimensional antiderivative constructions
are not ready substitutes for this problem. This breadth work supplied
constraints and possible mechanisms, not a second end-to-end nominee.
[Primary sources and reading scope](LITERATURE.md).

## Work and handoff

| Exclusive active category | Minutes |
|---|---:|
| Derivation | 119.71 |
| Empirical design, implementation and interpretation | 83.64 |
| Literature | 23.22 |
| Selection | 13.61 |
| **Research total** | **240.18** |

There were **148 completed full-shape calls** across 44 unique networks:
120 feature-collection calls and 28 prototype/candidate calls, totaling
**68.820 T metered FLOPs**. Their 102.96 prediction minutes, 41 generated
recurrences' 134.98 minutes, and new references' 10.77 minutes overlap research
and must not be added to active time. Generated recurrences have 40 distinct
source hashes: P53 was an identical-source replay, not a new algorithm.
Failed partial work and untimed analysis are not fully included in machine
subtotals. Operational failures and superseded sources remain preserved.
No agents, interruption gaps, passive waiting or final-blind access occurred.
Exact per-route hours were not separately clocked.
[Cost/source inventory](COST_AND_SOURCE_INVENTORY.json), [timing](TIMING.json).

**Recommended T164:** register and qualify the frozen P67 archive, reuse this
evidence, then attempt submission under the standing 60-minute wait and one
unchanged retry for a generic evaluator problem. No extra cohort or refitting
is presently justified. T164 is proposed, not started or authorized by this
research task. All T163 prediction and reference jobs have finished.
