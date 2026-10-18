# A genuine attempt at the ARC White-Box Estimation Challenge

**Date:** 2026-08-04  
**Status:** Original method investigated and falsified as a safe submission; conservative estimator packaged; no official grader score claimed.

## Executive result

I tried to improve randomized quasi-Monte Carlo (RQMC) by using the network weights to choose a better coordinate system for the Sobol points. The proposed white-box signal was the input-gradient energy of the **antithetically evenized** final-layer output. In synthetic depth-32 tests, this paired-gradient active-subspace rotation looked genuinely promising at width 128 and produced a modest average gain in several width-256 validation batches.

It did **not** survive the strongest fixed-point tests. A fixed top-64 rotation suffered a large outlier, and a safer top-16 hedge was 2.424× worse than ordinary antithetic Sobol in the one completed full-size width-256 sanity case. I therefore do not claim the active rotation is an improvement, and I did not enable it in the recommended estimator.

The deliverables instead separate two things:

1. `submission_candidate/`: a conservative, contract-oriented estimator using three scrambled Sobol banks, exact radial Rao–Blackwellization, antithetic pairs, a seed-derived coordinate reflection, and the exact first-layer mean.
2. `experimental_active/` and `research/`: the novel active-subspace method, its readable NumPy implementation, raw results, negative experiments, and the falsification evidence.

This is a useful result despite the failed final hypothesis: it identifies a tempting source of selection error in high-dimensional QMC—network-adapted rotations can improve typical cases while creating rare, leaderboard-dominating failures.

## 1. Problem and environment

For a square, bias-free, He-initialized ReLU MLP with standard-normal input, the estimator must return every layer’s vector of expected post-ReLU activations. The primary score uses final-layer mean-squared error under an analytical compute budget. The current starter-kit defaults are width 256, depth 32, and a per-MLP budget of 272 billion FLOPs.

Relevant public materials:

