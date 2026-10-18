# ARC White-Box Estimation Challenge 2026

Research and submissions by **Tristan Miano** (`tristan_miano`), with extensive assistance from GPT-5.6 Sol, GPT-6 Astra and the other model contributions documented below.

The best retained public submission is **336809 / ALG058-V001**, with adjusted final-layer error **2.971106406126817e−9**. It combines the credited public factored-cumulant implementation with our fitted physical covariance correction and transported learned mean innovations. This is a public score, not a final private rank or prize decision.

## Read the work

- **[All 24 submitted algorithm writeups](writeups/README.md)** — method, provenance, results, exact source and accepted package for every graded version; failed attempts are also disclosed.
- **[How the research was done](docs/WORKFLOW_AND_MODEL_REPORT.md)** — human/model roles, task and TODO structure, protocol changes, theory versus fitting, delegation, failures and reproducible workflow prompts.
- **[Time between submissions](docs/SUBMISSION_TIMELINE.md)** — recorded sessions, active research, interruption exclusions, overlapping agent time and missing records; includes CSV/JSON data and a rebuild script.
- **[Final 12-page technical report](experiments/finalization/t174/writeup/arc-whestbench-phase2-336809.pdf)** and [LaTeX source](experiments/finalization/t174/writeup/main.tex) — associated with submission 336809. The earlier review draft is preserved.
- **[Reproduction guide](docs/REPRODUCTION.md)** — exact packages, runtime versions, local inference harness, evidence and report rebuilding, and explicit limits of the historical archive.

## Final candidates

| Role in the owner-approved selection | Algorithm | Submission | Official public adjusted error |
|---|---|---:|---:|
| Primary | [ALG058-V001](writeups/ALG058-V001.md) | 336809 | 2.971106406126817e−9 |
| Second | [ALG055-V000](writeups/ALG055-V000.md) | 336785 | 2.982822327838572e−9 |
| Reserve | [ALG054-V000](writeups/ALG054-V000.md) | 336778 | 3.0332910471237746e−9 |

The owner approved 336809 and 336785 on October 18, 2026. The owner has confirmed selecting nominations **336809 and 336785**. Forum publication remains pending. [Website instructions and prepared post](experiments/finalization/t174/OWNER_HANDOFF.md).

## Attribution and evidence

The theoretical foundation is the published cumulant/Hermite framework, including [Wu et al.](https://arxiv.org/abs/2605.05179v2). The immediate final implementation base is LordProcciuto's MIT-licensed [public estimator](https://github.com/siming767-creator/whestbench-lordprocciuto), derived from [504aldo's V29](https://github.com/504aldo/whest-p2-cumulant-k3). Original notices are retained. [Third-party notices](THIRD_PARTY_NOTICES.md) distinguish inherited work from local adaptations.

Most of the final **28.50% historical score reduction** came with the public lower-cost engine. Our complete adaptation improves adjusted error by **4.55%** on four reused development networks under the same meter; the mean-source addition improves the official score by **2.05%** over our covariance-only entry. These comparisons have different scopes. We do not claim the public engine's contribution as our own or claim academic priority for established methods.

## Release scope

This is a curated public snapshot of the local research repository. It includes exact graded packages and their required assets, method writeups, selected task reports, timing evidence, workflow snapshots, and the final report project. The original repository and Git history remain preserved locally. Raw network weights, labels, local caches, credentials and bulky experimental binaries are excluded. Some archived report links refer to that larger workspace; the reproduction guide identifies what can be rerun directly from this release.

```bash
python3 tools/verify_release.py
python3 tools/build_reports.py
```

See [publication rules review](docs/PUBLICATION_RULES.md) and [MIT license](LICENSE). Original third-party licenses continue to apply to their code. This project is an independent participant's work, not an endorsement by ARC or AIcrowd.
