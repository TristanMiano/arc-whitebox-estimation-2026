# GPT-6 Astra handoff — ARC White-Box Estimation project

**Created:** 2026-09-04 PDT after T120/E109  
**Workspace:** `/home/trist/arc_challenge/arc_whest_seed_workspace`  
**Immediate next task:** **T120A**  
**Work currently running:** none; T120 is complete and T120A has not started

This is a high-signal replacement for the prior conversation context. Do not
assume access to that conversation. The durable project files remain the
authority; if a later-dated task result conflicts with this snapshot, follow
the later evidence and reconcile the pointers.

## First read, in order

1. `docs/OWNER_OPERATING_DIRECTIVES.md` — mandatory owner policies.
2. `TODO.md`, beginning at T119/T120 — T120 is checked off; T120A is first
   unchecked and precedes T121.
3. `experiments/checkpoint3/t120/REPORT.md` and `TERMINAL_RESULT.json` — result
   and promotion disposition.
4. `experiments/checkpoint3/t120/RUNTIME_SPEC.md`, `R3_FIT.json`,
   `PARITY_REPAIR.json`, and `ARTIFACT_MANIFEST.json` — exact winning spelling,
   frozen coefficients, repair boundary, and evidence hashes.
5. `state/algorithm_specs/ALG027-V000.json` — canonical winning identity.
6. `state/current_state.json` and `state/competitive_research_policy.json` —
   synchronized current queue and policy state.
7. For the packaging/upload pattern, read
   `experiments/submission_policy/t118a/README.md`, `REPORT.md`,
   `qualify_exact_package.py`, and `verify_evidence.sh`.

Do not begin by rerunning T120, reopening its arm selection, or changing R3's
coefficients. Begin T120A only when the owner explicitly instructs execution.

## Current status in one page

### Local best

**`ALG027-V000` is the local project-best submission candidate.** It is T120's
frozen R3 arm: the ALG026 exact-fast main/independent-child frame, with a late
order-12 trace/diagonal closure replacement, terminal trace residual, and a
Full-F-fitted anchored 14-column analytic-synthesis update.

Primary prospective comparison, Full V_D+H rows 750--999:

| Metric | ALG027 R3 | byte-parent ALG026 |
|---|---:|---:|
| Adjusted proxy | `1.2836834020053274e-7` | `1.4930997299798193e-7` |
| Ratio | `.8597439114282592` | `1` |
| Reduction | `14.025609%` | — |
| Network wins | `249/250` | — |
| Bootstrap P(win) | `1` | — |
| Worst network ratio | `1.0035370517` | — |
| Conservative executable FLOPs | `219,265,427,442` | `218,819,123,305` |
| Score multiplier | `.1` | `.1` |

V_D alone won 99/100 at adjusted `1.253714422e-7`; H alone won 150/150
at `1.303662722e-7`. The physical, unfitted R1P trace rebase also won by
3.5932%, so evidence for the trace signal does not depend solely on the fitted
R3 update. R2's late-TD physical arm gained only `.4914%`; most of R3's larger
gain comes from the anchored update, which transferred consistently from F to
both held panels.

The >=10% improvement outcome had frozen prior `.10`, making the 14.03% result
materially surprising (`3.322` bits). It did not reach the frozen `<=1e-7`
milestone.

Status: N1 novel combination/dimension 3, current-shape M1 awarded. Historical
P1, rigorous R1/P2 science, production-package qualification, official grade,
and final two-slot designation are **NOT RUN**, not failed. Under owner policy,
those scientific tiers are not prerequisites for submitting the best lawful,
at-least-somewhat-novel candidate.

### Official best

`ALG026-V000` remains the official best until ALG027 is graded:

- submission `329690`;
- adjusted `1.4791658804824692e-7`;
- final-layer MSE `1.4791658804824692e-6`;
- `8.112680x` versus sampling;
- immutable archive SHA-256
  `a1d66a380afd79e99411ac0ad564c6eba3cdb9939b5a1effb0b41f9d3a84eb9c`.

If T120's local ratio transferred exactly, ALG027 would project to adjusted
about `1.271703860e-7`, raw MSE `1.271703860e-6`, and `9.4362x`. This is only a
projection; never record it as an official score.

