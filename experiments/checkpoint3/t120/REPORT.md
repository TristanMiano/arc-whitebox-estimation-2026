# T120 report — COA-R direct competition decision

## Outcome

**The frozen R3 arm is the new local project-best submission candidate,
registered as `ALG027-V000`.** On the prospectively declared primary pool of
Full V_D and H rows 750--999 it scored adjusted `1.2836834020053274e-7`
against byte-parent `ALG026-V000` at `1.4930997299798193e-7`: ratio
`.8597439114282592`, a **14.025609% reduction**, with 249/250 network wins.
The deterministic network bootstrap gives `P(win)=1` and a 90% adjusted-change
interval `[-2.2005806e-8,-1.9890444e-8]`. This is a direct competition-screen
succession under the owner's flexible rule, not a claim of final rigorous
scientific confirmation or an official leaderboard result.

R3 passed separately on both diagnostic panels: V_D adjusted
`1.2537144217175134e-7` versus `1.447994541241321e-7` (ratio `.865828141`,
99/100 wins), and H adjusted `1.3036627221972032e-7` versus
`1.5231698558054847e-7` (ratio `.855887948`, 150/150 wins). The worst pooled
network ratio is `1.0035371`, median `.8680911`, and p95 `.9383754`.

If the pooled local ratio transferred unchanged to the current official
ALG026 grade, the inferred leaderboard result would be approximately adjusted
`1.271703860e-7`, raw final-layer MSE `1.271703860e-6`, and `9.4362x` versus
sampling. That is a projection, not a grade. It remains above the `1e-7`
adjusted milestone.

## Frozen arm comparison

All arms remain on the `.1` score-multiplier floor, so the required raw ratio
for a point win is exactly `<1`.

| Arm | Mechanism role | Exact conservative FLOPs | Pooled adjusted | Ratio to R0 | Wins | Bootstrap P(win) | 90% adjusted-change interval | Cap-active coordinates |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| R0 | byte-parent ALG026 | 218,819,123,305 | 1.493099730e-7 | 1.000000 | 0/250 | 0 | [0,0] | 0% |
| R1P | physical trace-projected carrier rebase, frozen AS | 218,980,769,838 | 1.439449722e-7 | .964068 | 203/250 | 1 | [-6.0431e-9,-4.6950e-9] | 6.59297% |
| R1O | parent plus two fitted residual trace columns | 218,980,769,838 | 1.489199314e-7 | .997388 | 145/250 | .99004 | [-6.6941e-10,-1.1575e-10] | .96016% |
| R2 | physical late trace/diagonal closure, frozen AS | 219,103,780,909 | 1.485762700e-7 | .995086 | 130/250 | .94166 | [-1.5140e-9,3.4685e-11] | .00781% |
| R3 | R2 plus trace columns and anchored 14-column AS update | 219,265,427,442 | **1.283683402e-7** | **.859744** | **249/250** | **1** | **[-2.2006e-8,-1.9890e-8]** | 5.26563% |

R1P matters for attribution: a target-free physical trace rebase with the
already-frozen parent coefficients improves the pooled point score by 3.5932%
and has a wholly favorable interval. R2 is only a weak point improvement, so
the late TD replacement alone is not the main gain. The large R3 increment is
the Full-F-fitted re-anchoring of the late-TD design plus its two trace
columns. Its fivefold F result was also favorable (`1.286982e-6` versus
`1.495884e-6` for R2), and the gain transferred consistently to both held
panels. Thus the evidence supports both a physical trace mechanism and a much
larger fitted composition effect; it does not establish that every component
of the fitted update is individually necessary.

## Integrity and feasibility

- All eight trace identities/metamorphic fixtures passed; the largest scaled
  numerical error was `3.82e-14`. The explicit symmetric-tensor projection
  matched to `1.67e-16`.
- All 1,000 trace and all 1,000 late-TD rows were generated from public input
  columns only and hash-sealed before F fitting or V_D/H scoring. Trace and TD
  residual maxima were `.30527 s` and `.04013 s` respectively.
- The mechanism was active on 100% of the 750 fitted/decision rows. Both pooled
  held-source trace-action inner products were positive (`.0279780` and
  `.0280577`), so the only frozen cheap-stop rule did not fire. Mean source
  trace-action cosine was `.8010`; mean trace energy outside the inherited AS
  action basis was `.98849` (median `.98983`).
- Every scored array has the required terminal `(networks,1024)` shape and is
  deterministic, finite, and nonnegative. R3's conservative composed cost is
  `219,265,427,442`, leaving `636,898,113.2` FLOPs below the `.1` floor
  boundary. The production design reuses ALG026's main/child clouds rather
  than paying the standalone experimental cache-generation pass.
- The first audit found that cache-recomposed R0 differed from qualified
  ALG026 by up to `2.38e-7` per coordinate due solely to precision of cached
  components. The original scored files are preserved. The prescribed
  baseline-only repair replaces R0 with T118's target-free, package-qualified
  `dffh_as` predictions. Candidate bytes and coefficients did not change; the
  R3 ratio moved only from `.8597438970` to `.8597439114`. See
  `PARITY_REPAIR.json`.
- A transient Python/zip close error occurred on the first R1O fit. The exact
  operation succeeded on retry; no semantic workaround or owner action was
  required.

T120 establishes executable numerical behavior and conservative component
cost, but intentionally does not create a submission archive. T120A must
consolidate R3 into the Phase-2 estimator interface, prove complete-route
fallback and prediction parity, meter the integrated route, check package
imports/determinism/wall/residual/memory, create an immutable archive, and—on
an owner instruction to execute T120A—upload and monitor it. This is an
operational evidence gap, not a scientific or strict-score rejection.

## Surprise and disposition

The frozen probability of any win was `.42`; observing one carries `1.252`
bits and is mildly surprising. The probability of at least a 10% win was only
`.10`; R3's 14.03% gain therefore carries `3.322` bits and is the materially
surprising result. The `.03` event of adjusted `<=1e-7` did not occur.

`ALG027-V000` receives current-shape M1 and local submission succession.
Historical P1, rigorous R1/P2 science, package qualification, official grade,
and final two-slot designation are all **NOT RUN**, not failed. The primary
blocker to an official result is `EVIDENCE_INCOMPLETE`/operational packaging,
not a strict gate. No owner-side intervention is needed now; the high-leverage
next action is for the agent to execute T120A when instructed. Standalone T121
CGMA remains frozen from ALG026, not outcome-composed with ALG027.

## Timing

- Start: `2026-09-04T09:53:23,523738603-07:00`
- Pre-result estimate: **2 hours 30 minutes wall clock**
- End/checkoff: `2026-09-04T12:02:23,438244413-07:00`
- Elapsed: `02:08:59.913979284` (`7739913979284` ns)
- Difference from estimate: `00:21:00.086020716` (`1260086020716` ns),
  `earlier_than_point_estimate`
