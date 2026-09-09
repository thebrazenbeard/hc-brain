# Chronology subsystem

## Purpose

The Chronology subsystem records when events occurred, preserves ordering, and computes temporal relations without deciding what those events mean.

## Source-derived design rules

The `thebrazenbeard/temporal` repository supplies a clean separation that is appropriate for the HC template:

- Chronology is not memory, identity, preference, consent, authority, or truth adjudication.
- Event records should be timestamped with timezone-aware canonical time.
- Original local/offset timestamps may be preserved separately when relevant.
- Stable event IDs prevent ambiguous temporal reference.
- Duplicate IDs and malformed records should fail loudly.
- Canonical ordering should be based on timestamp plus stable ID, not inferred conversational sequence.
- Temporal arithmetic should operate on parsed timestamps, not narrative assumptions.
- History should be append-oriented.

## Event representation

A minimal event record should include:

- stable event ID;
- canonical UTC timestamp;
- optional original local timestamp;
- source/provenance;
- event descriptor;
- optional references;
- bounded metadata.

## Responsibilities

1. **Temporal indexing** — place events on a stable timeline.
2. **Ordering** — provide deterministic sequence when events share close or identical times.
3. **Duration calculation** — compute elapsed time between known timestamps or events.
4. **Temporal windows** — support bounded retrieval by start/end time.
5. **Provenance preservation** — keep event source separate from semantic interpretation.

## Non-responsibilities

Chronology does not decide whether an event is important, true, identity-defining, remembered, believed, desired, or current.

## Cross-system interfaces

Chronology should serve `current memory storage`, `deep memory storage`, `self identity`, `psychological behaviors`, `sociological behaviors`, `volitions-conations`, and `integration-arbitration` as a temporal substrate.

## Provenance

Generalized from `thebrazenbeard/temporal`; identity-specific naming is excluded from the template.