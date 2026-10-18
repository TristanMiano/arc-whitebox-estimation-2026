# T117B — Fable 5.1 exact-anchor target-free screen

## Outcome

T117B is complete without opening any Full V_D/H target. The result separates
two claims that point in different directions:

1. **The exact H002 early-generation mechanism is scientifically negative in
   this spelling.** Main-frame exact layer-1/layer-2 transports reduce A/B
   cross-risk by only `3.560874%`, below Fable's `<10%` falsification boundary.
   The first-anchor shrink is plausible (`.912347`, fold spread `.227703`), but
   the layer-15 control reduces risk by `64.531273%` rather than the predicted
   `<5%`. Error is not predominantly generated at the exact early anchors.
2. **The predeclared ALG024 composition weakly passes the separate flexible
   competition screen.** Its target-free adjusted forecast is
   `1.762602769e-7` versus `1.767819410e-7` for ALG024, a `0.295089%`
   reduction, with 53/100 network improvements and bootstrap `P(win)=.65026`.
   Therefore N1/dimension-4 `ALG025-V000` is registered as a prospective T118
   challenger only. It is not implemented, cost-qualified, promoted, packaged,
   uploaded, or a project-best successor.

ALG024-V000 submission `329529` remains the local and official incumbent.

## Pre-result bookkeeping and rules

The historical T116 `SURPRISE_FREEZE.json` remains byte-for-byte unchanged at
SHA-256 `ea163551c645caad3ca6b4ee1fbac5563bd261d1e898bcdd2f4dd44ee5f2929a`.
`POST_T117_FORECAST_ADDENDUM_2026-09-03.json` separately rebases future events
to official ALG024 and froze H002 probabilities before this empirical screen.

The local Rule-5.5 memo distinguishes genuine computation reduction from
under-declaration or cost-model divergence. Official Rules §5.5 lines 172--179
expressly encourage mathematical structure, symmetry, reduced precision, and
better algorithms. Written Sponsor confirmation is an optional reliance route
when unsure, not a prerequisite to local DF0/T118 research. T118 should ask the
owner only if repeated local inspection leaves a material accounting ambiguity
that would affect designation or submission.

The DF0 parity specification now requires maximum absolute error, RMS error,
and signed systematic drift, including aggregate, per-network, and per-layer
signed means. This addition is documented now; T117B did not execute DF0.

## Data boundary and implementation

The cache loaded only `mlp_id`, `mlp_name`, `mlp_seed`, and `weights` from all
100 public Phase-2 Mini networks at revision
`ce926b7d1ced65faa668c01b94a43f8c4f43783d`. It reused T115's independent A/B
audits at the 1,024-positive-row endpoint. `all_layer_means`, `final_means`,
`avg_variance`, Full V_D, and Full H were not loaded.

For each main and partial antithetic frame, the implementation retained the
actual layer-1 activation cloud, computed the exact Gaussian ReLU mean and
arc-cosine covariance, constructed layer-1 mean and layer-2 variance
discrepancies, and transported them through the closure mean Jacobian. Five
network folds (`index mod 5`) fit global coefficients to the independent A/B
midpoint with fixed normalized ridge `1e-3`; cross-risk was always evaluated
on the held network fold.

Independent derivation found that the source's proposed preactivation feature
is redundant:

```text
d2pre = mean(h1_frame W2) - m1_exact W2
       = (mean(h1_frame) - m1_exact) W2
       = d1 W2.
```

After the layer-2 ReLU Jacobian it is the same transport as `T1`. Treating it
as a second regressor would double-count one channel and make its shrink
non-identifiable. It was retained only as a parity diagnostic. Across all 100
networks, main transport relative RMS disagreement was at most `1.49425e-6`
and partial disagreement at most `6.87135e-7` (float reduction order).

Captured ALG019 components agree with the independent T115 cache to maximum
absolute differences `4.06e-6` (incumbent), `1.44e-6` (frame), and `6.68e-6`
(closure). A one-row reconstruction of ALG024 agrees with the sealed estimator
to maximum `2.282e-7`, RMS `2.437e-8`, and signed mean `-7.866e-10`.

The 100-network cache took `159.916 s` of summed row execution. An initial
Windows Python probe found that the installed interpreter lacks FlopScope; the
same frozen code then ran once to completion in the project WSL environment,
with no transient crash or retry and no owner action required. T118 production
qualification should reproduce candidate-relevant paths in the Windows-native
challenge environment before protected access.

## Target-free diagnostic results

| Held-fold arm | Cross-risk reduction | networks improved | bootstrap P(improve) | coefficient mean |
|---|---:|---:|---:|---|
| main frame `T1+T2var` | `3.560874%` | 68/100 | `1.00000` | `[.912347,.930307]` |
| layer-15 transport control | `64.531273%` | 100/100 | `1.00000` | `[.708216]` |
| matched-norm random layer-1 | `-0.022541%` | 49/100 | `.25422` | `[.045377]` |
| network-shuffled early | `0.003235%` | 52/100 | `.58852` | `[-.013469,-.103055]` |

