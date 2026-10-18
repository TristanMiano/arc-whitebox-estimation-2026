# ALG051-V000 — marginal-and-pair propagated residual

Based on 504aldo's MIT-licensed public V29 estimator at commit
18c17e2d7a9aeacd399cfc2c6b571e4e16dbfb45:
https://github.com/504aldo/whest-p2-cumulant-k3

This repository's ALG049 adds trace compensation and Winograd arithmetic;
ALG050 adds a trace-repaired partial nonlinear interface and young-coordinate
packing. ALG051 adds124 frozen learned coefficients on marginal and pair-state
features, propagated as one mean-response vector. Coefficients were fitted on
32 permitted training networks with whole-network cross-validation. No row
identifiers, seeds or challenge inputs/targets are bundled. The physical state
and first15 outputs remain unchanged. The shape-generic path remains available.
This estimator is exactly the T163 P67 research source, including charged
numerical diagnostics. No refitting or configuration override is part of T164.
See the included MIT LICENSE and repository T163/T164 records.
