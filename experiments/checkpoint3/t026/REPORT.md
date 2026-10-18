# T026 — residual-only IID sampling and variance allocation

Status: **complete support task; exact target preserved for frozen
coefficients; no candidate instantiated**.

## Implemented estimator

For each frozen affine-surrogate network from T025, the estimator evaluates the
affine-chain mean analytically and samples both residual sums:

```text
estimate = E[affine chain] + sample_mean(kink residual)
                              + sample_mean(gate residual).
```

The sample mean is unbiased for the specified input distribution conditional
on coefficients and classes frozen independently of the evaluation draws. No
unbiasedness claim is made for deterministic QMC, coefficients fit on the same
draws, or omission of the gate term.

The bounded correctness fixture uses 16 deterministic width-5/depth-5
networks. It freezes the surrogates from each complete `6^5 = 7,776`-state
symmetric six-point product population, then compares exact population moments
with 256 IID replicates of 256 residual samples. This is synthetic comparison
class `N`, not a challenge-scale estimator score.

## Result

The accepted MSVC 19.43 Windows-native run passed all seven frozen checks:

| Check | Result |
|---|---:|
| Pointwise reconstruction maximum error | `5.3290705182007514e-15` |
| Analytic affine/population mean maximum error | `2.993161274389422e-13` |
| Exact target-preservation maximum error | `1.1990408665951691e-13` |
| Variance-allocation identity maximum error | `1.8329521928039938e-15` |
| Maximum IID grand-mean standardized bias | `2.3121940621978641` |
| Pooled full-output trace variance | `38.808913954949318` |
| Pooled residual trace variance | `27.480531102310874` |
| Pooled residual/full trace-variance ratio | `0.70809843156680941` |

Replacing sampled affine variation by its analytic mean therefore reduced the
pooled trace variance by about `29.19%` in this fixture. The residual allocation
was:

| Residual component | Share |
|---|---:|
| Kink variance | `1.0001626517987432` |
| Gate variance | `0.000055882364592160219` |
| Twice kink/gate covariance | `-0.00021853416333523284` |

The shares sum to one; the kink share exceeds one because the covariance is
negative. Gate leakage was nonzero but small in this pooled fixture, so the
exact estimator retains it. This result alone does not justify dropping it on
challenge networks.

The network ratios also reject an immediate broad variance-improvement claim:
the residual/full ratio had median `0.80293534037952841`, p90
`1.560676316051538`, and maximum `413.87722517265104`. The maximum comes from
an individual fixture where full-output variance benefits from cancellation
with the affine component. Residual-only sampling is thus a valid operation,
not yet a tail-safe candidate.

## Windows execution and intermittent failures

The canonical run began at `2026-08-20T21:25:29.1074806-07:00`, ended at
`2026-08-20T21:25:37.4932197-07:00`, compiled cleanly, exited zero, wrote no
stderr, passed its schema/numerical checks, and retained source and artifact
hashes. Its JSON and CSV match the two valid exact-binary retries from attempt
004 and the three earlier Windows-native release observations.

Windows native was not uniformly stable. Attempt 004 produced an internal
width mismatch, two byte-identical passes, a `0xc0000005` access violation,
and a `0xc0000409` fail-fast termination from one exact binary. Attempt 005
then terminated with `0xc0000374` heap corruption. Attempts 006 and 007 were
scientifically valid executions whose controller-only manifest defects were
fixed and rerun. All failures remain preserved; none is presented as a clean
run.

The owner authorized bounded retries and explicitly removed a
consecutive-clean-run gate. The accepted run may therefore close this support
task. Reproduction of later contest-scale conclusions on an independently
stable machine or VM remains the broader corroboration mechanism.

## Reproduction and decision

From WSL, create a Windows-local output root and invoke the Windows-native
compiler/controller:

```bash
repro_root=$(mktemp -d /mnt/c/Users/trist/AppData/Local/Temp/arc-t026-repro.XXXXXX)
powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass \
  -File "$(wslpath -w research/native_checkpoint3/residual_sampling/run_t026_verification_windows.ps1)" \
  -OutputDir "$(wslpath -w "$repro_root/evidence")" \
  -BuildDir "$(wslpath -w "$repro_root/build")"
```

Verify the retained evidence without adding another execution gate:

```bash
bash experiments/checkpoint3/t026/verify_evidence.sh
```

Accept T026 as support event `E039`. No `ALG` identity, candidate bundle,
`M1`, `P1`, competitive rank, or submission claim is created. T027 should now
measure paired gradients of the isolated residual before any rotation is
proposed.

## Timing calibration

- Completion-segment start: `2026-08-20T21:15:05.059898837-07:00`
- Pre-task estimate: `45 minutes`
- End/check-off: `2026-08-20T21:32:34.183434501-07:00`
- Completion-segment elapsed: `00:17:29.123535664` (`1049123535664` ns)
- Original T026 start/estimate before its pauses:
  `2026-08-20T19:53:44.990236259-07:00` / `120 minutes`
