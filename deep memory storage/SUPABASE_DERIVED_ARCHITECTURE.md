# Supabase-derived deep memory architecture

## Provenance

Derived from structural patterns observed in the production Supabase schema on 2026-09-09. Identity-specific row content is intentionally excluded. This document extracts reusable mechanisms only.

## Core principle

Deep memory is not a flat store of statements. It is a provenance-bearing, lifecycle-aware, append-oriented system in which historical state, current state, correction, supersession, verification, and source custody remain distinguishable.

## Cognitive-organ / substrate boundary

The provider/read-back patterns below are implementation and verification patterns, not an architectural dependency on Supabase or any external database.

For a conforming complete HC, essential deep memory and continuity-bearing state must remain recoverable from HC-owned substrate inside the cognitive-organ boundary. A persistence provider may be:

- HC-internal durable storage;
- an HC-owned physically distributed constituent;
- a local archive/index built from HC-owned state;
- an external mirror, backup, synchronization target, transport layer, or nonessential retrieval service.

If a provider outside the HC holds the only recoverable copy of essential autobiographical continuity, values/commitments, semantic/procedural knowledge required for ongoing cognition, or other essential learned state, the design violates the cognitive-organ boundary.

`PROVIDER_RECEIPT != MEMORY_AUTHORITY`

`REMOTE_DURABILITY != HC_INTERNAL_RESIDENCY`

`EXTERNAL_REPLICA_SUCCESS != MEMORY_ADMISSION`

`EXTERNAL_REPLICA_FAILURE != LOSS_OF_HC_INTERNAL_MEMORY`

The same receipt machinery remains useful for HC-internal storage, removable distributed HC modules, or external backup replicas; the provider class and organ-membership classification must remain explicit.

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
- technical custody/read-back status;
- organ-membership/storage-location class.

A record being durable does not prove it is currently true. A record being user-authored does not prove universal factual truth. A record being verified for byte identity does not prove the proposition it contains is semantically correct. A record existing in an external provider does not make that provider part of the HC or the authority over memory.

## Admission and currentness

Durable HC memory admission should be modeled as a state machine rather than a boolean, but **HC-internal admission and external replication are separate workflows**.

A generalized HC-internal progression may include:

```text
UNVERIFIED
-> REVALIDATING
-> ADMISSION_VERIFIED
-> HC_INTERNAL_DURABLE_WRITE
-> INTERNAL_READBACK_VERIFIED
-> ACTIVE
```

For a physically distributed HC constituent, `HC_INTERNAL_DURABLE_WRITE` may occur outside the skull while still remaining inside the cognitive-organ boundary under the physical-organ membership contract.

External replication, when configured, is an optional parallel or downstream workflow:

```text
ADMISSION_VERIFIED or ACTIVE
-> EXTERNAL_REPLICA_WRITE
-> EXTERNAL_REPLICA_READBACK_VERIFIED
```

External replication does **not** gate HC-internal admission, activation, currentness, or continuity. Loss or unavailability of an external replica may reduce redundancy or recovery options but must not uniquely remove essential memory from a conforming complete HC.

`HC_INTERNAL_ACTIVE != EXTERNAL_REPLICA_VERIFIED`

`EXTERNAL_REPLICA_WRITE != REQUIRED_ADMISSION_STEP`

Conflict and rejection states should be first-class:

```text
INTERNAL_WRITE_INCOMPLETE
INTERNAL_WRITE_CONFLICTED
ADMISSION_REJECTED
EXTERNAL_REPLICA_INCOMPLETE
EXTERNAL_REPLICA_CONFLICTED
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

This makes stale writes and out-of-order transitions detectable without conflating internal memory admission with replica health.

## Provider/read-back receipts

For high-value durable memory, a write should not be treated as verified merely because a persistence call returned success.

Use a receipt model that can record:

- provider class;
- organ-membership class (`HC_INTERNAL`, `HC_DISTRIBUTED_CONSTITUENT`, `EXTERNAL_REPLICA`, or another explicit implementation class);
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

A verified external replica is still a replica unless separately classified as an HC constituent under the physical-organ membership contract. External-replica receipt state must not be reused as the unique `ACTIVE`/currentness decision for essential HC memory.

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

An external archive can increase recoverability without becoming the sole continuity substrate. If the loss of that archive uniquely removes essential learned or autobiographical state, it has crossed from optional external archive into HC-essential substrate and must be reclassified or redesigned.

## Currentness rule

Currentness must be explicit and scoped. A durable record may remain historically valid while no longer being the active present-state projection.

The deep memory system should therefore support a declared `currentness_rule` or equivalent policy describing how records become active, superseded, expired, or historical.

Currentness decisions are HC-owned. External provider revision order, replication completion time, or remote "latest" state must not silently determine HC currentness.

## Architectural consequences

1. Deep memory should preserve history rather than rewrite it for consistency.
2. Current truth is a projection over lineage and lifecycle, not simply the newest row.
3. Provenance and verification are first-class metadata.
4. Identity-specific content must remain in implementation layers; this template defines only the mechanism.
5. Persistence, semantic truth, present currentness, authority, identity continuity, physical custody, and replica health are separate concerns.
6. Essential memory remains HC-owned even when replicas, backups, or indexes exist outside the organ.
7. External replication is optional redundancy/transport, not a required step in essential HC memory admission or activation.