## Exact T120 integrity boundary

T120's target-free trace and late-TD caches cover all 1,000 Full rows and were
sealed before F fitting or V_D/H scoring. Trace identities, radial conversion,
source pooling, explicit symmetric-tensor projection, deterministic finite
nonnegative predictions, source-action signs, and conservative cost passed.
`experiments/checkpoint3/t120/verify_t120.py` is the final integrity check.

A post-score audit found that the first cache-recomposed R0 differed from the
qualified ALG026 output by at most `2.38e-7` per coordinate because primitive
components were recomposed at a different precision. The first artifacts are
preserved. The repair replaced **only R0** with T118's pre-existing target-free,
package-qualified `dffh_as` predictions. R1P/R1O/R2/R3 arrays and coefficients
remained byte-identical. R3's ratio changed only from `.8597438970` to
`.8597439114`. Treat `PARITY_REPAIR.json` as mandatory provenance; do not
misdescribe this as target-driven candidate tuning.

There was one transient Python/zip close error during R1O fitting. The exact
retry succeeded. No worker process is still running and no task needs recovery
from a partial computation.

## Execute T120A next

T120A exists because a local winner must be submitted immediately before more
research. Its goal is to turn the research R3 spelling into one immutable,
competition-valid `ALG027-V000` package and obtain its official grade.

Required sequence:

1. **Pull the start clock and write a wall-clock estimate before material
   execution.** The user wants start, estimate, end/checkoff, actual elapsed,
   and estimate error reported for every numbered task. Runtime estimation
   should be dominated by program execution, debugging, reruns, packaging, and
   grader waiting—not an assumption that prose reasoning itself consumes much
   wall time.
2. Preserve R3 exactly. Use `RUNTIME_SPEC.md`, `R3_FIT.json`, and the T120
   hashes as authority. Do not refit, introduce a coefficient grid, select an
   arm again, or access targets to repair production behavior.
3. Start from `submissions/phase2_alg026_v000/`, but integrate rather than
   naively append the TD route. The `.1` score-floor headroom is only
   `636,898,113.2` FLOPs. The conservative R3 count assumes the TD closure
   **replaces** ALG026's existing K2 closure and that terminal trace statistics
   reuse the existing main/child propagated clouds. Calling the complete
   parent closure and then a second complete TD closure, or repeating particle
   propagation, will exceed the intended cost and invalidate the result.
4. Consolidate a standard Phase-2 `Estimator` with byte-parent behavior for
   unsupported shape/insufficient budget. Preserve full `(16,1024)` output,
   final nonnegative projection, single `.25 * carrier RMS` correction cap,
   and frozen R3 formula `X_TD @ theta_parent + D14 @ delta`.
5. Prove integrated-route numerical parity against T120's sealed R3 outputs
   before packaging. The experimental generator used target-free cached
   primitives; diagnose dtype/order discrepancies rather than silently
   weakening parity or changing the candidate. If exact parity cannot be
   achieved without a semantic change, preserve evidence, make bounded
   self-repair attempts, and report an operational blocker rather than upload a
   different estimator under the same ID.
6. Meter the **integrated** route under the current WhestBench/FlopScope stack.
   Verify exact deterministic cost, `.1` multiplier, budget, finite and
   nonnegative output, complete shape, byte replay, fallback parity, wall time,
   residual `<.4s`, and process memory `<8 GiB`. The T120 cost is a conservative
   component composition, not a substitute for this final integrated meter.
7. Avoid the T117A failure: Phase 2 does not provide arbitrary raw NumPy.
   Candidate code should use permitted `flopscope.numpy` operations and pure
   Python fixed constants. Run a static prohibited-import check, `whest
   validate`, clean-extraction qualification, and archive-manifest/hash checks.
8. Create a dedicated `experiments/submission_policy/t120a/` evidence folder
   and immutable package. Adapt the proven T118A qualification/upload workflow;
   do not overwrite T118A evidence.
9. **Upload only after the owner says to execute T120A.** The current handoff
   request does not itself start T120A or authorize an upload. Under the
   standing directive, a future instruction such as “work on T120A” is
   sufficient authorization to revalidate, upload, and monitor.
