# T108 — frozen FC007 competition screen

## Outcome

**ALG019-V000 / H107-O beat `ALG018-V000` and is the new local Phase-2
submission candidate.** On the prospectively sealed Phase-2 mini rows 76--87,
its adjusted score was `2.4508671800218226e-7` versus the incumbent's
`2.7872975808683986e-7`: pooled ratio `0.8792987145844114`, 12/12 paired wins,
and maximum paired ratio `.959225`. The bootstrap ratio upper-95 was `.900573`.

All five ALG019 arms beat the incumbent under the predeclared direct rule.
Because every complete route stayed on the `.1` floor, adjusted and raw-MSE
ordering are identical.

| Rank | Algorithm / hypothesis | Adjusted score | Ratio to ALG018 | Wins | Max paired | Bootstrap upper-95 | Submission disposition |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | **ALG019-V000 / H107-O** | **`2.4508672e-7`** | **`.879299`** | **12/12** | `.959225` | `.900573` | **new local candidate** |
| 2 | ALG019-V002 / H107-N | `2.4918891e-7` | `.894016` | 12/12 | `.971810` | `.914560` | valid winner, superseded by V000 |
| 3 | ALG019-V003 / H107-J | `2.5982339e-7` | `.932170` | 11/12 | `1.018087` | `.953464` | valid winner, superseded by V000 |
| 4 | ALG019-V001 / H107-I | `2.6016318e-7` | `.933389` | 11/12 | `1.020589` | `.954696` | valid winner, superseded by V000 |
| 5 | ALG019-V004 / H107-F | `2.7555678e-7` | `.988616` | 7/12 | `1.015420` | `.997378` | marginal valid winner, superseded by V000 |
| 6 | ALG018-V000 | `2.7872976e-7` | `1.000000` | — | — | — | former local/official incumbent |

The official ALG018 score (`2.6931472416436013e-7`, submission 328686) is from
a different grader cohort. V000's T108 number is also lower than that value,
but only an official upload can establish the official head-to-head ranking.
No upload occurred in T108.

## Qualification and seal

Before `final_means` were read, ALG019-V000--V004 were registered and their
common source was frozen at SHA-256 `74879a41...6efec6`. Independent checks
passed for stable float64 moments, direct beta/rho/harmonic references,
pair-preserving halves, translation/positive-scale/permutation/half-swap
invariants, exact Q0 prediction parity with ALG018, Q0/Q1 orthogonality,
closure byte parity, exact band weights, last-ReLU tensor identity, layers
1--15, exact layer 1, fallback, shape, and finiteness.

Windows-native FlopScope 0.12 / WhestBench 0.16 measured each production route
twice. The cost-maximal O/N route used `219,788,985,209` FLOPs, leaving
`113,340,346.2` below the `.1` boundary; therefore the frozen cost rule kept
all 332 partial rows. Maximum residual time was `.194881s` against the `.4s`
cap, maximum wall time `2.588052s`, and maximum process peak working set
`311,115,776` bytes. All five contract and archive validators passed.

The protected-input generator loaded only `mlp_id`, name, seed, and weights.
It sealed `PREDICTIONS.npz` at SHA-256 `0e91146b...22027` before the separate,
already-hashed scorer loaded `final_means` once. No source, rows, weights,
precision, thresholds, or formulas changed after target access.

## Nested mechanism results

Every predeclared nested comparison had the anticipated sign:

| Mechanism comparison | Pooled ratio | Wins | Prior | Surprise / belief update |
|---|---:|---:|---:|---|
| O harmonic shrink vs N | `.983538` | 12/12 | `.96` O win | Expected; consistent target-blind reliability removed repeatable skew noise. |
| N terminal skew vs J | `.959070` | 12/12 | `.94` N win | Expected; the effect was somewhat stronger than the already-favorable prior forecast. |
| I coarse alpha split vs F | `.944136` | 11/12 | `.82` I win | Expected and clearly positive; the simple conditional covariance rule transferred. |
| J three-band split vs F | `.942903` | 11/12 | `.80` J win | Expected in sign, favorably larger than the anticipated basis-point refinement. |

O's incumbent win had prior `.95`, so the direction is not surprising. Its
`.8793` ratio is better than the conservative `.91` forecast and is mildly
favorable in magnitude. I's `.9334` ratio is also expected and close to its
`.945` forecast. F's very narrow `.9886` win is compatible with its `.72`
prior and confirms that the large complete-family gain is not attributable
only to partial-row headroom.

Target-blind O diagnostics were stable across all 12 networks: beta ranged
`.02943--.03732` (mean `.03316`, near `1/sqrt(1024)`), rho ranged
`.22663--.51562` (mean `.41586`), closure/frame median-sigma ratio ranged
`.98698--.99082`, and no full-skew coordinate hit the `[-1,1]` clip.

## Component evidence

Raw pooled final-layer component risks were:

| Component / report-only arm | Raw MSE | Ratio to ALG018 raw MSE |
|---|---:|---:|
| retune-only, 288 partial rows | `2.7368101e-6` | `.981887` |
| extension-only, incumbent weights | `2.8009938e-6` | `1.004914` |
| closure | `3.9927502e-6` | `1.432481` |
| frame | `9.9546007e-6` | `3.571417` |
| partial-332 | `8.9697876e-5` | `32.180947` |
| partial-288 | `1.0215197e-4` | `36.649108` |
| isolated 44-row extension | `7.5019972e-4` | `269.149487` |

The retune alone transfers, while adding the extension under incumbent weights
does not. Partial-332 has lower standalone variance than partial-288, but its
closure residual inner product changed from `-2.17e-7` to `+5.43e-7`; that
adverse covariance explains why row-count headroom is not a free complete-
estimator gain. H107-F still narrowly beats ALG018 because its retuned weights
and extension act jointly. The much larger O/N/J/I gains come from conditional
fusion and terminal-shape corrections, not merely extra samples.

## Disposition

- `ALG019-V000` receives current-shape M1 mechanism signal and local submission
  succession. It has not undergone historical P1/F0--F3 or final rigorous
  science; current policy defers that work until it is decision-relevant.
- V001--V004 also pass the direct incumbent screen and provide positive nested
  mechanism evidence, but are competitively dominated on this same frozen
  cohort by V000. They are not scientific rejections.
- No unchanged ALG019 branch had ratio `>=1`, so the immediate-negation rule
  closed none for incumbent noncompetitiveness. Lower-scoring V000 nevertheless
  becomes the only active upload priority.
- `ALG018-V000` remains the officially graded best until a separately
  authorized upload succeeds. T108 does not authorize or perform that upload.
- Later reproduction on an independent stable machine/VM remains required.
  The next high-leverage research step is FC008 theory generation/target-blind
  qualification against the stronger ALG019 incumbent, unless the owner first
  authorizes an ALG019-V000 upload.

## Timing

- Start: `2026-08-27T21:35:08,576480698-07:00`
- Estimate: `55 minutes` (plausible range `35--85 minutes`)
- Checkoff: `2026-08-27T22:55:46,027482483-07:00`
- Actual wall time: `01:20:37.451001785` (`4837451001785` ns)
