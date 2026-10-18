# T119A — target-free RVRC screen

## Outcome

The repaired Opus-5 variance-recalibration idea is **scientifically and
competitively negative in this exact spelling**.  RVRC produced a coherent,
network-specific variance signal, but applying that signal to ALG026 made the
independent A/B cross-risk `1.0422%` worse.  It improved only 35 of 100 Mini
networks, and the 100,000-draw network bootstrap assigned probability
`0.00002` to a favorable mean change.  Its 90% change interval,
`[9.8403e-9, 2.3653e-8]`, is wholly harmful.

This is not a strict-gate-only miss.  The owner-approved flexible rule required
only a favorable point result after valid execution; the result was
unfavorable.  No candidate ID, tier, package, upload, or T119B is created.
`ALG026-V000` submission `329690` remains the local and official incumbent, and
the next task is the already-frozen **T120 COA-R** test.

| arm | cross-risk change vs ALG026 | reduction | wins / 100 | bootstrap P(mean improvement) |
|---|---:|---:|---:|---:|
| corrected RVRC | `+1.67499e-8` | `-1.0422%` | 35 | `.00002` |
| unshrunk radial measurement | `+2.57023e-7` | `-15.9916%` | 2 | `0` |
| radial-omission diagnostic | `+1.50873e-8` | `-0.9387%` | 37 | `.00003` |
| matched random direction | `+3.96312e-7` | `-24.6580%` | 1 | `0` |
| cyclic source shuffle | `+8.10349e-5` | `-5041.8784%` | 0 | `0` |

Source swap reproduced RVRC exactly.  The external 4% threshold also failed,
but it was diagnostic only and played no role in closing the branch.

## What was tested

The 100 public Phase-2 Mini networks were loaded using only `mlp_id`,
`mlp_name`, `mlp_seed`, and `weights`.  Every candidate/control prediction was
sealed before reading the pre-existing T115 independent audit-A and audit-B
endpoints.  No challenge target array was loaded.

For fixed-radius source mean `m_A` and centered variance `v_A`, the screen first
performed the required raw-moment radial repair,

```text
rho2 = R^2/1024 = 0.9995118380168916
v_G  = (v_A + m_A^2)/rho2 - m_A^2.
```

With closure variance `v0`, source discrepancies `dM,dC`, and local response
`J=phi(alpha)/(2 sigma)`, the sole selectable reliability was

```text
A = max(sum(J^2 dM dC), 0)
N = sum(J^2 (dM-dC)^2)/4
k = A/(A+N)
v_tilde = v0 + k (v_pool-v0).
```

The screen then recomputed terminal sigma, alpha, Gaussian ReLU mean, DFFH
action/reliability, closure weight, frame direction, SF feature, inherited cap,
and the unchanged frozen ALG026 AS grammar and coefficients.  There was no
coordinatewise target fit.

The external iid formula `12/49=.2448979592` was reported but not used because
an exact `1/R` variance law is unjustified for leverage-normalized antipodal
Stiefel clusters.

## Mechanism interpretation

The proposed measurement is real, but its proposed corrective direction is
wrong for the final estimator:

- source agreement was positive on 100/100 networks;
- `k` had mean `.28815`, median `.28638`, and range `.03888–.48928`;
- the median within-source-half to cross-source noise ratio was `2.173`, inside
  the prospectively frozen order-of-magnitude coherence band;
- nevertheless, RVRC increased risk, and the unshrunk arm was much worse.

Thus the screen supports “main and child agree on a terminal variance
discrepancy” but rejects “moving the closure variance toward that measured
discrepancy improves ALG026.”  Plausible explanations are that the analytic
closure variance is already better aligned to mean-output error after the
transferred AS observer, or that the empirical second-moment discrepancy
contains shape/aliasing error that is coherent between source designs but is
not a useful variance-bias correction.  The experiment does not distinguish
those explanations by itself.

The negative result was unsurprising: the frozen loss probability was `.62`,
so it carries only `.690` bits of surprise.  The coherent-mechanism result
carries `.862` bits under its `.55` prior.

## Important nonselectable SRR lead

The predeclared studentized-shape readout was attribution-only and could not
rescue RVRC.  Nevertheless, it improved the *closure-only* cross-risk by
`3.91595%`, won 90/100 networks, and had bootstrap probability `1.0` of a mean
improvement.  This is not a full ALG026 head-to-head: the closure baseline is
much weaker than the composed incumbent, the frozen AS observer was not rebuilt
around SRR, and no candidate was qualified.  It therefore creates no T119B.

It is, however, a strong new lead: measured standardized shape appears useful
even though replacing the closure variance is harmful.  Preserve SRR as a
high-priority T122 recurrence input after the already-frozen T120/T121
decisions; do not describe it as rejected merely because RVRC failed.

## Integrity and operational record

All fixtures passed:

- instrumented and official ALG026 parent arrays were byte-identical;
- direct `k=0` parent parity held on all 100 networks;
- source swap was exact (`max_abs=0`);
- final-weight 2x homogeneity had zero relative RMS error;
- output-permutation maximum difference was `3.5763e-6`;
- every result was finite and nonnegative.

An independent replay verified all per-row hashes and recomputed parent
cross-risk `1.6072355297709455e-6` and RVRC cross-risk
`1.6239854175277428e-6` from the cached predictions and A/B audits.

The first attempt stopped before writing row 0 because an experiment helper
used unsupported in-place addition on a metered immutable array.  The one-line
repair was retried successfully.  After both 100-row passes, an all-16-layer
2x scaling fixture overflowed the covariance symmetry certificate; the
fixture was repaired to the relevant and exact final-matrix 2x homogeneity
law.  The sealed prediction rows were resumed unchanged.  Neither incident is
candidate evidence, neither required owner action, and no intermittent machine
failure occurred.

## Timing

- Start: `2026-09-04T08:40:09,307855605-07:00`
- Pre-task estimate: **75 minutes**
- End/checkoff: `2026-09-04T09:48:30,860325964-07:00`
- Actual elapsed: `01:08:21.552470359` (`4101552470359` ns)
- Estimate difference: completed `00:06:38.447529641` earlier than the point
  estimate

Approximate exclusive allocation: 7 minutes protocol/formula audit; 13 minutes
implementation, two local repairs, independent verification, and durable
documentation; 49 minutes deterministic program execution/monitoring.  The
100-row primary pass alone recorded `1474.318 s` (24.572 minutes); the exact
physical source-shuffle pass and four structural fixture propagations dominate
the rest of the execution time.
