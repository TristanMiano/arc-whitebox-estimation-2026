# T088 — Lyapunov-subspace projected auxiliary-prefix control

## Decision

Reject unchanged `H087-A` before M1 and continue to conditional H087-B/T089.
P1 is not awarded; width 128, complete width-256 registration, FC004/F0--F3,
and official scoring were correctly not run.

This is a scientific near-null/effect-breadth rejection, not an operational
failure or a strict-gate-only near miss. On the frozen Windows-native width64
fixture, the fully charged candidate/direct ratio was
`0.9971233250349718` versus required `<0.88`: a favorable point direction of
only `0.2877%`, short of the required effect by `0.1171233250` absolute
(`13.3095%` of the threshold). It won only `1/12` networks versus `>=9/12`.
Maximum ratio `1.0042446462` safely passed `<1.25`.

The weight-selected basis did beat the fixed-six-coordinate ablation pooled,
but only by `2.5986%`: candidate/ablation was `0.9740143768` versus `<0.95`,
missing by `0.0240143768` (`2.5278%` of the threshold). That is weak retained
directional evidence, not an M1 mechanism signal. Ten of twelve pilot plans
selected the exact `M/N=0` direct boundary; only two selected a nonzero
auxiliary center. The claim that this six-dimensional deterministic subspace
captures enough stochastic final/hidden covariance is therefore rejected at
the first width.

## Frozen exact estimator

At each candidate cut, four forward/backward subspace iterations plus one
final paired pass use only the expected-gate suffix weights to form orthonormal
rank-six bases `P` at the hidden state and `Q` at the output. Layerwise QR
makes the common expected-gate scalar irrelevant to the subspace. No sampled
network output enters either basis.

For full antithetic output `Y`, same-path hidden state `H`, independent
same-law prefix state `H'`, and a pilot-fitted `6 x 6` response `B`, the frozen
estimator is

```text
Z = mean(Y) - Q B [mean(P^T H) - mean(P^T H')].
```

The two projected hidden means have the same expectation, so the correction
is exactly zero mean for every pilot-frozen basis and response. The nearest
ablation replaces `P,Q` by the first six coordinate axes with identical cut,
streams, rank, allocation, and charged work. The direct comparator receives
as many full antithetic pairs as fit in the candidate's used work.

The `261B` work model charged all eight cut-specific forward/backward basis
constructions, the 512-pair full pilot, selection and ablation projections,
rank-six covariance/solve work, main and prefix paths and projections, and
integer rounding. The separate `11B` reserve remained untouched.

## Gate results

| Gate | Frozen requirement | Observation | Status |
|---|---:|---:|---|
| Basis/full-prefix/solve correctness | all numerical limits pass | orthonormality `1.11e-15`; projected replay `0`; solve residual `1.11e-16` | PASS |
| Width64 candidate/direct | `<0.88` | `0.9971233250` | FAIL-SCIENTIFIC |
| Width64 network wins | `>=9/12` | `1/12` | FAIL-SCIENTIFIC |
| Width64 maximum network ratio | `<1.25` | `1.0042446462` | PASS |
| Width64 selected/fixed-coordinate | `<0.95` | `0.9740143768` | FAIL-STRICT-EFFECT |
| Width128 equivalent gates | only after every width64 gate passes | `NOT-RUN` | NOT-RUN |
| Width128 minus width64 | `<0.10` after width128 opens | `NOT-RUN` | NOT-RUN |
| M1 / registration / F0--F3 / P1 | only after two-width pass | no / no / `NOT-RUN` / no | NOT-RUN |

The direct and win gates independently reject the claimed effect; relaxing the
ablation threshold would not promote a candidate that is essentially direct
and wins one network. Conversely, the safe maximum and modest pooled ablation
advantage should remain visible in future hypothesis generation.

## Reproduction and defect audit

The accepted MSVC 19.43 Windows-native run used only `KERNEL32.dll`, passed
source stability, and produced byte-identical JSON and CSV on replay. An
independent GCC/Linux build reproduced the terminal decision and every
principal aggregate within `2.22e-16` absolute. A separate CSV recomputation
recovered the four Windows aggregates exactly at printed precision.

The first sealed Windows attempt is preserved under
`attempts/no_rank_six_plan_001`. It compiled cleanly and stopped before any
JSON/CSV because every cut was at or above the direct boundary and the
controller failed to retain a finite least-bad cut. Amendment 001 changed the
initial comparison from `1` to positive infinity, allowing the already-frozen
`r=0` boundary to serialize with response scale zero and all basis/pilot costs.
No outcome had opened, and no estimator, cost, stream, fingerprint, gate, or
prior changed. The accepted result then completed normally twice. This repair
prevents the early controller defect from being mistaken for scientific
evidence.

## Human promotion disposition

- Subject/evidence: H087-A exact rank-six mechanism fixture, local synthetic
  C2 evidence at width64.
- Current/highest/next tier: no new tier; H087-A remains an exact-support
  negative. The considered next tier was M1.
- Strongest favorable evidence: pooled candidate/direct was slightly favorable
  at `0.997123`, maximum tail passed at `1.004245`, and selected/fixed axes was
  `0.974014`.
- Gate-by-gate status: correctness and maximum tail `PASS`; direct effect and
  network wins `FAIL-SCIENTIFIC`; fixed-coordinate effect
  `FAIL-STRICT-EFFECT`; width128, scaling, M1, registration, F0--F3, and P1
  `NOT-RUN`.
- Primary blocker: `SCIENTIFIC_NEGATIVE_EFFECT_MAGNITUDE_AND_BREADTH`.
- Strict gate sole blocker: **No.** The candidate missed the direct-effect
  requirement by `0.117123` and the win requirement by eight networks.
- Why not promoted: the weight-only six-dimensional basis rarely justified a
  nonzero exact center and produced only a `0.2877%` pooled gain.
- Immediate high-impact unlock: none for unchanged H087-A. The agent executes
  already frozen mechanism-distinct H087-B/T089. No owner action or gate
  change can promote this fingerprint.

## Surprise

T087 froze `.55` probability for rejection before M1. That category occurred,
so the result was **expected** at `-log2(.55)=0.8624964763` bits. The weak
favorable directions do not alter the prospectively frozen terminal category.

## Verification

```bash
bash experiments/checkpoint3/t088/verify_evidence.sh
```

## Task timing

- Start: `2026-08-22T17:06:39,211242402-07:00`
- Pre-task estimate: `60 minutes`
- End/check-off: `2026-08-22T17:22:59,767574951-07:00`
- Actual wall-clock difference: `00:16:20.556332549`
  (`980556332549` ns)
