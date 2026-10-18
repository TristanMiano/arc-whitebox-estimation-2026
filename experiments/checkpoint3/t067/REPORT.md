# T067 — rigorous Cycle 1 freeze

## Decision

Rigorous Cycle 1 (`RC001`) is prospectively frozen around the singleton
`P1-promising` candidate `ALG014-V000`. No Cycle 1 reference, prediction,
score, ratio, or pass/fail outcome was opened. T068 is now authorized to run
the exact frozen program; T069 will adjudicate it.

The slate contains only `ALG014-V000` because it is the sole project P1 after
the two required post-first-P1 mechanism-distinct attempts, T092 and T094,
ended scientifically negative. This is a design/integrity event, not a new
empirical tier or submission-candidate succession result.

## Frozen identities

| Role | ID | Modeled FLOPs | Binding |
|---|---|---:|---|
| candidate | `ALG014-V000` | `247350948181` | identity `47accecf...`; exact T091A behavior/source |
| equal-work mechanism control | `ALG014-V002` | `247347893760` | identity `c72b1209...`; remove collective Stiefel dependence |
| actual incumbent comparator | `ALG003-V008` | `262549156608` | identity `68b9dd81...`; exact point asset and route specification |

The candidate/control work difference is `0.001234853%`. The incumbent is
evaluated as the actual algorithm identity through the frozen native
realization. The T065 parity scope does not establish packaged-Python bit
parity, Whest/flopscope billing, wall-time, or grader parity; any Cycle 1 P2 is
therefore native-stage competitiveness, not submission readiness.

## Fresh evidence and inference

Three immutable blocks—`RIG-RC001-B1`, `B2`, and `B3`—contain 24 new networks
each. Their 72 network seeds and 72 reference seeds are mutually unique and
disjoint from all tracked fast lanes. Each route uses eight independent
65,536-positive antithetic reference banks, or 1,048,576 effective reference
trajectories. The verifier confirms that the protected T068 output directory
contains zero files.

Cycle `j=1` receives one-sided familywise alpha `0.025`. With a singleton
slate, Holm has one rank. Both comparisons use a frozen 200,000-replicate
within-block network bootstrap and one-sided 97.5% upper ratio. Pair-specific
target-noise MDEs use eight-bank leave-one-out jackknife three-sigma values,
floored at `1.1e-12`, and must be sealed before a score or ratio is published.

R1 requires candidate/mechanism arithmetic adjusted-score ratios below one on
all three blocks and pooled, pooled upper 97.5% below one, benefit above the
MDE, p95 below `2.5`, maximum below `4.0`, and every identity, invariant,
budget, finiteness, T064, replay, and operation check. P2 additionally requires
R1, candidate/incumbent ratios at most `1.05` on every block and below one
pooled, upper 97.5% below one, benefit above its MDE, the same frozen tail
limits, and at least 11B modeled-FLOP reserve.

The p95/maximum rule is the prospective exception to the generic rigorous
maximum-1.5 default. E0004 had an overwhelming `0.546933` pooled mechanism
ratio but a `2.312252` maximum caused by volatile small per-network
denominators. The frozen rule retains a breadth constraint and catastrophic
limit without letting one known ratio pathology automatically veto rigorous
confirmation. It cannot be waived after output.

## Integrity verification

`freeze_t067_cycle1.sh` is idempotent: two successive executions produced the
same seal and manifests. `verify_freeze.sh` passed all hashes, route preimages,
cardinalities, uniqueness/disjointness checks, thresholds, and the unopened
outcome boundary. The independently retained T064 evidence verifier also
passed.

The first verifier invocation caught a missing final newline in the generated
route-hash preimage. The incorrect prospective manifests and seal were removed
and regenerated after fixing the generator. No T068 directory or empirical
output existed, so candidate identity, scientific rules, and evidence were not
affected. No owner action was required.

Reproduce the freeze verification with:

```bash
bash research/native_checkpoint3/freeze_t067_cycle1.sh
T067_REQUIRE_UNOPENED=1 bash experiments/checkpoint3/t067/verify_freeze.sh
bash experiments/checkpoint3/t064/verify_evidence.sh
```

## Human promotion disposition

- Subject/evidence class: `ALG014-V000`, prospective native RC001 freeze.
- Current/highest/next tier: `P1-promising` / `P1-promising` /
  `R1-mechanism-confirmed`, then `P2-competitive`.
- Positive evidence: retained E0004 pooled candidate/iid `0.546933`, `24/32`
  wins, bootstrap upper `0.678312`, maximum `2.312252`, and incumbent context
  `0.864198`.
- Gates: identity, slate, comparator, block, multiplicity, metric, MDE, tail,
  and outcome-containment freezes are `PASS`; R1 and P2 empirical gates are
  `NOT-RUN`.
- Primary blocker: `EVIDENCE_INCOMPLETE`. No strict gate has failed and a
  strict gate is not the reason R1 is absent.
- Plain-language reason not yet promoted: no rigorous outcome has been run.
- Immediate high-impact unlock: agent executes T068 on all three sealed blocks
  and T069 adjudicates; no owner action is required.
