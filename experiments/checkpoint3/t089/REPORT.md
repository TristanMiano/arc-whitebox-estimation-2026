# T089 — Coupled-survival affine-hybrid randomized telescope

## Decision

Reject unchanged `H087-B` before M1 and continue to the mandatory T090
novelty recurrence. P1 is not awarded. The held-out exact-frequency schedule,
T083 single-cut comparison, width-256 registration, FC004/F0--F3, and official
scoring were correctly not opened.

This is a strong scientific variance-cost rejection, not a strict-gate-only
near miss. The pooled optimistic tail-covariance oracle was
`1.6084774993462183` of direct antithetic sampling versus required `<0.80`.
It missed the threshold by `0.8084774993462183` absolute (`101.0597%` of the
threshold) and was itself `60.8477%` worse than direct. Every one of the 12
networks was adverse: the best per-network ratio was `1.2544057345`, the
median `1.6192909896`, and the worst `1.9968885865`.

Because this oracle already knows the complete pilot increment covariance and
omits probability rounding, reserve, and precomputation, downstream
implementation realism can only add burdens absent a new mechanism. Relaxing
the `<0.80` gate would not rescue an estimator that fails even the direct
`<1` direction on all networks.

## Frozen estimator and cost

At depths `{0,4,8,12,16,20,24,28,32}`, `F_d` is the T025 affine chain plus
the exact residual contributions through layer `d`. For a single nested
truncation rank and positive monotone survival probabilities, the estimator is

```text
Z = F_0 + sum_{b=1}^8 I(K >= b) (F_{4b} - F_{4(b-1)}) / p_b.
```

The same antithetic inputs, nonlinear prefixes, and rank are shared across all
increments. Consequently `E[I_i I_j]=p_max(i,j)`, and the oracle retained the
entire `8 x 8` raw increment second-moment matrix rather than discarding
cross-increment covariance. The frozen charge was `16 w^2` per four-layer
block—both antipodes' four exact forward layers and four suffix products—
versus `64 w^2` for direct.

The 12 selected schedules were genuinely nontrivial and network-specific.
For example, network 0 selected approximately
`[1,.4866,.2577,.2577,.2577,.2577,.2577,.2577]`; network 5 selected
`[1,.6368,.3243,.2622,.2,.2,.1722,.1328]`. Thus the result is not an
accidental all-direct boundary. Even the best network's optimized schedule
remained 25.44% worse than direct.

## Gate results

| Gate | Frozen requirement | Observation | Status |
|---|---:|---:|---|
| T025 coefficients, suffix, block, conditional, and `p=1` identities | numerical limits pass | max telescope error `8.44e-15`; suffix `5.33e-15` | PASS |
| Positive monotone survival schedules | all 12 | all valid | PASS |
| Pooled optimistic oracle/direct | `<0.80` | `1.6084774993` | FAIL-SCIENTIFIC |
| Oracle network direction | contextual `<1` | `0/12`; range `1.254406–1.996889` | FAIL-SCIENTIFIC |
| Held-out candidate/direct | only after oracle pass; `<0.90` | `NOT-RUN` | NOT-RUN |
| Held-out wins / maximum | `>=9/12`; `<1.25` after oracle pass | `NOT-RUN` | NOT-RUN |
| Candidate/T083 single-cut | `<0.95` after oracle pass | `NOT-RUN` | NOT-RUN |
| M1 / registration / F0--F3 / P1 | only after all prior gates | no / no / `NOT-RUN` / no | NOT-RUN |

## Defect and reproducibility audit

The accepted MSVC 19.43 Windows-native executable depended only on
`KERNEL32.dll`. Source hashes were unchanged during execution; its two JSON
and CSV runs were byte-identical; stderr was empty; and all analytic checks
passed by large margins. An independent GCC/Linux build reproduced the pooled
ratio exactly at printed precision, the median within `2.22e-16`, the maximum
within `4.44e-16`, and the terminal decision.

The tail-noise equation was implemented directly from the frozen nested-event
identity, including all signed off-diagonal covariances. The optimizer used
constant, geometric, and single-cut starts followed by repeated log and linear
coordinate searches over every positive monotone coordinate interval. This
is extensive deterministic numerical optimization, not a formal symbolic
global-optimum certificate. A hard-to-spot optimizer defect would therefore
remain logically possible, but it would have to hide more than a 50% further
reduction—from `1.60848` to below `0.80`—while all 12 independently optimized
networks currently lose to direct. Together with cross-compiler agreement and
the exact identities, that makes an implementation defect capable of
reversing this decision unlikely. Later stable-machine/VM reproduction remains
required under the project-wide containment policy.

No operational failure occurred and no repair or retry was needed.

## Human promotion disposition

- Subject/evidence: H087-B exact common-path nested-survival mechanism,
  local synthetic C2 evidence.
- Current/highest/next tier: no new tier; exact-target negative. The considered
  next tier was M1.
- Strongest favorable evidence: the covariance-aware schedules reduced the
  naive all-survive telescope's `2x` work ratio on every network; the best
  reached `1.254406`.
- Gate-by-gate status: identities and schedule construction `PASS`; optimistic
  oracle `FAIL-SCIENTIFIC`; held-out, ablation, M1, registration, F0--F3, and
  P1 `NOT-RUN`.
- Primary blocker: `SCIENTIFIC_NEGATIVE_OPTIMISTIC_VARIANCE_COST`.
- Strict gate sole blocker: **No.** The optimistic candidate was worse than
  direct on all 12 networks and pooled at `1.60848`.
- Why not promoted: preserving cross-increment covariance did not overcome
  the residual-suffix work and survival noise.
- Immediate high-impact unlock: none for unchanged H087-B. T090 must generate
  or rerank a materially different mechanism; no owner action or threshold
  change can promote this fingerprint.

## Novelty and surprise

H087-B remains an `OURS+PUBLIC`, `N1-NOVEL-COMBINATION` negative result. It is
a real project hypothesis, not a control, but it is not registered as an ALG,
promoted contribution, or submission route. Randomized telescoping is close
public prior art; the project-specific affine-hybrid/common-path combination
does not alter that provenance assessment.

T087 froze `.63` probability for rejection before M1. That category occurred,
so the outcome was **expected** at `-log2(.63)=0.6665762663` bits. The magnitude
of the loss is stronger than the category label alone, but category surprise
is reported prospectively as required.

## Verification

```bash
bash experiments/checkpoint3/t089/verify_evidence.sh
```

## Task timing

- Start: `2026-08-22T17:26:05,536104783-07:00`
- Pre-task estimate: `60 minutes`
- End/check-off: `2026-08-22T17:41:55,465599552-07:00`
- Actual wall-clock difference: `00:15:49.929494769`
  (`949929494769` ns)
