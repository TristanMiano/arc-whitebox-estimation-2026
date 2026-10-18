# T173 final selection

**Select ALG058-V001 / 336809 and ALG055-V000 / 336785 for the Phase 2 private re-evaluation.** This is the completed selection decision for owner review. The AIcrowd nomination interface has not been changed; that action is reserved for T174.

| Role | Algorithm | Accepted submission | Current official adjusted score | Reason |
|---|---|---:|---:|---|
| Primary | ALG058-V001 | 336809 | 2.971106406126817e-9 | Best official score; equal average of our trace and context sources, batched with separate normalizers |
| Second entry | ALG055-V000 | 336785 | 2.982822327838572e-9 | Simpler trace-only source; close enough that fresh private networks could reverse their order |
| Reserve, not selected | ALG054-V000 | 336778 | 3.0332910471237746e-9 | Removes our new neural sources, but has weaker official and paired-development evidence |

All three live grades were rechecked on 2026-10-18. All still report `graded`, with scores unchanged. Exact archived bytes and all qualified source-file hashes match their preserved qualification records and current shipped directories. See `CURRENT_GRADES.json` and `PACKAGE_IDENTITY_AUDIT.json`.

## Why these two

ALG058 improves on ALG055 by 0.3928% officially and 0.1702% on the twelve exposed development networks. The final local comparison wins8/12, with descriptive bootstrap support0.89306; the interval includes a tie. ALG055 wins four of those individual rows. Their public scores are close enough that keeping both is a reasonable hedge on the fresh private mean. This is not a claim that they are independent methods or that resampling support measures private-suite win probability.

ALG055 improves on ALG054 by1.6638% officially and2.2284% in the twelve-row comparison, winning11/12. Giving the second slot to ALG054 solely for architectural diversity would discard stronger evidence for ALG055. ALG054 still uses fitted covariance coefficients and the public engine's fitted tables, so it is not a parameter-free alternative. Reconsider it only if a concrete new eligibility, evaluator, or resource issue affects the selected entries.

The unsubmitted variants do not justify a final slot: ALG056 lost its larger development comparison; ALG057 was effectively tied and did not establish a gain; ALG058-V000 failed a residual-time qualification case and was superseded by the accepted V001 batch. Older entries have substantially worse recorded adjusted scores and older runtime evidence.

No new fitting, estimator inference, expanded validation, protected blind evaluation, code modification, upload, or final nomination was needed for this decision. Existing official and qualification evidence was reused.

## Exact artifacts

- Primary archive: `experiments/theory/t172/candidates/ALG058-V001/ALG058-V001.tar.gz`
  SHA-256 `2c28711f6d44709182886eb6e1535503af415ecd97721b46868b39f2ff0660db`.
- Second archive: `experiments/theory/t172/candidates/ALG055-V000/ALG055-V000.tar.gz`
  SHA-256 `d8d1b905632e0e5937ed3f61a6ca86b2e4afb9f28366d6a4f32c185f29ebc394`.

Nominate the already accepted submission IDs, without repackaging or reuploading them merely to finalize selection. The score winner is determined by the organizer's fresh private evaluation; the two nominations do not form a per-network routing ensemble.

## T174 actions after owner review

1. Apply any author corrections to the draft report, which corresponds to exactly one submission: **336809**.
2. Confirm the organizer has announced no further material evaluator or deadline change, then use **Submissions → Your team → Select** for336809 and336785. Save confirmation of both selections.
3. Prepare the final PDF and the selected public evidence/code release. Preserve upstream MIT notices and make our own changes easy to locate. Do not publish the entire research workspace or private challenge weights/labels.
4. With explicit authority for external delivery, publish the PDF on the challenge forum (recommended) or email it privately. State the single associated submission ID336809. Save the delivery URL or receipt.

The organizer requires substantial own changes to participant code, not attribution alone. Our report documents the covariance/source adaptations and their incremental measurements, without claiming advance eligibility approval. Public release and final writeup delivery are not completed in T173.

## Current deadlines

The October17 organizer announcement supersedes older dates still visible in some rules copies:

| Action | UTC deadline | America/Los_Angeles |
|---|---|---|
| Code submissions close | October21,2026 23:59 | October21,4:59p.m. PDT |
| Nominate up to two submissions | October22,2026 23:59 | October22,4:59p.m. PDT |
| Algorithmic-contribution PDF | October28,2026 23:59 | October28,4:59p.m. PDT |

Sources: [deadline and selection update](https://discourse.aicrowd.com/t/18251), [PDF + exactly one graded ID; delivery channels](https://discourse.aicrowd.com/t/18041/4), [public-code clarification](https://discourse.aicrowd.com/t/18240). Read-only organizer snapshots are preserved under `sources/`.
