# T117 — Full-1000 nested audit-free observer decision

## Outcome

**`ALG024-V000` / AS is the new local project-best submission candidate.**
On untouched Full V_O rows 650--749 it achieved adjusted score
`1.760428242828e-7` versus `2.490222720778e-7` for `ALG019-V000`, ratio
`0.706936062`, a `29.3064%` reduction. It won `100/100` paired networks;
the maximum network ratio was `.835049`, bootstrap `P(win)=1`, and the 90%
network-bootstrap ratio interval was `[.699597,.714704]`.

This is strong current-Phase-2 competition evidence and awards current-shape
M1. It is not an official grade, historical P1, or final rigorous scientific
designation. The exact N1/dimension-4 `OURS+PUBLIC` combination is registered
as `ALG024-V000`, and its Windows-native contract-valid archive is ready but
was **not uploaded** because T117 contains no owner authorization to upload.
`ALG019-V000` submission `328762` remains the official project best until a
future explicitly authorized upload is graded.

## Prospective data discipline

The official `aicrowd/arc-whestbench-public-2026` Full split was pinned to
commit `ce926b7d1ced65faa668c01b94a43f8c4f43783d`. All 63 available shards
(`69,955,020,892` bytes, 1,000 rows; filenames retain the upstream stale
`of-00067` suffix) were downloaded Windows-native and SHA-256 hashed before
target access.

Every feature for all 1,000 networks was then generated from only
`mlp_id`, `mlp_name`, `mlp_seed`, and `weights`. The complete 26-feature cache
was hash-sealed before F targets were opened. The chronological order was:

1. seal all 1,000 weights-only feature rows;
2. open F 0--499, fit all rung/ridge alternatives, and seal all S predictions;
3. open S_O 500--649 and choose one rung;
4. regenerate, meter, and seal that one candidate on V_O 650--749;
5. open V_O once and score the terminal comparison.

V_D 750--849 and H 850--999 targets remain logically untouched for T118.
The official Parquet files have one 16-row row group per shard, so boundary
shards had to be decoded as physical units. `open_panel_targets.py` copied and
exposed only the named logical rows and recorded every physical edge spill;
no downstream artifact contains V_D or H targets.

## Feature and implementation qualification

The frozen grammar passed Windows-native finite output, deterministic replay,
parent and discovery-feature parity, power-of-two homogeneity, output
permutation equivariance, quarter-carrier-RMS cap, and nonnegative final
projection checks. Cross-BLAS SF differences were bounded explicitly:

| Check | Result |
|---|---:|
| full feature count | `26` |
| deterministic replay | exact |
| ALG019 parent parity | exact |
| GL maximum parity error | `3.47e-18` |
| SF maximum / RMS-relative parity error | `2.146e-6` / `8.908e-4` |
| maximum permutation-equivariance error | `5.245e-6` |
| full-M feature FLOPs | `219,877,263,001` |
| headroom below `.1` floor | `25,062,554` FLOPs |
| residual wall time | `.341 s` on the qualification row |

The all-1,000 run consumed 3,417.312 aggregate outer estimator seconds. Every
row had the identical `219,877,263,001`-FLOP receipt and published atomically
with feature/origin hashes.

The first selected-V attempt found one inherited earlier-layer value of
`-4.331092e-17`; the selected final layer was already nonnegative and matched
the sealed cache within `1.128e-7`. Before V targets, the output assembly was
repaired to apply the same zero clamp to all 16 layers. Selection,
coefficients, and selected final-layer bytes did not change. The transparent
old/new source hashes and failed row are in `POSTSELECTION_CONTRACT_REPAIR.json`.
The repaired 100/100 run passed at `219,827,350,403` FLOPs, `.1` multiplier,
and maximum `.314 s` residual time.

The durable package independently passed `whest validate`, full-shape replay,
byte-exact parity with sealed row 650, deterministic/cost replay, archive
content inspection, clean-directory extracted-archive replay, and
`whest validate-package`. The audit caught and replaced an initial manifest-
valid but dependency-incomplete single-file archive before completion. Final
archive SHA-256 is
`aa55acb9c2af9c9041a60c04390c30a3b34e32d78fa0fa6bced40101fe444ba2`.

## F fitting

For each rung, five whole-network folds selected among the fixed normalized
ridge grid. In every case lambda `1e-4` had the lowest point risk, but
`1e-3` was within the fixed `2e-9` tie band and therefore won the mandated
larger-lambda tie break. Lambda `1e-2` was outside the band. All 18 results
are shown rather than hiding ridge sensitivity:

| Rung | `1e-4` | `1e-3` | `1e-2` | selected |
|---|---:|---:|---:|---:|
| BO | `2.060883343e-6` | `2.061068102e-6` | `2.062927232e-6` | `1e-3` |
| GL | `1.992413925e-6` | `1.992901870e-6` | `1.997845758e-6` | `1e-3` |
| SF | `1.945796062e-6` | `1.946276174e-6` | `1.951151469e-6` | `1e-3` |
| AS | `1.752713677e-6` | `1.754026476e-6` | `1.762763559e-6` | `1e-3` |
| DS | `1.749457632e-6` | `1.750726955e-6` | `1.759027910e-6` | `1e-3` |
| M | `1.741694958e-6` | `1.742982829e-6` | `1.751619301e-6` | `1e-3` |

Every individual fold also point-preferred `1e-4`; the pooled `1e-3` choices
are therefore deliberate tie-rule shrinkage, not hidden fold instability.

## S_O nested selection

