# WhestBench 2026 — Team LordProcciuto, best submission (e30_a)

Our best scored submission to the ARC White-Box Estimation Challenge 2026 (Phase 2, AIcrowd):

| Submission | Score | MSE (approx.) | Cost (approx.) |
|---|---|---|---|
| 335981 (`e30_a`) | **3.1163e-9** | ~2.0e-8 | ~158 u (u = 2^31 FLOPs) |

> **Notice.** Our full write-up (a census of public chains, 111 closed avenues with the
> condition under which each would work, the levers we could not use, and open questions) is in
> [`WRITEUP.md`](WRITEUP.md). We meant to post it as a topic on the AIcrowd forum, but new forum
> accounts cannot open topics there (trust level 2 is required), so it lives here instead.

## Contents

- `estimator.py` — the submitted estimator, byte-identical to the scored package
  (sha256 `6ddd97a96c30397683815c530bfb422f0a49ffdea49e4f7827149ed0a14729b0`).
- `manifest.json` — the package manifest (whestbench 0.16.1, flopscope 0.12.1, Python 3.14).
- `e30_a.tar.gz` — the exact package that was uploaded.
- `WRITEUP.md` — our full write-up (see the notice above).

## Provenance

The estimator is a modified version of 504aldo's public V29 estimator
([504aldo/whest-p2-cumulant-k3](https://github.com/504aldo/whest-p2-cumulant-k3), MIT).
Our changes are calibration knobs and cost trims on top of V29 (e30_a = our e29 cost
trims + `X_VB_HOT 3.0`, `X_LAM_TILT -0.1`, `X_DEAD_TAU 2.85`, `V21_R_OLD 416`, baked in).
Code comments are partly in Spanish.

Disclosure: an LLM (Claude) was used for this work.

## License

MIT (see `LICENSE`), keeping 504aldo's original copyright notice.
