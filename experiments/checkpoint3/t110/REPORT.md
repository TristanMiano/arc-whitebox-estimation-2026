# T110 — terminal test of H109 trace-plus-diagonal EMC

## Outcome

T110 ends without a new submission candidate. The sole route independently
allowed to reach protected scoring was the order-2/cost-order control,
registered as `ALG020-V000`. On every genuinely fresh row remaining in the
pinned public Phase-2 mini split, it scored slightly worse than the incumbent:

| Route | Raw final-layer MSE | Adjusted score | Multiplier |
|---|---:|---:|---:|
| `ALG020-V000` | `2.504291275e-6` | `2.504291275e-7` | `.1` |
| `ALG019-V000` | `2.503858264e-6` | `2.503858264e-7` | `.1` |

The adjusted ratio was `1.000172937`, with `3/8` wins, median paired ratio
`1.000167387`, maximum `1.001134855`, and bootstrap ratio interval lower-05
`0.999811384`, upper-90 `1.000487989`, upper-95 `1.000573381`. It also missed
the ambitious adjusted `1e-7` milestone. Under the frozen rule, the exact
route is competitively rejected and closed unchanged. **`ALG019-V000`
remains the local and official project best**, submission `328762`, official
adjusted score `2.399598318e-7`.

The local numbers above are a paired cohort comparison. They must not be
mixed directly with ALG019's official score, which came from the grader's
different hidden cohort.

## What happened to the proposed TD mechanism

The theoretical mechanism produced real positive evidence:

- all 30 independent shifted-ReLU quadrature cases passed, with maximum error
  `1.22e-15`;
- exact linear TD transport passed at `5.55e-17`, the production activation
  matched its independent reference at `1.27e-7` under the frozen `5e-7`
  float32 tolerance, and the remaining semantic checks passed;
- TD improved K2 small-width final-mean MSE to `0.448735` and late-layer MSE to
  `0.384818`; trace and diagonal MSEs were `0.237721` and `0.308124` of their
  zero controls;
- all five preregistered target-free TD trace/action/mean gates passed. Late
  pooled `Q_trace=-10.51246`, `Q_action=-1.5986e-7`, and all nine late-layer
  crossed-mean comparisons were favorable.

The required pinned public full-K3 comparator, however, was numerically
pathological in the same small-width test: its pooled final-mean MSE was
`2.154950289e8` times K2 and its late-layer ratio was `7.372921518e7`.
Because K3-improves-K2 was frozen as a prerequisite, no TD arm could access
protected targets. This is a **strict-gate/reference-control limitation**, not
a scientific negation of TD.

That distinction differs by arm:

| Frozen arm | Target-free adjusted complete-risk difference vs ALG019 | Wins | Disposition |
|---|---:|---:|---|
| V005 late-half TD + O | `-7.75944e-9` | 8/12 | all non-K3 gates pass; **solely K3-limited** |
| V004 half-strength TD + O | `-4.84281e-10` | 5/12 | all non-K3 gates pass; **solely K3-limited** |
| V002 K2 + ordinary O | `-2.00871e-11` | 5/12 | qualified; protected loss as `ALG020-V000` |
| V003 K2, no O | `+7.02062e-9` | 4/12 | target-free competition loss |
| V000 full TD + re-aimed O | `+3.77731e-8` | 3/12 | target-free competition loss in addition to K3 block |
| V001 full TD, no O | `+4.25884e-8` | 3/12 | target-free competition loss in addition to K3 block |

Thus H109's aggressive all-layer forms are not supported as current
submission routes, but the damped/late TD mechanism remains academically
unresolved. Reconsideration requires a new prospective higher-order reference
or replacement gate, not a retroactive T110 waiver.

## Exact cost and protected-data discipline

All six candidate routes and ALG019 were exactly metered twice on Windows
native with WhestBench 0.16 and FlopScope 0.12. Every route stayed at the `.1`
floor. V002 used `219,755,848,521` FLOPs; ALG019 used `219,788,985,209`.
Shapes, finiteness, deterministic bytes/FLOPs, the hard budget, reserve, and
residual-time qualification passed.

The source-frozen target-free proxy read only metadata and weights on rows
64--75 and wrote atomic per-row checkpoints. Only after V002's direct proxy
pass were protected-input predictions generated. Their arrays were sealed at
SHA-256 `9b37f6fb...f10b4` before the separately frozen scorer loaded
`final_means` once.

Two pre-target infrastructure corrections are preserved:

1. T109's first cohort seal named `full` shard paths despite freezing the
   Phase-2 `mini` split; T110 repaired the paths and official LFS hashes before
   candidate evidence.
2. The pinned final mini shard has four rows, not eight. Therefore global rows
   100--103 do not exist. T110 used all eight genuinely fresh remaining rows
   92--99 and did not backfill already opened rows 88--91. The requested
   minimum of 12 was impossible and is explicitly **not met**, so this is an
   eight-network competition screen rather than a minimum-12 scientific test.

The target-blind generator also encountered four transient incumbent
residual-time vetoes. Three unchanged retries and a garbage-collection repair
were attempted first. The redundant per-protected-row veto was then removed
because both sources had already passed the frozen exact gate twice and the
timings remained recorded. The subsequently successful run in fact stayed
under the original cap on every row (candidate max `.19294s`, incumbent max
`.34690s`). No estimator source, threshold, prediction semantics, or protected
outcome changed during those repairs.

## Surprise and routing

Before protected access, the control-derived ALG020 route had only `.10`
probability of beating ALG019 because its proxy advantage was microscopic.
The observed loss is therefore expected (`-log2(.90)=0.152003` bits). Failure
to reach `1e-7` was even more expected under the frozen `.005` success prior.

No scientific M1/P1/R1/P2 tier is awarded or denied by this competition
screen. ALG020 is closed for submission competition, no package or upload is
authorized, and no official state changed. T110 consumes FC008 decision 1;
T111 is next and is the sole conditional H107-U0/U1 decision.

## Evidence

- `SEMANTIC_QUALIFICATION.json` — algebra, quadrature, and production parity.
- `SMALL_WIDTH_QUALIFICATION.json` and `PUBLIC_K3_AUDIT.md` — TD and public-K3
  small-width results.
- `EXACT_COST_RESULT_WINDOWS.json` — twice-repeated exact cost/hard gates.
- `TARGET_FREE_PROXY.json` plus `proxy_rows/` — sealed target-free evidence.
- `PREOUTCOME_SEAL.json`, `PREDICTION_SEAL.json`, and `PREDICTIONS.npz` —
  identity, cohort, source, timing, and prediction seals.
- `PROTECTED_SCORE.json` — the one protected scoring result.

Later reproduction on an independent stable machine or VM remains required
for substantive scientific use of the positive TD evidence.

## Timing and work allocation

- Start: `2026-08-28T14:16:32,368125998-07:00`
- Pre-task estimate: **about 3 hours**
- End/checkoff: `2026-08-28T15:08:23,013485875-07:00`
- Actual wall time: `00:51:50.645795351` (`3110645795351` ns)
- Estimate error: completed `02:08:09.354204649` earlier than estimated

Approximate allocation was 14 minutes of mathematical/mechanism analysis and
public-K3 source audit, 29 minutes of implementation, debugging, verification,
and durable documentation, and 9 minutes of machine execution/download/wait.
The categories are rounded and overlap slightly at analysis-driven debugging
boundaries; there was no owner-blocked idle interval.
