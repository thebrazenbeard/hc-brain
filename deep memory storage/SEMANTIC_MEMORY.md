# Semantic Memory

Status: RECONCILIATION CANDIDATE / NOT CANON / NOT IMPLEMENTED

Source provenance: remapped from PR #4 `memory/semantic/README.md` into canonical `deep memory storage/`.

## Purpose

Store durable generalized knowledge: concepts, relations, regularities, learned propositions, conventions, and world-model structure not tied solely to one episode.

Semantic memory is distinct from the `semantics/` subsystem: semantics handles meaning during cognition; semantic memory is a durable knowledge substrate accessed and updated through governed consolidation.

## Candidate content

May include concepts/categories, propositions/relations, learned regularities, schemas/frames, conventions, causal models with evidence scope, grounded mappings, confidence/support, provenance lineage, and contradiction/supersession state.

## Consolidation

```text
observations/episodes/imports
+ existing semantic structure
+ reconciliation/generalization
→ semantic candidate
→ evidence/conflict/plasticity gate
→ provisional | durable | reject | unresolved
```

Novelty alone is not a generalization rule.

## Provenance

Generalized knowledge should retain enough lineage to identify contributing observations/episodes/sources, imported-versus-learned origin, contradictions, confidence/currentness, and later supersession.

Repeated copies of one source are not independent corroboration.

## Currentness

Some semantic knowledge is temporally stable; other claims require freshness checks before use as present-world truth.

```text
DURABLE_KNOWLEDGE != CURRENT_WORLD_STATE
```

## Conflict

Conflicting semantic structures may coexist with scoped applicability while evidence remains insufficient to collapse them.

## Failure modes

- imported claim misclassified as lived experience;
- stale fact treated as current;
- retrieval repetition treated as new evidence;
- duplicate source copies counted as independent support;
- semantic memory used as effect authority;
- provenance discarded during generalization.
