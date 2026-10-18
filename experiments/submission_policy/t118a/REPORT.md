# T118A — qualify and officially evaluate ALG026-V000

## Outcome

**`ALG026-V000` is now the best officially graded project submission.**
Submission `329690` graded successfully at adjusted score
`1.4791658804824692e-7`, final-layer MSE `1.4791658804824692e-6`, and
approximately `8.112680x` versus sampling.

Against prior official best `ALG024-V000` submission `329529`, the adjusted
ratio is `.862294839`, a **13.770516% official reduction**. The official score
is 2.888974% below T118's prospective Full-H estimate. Both use the `.1`
score multiplier.

## Qualification and upload identity

The T118 archive was not rebuilt or retuned. The uploaded file is exactly
`packages/ALG026-V000.tar.gz`, SHA-256
`a1d66a380afd79e99411ac0ad564c6eba3cdb9939b5a1effb0b41f9d3a84eb9c`,
with exact charge `218,819,123,305` FLOPs.

WhestBench 0.16.0 accepted the archive manifest and contract. A clean Linux
qualification using WhestBench 0.16.0, FlopScope 0.12.0, Python 3.10.20, and
NumPy 2.2.6 passed full-shape, static-import, exact-cost, `.1` multiplier,
deterministic replay, byte-exact sealed-H parity, finite/nonnegative, wall,
memory, and residual checks. Residual times were `.3661s/.3565s`, and peak RSS
was 4.825 GB.

The separately preserved Windows-native result passed every check except the
`.4s` residual-time cap, reporting `.8657s/.8461s`. Repeated execution made
that a stable Windows timing incompatibility rather than a transient result.
The current-version Linux evaluator stack passed the same immutable bytes, so
the standing Windows-or-WSL containment rule supported upload. This exception
is explicit; it is not represented as a Windows pass.

## Monitoring and scientific disposition

The Windows CLI had no credential in its separate store, so no submission was
created by that first command. The authenticated WSL client then created only
submission `329690`. Its watch detached after ten minutes while the server
remained `submitted`; the owner directed a 15-minute cutoff followed by at
most one retry. The submission graded successfully just before that first
cutoff, so no duplicate/retry was created.

The official grade establishes competition succession only. ALG026 retains
T118 current-shape M1 and N1/dimension-4 provenance; historical P1 and rigorous
science remain `NOT-RUN`/deferred. No final two-entry designation was made.
`ALG025-V000` remains the mechanism-distinct packaged hedge.

Targeted JSON, CSV, archive-hash, and diff checks pass. The broad historical
`make verify` command remains red for unrelated Python-3.12 `type` statements
under `tmp/mlp_cumulant_propagation` when compiled by the workspace's Python
3.10 verifier; T118A did not modify that scratch dependency.

## Timing

Timing is recorded in `RESULT.json` and the T118A checkbox in `TODO.md` at the
instant of final checkoff.
