# ALG053-V000 — quadratic mixed-cumulant covariance correction

Based on 504aldo's MIT-licensed public V29 estimator, through our ALG052:
https://github.com/504aldo/whest-p2-cumulant-k3
Original public source commit:18c17e2d7a9aeacd399cfc2c6b571e4e16dbfb45.
Original notices and LICENSE are retained.

Our addition is a physical covariance-defect update:32 analytic directions
in3layer bins, with96fixed ridge coefficients fitted on permitted training
networks using intermediate and final mean-response objectives. Directions
include marginal third/fourth, mixed21/22/31 and quadratic third-cumulant terms.
The Gaussian covariance reference uses eight Hermite terms. Retains our existing
644-parameter intermediate-supervised neural mean-response asset and prior
trace, interface and Winograd adaptations. This is not a claim of independent
invention of cumulant propagation, Hermite series or learned closures.

All numerical inference uses accounted flopscope APIs. JSON/pathlib load the
fixed neural asset during setup. No challenge weights, labels, network IDs or
sampling seeds are bundled. Exact source/asset from T170P49; no T171refit.
