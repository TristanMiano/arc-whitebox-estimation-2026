# T096A — qualify and officially grade ALG015-V000

T096A is complete. Under the owner's explicit authorization, the exact
T096 realization passed the independent Phase 2 hard package/runtime gate,
was uploaded once, and reached the terminal `graded` state as submission
`328500`.

| metric | `ALG015-V000` | prior official best `ALG014-V003` | ratio / change |
|---|---:|---:|---:|
| adjusted score, lower is better | `2.843538175e-7` | `6.607199503e-7` | `0.430370`; **56.963% lower** |
| final-layer MSE | `2.843538175e-6` | `2.509378157e-6` | `1.133164`; 13.316% higher |
| vs sampling approximation | `4.220095x` | `1.816201x` | `2.3236x` as large |

**`ALG015-V000` beat our prior best officially graded submission and is now
our official Phase 2 submission candidate.** The raw MSE is modestly worse
than `ALG014-V003`, but the contest's adjusted score rewards the much lower
fully charged compute: `ALG015-V000` stays on the `0.1` score floor at
`196,459,652,235` FLOPs, versus the predecessor's `0.263293` multiplier and
`578,986,643,120` FLOPs. The official adjusted score was only 2.84% above
T096's prospective public-cohort estimate, so the official result closely
confirmed the predicted direction and scale.

## Qualification and identity

The submitted archive is
`experiments/submission_policy/t096a/packages/ALG015-V000.tar.gz`, SHA-256
`9591d5fdcc316e7d7e08aa7c57f2514ad64127e3b3336965690e16f023dc1bda`,
size 3,011 bytes. Its manifest binds estimator SHA-256
`4b0f219c144da6be977098ad863f4650dc8ada647999d289a3705d3296f6e53d`
and the MIT license.

The current contract and package validators passed. From a fresh extraction,
two fixed-seed runs reproduced prediction hash `f317089e...` and exactly
`196,459,652,235` FLOPs. The same extracted file scored the shared public
Phase 2 smoke MLP in local and isolated-subprocess modes with zero failures,
identical adjusted score `2.782138154e-7`, maximum wall time `0.911` seconds,
and maximum residual time `0.0303` seconds.

The first packaging attempt used valid single-file mode and therefore omitted
the sibling license. This was detected before upload. The folder was
repackaged, the candidate bytes remained unchanged, and every qualification
check was rerun on the replacement archive. Only the replacement hash above
was uploaded.

## Scientific and contest disposition

Official grading changes submission-facing succession, not scientific tier.
`ALG015-V000` retains T096's current-shape M1 and its scientifically negative
historical adapter disposition; historical P1 remains not awarded. No final
submission was designated. T097 remains the next scientific task.

Timing: start `2026-08-26T00:09:06.963203926-07:00`; estimate `30 minutes`;
end/check-off `2026-08-26T00:23:01.290759282-07:00`; elapsed
`00:13:54.327555356` (`834327555356` ns).
