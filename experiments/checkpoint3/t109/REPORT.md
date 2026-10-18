# T109 — FC008 theory against ALG019

## Result

T109 completed the required **60 active minutes of theory** without opening a
protected target or assigning an algorithm ID. It selects `H109-EMC` for T110,
but materially repairs the external proposal into **trace-plus-diagonal EMC
(TD-EMC)**: a canonical minimum-norm cubic completion with an exact `O(d^2)`
linear recurrence, a closed first-Wick ReLU approximation, exact marginal
Edgeworth action, chi-radial terminal re-aiming, and an unbiased target-free
cubic/complete-risk proxy.

The current incumbent remains `ALG019-V000`, official submission `328762`, at
adjusted `2.3995983178792816e-7`, final-layer MSE
`2.399598317879281e-6`, multiplier `.1`, and `219,788,985,209` FLOPs. T109
created no score, tier, package, submission, or succession event.

## Main theoretical changes

1. Fable's marginal-cubic state is not closed. T109 retains both cubic trace
   `t_i=sum_j Cum(Z_i,Z_j,Z_j)` and marginal cubic `k_i`, and reconstructs

   ```text
   T_hat(t,k)=T_tr(t-r)+D3(r),
   r=(d+2)[k-3t/(d+2)]/(d-1).
   ```

   This is the unique minimum-Frobenius tensor with the declared trace and
   diagonal. Dense float64 tests verified trace, diagonal, exact weight
   propagation, and first-Wick activation contractions to maximum error
   `8.53e-14`.
2. Full cumulant propagation is public. The defensible classification is
   `EXT+OURS+PUBLIC`, **N1-NOVEL-COMBINATION, novelty dimension 4**, not N2.
3. Fable's `3.5x` inverse-precision calculation is invalid for T108's biased,
   correlated fields. The ambitious `1e-7` target needs a `.416736415` ratio
   to the official incumbent and roughly `86--89%` closure-power removal in
   favorable standalone arithmetic.
4. The terminal sampled skew is constant-radius/angular while TD predicts
   Gaussian-input cumulants. T109 derived an exact chi-moment raw-moment
   conversion before overlap subtraction, eliminating a subtle double-count
   mismatch.
5. Naively centering one Haar frame biases a third moment. T110 instead uses
   two independent four-source witnesses with exact chi restoration. The same
   streams yield unbiased cubic-trace, marginal-cubic-action, layer-mean, and
   complete-risk comparisons without reading `final_means`.
6. The former arbitrary 10% closure-only proxy gate is removed. The final
   competition proxy directly compares exact-multiplier-adjusted complete risk
   to ALG019; breadth, tails, and uncertainty remain visible but are not vetoes.

## Frozen family and priors

T110 receives six prospectively frozen arms: full TD+residual primary,
deterministic TD, order-2 terminal-only control, order-2 correction-disabled
control, a `.5` damped TD recurrence, and a fixed layer-8 late-half restart.
The final priors are:

| Event | Probability |
|---|---:|
| target-free TD mechanism pass | `.50` |
| valid hard/cost route given pass | `.92` |
| V000 beats ALG019 | `.16` |
| any TD arm beats ALG019 | `.20` |
| any TD arm reaches adjusted `1e-7` | `.025` |

A TD-family win would be a `2.322`-bit favorable surprise. A clear failure is
expected overall and must be classified by the first failed boundary rather
than rerun for a better sign.

## Next decisions

- **Decision 1 / T110:** implement and test the immutable TD family. Only a
  route passing algebra/public-K3, target-free cubic/action, layer-mean,
  adjusted complete-risk, and hard/cost checks may open the sealed Phase-2
  rows 92--103. A passing ratio below one must be announced in bold as the new
  local submission candidate.
- **Decision 2 / T111:** if T110 completes, run exactly one rebased H107-U0/U1
  complete-risk proxy. K/R/S/Q remain ranked reserves.

Rigorous historical M1/P1/F0--F3 work remains deferred. This task is theory
and pre-outcome freezing, not scientific promotion.

## Timing and work allocation

Start: `2026-08-28T12:57:33,736744899-07:00`. Pre-task estimate: **about 90
minutes**. The theory floor was reached at
`2026-08-28T13:57:36,625279666-07:00`, after
`01:00:02.888534767`. Approximately 45 minutes were direct derivation/writing
and 15 minutes were theory-relevant literature/source/algebra work; code
execution was under one minute and code waiting was zero during that interval.

End/checkoff: `2026-08-28T14:12:55,337612440-07:00`. Total elapsed:
`01:15:21.600867541` (`4521600867541` ns), beating the 90-minute estimate by
`00:14:38.399132459`. Post-theory documentation, state sealing, code execution,
and verification occupied approximately `15.312` minutes; machine waiting was
zero.
