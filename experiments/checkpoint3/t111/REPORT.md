# T111 — terminal H107-U complete-risk proxy

## Outcome

T111 closes both frozen H107-U routes without protected-target access.  U0 was
the lower target-free prediction, but neither route reduced its own complete
risk estimate and neither came close to the rebased ALG019 incumbent hurdle.
No algorithm ID, protected cohort, package, upload, scientific tier, or
submission succession is authorized.  **ALG019-V000 remains the local and
official project best**, submission 328762 at adjusted
`2.3995983178792816e-7`.

| Frozen route | Base raw complete-risk proxy | Candidate raw proxy | Candidate/base | Wins | Gate |
|---|---:|---:|---:|---:|---|
| H107-U0 | `9.430844304e-6` | `1.219734772e-5` | `1.293346314` | 6/12 | fail |
| H107-U1 | `9.327839371e-6` | `1.246151218e-5` | `1.335948410` | 6/12 | fail |

At the shared `.1` score multiplier, U0/U1 predicted adjusted risks were
`1.219734772e-6` and `1.246151218e-6`; these are respectively `5.0831x` and
`5.1932x` the official incumbent score proxy.  The two 332-row witnesses also
estimated the unchanged bases at roughly `3.9x` official risk, so those
absolute transfers are visibly noisy.  The decisive same-network comparison
does not depend on mixing cohorts: U0 increased pooled raw risk by
`2.766503414e-6` and U1 by `3.133672808e-6`.

The breadth result is heterogeneous rather than uniformly adverse. Both arms
improved exactly 6/12 networks, and the predeclared row bootstrap intervals for
the pooled change include zero. U0's 5--95% interval was
`[-1.8265e-6, 8.3990e-6]`; U1's was `[-1.6219e-6, 9.0384e-6]`. Row 69 was a
large adverse realization (`+3.4843e-5` U0, `+3.6657e-5` U1); deleting only
that maximum changes U0's mean to `-1.4950e-7` and U1's to `+8.6054e-8`.
Those post-outcome sensitivity figures do not change the frozen pooled rule.

## Interpretation and rejection strength

This is a **clear submission-funnel rejection of the exact unregularized
H107-U0/U1 identities**, because the point estimate had to beat both its own
base and the official incumbent proxy. It is only **weak-to-moderate scientific
negative evidence** for the broader low-rank self-supervision idea: wins split
6/12, uncertainty includes benefit, the absolute witness calibration was
noisy, and no protected target was opened. The rejection is not caused by an
unrelated strict gate. It is caused by the candidate's frozen direct
complete-risk point estimate being adverse.

The most plausible mechanism is coefficient variance. The unregularized
projector estimates a global closure-scale direction from only 332 partial
Haar rows. On some networks it learns a large correction: correction mean
square reached `7.57887e-5`. Low rank limits coordinatewise noise but does not
shrink a noisy coefficient along a high-energy global direction. Future theory
may consider a prospectively derived shrinkage/cross-fit rule, but that would
be a new identity and cannot repair this frozen result post hoc.

Before the proxy, the probability of clearing was `.30`; failure is therefore
expected and carries `-log2(.70)=0.514573` bits of surprise. Not reaching
adjusted `1e-7` was overwhelmingly expected under the frozen `.005` prior.

## Implementation audit and cost

The four declared feature columns have exact algebraic rank at most three:
the declared quartic-shaped column is a linear combination of the scale and
cubic-shaped columns. This was found by the target-blind fixture before proxy
opening. The source retained all four prospectively declared columns and used
the frozen Moore--Penrose pseudoinverse; effective rank was three on every
network. This is a specification redundancy, not a hidden fourth degree of
freedom or a numerical failure.

Independent NumPy projector parity passed at maximum error `6.51e-18`;
permutation, positive-scale, `P=C`, and degenerate-feature fixtures passed.
All coefficients were finite. Direct candidate/base risk differences matched
the independently expanded same-P operator formula to maximum absolute error
`2.81e-11`. U0 and U1 each cost exactly `219,728,124,281` FLOPs twice on
Windows native, were byte deterministic, retained the `.1` multiplier, and
had about `174.2M` FLOPs of score-floor headroom.

The first native proxy launch stopped before reading a row because Windows
rejected the WSL spelling of the shard path. The unchanged sealed runner was
retried with the native `C:/...` spelling and completed all 12 rows. This was
an infrastructure path repair, not an estimator or evidence change.

## Evidence and routing

- `PREPROXY_SEAL.json` freezes source, equations, hurdle, witnesses, and rule.
- `TARGET_BLIND_QUALIFICATION_WINDOWS.json` records fixtures and exact cost.
- `TARGET_FREE_PROXY.json` and `proxy_rows/` preserve the complete one-shot
  weights-only evidence and crash-resumable row records.
- `candidate_family.py`, `qualify_and_meter.py`, and `target_free_proxy.py`
  preserve exact implementation bytes.

T111 consumes the second and final FC008 decision. K/R/S/Q remain unapplied
reserves rather than automatic follow-ons. T112 begins FC009 with the default
owner-duration 60-active-minute written-theory recurrence, explicitly using
U's coefficient-variance failure and T110's TD/K3-control evidence.

## Timing and work allocation

- Start: `2026-08-28T15:20:52,803629687-07:00`
- Pre-task estimate: **about 90 minutes**
- End/checkoff: `2026-08-28T15:36:41,198142464-07:00`
- Actual wall time: `00:15:48.395623778` (`948395623778` ns)
- Estimate error: completed `01:14:11.604376222` earlier than estimated

Approximate allocation was 4 minutes of mathematical/specification analysis,
10 minutes of implementation, debugging, verification, and durable
documentation, and 2 minutes of machine execution/wait. Categories are
rounded and overlap slightly at debugging boundaries. As anticipated by the
owner's calibration note, source/analysis work itself was fast; the measurable
machine costs were native metering, the one path-error repair/retry, and the
24 diagnostic witness propagations.
