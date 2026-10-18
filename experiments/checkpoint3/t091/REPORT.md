# T091 — leverage-exact Haar–Stiefel adjudication

## Decision

`H090-B` earned M1 and retained its provisional N2 novelty classification, but
`ALG014-V001` is **not P1-promising**. Its complete candidate was narrowly but
scientifically worse than the otherwise identical equal-weight Haar–Stiefel
ablation on the pooled fresh F3 networks: `1.00884227` versus the required
`<1.0`. This is a `0.8842%` adverse direction, not a failure of an arbitrary
significance or tail gate.

The rejection is specifically about the exact leverage weights. Collective
Haar–Stiefel sampling remains unusually promising: the leverage candidate
beat the incumbent by `22.53%`, and its equal-weight ablation beat the
incumbent by `23.21%` on the same 32-network local adjusted-score proxy. These
are development proxies, not official scores or rank claims.

## Gate audit

| Gate | Observation | Threshold | Status |
|---|---:|---:|---|
| Construction/source/replay | all exact checks; Windows replay byte exact | all pass | PASS |
| M1 candidate / equal-work iid | `0.437314` | `<=0.99` | PASS |
| M1 wins | `12/12` | `>=7/12` | PASS |
| M1 maximum | `0.710452` | `<2` | PASS |
| N2 isolation: candidate / equal Stiefel | `0.983618` | `<=0.99` | PASS |
| FFSP003 adapter qualification | positive/reject/stop/resume/mutation all pass | all pass | PASS |
| F0 math, leakage, package, compute | `247.352B`, reserve `24.648B` | reserve `>=11B` | PASS |
| F1 determinism | both routes byte-identical | exact | PASS |
| F2 pooled candidate / equal | `0.928719` | reject only if `>1.10` | PASS |
| F2 maximum | `1.095947` | reject if `>=4` | PASS |
| F3A candidate / equal | `1.004900` | `<=1.05` | PASS |
| F3B candidate / equal | `1.014361` | `<=1.05` | PASS |
| Pooled F3 candidate / equal | `1.008842` | `<1.0` | **FAIL-SCIENTIFIC** |
| Pooled bootstrap upper 90% | `1.030368` | `<1.10` | PASS |
| Maximum F3 paired ratio | `1.165286` | `<4` | PASS |
| Candidate / incumbent context | `0.774716` | report-only | PASS / favorable |

The pooled directional gate is the only P1 gate that failed. It is not
classified as strict-gate-limited: the candidate is empirically worse than
its exact mechanism ablation. `ALG014-V001` therefore remains at its highest
supported tier, M1, and the project P1 pool remains empty.

The 32-network mean adjusted-score proxies were:

| Arm | Mean local adjusted-score proxy |
|---|---:|
| leverage-exact `ALG014-V001` | `4.52852489e-7` |
| equal-weight `ALG014-V000` | `4.48883343e-7` |
| incumbent `ALG003-V008` | `5.84540132e-7` |

Cross-cohort score or leaderboard-rank inference is not warranted from this
renewable synthetic lane.

## What the failure changes theoretically

The public batch-whitening reports motivated a broad collective-balancing
hypothesis. T091 now separates that hypothesis from the proposed exact
leverage refinement:

1. The large gain is shared by the entire Haar–Stiefel/whitening family. At
   width 64, equal-weight Stiefel scored `0.444598` of iid after work
   normalization and leverage-exact scored `0.437314`. Thus about a `2.25x`
   variance gain came from collective orthogonalization and negative
   dependence; the leverage exponent supplied only the last `1.64%` in that
   fixture.
2. The exact identity removes degree-two angular error, but the antithetic
   bias-free network integrand is an even piecewise-linear function with
   spherical-harmonic energy at degrees `2,4,6,...`. Exactness at degree two
   helps only to the extent that degree-two energy dominates.
