# Working Memory

Status: RECONCILIATION CANDIDATE / NOT CANON / NOT IMPLEMENTED

Source provenance: remapped from PR #4 `memory/working/README.md` into canonical `current memory storage/`.

## Purpose

Maintain short-lived task/context state used by active coalitions.

Working memory is not durable autobiography, semantic truth, or a universal scratchpad with automatic access to every subsystem.

## Working object

May include task/context refs, attended entities/propositions, candidate hypotheses, active goals/subgoals, retrieved trace refs, intermediate results, uncertainty/conflict, temporal validity, source/provenance refs, privacy scope, and coalition ownership/audience.

## Admission

```text
retrieved_or_received
→ relevance/currentness/privacy/capacity gate
→ working state | defer | reject | unresolved
```

Retrieval alone does not guarantee admission.

## Eviction

Working state may be evicted by task completion, timeout/expiry, relevance decay, capacity pressure, explicit invalidation/correction, or coalition termination.

Eviction does not delete source evidence or durable memory.

## Attention relation

Attention may raise processing/retention priority. Priority does not make content more true, current, or authoritative.

## Conflict

Competing working representations may coexist under `UNRESOLVED` or `CONFLICT` instead of being destructively merged.

## Durable-promotion boundary

Working state may generate candidates for episodic capture, semantic consolidation, procedural learning, self-model update, or plasticity. Each destination applies its own admission rules.

```text
WORKING_STATE != DURABLE_MEMORY
```

## Failure modes

- stale task state survives correction;
- working hypothesis becomes fact by repetition;
- temporary coalition state silently becomes durable;
- private context broadcasts outside scope;
- eviction destroys provenance required to interpret retained content.
