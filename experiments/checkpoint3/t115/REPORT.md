# T115 — H113-N replicate-held audit-carrier terminal decision

## Outcome

T115 reached its terminal direct decision. The target-free screen lawfully
opened exactly one comparison, but frozen N1/dimension-4 `ALG023-V000` lost to
`ALG019-V000`. The exact spelling is closed; no second carrier was tested, no
scientific tier or submission incumbent changed, no package was required, and
no upload occurred. `ALG019-V000` remains the local and official project best,
submission `328762`.

| Direct quantity, reused Mini 100 | `ALG023-V000` | `ALG019-V000` | candidate / incumbent |
|---|---:|---:|---:|
| raw final-layer MSE | `3.022166400185e-6` | `2.438169963016e-6` | `1.239522448` |
| adjusted score | `3.396486871560e-7` | `2.438169963016e-7` | `1.393047623` |
| per-network wins | `45/100` raw | — | `14/100` adjusted |
| maximum paired ratio | — | — | `6.295173` raw / `7.074883` adjusted |
| bootstrap `P(adjusted win)` | — | — | `0.000000` |

This is a direct competition rejection, not a rejection caused by a strict
confidence gate. The direct adjusted 90% ratio interval was
`[1.252504,1.515494]`, entirely adverse.

## Target-free selection and why it opened

Windows-native L0 qualification passed every frozen source, independence,
swap, risk-identity, homogeneity, parent/endpoint/LOO parity, clamp,
determinism, exact-cost, and hard-budget check. The 100-network development
cache loaded only `mlp_id`, `mlp_name`, `mlp_seed`, and `weights`; it cached
one maximal A/B propagation per network and reused nested prefixes.

The full-space replicate estimate was calibrated: pooled incumbent risk
`T=2.592816797396e-6`, 90% interval
`[2.210912181216e-6,2.988296004811e-6]`, containing the recorded local
`2.4381829362e-6`. The selected arm was full-response rank-16, equal-dual-half
DALT at 384 total positive rows, with the gap rule

```text
h0 = .0729589803,  h1 = .4672147205,  h_rest = 0,
gap iff sigma1/sigma2 >= 1.5.
```

Its paired equation-(227) forecast was `-1.450185855e-8` adjusted relative to
the audit-estimated incumbent, a 5.59% paired improvement, with bootstrap
`P(win)=.53316`. That passes the deliberately flexible rule (212). Its
absolute forecast `2.447798211883e-7` was `1.003944x` the previously recorded
local score, and its upper interval and strict 5% margin both failed. Those
strict diagnostics were visibly weak, but—as the owner required—they did not
silently ban the direct comparison.

The gap arm was not more than one standard error better than its global arm.
The first analyzer draft incorrectly treated that secondary simplicity rule
as a veto. It was repaired before targets because the final T113 authority
explicitly says one-SE preference cannot close all arms that pass (212).

## Why the proxy failed

The selected cross-fitted audit proxy forecast mean raw change
`-4.147859077e-7`; direct targets measured `+5.839964372e-7`, a calibration
error of `+9.987823448e-7`. Their network correlation was `-.57250`.
The miss was concentrated in the 36 gap-qualified networks:

| subgroup | proxy raw change | direct raw change | raw wins |
|---|---:|---:|---:|
| gap-qualified, `n=36` | `-1.787360762e-6` | `+1.631194480e-6` | `14/36` |
| ordinary scalar, `n=64` | `+3.572874481e-7` | `-5.052461842e-9` | `31/64` |

Thus the exact dual-audit identity exposed real but extremely noisy projected
capacity and selected a gap coefficient whose favorable replicate estimate
did not transfer to the actual means. The direct result is strong evidence
against this frozen gap-DALT spelling and moderate evidence against using the
same high-shrink gap policy without a new mechanism. It is not proof that all
response-space correction is absent.

## Controls, fallbacks, and conditional branches

The selected full-chain proxy was materially lower than matched controls:

