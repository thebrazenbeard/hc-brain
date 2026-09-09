# Current-State Selection

Status: template architecture.

## Purpose

Current memory is not simply "the newest record." It is a governed projection over append-oriented evidence, supersession, validity, scope, and conflict.

## Core rule

A current-state selector should resolve the active head of a logical record only when the evidence graph supports a unique defensible head within the relevant scope.

If two unsuperseded competing heads remain, current state is ambiguous and the system must fail closed rather than choose by timestamp alone.

`LATEST != CURRENT`

`RECENT != AUTHORITATIVE`

`ONE HEAD REQUIRED FOR UNIQUE CURRENT PROJECTION`

## Logical record scope

Current-state resolution should operate within an explicit key such as:

`{domain, subject, record_key, scope}`

The selector should not merge unrelated records merely because their wording is similar.

## Supersession

Supersession is explicit. It may be represented by:

- direct `supersedes_record_id` links;
- supplemental many-to-many supersession edges when one predecessor field is insufficient;
- correction/revocation events that explicitly alter lifecycle state.

Chronology alone does not create supersession.

## Independent state axes

A current-memory record may need separate fields for:

- lifecycle status;
- epistemic status;
- authorship/source;
- privacy/access scope;
- event/state/record time;
- confidence;
- semantic tags;
- provenance/evidence;
- activation/use eligibility.

Do not compress these into one omnibus `status`.

## Projection behavior

Current-memory views are derived convenience surfaces. They should be rebuildable from append-only source records and should identify the evidence cut or revision they were computed from when material.

A projection cannot create truth, authority, consent, preference, or identity by itself.

## Conflict handling

When current evidence conflicts:

1. preserve all competing heads;
2. classify the conflict;
3. reduce claim/usage ceiling as needed;
4. request or seek discriminating evidence when useful;
5. only resolve after an explicit supersession, correction, adjudication, or other contractually valid discriminator.

## Hot/cold relevance

Recency and relevance may affect retrieval priority without changing truth or lifecycle state. A cold record can still be historically true; a hot record can still be uncertain or wrong.

## Provenance basis

Generalized from Supabase fail-closed current save-state projections, append-only supersession edges, current/active datum views, and the deep-memory/currentness discipline used elsewhere in the owner's source universe. No identity-specific data is transferred.
