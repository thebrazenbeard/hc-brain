# Semantic Memory

Status: RECONCILED FOCUSED CONTRACT / DESIGN / NOT IMPLEMENTED

## Purpose

Within `deep memory storage/`, semantic memory stores durable generalized knowledge: concepts, relations, regularities, learned propositions, conventions, and world-model structure that are not tied solely to one episode.

Semantic memory is distinct from the `semantics/` subsystem. `semantics/` participates in meaning construction and interpretation during cognition; semantic memory is a durable knowledge substrate that semantic and other HC systems may query or update through governed consolidation.

## Candidate content

Semantic memory may contain:

- concepts/categories;
- propositions and relations;
- learned invariants/regularities;
- schemas/frames;
- shared conventions;
- causal models with evidence scope;
- vocabulary/grounded mappings;
- confidence/support;
- provenance lineage;
- contradiction/supersession state;
- temporal validity/currentness requirements.

## Consolidation

Generalized knowledge should usually arise through integration rather than direct copying of transient state.

```text
multiple episodes / observations / qualified sources
+ existing semantic structure
+ reconciliation / generalization
→ semantic candidate
→ evidence / conflict / plasticity gate
→ provisional or durable semantic update
```

One observation may justify a semantic update when the proposition itself is adequately supported; novelty alone is not a generalization rule.

## Provenance

Generalized knowledge should retain enough lineage to answer:

- which observations, episodes, or sources contributed;
- whether the claim was imported, instructed, inferred, or learned from consequence;
- which contradictions remain;
- what confidence/evidence ceiling applies;
- what currentness rule applies;
- what later state superseded it.

Repeated retrieval of one source must not masquerade as independent corroboration.

## Currentness

Some semantic knowledge is stable; other claims are time-sensitive.

```text
DURABLE_SEMANTIC_RECORD != CURRENT_WORLD_FACT
```

A durable record may require freshness/currentness evaluation before it is used as present-world truth.

## Conflict and scope

Conflicting semantic structures may coexist with scoped applicability rather than being flattened prematurely. Contradiction, alternative models, and unresolved applicability should remain representable.

## Failure modes

- imported claim misclassified as learned experience;
- old fact treated as current without freshness check;
- repeated retrieval strengthens confidence without new evidence;
- one source duplicated many times and mistaken for independent corroboration;
- semantic memory is used as effect authority;
- provenance is discarded during generalization;
- semantic memory is conflated with the live `semantics/` processing subsystem.

## Provenance

Reconciled from PR #4 `memory/semantic/README.md` into the canonical `deep memory storage/` root.