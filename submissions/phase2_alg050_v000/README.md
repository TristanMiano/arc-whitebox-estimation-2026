# ALG050-V000 — partial nonlinear interface and young-coordinate packing

Based on 504aldo's MIT-licensed public V29 estimator at commit
18c17e2d7a9aeacd399cfc2c6b571e4e16dbfb45:
https://github.com/504aldo/whest-p2-cumulant-k3

This repository's ALG049 adds native lost-trace compensation and Winograd
arithmetic. T160 further restricts expensive nonlinear hub rows using |alpha|
<=2.5 with padding64, repairs the omitted semilinear trace by factor actions,
and packs young native coordinates with prior Gaussian gate>=.03 from layer5.
Native history, cheap thin slices and inherited calibration are retained.
All tested settings are already defaults. The estimator source is exactly the
selected T160 P25a research source; diagnostic numerical work is retained and
charged. No new target coefficient fit or bundled network inputs/targets.
See the included MIT LICENSE and repository T160/T161 records.
