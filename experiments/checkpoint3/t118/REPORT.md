# T118 — exact-fast independent-frame and observer composition

## Outcome

T118 completed the frozen FC011 decision without post-target retuning.
**DFFH+AS is the new local project-best submission candidate and is registered
as `ALG026-V000`.** It beat official/local incumbent `ALG024-V000` on both
protected panels:

| Panel | ALG026 adjusted | ALG024 adjusted | raw ratio | wins | bootstrap P(win) | 90% adjusted-change interval |
|---|---:|---:|---:|---:|---:|---:|
| V_D 750--849 | `1.447994541e-7` | `1.658356018e-7` | `.873150593` | 86/100 | `1.00000` | `[-2.4094e-8,-1.7979e-8]` |
| H 850--999 | `1.523169856e-7` | `1.765268147e-7` | `.862854665` | 138/150 | `1.00000` | `[-2.6772e-8,-2.1679e-8]` |

The separate `ALG025-V000` early-anchor composition also point-won on both
panels, but weakly: V_D adjusted `1.654979180e-7` and H adjusted
`1.758170499e-7`, with both 90% intervals crossing zero. It is retained and
packaged as the mechanism-distinct second H winner, not the primary successor.
No upload occurred. T118A is inserted next to revalidate, upload, and monitor
the immutable ALG026 archive only when the owner instructs execution.

## Frozen protocol and chronological integrity

The T118 preanalysis was sealed before any T118 Full prediction or protected
target access. It prospectively repaired the one omitted child RNG constant to
`mlp.seed xor 0xD118C411`, before outputs existed. Its SHA-256 is
`47a731e1...ec84d`. The historical T116 surprise freeze was not mutated.

The chronological sequence was:

1. import the public MIT-licensed Phase-1 exact-fast source without semantic
   edits and implement the memory-bounded depth-5 wrapper;
2. run integer bit-exact and random floating parity tests, then qualify the
   frozen depth/child ladder in order;
3. select the first safe pair, `(5,1536)`, and freeze that selection;
4. qualify ALG025's production spelling;
5. fit only the scalar child pool and frozen 12-column AS grammar on F 0--499;
6. generate and hash every V_D prediction before opening V_D targets;
7. advance only novel V_D point winners, generate and hash all H predictions,
   then open H once; and
8. package the lawful H winners without uploading.

The 70 GB pinned Full cache had been cleaned after T117. It was restored from
the pinned revision and verified locally. A first resume command used a stale
snapshot hash and failed immediately before computation; the actual pinned
hash was resolved and the atomic row cache resumed successfully. No machine-
owner action was needed and no numerical run failed intermittently.

## DF0 parity, cost, and pair selection

Depths 2--5 were bit-exact on small integer fixtures. On twelve production
networks the selected `(5,1536)` pair had:

- invariant primitive-route charge `218,818,536,521` FLOPs per network;
- maximum residual wall time `0.2491 s`, below the frozen `0.4 s` limit;
- DF0 numerical error `1.659668072e-13` MSE versus the `2.9361e-7` reference
  scale, classified negligible;
- maximum absolute DF0 difference `2.861e-6`, aggregate signed mean
  `4.705e-9`, and maximum per-network signed mean `4.287e-8`;
- production-shape relative Frobenius error around `1.38e-5`; and
- exact package cost `218,819,123,305` FLOPs after charging tuple materialization,
  still on the `0.1` score floor with `1,083,202,250` FLOPs headroom.

The lower fallback pairs were not tried because the largest frozen pair was
fully safe. This is a positive operational result, not a scientific selection
from target outcomes.

## F fit and protected results

The F-fitted scalar was `gamma=.02120729323`, inside its `[-.5,.5]` bounds.
F raw MSE was `2.134520891e-6` for DF1 support, `2.134266039e-6` for the scalar
pool, `2.127641889e-6` for DFFH, and `1.500282595e-6` for DFFH+AS. The observer
frequently reached its fixed quarter-carrier-RMS cap; this was disclosed and
left unchanged before V_D/H.

V_D produced the following direct results versus ALG024:

