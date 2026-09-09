# Semantic Memory

Status: GENERIC SUBSYSTEM CONTRACT / DESIGN

## Purpose

`memory/semantic/` stores durable generalized knowledge: concepts, relations, regularities, learned propositions, conventions, and world-model structure that are not tied solely to one episode.

Semantic memory is separate from the semantics subsystem: `semantics/` represents meaning during cognition; semantic memory is a durable knowledge substrate those processes may read/write through governed consolidation.

## Candidate content

- concepts/categories;
- propositions and relations;
- learned invariants/regularities;
- schemas/frames;
- shared conventions;
- causal models with evidence scope;
- vocabulary/grounded mappings;
- confidence/support;
- provenance lineage;
- contradiction/supersession state.

## Consolidation

Generalized knowledge should usually arise through slower integration than episodic capture.

```text
multiple episodes/observations
+ existing semantic structure
+ reconciliation/generalization
→ semantic candidate
→ evidence/conflict/plasticity gate
→ provisional or durable semantic update
```

One striking episode may justify a semantic update when evidence supports it, but novelty alone is not a generalization rule.

## Provenance

Generalized knowledge should retain enough lineage to answer:

- what observations/episodes/sources contributed;
- whether the claim was imported or learned;
- what contradictions exist;
- what confidence/currentness applies;
- what later state superseded it.

## Currentness

Some semantic facts are stable; others are time-sensitive. A durable semantic record may therefore require freshness checks before being used as present-world truth.

## Conflict

Conflicting semantic structures may coexist with scoped applicability rather than being flattened prematurely.

## Failure modes

- imported claim misclassified as learned experience;
- old fact treated as current without freshness check;
- repeated retrieval strengthening a claim without external evidence;
- one source duplicated many times and mistaken for independent corroboration;
- semantic memory used as effect authority;
- provenance discarded during generalization.