- [ARC announcement](https://www.alignment.org/blog/announcing-the-arc-white-box-estimation-challenge/)
- [AIcrowd challenge page](https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026)
- [Official starter kit](https://github.com/AIcrowd/whest-starterkit)
- [Flopscope](https://github.com/AIcrowd/flopscope)
- [Companion paper: *Estimating the expected output of wide random MLPs more efficiently than sampling*](https://arxiv.org/abs/2605.05179)
- [Public RQMC + Rao–Blackwell write-up](https://discourse.aicrowd.com/t/unbiased-randomized-qmc-rao-blackwell-for-post-relu-activation-means-method-unbiasedness-proof-and-where-the-frontier-is/18053)
- [Public structure-aware submission](https://discourse.aicrowd.com/t/phase-i-submission-structure-aware-estimation-for-random-relu-mlps/18106)

The public frontier already established that plain moment propagation deteriorates with depth, RQMC is a strong baseline, and the best reported Phase 1 method obtained a large gain by classifying neurons into dead, on, and kink regimes and spending sampling compute primarily on the uncertain structure. My goal was to test a different white-box route: use derivatives to expose low-dimensional directions that QMC should resolve preferentially.

## 2. Baseline sampler study

I first compared samplers on synthetic He-Gaussian, width-64, depth-32 networks. Each method used the same number of effective trajectories and was compared against a higher-sample multi-scramble reference. Across 48 trials per method:

| Sampler | Arithmetic mean MSE | Geometric mean MSE | Geometric improvement over IID |
|---|---:|---:|---:|
| IID Gaussian | 9.412e-6 | 4.115e-6 | 1.00× |
| Antithetic IID | 8.550e-6 | 3.035e-6 | 1.36× |
| Scrambled Sobol | 4.466e-6 | 1.514e-6 | 2.72× |
| Antithetic scrambled Sobol | 3.264e-6 | 1.253e-6 | 3.28× |
| Spherical antithetic Sobol | 3.203e-6 | 1.230e-6 | 3.35× |

The spherical method analytically integrates the Gaussian radius. Write a Gaussian input as

\[
X = R U,
\]

where \(U\) is uniform on the unit sphere and \(R\) is an independent chi-distributed radius. A bias-free ReLU network is positively homogeneous:

\[
F(r x)=rF(x),\qquad r\ge 0.
\]

Therefore

\[
\mathbb E[F(X)]
= \mathbb E[R]\,\mathbb E[F(U)]
= \mathbb E\!\left[F\!\left(\mathbb E[R]U\right)\right].
\]

Replacing each sampled Gaussian radius by the constant \(\mathbb E[R]\) is thus exact in expectation, not a Gaussian approximation. It gave only a small empirical gain, but it is low-risk and appears in the conservative candidate.

## 3. The original hypothesis: paired-gradient active-subspace RQMC

### 3.1 Antithetic evenization

Let \(f(x)\in\mathbb R^n\) be the final-layer activation vector and let \(\bar f(x)\) be its normalized neuron average. Antithetic sampling estimates the evenized scalar integrand

\[
g(x)=\frac{\bar f(x)+\bar f(-x)}{2}.
\]

Its input gradient is

\[
q(x)=\nabla g(x)
=\frac{\nabla \bar f(x)-\nabla \bar f(-x)}{2}.
\]

The minus sign is important: it comes from differentiating \(f(-x)\) with respect to \(x\).

### 3.2 Gradient-energy matrix

A small pilot set estimates

\[
C = \mathbb E[q(X)q(X)^\top].
\]

The leading eigenvectors of \(C\) are directions along which the evenized final output changes most. The proposed estimator aligns the highest-quality Sobol coordinates with those directions before performing the main forward pass.

The intuition is standard active-subspace logic applied specifically to QMC: if most low-order variation lies along a small number of directions, giving those directions the best digital-net coordinates can lower integration error without reducing the number of samples.

### 3.3 Why this was not merely a random rotation

The pilot uses the actual network gates and weights. It forwards antithetic samples, backpropagates the final-output average to the input, forms paired gradients, and eigendecomposes their Gram matrix. At width 256, the estimated participation ratio was usually around 75–80, suggesting a broad but non-isotropic active subspace.

Rotating all 256 coordinates was fragile. The later width-256 version preserved only the leading 64 active directions and completed the remaining basis from projected coordinate axes. A still safer hedge rotated only the leading 16 directions in the largest Sobol block.

## 4. Experimental protocol

The experiments used independently generated square He-Gaussian ReLU MLPs with depth 32 and widths 64, 128, or 256. References were averages of multiple larger antithetic scrambled-Sobol runs. Active and plain methods were compared on the same network and main point count.

The reported ratio is

\[
\frac{\text{arithmetic mean active MSE}}
     {\text{arithmetic mean plain MSE}},
\]

so lower than 1 is better. Arithmetic means matter because rare large misses dominate the challenge’s average-MSE objective.

Two qualifications make the reported active ratios optimistic:

- They compare raw integration error at matched main-sample count; the active pilot’s extra FLOPs are not charged in the ratio.
- The local high-sample references are still estimates, especially in the smaller width-256 tests. Matched comparisons reduce but do not remove reference noise.

Selection and frozen-validation batches are labeled separately.

## 5. Main empirical result

| Experiment | Status | Width | Networks | Active / plain mean MSE | Median network ratio | Network win rate |
|---|---|---:|---:|---:|---:|---:|
| Full active basis | Selection | 128 | 10 | **0.390** | 0.467 | 80% |
| Full active basis | Frozen validation | 128 | 20 | **0.655** | 0.646 | 70% |
| Top-64 active basis | Frozen validation | 256 | 20 | **0.889** | 0.977 | 50% |
| Fixed float16 top-64 set | Validation | 256 | 8 | **1.190** | — | 67% of trials |
| Top-16 largest-block hedge | Selection | 256 | 8 | **0.483** | 0.420 | 87.5% |
| Top-16 hedge | Frozen validation | 256 | 16 | **0.948** | 1.012 | 50% |
| Top-16 hedge, full-size fixed set | Falsification sanity check | 256 | 1 | **2.424** | — | — |

The width-128 frozen result was initially encouraging. A network-cluster bootstrap on those 20 networks put approximately 96.6% probability on an improvement, although its 95% interval still reached slightly above parity. At width 256, the effect weakened: the 20-network top-64 aggregate was an 11.1% arithmetic-mean improvement, but its bootstrap interval was broad and its win rate was only 50%.

The decisive evidence came from fixed-point tests. Averaging over many fresh Sobol scrambles had hidden orientation risk. With the exact fixed float16 points a submission would ship, top-64 had a severe outlier and lost in arithmetic mean. The top-16 hedge reduced the tails in its selection batch but was effectively neutral on 16 frozen networks and had a worst-network ratio of 1.918.

Finally, I ran the near-full-size fixed configuration. On the one completed network:

- plain fixed Sobol MSE: \(7.514\times10^{-8}\)
- active hedge MSE: \(1.821\times10^{-7}\)
- ratio: **2.424**

A second network’s expensive reference completed, but the full active comparison exceeded the available execution window. One network is not a population estimate, but it is enough to reject the method as a safe submission: the proposed change was supposed to be a robust variance reduction and instead created a large miss under the exact deployment conditions.

## 6. Negative results

Several other apparently reasonable ideas failed to produce a stable gain:

1. **Conditional-Gaussian / low-rank final-layer integration.** Integrating a low-rank Gaussian residual around sampled penultimate activations changed MSE only by a few percent and was unstable. It cannot remove the dominant common mean-estimation error.
2. **Exact sample mean or covariance matching.** Whitening or moment-matching the input point set was neutral or harmful. Better low-order Gaussian moments did not imply better deep ReLU integration.
3. **Exact first-layer linear control variates.** Regressing on the first-layer activations, whose means are known exactly, was neutral on average and occasionally harmful. Thirty-one subsequent ReLU layers largely destroy the useful correlation.
4. **Quadratic controls from antithetic first-layer features.** Features based on \(|W_1^\top x|\) have tractable moments and looked promising in a discovery batch, but a fresh 40-network validation set erased the gain and exposed outliers.
5. **Random dense rotations.** These sometimes improved geometric mean error but worsened arithmetic mean through rare catastrophic orientations.
6. **Full active rotations.** The active directions themselves were informative, but using the entire eigenbasis as the QMC coordinate system was substantially less robust than retaining the coordinate-like inactive complement.

The general lesson is that high-dimensional QMC orientation selection has a heavy multiple-testing penalty. A rotation can look excellent over several networks and scrambles because typical-case gains are real, while a small number of bad network–point-set alignments dominate the actual objective.

## 7. Conservative submission candidate

The recommended folder is `submission_candidate/`. Its estimator deliberately excludes the failed active rotation.

### 7.1 Algorithm

For each MLP it:

1. Loads three precomputed float16 banks of scrambled Sobol directions, each divided into independently scrambled power-of-two blocks.
2. Chooses one bank using `mlp.seed`.
3. Applies a seed-derived coordinate reflection. Reflections preserve the spherical target distribution and do not reorder Sobol dimensions.
4. Uses points on the sphere of radius \(\mathbb E\|N(0,I_{256})\|\), exactly integrating radial variation by positive homogeneity.
5. Adds the global antithetic partners.
6. Propagates 62,464 trajectories in float32 and records every layer mean.
7. Replaces layer 1 with the exact value

\[
\mathbb E[\operatorname{ReLU}(w_i^\top X)]
=\frac{\|w_i\|_2}{\sqrt{2\pi}}.
\]

For a nonstandard width/depth, missing data file, or very small budget, it falls back to diagonal Gaussian moment propagation.

### 7.2 Analytical budget estimate

At width 256, depth 32, and 31,232 stored positive points:

| Component | Estimated FLOPs |
|---|---:|
| 32 dense forward matmuls | 261,481,299,968 |
| ReLUs | 511,705,088 |
| Float32 means | 511,705,088 |
| Reflection, negation, exact first row | 16,122,368 |
| **Estimated total** | **262,520,832,512** |
| Budget | 272,000,000,000 |
| **Estimated reserve** | **9,479,167,488** |

This uses the current flopscope textbook formula \(2mkn-mn\) for a dense \((m,k)@(k,n)\) matrix multiplication. The first draft mistakenly used \(mkn\); catching and correcting that error reduced the main point count by roughly half.

The largest float32 activation array is approximately 64.0 MB. The submission files total approximately 45.8 MiB before packaging, below the documented 50 MiB submission cap.

### 7.3 Validation status

Completed locally:

- Python compilation for both estimator implementations and all smoke tests.
- Dependency-independent NumPy smoke test of the candidate’s output shape, finite values, budget fallback, bank handling, seed reflection, and exact first-layer row.
- Reproducible point generation with seeds, SHA-256 hashes, finite-value checks, and near-constant spherical radii after float16 quantization.
- Corrected analytical FMA=2 budget audit.

Not completed:

- `whest validate` or a real `whest run` under the pinned flopscope/whestbench environment.
- An official AIcrowd submission or grader score.

The execution container had neither dependency installed and could not resolve external package hosts, so I could not honestly claim an official contract or FLOP-count pass. The archive should therefore be treated as a serious candidate that still has one hard gate: run it through the current starter kit before submission.

## 8. What I would try next

The most promising continuation is not another global input rotation. It is to combine the paired-gradient idea with the public dead/on/kink decomposition:

- Remove dead neurons analytically.
- Fold confidently on neurons into the linear map.
- Define the pilot objective only on the uncertain kink contribution.
- Estimate an active subspace for that smaller residual integrand.
- Use an independent pilot split to decide whether a rotation is enabled, with a conservative no-rotation default.

That attacks the part of the integrand where the public structure-aware work says the remaining variance actually lives. It also avoids letting a global coordinate transform disturb the large smooth/linear component that ordinary Sobol already integrates well.

A second route is robust model selection across a small bank of coordinate systems. The selector would need an unbiased or cross-fitted estimate of **arithmetic MSE risk**, not merely pilot variance or geometric-mean improvement. The experiments here suggest that tail control is more important than maximizing the typical gain.

## 9. Reproduction map

- `submission_candidate/estimator.py` — conservative estimator.
- `submission_candidate/sobol_sphere_banks_f16.npy` — three shipped point banks.
- `submission_candidate/points_metadata.json` — shapes, seeds, radius, quantization error, hash.
- `experimental_active/estimator.py` — experimental paired-gradient estimator.
- `research/prototype_numpy.py` — readable NumPy/SciPy active-subspace implementation.
- `research/benchmark_*.py`, `research/validate_*.py` — experiment drivers.
- `research/raw_results/` — raw JSON outputs.
- `research/experiment_summary.csv` — compact result ledger.
- `research/budget_estimate.json` — conservative candidate budget calculation.
- `research/figures/` — validation plots.
- `tests/` — dependency-independent smoke tests.

The central conclusion is deliberately not polished into a false success: the paired-gradient basis contained real signal, but the proposed way of feeding that signal into a fixed high-dimensional Sobol rule was not robust enough for an arithmetic-mean leaderboard. The conservative candidate is usable; the experimental method is evidence and a direction for a more targeted successor.
