# Literature index for competitive estimation

Established by the owner-authorized **T132** trial, 2026-09-06. The objective is
better official submissions, regardless of academic novelty. This is a living
index: reuse entries and update access/scope when a later task adds information.
The [route tracker](RESEARCH_ROUTE_STATUS.md) determines where another search
could repay its time. [T132's report](../experiments/literature/t132/REPORT.md)
contains the ranked handoff. Listing a paper does not establish implementation
feasibility or transfer its performance to this challenge.

Access labels: **code** = relevant implementation inspected without execution;
**sections** = named substantive parts read, not a full proof audit;
**abstract** = primary abstract/overview only. Search snippets alone do not
support an implementation recommendation. Dates below are publication or
preprint years, not search-engine crawl dates. Last checked: 2026-09-08.

| ID | Primary source | What to reuse / relevant limit | Access and project relationship |
|---|---|---|---|
| L01 | venture_agent_ai, [Phase 2 write-up](https://github.com/agentaiventure-dot/arc-whest-estimator/blob/fb33bb5a66b4b0aed3022e6a70a9274d5957d61d/docs/ALGORITHMIC_CONTRIBUTION.md), 2026; [estimator](https://github.com/agentaiventure-dot/arc-whest-estimator/blob/fb33bb5a66b4b0aed3022e6a70a9274d5957d61d/estimator/estimator.py) | Fixed Gaussian propagation with quadrature covariance and a five-coefficient output correction per layer. Provides a concrete inexpensive comparator. Calibration stays outside the propagated state. | **Code**, full estimator and write-up; selected result logs and MIT license. New actionable public implementation found in T132. Reported score is not independently verified here. [Pin](../experiments/literature/t132/PUBLIC_SOURCE_PIN.json). |
| L02 | Same author, [exact covariance results](https://github.com/agentaiventure-dot/arc-whest-estimator/blob/fb33bb5a66b4b0aed3022e6a70a9274d5957d61d/results/exact_cov_RESULTS.md) | Reports 55,694,969,087 FLOPs and about 1.3695e-7 adjusted on four public MLPs after calibration. This is external evidence on a different panel. | **Sections** 3, 5, 6 and execution summary. No local reproduction or imported targets. |
| L03 | Wu et al., [Estimating the expected output of wide random MLPs more efficiently than sampling](https://arxiv.org/html/2605.05179v2), 2026; [public code](https://github.com/alignment-research-center/mlp_cumulant_propagation) | Full/power cumulants and factorized propagation. Appendix S.4.3 makes the depth cost explicit: the basic K=3 factor list grows with depth, giving O(n^3 L^2), not a fixed-rank free upgrade. | **Sections** 4.3 and S.4.3 revisited; code availability checked, implementation not newly audited. Already central to the project. |
| L04 | Wright, Nakahira & Moura, [An Analytic Solution to Covariance Propagation in Neural Networks](https://proceedings.mlr.press/v238/wright24a.html), 2024 | Established analytic Gaussian covariance propagation. Useful reference when changing covariance numerics; does not itself settle propagated non-Gaussian error. | **Abstract**, previously cited in T113/T119. No new mechanism claimed. |
| L05 | Gorodetsky et al., [A generalized approximate control variate framework for multifidelity uncertainty quantification](https://www.alexgorodetsky.com/static/papers/gorodetsky_et_all_acv_2020.pdf), 2020 | ACV-IS/ACV-MF explicitly price unknown control means and different sample overlaps. Reuse these covariance constructions when designing partial or multiple-source estimators. | **Sections** 3.1, Theorems 3–5 and Table 3. Already cited in T113; overlapping spherical frames require their actual covariance law rather than an iid substitution. |
| L06 | Peherstorfer, Willcox & Gunzburger, [Optimal Model Management for Multifidelity Monte Carlo Estimation](https://kiwi.oden.utexas.edu/papers/multi-fidelity-monte-carlo-peherstorfer-willcox-gunzburger.pdf), 2016 | Allocate evaluations using model costs and correlations. A cheap surrogate must save enough total variance to pay for its construction and estimation. | **Abstract/introduction**. General allocation framework; no ARC speedup inferred. |
| L07 | Oates & Girolami, [Control Functionals for Quasi-Monte Carlo Integration](https://proceedings.mlr.press/v51/oates16.html), 2016 | Approximate an integrand and integrate its residual. Reuse established formulation instead of rederiving control-function basics. | **Abstract**, T119/T122 already contain the design-matching warning. No new QMC convergence claim made. |
| L08 | Oates, Girolami & Chopin, [Control functionals for Monte Carlo integration](https://arxiv.org/abs/1410.2392), 2014/2017 | Stein-based function spaces give controls with tractable expectations; approximation and fitting costs remain part of the estimator. | **Abstract**. Broad control family is established; no fixed-width implementation lead recovered here. |
| L09 | Leluc et al., [Sliced-Wasserstein Estimation with Spherical Harmonics as Control Variates](https://arxiv.org/pdf/2402.01493), 2024 | Spherical-harmonic regression and an explicit dimension formula for its control space. Evenness removes odd harmonics. | **Sections** 4.1–4.2, Lemma 1, Algorithm 2 and experiment dimensions. Related to R4IF8-P; full polynomial fitting does not scale to our 1024-dimensional input at present sample counts. |
| L10 | Griewank et al., [High dimensional integration of kinks and jumps—smoothing by preintegration](https://arxiv.org/abs/1712.00920), 2017/2018 | Integrate one coordinate before outer quadrature, under assumptions that make that inner operation accurate and the remaining function smooth. | **Sections** 2 and numerical setup via publisher text. Potentially useful for a restricted conditional route, not a generic deep-ReLU shortcut. |
| L11 | Gilbert, Kuo & Sloan, [Preintegration is not smoothing when monotonicity fails](https://arxiv.org/pdf/2112.11621), 2021 preprint | Failure of the monotonicity assumption can leave singularities after preintegration. | **Abstract/introduction**. A limit on transferring smoothness guarantees, not a proof that conditional expectation cannot reduce variance. |
| L12 | Sotoudeh & Thakur, [Computing Linear Restrictions of Neural Networks](https://arxiv.org/pdf/1908.06214), 2019 | EXACTLINE computes piecewise-linear restrictions by composing layerwise breakpoint partitions. Existing algorithm can replace invention of this primitive. | **Section** 2, Theorems 1–3 and algorithm discussion. Already cited for T113's ALCI reserve; whole Gaussian lines and counted work still need adaptation. |
| L13 | Monchot et al., [Input uncertainty propagation through trained neural networks](https://proceedings.mlr.press/v202/monchot23a/monchot23a.pdf), 2023; [WGMprop](https://github.com/PaulMcht/WGMprop) | Gaussian splitting with a Wasserstein criterion. Practical algorithm uses sigma points and reduction to leading input-covariance eigendirections. | **Sections** 2, 3.4 and Algorithm 1; repository availability only. T119/T129 already cited it. Isotropic input has no preferred covariance eigensubspace, so direct low-rank adoption discards input variance. |
| L14 | Macdonald & Wäldchen, [A Complete Characterisation of ReLU-Invariant Distributions](https://proceedings.mlr.press/v151/macdonald22a.html), 2022 | Strong restrictions on exact parametrized families invariant under general ReLU layers. | **Abstract**, previously cited in T119. Does not rule out useful approximate closures or task-specific means. |
| L15 | Hayakawa, Oberhauser & Lyons, [Positively Weighted Kernel Quadrature via Subsampling](https://papers.neurips.cc/paper_files/paper/2022/hash/2dae7d1ccf1edf76f8ce7c282bdf4730-Abstract-Conference.html), 2022; [code](https://github.com/satoshi-hayakawa/kernel-quadrature) | Positive-weight subsampling of a larger empirical measure using a kernel representation. Public implementation identifies its numerical optimizer dependencies. | **Abstract and repository README**. The inspected code uses Gurobi; it is a reference, not a ready submission dependency. |
| L16 | Hayakawa, Oberhauser & Lyons, [Sampling-based Nyström Approximation and Kernel Quadrature](https://proceedings.mlr.press/v202/hayakawa23a/hayakawa23a.pdf), 2023 | Section 5 describes empirical-measure recombination with explicit approximation and construction costs. | **Section** 5, Theorem 3, empirical replacement and complexity discussion. Concrete library for the old output-compression question; no current-parent kernel or source-bank accuracy established. |
| L17 | Dolgov & Savostyanov, [Parallel cross interpolation for high-precision calculation of high-dimensional integrals](https://arxiv.org/abs/1903.11554), 2019/2020; [ttcross](https://github.com/savostyanov/ttcross) | Adaptive tensor-product approximation and quadrature, given sufficiently compressible functions. | **Abstract and repository README**. No evidence yet that dense random ReLU integrands have affordable tensor-train ranks. Source implementation is not a tracked Python submission. |
| L18 | Siahkoohi & Oh, [Conditional neural control variates for variance reduction in Bayesian inverse problems](https://proceedings.mlr.press/v337/siahkoohi26a.html), 2026 | Amortized conditional learned controls; relevant if training can transfer across different estimation instances. | **Abstract**, already in T119. Input conditioning in inverse problems does not establish transfer across our realized weight matrices. |
| L19 | Ott et al., [Bayesian Numerical Integration with Neural Networks](https://arxiv.org/abs/2305.13248), 2023 | Bayesian Stein networks offer an alternative to dense GP quadrature. | **Abstract only**. Training and derivative costs for each supplied MLP unresolved; retain as background rather than a nominee. |
| L20 | SkyeNygaard, [public ARC implementation](https://github.com/SkyeNygaard/arc-whitebox), 2026 | Public static-cubature construction, fast arithmetic and negative-result archive. | **README** checked. Public Phase 1 material is not the private Phase 2 algorithm; T112 already built and tested a certified Kerdock reconstruction. |

The September 5 participant's older write-up estimated a long Kerdock build;
its newer README links a completed construction. Neither is a reason to repeat
our already completed T112 construction. Search results must be compared with
both the latest source state and our own records.

T132 did not obtain the official receipt for external submission 329951 through
the browser. Its score remains **author-reported**. Failed access and the exact
search queries are in the [search log](../experiments/literature/t132/SEARCH_LOG.json).
No claims about current leaderboard rank or a reproduced external grade follow.

## T136 refresh — 2026-09-06/07 UTC

The [combined recurrence](../experiments/theory/t136/REPORT.md) reuses L03 and
L15–L16. L03 now has a targeted source audit at revision
`93d091a4c26c042bfffa28f2e76a81bc0aba94bb`, matching remote HEAD when checked.
The source's TODO says cached K>=2 results/counts need refresh after changed
diagram rules; factorized AUGMENT also drops some terms retained by dense
AUGMENT. Use its algorithms with those qualifications, not old plots as current
cost/score evidence. [Pinned files](../experiments/theory/t136/PUBLIC_SOURCE_PIN.json).
`get_r_x` explicitly supplies the trace-vector/fourth-scalar augmented-K2 state.

| ID | Primary source | Reuse / limitation | Access |
|---|---|---|---|
| L21 | Harshaw et al., [Balancing covariates in randomized experiments with the Gram–Schmidt Walk design](https://arxiv.org/html/1911.03071v4), JASA 2024 | A known randomized balancing algorithm with robustness and ridge-error bounds. Its fixed-group-size modification loses the orthogonality used in the original analysis. T136's bounded rejection observation is separate mathematics. | Algorithm4, covariance/ridge results, complexity12 and fixed-group13.2; not a full supplement audit. |
| L22 | Tillé & Rivest, [Existence and applications of finite-population samples that are exactly balanced](https://doi.org/10.1093/biomet/asaf058), Biometrika 2025 | Cube-flight martingale and balance geometry. This is established sampling machinery; exact balance alone does not control arbitrary residual variance. | Section3 read through publisher; final reopen failed on a CDN redirect. The older2004 PDF link returned410; no text imported from it. |
| L23 | Cosentino, Oberhauser & Abate, [A Randomized Algorithm to Reduce the Support of Discrete Measures](https://arxiv.org/abs/2006.01757), NeurIPS 2020 | Support-reduction algorithm pointer. Randomized geometric search is not by itself an unbiased quadrature guarantee. | Abstract and primary conference-PDF pointer only. |
| L24 | Li, Dwivedi & Mackey, [Debiased Distribution Compression](https://arxiv.org/abs/2404.12290), ICML 2024 | Stein thinning/recombination can address biased source sequences under kernel assumptions. No qualified ARC output-sensitive kernel follows. | Abstract and method structure; no full proof or implementation audit. |
| L25 | [Distribution Compression in Near-linear Time](https://arxiv.org/abs/2111.07941), 2021 preprint; [goodpoints](https://github.com/microsoft/goodpoints) | Compress++ is a construction-speed lead. Solver efficiency alone does not supply low quadrature error for the current network residual. | Abstract and repository README only. |

For L16, Section5.1 equations12–14 and Theorems3/4 were revisited. The empirical
bank error remains in the bound, and its displayed sampling rate uses an iid
bank. T136 derives the appropriate conditional decomposition separately and
does not substitute that iid rate for overlapping orthogonal frames.

The search log preserves access limits and normalized query topics. T136's
candidate improvements are mathematical adaptations of known methods, with
no academic-novelty requirement and no claim of an external score reproduction.


## T139 refresh — 2026-09-08

Focused search:10.665 minutes. The [search log](../experiments/theory/t139/SEARCH_LOG.json)
records normalized topics and access limits. L03's factorized source and
L13's Gaussian splitting were revisited; no new remote revision or external
score was independently reproduced.

| ID | Primary source | Reuse / limitation | Access |
|---|---|---|---|
| L26 | Jin, Kileel, Kolda & Ward, [Scalable symmetric Tucker tensor decomposition](https://arxiv.org/pdf/2204.10824), 2022 | Implicit symmetric tensor compression; core construction and basis changes must be charged. HOSVD is not a matrix-style exact best-rank theorem. | Sections2–3, HOEVD/PGD and costs; PDF read, HTML access failed. |
| L27 | Sun, Guo, Luo, Tropp & Udell, [Low-Rank Tucker Approximation of a Tensor from Streaming Data](https://tropp.caltech.edu/papers/SGLTU20-Low-Rank-Tucker.pdf), 2020 | Streaming sketches and Tucker approximation. Structured bilinear probes need their own accuracy justification. | Algorithms4.2–4.3, Theorems5.1–5.3 and tensor random projections. |
| L28 | Otto, Padovan & Rowley, [Model Reduction for Nonlinear Systems by Balanced Truncation of State and Gradient Covariance](https://arxiv.org/html/2207.14387v4), 2022/2023 | State magnitude and output sensitivity are different objectives. No ready ARC implementation inferred. | Abstract and Section2.1; not a full proof audit. |
| L29 | Tsilifis & Ghanem, [Reduced Wiener Chaos representation](https://arxiv.org/abs/1603.04803), 2016/2017 | Reduced Gaussian-chaos coordinates are established; covariance residuals still matter in a conditional source. | Abstract only this turn; also cited in T129. |
| L30 | Brillinger, [The calculation of cumulants via conditioning](https://www.ism.ac.jp/editsec/aism/pdf/021_1_0215.pdf), 1969 | Primary conditioning/cumulant reference pointer. T139 derives and checks its needed identity separately. | Located only: scanned PDF did not provide readable text; no newly audited proof claimed. |

T139's actionable result is the [C64-E mathematical handoff](../experiments/theory/t139/C64E_MATHEMATICAL_HANDOFF.md),
combining established tensor compression with persistence of the incumbent's
modeled old remainder. The independent [Q4D handoff](../experiments/theory/t139/Q4D_MATHEMATICAL_HANDOFF.md)
uses available fourth-moment constraints. Neither is an imported external
estimator, a new novelty claim, or a measured candidate score.


## T143 broader adjacent review — 2026-09-08/09 UTC

The owner allocated at least60 exclusive minutes to literature, alongside
separate120-minute derivation and30-minute selection floors. The
[reading notes](../experiments/theory/t143/LITERATURE_NOTES.md) contain50 new
source entries, L31–L80, plus a renewed L03 paper/code audit. They include
abstract-only and limited-section access; this is not a claim that50 complete
papers or proofs were audited. The [source registry](../experiments/theory/t143/SEARCH_LOG.json)
records normalized topics, URLs, access levels and limits.

The registry distinguishes40 entries read in selected substantive sections,
four limited introductory/formulation readings, three abstract/overview
readings, two public method write-ups, one indexed primary excerpt, and the
separate existing-paper/code audit. Source count measures search coverage;
candidate readiness is assessed separately in the T143 result.

[Adjacent-method synthesis](../experiments/theory/t143/ADJACENT_METHODS.md)
organizes what transfers and what remains missing. The most useful connections
are response-sensitive retention, explicit unresolved-state memory, and
Gaussian/full-covariance states supplemented by selected nonlinear information.
No clearly superior ready external estimator was recovered. No external
challenge dataset, individual prediction/target record or estimator execution
was imported. Public results are not treated as local reproductions.

The following compact catalog reserves the IDs; substantive access and transfer
limits are in the reading notes, rather than duplicated here.

| ID | Topic / source pointer | Access |
|---|---|---|
| L31 | [correlation-function network propagation](https://arxiv.org/html/2202.04925v2) | selected substantive sections |
| L32 | [moment-preserving kinetic reduction](https://doi.org/10.1007/s10915-024-02684-1) | selected substantive sections |
| L33 | [conservative dynamical low rank](https://doi.org/10.1016/j.jcp.2023.112060) | limited introductory/formulation sections |
| L34 | [generalized unscented transformation](https://arxiv.org/html/2104.01958v2) | limited introductory/formulation sections |
| L35 | [projection, memory and closure](https://www.cfm.brown.edu/faculty/gk/PUBS/documents/Venturi_RoySoc_Convolutionless.pdf) | selected substantive sections |
| L36 | [nonlinearity-aware Gaussian splitting](https://arxiv.org/pdf/2412.00343) | selected substantive sections |
| L37 | [expectation-consistent inference](https://www.jmlr.org/papers/volume6/opper05a/opper05a.pdf) | abstract or introductory overview only |
| L38 | [perturbative corrections around matched Gaussian inference](https://www.jmlr.org/papers/volume14/opper13a/opper13a.pdf) | selected substantive sections |
| L39 | [cumulants as weak-error indicators](https://arxiv.org/abs/1109.1546) | abstract or introductory overview only |
| L40 | [fresh public challenge feedback](https://discourse.aicrowd.com/t/phase-2-write-up-zero-fitted-constants-measured-what-the-64-calibration-numbers-in-a-relu-mlp-mean-propagator-are-actually-absorbing-submission-330001/18216) | author public write-up; external results not reproduced |
| L41 | [truncated Gaussian moment recurrence](https://www.cesarerobotti.com/wp-content/uploads/2019/04/JCGS-KR.pdf) | selected substantive sections |
| L42 | [tail expectation via saddlepoint methods](https://www.math.hkust.edu.hk/~maykwok/piblications/Saddlepoint.pdf) | selected substantive sections |
| L43 | [asymptotic order versus polynomial degree](https://arxiv.org/pdf/astro-ph/9711239) | selected substantive sections |
| L44 | [finite cumulant truncation is a formal closure](https://arxiv.org/html/2107.08469v3) | limited introductory/formulation sections |
| L45 | [maximum entropy does not eliminate dynamical closure error](https://arxiv.org/html/1103.4980v2) | selected substantive sections |
| L46 | [system-size expansions as a closure audit](https://doi.org/10.1063/1.3702848) | abstract or introductory overview only |
| L47 | [positive density closures and their cost](https://doi.org/10.1007/s10955-016-1529-5) | selected substantive sections |
| L48 | [nonlinear response and diagram resummation](https://doi.org/10.1371/journal.pcbi.1005583) | selected substantive sections |
| L49 | [fixed-rank first-order updates](https://www.jmlr.org/papers/volume24/21-0438/21-0438.pdf) | primary indexed excerpt only |
| L50 | [Generalized Price theorem (Voigtlaender)](https://arxiv.org/html/1710.03576v1) | selected substantive sections |
| L51 | [Gradient-based vector-valued dimension reduction (Zahm et al.)](https://arxiv.org/pdf/1801.07922) | selected substantive sections |
| L52 | [Hutch++ (Meyer, Musco, Musco & Woodruff)](https://arxiv.org/html/2010.09649v4) | selected substantive sections |
| L53 | [XTrace (Epperly, Tropp & Webber)](https://tropp.caltech.edu/papers/ETW24-XTrace-Making-SIMAX.pdf) | selected algorithm, efficient implementation and variance/error-estimate sections |
| L54 | [Wiener-chaos optimal prediction (Alpay & Kipnis)](https://arxiv.org/html/1411.3032v3) | selected substantive sections |
| L55 | [Optimal prediction with memory (Chorin, Hald & Kupferman)](https://math.berkeley.edu/~chorin/CHK02.pdf) | selected substantive sections |
| L56 | [Finite-width cumulant hierarchy (Hanin)](https://www.jmlr.org/papers/volume25/23-0643/23-0643.pdf) | selected substantive sections |
| L57 | [Neural covariance SDE (Li, Nica & Roy)](https://arxiv.org/abs/2206.02768) | selected substantive sections |
| L58 | [Quenched network Hamiltonians (Winer & Hanin)](https://arxiv.org/html/2503.23982v2) | limited introductory/formulation sections |
| L59 | [Public trajectory-calibrated moment chain (James Henry)](https://github.com/jamesrahenry/arc-whitebox-replication/blob/master/WRITEUP.md) | author public write-up; external results not reproduced |
| L60 | [Mori–Zwanzig neural-network formulation (Venturi & Li)](https://arxiv.org/html/2209.05544v3) | selected substantive sections |
| L61 | [History-enriched linear reduction (Vijaywargiya & Biros)](https://arxiv.org/html/2601.07101v1) | selected substantive sections |
| L62 | [Arc-cosine observable kernel (Cho & Saul, 2009)](https://papers.nips.cc/paper/2009/file/5751ec3e9a4feab575962e78e006250d-Paper.pdf) | selected substantive sections |
| L63 | [Higher-order Stein kernels (Fathi, 2019)](https://www.normalesup.org/~mfathi/docs/Higher%20order%20Stein%20kernels%20final.pdf) | selected substantive sections |
| L64 | [Second-order Poincare neural-network bounds (Bordino et al., 2024)](https://proceedings.mlr.press/v253/bordino24a.html) | selected substantive sections |
| L65 | [Goal-oriented model-constrained reduction (Bui-Thanh et al., 2007)](https://www.cs.cmu.edu/~oghattas/papers/goob-jcp.pdf) | selected substantive sections |
| L66 | [Fixed-realization binary-network cumulants (Dahmen, Bos & Helias, 2016)](https://journals.aps.org/prx/pdf/10.1103/PhysRevX.6.031024) | selected substantive sections |
| L67 | [ANOVA kernels and symmetric tensor factors (Blondel et al., 2016)](https://proceedings.mlr.press/v48/blondel16.pdf) | selected substantive sections |
| L68 | [TensorSketch (Pham & Pagh, 2013)](https://www.rasmuspagh.net/papers/tensorsketch.pdf) | selected substantive sections |
| L69 | [Complex TensorSketch (Sharma et al., UAI2026)](https://arxiv.org/html/2608.10523v1) | selected substantive sections |
| L70 | [Bussgang decomposition (Demir & Bjornson, 2021)](https://arxiv.org/pdf/2005.01597) | selected substantive sections |
| L71 | [Deep Gaussian-field functional fluctuations (Di Lillo et al., 2026)](https://arxiv.org/html/2604.19738v1) | selected substantive sections |
| L72 | [Products of Gaussian quadratic forms (Magnus, 1978)](https://www.janmagnus.nl/papers/JRM003.pdf) | selected substantive sections |
| L73 | [Loop calculus and representation gauges (Chertkov & Chernyak, 2006)](https://arxiv.org/pdf/cond-mat/0601487) | selected substantive sections |
| L74 | [Carleman moment propagation (Pruekprasert et al., 2024)](https://arxiv.org/pdf/2201.08648) | selected substantive sections |
| L75 | [Recursive polynomial chaos (Bal et al., 2026)](https://arxiv.org/html/2605.03853v1) | selected substantive sections |
| L76 | [Dynamical polynomial chaos with KL restarting (Ozen & Bal, 2017)](https://arxiv.org/html/1605.04604v2) | selected substantive sections |
| L77 | [Adaptive split–combine filtering (2026)](https://arxiv.org/html/2608.04430v1) | selected substantive sections |
| L78 | [Blended full-covariance and reduced nonlinear dynamics (Sapsis & Majda, 2013)](https://bpb-us-e1.wpmucdn.com/sites.mit.edu/dist/6/1408/files/2023/03/13_PhysicaDb.pdf) | selected substantive sections |
| L79 | [Full-environment tensor truncation (Evenbly, 2018)](https://arxiv.org/html/1801.05390v2) | selected substantive sections |
| L80 | [Zero-mode tensor-network truncation (2026)](https://arxiv.org/html/2605.09385v1) | selected substantive sections |


L03 remains at arXiv v2 and code revision
`93d091a4c26c042bfffa28f2e76a81bc0aba94bb` when checked during T143.
The augmented paths are published prior art. The unchanged-column paired
source proposal is a repository adaptation; its finite factor update also
retains explicitly identified higher-order terms. The ANOVA query Gram,
arc-cosine kernel and Bussgang identities likewise have established origins.
No broad mathematical novelty or inherited deep-ReLU guarantee is claimed.

## T146 — focused response, fourth-source and homogeneous-state review

Sixteen additional entries were inspected, with actual reading depth and
transfer limits in [T146's notes](../experiments/theory/t146/LITERATURE_NOTES.md).
These are source entries, not sixteen new algorithms or full-paper readings.
The decision-changing discovery is L85's newly public Phase2 implementation.
Its external result has not been independently reproduced in this repository.

| ID | Primary source | Reading and use in T146 |
|---|---|---|
| L81 | [Williams, Computing with Infinite Networks](https://papers.nips.cc/paper/1996/file/ae5e3ce40e0404a45ecacaaf05e5f735-Paper.pdf) | Section3 and integration-by-parts argument; analytic gated-row metric under a stated variance approximation. |
| L82 | [Fengler–Jung, centered quadratic feature concentration](https://arxiv.org/pdf/1905.09245) | Main RIP statements and spherical argument; assumptions do not directly certify our solver. |
| L83 | [Adamczak et al., independent-column random matrices](https://www.math.ualberta.ca/~alexandr/papers/ALPT-II-rev10.pdf) | Section3.1, Theorems3.1–3.2; no useful numerical iteration guarantee imported. |
| L84 | [Bandeira et al., matrix chaos inequalities](https://web.math.princeton.edu/~rvan/chaosconf241224.pdf) | Introduction and theorem statements; not a full proof audit. |
| L85 | [504aldo, public Phase2 cumulant estimator](https://github.com/504aldo/whest-p2-cumulant-k3/tree/18c17e2d7a9aeacd399cfc2c6b571e4e16dbfb45) | Selected source, derivation, ablation and evidence documents. One concrete reproduction nominee; author-reported score5.40e-9, unverified locally. |
| L86 | [Shim, Gaussian reference and Hermite tails](https://arxiv.org/html/2607.07712v1) | Sections2.1–2.2,4–8,11 and isotropic specialization; no deep homogeneous-closure bound follows. |
| L87 | [Cortinovis–Kressner, indefinite trace estimation](https://arxiv.org/pdf/2005.10009) | Gaussian proof and Rademacher bounds; evaluate absolute or total-source uncertainty for a small signed trace. |
| L88 | [Eldan–Moshkovitz, restricted Hermite tensors](https://drops.dagstuhl.de/storage/00lipics/lipics-vol215-itcs2022/LIPIcs.ITCS.2022.64/LIPIcs.ITCS.2022.64.pdf) | Theorem8 and Sections5.1–5.3; restriction differs from marginalization and recurrent closure. |
| L89 | [Herrera-Esposito–Burge, projected-normal moments](https://arxiv.org/html/2506.17461v1) | Selected moment formulas and appendices; ordinary angular normalization differs from the needed weighted law. |
| L90 | [Ospald–Herzog, angular-central-Gaussian closure](https://d-nb.info/1247661113/34) | Both pages; low-dimensional closure context, no width1024 implementation. |
| L91 | [Bach, spherical ridge-function harmonics](https://jmlr.org/papers/volume18/14-546/14-546.pdf) | AppendixD.1–D.2; single-layer harmonic null spaces do not transfer to arbitrary depth. |
| L92 | [Molchanov–Schmutz–Stucki, zonoid equivalence](https://arxiv.org/pdf/1203.6085) | Main equivalence proof, consequences and change of measure; weighted positive-cone observable state. |
| L93 | [Molchanov–Nagel, diagonal transforms and zonoids](https://arxiv.org/pdf/1806.08036) | Main statements and positive-case proof; zero-coordinate support faces matter. |
| L94 | [Siegel, zonoid approximation](https://doi.org/10.1007/s00365-025-09712-9) | Theorems1–3 and selected discrepancy proof; fixed-dimension rate does not supply a ready high-dimensional deep estimator. |
| L95 | [Heddes et al., tensor-network sketches](https://arxiv.org/pdf/2603.07387) | Algorithms, guarantees and selected proofs; cyclic contraction bound is relative to input norms, not our small signed output. |
| L96 | [Han et al., polynomial TensorSketch for elementwise functions](https://proceedings.mlr.press/v119/han20a/han20a.pdf) | Algorithms1–2, Theorem1 and coefficient/coreset formulation; no fitted polynomial or estimator adopted. |

L03's selected current source, L50's Price theorem, L51's response objective,
L53's trace estimator, L56's finite-width hierarchy, L63's Stein kernels and
L79's tensor environment were revisited. The
[corrected TensorSketch version](https://arxiv.org/pdf/2505.08146) clarifies
L68: its general variance bound has `(3^p-1)/D`, not the original false
product-sign four-wise-independence argument. T143 had already avoided relying
on that old claim. L69's complex-sketch bound is a constant-factor alternative;
neither establishes a cheap relative-error guarantee for the current source.

L85 changes the immediate action: propose an unchanged V29 reproduction before
another home-grown modification. The homogeneous-response and paired-fourth
derivations remain explicit reserves. The public author's broad claims about
exhausted methods or what leaderboard leaders must be doing are hypotheses,
not established consequences of their ablations.

See [candidate selection](../experiments/theory/t146/CANDIDATE_SELECTION.md),
[reserves](../experiments/theory/t146/RESERVES.md), and the
[route tracker](RESEARCH_ROUTE_STATUS.md). The research outcome is a nominee
and mathematical information; no retained submission gain has yet been measured
for T146. Category timing is recorded separately in the task's time log, and
the entire round is not attributed to each source or route.

T146 timing: **120.11 derivation,30.24 literature,30.14 selection minutes**;
**180.49 useful minutes**, **219.87 elapsed minutes through records**.
[Exclusive timing](../experiments/theory/t146/TIMING.json). Per-route and
per-source stopwatches were not recorded.


## T147 reproduction outcome for L85

The previously external V29 claim now has an independent project reproduction.
ALG043-V000 uses the unchanged source and defaults. Official submission
330597 returns adjusted 5.41905133451e-09, raw 2.13274181249e-08; local adjusted
gain 54.04% versus JSP on 12 reused networks. No local
fit or algorithm adaptation. This updates execution evidence. A brief owner-requested availability check during grading found no stronger released Phase 2 implementation; no new saturation estimate. [T147 report](../experiments/submission_policy/t147/REPORT.md).

## T148 — conditional metric and native response review, 2026-09-11 UTC

[Focused notes](../experiments/theory/t148/LITERATURE_NOTES.md) record30.10
active minutes, separately from121.19 derivation and30.14 selection minutes.
The16 local labels below include15 newly indexed unique sources and one
revisit: L110 is an alias of existing L38, retained only for traceability.
Selected sections were read; no full-paper audit or ready superior external
estimator is claimed. No challenge targets or candidate execution were used.

| ID | Primary source pointer | Relevant reading / boundary |
|---|---|---|
| L97 | [Burr, Elcock & Zhao, generalized signal/noise decomposition](https://arxiv.org/pdf/2408.13205) | Lemmas1–2 and Theorems2–3; non-Gaussian coefficients differ. |
| L98 | [Magnus, Gaussian quadratic-form products](https://janmagnus.nl/papers/JRM006.pdf) | Section2 theorem and fourth-product example; singular covariance allowed. |
| L99 | [Belrose & Rigg, converting MLPs to polynomials](https://arxiv.org/html/2502.01032v1) | Single hidden-layer conditional formulas; displayed formula inconsistencies and depth limits recorded. |
| L100 | [Yaida, finite-width non-Gaussian processes](https://proceedings.mlr.press/v107/yaida20a/yaida20a.pdf) | Sections2–3 and AppendixC.2; weight-averaged recurrence differs from supplied-network estimation. |
| L101 | [Lu, conditional Edgeworth response](https://arxiv.org/html/2303.02859v2) | SectionsIII.1–III.3 and AppendixB; no fixed-network implementation imported. |
| L102 | [Chen et al., covariance shrinkage](https://arxiv.org/html/0907.4698) | Oracle/Rao–Blackwell formulas and Haar moments; population-covariance dominance does not transfer to Gram recovery. |
| L103 | [Wiens, spherical quadratic moments](https://sites.ualberta.ca/~dwiens/home%20page/pubs/moments.pdf) | Sections1–3; separate radial and angular moments. |
| L104 | [Toth & Turyshev, trace-free tensors](https://arxiv.org/html/2109.11743) | Trace/dual-metric construction; no free nonlinear recurrent closure. |
| L105 | [McCullagh, tensor methods in statistics](https://www.stat.uchicago.edu/~pmcc/tensorbook/edition2.pdf) | Sections5.4.4–5.6; mixed conditional cumulants and approximation scope. |
| L106 | [Darling, conditional nonlinear regression](https://statistics.berkeley.edu/sites/default/files/tech-reports/512.pdf) | Leading Gaussian observation assumptions; no direct substitute for quadratic conditioning. |
| L107 | [Sei & Kume, Bingham normalizer](https://arxiv.org/html/1304.7973) | Sections1,3,4; exponential tilt differs from exact quadratic conditioning. |
| L108 | [Gilitschenski et al., deterministic Bingham sampling](https://isas.iar.kit.edu/pdf/MFI2014_Gilitschenski.pdf) | SectionsII–IV; orientation dimension and moment-matching limits. |
| L109 | [Kume, Preston & Wood, joint quadratic constraints](https://pdfs.semanticscholar.org/c73f/174a9cdd13f67d844434d9dd7bfc41538da5.pdf) | Sections2–4; saddlepoint precision/accuracy hypotheses, primary paper through a mirror. |
| L110 = L38 | [Opper, Paquet & Winther](https://jmlr.org/papers/volume14/opper13a/opper13a.pdf) | Revisited sections3–6 and AppendixD; matching the actual approximation matters. Not a new unique source. |
| L111 | [Bun et al., general multiplicative matrix denoising](https://arxiv.org/html/1502.06736v2) | SectionsII,III-B,IV-B,V and transforms/replica construction; asymptotic Frobenius objective. |
| L112 | [Semerjian, low-degree matrix denoising](https://arxiv.org/html/2402.16719v2) | SectionsII.1,III,IV.2–IV.4; additive-noise coefficients not imported into our multiplicative problem. |

Revisits: L03 paper/source, L14 exact ReLU-invariance assumptions (upgraded
from abstract to theorems/proof scope), L31, L38, L44, L45, L70, L72 and L85.
L03's pinned source reports a small empirical exact-metric effect; its inspected
material gives no V29/width1024 paired result. This tempers the nominee's
forecast. The public lean B1/source-generator comparison distinguishes the
missing far-CT term from F69's adverse B2 intervention. The next decision is
an actual small score screen, not more generic source or shrinkage literature.
Scarano1993 and the inaccessible Ledoit–Wolf PDF remain located-only material.
[Candidate selection](../experiments/theory/t148/CANDIDATE_SELECTION.md).

## T153 — response-aware reduction and interleaved empirical theory,2026-09-12

30.36 active literature minutes;16 newly indexed sources plus selected revisits.
[Reading scope and transfer limits](../experiments/theory/t153/LITERATURE_NOTES.md).
These are selected-section readings, not16 complete paper audits. No new ready
superior ARC implementation was found. The actionable transfer is a native
future-response compression nominee, whose complete implementation is untested.

| ID | Primary source | Relevant reading / limitation |
|---|---|---|
| L113 | [Corbin & Kramer, nonlinear balanced truncation](https://arxiv.org/html/2604.23044) | Polynomial coordinates and finite-order composition; no automatic closure invariance. |
| L114 | [Alger, Chen & Ghattas, tensor trains from actions](https://arxiv.org/pdf/2002.06244) | Algorithms1–2; action access helps, rank-dependent cost remains. |
| L115 | [Pellegrino et al., SliceTCA](https://www.nature.com/articles/s41593-024-01626-2) | Vector–matrix components and nonuniqueness; no ARC rank guarantee. |
| L116 | [Cui & Scalone, stochastic conservative low-rank schemes](https://arxiv.org/html/2608.00397v1) | Scheme-specific preservation conditions; a continuous symmetry need not survive truncation. |
| L117 | [Guo & Qiu, conservative low-rank Vlasov method](https://arxiv.org/pdf/2201.10397) | Protected moment sector and remainder; does not preserve all future nonlinear queries. |
| L118 | [Sokolov et al., zero-mode tensor gauges](https://arxiv.org/html/2508.00338v1) | Environment-weighted truncation; small local norm is insufficient. |
| L119 | [Phien et al., environment recycling](https://arxiv.org/html/1411.0391v2) | Reuse after gauge alignment; nearby-state assumptions differ from our dense finite rotations. |
| L120 | [Khoromskaia & Khoromskij, reduced HOSVD](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2022.826988/full) | Section2 bounds; relative stability requires structure absent from generic signed sources. |
| L121 | [Wan et al., neural control variates](https://arxiv.org/pdf/1806.00159) | Stein controls and train/test distinction; no free high-dimensional variance reduction. |
| L122 | [Minster, Li & Ballard, parallel randomized Tucker](https://arxiv.org/abs/2211.13028) | Sections4–5; structured sketch cost does not imply a small useful source rank. |
| L123 | [Amsel et al., query-efficient structured matrix learning](https://proceedings.mlr.press/v336/amsel26a.html) | Theorem1/Corollary3; approximation factor and family-size runtime limit direct transfer. |
| L124 | [Tropp et al., practical matrix sketches](https://web.stanford.edu/~udell/doc/TYUC18-More-Practical-TR.pdf) | Independent range/core sketches; spectral tail remains the obstacle. |
| L125 | [Yeon & Anitescu, low-rank plus diagonal](https://arxiv.org/html/2512.17120v1) | Selected local convergence algebra; notes preserve a scoped derivative counterexample. |
| L126 | [Kuang & Lin, exact Gaussian moments](https://arxiv.org/html/2601.22307v2) | Gaussian-layer exactness is not non-Gaussian propagation; smooth/small-variance theorem limits. Already mentioned in public findings. |
| L127 | [Chen et al., conditional Bayesian quadrature](https://proceedings.mlr.press/v244/chen24b.html) | Sections2–4; kernel cost and high smoothness assumptions require a useful conditional reduction first. |
| L128 | [Torop et al., SmoothHess](https://arxiv.org/abs/2311.00858) | Smoothed-Hessian gradient identity; its direct homogeneous trace reduces to ordinary sampling here. |

Revisited L28/CoBRAS, L33 conservative reduction, L37/L38 expectation
consistency, L79 tensor environments, L85 public V29, and L10/L11 conditional
integration. L28's future-response view and the explicit native tensor metric
helped change the next action. P25–P28 support components of H153-NFC128;
no retained submission gain is yet attributable to this round. Conditional
integration, positive-cone states and compatible homogeneous conversion remain
open with concrete finite-state/cost gaps. [Decision](../experiments/theory/t153/CANDIDATE_SELECTION.md).

## T163 scoped collection — 2026-09-23

[T163 literature notes](../experiments/theory/t163/LITERATURE.md) contain
**task-local L01–L20**, not extensions of the global L001–L128 numbering above.
Reading scope and access limitations are recorded individually. The exclusive
literature clock totals23.22minutes within240.18active research minutes;
mathematical application and experiments are counted separately.

The collection covers cumulant response, tensor actions and sketches,
source-aware basis augmentation, learned residual/control methods, and adjacent
conditional integration. The final adjacent sources include basis-update and
Galerkin methods, conditional neural Stein controls, geometric2Dintegration
and AutoInt. Their hypotheses and dimensional/cost limits prevent treating
them as ready ARC replacements. The useful transfers are source-aware basis
reuse and exact implicit query identities; the readyP67 nominee is our learned
adaptation of the existing cumulant estimator, not a newly copied public
submission. No claim of exhaustive literature coverage or academic priority.
[Scratchpad](../experiments/theory/t163/SCRATCHPAD.md),
[round result](../experiments/theory/t163/REPORT.md).

## T165 scoped collection — 2026-09-27

[T165 literature notes](../experiments/theory/t165/LITERATURE.md) record
**task-localL01–L23**, including repeats and explicit reading scopes; these do
not extend the global numbering. Exclusive literature time30.86minutes within
241.72active research minutes. Topics include cross interpolation, constrained
and augmented bases, symmetric tensor metrics/representation freedom, memory
closures, unbiased compression, conditional integration, learned controls,
EP corrections and pairwise dynamical mean fields.

Useful transfers produced source projection/query identities and finite tests,
not a ready public successor. The public ancestor's September22 clarification
changed documentation only. Ensemble-over-weights formulas, positive-law
assumptions and dimension/cost conditions were not silently transferred to
fixed-weight ARC. One advertised tensor-sketch variance bound has an apparent
small scalar-sketch counterexample, retained as a scoped caution rather than
an accusation about the entire method. No corpus download, external message,
exhaustive-best-method claim or academic novelty claim. No nominee this round.
[Report](../experiments/theory/t165/REPORT.md),
[continuation](../experiments/theory/t165/CONTINUATION.md).

## T166 literature refresh — 2026-09-27

[Task-local L01–L26 notes](../experiments/theory/t166/LITERATURE.md) cover
learned closures and trajectory supervision, non-Markov reduced states,
interpolatory tensor methods, angular/self-normalized laws, Gaussian function
controls and finite-width cumulants. Each note states the actual reading scope
and transfer limitation;26 entries do not mean26 complete papers were read.
The review informed intermediate supervision and alternatives to full tensor
construction; it did not identify a turnkey new ARC submission.

## T169 focused constructor cross-check — 2026-10-09

[Task-local L01–L05](../experiments/theory/t169/LITERATURE.md) record a brief
primary-source check of ICA sketches, higher-order Count Sketch, harmonic
factorization, conservative LoMaC truncation and the public V29 README.
Reading scope and transfer limits are explicit. No ready published replacement
or exhaustive-best-method claim; preservation of selected observables does not
establish accuracy of the underlying ARC closure. No protocol change.

## T170 refresh — 2026-10-11

[Task-local L01–L22](../experiments/theory/t170/LITERATURE.md) cover public
challenge implementations, operator/conditional moment corrections, source
quadrature, tensor sketches, implicit moments, goal-oriented compression and
adjacent low-rank representations. Reading scopes and transfer limits are
explicit;22entries do not mean22complete papers. Known Hermite covariance
series made the native mixed closure affordable. October4public deeper-leaf
measurements add a narrow engineering reserve, not a reproduced new method.
An organizer attribution clarification and an unanswered lifecycle question are
recorded separately from algorithm evidence. No exhaustive best-method claim.

## T172 — October 17 final broad recurrence

[Primary-source notes](../experiments/theory/t172/LITERATURE.md) cover the current
evaluator/deadline announcement, the public lower-cost LordProcciuto engine,
scale extraction, the third-order boundary analysis, two-term K31, and the
organizer's reuse clarification. The public cost engine was empirically useful;
our covariance and learned mean adaptations were combined with it in three
official improvements. Research fourth-core capacity and cost limitations are
separated in the [task report](../experiments/theory/t172/REPORT.md).
