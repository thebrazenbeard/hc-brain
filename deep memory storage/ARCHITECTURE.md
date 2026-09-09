# Deep Memory Storage Architecture

Status: intrinsic HC system / template architecture.

## Purpose

Deep memory storage is the HC-owned durable memory subsystem for episodic, semantic, procedural, autobiographical, learned, and other long-horizon memory classes whose persistence outlives the current active context.

It belongs inside the Hyperconnectome Brain cognitive-organ boundary. External storage providers, databases, archives, vector systems, or retrieval services may be implementation substrates or bounded peripherals, but they do not become the seat of identity, authority, or cognition merely because they persist data.

## Core distinctions

`DURABLE != CURRENT`

`STORED != TRUE`

`RETRIEVED != ADMITTED_AS_TRUE`

`WRITE_REQUESTED != DURABLY_STORED`

`READBACK_VERIFIED != SEMANTICALLY_CORRECT`

`ARCHIVED != ACTIVE_MEMORY`

## Memory classes and lineage

Deep memory should preserve distinct memory classes and their provenance. Corrections, contradiction, reinterpretation, supersession, consolidation, and forgetting/inhibition should add lineage or state transitions rather than silently rewrite historical source records.

A durable memory may remain historically valid while no longer contributing to current-state projection.

## Admission and consolidation

Deep-memory admission is a governed transition from candidate material into durable HC memory. It should preserve source evidence, currentness context, privacy/scope, epistemic status, temporal metadata, and consolidation rationale.

Consolidation may abstract, generalize, compress, or connect memories while retaining enough provenance to distinguish source experience from derived interpretation or semantic learning.

## Retrieval

Retrieval is a candidate-generation operation. Retrieved content returns to current cognitive processing with provenance and confidence intact; retrieval frequency or salience does not make the content more true, current, important, or identity-defining.

## Technology boundary

A conforming implementation may use local databases, append-only logs, object stores, content-addressed archives, associative memory hardware, vector indexes, or other mechanisms. Essential durable memory and identity continuity must remain HC-owned. If an external provider is used, the HC must retain sufficient internal state, lineage, verification, and recovery semantics so provider state is not promoted into cognitive authority.

## Related contracts

- `ARCHIVAL_CONSOLIDATION.md`
- `SUPABASE_DERIVED_ARCHITECTURE.md`
- `../current memory storage/CURRENT_STATE_SELECTION.md`
- `../chronology/TEMPORAL_EVENT_CONTRACT.md`
- `../self identity/CONTINUITY_SUBSTRATE.md`
