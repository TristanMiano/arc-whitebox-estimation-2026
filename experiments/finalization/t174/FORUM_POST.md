I am submitting this Phase 2 technical writeup for **submission 336809 (ALG058-V001)**, successfully graded on 17 October 2026. This writeup corresponds to that submission only.

**Author:** Tristan Miano (AIcrowd: `tristan_miano`).

- [Final technical writeup (PDF, 12 pages)](https://github.com/TristanMiano/arc-whitebox-estimation-2026/raw/refs/heads/main/experiments/finalization/t174/writeup/arc-whestbench-phase2-336809.pdf)
- [Public code, exact accepted packages, and research evidence](https://github.com/TristanMiano/arc-whitebox-estimation-2026)
- [Research workflow, model/agent disclosure, and task structure](https://github.com/TristanMiano/arc-whitebox-estimation-2026/blob/main/docs/WORKFLOW_AND_MODEL_REPORT.md)
- [Recorded work between submissions](https://github.com/TristanMiano/arc-whitebox-estimation-2026/blob/main/docs/SUBMISSION_TIMELINE.md)

The public adjusted score is **2.971106406126817e-9**, with raw final-layer MSE **1.9446764376596092e-8**. Final private evaluation has not yet occurred.

The estimator builds on LordProcciuto's MIT-licensed `e30_a` engine, derived from 504aldo's V29. Our additions are a fitted covariance-defect dictionary inside the physical recurrence and learned local mean innovations transported through a separate response recurrence. The final estimator averages two fixed innovation sources while preserving their individual normalizations and clipping.

Our complete adaptation improved adjusted error by **4.55% on four exposed development networks** relative to the unmodified public engine under the same FLOP meter. The mean-source addition improved the official score by **2.05%** over our covariance-only entry. These comparisons have different scopes; most of the larger historical improvement over our earlier incumbent came from adopting the public lower-cost engine. The report distinguishes inherited work, local adaptations, fitting, reused development evidence, negative results, and explanations that remain hypotheses.

LLM agents performed most code writing, mathematical exploration, experiment orchestration, literature review, and drafting. Substantial earlier work used GPT-5.6 Sol; later work primarily used **GPT-6 Astra at extra-high effort, locally through the ChatGPT Desktop application**. An Ultra-effort trial used parallel sub-agents, with smaller Fable and Opus contributions. I set the objectives, directed the strategy, authorized tasks and submissions, and reviewed progress. The repository documents this workflow and its reproduction limits in detail.

The accepted code tarball remains unchanged; its SHA-256 is `2c28711f6d44709182886eb6e1535503af415ecd97721b46868b39f2ff0660db`. Both upstream MIT notices are preserved. Thank you to the original authors and the challenge organizers.