| target-free arm | expected adjusted | bootstrap `P(win)` |
|---|---:|---:|
| full rank-16 dual-384 gap | `2.447798212e-7` | `.53316` |
| random rank-16 dual-256 global | `2.798653319e-7` | `0` |
| local rank-16 dual-256 H | `2.804131229e-7` | `.00026` |

This preserves positive mechanism evidence despite failed direct transfer.
NAAR's best arm improved raw risk by only `7.299e-8` and lost after compute at
`2.718987156e-7`; NASES's best arm worsened its P1 parent by `1.024e-7` and
was decisively noncompetitive at `7.010903743e-7`. They did not open separate
direct comparisons because T115 prospectively allowed exactly one.

The conservative multi-basis optimum was one row, so `{2048,4096}` was
`NOT-TRIGGERED`, not empirically rejected. Its lower-90 projected capacity was
`5.6831e-7`, but upper outside risk `2.0699e-6` and audit noise `2.7662e-6`
made additional audit compute unattractive.

## Explicit unresolved strict-rule case

Rank-32 full dual-384 gap was the numerically best diagnostic proxy:
adjusted `2.401625326e-7`, paired `P(win)=.54524`. It was not eligible because
T113 admitted rank 32 only when it was the **unique** passing DALT rank; rank
16 also passed. After rank 16 lost directly, the separate frozen no-second-
candidate rule forbade opening rank 32.

Therefore rank 32 is **not scientifically rejected**. It is unresolved and
strict-rule-limited, while rank-16 `ALG023-V000` is directly rejected. An
owner could explicitly authorize a new decision if they judged this diagnostic
worth the target-selection risk, but T115 itself cannot do so. This distinction
is recorded so a future handoff cannot misstate rank 32 as tested or failed.

## Implementation and operational audit

The selected estimator used exactly two 192-row child-separated Haar frames.
Its 64 non-gap routes cost `247,139,053,474` FLOPs and its 36 gap routes cost
`247,139,065,760`, multipliers `.1123858299/.1123858355`; all were below
`2^41`. An independent cache reconstruction matched production predictions to
`4.7684e-7` maximum absolute output difference (floating reduction order),
reproduced all 36 gap decisions, and matched both exact cost receipts.

One audit-cache operation hit a transient internal FlopScope `TypeError` at
row 67; identical resume completed it. The first in-memory direct-prediction
run exited at row 89 with Windows code 5 and no traceback. The runner was made
atomically row-resumable, and the identical retry completed all 100 rows.
Neither event changed sources, seeds, coefficients, targets, or scientific
outcomes; no owner action was needed.

## Prior surprise and next work

The selected DALT family had frozen `.47` probability to beat the incumbent.
The direct loss has prior probability `.53`, or `.916` bits: unsurprising to
mild negative evidence. Target-free capacity did clear a lawful score path,
the `.57`-prior event (`.811` bits). Across FC010, neither the `.48` LPITF nor
`.47` DALT decision produced a successor; the frozen dependence-aware
portfolio miss probability was `.36`, or `1.474` bits—moderately surprising
negative evidence.

The DALT capacity trigger for FC011 is satisfied: response-space signal was
materially positive, but paid production auditing failed. T116 should begin a
new owner-duration theory recurrence, re-rank the audit-trained/audit-free
response-correction reserve against wholly new avenues, and not spend ordinary
work proving this known direct loser more rigorously.

## Timing and work allocation

- Start: `2026-08-31T15:32:17,333128856-07:00`
- Pre-task estimate: **about 3 hours active wall-clock** (planning range
  `2--5 hours`)
- End/checkoff: `2026-08-31T16:23:28,363949366-07:00`
- Actual wall time: `00:51:11.030820510` (`3071030820510` ns)
- Estimate difference: completed `02:08:48.969179490` earlier than the
  three-hour point estimate.

Approximate allocation was 7 minutes reading/fixing the frozen scientific
authority, 24 minutes implementation/debugging/documentation, and 20 minutes
program execution or waiting. The execution category includes the 515-second
audit cache, qualification/analysis, the interrupted direct run, and its
crash-resumable successful replay; categories are rounded.
