# Claim and provenance audit for the 336809 writeup

The public-facing draft is `writeup/main.tex` plus `appendix.tex`; the compiled PDF is `writeup/arc-whestbench-phase2-336809-draft.pdf`. This internal index separates documentary checks from new experiments. T173 performs no new model inference or fitting.

| Claim | Evidence | Scope / qualification |
|---|---|---|
| Current adjusted2.971106406126817e-9 and raw1.9446764376596092e-8 | `CURRENT_GRADES.json`, T172 `ALG058-V001/OFFICIAL_RESULT.json` | Official public grade, not final private rank |
| Source and assets are the accepted qualified bytes | `PACKAGE_IDENTITY_AUDIT.json` | Local archive and qualification/upload hashes; no claim of downloading the server's archive |
| Own adaptation gives4.5478% adjusted gain over public engine | `WRITEUP_EVIDENCE.json:matched_four` | Four adaptively reused exposed networks, same current runtime |
| Overall historical gain28.5038% | T172 `OFFICIAL_GAIN_DECOMPOSITION.json` | Includes public engine and historical meter differences; not our isolated contribution |
| Mean sources give2.0501% official gain over covariance-only | Official336809 versus336778 | Three official grades on current evaluator; not an official ablation of the public engine |
| All96 covariance coefficients are unchanged from the T170 all32fit | `build_evidence.py`, `WRITEUP_EVIDENCE.json:covariance_asset` | AST extraction and exact array equality; source grouping can alter rounding |
| Covariance is added to the physical trajectory | Accepted `estimator.py`, lines3540–3542 | Alters covariance and stored variance; subsequent feedback is part of the full recurrence |
| Mean response is separate and added at final layer | Accepted source, lines3287–3311 | Gaussian gate is an approximate response model; intermediate returned outputs remain physical |
| Source training uses32and64networks | Original fit records and asset identities | The64include the32; covariance fit already used original32, making CV conditional |
| Two models' normalizers and clipping are preserved | `build_evidence.py:mean_asset` and T172 `P82_MERGE_IDENTITY.json` | Exact block/normalizer construction; mathematical equivalence is not old/new float32 byte equality |
| Shipped package passes byte replay | T172 `ALG058-V001/QUALIFICATION.json` and final pipeline | Separate claim from batch equivalence |
| More fourth-moment information has raw capacity but current cost obstacle | T172 report, `P80_G_COST.json`, `P80_COST_INTERPRETATION.json` | Two-row research accuracy and separate kernel cost projection; not an integrated score or impossibility result |

## Public foundations

- Wu, Lecomte, Winer, Robinson, Hilton and Christiano, arXiv2605.05179v2: cumulant/Hermite framework. Do not attribute this framework to our project.
- 504aldo's MIT V29: factored third history, fourth regeneration, source compression and efficient transport. Earlier project reuse was an unmodified published reproduction.
- LordProcciuto's MIT e30_a, commit3d038e9f48a97671878ee7bbef02e193f128b61c: the immediate public implementation, fixed bases/pruning/core cost engineering and existing87-feature fitted correction. This supplied most of the last historical score gain.
- Our additions: the specific32-field/96-coefficient physical covariance defect model, its fused evaluation, local learned mean innovations, and normalization-preserving fixed average.

The covariance field shapes use known cumulant/response identities. Their fitted amplitudes approximate a residual and are not proofs that an exact missing diagram was identified. The report makes no academic-priority claim. Generalization of the learned sources, the reason averaging helps, and all private-ranking outcomes remain empirical or uncertain.

## Human / model attribution

Author byline confirmed by the user: **Tristan Miano**. Public AIcrowd submission page identifies **tristan_miano**. The report discloses extensive LLM code, derivation, experiment, and drafting work; it does not imply the human manually wrote or independently proved every part. The author-review status remains visible on every draft PDF page.
