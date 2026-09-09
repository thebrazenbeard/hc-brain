# Semantics subsystem

## Purpose

The Semantics subsystem represents concepts, definitions, propositions, relations, interpretations, evidence links, lifecycle, and current adjudicated meaning without collapsing those dimensions into one status field.

## Source-derived design rules

The directly relevant `thebrazenbeard/semanticatlas` repository supplies a mature reusable semantic architecture:

- Stable concept identity should be separated from mutable definitions.
- Exact evidence, derivative evidence projections, interpretations, propositions, and adjudications are distinct object classes.
- A relation vocabulary defines predicate semantics but does not itself assert truth.
- Truth-bearing assertions belong in propositions rather than bare graph edges.
- Authorship, endorsement, truth, currentness, canon authority, consent, salience, and identity relevance are independent dimensions.
- Historical lifecycle should remain append-oriented: refinement, supersession, retraction, reopening, correction, and reinstatement preserve prior state rather than erase it.
- Generated views and indexes are derived projections, not authority surfaces.
- Semantic continuity must be justified; material discontinuity requires a new concept identity plus explicit lineage.
- Unknown and not-applicable states should remain explicit rather than coerced into false certainty.

## Core object model

The HC semantic layer should support equivalents of:

- `source_instance`
- `evidence_span`
- `evidence_projection`
- `concept_node`
- `concept_definition`
- `relation_type`
- `proposition`
- `interpretation`
- `adjudication`
- `lifecycle_event`

## Architectural invariants

`CONCEPT_ID != CURRENT_DEFINITION`

`INTERPRETATION != EVIDENCE`

`GRAPH_EDGE != CANONICAL_FACT`

`DERIVED_VIEW != AUTHORITY`

## Cross-system interfaces

Semantics should interoperate tightly with `pragmatics`, `phoenetics`, `speech recognition & synthesis`, `cognition`, `current memory storage`, `deep memory storage`, `chronology`, `self identity`, `resolver`, and `integration-arbitration`.

## Provenance

Generalized from `thebrazenbeard/semanticatlas`; identity-specific semantic decisions are intentionally excluded.