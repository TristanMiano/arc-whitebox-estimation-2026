# T112 — public-frontier reconstruction and N1 improvement attempts

## Outcome

T112 returns both requested runnable artifacts, but it also establishes an
important negative result: the current official Phase-2 leader cannot be
faithfully reconstructed from the public record available on 2026-08-28.
Team Puffi submission `328774` remains an external numerical reference because
its Phase-2 equations, fitted coefficients, assets, and estimator bytes are not
public. The strongest honest public-family reconstruction here is
`PUB112-P1`; the strongest at-least-N1 child is `ALG022-V000`.

| Role | Algorithm | Evidence | Adjusted score | Final-layer MSE | vs sampling approx | Multiplier |
|---|---|---|---:|---:|---:|---:|
| official public numerical best | Puffi `328774` | official 50-network grade | `7.25719e-9` | `2.58030e-8` | `164x` | `.281312` |
| project incumbent | `ALG019-V000` | local Phase-2 Mini 100 | `2.43818e-7` | `2.43818e-6` | `4.680x` | `.1` |
| **reconstructed public control** | **`PUB112-P1`** | Mini 12 selection + untouched-to-P1 88 confirmation | **`5.84319e-7`** | **`2.20366e-6`** | **`1.953x`** | **`.265158`** |
| **our at-least-N1 attempt** | **`ALG022-V000`** | post-initial-audit exploratory Mini 100 | **`5.83541e-7`** | **`2.19972e-6`** | **`1.955x`** | **`.265280`** |

`ALG022-V000` is `0.1331%` lower in adjusted score than the strongest
reconstructed public control. It is therefore the requested best N1 attempt,
but **it is not the project's new submission candidate**: it is `2.3933x`
worse than `ALG019-V000` on identical local Mini targets and wins `0/100`
networks after compute adjustment. The exact submission-facing identity is
closed unchanged and was not uploaded.

The official leader is still `80.41x` below ALG022 in adjusted score and
`85.25x` below it in raw MSE. Those ratios compare different cohorts and are
diagnostic, not a claim about an official grade. They are far too large to
attribute to ordinary cohort variation. The public reconstruction is missing
a decisive private Phase-2 mechanism.

## What was reconstructed

The public carrier is an independently implemented union of the coordinate
basis and eight width-1024 Kerdock bases, each with its antipode, at the exact
mean Gaussian radius. Its first layer uses the public chirp/FWHT identity. An
exact finite-field/MUB certificate verifies all 512 alternating Kerdock forms,
all 130,816 pair differences, the selected packet, and the seed-3 rotation.

The original public ladder was:

- P0: direct nine-basis carrier;
- P1: P0 plus exact first-layer mean/variance repair;
- P2: P1 plus a terminal full-covariance proxy pull;
- P3: P2 plus the public `.35/.45` H2 repair;
- P4: P3 plus the public radial L4 skew/kurtosis snap.

P4 achieved the best raw MSE among that ladder on full Mini (`1.95110e-6`),
but its `.310159` multiplier made it worse in adjusted score. P1 was selected
as the lowest adjusted public arm on rows 0--11 and confirmed on the other 88
rows at `5.77752e-7`; its all-100 score is `5.84319e-7`. Selection and
confirmation are reported separately to avoid hiding the selection step.

The first N1 child, `ALG021-V000`, added a ridged simplex stack of direct,
proxy-pull, and shifted Edgeworth endpoints. It improved P4 by `0.4164%`
adjusted (`6.02631e-7` versus `6.05150e-7`) but lost to P1 by `3.1338%` and
to ALG019 by `2.4716x`. Its pre-outcome `.30` parent-win event occurred and
therefore carried `1.737` bits of favorable surprise, but the magnitude was
not competitive.

## Corrected terminal endpoint audit

The initial P0--P4 implementation audit exposed one real omission: the theory
ledger had identified a terminal Gaussian projection as the most plausible
public Phase-2 endpoint, but no standalone arm implemented it. T112 did not
rewrite or reinterpret the sealed P0--P4 result. It created a source-separated
second decision instead:

- `PUB112-G` estimates the final preactivation's radial first and second
  moments from the nine-basis carrier, then integrates the Gaussian positive
  part analytically;
- `ALG022-V000` adds the leading terminal skew Edgeworth term, multiplied by a
  leave-complete-basis-out jackknife reliability in `[.8649,.9113]`.

