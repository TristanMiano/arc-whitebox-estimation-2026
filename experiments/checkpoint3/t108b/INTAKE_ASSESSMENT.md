# T108B — Fable EMC follow-up intake and test decision

## Decision

`EXT-FABLE5-H007`, given project alias **`H109-EMC`**, is promising enough to
test. It is accepted as a **provisional hypothesis/test candidate**, not yet an
algorithm identity and not evidence that the `1e-7` target is likely. T110 is
assigned to test it after T109 finishes the exact derivation, cost recovery,
prior-art audit, and pre-outcome freeze.

The reason to spend a test is the combination of high upside, a positive
terminal-slice ancestor in ALG019/H107-O, a mathematically valid first-order
ReLU Edgeworth ladder, and an unusually cheap target-free failure test. The
reason not to accept Fable's headline forecast is that three load-bearing
steps remain unproved on the project ensemble.

## Corrected target arithmetic

The actual incumbent is now ALG019-V000 submission 328762, not the ALG018
score used in the follow-up. Its official adjusted score is
`2.3995983178792816e-7`, raw final-layer MSE is
`2.399598317879281e-6`, and multiplier is `.1`. Reaching adjusted `1e-7` at
the floor therefore requires raw MSE at most `1e-6`: a ratio
`.4167364148` to the incumbent, or **58.326359% raw/adjusted reduction**.

ALG019 uses `219,788,985,209` FLOPs and has only `113,340,346.2` FLOPs of
headroom below the `.1` boundary. Fable projects `0.6--1.0B` new FLOPs. That
does **not** fit unchanged. At T108's measured approximately `69.94M` FLOPs per
extra partial row, an otherwise unchanged implementation must recover roughly
9--15 rows' cost, or recover equivalent closure work, before it can retain the
`.1` multiplier. T107's already-open order reanalysis makes order-2 closure a
legitimate cost-recovery control: it saved about `504.4M` FLOPs relative to
order 12 in that implementation and changed pooled blend MSE by only
`.0198%`, but T110 must remeasure both cost and parity in the ALG019/EMC code.

## What is theoretically supported

1. For standardized third cumulant `kappa3`, the first-order Edgeworth action
   on shifted ReLU moments is correct, including
   `Delta mean = -sigma*kappa3*alpha*phi(alpha)/6` and the corresponding
   second-, third-, and fourth-moment ladder.
2. Finite-width networks admit systematic non-Gaussian corrections and
   layer-to-layer perturbative treatments in published work. This supports the
   research direction, not Fable's particular trace-only recursion or effect
   size.
3. H107-O's terminal correction already produced positive local and official
   evidence as one component of ALG019. Extending a winning terminal slice to
   accumulated layers is a coherent, falsifiable hypothesis rather than an
   arbitrary formula search.
4. Fable's synthetic channel decomposition is useful directional evidence:
   final preactivation mean transport dominates its closure error at
   `d=128/256`. The result is external synthetic evidence only because scripts
   and raw outputs were not delivered and it is not the contest ensemble.

## What is not yet supported

1. **The `3.5x` closure calculation is not a valid risk proof.** Treating the
   fusion weights as independent precision shares ignores bias, covariance
   between F/P/C fields, alpha-dependent weights, and the changed ALG019
   estimator. T109/T110 must use measured complete residual covariance and
   route-matched score arithmetic instead.
2. **Mean-transport dominance does not identify its cause.** Showing that
   `Phi(alpha)*(mu_true-mu_closure)` explains most final error does not show
   that accumulated marginal third cumulants caused that mean discrepancy.
   Higher cumulants and joint/cross-coordinate cumulants can contribute.
3. **The proposed state is not a closed third-order system.** A vector of
   marginal preactivation third cumulants is insufficient to propagate all
   bivariate ReLU cumulants. The trace-generated and diagonal-transport
   truncations are approximations whose sign and fidelity must be tested.
4. **The `40%` probability of reaching `1e-7` is not calibrated.** It rests on
   synthetic `d<=256` effects, an invalid independent-precision reconstruction,
   and the unverified causal/trace truncations. The project intake prior is
   deliberately lower: `.45` that the target-free mechanism test passes,
   `.40` conditional probability of beating ALG019 if it passes and remains
   sub-floor, for `.18` unconditional incumbent-win probability; `.08`
   unconditional probability of adjusted score at most `1e-7`. These are
   subjective frozen intake priors, not confidence intervals.

## Novelty and literature disposition

The project provisionally labels H109-EMC **N1-NOVEL-COMBINATION, dimension
4**: layerwise finite-width/Edgeworth correction, an `O(d^2)` trace reduction,
realized-column projection, and score-floor-aware fusion/cost recovery. The
general finite-width perturbation and Edgeworth ideas are prior art, so N2 is
not justified without a deeper audit. Primary sources checked at intake:

- Sho Yaida, [*Non-Gaussian processes and neural networks at finite
  widths*](https://proceedings.mlr.press/v107/yaida20a.html), PMLR 2020 /
  arXiv:1910.00019.
- Roberts, Yaida, and Hanin, [*The Principles of Deep Learning
  Theory*](https://arxiv.org/abs/2106.10165), arXiv:2106.10165 / Cambridge
  University Press 2022.

## Assigned route

T109 must turn the prose into an executable closed approximation and freeze
the exact recursion, controls, cost-recovery rule, coefficients, priors, and
fresh cohort before targets. T110 then performs:

1. independent quadrature/direct-Monte-Carlo checks of every moment action and
   small-width layer recursion;
2. a target-free contest-ensemble kill comparing generated cumulant traces and
   per-layer closure-vs-independent-frame/partial mean discrepancies;
3. exact Windows-native FlopScope/resource/package qualification with a
   predeclared cost-recovery rule and unchanged `.1` multiplier, or exact
   pricing above the floor;
4. only on a target-free pass, one frozen minimum-12-network Phase-2 adjusted
   screen against ALG019-V000, with terminal-only and correction-disabled
   route-matched controls.

If the target-free mechanism or cost route fails, close H109-EMC immediately
without protected score work. If it survives but adjusted ratio is `>=1`,
close the unchanged submission branch. If it beats ALG019, report the new
project best in bold. Separately report whether it reaches `1e-7`; missing that
ambitious milestone is not itself a rejection if it still improves the
incumbent.

## Intake provenance

The exact owner attachment is preserved at
`external_handoffs/fable_followup_emc_2026-08-28/FABLE5_EMC_FOLLOWUP.txt`,
SHA-256 `98c5b9b672e0d1e451f1b61f0215416c5dbbb49ad65b988a35150c9b487c0077`.
No protected outcome, algorithm ID, tier, or submission state changed in this
intake.

Timing: formal registration started `2026-08-28T09:00:04,798690789-07:00`;
estimated `25 minutes`; final checkoff
`2026-08-28T09:07:04,786890697-07:00`; actual elapsed
`00:06:59.988199908` (`419988199908` ns). The formal task clock begins after
the initial attachment read and covers the durable audit/registration work.
