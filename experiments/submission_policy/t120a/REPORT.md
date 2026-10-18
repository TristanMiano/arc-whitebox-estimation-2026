# T120A production and submission audit

## Current disposition

**The inherited T120 cost claim does not cover its frozen R3 implementation.**
R3's cache retains the original ALG026 closure's gate masks and rounded source
reconstruction. The complete parent closure cannot simply be subtracted from
the cost, as `T120/COST_COMPONENTS.json` did. A production implementation that
shares the common prefix and retains the required parent features meters at
**245,269,647,291 FLOPs**, multiplier **0.11153572235843967**. This is
25,367,321,735.8 FLOPs above the 0.1-floor boundary. It remains comfortably
below the actual competition budget of 2^41 FLOPs. This distinction matters:
0.1 is a frozen T120A design requirement, not an official eligibility limit.

T120A is **not checked off and no upload has occurred**. A concrete diagnostic
archive is available at `packages/ALG027-V000-UNQUALIFIED.tar.gz`, SHA-256
`9c52ef88fedf69206e9fc64cc1874f2b36702bb4ffb9662faf955fc5e0dc94c1`.
Its source is `submissions/phase2_alg027_v000/`. It is explicitly marked
unqualified and must not be mistaken for the sealed T120 prediction identity.

## Why the proposed one-closure implementation is not R3

`build_td_arm_cache.py` replaces `row_for_design["closure_weight"]` but leaves
`row_for_design["alpha"]` pointing to the parent K2 closure. The inherited
`build_trace_arm_cache.design` uses that alpha for four gate-dependent columns.
The TD alpha cannot replace it without changing the frozen output. On each of
the target-free fixtures 750, 850, and 999, two gate classifications differ.
Substituting only TD masks changes respectively 842, 666, and 595 output
coordinates, with maximum absolute changes 8.7351e-5, 5.6602e-5, and 1.2827e-4.
These are diagnostic counterexamples, not new candidate selections.

The source reconstruction also uses the parent's rounded frame direction and
closure weight. Production therefore reconstructs these quantities in the
same order as the cached formula instead of substituting the mathematical
unrounded main/child means. `CLOSURE_DEPENDENCY_AUDIT_LINUX.json` preserves the
counterexamples and byte-exact replay of the original frozen formulas.

The implementation shares the first eight linear covariance steps, retains
the main terminal cloud before the child overwrites its workspace, and reuses
both propagated clouds for the trace contractions. It omits unused parent
arms, unused half-frame moments, unused parent TD moments, and terminal
postactivation covariance calculations. These removals preserved the complete
production output byte-for-byte across Linux attempts 001, 002, and 003.
Cost fell from 245,509,997,043 to 245,269,647,291 FLOPs. This audit does not
claim a mathematical impossibility theorem for all future exact accelerations;
it falsifies the inherited component-subtraction argument and records the
bounded production work actually qualified here.

## Historical byte-parity gap

On global row 850, the integrated trace statistic, TD closure path, terminal
alpha/sigma/pdf, predicted angular skew, and sampled residual skew reproduce
T120's sealed values exactly on Linux. Applying the production composition
to the original cached primitives also reproduces all its design arrays and
the final sealed R3 output exactly.

The end-to-end production output nevertheless differs from the historical R3
seal in 49 of 1,024 final coordinates, by at most **2.384185791015625e-7**.
Its mean squared numerical difference is **1.5730145236146552e-16**. This is
small, but T120A explicitly requires byte equality, and that requirement has
not been silently relaxed.

The discrepancy is inherited: the unchanged T118 primitive generator, run
with its original source and original Linux package versions, also differs
from its old cached partial frame by 9.5367431640625e-7 and from its old K2
alpha by 7.860362529754639e-6. Repeated isolated partial-frame calls are
deterministic, and both old/current Linux stacks agree with each other.
Two- and four-thread diagnostic runs produce other deterministic results but
do not recover the cache. These are environment diagnostics; the proposed
submission does not alter thread settings or use accounting internals.

The unchanged official ALG026 archive also reproduces a small difference from
its historical H seal today: maximum 2.9802322387695312e-6, numerical MSE
3.543988232808553e-13. Its old numerical-tolerance gate passes, but it is not
byte-exact. The historical evidence files have not been rewritten. The cause
of this inherited reproducibility difference remains unresolved; the audit
does not attribute it to a particular host fault without evidence.

## Operational evidence

