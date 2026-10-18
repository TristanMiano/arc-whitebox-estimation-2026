# T033 — layer-local paired-gradient concentration

Status: **complete positive mechanism result; M1 awarded; no complete candidate
or P1 created**.

## Result

The predeclared Windows-native fixture compared the paired gradient with
respect to the input against gradients with respect to exact hidden
activations after layers 24, 28, and 30. It used 12 independently seeded
width-64/depth-32 He-Gaussian ReLU networks and 512 deterministic antithetic
input pairs per network. The normalized final-output sum was the scalar probe.

| Route | Mean participation ratio | Mean ratio to input | Worst network ratio | Mean top-8 energy | Modeled pilot-gradient cost |
|---|---:|---:|---:|---:|---:|
| Input-global | `21.6391` | `1.0000` | `1.0000` | `0.5133` | `1.0000` |
| Cut 24 | `7.8036` | `0.357515` | `0.556119` | `0.8170` | `0.6250` |
| Cut 28 | `5.9517` | `0.275832` | `0.423603` | `0.8686` | `0.5625` |
| Cut 30 diagnostic | `4.9868` | `0.233003` | `0.409763` | `0.8908` | `0.53125` |

Both primary routes passed the frozen M1 rule by wide margins. Their mean
ratios were respectively `0.632485` and `0.714168` below the `0.99` threshold,
and their worst-network ratios were `0.693881` and `0.826397` below the `1.25`
tail boundary. All 12 networks improved on both routes. The trend continued at
the predeclared cut-30 diagnostic.

The modeled cost comparison charges the same full forward propagation to both
routes. The input-global pilot then backpropagates through 32 layers, whereas
a cut-`c` pilot backpropagates through only `32-c`; this yields `(32 + 32-c) /
64`. It is a native operation model, not a Whest/flopscope or submission-cost
claim.

## Interpretation boundary and next candidate

This is materially different from the affine-residual identity closed by
T027/T028. It changes the differentiation coordinate to a late hidden state;
the suffix gates are non-affine and no constant affine gradient cancels it.

The result does **not** yet specify a legal way to rotate the input point law.
Hidden activations are not independent Gaussian inputs, and applying an
orthogonal transform in hidden space without an exact estimator construction
could change the target. Therefore E042 is an M1 mechanism signal, not an
`ALG` candidate and not P1. T070 is appended as the immediate next task: define
and register a target-preserving suffix/local estimator with an explicit
operation plan, duplicate fingerprint, and tail fallback, then enter F0-F3.
T034 remains the alternate independent control-variate family.

## Windows execution and repairs

The accepted Windows-native run began at
`2026-08-21T17:46:57.4003786-07:00`, ended at
`2026-08-21T17:47:08.4286499-07:00`, ran the normal fixture twice, and produced
byte-identical JSON and CSV outputs. The executable depends only on
`KERNEL32.dll`; no Python was loaded.

Two failed attempts are retained. Attempt 001 compiled successfully but the
PowerShell `Start-Process` compile wrapper failed to return; it was stopped
after confirming there was no compiler child or result. Attempt 002 exercised
the repaired controller but correctly rejected invalid unused affine-support
fields before any network metric was evaluated. Those fields were initialized
with the already-audited Gaussian coefficients, after which the accepted run
passed. No owner action or reboot was required.

## Human promotion disposition

- **Subject / evidence class:** E042/T033 synthetic native mechanism diagnostic
  (`N`), not a complete estimator.
- **Current / highest supported / next tier:** `M1-mechanism-signal` / M1 / P1
  only after a complete target-preserving candidate enters F0-F3.
- **Positive evidence:** cut-24 and cut-28 mean participation-ratio ratios were
  `0.357515` and `0.275832`; worst-network ratios were `0.556119` and
  `0.423603`; modeled cost ratios were `0.625` and `0.5625`. Both routes passed
  the predeclared signal, tail, finiteness, replay, and cost conditions.
- **Gate results:** mechanism magnitude `PASS` (threshold `<0.99`; observations
  `0.357515`/`0.275832`; favorable margins `0.632485`/`0.714168`); mechanism
  tail `PASS` (threshold `<1.25`; observations `0.556119`/`0.423603`;
  favorable margins `0.693881`/`0.826397`); modeled local cost `PASS`
  (threshold `<1`; observations `0.625`/`0.5625`; favorable margins
  `0.375`/`0.4375`); deterministic
  replay `PASS` (byte-identical); native dependency boundary `PASS`; candidate
  target preservation and registration `NOT-RUN`; F0-F3 `NOT-RUN`; incumbent
  competitiveness `NOT-APPLICABLE` at M1.
- **Primary blocker:** `EVIDENCE_INCOMPLETE` for P1; this is not a scientific
  negative.
- **Strict gate sole blocker:** **No.** No strict gate rejected the mechanism;
  the missing piece is a complete target-preserving estimator definition.
- **Why not yet P1:** concentration in a hidden coordinate is strong evidence,
  but it does not itself say how to sample or correct the original Gaussian
  expectation without bias.
- **Immediate high-impact unlock:** agent executes T070 to derive/register the
  exact suffix/local estimator and run it through the qualified F0-F3 funnel.
  No owner action or gate relaxation is indicated.

## Verification

```bash
bash experiments/checkpoint3/t033/verify_evidence.sh
```

## Timing calibration

- Task start: `2026-08-21T17:41:17.514514657-07:00`
- Pre-task estimate: `45 minutes`
- End/check-off: `2026-08-21T17:51:18.833339936-07:00`
- Elapsed: `00:10:01.318742361` (`601318742361` ns)
