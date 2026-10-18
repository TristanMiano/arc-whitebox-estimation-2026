# T165 — four-hour empirical theory recurrence

**Complete: no submission nominee.** Retain ALG051-V000, official332018,
adjusted **4.36851423131e-9**. Research lasted **241.72 active minutes**:
146.05 written derivation,47.26 empirical work,30.86 literature and17.54
selection. Administration and overlapping compute are not added to those hours.
[Timing](TIMING.json), [candidate forecasts](CANDIDATE_SELECTION.md),
[next proposed research](CONTINUATION.md).

The main finding is a persistent **accuracy–cost mismatch**. Rich fourth-order
states contain useful information, and their errors complement the ordinary
third-order approximation. Most affordable-looking compressions lose that
information; the representations retaining it still have expensive constructors
or responses. The late compact-third efficiency route also fails its present
cost test. No official comparison, package or upload was performed.

## What we learned

Equal endpoint mixtures of the ordinary third-order and richer fourth-order
estimates reduce raw error substantially on saved generated examples:

| Width | Third-order MSE | Full fourth-order MSE | Equal-mixture MSE | Mixture reduction |
|---:|---:|---:|---:|---:|
|256|9.155e-7|5.290e-7|4.159e-7|54.6%|
|384|4.039e-7|2.628e-7|1.309e-7|67.6%|
|512|1.437e-7|1.372e-7|6.995e-8|51.3%|

These are **one generated network per width**, with different retained ranks,
not three independent evaluations of one frozen submission algorithm. The512
reference uses eight independent2^20-sample banks. Its fourth-only advantage
is smaller than the paired reference-only standard error, so that endpoint's
win is not established. Its mixture signal survives the stronger reference.
The512 reference implementation uses float32 storage and a recorded tiny
negative-variance clamp; it is neither an official resource pass nor ALG051.
[Error geometry](ERROR_GEOMETRY.json) shows mostly decorrelated errors, rather
than one common opposite bias that a scalar correction obviously fixes.

A source-aware256 state preserving the entire newest fourth birth reaches
**3.951e-7**,56.8% below the third control. A joint compact-third/exact-young-
fourth version reaches4.657e-7. But removing mixed births, keeping only a quarter
of source groups, or damping the coupled response loses most of that gain.
The cheaper trace-only part of the22 response is worse than omitting that
response entirely: its terms need balanced treatment.

Several different repairs were tested rather than only increasing rank:

| Probe | Result and implication |
|---|---|
|P31, previously deferred augmented fourth at128|MSE4.024e-5;3.85x matched SIMPLE4. More expansion terms do not ensure better predictions.|
|P44/P45, selected squared-third terms|Worse than the jointP33 control by34%/40%. These finite additions are closed.|
|P46, fixed coupled-half recurrence|9.070e-7, almost the ordinary third control; endpoint mixture capacity does not transfer to this one-state interpolation.|
|P47, independent baseline plus compressed cubic difference|Rich5.196e-7; equal mixture4.893e-7,46.6% below baseline. Useful capacity, weaker than uncompressedP24, with the constructor still unresolved.|
|P48, exact anchors and compressed companions|6.896e-7,74.5% worse than exact-youngP24. Preserving anchors alone is insufficient in this spelling.|
|P34c, full fourth only in the last four steps|7.740e-7,15.5% below baseline; current constructor costs consume this smaller gain.|
|P49/P53, compact third alone|Raw error+47.2%/+44.1% for exact/sampled basis actions. Would require large total savings, which the measured components do not provide.|

Full-width metering prevented optimistic cost claims. The selectedq192 fourth
constructor costs **53.47B FLOPs per step** before parent/basis/transport work;
all-source projected hypertree birth costs **61.35B**, excluding finite repair
and the rest of the map. The exact cubic compressor costs53.00B; its sampled
alternative costs31.69B. Fifteen sampled compressions alone cost475.3B, already
above the roughly450B entire parent. These are measured components, not universal
lower bounds: a different joint representation could share or remove work.

## Broader routes and useful mathematics

The breadth tests were informative but negative. A shallow function control
on actual public row750 removes little variance; even its optimistic arithmetic
estimate is about171times the incumbent's adjusted score. At generated128,
the top16 gradient coordinates leave76.7% variance to any function surrogate
using only those coordinates. Exact conditional integration over them would
remove81.4%, but no cheap16-dimensional integral is available. These statements
concern different conditional operations and do not conflict.

Two new feature collectors ran on16 existing F networks. Neighbor-curvature,
interaction-cycle and trace-carrier additions all lose to the matched original
124-feature model in whole-network cross-validation. No coefficients in the
incumbent changed. Reusing the existing32F learning curve suggests about0.9%
possible gain from64F, with substantial model uncertainty; no64F corpus was
created. This remains a small reserve, not a ready algorithm.

The [scratchpad](SCRATCHPAD.md) derives complete source projections,
asymmetric fourth responses, representation-gauge limitations, cubic Gram
and query identities, and a regrouping of the actual factorable third newborn.
Independent small tensor checks pass at numerical precision. The regrouping
reduces several source families to one triple bank plus a matrix–vector term;
its complete native implementation remains unbuilt. Equal quartic tensors can
compress differently under different pair-space representations—a concrete
bug/assumption diagnosis, not merely another negative score.

The [23-source literature collection](LITERATURE.md) covers tensor interpolation,
basis updates, unbiased compression, conditional integration, neural controls,
EP corrections and pairwise dynamic mean fields. Reading scopes and transfer
limits are recorded. A new public-ancestor clarification changed documentation,
not estimator code; no superior executable successor was found in this limited
search. No academic-novelty claim is needed for the derived adaptations.

## Evidence, limits and disposition

The inventory records **32 full-size feature calls on16 unique networks**,
14.504T charged FLOPs, **38 completed generated trajectory records**,20 saved
component/analysis results and two new reference-generation results. These are
not counts of independent algorithms; P35 deliberately replaysP24 while
measuring noise, and other records include controls/numerical realizations.
Root-level algebra checks and saved-data analyses are additional.
[Reproducible inventory](COST_AND_SOURCE_INVENTORY.json), [probe log](PROBES.md).

Preserved failures include a width512 memory-guard stop and two late-switch
API/memory failures. Float32 storage and bounded chunk expansion enabled the
corresponding later research tests; earlier failures were not erased. Dense
research memory/runtime may exceed official caps. No production pass is inferred.
All queued jobs finished. No agents, private-data commits, blind access or upload.
The incumbent source hash remains
db714c48d45653fb1c9bdd9ccd880f6f25c0ab3ad7584f8f13b852571cb44067.

The current fourth-compression neighborhood is showing diminishing returns.
Propose a broader T166 recurrence with an early, finite cost check for the new
source algebra, substantial room for a different state/information mechanism,
and the small training reserve kept in view. The task has not started.
