# T094 — complete-MUB rotation-level subframe ACV adjudication

## Decision

`H090-C` is **scientifically rejected before M1**. The held-out independently
centered subframe correction was `1.0943592164` times the fully charged
unchanged complete-MUB carrier, with `0/12` network wins and maximum
`1.1694740799`. The pooled and breadth gates fail; the maximum-tail gate
passes. This is not a strict-gate near miss.

No ALG identity was registered, no M1/P1 or F0--F3 result was created, and the
PUBLIC complete-MUB carrier's external P1 did not transfer. `ALG014-V000`
remains the project's sole P1 and current submission candidate. Both required
post-first-P1 mechanism-distinct attempts are now complete, so T067 is next.

The frozen `.74` pre-M1-rejection category makes this result **expected** at
`0.434403` information bits.

## Frozen estimator and selection

The estimator used one complete 33-basis Haar-MUB output `Q(R0)`, a contained
same-rotation `s`-basis output `A_s(R0)`, and `k` independent Haar subframe
outputs:

```text
Z = Q(R0) - B [A_s(R0) - (1/k) sum_j A_s(Rj)].
```

The bracket has exactly zero expectation. A 24-group pilot-fit fold froze the
per-network diagonal response with 5% ridge shrink and absolute cap 2. A
separate 24-group pilot-selection fold chose one global production-feasible
pair from 11 configurations. It selected the smallest correction, `s=1` and
`k=1`, at pilot variance-cost ratio `1.115537`. The width-256 proportional
projection uses four of 129 bases, costs `145.174B`, and fits the `250B`
working limit with more than the required reserve.

Pilot evidence could not award M1. The chosen response and configuration were
locked before the independent 64-group held-out fold.

## Held-out result

| Metric | Frozen requirement | Observation | Status |
|---|---:|---:|---|
| pooled candidate/carrier variance-cost | `<=0.99` | `1.094359` | **FAIL-SCIENTIFIC**, adverse by `0.104359` |
| network wins after cost | `>=7/12` | `0/12` | **FAIL-SCIENTIFIC**, short by 7 |
| maximum network ratio | `<2` | `1.169474` | PASS by `0.830526` |
| pooled raw trace variance | report context | `1.060256` | correction itself increased variance `6.03%` |
| cost ratio | fully charged context | `1.032165` | `3.22%` overhead |
| raw-variance wins before cost | report context | `2/12` | weak and non-broad |

Every fully charged network ratio was adverse, ranging from `1.020233` to
`1.169474`. Thus removing or relaxing the `0.99` gate would not create a
credible mechanism signal: the candidate is worse in aggregate, loses on all
networks after cost, and is already adverse on ten networks before cost.

## Theoretical update

The result matches the main predicted failure mode. The complete carrier
already averages 33 collectively balanced bases. A very small subframe is a
noisy proxy for its residual orientation error, while estimating that
subframe's unknown mean requires another Haar rotation. In an idealized model
with independent equal-variance basis errors, `t=s/B`, the optimal diagonal
correction removes only about `t/(1+1/k)` of raw variance while cost grows by
approximately `k t`; their product is adverse for the tested `t<1`. The
empirical pilot therefore chose the smallest possible `s,k`, yet still lost.

More strongly, the empirical correction increased raw variance by `6.03%`, so
the failure is not merely administration cost. The 24-group fitted diagonal
response did not transfer: outputwise subframe/full covariance was too weak or
unstable across independent orientations. This lowers belief in further
small-subframe estimated-mean ACV retunes around an already complete carrier.
An unchanged response ridge, subframe count, extra center, or different basis
prefix must not be rerun as H090-C.

## Correctness and operational evidence

The executable passed:

- all 496 Kerdock pairwise-rank certificates and exact MUB inner products;
- Haar orthogonality (`1.55e-15` maximum), rotated norms (`1.22e-15`), exact
  antipodes, and radial homogeneity (`5.55e-15`);
- exact complete/subframe containment and zero-sum centering coefficients;
- 6,720 distinct source-bound main/center seeds and correct Gaussian raw
  moments (`mean=-1.02e-4`, variance `0.999916`);
- finite outputs, production feasibility, stable source hashes, and byte-exact
  Windows-native replay; and
- GCC/Linux decision and gate-critical reproduction within `2.67e-15` for
  the reported ratios. Compiler-specific low-order bytes differ, as expected.

One pre-result attempt produced no executable or candidate output because
`cmd.exe` defaulted from a UNC working directory to `C:\Windows` and could not
create its object file. The attempt is preserved. Amendment 001 changed only
the compiler process's working directory to the already frozen build path; the
estimator source and every scientific rule remained unchanged. No owner action
was required.

## Human promotion disposition

- Subject/evidence: E068/T094 lawful width-64 held-out mechanism test of
  H090-C's new correction against its unchanged complete-MUB carrier.
- Provenance/novelty: `OURS+PUBLIC`, N1/dimension 2; the PUBLIC carrier remains
  external and outside the project pool.
- Current/highest/next tier: no new tier; M1 considered and not awarded.
- Strongest favorable evidence: maximum `1.169474 <2`; only a safety result.
  Two networks had raw variance below the carrier before cost, but none won
  after cost.
- Gate status: construction/identity/streams/source/replay/cost PASS; pooled
  efficacy FAIL-SCIENTIFIC; breadth FAIL-SCIENTIFIC; maximum PASS; M1 not
  awarded; registration/F0--F3/P1 NOT-RUN.
- Primary blocker: `SCIENTIFIC_NEGATIVE_VARIANCE_DIRECTION_AND_BREADTH`.
- Strict gate sole blocker: **No.** The fully charged aggregate is `9.44%`
  adverse, all 12 networks lose, and raw variance itself is `6.03%` adverse.
- Why not promoted: the new correction fails to predict and cancel the
  complete carrier's residual orientation error after independent centering.
- Immediate high-impact unlock: agent executes T067 and freezes rigorous cycle
  1 around `ALG014-V000`. No machine-owner action is required.

## Verification

```bash
bash experiments/checkpoint3/t094/verify_evidence.sh
```

## Task timing

- Start: `2026-08-23T19:39:53,508134746-07:00`
- Pre-task estimate: `55 minutes`
- End/check-off: `2026-08-23T20:16:49,256051230-07:00`
- Actual wall-clock difference: `00:36:55.747916484`
  (`2215747916484` ns)
