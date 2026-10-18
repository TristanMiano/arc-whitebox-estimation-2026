# T105 — FC006 adjudication and route

## Decision

FC006 closes **positive**. `ALG017-V000` is a newly eligible historical
`P1-promising` candidate, so the T099 condition is satisfied and rigorous
Cycle 2 (`RC002`) is now active for prospective freeze. The RC002 slate is
singleton `ALG017-V000`; its exact mechanism control is `ALG017-V001`, and
the native contest incumbent is `ALG003-V008`. T099 must bind a native exact
realization, fresh blocks and seeds, pair-specific MDEs, deterministic replay,
fully charged failure routes, all R1/P2 gates, and familywise one-sided alpha
`.0125` before score access. RC001 blocks are forbidden.

`ALG014-V000` remains historical P1 but is excluded from RC002 because its
exact identity already completed RC001 and may not re-enter unchanged.
`ALG017-V002` is support-only current-shape M1. `ALG018-V000` and V001 remain
current-shape M1; they cannot enter RC002 by silently substituting Phase-2
succession evidence for historical F0--F3.

## Complete FC006 disposition

| Algorithm | Novelty | Exact cost | Strongest evidence and tails | Promotion | Surprise | Submission |
|---|---|---:|---|---|---|---|
| `ALG017-V000` / H098-D | N1, dimension 3 | 23.841B, multiplier 0.1 | F3 `0.944459`, upper90 `0.966411`, 24/32, p95 `1.090611`, max `1.158732` | historical M1 and **P1 awarded**; R1/P2 NOT-RUN | `.45`, `1.152003` bits; favorable/mildly surprising | historical shape, succession not comparable |
| `ALG017-V002` | N1, dimension 3 child | 776.207B, multiplier `0.352978` | carrier `0.603707`, 12/12, max `0.675744`; incumbent `1.505849`, 0/12, max `2.602969` | current-shape M1; no P1 transfer | no-succession `.90`, `0.152003` bits; expected | no succession; compute competitiveness only |
| `ALG018-V000` / H098-A | N1, dimension 3 | 216.712B, multiplier 0.1 | nested `0.971551`, 9/12, max `1.042599`; incumbent `0.942616`, 11/12, max `1.004055` | current-shape M1; historical P1 NOT-RUN | succession `.60`, `0.736966` bits; expected | **current local candidate**; not uploaded |
| `ALG018-V001` / H098-B | N1, dimension 2 | 197.054B, multiplier 0.1 | incumbent `0.970218`, 11/12, max `1.005959` | current-shape M1; historical P1 NOT-RUN | succession `.55`, `0.862496` bits; expected | lawful successor if primary absent, but V000 scores lower |

No FC006 algorithm was scientifically rejected. No strict gate was the sole
blocker for any retained promotion. The two `NOT-RUN` historical P1 statuses
are evidence-incomplete, not negatives. T103A's submission loss is a genuine
compute-competitiveness result for that child only and does not erase its
current-shape mechanism signal or its parent's historical P1.

## Promotion transparency

- `ALG017-V000`: blocker class `PROMOTED` through P1. R1/P2 are `NOT-RUN`
  solely because a separately frozen rigorous cycle has not executed. The
  immediate agent-side unlock is T099, then T100/T101.
- `ALG018-V000`: blocker class `EVIDENCE_INCOMPLETE` for historical P1. Every
  T104 current-shape gate passed; a prospectively sealed historical adapter
  and F0--F3 would be needed for P1. This does not block submission use.
- `ALG018-V001`: same evidence-class limitation; it is not rejected merely
  because it served as the nested control, but V000 is the lower-score local
  candidate.
- `ALG014-V000`: historical P1 is preserved. RC001's strict-tail-limited R1
  denial and broader P2 scientific negative remain binding; exact unchanged
  re-entry is prohibited.

T105 itself opens no candidate outcome, changes no tier, and changes no
submission candidate. `ALG018-V000` remains local best; `ALG015-V000`
submission `328500` remains best officially graded. No upload occurred and no
owner action is required.

## Timing

Start: `2026-08-27T12:12:02,962606180-07:00`. Pre-outcome estimate:
`30 minutes`. Final TODO checkoff: `2026-08-27T12:19:59,519169339-07:00`. Elapsed:
`00:07:56.556563159` (`476556563159` ns).