S_O incumbent raw MSE was `2.508006768e-6`. Every rung beat the incumbent on
all 150 networks. The final two rungs had the lowest point estimates but did
not become eligible under the prospectively frozen sequential complexity
margin.

| Rung | raw MSE | ratio to ALG019 | wins | max ratio |
|---|---:|---:|---:|---:|
| BO | `2.075853374e-6` | `.827690` | `150/150` | `.974006` |
| GL | `2.010132024e-6` | `.801486` | `150/150` | `.920711` |
| SF | `1.964406343e-6` | `.783254` | `150/150` | `.897949` |
| **AS** | `1.766009462e-6` | `.704149` | `150/150` | `.837823` |
| DS | `1.761641530e-6` | `.702407` | `150/150` | `.848002` |
| M | `1.754334658e-6` | `.699494` | `150/150` | `.844757` |

| Increment | raw-MSE change | SE | favorable networks | disposition | surprise |
|---|---:|---:|---:|---|---|
| BO -> GL | `-6.572135014e-8` | `5.842e-9` | `121/150` | PASS | `.862` bits, unsurprising |
| GL -> SF | `-4.572568049e-8` | `3.703e-9` | `134/150` | PASS | `.862` bits, unsurprising |
| SF -> AS | `-1.983968813e-7` | `4.509e-9` | `150/150` | PASS | `1.152` bits, mildly surprising favorable |
| AS -> DS | `-4.367931313e-9` | `2.167e-9` | `81/150` | FAIL-STRICT-GATE | `1.059` bits, mildly surprising miss |
| DS -> M | `-7.306872632e-9` | `5.359e-10` | `132/150` | NOT-APPLICABLE after DS stop | `.862` bits, unsurprising miss |

DS is favorable, not scientifically negative; it missed the `2e-8` increment
by `1.5632e-8` and is strict-rule-limited. M is also favorable and has the
best S point estimate, but the frozen sequential rule made it selection-
ineligible after DS stopped. These are exactly the kinds of promising strict-
gate cases the owner asked to keep visible. AS is the lawful selected identity.

## Untouched V_O result

| Quantity | `ALG024-V000` | `ALG019-V000` | ratio / difference |
|---|---:|---:|---:|
| raw final-layer MSE | `1.760428243e-6` | `2.490222721e-6` | `.706936062` |
| adjusted score | `1.760428243e-7` | `2.490222721e-7` | `.706936062` |
| paired wins | `100/100` | — | — |
| adjusted change | — | — | `-7.297944779e-8` |
| median / p90 / maximum ratio | — | — | `.702539 / .780966 / .835049` |
| bootstrap 90% ratio interval | — | — | `[.699597,.714704]` |
| bootstrap `P(win)` | — | — | `1.000000` |

The candidate improves the `1<|alpha|<=3` and `|alpha|>3` regions at ratios
`.839368` and `.605606`; the `|alpha|<=1` region is nearly neutral/slightly
adverse at `1.005775`. Cap/clamp incidence was `2,238/22,134` of 102,400
coordinates. The win and at-least-10%-gain events were both unsurprising
under frozen priors (`.322` and `.737` bits).

## Human promotion and submission disposition

| Subject | Highest supported status | Why not further / submitted now | Blocker | Strict gate sole? | Immediate action |
|---|---|---|---|---|---|
| `ALG024-V000` AS | **new local submission candidate; current-shape M1; N1/dim-4; package-ready** | no official grade, historical P1, final H result, or owner upload authorization | `EVIDENCE_INCOMPLETE` for rigorous tier; authorization absent for upload | No | T118 tests frame/composition on V_D and then one H opening; owner may separately authorize upload |
| DS increment | S point-favorable, `-.004368e-6` beyond AS | improvement did not reach frozen `2e-8` complexity margin | `STRICT_GATE_LIMITED` | **Yes** | Preserve for a future owner override or recurrence; do not call it rejected |
| M increment | best S point estimate, favorable beyond DS | sequential ladder stopped at DS, so M could not be selected or tested on V | `STRICT_GATE_LIMITED` / `EVIDENCE_INCOMPLETE` | **Yes for T117 V access** | Keep visible; no post-outcome substitution in T117 |
| `ALG019-V000` | official project best, submission `328762` | loses local Full V_O comparison but remains officially graded incumbent | official grade not superseded yet | Not applicable | Use ALG024 as T118 local incumbent; no upload without authorization |

## Next task

T118 executes H116-B starting from `ALG024-V000`/AS, proves the exact-fast
frame path, fits the frozen child/composition on F, uses still-untouched V_D
for its nested decision, and opens H once for final head-to-head. No T117
upload occurred.

**Post-task queue amendment:** the owner's prospective immediate-submission
rule inserts T117A before T118. T117A revalidates, uploads, and monitors the
exact frozen ALG024 archive when explicitly instructed; T118 remains the next
scientific task. This amendment changes only task order, not E102 evidence or
the sealed V_D/H panels.

## Timing and work allocation

- Start: `2026-09-01T19:36:39,905009488-07:00`
- Pre-task estimate: **7 hours wall-clock** (planning range `4--10 hours`)
- End/checkoff: `2026-09-01T21:31:23,608409734-07:00`
- Actual wall time: `01:54:43.703400246` (`6883703400246` ns)
- Estimate difference: completed `05:05:16.296599754` earlier than the
  seven-hour point estimate.

Approximate allocation was 12 minutes protocol/result analysis, 27 minutes
implementation/debugging/documentation/package repair, and 76 minutes program
execution/network transfer/hashing/waiting. The last category includes the
56m57s all-row feature compute and 4m52s selected-V compute; categories are
rounded and overlap very small orchestration intervals.
