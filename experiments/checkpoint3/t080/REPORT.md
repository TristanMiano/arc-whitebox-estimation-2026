# T080 — exact multilevel kink-telescope adjudication

## Decision

Reject the frozen `H078-B` independent-level multilevel telescope before M1.
The exact telescope is correct, but even its optimistic continuous allocation
oracle has `5.1721158472697235` times the variance-cost product of direct
antithetic sampling, against the prospectively frozen strict requirement
`<0.75`. Every one of the 12 networks loses. No `ALG` identity, M1, allocation
implementation, held-out fold, F0-F3 outcome, P1, official score, or rank
change is created. With both T078-selected mechanisms now terminal and P1
still empty, T081 is the required rejection-informed novelty recurrence.

This is a strong `SCIENTIFIC_NEGATIVE_INDEPENDENT_LEVEL_EFFICIENCY`, not a
strict-gate-limited near miss. The failure occurs before the costs of suffix
construction, rounding, reserve, or stream administration are charged.
Relaxing the gate from `0.75` even to parity would not pass any network.

## Frozen exact target

T025's fixed affine hybrids give the pointwise identity

```text
f = F^(0) + sum_k Delta_k,
Delta_k = [relu(z_k) - a_k*z_k - b_k] B_k.
```

T080 froze T025's class-aware coefficients: zero for dead neurons, identity
for on neurons, and the diagonal-Gaussian L2 affine projection for kink
neurons. It estimated each antithetic `Delta_k` on an independent stream. If
`V_k` is its trace variance and `C_k` its paired prefix/suffix cost, the best
continuous independent allocation at fixed work has variance-cost product

```text
Q_opt = (sum_k sqrt(V_k C_k))^2.
```

The direct comparator has `Q_direct=V_direct*C_direct`. The fixture used 12
deterministic He-Gaussian width-64/depth-32 networks and 512 fixed-radius
spherical antithetic pairs per network for the oracle fold. Common diagnostic
points estimated all marginal `V_k` efficiently; they were not used as a
correlated estimator and therefore could not hide the covariance loss caused
by independent level streams.

All six construction checks passed:

| Check | Observation | Status |
|---|---:|---|
| T025 class-aware coefficient rules | 4,101 dead / 16,565 kink / 3,910 on coefficients | PASS |
| Pointwise telescope reconstruction | maximum error `7.54952e-15` | PASS |
| Antithetic telescope reconstruction | maximum error `8.88178e-15` | PASS |
| Analytic affine-pair mean | maximum error `9.32587e-15` | PASS |
| Dense suffix recursion | maximum error `5.32907e-15` | PASS |
| Independent `(network,fold,level)` domains | 768/768 unique | PASS |

These results retain the exact decomposition as support. They do not make
independent estimation of its levels efficient.

## Decisive continuous-oracle result

| Quantity | Frozen requirement | Observation | Margin / interpretation |
|---|---:|---:|---|
| Pooled `Q_opt/Q_direct` | `<0.75` | `5.1721158472697235` | fails by `4.4221158472697235`; `6.89615x` the gate |
| Network wins versus direct parity | diagnostic | `0/12` | no favorable network |
| Minimum network oracle ratio | diagnostic | `3.1372293683105741` | even the best network is `3.14x` direct |
| Median network oracle ratio | diagnostic | `4.4398709953034476` | broad rather than one-tail failure |
| Maximum network oracle ratio | diagnostic | `10.391147505692423` | severe adverse tail |
| Summed optimal level variance-cost | diagnostic | `25,694,269.760926928` | numerator |
| Summed direct variance-cost | diagnostic | `4,967,844.982530799` | denominator |

The empirical pattern matches T078's predicted covariance-loss failure mode.
The exact level sum reconstructs direct output on common points, so direct
sampling retains cross-level covariance. Independent streams remove that
cancellation and must pay separate prefix/suffix work for every level. Even
perfect continuous allocation cannot compensate here.

## Gate-by-gate disposition