10. Monitor to terminal status. For a generic evaluator hang/error, wait up to
    15 minutes, cancel if possible, revalidate and retry the exact unchanged
    archive once. If the second attempt also hangs for 15 minutes, stop and
    preserve state for later. A diagnosed compliance defect may be repaired
    only with prediction-identity proof and a new seal/archive hash.
11. If the grade beats official ALG026, announce the new official best in
    **bold** even though no P1/R1/P2 tier transfers. Update in the same change:
    `TODO.md`, `PROJECT_STATE.md`, `START_HERE.md`, `ALGORITHM_LEDGER.md`,
    `docs/OWNER_OPERATING_DIRECTIVES.md`, `state/current_state.json`,
    `state/competitive_research_policy.json`, `state/experiments.csv`, and the
    ALG027 canonical spec.
12. At actual completion, pull the end clock as the TODO box is checked and
    record all timing fields. Do not check off T120A merely because a grader job
    was created if the task's authorized monitoring/retry window is unresolved.

## Queue after T120A

- **T121:** standalone CGMA, built from ALG026 even though ALG027 won. Read
  `experiments/checkpoint3/t119/CGMA_SCALAR_SEAL.md` and
  `T121_IMPLEMENTATION_HANDOFF.md`. Compare valid arms to both ALG026 and
  ALG027. A win over ALG026 but not ALG027 is positive/superseded mechanism
  evidence. A win over ALG027 becomes the new local candidate and inserts
  T121A immediately.
- **T121A:** conditional only if T121 beats the then-current local best.
- **T122:** FC013 theory recurrence after both FC012 decisions are terminal.
  Default is at least 60 active minutes of written theory unless the owner
  overrides it. Inputs include the T119A SRR closure-only 3.91595% lead,
  RCERC/KCAS/RLCE, and T120/T121 result-direction evidence.

## Owner preferences and standing rules worth preserving

- Immediately stop spending compute on an exact candidate once it is genuinely
  scientifically or competitively negated; move to the next materially
  different candidate. Preserve promising strict-gate-only misses visibly.
- Submission policy is flexible: submit the best lawful, at-least-somewhat-
  novel algorithm. P1/R1/P2 are research tiers, not submission bans. Defer
  rigorous science until it is decision-relevant for the final best or a
  prospectively defined near-top candidate.
- Whenever one of our algorithms beats the prior project best on comparable
  evidence, say so in **bold**, make it the new submission candidate even if it
  misses P1, and insert an immediate submission task.
- Make it unmistakable why an algorithm was or was not promoted: distinguish
  scientific negative, strict-gate-limited, evidence-incomplete,
  operationally blocked, competitiveness-only, and support/control status.
- Report whether outcomes were surprising under the prospectively frozen
  beliefs. Preserve priors rather than editing them after results.
- Theory recurrence is high leverage. Default to 60 active written-theory
  minutes per cycle, but the owner's latest explicit duration overrides it.
  Maintain a written derivation ledger with equations, use prior rejections,
  and use public literature/contest disclosures when helpful.
- Machine containment: first diagnose and make bounded self-service attempts,
  including several safe exact retries to rule out transient errors. Either
  Windows native or WSL may be used; neither is assumed categorically more
  stable. A normally validated completed run is acceptable—there is no
  three-consecutive-clean-runs rule. Ask the owner to intervene only when an
  owner-only action is genuinely necessary and reasonably likely to help.
  Reboots are a last resort, not a default diagnostic.
- Reproduce substantive conclusions later on an independent stable machine or
  VM when practical; do not use that future reproduction requirement to halt
  ordinary competition progress now.
- Preserve the dirty worktree. Do not reset or discard unrelated user work.

## Quick consistency checks before resuming

```bash
.venv/bin/python experiments/checkpoint3/t120/verify_t120.py
.venv/bin/python -m json.tool state/current_state.json >/dev/null
.venv/bin/python -m json.tool state/competitive_research_policy.json >/dev/null
git diff --check
```

Expected state after these checks:

- `state/current_state.json.next_task == "T120A"`;
- local candidate `ALG027-V000`;
- official best `ALG026-V000`, submission `329690`;
- T120 checked, T120A unchecked, T121 unchecked;
- no T120 cache generator or grader process running.

