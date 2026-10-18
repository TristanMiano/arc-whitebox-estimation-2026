# Reproduction and release scope

This release supports exact access to the 24 retained graded packages, inspection of every submitted algorithm, recomputation of the effort tables, and rebuilding the final writeup's numerical evidence. It also exposes the research workflow and selected training scripts. It does not claim to be a one-command replay of every historical experiment or every model conversation.

## Verify the published files

```bash
git clone https://github.com/TristanMiano/arc-whitebox-estimation-2026.git
cd arc-whitebox-estimation-2026
python3 tools/verify_release.py
python3 tools/build_reports.py
```

The verifier checks the release manifest, each archive's recorded hash, archive members against their embedded manifests, and extracted source/assets against the same archived bytes. It does not run estimators, download challenge data or contact AIcrowd. The report builder uses only saved JSON records and the Python standard library.

The original research repository and its 224 pre-release commits were retained locally. This public repository begins with a curated snapshot. [Export origins](../evidence/export_origins.json) identify copied file paths, hashes and the source repository commit. Required sampling banks and fitted coefficients are shipped as solution assets; raw challenge network weights, labels, training caches, credentials, virtual environments and large experimental binaries are excluded.

## Run a submitted estimator

Use Python 3.12 on Linux/WSL and the official [WhestBench starter kit](https://github.com/AIcrowd/whest-starterkit) and [FlopScope](https://github.com/AIcrowd/flopscope). The final packages were qualified with Python 3.12.3, WhestBench 0.16.2, FlopScope 0.12.3 and NumPy 2.2.6. The official kit supplies the compatible metering server. Older packages retain their own recorded runtime versions in `manifest.json`; do not assume a current meter reproduces historical charges.

For the final package:

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install whestbench==0.16.2 flopscope==0.12.3 numpy==2.2.6
.venv/bin/whest validate --estimator submissions/phase2_alg058_v001/estimator.py --json
```

Validation alone is not a full-width benchmark. The retained package is [ALG058-V001.tar.gz](../packages/ALG058-V001.tar.gz); the [manifest](../submissions/phase2_alg058_v001/manifest.json) records its entrypoint, runtime and file hashes. For inference, `Estimator.setup(SetupContext(...))` runs once, followed by `Estimator.predict(mlp, flop_budget)` for each supplied `MLP`, inside the official meter. Preserve this natural call lifecycle and the package's supporting files. The full-shape contract is width1024, depth16, budget `2**41`; all meaningful inference computation must be charged through FlopScope. The saved final qualification used a 120-second call cap, 400ms residual cap, 5-second setup cap and 8GiB memory cap.

`tools/run_public_row.py` provides a concrete local harness for an **already downloaded public dataset row**. It accepts a row saved as an NPZ containing `weights` and `mlp_seed`, uses the proper setup/predict lifecycle and records the real meter. It is not a generator of private evaluation inputs. See its `--help`. The example harness is additional release tooling; the qualified estimator bytes remain unchanged.

The scripts under `experiments/...` are preserved historical implementations, with original workspace paths and assumptions. In particular, `run_probe.py` and the training scripts expect local public-data caches that are not included. They are useful for inspecting the precise method, not advertised as immediately runnable on an empty clone. Follow the official kit for obtaining permitted public examples and account access; no credentials are embedded here.

## Public data and training

The development/training source was the organizer's [aicrowd/arc-whestbench-public-2026 dataset](https://huggingface.co/datasets/aicrowd/arc-whestbench-public-2026). The layer-label source manifest used revision `ce926b7d1ced65faa668c01b94a43f8c4f43783d`. Training and development row positions are listed in the writeup appendix and `WRITEUP_EVIDENCE.json`. The original 32 training positions are contained within the later 64; the twelve submission-comparison positions are disjoint from those training positions but were adaptively exposed during research.

The final estimator requires only its shipped coefficients and `nn_asset.json`, not training labels or network-specific lookup data. The 96 covariance coefficients equal the saved T170 fit. The merged mean asset preserves two independent normalizers, clipping, hidden layers and a fixed equal average. The evidence builder checks these identities without running training.

Preserved method scripts include:

- [Covariance fit](../experiments/theory/t170/fit_quadratic.py) and [fit output](../experiments/theory/t170/P27_FIT/RESULT.json).
- [32-network source training](../experiments/theory/t172/train_source.py) and [64-network source training](../experiments/theory/t172/train_expanded_source.py).
- [Fixed-average batching construction](../experiments/theory/t172/build_anchor_merged.py), with the two source assets retained.

To rerun fitting, reconstruct the specified public rows and intermediate feature/response captures, retain the recorded fold assignments/seeds/objective, then run those scripts in their expected directory layout. PyTorch is used offline for fitting, not by the submitted inference algorithm. This release does not include all intermediate captures or a complete cache-restoration pipeline; retraining every historical experiment from this snapshot therefore requires additional setup. No claim of complete end-to-end retraining reproduction is made. The accepted inference packages and report evidence can be reproduced independently of that missing cache layer.

## Rebuild the final report

The final report is linked to exactly one accepted submission: **336809**. The T173 review draft remains preserved; T174 contains the final source and PDF. The additional algorithm pages are retrospective history, not separate formal prize submissions.

```bash
.venv/bin/python -m pip install matplotlib
.venv/bin/python experiments/finalization/t173/build_evidence.py
.venv/bin/python experiments/finalization/t173/build_figures.py
# Install Tectonic 0.17.0 and DejaVu Serif/Sans fonts, then:
.venv/bin/python experiments/finalization/t174/build_pdf.py
```

The source is [main.tex](../experiments/finalization/t174/writeup/main.tex), with [appendix.tex](../experiments/finalization/t174/writeup/appendix.tex) and included vector figures. Evidence rebuilding verifies source/asset identities and recomputes the quoted comparisons from preserved records. PDF compilation can differ in byte identity between environments; the committed PDF has its own hash. The final document check used Tectonic 0.17.0, checked all 12 pages for text bounds and missing references, and visually inspected the changed pages. Optional validation requires PyMuPDF: run `python experiments/finalization/t174/validate_final.py` after compilation. T173 evidence/figure rebuilding validates the preserved comparisons; T174 retains identical vector figures and its own hashes.

## Historical evidence boundaries

Historical reports are retained under their original paths to make the evolution and failures inspectable. Some refer to files outside this curated release, to untested hypotheses, or to obsolete policies. An absent old artifact is not evidence that an experiment passed, and an old conclusion is not a statement about the current best algorithm. The new index, individual writeups, timeline and workflow report are the supported entry points.

The release verifies identities and document arithmetic. It does not rerun every expensive benchmark, claim access to the organizer's private final networks, guarantee a leaderboard rank, or establish academic novelty. Final prize eligibility and private evaluation remain organizer decisions.