| Gate | Frozen requirement | Result |
|---|---|---|
| Six exact construction checks | `6/6` | PASS |
| Deterministic replay | byte-identical JSON/CSV | PASS |
| Native dependency boundary | no Python | PASS; only `KERNEL32.dll` |
| Continuous oracle | pooled `Q_opt/Q_direct <0.75` | FAIL-SCIENTIFIC, `5.1721158472697235` |
| Integer allocation and reserve | run only after oracle pass | NOT-RUN |
| Candidate/uniform held-out ratio | `<0.90` after oracle pass | NOT-RUN |
| Candidate/direct held-out ratio | `<0.95` after oracle pass | NOT-RUN |
| Held-out wins / maximum | `>=9/12`, maximum `<1.25` | NOT-RUN |
| Complete candidate registration and F0-F3 | required after M1 | NOT-APPLICABLE |
| Incumbent competitiveness | P2-only context | NOT-APPLICABLE |

Stopping saved the held-out allocation and funnel compute exactly as required.
The unrun gates cannot conceal a favorable result because they add real costs
and integer restrictions to an oracle already more than five times worse than
direct sampling.

## Surprise assessment

T078 froze probability `0.55` for rejection before M1. The observed result is
that category and carries `-log2(0.55) = 0.862496476250065` bits. It is
**expected**, not surprising. Its severity across all 12 networks is useful
mechanistic information, but it does not change the prospectively frozen
category after seeing the result.

## Human promotion disposition

- Subject/evidence class: E051/T080 synthetic native exact variance-cost
  oracle (`N`), not a complete estimator comparison.
- Current/highest/next tier: no new tier / exact T025 telescope support only /
  M1 was considered and decisively rejected.
- Strongest positive evidence: the pointwise and antithetic identities hold to
  `8.88e-15`; all six construction checks and deterministic replay passed.
- Failed gate: pooled oracle ratio `5.1721158472697235` versus strict `<0.75`,
  an adverse absolute margin `4.4221158472697235`; all 12 network ratios exceed
  one and the minimum is `3.1372293683105741`.
- Primary blocker: `SCIENTIFIC_NEGATIVE_INDEPENDENT_LEVEL_EFFICIENCY`.
- Strict gate sole blocker: **No.** The observation is directionally and
  materially worse than direct sampling even at parity, and the oracle omits
  costs that could only worsen the candidate.
- Why not promoted: independently sampling exact telescope increments destroys
  useful cross-level cancellation and repeats prefix/suffix work; optimal
  allocation cannot recover direct-sampling efficiency on this fixture.
- Immediate high-impact unlock: the agent performs T081's new theory- and
  rejection-informed novelty slate. No owner action is required. A future
  telescope successor needs a materially new target-preserving way to retain
  covariance or share work, a new fingerprint, and a cheap precomputed bound;
  merely retuning allocation or the `0.75` gate cannot revisit H078-B.

## Windows-native attempts

Attempt 1 completed verification and replay with empty stderr and byte-identical
outputs, then the controller compared JSON's decimal
`0.55000000000000004` to decimal `0.55` exactly and stopped. The payload is
preserved under `attempt1_controller_decimal_failure/`. The sealed controller-
only repair changed this assertion to an absolute tolerance of `1e-15`; the
predeclaration and scientific C++ source did not change.

Attempt 2 completed the same verification payload, then the executable on the
WSL UNC build path disappeared before replay launch. That attempt is preserved
under `attempt2_executable_disappeared/`. Attempt 3 moved only the build tree to
Windows local temporary storage and passed. All three available verification
JSON files have identical SHA-256
`78726b4e169dd01f055ab1e5c087d62c0ad771c30eb4ef2e4c97b5ce3a826276`.
The accepted MSVC 19.43 / Windows SDK 10.0.22621.0 run started at
`2026-08-22T11:31:00.9723867-07:00` and ended at
`2026-08-22T11:31:08.2711850-07:00`. Later independent reproduction on a
stable machine or VM remains appropriate.

## Verification

```bash
bash experiments/checkpoint3/t080/verify_evidence.sh
```

## Task timing

- Start: `2026-08-22T11:19:53,824346523-07:00`
- Pre-task estimate: `60 minutes`
- End/check-off: `2026-08-22T11:39:30,350242127-07:00`
- Actual wall-clock difference: `00:19:36.526689666`
  (`1176526689666` ns)
