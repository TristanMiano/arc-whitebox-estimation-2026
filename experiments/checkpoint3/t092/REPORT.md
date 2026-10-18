# T092 — balanced gate-risk affine-suffix continuation

## Decision

Reject unchanged `H090-A` before M1 and continue to T093. The target-free
affine signed-margin/leakage PPS rule was `1.016713259460243` of its same-cut,
same-count uniform fixed-size ablation on the held-out fold, against the frozen
`<=0.99` requirement. It won only `5/12` networks against the required `>=7`.
The maximum ratio was `1.8876002954707183` and passed the `<2` tail gate.

This is a scientific negative for the adaptive score/allocation mechanism, not
merely an arbitrary strict-gate miss. The pooled direction itself is adverse
by `0.026713259460243` relative to the threshold, and breadth misses by two
networks. No algorithm ID, M1, F0--F3 outcome, P1, rank, package, or official
score was created.

## Retained positive evidence

The broader affine-suffix continuation family remains interesting. H090-A was
`0.63002658244162235` of equal-work direct in the conditional finite-population
proxy, with `10/12` direct wins; its uniform ablation was stronger still at
`0.61966987897462222`. This is support-only context, not M1, because T092's
predeclared scientific question was whether the new margin-risk PPS allocation
improved the uniform fixed-count continuation. Two candidate/direct networks
also had adverse tails and the maximum direct ratio was `2.3221480376616896`.

The pilot/held-out reversal is theoretically informative. The pilot mean and
median candidate/uniform ratios were `0.753048` and `0.677444`, with `9/12`
wins, but the independently seeded held-out fold reversed to `1.016713` and
`5/12`. The first-omitted-layer affine leakage bound is therefore not a stable
network-level proxy for the nonlinear suffix residuals selected by this route.
It likely over-specializes cut/count selection and sometimes assigns unequal
weights where uniform residual coverage is safer. T093 should preserve the
uniform-continuation clue, but must not retune or rerun this exact score.

## Frozen construction and evidence

The estimator used positive floored inclusion probabilities from deterministic
capped water filling and one cyclic systematic-PPS selection of exactly `m`
pairs. The Horvitz--Thompson residual correction is conditionally unbiased.
All construction checks passed: minimum probability `0.0511012`, maximum `1`,
probability-sum error `5.68e-14`, conditional recovery error `9.33e-15`, exact
count, exact interval-length marginals, uniform-limit reduction, T025 affine
equivalence (`4.88e-15`), unique domains, finiteness, and byte-identical replay.

GCC 13 reproduced the MSVC decision, `5/12` wins, and primary ratios. The
pooled candidate/uniform absolute difference was `1.55e-14`; the largest CSV
numeric difference was `7.72e-10` on large unnormalized `Q` values.

## Gate table

| Gate | Requirement | Observation | Status |
|---|---:|---:|---|
| construction, identity, replay | all pass | all pass | PASS |
| pooled candidate/uniform | `<=0.99` | `1.016713` | FAIL-SCIENTIFIC |
| network wins | `>=7/12` | `5/12` | FAIL-SCIENTIFIC |
| maximum candidate/uniform | `<2` | `1.887600` | PASS |
| equal-work direct | context required | candidate `0.630027`; uniform `0.619670` | favorable support / report-only |
| M1 | all preceding M1 gates | two scientific failures | NOT-AWARDED |
| registration / F0--F3 / P1 | sequential after M1 | not run | NOT-RUN |

## Human promotion disposition

- Subject/evidence: H090-A held-out width-64 mechanism test; no registered ALG.
- Current/highest tier: no new empirical tier; support-only evidence remains
  for uniform affine continuation. M1 was considered and rejected.
- Strongest positive evidence: candidate/direct `0.630027`, `10/12`; the
  uniform control was stronger at `0.619670`.
- Primary blocker: `SCIENTIFIC_NEGATIVE_ADAPTIVE_SCORE_DIRECTION_AND_BREADTH`.
- Strict gate sole blocker: **No.** The claimed adaptive mechanism was worse
  than its exact ablation in the pooled held-out direction.
- Smallest credible unlock: T093 should consider a prospectively bound uniform
  continuation candidate or a mechanism-distinct alternative; neither the
  owner nor agent should relax these completed gates or retune H090-A.
- Submission succession: unknown/not applicable. No complete submission-facing
  route was produced, so `ALG014-V000` remains the submission candidate.

The frozen `.61` pre-M1-rejection probability makes this result expected at
`0.713119` bits. `H090-A` remains `OURS+PUBLIC`, N1/dimension 2 as an academic
design classification, but the exact implementation is empirically terminal.

## Operational record

Four pre-publication attempts are preserved. Attempt 001 exposed a non-finite
equal-work-direct diagnostic for cost-dominated pilot routes. Later retries
were found to be rerunning that stale executable because the Windows controller
accepted an existing stable file without proving recreation. The controller
now removes the exact task executable before compilation; dominated diagnostic
ratios saturate adversely instead of becoming non-finite. No JSON/CSV outcome
was published by the failed attempts, the estimator and gates did not change,
and the accepted Windows run replayed byte-identically. No owner action was
needed.

A final audit then found that the first-order interval check was tautological
and the domain-cardinality check covered only one fold. Post-outcome validation
amendment 001 replaced them with an explicit wrapped-interval calculation and
joint pilot/held-out domain enumeration. The strengthened run covered
`1,474,560` unique domains, had maximum interval-length error `1.11e-16`, and
reproduced the scientific metrics CSV byte-for-byte. This changed validation
strength only, not the opened result.

## Verification

```bash
bash experiments/checkpoint3/t092/verify_evidence.sh
```

## Task timing

- Start: `2026-08-23T15:07:13-07:00`
- Pre-task estimate: `50 minutes`
- End/check-off: `2026-08-23T15:31:48-07:00`
- Actual wall-clock difference: `00:24:35` (`1475` seconds)