3. Equal-weight normalized Stiefel rows are already an increasingly good
   approximate tight frame as dimension grows. With `n=2d`, a projector
   diagonal has `ell ~ Beta(d/2,(n-d)/2)`. Its relative variance is
   `2(n-d)/(d(n+2))`: `0.015385` at `d=64`, but only `0.003891` at `d=256`.
   The correction opportunity therefore shrinks at contest width.
4. Exact leverage weighting trades that shrinking degree-two correction for
   nonuniform weights on all higher harmonics. At `d=256,n=512`, the
   weight-only effective sample size is about `510.02/512` per block. The
   observed pooled `0.884%` loss is consistent with higher-order angular
   energy plus this nonuniform-weight penalty overwhelming the smaller
   degree-two benefit.
5. Ordinary whitening and the exact debiased square-root-leverage arm were
   distinguished prospectively. On the homogeneous width-64 fixture,
   leverage-exact was only `0.998434` of debiased ordinary whitening. The
   prior belief that replacing ordinary whitening with the exact identity
   would preserve most of the public benefit was correct; the stronger belief
   that the replacement itself would add a robust benefit was not.

So the result does **not** say exactness made the whole algorithm bad. It says
the ordinary/equal-weight collective frame was already doing almost all the
useful work, and exact leverage weights slightly harmed the contest-width
mixture of higher angular modes.

## Implementation-defect audit

- The cheap scientific fixture ran Windows-native under MSVC; its source was
  sealed before output and its replay was byte-identical.
- The complete evaluator ran as standalone C++20 under Clang 17 with pinned,
  single-thread NumPy OpenBLAS. No CPython entered the result path.
- Candidate and ablation share the exact same Gaussian matrices, QR frames,
  normalized directions, antipodes, network weights, forward activations,
  reference, and accumulation precision. The only difference is
  `ell_i/256` versus `1/512`. This makes a hidden route or network mismatch an
  implausible explanation of the pooled sign.
- Every production frame checked column orthogonality and leverage sum. The
  smoke errors were `5.52e-7` and `1.20e-5`, inside the frozen `2e-5` and
  `2e-4` limits.
- Both F1 routes replayed byte-for-byte, and an independent raw-TSV aggregate
  recomputation matched the adapter decision.
- An independently compiled GCC 13 evaluator reproduced all ten scientific
  and work fields of Clang route `F3A/000` exactly (maximum absolute
  difference `0`).
- Candidate and ablation were conservatively charged the same full QR and
  forward cost even though the evaluator shared their activations. Therefore
  implementation sharing cannot create an adjusted-score advantage.
- The final metadata audit caught stale derived `identity_hash_sha256` fields:
  they had been calculated before descriptive build/duplicate metadata was
  appended. The exact registered spec bytes and hashes are preserved, the
  canonical current specs now pass the repository's recomputation rule, and
  `REGISTRATION_AMENDMENT.json` binds both versions. No behavior, fingerprint,
  source, binary, route, or decision changed.

No defect signal was found. Independent-machine reproduction remains desirable
under the general containment policy, but the matched-arm design and narrow
loss make an undetected implementation error less likely than a genuine small
negative effect.

## Surprise and next route

The frozen unconditional category `M1 then no P1` had probability `.25`, so
this outcome carries `2.0` bits and is mildly surprising from task start.
Conditioned on already observing M1, rejection had probability
`.25/(.25+.18)=.5814` and was expected. The directionally adverse pooled F3
result reduces belief in leverage-exact weighting, while increasing belief
that equal-weight collective Stiefel sampling deserves its own candidate
identity.

The high-impact next step is not to retune `ALG014-V001`. T091A will
prospectively clone the already frozen equal-weight behavior into a candidate
identity, compare it against a direct collective-balancing-removal control on
fresh E0004 evidence, and carry it to P1/rejection. It may not be
retroactively promoted from its ablation role. H090-A moves after T091A if the
project P1 pool remains empty. No owner action is required.
