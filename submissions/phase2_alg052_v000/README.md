# ALG052-V000 — intermediate-supervised nonlinear mean source

Adapted from 504aldo's MIT-licensed public V29 estimator, commit
18c17e2d7a9aeacd399cfc2c6b571e4e16dbfb45:
https://github.com/504aldo/whest-p2-cumulant-k3

Retains the physical cumulant trajectory and ALG049/ALG050 changes. Replaces
ALG051's terminal linear correction with a frozen644-parameter neural local
source propagated as a mean-response vector. The weights and normalization in
nn_asset.json were fitted on32 permitted training networks, using intermediate
and final means. Training and labels are not included or used at inference.
All numerical inference uses charged flopscope.numpy. JSON is loaded in setup
from the submission directory. No network identifiers, challenge inputs or
sampling seeds are bundled. Source and weights exactly match T166 P45.
See the included LICENSE and the repository's T166/T167 evidence.
