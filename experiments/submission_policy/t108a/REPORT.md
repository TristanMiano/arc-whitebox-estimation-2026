# T108A — qualify and officially evaluate ALG019-V000 / H107-O

## Result

**`ALG019-V000` is now the best officially graded project submission.** The
single owner-authorized live upload is AIcrowd submission `328762`. It graded
successfully at adjusted score `2.3995983178792816e-7`, final-layer MSE
`2.399598317879281e-6`, and `5.000837x` versus the Phase-2 sampling
approximation.

Against prior official best `ALG018-V000` submission `328686`, the adjusted
score ratio is `.891001532`: a **10.899847% official reduction**. Both entries
use the `.1` score multiplier, so the raw final-layer-MSE ratio is the same.
The official result was `2.091866%` lower than T108's prospective
`2.4508671800218226e-7` estimate, confirming and slightly exceeding the local
forecast.

## Preparation and hard gate

The immutable archive is
`experiments/submission_policy/t108a/packages/ALG019-V000.tar.gz`, SHA-256
`cf95929aaf2f76b35f0c5374339943ffbcceeaf0a7617b0d6ff56ccc3887bb7a`,
size 4,721 bytes. It is byte-identical to T108's already qualified archive and
binds estimator SHA-256
`74879a41f02313096a02b58684f9fa795af94b0827763aad045b4225606efec6`.
The manifest records Python 3.10.20, WhestBench 0.16.0, flopscope 0.12.0, and
NumPy 2.2.6.

The estimator contract and complete archive manifest were rerun under Windows
native immediately before upload and both passed. T108's exact frozen package
had already passed target-blind invariants, repeated deterministic prediction
and FLOP checks, contract/archive checks, graceful fallback, resource limits,
and the true budget. It uses `219,788,985,209` FLOPs, retains the `.1`
multiplier with `113,340,346.2` FLOPs of floor headroom, and had maximum
observed residual time `.194881s`, wall time `2.588052s`, and process peak
working set `311,115,776` bytes.

After the Windows reboot, two uploader invocations stopped locally before
contacting AIcrowd because the native child process could not see the existing
credential stored in WSL: the first also required completing a local terminal
handshake, and a direct environment assignment on the second was not propagated
by WSL interop. A dummy-value probe identified the missing `WSLENV` bridge.
The existing credential was then passed to the unchanged native process in
memory, without displaying or copying it. The next invocation created exactly
one live submission and watched it to its successful grade. These were
operational environment repairs, not candidate evidence.

## Official and scientific disposition

Submission `328762` replaces `ALG018-V000` submission `328686` as the best
officially graded project entry and agrees with T108's positive local
succession. The official grade transfers no scientific tier: ALG019-V000
retains current-shape M1, while historical P1 and rigorous scientific testing
remain `NOT-RUN`/deferred rather than failed. No final Phase-2 designation was
made. T109/FC008 remains next.

Timing: start `2026-08-28T08:31:17,357330906-07:00`; estimate `25 minutes`;
final checkoff `2026-08-28T08:53:10,257795860-07:00`; actual elapsed
`00:21:52.900464954` (`1312900464954` ns).
