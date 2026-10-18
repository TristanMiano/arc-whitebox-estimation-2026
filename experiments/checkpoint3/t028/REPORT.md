# T028 — top-k residual-rotation duplicate adjudication

Status: **complete negative duplicate adjudication; no new compute, candidate,
or tier created**.

## Decision

T028's proposed top-k affine-residual rotation is not a materially distinct
algorithm. T027/E040 proved the pointwise paired-gradient identity

```text
0.5 * ((grad f(x) - grad a) - (grad f(-x) - grad a))
  = 0.5 * (grad f(x) - grad f(-x)),
```

for every frozen affine chain `a`. Consequently the energy matrix, ordered
eigenbasis, top-k subspaces, and antithetic pair sample errors are the same as
for the historical global-gradient rotation. Rank truncation does not break
the identity: applying the same deterministic eigensolver and rank rule to
equal matrices yields the same rotation. Registering or executing the proposal
under a residual label would therefore duplicate `ALG005-V001`/`ALG005-V004`.

The task explicitly required duplicate adjudication before protected compute.
No materially different signal was predeclared, so no new Windows or WSL
scientific execution was warranted. This is completion of T028's decision
branch, not an interrupted run.

## Reused fresh-scramble evidence

The historical evidence already covers the requested ranks and pilot sizes:

| Existing semantic variant | Frozen rank / pilot | Fresh-scramble result | Retained decision |
|---|---|---:|---|
| `ALG005-V001` | full basis, 256 pilot pairs, width 128 | pooled 20-network MSE ratio `0.654856` to plain; median `0.645853`; win rate `0.70` | retain `M1-mechanism-signal`; global deployment descendants failed |
| `ALG005-V004` | top 64, 512 pilot pairs, width 256 | pooled 20-network MSE ratio `0.888506`; median `0.976728`; win rate `0.50` | retain cautious `M1-mechanism-signal`; exact fixed descendants failed |

T027's identity means an affine-residual rerun at these same ranks, pilots,
networks, and point laws would reproduce the same semantic experiment. The
favorable historical signals remain visible; this adjudication does not erase
their M1 tier. It also does not convert them into a complete F0-F3 candidate.

## Downstream route

- T029's exact fixed affine-residual rotation is closed unchanged because the
  basis and pair outputs are identical to the already-negative exact global
  descendants. It becomes actionable only after a materially different basis
  is defined.
- T030's affine-residual unrotated/rotated mixture has no new rotated arm and
  is likewise conditional on a materially different basis.
- T031 has no current selector to cross-fit. It remains a mandatory method for
  any later learned selector, not an executable task today.
- T033 is therefore the next actionable task. It asks whether layer-local or
  non-affine directions avoid the cancellation identity. T034 remains the
  independent control-variate alternative.

Any result from T033/T034 that becomes a complete candidate must receive an
`ALG###-V###` specification before F0 and enter the qualified F0-F3 funnel.

## Human promotion disposition

- **Subject / evidence class:** E041/T028 duplicate adjudication (`N`), not a
  new algorithm candidate.
- **Current / highest supported tier / next tier:** no new tier / historical
  `ALG005-V001` and `ALG005-V004` remain `M1-mechanism-signal` / no tier is
  considered for the duplicate proposal.
- **Strongest positive evidence:** the existing fresh-scramble ratios are
  `0.654856` and `0.888506`. These are retained local mechanism signals, with
  respective win rates `0.70` and `0.50`; they are not complete current-funnel
  results, and their exact fixed descendants had severe tails.
- **Gate results:** semantic novelty `FAIL-SCIENTIFIC` (matrix and
  participation-ratio ratio `1.0`, requested residual/global difference `0`);
  duplicate rejection `PASS`; historical evidence integrity `PASS`; candidate
  registration `NOT-APPLICABLE`; F0, F1, F2, and F3 `NOT-APPLICABLE` because a
  distinct candidate does not exist; incumbent comparison `NOT-APPLICABLE`.
- **Strict thresholds:** no strict effect, confidence, tail, compute, or
  operational gate was reached. There is therefore no threshold margin whose
  relaxation could promote this proposal.
- **Primary blocker:** `SUPPORT_ONLY` plus `SCIENTIFIC_NEGATIVE` for claimed
  novelty.
- **Strict gate sole blocker:** **No.** Exact semantic identity—not an
  unusually strict promotion rule—prevents a second candidate identity.
- **Plain-language reason not promoted:** it is the already-known global
  rotation under a new name. The positive M1 evidence is preserved on the
  original IDs, while the duplicated residual proposal creates no additional
  evidence or deployable solution.
- **Immediate high-impact unlock:** no owner action, reboot, or gate change is
  indicated. Agent: test a genuinely different layer-local/non-affine basis in
  T033, or an independently fit residual control variate in T034.

## Verification

The verifier checks the immutable T027 identity evidence, historical raw
configurations, P002/P003 ledger metrics, and this disposition without
executing the estimator:

```bash
bash experiments/checkpoint3/t028/verify_evidence.sh
```

## Timing calibration

- Task start: `2026-08-21T17:33:45.060786135-07:00`
- Pre-task estimate: `15 minutes`
- End/check-off: `2026-08-21T17:40:55.106304944-07:00`
- Elapsed: `00:07:10.045446309` (`430045446309` ns)
