# Attribution and licenses

Project-authored code and documentation are released under the root MIT license, copyright2026 Tristan Miano and contributors. “Project-authored” includes extensively AI-assisted work. Existing third-party code retains its own notices and license terms; the root notice does not replace those rights.

## Published foundations and implementations

- **504aldo**, MIT [whest-p2-cumulant-k3](https://github.com/504aldo/whest-p2-cumulant-k3): public V29 factored third-cumulant history, fourth regeneration, compression, transport and calibrated tables. ALG043-V000 is the unchanged numerical reproduction at commit`18c17e2d7a9aeacd399cfc2c6b571e4e16dbfb45`; later variants adapt this lineage. MIT notices are in the relevant submission directories and packages.
- **LordProcciuto**, MIT [whestbench-lordprocciuto](https://github.com/siming767-creator/whestbench-lordprocciuto), final base commit`3d038e9f48a97671878ee7bbef02e193f128b61c`: lower-cost e30_a fixed-basis/compaction engine and existing fitted mean table, derived from504aldo. The final packages retain both copyright notices and the inherited ALG053 license.
- **Kellen Heraty's MIT public fast multiplication kernels** used in the earlier project lineage retain their `PUBLIC_FAST_LICENSE` files. Their algorithmic ideas and licensed implementation are inherited, not invented by this project. Inspect the notices beside the exact archived source for the applicable attribution.
- **venture_agent_ai public features**, transferred in ALG036 and retained/refitted in ALG037: the five absolute-state feature vocabulary is credited in those writeups and specifications. This was feature transfer into our estimator, not authorship of the public vocabulary or copying an entire estimator.
- **Wu, Lecomte, Winer, Robinson, Hilton and Christiano**, [arXiv2605.05179v2](https://arxiv.org/abs/2605.05179v2): published cumulant/Hermite estimation framework. This theoretical foundation is not claimed as a project invention.
- **ARC / AIcrowd**, [WhestBench](https://github.com/AIcrowd/whest-starterkit) and [FlopScope](https://github.com/AIcrowd/flopscope): external benchmark/API/metering dependencies. Their runtime distributions and challenge datasets are not relicensed or bundled here.

Established Sobol sampling, Haar frames, Gaussian closure, Price/Hermite identities, Edgeworth expansions, Winograd multiplication and supervised-learning methods are credited as established ingredients. A local combination or implementation does not establish academic priority.

## Project adaptations

Individual [submitted-method writeups](writeups/README.md) identify what changed at each step, ranging from unchanged public reproduction, to implementation-only changes and fitted calibration, to recurrence changes. The final local additions are the32-field/96-coefficient physical covariance-defect correction, fused evaluation, small local mean-innovation sources and normalization-preserving fixed averaging.

The exact accepted archives are retained without modification. An early archive that omitted a project license is accompanied by a release-level license in its extracted directory; this adds permission without changing the accepted bytes. The [package identity evidence](evidence/package_identity.json) and verifier check all archived source/asset bytes.

## Model and human attribution

GPT-5.6 Sol did much of the earlier work. Later work primarily used GPT-6 Astra at extra-high effort locally through the ChatGPT Desktop application, with a recorded Ultra/sub-agent trial and smaller Fable/Opus contributions. The [workflow report](docs/WORKFLOW_AND_MODEL_REPORT.md) explains the evidence and limits of this attribution. Tristan Miano directed the project and retains responsibility for the report.

Licensing, originality, and competition eligibility are separate questions. Public release and successful grading do not prove that the organizer's substantial-contribution requirement has been met.
