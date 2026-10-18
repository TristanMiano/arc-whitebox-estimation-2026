# T157 — NFC128 loses the initial paired screen

**Complete: retain ALG043-V000 / submission330597, official adjusted score
5.419051334510831e−9. No upload.** The fixed NFC128 / ALG048-V000 source runs
within resource limits, but loses on both repeatedly exposed development
networks. Stop after this pair; no additional score cohort, rank/ridge/seed
ladder, fitting, package qualification or grading attempt.

## Actual result

| Development row | Raw MSE / parent | Adjusted score / parent | FLOPs, billions | Residual seconds |
|---|---:|---:|---:|---:|
| 750 | 1.3810 | 1.2700 | 540.062 | 0.246 |
| 976 | 1.3507 | 1.2371 | 511.508 | 0.252 |

Arithmetic mean raw MSE rises **36.65%**: 2.940095534e-08 versus
2.151485850e-08. Arithmetic mean adjusted score worsens **25.47%**:
7.040836512e-09 versus 5.611462575e-09. There are0/2
adjusted wins. These are local exploratory results, not official grades or a
calibrated success probability. The pair was explicitly allowed to reject a
large loss before a12-network screen. Predictions and identities were saved
before this task's scoring pass. Earlier exposure to these targets is disclosed.

The first/cold call costs540.062B; steady cost is**511.508B**, **8.41% below**
the matched parent's558.473B. That is inside the500–530B research estimate.
Setup takes.026s, maximum prediction wall32.74s, maximum residual.253s, and
maximum peak process memory5.33GiB. Both calls pass every cap. Two full-size
calls total1.051570T FLOPs and57.54 prediction seconds. Generated algebra and
fallback fixtures are additional checks, not additional challenge networks.

## Implemented and checked

The fixed specification is [H153-NFC128](../../theory/t153/NFC128_SPEC.md).
The source preserves native births, thin feedback/residuals, fourth regeneration
and public calibration, and changes suite-only old-source selection at256/128.
It uses the64-column mean sketch,16 independent128-column response designs,
fresh coupled coefficients at both tiers, the physical trace denominator1024,
and weighted **dual** factor projections. Old resident legs get the actual
previous gate; the young joiner already has it. Both predictors and the entire
new numerical path use FlopScope; static input-independent signs use fnp.load.
There were no API failures, algorithm repairs or adaptive formula changes.

17 generated checks compare the matrix-free roots, weighted projector,
factored/coherent native Gram and nested refresh against explicit matrix/tensor
constructions; they also expand the future-response sum independently to check
its coordinates. They pass. The generic core is structurally identical after
resolving suite branches, and1x1,32x6 and512x10 generated fixtures match the
parent's output bytes and FLOPs. The512x10 fixture exercises its original two
compression tiers. On the challenge pair, layers0–4 also match the current
parent exactly, before the first changed compression.

No concrete integration error was found. These checks are narrower than full
archive qualification or a proof of every suite-path invariant. Current-package
byte replay was not run for this rejected candidate, and historical parent
byte-replay discrepancies remain preserved in their original records.

## What the failure does and does not show

The additional future metric did not buy the required accuracy. The cheaper
T153 P15 coupled256/128 comparator has a1.3555 mean raw ratio and1.1332 adjusted
ratio on this same pair, versus NFC128's1.3665 and1.2547. Thus this realization
spends about46.8B additional steady FLOPs without a mean raw improvement.
That comparison changes several things together and is not an isolated ablation.

The earlier encouraging P25–P28 measurements used saved parent states and
spectral selection. The actual candidate additionally uses combined sketches,
a narrow range finder, two interacting projection tiers and its own evolving
state. The single-leg future metric is itself only a surrogate for final error.
Any of those gaps, including altered covariance/fourth-state feedback, could
explain the failure. **This task did not isolate the cause.** Improving a saved
old-source response is insufficient evidence of an improved full recurrence.
The fixed leaf is now tested and closed; the entire future-compression route
has not been disproved.

Recommend the proposed **T158 empirical theory recurrence**, beginning with one
small saved-state check of the approximation gap. Continue a compression repair
only with a concrete positive lead; otherwise prioritize a compatible homogeneous
or conditional/observable state with larger possible gain. Keep the untested
current-rank coupled metric and fresh trajectory-matched head as cheap reserves.
No next task, agent, parameter sweep or fit is authorized by this report.

## Evidence and reproduction

- [Registered scope](START_AND_SPEC.json), [fixed source/design hashes](SOURCE_FREEZE.json).
- [Sealed calls](attempts/exploratory-001/RESULT.json), [paired score](attempts/exploratory-001/SCORE.json).
- [Algebra checks](ALGEBRA_CHECK.json), [generic fallback check](FALLBACK_CHECK.json).
- [Task result](RESULT.json), [measured timing and estimate error](TIMING.json), [next proposal](NEXT_PROPOSAL.json).
- Production source: submissions/phase2_alg048_v000/estimator.py, SHA256
  `cef30a8da11b9ccf3b415c3cf28b77c994fb6700191f0eb06788b7a33900bb4a`. Designs were generated once with
  PCG64 seed15329 before the first candidate call; no seed selection.

From the repository root, use the recorded runtime and a new output directory:

```sh
OPENBLAS_NUM_THREADS=4 OMP_NUM_THREADS=4 MKL_NUM_THREADS=4 tmp/t128-runtime312/bin/python experiments/submission_policy/t157/run_candidate.py --rows 750 976 --output experiments/submission_policy/t157/attempts/NEW_REPLAY_DIRECTORY
```

The original150–240 minute planning range was not a time floor. Early clear
rejection made the rest of the submission pipeline unnecessary. TIMING.json
records measured elapsed time and the untimed preliminary-orientation limitation;
no active research floor is claimed for this implementation task.
