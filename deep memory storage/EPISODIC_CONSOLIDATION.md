# Episodic Consolidation

Status: RECONCILED FOCUSED CONTRACT / DESIGN / NOT IMPLEMENTED

## Purpose

Within `deep memory storage/`, episodic consolidation governs promotion of eligible event-specific traces into durable memory while preserving event identity, provenance, uncertainty, correction lineage, and privacy scope.

Durability is a lifecycle property. It does not make an episode current, objectively true, identity-defining, or authoritative.

## Candidate path

```text
current episodic trace
+ replay / relevance / retention signal
+ provenance / privacy / conflict checks
→ consolidation candidate
→ provisional durable trace
→ evaluate / reconcile
→ consolidate | revise | quarantine | reject
```

Not every captured episode requires durable retention.

## Fidelity requirement

Durable consolidation should preserve, when available:

- stable episode/event ID;
- observed time/interval;
- recorded/capture time;
- source/evidence references;
- representation at capture time;
- uncertainty/confidence;
- privacy scope;
- correction/reinterpretation links;
- integrity digest where used;
- later supersession or contradiction state.

Later interpretation must not silently overwrite the historical trace.

## Replay

Replay may reactivate a durable episode into current cognition for:

- retrieval;
- prediction/planning;
- semantic generalization;
- procedural learning;
- self/social-model revision;
- conflict resolution.

```text
REPLAYED != CURRENT
REPLAYED != TRUE
REPLAYED != AUTHORIZED
```

The consuming coalition applies present currentness, relevance, privacy, and evidence rules.

## Pattern separation

Durable storage should retain enough episode identity to prevent semantically similar events from collapsing into one occurrence when their distinction matters.

## Forgetting and decay

A conforming implementation may support decay, compression, archival tiering, or selective forgetting while preserving required governance/provenance constraints. Loss of easy retrieval must remain distinguishable from proof that an event never occurred.

## Failure modes

- later knowledge retroactively alters original event state;
- reconstructed details are labeled original observation;
- replay is treated as current evidence without qualification;
- one salient episode is generalized into a broad rule without evidence;
- durable storage is treated as permanent relevance;
- privacy scope is lost during consolidation;
- separate events are collapsed because their semantic content overlaps.

## Provenance

Reconciled from PR #4 `memory/episodic/README.md` into the canonical `deep memory storage/` role, complementary to `current memory storage/EPISODIC_CAPTURE.md`.