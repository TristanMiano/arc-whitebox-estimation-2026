# T079 — exact angular-orbit Rao–Blackwell adjudication

## Decision

Reject the frozen `H078-A` common-partition realization before M1 for decisive
tractability failure. The exact conditional-expectation theorem and small
piecewise integrator are valid, but the proposed full-depth propagation cannot
satisfy T078's completion and p95-work gates simultaneously. No `ALG` identity,
M1, protected F0–F3 outcome, P1, official score, or rank change is created.
T080's materially distinct exact multilevel kink telescope is next.

This is `SCIENTIFIC_NEGATIVE_TRACTABILITY` for the exact common-partition
implementation, not evidence that conditional expectation increases variance.
The variance, network-win, maximum-ratio, and fixed-plane-ablation gates are
`NOT-RUN` because the prospectively frozen sequential proof had already made
the M1 conjunction impossible.

## Frozen target and theorem checks

For a network-selected two-plane `P`, a uniform spherical input can be written

`U = Z + rho(cos(theta)e1 + sin(theta)e2)`.

Conditional on `(Z,rho)`, the angle is uniform, so exact circular integration
is `E[f(U)|Z,rho]` and preserves `E[f(U)]`. On any fixed ReLU gate cell, every
activation on the circle has the form `a+b*cos(theta)+c*sin(theta)`. The frozen
integrator propagated a common angular partition, inserted all ReLU roots, and
integrated the final coefficients analytically. The selected plane came from a
deterministic Jacobi eigendecomposition of the input-side expected-gate
`J J^T`, with frozen ordering and sign canonicalization.

All six construction checks passed:

| Check | Observation | Status |
|---|---:|---|
| Small width-3/depth-2 exact integral vs 262,144-angle midpoint quadrature | max absolute difference `3.1209479445237776e-12` | PASS |
| Selected-plane unit norms and orthogonality | max error `2.3314683517128287e-15` | PASS |
| Orbit decomposition/reconstruction | max error `4.4408920985006262e-16` | PASS |
| Eigenvalue ordering/canonical selector | all examined networks | PASS |
| Orbit-invariant cap/work decision | depends only on network, `Z`, and `rho` | PASS by construction |
| Exact analytic coefficient integration | included in dense-quadrature seal | PASS |

These checks support the target identity and the small exact integrator. They
do not award M1 without a tractable variance-reduction result.

## Decisive tractability result

The planned fixture contained 3,072 ordered anchors (`12` networks times
`256`). It required at least 2,304 completed orbits and p95 completed-orbit work
no greater than eight dense forwards. The frozen implementation charges three
coefficient channels across each common interval. Its accumulated charge is a
lower bound because root finding, sorting, and integration are not included.

At the minimum completion count, at most 768 anchors can fail completion and
at most 115 completed anchors can lie above the p95 work boundary. Therefore
no more than `768 + 115 = 883` of all anchors can be over the work limit if the
two gates are both to pass. The experiment stopped prospectively at the 884th
certified over-limit anchor.

| Quantity | Frozen boundary | Observation | Margin / interpretation |
|---|---:|---:|---|
| Over-limit anchors compatible with both gates | `<=883` | `884` | exceeds by 1; conjunction mathematically impossible |
| Anchors examined before decisive stop | at most 3,072 | `884` | all 884 were certified over eight forwards |
| Work lower bound among examined anchors | `<=8` for p95 completed | median `11.53125`, empirical p95 `16.6875`, maximum `22.40625` | even the uncharged lower bound is materially above the limit |
| First crossing layer | diagnostic | 452 at layer 3; 311 at layer 4; 121 later | cost growth appears early |

The counting result does not extrapolate from the first 884 anchors. It is a
deterministic impossibility statement over the complete 3,072-anchor set: even
if every unseen anchor were cheap and completed, any set completing at least
75% would contain more than 5% already-certified high-cost anchors. Continuing
the remaining 2,188 anchors could not alter the decision.

