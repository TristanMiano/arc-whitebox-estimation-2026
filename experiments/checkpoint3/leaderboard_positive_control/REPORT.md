# D001 — Phase 1 leaderboard positive-control battery

## Decision

The disclosed leaderboard candidate **does not pass the project's frozen P1
funnel**. It passes F0, earns M1 at F1, passes the 12-network F2 sentinel, and
has an excellent F3A aggregate. It is nevertheless rejected at F3A because
one of 16 routes crosses the separate `>=1.25` unexplained-tail boundary.
F3B was correctly not opened, so P1 is not awarded.

This is a `FAIL-STRICT-GATE` positive-control failure, not a broad scientific
rejection. The sole completed-tier blocker is one candidate/control ratio of
`1.4109020940`. It passes the nominal maximum-ratio rule (`<1.5`) by
`0.0890979060`, but fails the stricter unexplained-tail rule (`<1.25`) by
`0.1609020940`. F3A otherwise has candidate/control ratio `0.3600480349`,
`15/16` wins, candidate/incumbent ratio `0.3530018997`, and an absolute mean
adjusted-score advantage of `1.9934596842e-7`, more than 456 times the frozen
T014 screening floor.

Across every opened empirical route (F1, F2, and F3A), the candidate wins
`29/30` against its mechanism control and `28/30` against the incumbent; the
pooled ratios are `0.3824796225` and `0.3796487606`, respectively. Those
cross-tier aggregates are context only because the funnel stops and decides
by tier.

## Why this leaderboard entry

The final Phase 1 board is led by entries for which a complete reproducible
estimator was not found during this bounded audit. The highest detailed public
write-up found was rank-12 Team Puffi, but its A716 control uses 90 frozen
fitted coefficients that the public PDF does not enumerate, so an exact
implementation would require inventing material behavior. Ranks 13 and 14
likewise did not yield a complete released artifact in the audit.

The selected candidate is kaileh57 submission `327786`, rank 15 on the final
board with adjusted score `9.686489982715155e-08` and raw final-layer MSE
`2.0883231030666138e-07`. Its author released source, retained upload,
receipts, proofs, and a hash manifest. The release archive SHA-256 is
`956ca7e40b35e5bc4a52ae1949d2f3f18eeffe94ae6261eaa6c3034ffe3dac38`;
the exact estimator SHA-256 is
`b5418459c4c0cce62129027affb15170cc5aca477ff0af6c5590d718bc9947ed`.
The retained upload validates under WhestBench 0.14.0.

Sources:

