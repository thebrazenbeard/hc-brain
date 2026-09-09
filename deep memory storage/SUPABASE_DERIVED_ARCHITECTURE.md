# Supabase-derived deep memory architecture

## Provenance

Derived from structural patterns observed in the production Supabase schema on 2026-09-09. Identity-specific row content is intentionally excluded. This document extracts reusable mechanisms only.

## Core principle

Deep memory is not a flat store of statements. It is a provenance-bearing, lifecycle-aware, append-oriented system in which historical state, current state, correction, supersession, verification, and source custody remain distinguishable.

## Record model

A durable memory record should carry, at minimum:

- stable record identifier;
- logical memory identifier;
- record kind / memory class;
- statement or payload;
- lifecycle status;
- epistemic status;
- source actor / authorship;
- privacy scope;
- event time;
- state time;
- record time;
- source evidence;
- semantic tags;
- limitations;
- optional predecessor / superseded record reference.

The distinction among the three clocks is important:

- **event time** — when the represented event occurred;
- **state time** — when the represented state is asserted to apply;
- **record time** — when the memory record itself was persisted.

These must not be silently collapsed into one timestamp.

## Append-oriented correction and supersession

Correction should normally create a successor record rather than destructively rewriting the old one.

Preferred pattern:

```text
record A
  -> record B supersedes A
  -> record C refines or contradicts B
```

When a single predecessor pointer is insufficient, a supplemental edge relation may represent branch reconciliation or many-to-one supersession without mutating historical source records.

A supersession edge is evidence of lineage, not semantic authority by itself.

## Independent state axes

The architecture should keep these axes separate:

- lifecycle/currentness;
- epistemic support;
- authorship/source actor;
- privacy scope;
- verification process/outcome;
- semantic classification;
- technical custody/read-back status.

A record being durable does not prove it is currently true. A record being user-authored does not prove universal factual truth. A record being verified for byte identity does not prove the proposition it contains is semantically correct.

## Admission and currentness

Durable admission should be modeled as a state machine rather than a boolean.

A generalized progression may include states such as:

```text
UNVERIFIED
-> REVALIDATING
-> ADMISSION_VERIFIED
-> REPLICA_OR_PROVIDER_WRITE
-> READBACK_VERIFIED
-> ACTIVE
```

Conflict and rejection states should be first-class:

```text
MIGRATION_INCOMPLETE
MIGRATION_CONFLICTED
ADMISSION_REJECTED
```

State transitions should carry:

- prior state;
- new state;
- state version;
- expected prior version;
- attempt ID;
- operation ID;
- event kind;
- observed timestamp;
- event payload.

This makes stale writes and out-of-order transitions detectable.

## Provider/read-back receipts

For high-value durable memory, a write should not be treated as verified merely because a persistence call returned success.

Use a receipt model that can record:

- provider class;
- provider identity and locator;
- provider revision/version;
- operation ID;
- written byte length;
- content digest;
- read-back time;
- read-back byte length;
- read-back digest;
- verifier route;
- verification result;
- limitations.

Useful result classes include:

```text
VERIFIED_EXACT
ABSENT
AMBIGUOUS
MISMATCH
ERROR
```

## Archive receipts

Where a memory has both an active representation and a lossless archive representation, keep those verification chains distinct.

An archive receipt may bind:

- original source locator;
- original digest and byte length;
- archive bundle/container identity;
- archive member path;
- archive member digest;
- extracted read-back digest;
- provider receipts;
- admission receipt;
- verification result.

## Currentness rule

Currentness must be explicit and scoped. A durable record may remain historically valid while no longer being the active present-state projection.

The deep memory system should therefore support a declared `currentness_rule` or equivalent policy describing how records become active, superseded, expired, or historical.

## Architectural consequences

1. Deep memory should preserve history rather than rewrite it for consistency.
2. Current truth is a projection over lineage and lifecycle, not simply the newest row.
3. Provenance and verification are first-class metadata.
4. Identity-specific content must remain in implementation layers; this template defines only the mechanism.
5. Persistence, semantic truth, present currentness, authority, and identity continuity are separate concerns.
