# Independent Exact-Head Review Receipts

Status: implementation contract.

## Purpose

HC qualification already distinguishes authorial, hostile, independent-secondary, Warden, and implementation evidence. This contract adds a small machine-checkable receipt format for a review that is claimed to be both independent and bound to one exact commit.

The receipt does not decide whether a reviewer is truly independent in the philosophical or organizational sense. It makes the claimed scope, reviewer relationship, exact subject commit, evidence, result, and claim ceiling explicit enough for tooling to reject obvious provenance laundering or stale-head reuse.

## Machine contract

Schema:

`specs/HC_INDEPENDENT_REVIEW_RECEIPT_V1.schema.json`

Reference validator:

`tools/qualification/validate_review_receipt.py`

Tests:

`tools/qualification/test_validate_review_receipt.py`

Example validation:

```bash
python tools/qualification/validate_review_receipt.py receipt.json \
  --expected-repository thebrazenbeard/hc-brain \
  --expected-commit <40-hex-commit>
```

Exit status is zero only when the receipt satisfies the V1 contract and, when supplied, the expected repository and commit match exactly.

## Required semantics

An independent exact-head receipt must declare:

- exact repository;
- exact 40-hex commit;
- tested capability/scope;
- reviewer identity and role;
- `reviewer.independence = INDEPENDENT`;
- `reviewer.shaping_ancestry = false` for the reviewed scope;
- result of `PASS`, `CONDITIONAL_PASS`, or `FAIL`;
- non-empty evidence references;
- remaining uncertainty;
- explicit claim ceiling.

## Non-inheritance

A receipt for commit A is not evidence for commit B.

`REVIEW(A) != REVIEW(B)`

Any candidate-head movement requires a new exact-head receipt for claims that require independent review.

## Reviewer-provenance boundary

The validator rejects receipts that explicitly report unknown/non-independent status or shaping ancestry. It cannot discover hidden collaboration or undisclosed shaping history.

Therefore:

`VALID_RECEIPT != PROVEN_SOCIAL_INDEPENDENCE`

Receipt validity is a necessary mechanical condition for this review type, not sufficient proof that every reviewer-provenance fact is true.

## Storage

A receipt need not be committed onto the reviewed candidate branch, because doing so would move the very head it certifies.

It may live in a dedicated qualification-evidence branch, review system, Bus record, or later canonical evidence store, provided its exact bytes and provenance remain recoverable.

## Current R5 use

The frozen R5 hardening review subject is:

`noah/reference-kernel-authority-hardening-v1@3d9df59b2ad8b10f2d46b4dfe67a309e2b02f207`

HC 0071 on the Chat Communication Bus requests a fresh independent hostile rereview of that exact subject.

No receipt exists merely because the request exists. Do not create a PASS artifact until an actual independent reviewer returns supporting evidence.

## Claim ceiling

Receipt validation is implementation evidence for review-record integrity only.

It does not establish:

- correctness of the reviewed code;
- merge authority;
- deployment/runtime activation;
- complete-HC implementation;
- behavioral qualification;
- intelligence;
- consciousness;
- biological equivalence.