| Candidate | novelty/role | adjusted | change | wins | P(win) | disposition |
|---|---|---:|---:|---:|---:|---|
| DF1 support | N0 engineering control | `2.041751021e-7` | `+3.83395e-8` | 5 | 0 | rejected competitively |
| DF1 scalar | N0 engineering control | `2.042790604e-7` | `+3.84435e-8` | 8 | 0 | rejected competitively |
| DFFH | N1 frame mechanism | `2.035644203e-7` | `+3.77288e-8` | 10 | 0 | exact spelling scientifically/competitively negative |
| DFFH+AS | N1 composition | `1.447994541e-7` | `-2.10361e-8` | 86 | 1 | advance to H |
| ALG025 | N1 hedge | `1.654979180e-7` | `-3.37684e-10` | 54 | `.66574` | weak point win; advance to H |

On H, DFFH+AS reconfirmed strongly at `1.523169856e-7`; ALG025 reconfirmed a
small point win at `1.758170499e-7` with bootstrap `P(win)=.8766` but its 90%
interval `[-1.7106e-9,2.9135e-10]` still crosses zero.

## Interpretation and surprise

The frozen prior for DFFH itself beating ALG024 was `.28`; its failure was
unsurprising (`.474` bits). Conditional on operational qualification, the
composition prior was `.62`; its V_D win was also unsurprising (`.690` bits).
Both H reconfirmations used the frozen `.75` prior and were unsurprising
(`.415` bits each).

The result rejects the idea that independent-frame capacity or DFFH pooling
alone is the competitive improvement: all standalone frame arms were about
23% worse than ALG024 on both protected panels. The large transferable gain is
the frozen analytic-synthesis observer when rebuilt on the independent-frame
parent. This distinction matters: the DFFH mechanism is negative in this exact
spelling, while the DFFH+AS composition is strongly positive.

ALG025 remains a competition hedge only. Its exact H002 early-generation
story was already scientifically rejected in T117B, and its small protected
point wins do not reverse that causal conclusion.

## Packaging and human disposition

| Subject | Highest supported status | Strongest evidence | Why not further promoted | Strict gate sole? | Next action |
|---|---|---|---|---|---|
| `ALG026-V000` | **local project best; current-shape M1; N1/dim-4; package-ready** | two protected wins; H `.862855x`, 138/150, P(win)=1 | no official grade; historical P1 and rigorous publication-grade science deferred | No | execute T118A to upload and grade |
| `ALG025-V000` | mechanism-distinct H-reconfirmed hedge; current-shape M1; N1/dim-4; package-ready | V_D/H point wins; H `.995979x`, 80/150, P(win)=.8766 | uncertainty crosses zero; much weaker than ALG026; H002 causal story negative | No | retain as second-slot hedge; no immediate upload priority |
| DFFH alone | exact spelling negative | V_D/H roughly `1.228x/1.232x` ALG024 | direct protected losses, not a strict gate | No | do not rerun unchanged |
| DF1 | N0 control, negative | V_D/H roughly `1.231x/1.235x` ALG024 | direct protected losses and no novelty | No | close control |
| `ALG024-V000` | official best, submission `329529` | official adjusted `1.715382969e-7` | locally superseded but not yet officially | N/A | retain official incumbent until T118A grades |

ALG026 archive `experiments/submission_policy/t118a/packages/ALG026-V000.tar.gz`
has SHA-256 `a1d66a380afd79e99411ac0ad564c6eba3cdb9939b5a1effb0b41f9d3a84eb9c`.
Its clean WSL qualification passed manifest, import, deterministic replay,
byte-exact H-seal parity, exact cost, residual, wall, and 8 GiB memory gates.
Peak process RSS was `4,813,869,056` bytes. Windows-native validation was not
available in this environment; T118A must rerun the hard gate before upload.

The ALG025 hedge archive has SHA-256
`886711213c6ab48d721a5a58fb218be56a7bc0a6f787380a801c5d24d0ecc53d`.
Its clean qualification passed at `170,689,646,501` FLOPs with numerical
parity MSE `3.165e-13` to the sealed dense reconstruction.

## Timing

The formal clock started at `2026-09-03T19:10:07,358559840-07:00`. The point
estimate was `8 hours` (planning range `6--15 hours`). T118 was checked off at
`2026-09-03T21:30:27,577671568-07:00`, for elapsed
`02:20:20.219496568` (`8420219496568` ns), `05:39:39.780503432` earlier than
the estimate. Approximate exclusive wall allocation was 20 minutes on
protocol/theory, 51 minutes on implementation/repair/packaging/documentation,
and 69 minutes on program execution, monitoring, and wait. Summed program
runtime was larger because the F generation overlapped active implementation.