The scope is important. This rejects the exact common-partition propagation
and work plan fingerprint frozen for H078-A. A future integrator with a
materially different event representation and a static subquadratic work proof
could receive a new fingerprint. Merely raising the eight-forward gate or
running the unchanged variance study would not establish efficiency.

## Gate-by-gate disposition

| Gate | Frozen requirement | Result |
|---|---|---|
| Six analytic/construction checks | `6/6` | PASS, `6/6` |
| Deterministic replay | byte-identical JSON/CSV | PASS |
| Native dependency boundary | no Python | PASS; executable depends only on `KERNEL32.dll` |
| Completion plus p95 work | completion `>=75%` and completed p95 `<=8` dense-forward equivalents | FAIL-SCIENTIFIC as a conjunction: 884 over-limit anchors versus maximum compatible 883 |
| Work-normalized ratio to equal-work antithetic | `<0.85` | NOT-RUN after decisive stop |
| Network wins | `>=9/12` | NOT-RUN |
| Maximum network ratio | `<1.25` | NOT-RUN |
| Selected/fixed-plane ablation | `<0.95` | NOT-RUN |
| Complete candidate registration and F0–F3 | required after M1 | NOT-APPLICABLE |
| Incumbent competitiveness | P2-only context | NOT-APPLICABLE |

## Surprise assessment

T078 froze probability `0.72` for rejection before M1. The observed outcome is
exactly that category, carrying `-log2(0.72) = 0.473931` bits. Under the frozen
rubric it is **expected**, not surprising. This agrees with the pre-result
prediction that exact conditional variance reduction would likely be defeated
by interval growth or equal-work cost.

## Human promotion disposition

- Subject/evidence class: E050/T079 synthetic native theorem/tractability kill
  (`N`), not a complete estimator comparison.
- Current/highest/next tier: no new tier / exact construction support only / M1
  was considered and rejected before variance evaluation.
- Positive evidence: the target identity is exact; all six construction checks
  passed; dense quadrature agreement was `3.12e-12`; replay was byte-identical;
  no target-bias, dependency, or infrastructure defect was observed.
- Failed gate: the conjunction of 75% completion and p95 work `<=8`. The
  largest compatible high-cost count was 883; the observed count reached 884,
  an adverse margin of one, with all 884 examined anchors over the work limit.
- Primary blocker: `SCIENTIFIC_NEGATIVE_TRACTABILITY` for the frozen common-
  partition realization, plus `EVIDENCE_INCOMPLETE` for variance because the
  later gates correctly remained unopened.
- Strict gate sole blocker: **No.** Raising the work threshold would only open
  an unrun variance/ablation study; it would not award M1 or reveal already-
  observed favorable effect evidence.
- Why not promoted: the exact estimator operation consumes too much work before
  its variance benefit can be tested under the selected route.
- Immediate high-impact unlock: agent executes T080's materially distinct exact
  multilevel telescope. No owner action is needed. Reopening angular orbits
  would require a new subquadratic event representation and static work proof,
  not a threshold relaxation or unchanged retry.

## Windows-native evidence

The accepted MSVC 19.43 / Windows SDK 10.0.22621.0 run started at
`2026-08-22T11:09:05.9170124-07:00` and ended at
`2026-08-22T11:09:13.9578364-07:00`. Normal and replay outputs were
byte-identical, stderr was empty, retained source hashes matched the
pre-outcome seal, and the binary loaded no Python. The substantive conclusion
still merits later independent reproduction on a stable machine or VM.

## Verification

```bash
bash experiments/checkpoint3/t079/verify_evidence.sh
```

## Task timing

- Start: `2026-08-22T11:01:41,254424284-07:00`
- Pre-task estimate: `55 minutes`
- End/check-off: `2026-08-22T11:13:34,128710638-07:00`
- Actual wall-clock difference: `00:11:52.874286354`
  (`712874286354` ns)
