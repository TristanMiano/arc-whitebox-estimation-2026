# T096 — fixed frame/covariance score-floor shrinkage

## Decision

`ALG015-V000` passes the exact Phase-2 cost premise and the prospectively
repaired current-shape M1 screen. It is the new local submission candidate.
It is not project P1: the separately sealed width-256/depth-32 historical
adapter fails all three FFSP003 M1 gates, so the stop-on-scientific-rejection
rule ends T096 before F0–F3.

These statements are intentionally separate. The historical failure does not
erase a directly observed Phase-2 score win, and the Phase-2 win does not
silently award an internal P1 tier.

## Exact implementation and cost

The estimator uses one 2048x1024 mean-chi-radius Haar-Stiefel block,
antithetic propagation, bundled float32 full-covariance propagation, fixed
weights `0.25/0.75`, and the exact first layer. Two outcome-blind probes were
byte-identical and each charged `196,459,652,235` FLOPs. The frozen score-floor
ceiling was `219,902,325,555.2`, leaving `23,442,673,320.2` FLOPs of headroom.

The first cost attempt exposed an immutable-array indexed-assignment defect.
No target or candidate accuracy had been opened. The implementation was
functionally repaired, rebound in the preoutcome seal, and then passed twice.
This is an implementation repair, not a favorable-result mutation.

## Current Phase-2 result

The first 12-row diagnostic run used the frozen thresholds but preceded the
adapter's boundary-fixture execution. It is explicitly ineligible for tier
evidence. The unchanged threshold semantics then passed positive, boundary,
rejection, and mutation fixtures. A fresh, untouched public Phase-2 cohort
(mini rows 16–27) supplied the prospective result:

| Arm | FLOPs | Multiplier | Pooled adjusted score |
|---|---:|---:|---:|
| `ALG015-V000` | 196,459,652,235 | 0.1 | `2.764913509e-7` |
| pure covariance endpoint | 51,711,338,975 | 0.1 | `3.726168562e-7` |
| pure one-frame endpoint | 144,746,149,548 | 0.1 | `1.019693394e-6` |
| official-candidate code `ALG014-V003` | 578,986,643,120 | 0.2632926422 | `6.643375274e-7` |

Against the frozen best endpoint, the candidate ratio is `0.742025881`, with
`12/12` wins and maximum paired ratio `0.884448586`. The required limits were
`<=0.99`, at least `7/12`, and `<4`; all pass. Current-shape M1 is awarded.

Against `ALG014-V003` on the identical networks, targets, scorer, and charged
compute base, the ratio is `0.416191077`, also with `12/12` wins and maximum
`0.509956873`. This is a `58.38%` adjusted-score reduction. Under the owner's
mandatory succession rule, **ALG015-V000 is our new submission candidate even
though it does not pass historical P1.** `ALG014-V003` remains the best
officially graded entry until this new candidate is separately packaged,
qualified, and—only with authorization—uploaded.

## Historical FFSP003 disposition

The explicit historical adapter dimension-scales the same construction to one
512x256 frame and the bundled closure, keeps `0.25/0.75`, and reports a four-
frame carrier plus `ALG003-V008` context. It was sealed before candidate
outcomes on public Phase-1 mini rows 32–43.

| Comparison | Observation | Gate | Status |
|---|---:|---:|---|
| candidate / best fixed endpoint (one frame) | `1.619842722` | `<=0.99` | **FAIL-SCIENTIFIC** |
| wins | `2/12` | `>=7/12` | **FAIL-SCIENTIFIC** |
| maximum paired ratio | `4.927357949` | `<4` | **FAIL-SCIENTIFIC** |
| candidate / four-frame carrier | `7.060808732` | context | adverse |
| candidate / `ALG003-V008` | `14.852570569` | context | adverse |

This is not strict-gate-limited. The fixed three-quarter closure weight is
scientifically rejected as a shape-general historical mechanism. The result
matches the pre-existing theoretical warning that depth-32 closure bias is
adverse. No FC005 F0–F3 evidence was opened, and FC005 remains empty because
the explicit pre-F0 historical adjudication rejected the candidate.

## Prior surprise and claim boundary

The terminal category is “M1 then rejected before P1,” frozen at probability
`.32` (`1.643856` bits). It is mildly informative but not a major surprise:
the current-shape win was separately assigned probability `.62` (`0.689660`
bits), and the theory notebook specifically expected poor historical shape
transfer. The exact size of the Phase-2 win is stronger than the projection,
but its direction is not surprising.

Highest supported status is current-shape M1 plus submission succession;
historical P1 is scientifically rejected. N1 novelty remains a project-specific
score-floor composition, not a new general shrinkage theorem. The strongest
next action is T097's already frozen adaptive cross-fitted shrinker, which was
designed to turn closure influence down when shape-specific bias is large.

Substantive results should still be reproduced later on an independently
stable machine or VM. No owner action is required for T096 completion.
