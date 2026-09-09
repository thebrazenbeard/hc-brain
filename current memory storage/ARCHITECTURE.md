# Current Memory Storage Architecture

Status: intrinsic HC system / template architecture.

## Purpose

Current memory storage is the HC-owned fast, revisable state surface for working context, active task state, recent observations, current hypotheses, current preferences/constraints, and other short-horizon state that must remain distinguishable from durable historical memory.

It is part of the Hyperconnectome Brain cognitive organ. A database, cache, vector store, model context window, or other storage technology may implement or assist this subsystem only if it remains subordinate to the HC-owned memory contract. No external provider becomes the authoritative owner of cognition, identity, or currentness merely because it stores bytes.

## Core distinctions

`CURRENT_MEMORY != DEEP_MEMORY`

`LATEST != CURRENT`

`RETRIEVED != TRUE`

`STORED != ACTIVE`

`ACTIVE != AUTHORITATIVE`

`PROVIDER_READBACK != SEMANTIC_TRUTH`

## State model

Current-memory items should preserve the distinctions needed by the rest of the HC, including lifecycle/currentness, epistemic status, origin/authorship, privacy scope, event/state/record time, provenance, limitations, confidence where appropriate, and supersession/contradiction lineage.

Current state may contain competing heads or unresolved alternatives. The system must fail closed when a unique current projection is not justified.

## Admission and eviction

Current memory receives candidates from perception, cognition, semantics/pragmatics, action/outcome loops, conation, affect, chronology, and memory retrieval. Admission should be explicit enough to preserve provenance and scope.

Eviction from the active surface does not erase history. Material that warrants durable retention becomes a deep-memory candidate through a separate consolidation/admission path.

## Technology boundary

The architecture is implementation-neutral. A conforming implementation may use local databases, durable logs, caches, in-memory state, specialized memory hardware, or other storage mechanisms. If a provider is physically external to the HC boundary, it is a storage peripheral and cannot be the sole seat of essential memory, identity continuity, or current-state authority.

## Related contracts

- `CURRENT_STATE_SELECTION.md`
- `SUPABASE_DERIVED_ARCHITECTURE.md`
- `../deep memory storage/ARCHIVAL_CONSOLIDATION.md`
- `../chronology/TEMPORAL_EVENT_CONTRACT.md`
- `../docs/architecture/CROSS_SYSTEM_INTEGRATION_CONTRACT.md`
