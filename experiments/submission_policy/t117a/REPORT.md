# T117A — qualify and officially evaluate ALG024-V000

## Outcome

**`ALG024-V000` is now the best officially graded project submission.**
Replacement submission `329529` graded successfully at adjusted score
`1.7153829685412346e-7`, final-layer MSE `1.7153829685412347e-6`, and
approximately `6.995522x` versus sampling.

Against prior official best `ALG019-V000` submission `328762`, the adjusted
ratio is `.714862548`, a **28.513745% official reduction**. The official score
is 2.558768% lower than T117's prospective Full V_O estimate. Both use the
`.1` score multiplier.

## Qualification, rejection, and repair

The exact original T117 archive passed Windows-native `whest validate`,
`validate-package`, clean extraction, full `16 x 1024` deterministic replay,
exact T117 prediction parity, cost, residual time, and memory checks. Initial
submission `329528` nevertheless failed before evaluation because
`estimator.py` imported raw NumPy to materialize twelve fixed coefficients.
The Phase-2 rules prohibit and omit NumPy. This was a package-compliance defect
missed by the local validator, not an algorithm result or transient failure.

The repair removed the raw import and represented the same constants as a
pure-Python tuple converted through `flopscope.numpy`. The repaired archive has
SHA-256 `4353f9cd6d50143bba7591cf158d6fe745afaa7c8a05279b356e0fc7bce42378`.
It reproduces T117's sealed prediction byte-for-byte. Exact cost rises by only
24 lawful FLOPs, from `219,827,350,403` to `219,827,350,427`; the multiplier
remains `.1`. Two extracted-archive runs were byte-identical, used the exact
new cost, had residual times `.2982s/.2920s`, and stayed below the 8 GiB
process-memory cap at 4.780 GB peak working set. Static prohibited-import,
contract, manifest, finite/nonnegative, wall, budget, and package gates pass.

## Scientific and workflow disposition

The official grade establishes competition succession but transfers no
scientific tier. ALG024 retains T117 current-shape M1 and N1/dimension-4
provenance; historical P1 and rigorous science remain `NOT-RUN`/deferred.
No final entry was designated. V_D rows 750--849 and H rows 850--999 remain
untouched. T118 is next and starts from ALG024 as both local and official
incumbent.

## Timing

- Start: `2026-09-02T13:47:43,751744798-07:00`
- Pre-task estimate: **45 minutes** (planning range 20--90 minutes)
- End/checkoff: `2026-09-02T14:06:57,579181804-07:00`
- Actual elapsed: `00:19:13.828455258` (`1153828455258` ns)
- Estimate difference: completed `00:25:46.171544742` earlier than estimated