The exact formulas were written in `THEORY_LEDGER.md` before initial target
access and contain no fitted target-derived constants. Their Python source was
implemented after the first score exposed the missing arm, so their result is
correctly labeled post-initial-audit exploratory rather than clean prospective
evidence. ALG022 improved G by `6.1375%` adjusted, with `99/100` wins. Its
frozen theory prior of `.35` makes that direction a favorable `1.515`-bit
surprise. G itself did not reconstruct the leader, and ALG022 still failed the
incumbent decisively.

## Why the official leader is not claimed as reproduced

Compute inversion remains highly informative. A dense forward of exactly
`18,432 = 9 * 2 * 1024` rows costs almost exactly Puffi's reported `618.611B`
effective operations, pointing strongly toward nine antipodal width-sized
bases plus a small adaptive or analytical layer. Public Phase-1 material also
discloses Kerdock/MUB quadrature, exact radial integration, A716, within-network
ridge discrepancy transport, probe pruning, and terminal bypass. It does not
disclose which of those mechanisms, fitted constants, frame IDs, or new ideas
make up submission `328774`.

Direct nine-basis propagation has target-free NNGP risk around `2.30e-6` at
depth 16. The official `2.58e-8` raw MSE is therefore mathematically
incompatible with geometry alone. T112's repairs move local raw MSE to roughly
`1.95e-6`, not `2.58e-8`. The missing factor is an in-flight analytical/error-
transport mechanism, not an unnoticed choice of equal-weight MUB labels. It
would be misleading to search many hidden frame subsets on the same public
targets and call the winner a reconstruction.

## Validation and packages

Target-blind checks passed for exact algebra, dense/FWHT parity, H1 moment
parity, negative shifts, Edgeworth sign, simplex vertices, deterministic
finite nonnegative outputs, and low-budget fallback. Windows-native Python
3.10.20 with WhestBench 0.16 / FlopScope 0.12 repeated the important routes
byte-deterministically. `ALG022-V000` costs `583,355,864,072` FLOPs with
multiplier `.2652795`; maximum native residual time was `.15694s`.

Current WhestBench 0.16 Windows contract and archive validation passed for the
two requested deliverables:

- `PUB112-P1.tar.gz`, SHA-256 `e9504ae1...e1538c003`;
- `ALG022-V000.tar.gz`, SHA-256 `330ee6da...2038886`.

`PUB112-P4` and `ALG021-V000` packages are also preserved as the first sealed
parent/child decision. No official upload was authorized or performed.

## Disposition and next work

- `PUB112-P1`: public reconstruction/control only; no scientific tier and no
  submission succession. It is `2.3965x` the local ALG019 adjusted score.
- `ALG021-V000`: real but small parent improvement; competition-negative and
  closed unchanged. No promotion; blocker is direct scientific
  noncompetitiveness, not a strict gate.
- `ALG022-V000`: N1/dimension-3 candidate with strong exploratory parent
  evidence, but competition-negative at `2.3933x` ALG019. Its post-target
  implementation timing also prevents using this run alone for a formal M1
  claim. No promotion; blocker is direct noncompetitiveness plus evidence
  scope, not a strict gate.
- `ALG019-V000`: remains the local and official project best, official
  submission `328762` at adjusted `2.399598318e-7`.

FC009 has consumed its two N1 decisions. T113 should begin a new written-theory
recurrence focused on the missing in-flight analytical/error-transport factor,
using the public A716/ridge equations and T112's measured endpoint failures;
it must not queue more ordinary nine-basis endpoint tweaks.

## Timing and work allocation

- Start: `2026-08-28T15:41:36,512691354-07:00`
- Pre-task estimate: **4--8 hours**
- End/checkoff: `2026-08-28T17:34:56,421385940-07:00`
- Actual wall time: `01:53:19.908694586` (`6799908694586` ns)
- Estimate error: completed `02:06:40.091305414` earlier than the four-hour
  lower bound.

Approximate allocation was 60 active minutes of written theory and public
reconnaissance, 31 minutes of implementation, audit diagnosis, analysis, and
durable documentation, and 22 minutes of program execution/waiting,
Windows-native reruns, and package validation. Categories are rounded; the
large prediction seals, not unaided thinking, dominated the machine portion.
