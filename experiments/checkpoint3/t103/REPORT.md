# T103 — H098-D terminal P1 adjudication

## Outcome

`H098-D` passed the prospectively frozen historical M1 screen, was registered
as `ALG017-V000`, and passed F0, F1, F2, F3A, and F3B. Its terminal status is
**P1-promising**. The result is a scientific pass, not a strict-gate waiver or
an operational exception.

This does **not** replace `ALG015-V000` as the project submission candidate.
T103 used historical width-256/depth-32 native-proxy evidence; `ALG015-V000`
is the best officially graded width-1024/depth-16 Phase-2 package. The two
scores are not directly comparable under the owner's succession rule.

## Frozen identity and evidence integrity

The pre-outcome seal fixed five independent 512-by-256 equal-weight Haar-
Stiefel frames with antithetic paths, order-12 density-weighted Price/Hermite
full-covariance closure, a per-layer affine span of the constant vector and
that closure, and half-strength positive-part James--Stein shrinkage of only
the residual orthogonal to that span. It also fixed constant-only, leading-
noise-mode-protection, and trace-guard ablations.

Rows 56--67 were selected as the next contiguous historical cohort after
T097 and were not accessed for exact H098-D accuracy before the source, rules,
controls, costs, and outcome probabilities were sealed. This evidence is fresh
for the exact candidate, but not globally target-sealed: earlier public-
leaderboard positive-control work had materialized rows 46--91. That overlap
is disclosed rather than treated as fully blind confirmation.

The first Windows invocation failed before Python because `cmd.exe` rejected
the UNC working-directory quoting. No candidate output was produced. The
sources were staged byte-identically to a Windows temporary directory and the
unchanged run then completed normally. A same-bundle WSL replay of F1 was
internally deterministic and reached the same disposition; cross-platform QR/
BLAS differences changed the pooled candidate/control ratio by only
`3.02e-6`. Substantive findings still require later reproduction on an
independently stable machine or VM.

## Historical M1 and ablations

| Arm versus five-frame carrier | Pooled adjusted ratio | Wins | Median | Maximum | Interpretation |
|---|---:|---:|---:|---:|---|
| primary H098-D | `0.905795` | 10/12 | `0.885050` | `1.011003` | all M1 gates pass |
| constant-only | `1.000051` | 5/12 | `1.000289` | `1.001173` | essentially neutral |
| top-noise protection | `0.918073` | 9/12 | `0.879538` | `1.067127` | favorable, weaker aggregate/tail |
| trace guard | `0.980384` | 10/12 | `0.986452` | `1.00000000007` | safest tail, much smaller gain |

The primary also scored `0.905748` relative to the constant-only arm with
10/12 wins. Thus the useful direction is not explained by generic shrinkage
toward a constant: the fixed Hermite-closure component is empirically
material. The primary factor ranged from zero through `0.907394`; the sampled
leading covariance-trace fraction ranged from `0.273295` to `0.673682`, so the
earlier anisotropy concern was real. The unguarded primary nevertheless won
the frozen aggregate, breadth, and tail test. Its exact historical cost was
`23,840,966,267` FLOPs, retained the `0.1` multiplier, and left
`3,359,033,733` FLOPs below the score-floor boundary.

## Complete F0--F3 funnel

| Stage | Candidate/control pooled ratio | Wins | Maximum | Disposition |
|---|---:|---:|---:|---|
| F0 | — | — | — | PASS: contract, budget, target independence, replay preflight |
| F1 | `0.940183` | 1/2 | `1.007846` | PASS, exact byte/FLOP replay |
| F2 | `0.951256` | 8/12 | `1.188583` | PASS |
| F3A | `0.934230` | 13/16 | `1.070118` | PASS |
| F3B | `0.954514` | 11/16 | `1.158732` | PASS |

Across the two F3 lanes, the candidate's pooled adjusted proxy was
`4.200670913e-7` versus `4.447702833e-7` for its exact mechanism control:
ratio `0.944459`, a `5.554%` reduction and absolute effect `2.4703192e-8`.
It won 24/32 networks; median, p95, and maximum paired ratios were `0.932094`,
`1.090611`, and `1.158732`. The context-only candidate/incumbent pooled ratio
was `0.726672`; that incumbent comparison was not a P1 veto.

## Human promotion audit

| Gate | Frozen requirement | Observation | Margin / status |
|---|---:|---:|---|
| historical M1 pooled | `<= 0.99` | `0.905795` | PASS by `0.084205` |
| historical M1 breadth | `>= 7/12` | `10/12` | PASS by 3 wins |
| historical M1 maximum | `< 2` | `1.011003` | PASS by `0.988997` |
| F3A mechanism ratio | `<= 1.05` | `0.934230` | PASS by `0.115770` |
| F3B mechanism ratio | `<= 1.05` | `0.954514` | PASS by `0.095486` |
| pooled F3 mechanism ratio | `< 1` | `0.944459` | PASS by `0.055541` |
| pooled bootstrap upper 90% | `< 1.10` | `0.966411` | PASS by `0.133589` |
| maximum F3 ratio | `< 4` | `1.158732` | PASS by `2.841268` |

- Subject/evidence: `ALG017-V000`, N1/dimension 3, fresh-for-candidate
  historical M1 plus complete registered FC006/E0006 F0--F3 evidence.
- Current and highest supported tier: **P1-promising**; M1 and P1 awarded.
- Next tier considered: R1, but it was not run because it requires a separate
  prospectively frozen rigorous cycle.
- Primary blocker class: `PROMOTED`. No strict or scientific gate blocked P1.
- Why not promoted further: T103 did not contain R1/P2 evidence; absence of a
  higher tier is evidence-incomplete, not a rejection.
- Immediate high-impact route: complete the independent T104 decision, then
  T105 adjudicates FC006 and routes its newly nonempty P1 pool to T099.
- Owner action required: none.

## Prior calibration and surprise

The terminal P1 prior was frozen at `.45`; observing P1 therefore carries
`-log2(.45) = 1.152003` bits. This is favorable and mildly surprising, but P1
was already the single most likely frozen outcome. The earlier theoretical
concern about covariance concentration was borne out in the measured trace
fractions, while its predicted harm did not overcome the candidate's pooled
benefit. That makes the positive result credible enough for P1, not a claim of
isotropic universal dominance.

## Route

T104 remains next. It independently tests H098-A with nested H098-B on fresh
current-shape evidence and can establish submission succession because it is
directly compared with `ALG015-V000`. No external upload is authorized by
T103.

Timing: start `2026-08-26T19:30:11,458270246-07:00`; estimate `50 minutes`;
end/checkoff `2026-08-26T20:08:30,155540662-07:00`; elapsed
`00:38:18.697270416` (`2298697270416` ns).
