# T097 — cross-fitted positive-part Stein shrinkage

T097 is complete and scientifically negative. The exact N1 project candidate
is `ALG016-V000`. It passed deterministic cost, finite-factor, unit-interval,
opposite-pair cross-fit, contract, and runtime preflights. It then failed both
the separate current-shape contest screen and the frozen historical FFSP003 M1
screen. The historical failure is terminal, so F0–F3 did not open and P1 was
not awarded.

## Results

| scope / comparison | pooled ratio | wins | maximum | disposition |
|---|---:|---:|---:|---|
| Phase 2 adjusted candidate / official `ALG015-V000` | `1.705803` | `0/12` | `2.332773` | contest-facing scientific rejection; no succession |
| historical candidate / four-frame carrier | `1.407245` | `3/12` | `2.215272` | all three M1 effect/tail gates fail |

Exact Phase 2 cost was `630,832,642,415` FLOPs, deterministic twice, with
score multiplier `0.286869473`. All observed shrink factors were finite and in
`[0,1]`, and the executable perturbation fixture proved opposite-pair
cross-fitting.

The Phase 2 candidate did improve raw MSE: it was `0.594627` of
`ALG015-V000` and `0.731120` of the four-frame carrier. Its extra compute erased
that gain, producing adjusted `5.505084489e-7` versus `3.227268077e-7` for the
current candidate. Therefore `ALG015-V000` remains our official submission
candidate; `ALG016-V000` does not trigger succession.

Historically, pure closure was `20.442546x` the carrier and the fixed
three-quarter blend was `13.045852x`. H095-D improved that fixed blend by
89.21%, but still lost the carrier by 40.72% and `ALG003-V008` by 28.70%.
Every effect/breadth/tail gate failed: ratio `1.407245` versus `<=0.99`
(`+0.417245`), 3 wins versus at least 7 (deficit 4), and maximum `2.215272`
versus `<2` (`+0.215272`). This is not a strict-gate-only near miss.

The report-only oracle retained `0.856461–1.0` of the carrier, chose exactly
`1.0` on 9/12 networks, and reached pooled oracle/carrier `0.928454`.
Candidate/oracle was `1.515686`. This preserves evidence that carefully
calibrated fusion can help, while locating the failure in the lawful scalar
noise/bias approximation rather than in fixed-target fusion as a whole.

## Surprise and theoretical update

The terminal category was `rejected_before_M1`, frozen at probability `.50`,
so the categorical result carries exactly `1.0` bit and is not surprising.
The magnitude was worse than the frozen ratio center `0.88` by `0.527245` and
exceeded the prior range's upper end `1.18` by `0.227245`, so the severity is
somewhat surprising.

Cross-fitting delivered the intended independence but could not repair
anisotropy, non-Gaussian frame errors, noisy one-pair variance estimation, or
closure bias. Positive-part clipping prevents extrapolation, not harmful
movement toward a bad target. `MECHANISM_ANALYSIS.md` records the detailed
update. The exact H095-D realization is closed; any successor must be a new,
prospectively frozen identity with a target-free bias/anisotropy diagnostic.

## Human promotion disposition

- Subject / evidence class: `ALG016-V000`, `OURS+PUBLIC`, N1 novel
  combination; fresh current-shape contest evidence plus fresh historical
  FFSP003 mechanism evidence.
- Current tier / highest supported tier / next tier considered: U0 / no M1;
  M1 was considered and scientifically rejected. P1 was not reached.
- Positive evidence: Phase 2 raw MSE ratio `0.594627` to `ALG015-V000`;
  historical ratio `0.107869` to the failed fixed blend; target-aware oracle
  ratio `0.928454` to the carrier. These are support, not promotion.
- Gate results: cost, determinism, factors, and cross-fit PASS. Historical
  ratio FAIL-SCIENTIFIC (`1.407245 > 0.99`), breadth FAIL-SCIENTIFIC (`3 < 7`),
  and maximum FAIL-STRICT-GATE (`2.215272 >= 2`). F0–F3 NOT-RUN.
- Primary blocker class: `SCIENTIFIC_NEGATIVE`; the maximum-tail strict miss
  is additional, not the sole blocker.
- Why not promoted: aggregate direction and breadth both contradict the
  claimed carrier improvement; relaxing the maximum gate would not award M1.
- Immediate high-impact unlock: none for the exact candidate. Agent should use
  T098 to rerank materially new anisotropy/bias-aware or lower-cost mechanisms;
  no owner action or gate waiver is indicated.

## Operational disposition

The current-shape WSL result completed normally. The first historical path
selection failed before row access; the next WSL attempts produced a segfault
and two impossible interpreter/library states with empty outputs. A disposable
Windows-native environment with the pinned NumPy/flopscope/WhestBench versions
then completed after an outcome-blind Parquet adapter repair and byte-identical
shard staging. No failed output was admitted, no candidate or gate changed,
and no owner action is required. Later independent-machine/VM reproduction
remains appropriate.

FC005 remains empty because the candidate stopped before formal F0
registration. T098 is next.

Timing: start `2026-08-26T09:35:35.557932708-07:00`; estimate `50 minutes`;
end/check-off `2026-08-26T10:01:18.495925132-07:00`; elapsed
`00:25:42.937992424` (`1542937992424` ns).
