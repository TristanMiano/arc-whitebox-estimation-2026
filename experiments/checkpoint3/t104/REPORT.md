# T104 — H098-A/H098-B current-shape decision

## Outcome

**`ALG018-V000` beat `ALG015-V000` and is the new local submission
candidate.** On the prospectively sealed Phase-2 rows 64--75, its pooled
adjusted score was `2.676436318e-7` versus `2.839371530e-7`, ratio
`0.942615748`: a 5.738% reduction. It won 11/12 networks, its median paired
ratio was `0.956767`, maximum `1.004055`, and report-only bootstrap upper90
was `0.961064`.

The nested mechanism also replicated. H098-B/`ALG018-V001` beat
`ALG015-V000` at `0.970217779`, 11/12 wins, maximum `1.005959`; adding the
independent partial-Haar arm improved H098-A/H098-B to `0.971550685`, 9/12,
maximum `1.042599`. Thus the primary gain is not solely inherited from the
order-12 closure.

| Arm | Exact FLOPs | Multiplier | Pooled raw MSE | Adjusted score |
|---|---:|---:|---:|---:|
| `ALG018-V000` / H098-A | 216,711,677,067 | 0.1 | `2.676436318e-6` | `2.676436318e-7` |
| `ALG018-V001` / H098-B | 197,054,218,379 | 0.1 | `2.754808740e-6` | `2.754808740e-7` |
| `ALG015-V000` | 196,459,652,235 | 0.1 | `2.839371530e-6` | `2.839371530e-7` |

All arms stay on the 0.1 multiplier. V000 retains `3.191B` FLOPs of score-
floor headroom, so the succession is not an artifact of unequal uncorrected
compute.

## Frozen gates and promotion

| Decision | Frozen rule | Observation | Margin | Status |
|---|---:|---:|---:|---|
| V000/V001 pooled effect | `<=0.99` | `0.971551` | 0.018449 favorable | PASS |
| V000/V001 breadth | `>=7/12` | `9/12` | +2 wins | PASS |
| V000/V001 maximum | `<4` | `1.042599` | 2.957401 favorable | PASS |
| V001/incumbent pooled effect | `<=0.99` | `0.970218` | 0.019782 favorable | PASS |
| V001/incumbent breadth | `>=7/12` | `11/12` | +4 wins | PASS |
| V001/incumbent maximum | `<4` | `1.005959` | 2.994041 favorable | PASS |
| V000 succession | `<1` | `0.942616` | 0.057384 favorable | PASS |

Both algorithms receive **current-shape M1**. No completed strict or
scientific gate failed. Historical P1, R1, and P2 are `NOT-RUN`; T104 was
explicitly a Phase-2 current-shape decision and did not execute a historical
adapter or F0--F3. Therefore the reason they are not P1 is evidence-class
incompleteness, not scientific rejection or an overly strict gate. A new,
prospectively sealed historical adapter and fast funnel would be the smallest
P1 unlock if T105 selects that investment. No owner action is required for
T105.

## Surprise

T098 froze H098-A succession probability at `.60` and H098-B at `.55`.
Observed succession therefore carries `0.736966` and `0.862496` bits,
respectively. These are favorable but expected outcomes; both were the largest
single frozen branch. The fresh partial-arm replication is useful positive
evidence, but not a surprise relative to the old-row mechanism screen.

## Integrity and defect audit

Before target access, the exact estimator hash, both exact costs, fallback,
incumbent hash, untouched shard and rows, gates, and original priors were
sealed. Target-blind checks passed the fixed formula, independent random
stream, order-12 recurrence, `abs(alpha)>12` zero guard, exact first layer,
finite shape, deterministic prediction/FLOPs, and low-budget fallback.

The first two `whest validate` attempts completed estimator loading but the CLI
failed while printing Unicode to a CP1252 console. Retrying under Windows
`cmd.exe` with `PYTHONIOENCODING=utf-8` passed every contract check; no
estimator failure occurred. A transient exact archive then passed
`validate-package`. No official upload occurred.

The complete WSL replay used the same source and 12 rows. FLOPs, win counts,
both M1 decisions, best arm, and succession were identical. Backend-dependent
floating-point differences changed V000/incumbent ratio by only `3.72e-5`
absolute and V000/V001 by `1.34e-6`, far below the favorable margins. This
makes a result-changing implementation/environment defect unlikely, though
later reproduction on an independent stable machine/VM remains required for
substantive scientific claims.

## Submission and route

`ALG018-V000` is the new **local** submission candidate and has estimator-
contract plus transient-package validation. It has no official score and the
full pre-upload hard-gate archive is not yet recorded. `ALG015-V000`, official
submission `328500`, remains the best officially graded project entry. No
upload was authorized or attempted in T104. T105 must now adjudicate FC006 and
route the nonempty historical P1 pool without waiting.

## Timing

Started `2026-08-27T11:08:29,911683527-07:00`; pre-outcome estimate
`55 minutes`; checked off `2026-08-27T11:35:06,860473683-07:00`; elapsed
`00:26:36.948790156` (`1596948790156` ns).
