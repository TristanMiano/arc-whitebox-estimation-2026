# T025 — exact kink-residual output decomposition

Status: **complete support task; exact identity recorded; no candidate
instantiated**.

T025 defines a pointwise telescoping decomposition for the bias-free square
ReLU MLP used by the challenge. It separates an analytically integrable affine
chain from uncertain kink residuals and confident-gate leakage residuals. The
identity is exact for every input and every fixed set of affine coefficients;
it does not assume Gaussian preactivations or correct dead/on labels.

## Definition

Use row-vector convention for a depth-`L` network:

```text
h_0(x) = x
z_l(x) = h_{l-1}(x) W_l
h_l(x) = rho(z_l(x)),       rho(z) = max(z, 0)
f(x) = h_L(x)
```

Freeze one class in `{dead, kink, on}` and one affine surrogate
`ell_lj(z) = a_lj z + b_lj` for every neuron before evaluating a residual
sample. The class-aware default is:

```text
dead:  a = 0, b = 0
on:    a = 1, b = 0
kink:  a = Phi(alpha), b = sigma phi(alpha)
```

For kink neurons the displayed values are the `L2` affine projection of ReLU
under the frozen marginal Gaussian `N(mu, sigma^2)`: Stein's identity gives
the slope `Phi(alpha)`, and matching the Gaussian ReLU mean gives the intercept
`sigma phi(alpha)`. The exact decomposition below remains valid if a later
task freezes different kink coefficients.

Let `D_l = diag(a_l)` and define the affine layer

```text
A_l(h) = h W_l D_l + b_l.
```

Its complete-chain mean is analytic. With `m_0 = E[x] = 0`, evaluate

```text
m_l = m_{l-1} W_l D_l + b_l.
```

Thus `m_L = E[A_L o ... o A_1(x)]` without sampling.

## Exact telescoping identity

Let `F^(k)` use exact ReLU layers `1..k` and affine surrogate layers
`k+1..L`. Then `F^(0)` is the affine chain and `F^(L) = f`. For the exact
preactivation `z_k(x)`, define the local residual

```text
r_k(z_k) = rho(z_k) - (z_k D_k + b_k)
B_k = (W_{k+1} D_{k+1}) ... (W_L D_L),    B_L = I.
```

Adjacent hybrids differ by `F^(k) - F^(k-1) = r_k(z_k) B_k`, so the
pointwise identity is

```text
f(x) = A_L o ... o A_1(x) + sum_{k=1}^L r_k(z_k(x)) B_k.       (1)
```

Split each local residual by the frozen class:

```text
r_k^K = 1{kink} r_k
r_k^G = 1{dead} rho(z_k) + 1{on} rho(-z_k).
```

Equation (1) therefore gives the requested separation:

```text
E[f(x)] = m_L
        + sum_k E[r_k^K(z_k(x)) B_k]
        + sum_k E[r_k^G(z_k(x)) B_k].                           (2)
```

The first term is analytic/affine, the second contains the intended kink
nonlinearity, and the third explicitly retains dead/on gate mistakes. Keeping
both sampled sums preserves the target exactly. If fixed coefficients are
chosen without using the evaluation samples, an IID or properly randomized-QMC
sample average of the two residual sums is unbiased over its sampling
randomization. A deterministic fixed QMC design has quadrature error rather
than a general probability-unbiasedness claim, but equation (2) still targets
the exact integral.

## Controlled approximation and error bounds

Dropping the gate-leakage sum is optional, not part of the exact default. Its
pointwise error `e_G(x)` satisfies

```text
||e_G(x)||_2
  <= sum_k ||r_k^G(z_k(x))||_2 ||B_k||_2
  <= sum_k ||r_k^G(z_k(x))||_2
           product_{j=k+1}^L ||W_j D_j||_F.                    (3)
```

Consequently the mean bias is bounded by the expectation of the final
right-hand side. This is conservative but distribution-free once the exact
gate residuals are measured. Under a marginal Gaussian diagnostic only,

```text
E[(Z_+)^2] = (mu^2 + sigma^2) Phi(alpha) + mu sigma phi(alpha)
E[(Z_-)^2] = (mu^2 + sigma^2) Phi(-alpha) - mu sigma phi(alpha).
```

The first formula applies to a dead neuron's leakage and the second to an on
neuron's leakage. At the strict `|alpha| = 3` boundary with `sigma = 1`, the
leakage second moment is `0.00020343508048693316`. These Gaussian formulas are
screening diagnostics, not rigorous bounds on the non-Gaussian deep-layer
distribution. T026 must retain the exact gate sum initially and measure its
actual variance and tails before any omission is proposed.

If coefficients or classes are estimated from samples, they must be frozen
independently of the residual-evaluation points or cross-fit as required by
T031. Otherwise a claimed unbiased residual estimator is not justified.

## Native verification

The standalone C++20 fixture checks equation (1), the affine-mean identity,
the gate-drop bound (3), Gaussian positive/negative second-moment identities,
strict class coefficients, deterministic replay, and normal-versus-ASan/UBSan
equality. It loads no Python.

Results over 257 deterministic width-5/depth-4 mixed-class fixtures:

| Check | Result |
|---|---:|
| Maximum pointwise reconstruction error | `1.0972125985553305e-16` |
| Maximum affine symmetric-pair mean error | `5.551115123125783e-17` |
| Maximum exact-error / bound ratio | `0.46355674019033927` |
| Nonzero gate-leakage cases checked | `257 / 257` |
| Normal/replay/sanitized payload equality | byte-identical |
| Sanitizer or run-window kernel fault | none |

Reproduce in a fresh output tree:

```bash
work=$(mktemp -d /tmp/arc-t025-reproduction.XXXXXX)
bash research/native_checkpoint3/kink_residual/run_t025_verification.sh \
  --output-dir "$work/evidence" --build-dir "$work/build"
```

Strictly verify the retained evidence and a fresh replay:

```bash
bash experiments/checkpoint3/t025/verify_evidence.sh
```

The first compile attempt is retained separately. It stopped before executing
the fixture because `-Werror` promoted an existing signedness warning in the
already-qualified checkpoint-2 header. The corrected command treats that
inherited include as a system header while retaining strict warnings for the
new T025 source; compiler stdout, stderr, and exit status are now explicit.

## Decision and next task

Accept the exact decomposition as the T025 support deliverable and continue to
T026. T025 does not choose a sample count, fixed point asset, router, operation
plan, or deployable estimator, so it creates no `ALG` identity, candidate
bundle, `M1` status, or `P1` claim. T026 should implement sampling of both
residual sums, verify target preservation, and measure affine/kink/gate
variance allocation before a screenable candidate is registered.

## Timing calibration

- Start: `2026-08-20T19:32:50.749338540-07:00`
- Pre-task estimate: `75 minutes`
- End/check-off: `2026-08-20T19:50:59.281454193-07:00`
- Actual elapsed: `00:18:08.532115653` (`1088532115653` ns)
