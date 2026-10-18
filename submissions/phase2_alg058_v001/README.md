# ALG058-V001: covariance-corrected fixed-basis cumulant estimator

Built during T172 from P82_anchor_merged. Source/provenance and full experiment records:
experiments/theory/t172/. This is an LLM-assisted research adaptation.

Public base: LordProcciuto e30_a, MIT, repository
https://github.com/siming767-creator/whestbench-lordprocciuto,
commit3d038e9f48a97671878ee7bbef02e193f128b61c; derived from504aldo's MIT V29.
The source header and LICENSE preserve both copyright notices.

Our contribution: a32-field physical covariance-defect dictionary containing
marginal, mixed and quadratic third-cumulant terms,96fixed coefficients in
three layer bins, fitted in T170 on32public training networks; an independent
low-rank-kernel regrouping in T172 reduces Python overhead and arithmetic.
This modifies the covariance trajectory, rather than only rescaling output.
The source's existing87-feature mean table and physical compaction/fixed-basis
engine are the public authors' work. No academic-priority claim is made.
Additional changes, if any, are identified by the selected probe configuration.

All inference array work uses flopscope. Data used for research were exposed
public development/training inputs. No final private-suite data were accessed.
Organizer topic18240 requires substantial own changes for final eligibility;
this disclosure describes the contribution without claiming advance approval.

The batched evaluation uses72 normalized coordinates and64 hidden tanh units,
combining a48-input/32-unit primary model and a24-input/32-unit secondary model.

Additional T172 contribution: a fitted local mean-innovation source
with 4 depth heads. It uses marginal moments and nine signed mean/trace
projections, fitted on 64 public training networks. A single
mean-response vector transports those local corrections through the known
weights and Gaussian gates. It is added to the final prediction while the
physical covariance trajectory retains the ALG054 model. The asset is fixed
before this package comparison; no evaluator data or per-network tuning.
Network-wide means of the local features condition the source. The exact selected probe CONFIG and training records describe its features and objective.

A second, unchanged24-input/32-hidden-unit trace source from ALG055 (trained on32 networks) is averaged equally with the64-network context source. Both retain their own normalization and clipping. No mixing weight or new model is fitted; there are64 hidden units in total.

The two source models are evaluated in one batched layer:72 normalized coordinates (including repeated local features) preserve both original normalization/clipping rules; a block-diagonal64-unit hidden layer and equally weighted output combine them. This changes evaluation order, not fitted coefficients or mixture weights.
