# ALG049-V000 — trace-compensated native history and Winograd arithmetic

Based on 504aldo's MIT-licensed public V29 estimator at commit
18c17e2d7a9aeacd399cfc2c6b571e4e16dbfb45:
https://github.com/504aldo/whest-p2-cumulant-k3

Repository adaptations retain a coupled native A/P range and carry the lost
principal third-tensor trace in a cheap covariance-cup residual after compression.
The native outer/nested ranks are320/192; ages and author calibration remain.
Matrix products use the classical15-addition Winograd identities with shared
scratch arenas, depth6 and minimum block16, retaining the original first-call
shallow safeguard. Diagnostic scalar arithmetic is retained and charged.
There are no new fitted coefficients or bundled network inputs/targets.

This is T158 P26 with its four tested settings encoded as shipping defaults,
including the covariance-product depth fallback. See the included MIT LICENSE.