Fable's diagnostic requires at least 15% early reduction, first-anchor shrink
in `[.4,1.3]`, and under 5% for the layer-15 control. Only the coefficient
range passes. The early result is also below the explicit `<10%` falsification
threshold. This is a scientific rejection of the exact early-dominance story,
not a strict-gate-only miss, incomplete test, implementation failure, or
rejection of all exact anchoring. The random/shuffled controls show the 3.56%
signal is structured, but its magnitude is too small for H002's claimed error
decomposition.

The high layer-15 result points the opposite way: accumulated late state
mismatch is a much stronger frame-error carrier than the exact early anchors.
That supports continuing frozen H116-B and makes late transport/observer work a
better future lead than H002/H003-style early repair. It does not by itself
authorize an outcome-selected new layer-15 candidate in T117B.

## Flexible competition result and candidate boundary

| ALG024 composition | adjusted cross-risk forecast | relative change | networks improved | bootstrap P(win) |
|---|---:|---:|---:|---:|
| ALG024 baseline | `1.767819410e-7` | — | — | — |
| main only | `1.772330145e-7` | `+0.255158%` worse | 46/100 | `.29016` |
| partial only (exploratory) | `1.759083532e-7` | `0.494161%` better | 55/100 | `.79052` |
| predeclared main+partial | `1.762602769e-7` | `0.295089%` better | 53/100 | `.65026` |

The cap and uncapped results are identical; no correction reached the
prospective `.25*cap_scale` cap. Ridge sensitivity is stable: `1e-4`, `1e-3`,
and `1e-2` give bootstrap probabilities `.64955`, `.65026`, and `.65658`.
The stronger partial-only arm is reported but is not selected post hoc.

The frozen full-discovery coefficients for prospective `ALG025-V000` are:

```text
[0.12538246111801082, -0.13111984006259860,
 0.039215021986251875, 0.012711238735215886]
```

in column order `[main T1, main T2var, partial T1, partial T2var]`, applied as
`max(ALG024 - X beta, 0)`. Its estimated advantage is only `5.22e-10`
adjusted, so it is weak evidence and far below the evidence needed for local
succession. It may join T118's pre-target slate only if DF0 funds the exact
anchor operations at the `.1` floor and contract/cost/parity checks pass.
H116-B remains the primary frozen decision and is not replaced.

## Priors and surprise

| Frozen event | prior | observed | surprise |
|---|---:|---|---:|
| full Fable mechanism diagnostic passes | `.50` | no | `1.000` bit |
| flexible competition screen passes | `.55` | yes | `.8625` bit |
| main frame explains at least 25% | `.40` | no | `.7370` bit |

None is materially surprising. The posterior update is qualitative: sharply
downweight early-anchor dominance and related full moment repair H003; retain a
small prior for exact-anchor columns as weak control variates; upweight
late/accumulated-state transport as a diagnostic direction. Do not reinterpret
the weak ALG025 forecast as confirmation of H002, because the gain is driven
by the partial columns and the main-only complete composition is adverse.

## Promotion transparency and next action

| Subject | Highest supported status | Why not promoted | blocker | strict gate sole? | next action |
|---|---|---|---|---|---|
| exact H002 early-dominance mechanism | structured signal but scientific negative | 3.56% is below its explicit 10% falsification boundary and layer-15 reverses the prediction | `SCIENTIFIC_NEGATIVE` | no | close exact claim; a new mechanism is required |
| `ALG025-V000` composition | prospective target-free competition-screen positive; N1/dim-4; U0 | tiny A/B-only forecast; no production source, exact cost, contract, V_D, M1, package, or official result | `EVIDENCE_INCOMPLETE` | no | T118 DF0 funds/qualifies it, then one prospective V_D comparison |
| H116-B | frozen primary T118 decision | not run yet | `EVIDENCE_INCOMPLETE` | no | execute T118 unchanged except for the additive ALG025 arm |
| `ALG024-V000` | local/official incumbent, current-shape M1 | not displaced by non-direct weak proxy evidence | incumbent retained | n/a | compare only on protected V_D/H under T118 |

T118 is next. No immediate upload task is inserted because ALG025 has not
beaten ALG024 on directly comparable submission-facing evidence.

## Timing

- Start: `2026-09-03T08:30:37,694881928-07:00`
- Pre-task estimate: **3 hours wall-clock** (planning range `1--5 hours`)
- End/checkoff: `2026-09-03T08:50:15,543339586-07:00`
- Actual wall time: `00:19:37.848499406` (`1177848499406` ns)
- Estimate difference: completed `02:40:22.151500594` earlier than the
  three-hour point estimate

Approximate allocation: 5 minutes independent derivation/protocol/rules;
11 minutes implementation, diagnostics, and documentation; 3 minutes program
execution/waiting. Categories are rounded.
