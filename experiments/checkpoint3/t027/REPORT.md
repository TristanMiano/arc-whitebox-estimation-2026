# T027 — residual-only paired-gradient spectrum

Status: **complete negative support task; the paired residual matrix is the
prior global active matrix; no candidate or tier created**.

## Decisive identity

Let the exact scalar output probe be (f(x)), and let the frozen affine-chain
surrogate be (a(x)=b+v^T x). The exact retained kink-plus-gate residual is
(r(x)=f(x)-a(x)). The historical active matrix uses the gradient of the
antithetically evenized integrand:

```text
q_full(x) = 0.5 * (grad f(x) - grad f(-x)).
```

Because `grad a(x) = grad a(-x) = v`, the residual paired gradient is

```text
q_residual(x)
  = 0.5 * ((grad f(x) - v) - (grad f(-x) - v))
  = q_full(x).
```

This is dimension-independent and does not depend on the chosen frozen affine
coefficients. Therefore the residual and global gradient-energy matrices,
eigenvectors, eigenvalue spectra, and participation ratios are exactly the
same apart from floating-point evaluation error. Moreover, the antithetic
pair mean of the affine chain is constant, so rotating the exact residual with
this basis gives the same paired sample error as the corresponding global
rotation at the same points. Calling it a residual rotation does not create a
new basis or a new QMC mechanism.

## Windows-native verification

The frozen MSVC 19.43 fixture used eight independently generated width-64,
depth-32 He-Gaussian networks, diagonal-Gaussian frozen surrogate coefficients,
all three dead/kink/on classes, and 512 deterministic Gaussian antithetic pairs
per network. It computed both gradients independently, accumulated both 64x64
energy matrices, and diagonalized both matrices.

| Check | Frozen tolerance | Observed maximum | Margin |
|---|---:|---:|---:|
| Paired-gradient absolute difference | `2.0e-12` | `8.8818e-16` | `1.9991e-12` |
| Energy-matrix absolute difference | `2.0e-12` | `4.4409e-16` | `1.9996e-12` |
| Eigenvalue absolute difference | `2.0e-11` | `5.3291e-15` | `1.9995e-11` |
| Participation-ratio absolute difference | `2.0e-11` | `2.4869e-14` | `1.9975e-11` |

The full and residual participation-ratio ratio was exactly `1.0`. On this
width-64 fixture the shared participation ratio ranged from `17.1155` to
`23.7745`, with mean `21.3926`. The shared mean energy captured by the leading
1, 8, and 16 directions was `0.110446`, `0.515089`, and `0.738970`.

The prior width-256 global matrices in
`research/raw_results/fixed_points_n256.json` had participation ratios
`74.3240`--`80.2266` with mean `77.2827`. T027 does not claim the new
width-64 fixture numerically reproduces that historical distribution. The
algebraic identity instead says that, for those same historical networks and
points, subtracting any frozen affine chain would leave each paired matrix and
those exact participation ratios unchanged.

## Windows controller attempts

The accepted attempt began at `2026-08-21T17:22:31.5832671-07:00`, ended at
`2026-08-21T17:22:38.5540621-07:00`, exited zero, wrote no stderr, passed five
frozen checks, retained its source hashes, and recorded no Python dependency.

Four earlier controller-only attempts are preserved under
`experiments/checkpoint3/t027_attempts/`. They respectively exposed a hanging
`Start-Process` compile wrapper, an unset `$LASTEXITCODE`, rejection of a
direct executable launch, and asynchronous visibility of a successfully linked
file. None ran the experiment or produced a scientific result. The final
controller retains direct compilation with a bounded stable-file observation
and uses synchronous `Start-Process` only for dependency and experiment
execution. No owner action or reboot was needed.

## Decision and route

Accept this as support event `E040`. The proposed concentration mechanism is
falsified: paired affine subtraction cannot concentrate a matrix from which it
cancels exactly. No `ALG` identity, candidate bundle, `M1`, `P1`, competitive
rank, or submission claim is created.

T028 should next adjudicate its top-k residual-rotation request as an exact
duplicate of the retained global paired-gradient basis and fresh-scramble
evidence, without spending new protected compute. T029/T030 likewise require a
materially different signal before execution. Scientifically distinct open
directions remain layer-local/non-affine gradients (T033) and independently
fit residual control variates (T034).

## Human promotion disposition

- **Subject / evidence class:** E040/T027, synthetic native mechanism identity
  (`N`), not an algorithm candidate.
- **Current tier / highest supported tier / next tier considered:**
  `U0-unclassified` / support-only `U0` / no promotion tier applicable.
- **Positive evidence:** exact residual/full paired-gradient agreement passed
  all four numerical checks above across 4,096 pairs and eight depth-32
  networks. This is positive correctness evidence, not a concentration win.
- **Gate results:** identity correctness `PASS`; matrix equality `PASS`;
  eigenspectrum equality `PASS`; participation-ratio equality `PASS`;
  residual concentration improvement `FAIL-SCIENTIFIC` (ratio `1.0`, zero
  improvement, below the `0.01` two-route M1 mechanism-signal floor by `0.01`);
  F0-F3 candidate gates `NOT-APPLICABLE` because no candidate exists;
  incumbent competitiveness `NOT-APPLICABLE`.
- **Primary blocker class:** `SCIENTIFIC_NEGATIVE` + `SUPPORT_ONLY`.
- **Why not promoted:** no strict gate blocked a promising result; the proposed
  paired residual signal is algebraically identical to the old global signal,
  so its claimed concentration improvement is exactly zero.
- **Immediate high-impact unlock:** no owner action and no gate relaxation can
  change this identity. Agent: close duplicate paired-residual rotation work
  using this evidence, then test a materially different signal such as
  layer-local/non-affine gradients or an independently fit control variate.

## Reproduction

From WSL, use a fresh Windows-local root:

```bash
repro_root=$(mktemp -d /mnt/c/Users/trist/AppData/Local/Temp/arc-t027-repro.XXXXXX)
powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass \
  -File "$(wslpath -w research/native_checkpoint3/residual_gradients/run_t027_verification_windows.ps1)" \
  -OutputDir "$(wslpath -w "$repro_root/evidence")" \
  -BuildDir "$(wslpath -w "$repro_root/build")"
```

Verify the retained evidence without creating another execution gate:

```bash
bash experiments/checkpoint3/t027/verify_evidence.sh
```

## Timing calibration

- Task start: `2026-08-21T17:07:38-07:00`
- Pre-task estimate: `50 minutes`
- End/check-off: `2026-08-21T17:28:26.880119725-07:00`
- Elapsed: `00:20:48.880555091` (`1248880555091` ns)
