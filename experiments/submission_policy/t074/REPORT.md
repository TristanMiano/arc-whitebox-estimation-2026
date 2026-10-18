# T074 — two Phase 2 submission-evaluation lanes

T074 is complete. Both exact archives pass the current Phase 2 hard compliance
and operational gate and are ready for the separately owner-authorized T075
upload. No upload was performed.

## Current contract pin

The official starter kit was refreshed to commit
`35164f3535c2103742772dd11a68ce840464db0b`, which pins WhestBench `0.16.0`
and flopscope `0.12.0`. The acceptance environment was disposable Windows
native Python `3.10.20`, NumPy `2.2.6`, with UTF-8 mode enabled for the CLI.
The current public dataset declaration is
`hf://aicrowd/arc-whestbench-public-2026@v2-phase2`, report SHA-256
`aab61cf11271d20118e2109065c165a931dfac493849f0d611f7a2d82a03790`.
The owner-provided rule and submission-instruction hashes remain unchanged.

The tested hard limits are width `1024`, depth `16`, finite `16 x 1024`
output, `2^41` analytical FLOPs, 120 seconds wall time, 400 milliseconds
residual time, eight GB memory, five seconds setup, and 50 MiB package size.

## New realization identities

| realization | parent / status | material Phase 2 realization change | archive SHA-256 |
|---|---|---|---|
| `ALG003-V009` | `ALG003-V008`; N0 fallback; U0 | one 8,192-row int8 scrambled-Sobol bank, row restoration/renormalization, width 1024/depth 16 | `6ecf8418f621af41e134ec7ea71a319817b11242881ce873de6cdaccee74cb7f` |
| `ALG014-V003` | `ALG014-V000`; N1 candidate; U0 | four grader-seeded 2,048-row flopscope Gaussian-QR frames, 8,192 positive pairs, width 1024/depth 16 | `f69e0762d637ca2f253316e6bb5e18b39403ba3d2d7776a3c1c028977e67cce9` |

Both preserve antipodal pairing, exact mean-chi radius, and exact layer-one
Gaussian-ReLU means. The packages contain MIT licenses. The fallback's asset
is generated offline by `scripts/generate_phase2_sobol_int8.py`; its hash and
generation parameters are bound in the spec. All candidate-time numerical
work uses the allowed flopscope surface. The validator also exercises a
finite, correctly shaped low-budget graceful fallback.

The Phase 1 historical P1 of `ALG014-V000` does **not** transfer to
`ALG014-V003`; both new identities are U0 until independently tested. This
translation task changes no scientific tier and does not reopen RC001.

## Acceptance evidence

All values below are from one Phase 2 public MLP and are smoke/operational
evidence, not a reliable leaderboard estimate or scientific promotion.

| gate | `ALG003-V009` | `ALG014-V003` |
|---|---:|---:|
| validator from fresh extraction | PASS | PASS |
| local / subprocess scorer | PASS / PASS | PASS / PASS |
| adjusted score | `6.95469796e-7` | `6.82781482e-7` |
| final-layer MSE | `2.78012908e-6` | `2.59324179e-6` |
| FLOPs / budget fraction | `550,101,888,000` / `0.250157` | `578,986,643,120` / `0.263293` |
| maximum observed wall / 120 s | `1.6075 s` | `3.3020 s` |
| maximum observed residual / 0.4 s | `0.0896 s` | `0.1418 s` |
| setup / 5 s | `0.002532 s` | `0.0000075 s` |
| peak working set / 8 GiB | `450.1 MiB` | `442.7 MiB` |
| repeated fixed-seed prediction and FLOPs | byte-identical / identical | byte-identical / identical |
| package size / 50 MiB | `6,766,089 B` | `2,759 B` |

**The N1 lane beat the N0 fallback by 1.82% in adjusted score on this single
smoke MLP.** That is directly comparable Phase 2 evidence, but one MLP is too
small to claim stable succession or scientific promotion. Official evaluation
is needed.

The exact source trees were packaged by the current Windows-native CLI,
archive contents and manifest hashes were inspected, and validators were run
from fresh extractions. The same source hashes then passed both local and
subprocess scoring. Fixed-seed tests used the fresh extracted files.

## Operational incident disposition

The known intermittent WSL corruption recurred during bounded retries. It
appeared outside or before candidate code as impossible Python states
(`'float' object is not callable`, `'cell' object is not callable`, `unknown
opcode`), plus process segfault/invalid-opcode/heap-abort attempts. Selected
machine-readable failures remain under `runs/`. The exact packages then passed
cleanly on Windows native in both runner modes, so these incidents are not
evidence of a candidate implementation defect and do not require an owner
pause. Independent-machine/VM reproduction remains desirable before final
designation.

## Next action

T075 is the only owner-only step: explicitly authorize the upload and ensure
AIcrowd credentials are configured, then submit these exact two archives. It
will consume two of the ten submissions allowed per UTC day. Preserve the
submission IDs and full grader reports. T095 scientific search is independent
and must not wait for credentials or upload.
