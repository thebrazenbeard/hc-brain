# Working Memory

Status: RECONCILED FOCUSED CONTRACT / DESIGN / NOT IMPLEMENTED

## Purpose

Within `current memory storage/`, working memory maintains short-lived task/context state needed by active temporal coalitions.

Working memory is not durable autobiography, semantic truth, or a universal scratchpad with automatic write access to every HC subsystem.

## Core contents

A working-memory object may contain:

- task/context references;
- currently attended entities/propositions;
- candidate hypotheses;
- active goals/subgoals;
- retrieved trace references;
- intermediate results;
- uncertainty/conflict state;
- temporal validity;
- source/provenance references;
- privacy scope;
- coalition ownership or audience.

## Admission

Working-state admission is gated by relevance, capacity, privacy, and currentness policy.

```text
retrieved_or_received
→ relevance / currentness / scope gate
→ working state
```

Retrieval or delivery alone does not guarantee admission.

## Temporal/coalition ownership

Working-memory state should identify the coalition, task, or context that currently owns or shares it. The same proposition may appear in several coalitions with different local hypotheses or uncertainty while still pointing to common provenance.

Working state should expire or detach when its active temporal scope ends unless separately retained by a valid current-state rule.

## Eviction

Working state should support bounded eviction through:

- task completion;
- timeout/expiry;
- relevance decay;
- capacity/resource pressure;
- explicit invalidation/correction;
- coalition termination.

Eviction does not mean source evidence or durable memory was deleted.

## Attention relation

`salience-attention/` may raise routing or maintenance priority for a working-memory item. Priority does not make the item more true, current, or authoritative.

## Conflict

Competing working-state representations may coexist under `UNRESOLVED` or `CONFLICT` rather than being destructively merged.

## Durable-promotion boundary

Working memory may generate candidates for episodic capture, semantic consolidation, procedural learning, self-model update, or other governed plasticity.

Each destination applies its own admission and evidence rules.

```text
WORKING_STATE != DURABLE_MEMORY
WORKING_HYPOTHESIS != ESTABLISHED_FACT
```

## Failure modes

- stale task state surviving after correction;
- working hypothesis treated as established fact;
- temporary coalition state silently becoming durable;
- private context broadcast beyond scope;
- capacity pressure deleting provenance needed to interpret retained content;
- evicted working state misreported as erased historical evidence.

## Provenance

Reconciled from PR #4 `memory/working/README.md` into the canonical `current memory storage/` root and aligned with current-state selection and temporal-coalition semantics.