| Check | Observation | Disposition |
|---|---|---|
| Frozen parent coefficients, gamma, R3 delta | Exact literal equality; no refit or coefficient search | PASS |
| Target access | Only public network inputs and sealed predictions/primitives; no targets | PASS |
| Whest contract | Current 0.16.0 validator accepts Estimator | PASS |
| Static imports | No raw NumPy, SciPy, Torch, ctypes, or subprocess imports in candidate | PASS |
| Output | Finite, nonnegative, full 16 by 1024 | PASS |
| Replay | Complete output byte-identical on repeats | PASS |
| Fallbacks | Exact parent on zero/diagonal/full-parent budget routes and unsupported shape | PASS |
| Integrated charge | 245,269,647,291, deterministic | PASS for actual 2^41 budget |
| Frozen 0.1 multiplier | 0.11153572235843967; exceeds by 0.01153572235843967 | BLOCKED-OPERATIONAL specification/cost gap |
| Historical R3 bytes | 49 changed coordinates; max 2.384185791015625e-7 versus required zero | BLOCKED-OPERATIONAL parity gap |
| Setup / prediction wall | About 0.001 seconds / 17.2 seconds | PASS |
| Peak process RSS | About 4.61 GB versus 8 GiB | PASS |
| Residual cap | Direct source 0.397771/0.394269s passes; extraction attempts 001, 002, 003 each have a miss; last attempt 0.396905/0.409354s | BLOCKED-OPERATIONAL; maximum final-source extraction excess 0.009354s |
| Archive/extraction/manifest | Exact hash, expected files and hashes, no prohibited imports | PASS |
| Official upload/grade | Not run | NOT-RUN |

Windows-native execution was tried first. It passed shape/finite/nonnegative,
wall, memory and budget checks, but showed platform numerical differences and
1.0944 seconds residual. The same source was then tested on the current Linux
WhestBench 0.16.0 / FlopScope 0.12.0 stack. Original source and per-attempt
hashes are retained in `attempts/`. A missing SciPy dependency in the initial
Windows static diagnostic was bypassed using the unchanged Linux diagnostic;
SciPy is not a submission dependency. The first package command selected a
single file; Whest correctly refused to omit its sibling modules. Packaging
the folder fixed that invocation without changing the estimator.

## Consequence for the earlier score claim

The recorded T120 raw prediction evidence and physical trace mechanism signal
are retained. Its 14.025609% adjusted-score reduction used the unqualified
0.1 cost assumption. That number is no longer a qualified production claim.
If the sealed raw predictions were reproduced at the measured integrated
cost, the corrected adjusted proxy would be 1.4317655552220347e-7, ratio
0.9589215820442126 to ALG026: a **4.107842% projected reduction**. This is
arithmetic cost correction, not a newly scored production result or an
official grade. No protected targets were opened to calculate it.

ALG026 submission 329690 remains the official best. ALG027's favorable
mechanism evidence and N1 provenance remain visible; this is not a scientific
negation of the trace mechanism. Historical P1/R1/P2 remain not run/deferred.
The original T120 surprise statement is preserved as historical: its >=10%
adjusted-win event is not established for the actual production cost.

## Human promotion disposition

- Subject/evidence: ALG027-V000; production consolidation, identity and cost audit.
- Highest retained evidence: T120 current-shape M1 and favorable raw prediction
  comparison; the claimed 0.1-cost adjusted gain is not production-qualified.
- Blocker: OPERATIONALLY_BLOCKED, with incomplete production evidence.
- Strict gate sole: no. Historical-byte parity and a false cost composition
  both conflict with the frozen task; residual readiness is also marginal.
- Immediate credible unlock: prospectively authorize a separately identified
  production realization using measured cost and a recorded numerical
  equivalence contract, keep the coefficients fixed, and verify its actual
  adjusted comparison and hard resource gates before any upload. That changes
  the explicit T120A frozen identity/cost requirements and needs owner direction.
  No reboot or owner machine intervention is indicated.

T121 has not started and remains standalone from ALG026. No arm was reselected,
no coefficient was refit, no scientific tier was inherited from an official
score, and no final designation was made.

## Timing and continuation

The task started at 12:16:20 PDT on 2026-09-04 with a 150-minute estimate.
The first audit pause was recorded at 12:43:05 PDT, elapsed 26m45s; this is
not a task checkoff or completion time. Approximate allocation to that point:
6 minutes analysis, 14 minutes implementation/debugging/documentation, and
6m45s execution/wait. Final elapsed time and estimate error remain unreported
until the numbered task actually completes. The owner scope question was sent
during work; the agent continued recording and verifying this audit meanwhile.
