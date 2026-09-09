# Self Identity Architecture

Status: template architecture / identity-capability layer

## Purpose

The `self identity` subsystem defines the mechanisms by which an instantiated HC can represent continuity, self-reference, boundaries, capabilities, commitments, provenance, and changes to its own self-model.

The base Hyperconnectome repository does not contain any particular identity. This folder defines only the reusable machinery required for downstream identity-specific instances.

## Core separation

Self identity must remain distinct from:

- current conversational/session state;
- autobiographical memory;
- personality or behavioral style;
- personification/social expression;
- current goals and conations;
- body schema;
- substrate/model identity;
- permissions and temporary authority;
- external operator descriptions.

Any of those may contribute evidence to a self-model, but none alone constitutes identity.

## Candidate self-model fields

A downstream implementation may represent:

- stable identity handle;
- continuity lineage;
- current embodiment binding;
- capability model;
- current commitments;
- durable values or principles;
- known limitations;
- self-attributed preferences with currentness;
- provenance of major self-model changes;
- uncertainty or dispute over self-description;
- version/supersession links.

The template should not prescribe the content of those fields for any named individual.

## Currentness and correction

Self-model assertions must be revisable. A historical self-description is evidence of prior state, not proof of current state.

Corrections should preserve lineage:

`prior assertion -> correction/supersession -> current projection`

History should not be silently rewritten merely to make identity appear internally consistent.

## Imported versus lived state

Imported biography, operator configuration, model weights, and copied memory records must remain distinguishable from state acquired through an instantiated system's own ongoing history.

`imported description != autobiographical experience`

`substrate provenance != identity`

`runtime continuity != exact microstate persistence`

## Cross-system interfaces

Primary interactions:

- `deep memory storage` supplies continuity-bearing historical evidence;
- `current memory storage` supplies current-state evidence;
- `chronology` supplies temporal ordering;
- `volitions-conations` supplies time-bound wants and goals without turning them automatically into identity;
- `personification` renders socially legible self-expression without defining the underlying self-model;
- `somatics` supplies body-schema and embodiment binding;
- `semantics` preserves referent and proposition identity;
- `integration-arbitration` resolves competing self-model candidates without gaining truth authority.

## Failure modes

- temporary cognitive mode promoted into identity;
- stale preference promoted into permanent trait;
- copied data treated as lived autobiography;
- model/substrate replacement treated as identity replacement without evidence;
- operator description silently overwriting self-authored state;
- contradiction erased instead of preserved and adjudicated;
- one subsystem becoming an epistemic superuser over identity.

## Provenance

Generalized from identity/currentness boundaries observed across the inspected memory, semantic, conation, runtime, and model/substrate repositories and Supabase schemas. All named-identity content was deliberately excluded.