- [Final AIcrowd Phase 1 leaderboard](https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/leaderboards)
- [Phase 1 technique census and disclosure update](https://discourse.aicrowd.com/t/a-technique-census-of-phase-1-what-the-mathematics-is-doing-what-walls-it-hit-and-whats-still-open/18157)
- [Selected submission write-up](https://discourse.aicrowd.com/t/phase-1-writeup-fixed-positive-sampling-is-nearly-saturated-submission-327786/18171)
- [Selected exact source/reproduction release](https://github.com/kaileh57/whitebox-phase1-327786/releases/tag/phase1-327786)
- [Team Puffi write-up used in the reproducibility comparison](https://discourse.aicrowd.com/t/phase-1-write-ups-team-puffi/18175)

## Exact candidate and comparison translation

The candidate arm executes the released Python source itself in the exact
Python 3.10.20 / NumPy 2.2.6 / WhestBench 0.14.0 / FlopScope 0.10.0 dependency
versions named by the release. There is no native or prose reimplementation.
Its algorithm uses a randomly rotated 66,048-point complete real-MUB rule and
data-dependent exact-zero pruning plus Strassen variants.

The project funnel ordinarily requires fixed modeled compute. The published
source has route-varying billed work and host-dependent residual time, so the
predeclaration conservatively freezes its screening projection to the rounded
released eight-network Stage B mean effective compute, `155917223329`. The
selected mechanism control is the project's canonical dense spherical Sobol
route at 18,550 positive points and `155912601600` modeled FLOPs. It is the
largest predeclared integer prefix below the candidate and differs by only
`0.00296422%`, versus the frozen maximum of 3%. The mandatory incumbent context
is exact `ALG003-V008` at `262549156608` modeled FLOPs.

All local actual compute is also retained. Candidate billed FLOPs ranged from
`113469706003` to `142871479069`, effective compute from
`122617592409.94` to `152329731562.64`, and no route exhausted a budget or
time limit. The fixed projection is thus conservative over every opened local
route. It remains a calibration translation, not a private-grader compute
reproduction.

The evidence schedule excluded the materialized row used for the initial
runtime trial. F1 used materialized exploration rows 46–47, F2 rows 48–59,
F3A rows 60–75, and the unopened F3B was frozen as rows 76–91. Every route uses
the official public one-billion-sample target. `EVIDENCE_PLAN.json` fixes the
source-row identities, controls, thresholds, compute, and stop rules.

## Gate results

| Tier / gate | Frozen requirement | Observation | Status |
|---|---:|---:|---|
| F0 release/archive manifest | exact hashes; all entries pass | outer/source/upload hashes exact; release manifest clean | PASS |
| F0 official package/API | validators pass | candidate package and all three estimator validators pass | PASS |
| F0 budget/reserve | `<272B`, no route failure | fixed `155.917B`; actual max effective `152.330B`; 0 failures | PASS |
| F0 comparator parity | control `<=` candidate, delta `<=3%` | `155.9126016B`; `0.00296422%` | PASS |
| F1 replay | exact scientific projection for 3 arms x 2 routes | `6/6` exact | PASS |
| F1 M1 signal | `>=0.01` on two routes | `0.70505715`, `0.27747821` | PASS — M1 |
| F1 candidate/control aggregate | contextual | `0.47929889`, `2/2` wins, max `0.72252179` | PASS |
| F2 aggregate | reject only if `>1.05` | `0.39605185`, `12/12` wins | PASS |
| F2 max / unexplained tails | reject at `>=1.5`; zero `>=1.25` | max `0.88013696`; zero tails | PASS |
| F3A aggregate | `<1.0` | `0.36004803`, `15/16` wins | PASS |
| F3A maximum | `<1.5` | `1.41090209` | PASS |
| F3A unexplained tails | zero ratios `>=1.25` | one (`1.41090209`) | **FAIL-STRICT-GATE** |
| F3B | only after clean F3A | `NOT-RUN` | NOT-RUN |
| pooled F3 / bootstrap / final MDE | complete F3 required | `NOT-RUN` | NOT-RUN |
| P1 | every F0–F3 gate | no | NOT-AWARDED |

The failing route is F3A order 13, public network `shane-long`. Candidate,
mechanism-control, and incumbent adjusted scores are respectively
`1.3215417637e-7`, `9.3666440023e-8`, and `1.1714176372e-7`. The candidate is
`1.4109020940x` the mechanism control and `1.1281559383x` the incumbent on
that network. Thus the outlier is real in the frozen comparison, even though
it is isolated and far too small to reverse the aggregate.

## Infrastructure attempts and reproducibility

The initial F1 command stopped before estimator import because the first
materialized subset was honestly marked `is_partial=true`; Whest requires
partials to be merged. Amendment 001 changed only that metadata flag to make
each frozen tier directory a complete standalone split. No scientific output
had been opened.

After the primary F1 pass, the first candidate replay stopped inside frozen
CPython import locking with `TypeError: 'int' object is not callable` followed
by an `UnboundLocalError`. It produced no Whest JSON. The failure is preserved
under `attempts/intermittent_import_002`; the exact retry succeeded, as did
both other arm replays. This follows the owner's retry-first containment rule
and required no owner action. No later execution failed.

The accepted reports contain 30 primary paired routes plus six F1 replay
projections. The exact released artifact and MIT license are retained under
`upstream/`. Recompute the decision and verify retained hashes with:

```bash
bash experiments/checkpoint3/leaderboard_positive_control/verify_evidence.sh
```

## Human promotion disposition

- Subject/evidence: public `LB001-V001` / AIcrowd Phase 1 submission 327786,
  exact released source, public one-billion-target C0-like calibration.
- Provenance/novelty: `PUBLIC`; not ours; no project academic-novelty claim.
- Current/highest/next tier: M1 earned; F3A reached; P1 considered and not
  awarded. F3B is the next empirical tier only after a prospective owner-
  reviewed gate decision.
- Strongest favorable evidence: F1 `0.479299`, F2 `0.396052`, F3A `0.360048`;
  29/30 total mechanism-control wins; strong incumbent context.
- Gate-by-gate status: F0 PASS, F1/M1 PASS, F2 PASS, F3A half ratio PASS,
  F3A maximum PASS, F3A zero-unexplained-tail gate FAIL, F3B/final pooled
  bootstrap/MDE NOT-RUN.
- Primary blocker: `F3A_UNEXPLAINED_TAIL_COUNT_NONZERO`.
- Strict gate sole blocker: **Yes, among every completed gate.** The exact miss
  is `1.4109020940 - 1.25 = 0.1609020940`; only one route is affected.
- Why not promoted: the frozen rule separately forbids any ratio `>=1.25`,
  even though the same funnel's nominal maximum gate permits ratios below
  `1.5` and all aggregate evidence is strongly favorable.
- Immediate high-impact owner review: prospectively remove the redundant
  `1.25` zero-tail veto, raise it to the existing `<1.5` maximum boundary, or
  replace it with a predeclared frequency/uncertainty-aware rule calibrated on
  disclosed leaderboard methods. Any change must be explicit and prospective;
  it would authorize F3B, not retroactively award P1.
- Project pool effect: none. This external calibration identity is excluded
  from the project-authored P1 pool and rigorous slate.

## Interpretation

The detour did not validate the funnel as a positive-control discriminator.
It instead found that the separate `1.25` zero-tail rule rejects a strongly
performing, fully disclosed leaderboard method while the method passes the
general `<1.5` tail rule and dominates aggregate/control/incumbent evidence.
That does not logically prove the `1.25` rule is always wrong, but it is direct
evidence that the rule is capable of a consequential false negative. The
human-readable blocker and smallest prospective unlock are recorded so this
calibration result can inform T090 and any owner decision without silently
weakening prior candidate gates.

## Task timing

- Start: `2026-08-22T17:58:52,333582854-07:00`
- Pre-task estimate: `60 minutes`
- End/check-off: `2026-08-22T18:40:26,832843502-07:00`
- Actual wall-clock difference: `00:41:34.499260648`
  (`2494499260648` ns)
