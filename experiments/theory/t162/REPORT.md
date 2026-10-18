# T162 — empirical theory recurrence

**No submission nominee. ALG050-V000 remains the official best**, submission
331607, adjusted4.544342423060378e-9. The round narrowed the larger fourth-order
route substantially, but did not produce an affordable challenge-width
algorithm with convincing score evidence. Both interruptions were recovered;
their gaps are excluded from active research. Active research totaled **240.00 minutes**: 77.94 derivation, 117.69 empirical, 31.39 literature and 12.98 selection. Final measured timing is in
[TIMING.json](TIMING.json).

## What changed our assessment

The most useful positive evidence came from a persistent fourth-order state.
At generated width256,32signed quadratic factors with full inner matrices
reduced raw MSE42.2% against the public augmented-third recurrence. The wider
384network had a nearly tied point estimate, but its reference was too noisy
to conclude that the full state had stopped helping. Reducing each inner matrix
to rank16, even with diagonal/trace repairs, clearly damaged the result.
This points to representation loss as a concrete obstacle, not a proven
failure of fourth-order propagation.

A retrospective half-blend of the full fourth and third predictions reduced
raw error54.6%/62.0% on those256/384networks. This is a useful research signal,
with important limits: the blend was selected after inspecting the errors,
the networks are generated development cases, and a literal implementation
pays for both recurrences. It does not prove that halving a fourth tensor
inside the recurrence works. It suggests investigating a compact, controlled
residual while keeping the incumbent's existing state.

A diagnostic constant-plus-scale projection explains only1.7%/16.5% of the
correction energy on those two networks, so this signal is mostly richer than
a simple output rescaling. That does not rule out a useful small learned head;
its current-incumbent combination remains an explicitly untested reserve.

| Generated recurrence | Width128, seed16223 | Width256, seed16232 | Width384, seed16243 |
|---|---:|---:|---:|
| Public augmentedthird baseline | 1.96270e-5 | 9.15537e-7 | 4.43898e-7 |
| Full SIMPLE fourth | 8.36005e-6 | Not run | Not run |
| Signed pair8, full inner matrices | 5.14205e-6 | 1.11517e-6 | Not run |
| Signed pair32, full inner matrices | Not run | 5.28958e-7 | 4.42323e-7 |
| Pair32, inner16 plus exact diagonal | Not run | 8.84859e-7 | 9.44500e-7 |
| Trace-only fourth | 4.62592e-5 | 1.15776e-6 | Not run |

Entries are raw final-layer MSE, not adjusted scores. None is a comparison
with ALG050. They use one weight realization per column, except additional
width128seed tests linked in the probe log. Four independent reference batches
quantify reference noise, not network-to-network generalization. See
[P55](P55_WIDTH_TRANSFER_ANALYSIS.json) and [P56](P56_RESPONSE_STRENGTH.json).

## Theory and representation progress

We now have an independently checked finite Gaussian fourth-birth polynomial
and a shared incoming-fourth response generator for mean, covariance, third
and fourth cumulants. Those equations make it possible to test a declared
approximate closure without mixing unrelated scalar and tensor corrections.
The residual Gaussian triangle omission is explicit. Earlier star/binary
prototypes did not include the complete Gaussian chain and do not reject it.

The experiments also distinguish three different approximation problems:
native quadratic-pair rank, fully symmetric tensor rank, and the downstream
response metric. They are not interchangeable. A stable matrix sketch can
still preserve the wrong quantity. Direct fitting to analytic queries helped,
but a flexible core overfit those queries more than a simple diagonal fit.

An exact full-matrix trace repair reduced one-step fourth response error from
43% to11% and97% to24% at two saved full-width layers. Yet trace-only and
trace-plus-diagonal recurrent states lost substantially. Trace conservation is
valuable information, not a complete state. Removing trace before compression
also provided only a small repair of an otherwise weaker variant.
The remaining task is to retain enough non-trace response at affordable cost.
[Derivations](SCRATCHPAD.md), [trace capacity](P52_TRACE_QUARTIC_CAPACITY.json),
[known-future query test](P59_KNOWN_FUTURE_QUERY_CAPACITY.json).

For positive-state alternatives, we found a concrete quadratic-Gaussian
skewness/kurtosis obstruction. A common binary mean/covariance mixture can
match the examined marginals but fails joint variance constraints in the
tested constructions. These are useful eliminations of specific shortcuts;
they do not exhaust higher-chaos or multiple-mixer states. Literature supplied
indefinite-sketch stabilization, implicit-moment tools and conservative
compression ideas, but no ready cheaper challenge algorithm.
[Literature and read scopes](LITERATURE.md).

## What disappointed, and what is unfinished

The cheap retained-ray fallback's two-network win did not survive expansion:
six-network adjusted ratio1.009586,3/6wins, descriptive bootstrap support.1565.
Other current/post/future compression variants either lost raw accuracy or
spent more arithmetic than their raw improvement justified. More local
rigor would not turn these into attractive submission candidates.

The larger route is still missing its integrated width1024 implementation.
We have not shown that an accurate compact constructor, fourth-to-cubic feed
and history transport all fit the budget together. The positive small-network
results are therefore capacity evidence, not a nearly qualified submission.
The public augmented-fourth width128 run remains interrupted and unscored;
the restart's cause is unknown. Its heavy research implementation will not
be retried unchanged. Exact source and failed/partial outputs are preserved.

## Effort, experiments and provenance

The authorized floor is240active research minutes, including at least60written
mathematics. The final category totals and excluded interruptions are recorded
separately in [TIMING.json](TIMING.json); overlapping compute is counted once.

There were **37 completed full-width calls**, on six previously exposed public
development networks, totaling **19.744T metered FLOPs** and **22.394 prediction
minutes**. These include retained first calls from interrupted batches and
one replay. Parent evidence was reused, not rerun. There were **57 completed
generated-network recurrences**, including baseline methods and observer
replay, with **41.987 measured recurrence minutes**. Reference generation,
failed work and every analysis kernel are not fully timed, so these are
subtotals, not total machine consumption. [Cost/source inventory](COST_AND_SOURCE_INVENTORY.json).

No new challenge-label coefficient fit, agent work, blind-block access or
upload occurred. Analytic-query least squares and adaptive generated-error
inspection are disclosed; the work is not claimed to be purely deductive.
The main cumulant framework is published prior art, with our representation,
trace and response adaptations. Novelty is separate from usefulness.

## Next recommendation

Continue research with a finite, response-oriented fourth residual, and obtain
a full-width cost/accuracy signal early. The subjective chance of this larger
route yielding an official improvement within another8–16hours is25–45%,
with10–30%conditional adjusted gain. Those are planning judgments, far below
a submission-ready claim. Keep cheaper NIG/readout reserves available and
allocate some effort to a genuinely different capacity question.

[Candidate inventory and probabilities](CANDIDATE_SELECTION.md),
[route saturation](ROUTE_UPDATE.md), [runnable continuation](CONTINUATION.md).
T163 is proposed only; no next task starts automatically.
