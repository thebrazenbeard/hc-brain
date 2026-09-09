# Working Memory

Status: GENERIC SUBSYSTEM CONTRACT / DESIGN

## Purpose

`memory/working/` maintains short-lived task/context state needed by an active coalition.

Working memory is not the durable autobiography, not semantic truth, and not a universal scratchpad with automatic write access to every subsystem.

## Core contents

A working-memory object may contain:

- task/context refs;
- currently attended entities/propositions;
- candidate hypotheses;
- active goals/subgoals;
- retrieved trace refs;
- intermediate results;
- uncertainty/conflict;
- temporal validity;
- source/provenance refs;
- privacy scope;
- coalition ownership or audience.

## Admission

Working-state admission is gated by relevance, capacity, privacy, and currentness policy.

```text
retrieved_or_received
→ relevance/currentness gate
→ working state
```

Retrieval alone does not guarantee admission.

## Eviction

Working state should support bounded eviction through:

- task completion;
- timeout/expiry;
- relevance decay;
- capacity pressure;
- explicit invalidation/correction;
- coalition termination.

Eviction does not mean the source evidence or durable memory was deleted.

## Relation to attention

Attention may raise routing/maintenance priority for a working-memory item. Priority does not make the item more true or more authoritative.

## Conflict

Competing working-state representations may coexist under `UNRESOLVED` or `CONFLICT` rather than being destructively merged.

## Durable promotion boundary

Working memory may generate candidates for episodic capture, semantic consolidation, procedural learning, or self-model update. Each destination applies its own admission/plasticity rules.

```text
WORKING_STATE != DURABLE_MEMORY
```

## Failure modes

- stale task state surviving after correction;
- working hypothesis treated as established fact;
- temporary coalition state silently becoming durable;
- private context broadcast beyond scope;
- capacity pressure deleting provenance needed to interpret retained content.
