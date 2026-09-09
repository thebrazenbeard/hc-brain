# Supabase-derived current memory architecture

## Provenance

Derived from structural patterns observed in the production Supabase schema on 2026-09-09. Identity-specific content is excluded.

## Core principle

Current memory is a fast, revisable state surface. It is not the durable historical ledger and it is not automatically authoritative simply because it is active.

## Recommended record classes

Current memory should be able to represent several distinct kinds of active context, for example:

- facts/data;
- user statements;
- model outputs;
- preferences;
- decisions;
- corrections;
- behavioral commitments;
- boundaries;
- permissions;
- task state;
- technical results;
- provenance;
- hypotheses;
- interpretations;
- evaluations;
- tombstones/retirements.

These classes should remain explicit rather than being flattened into one generic memory blob.

## State axes

Each current-memory record should independently track:

- lifecycle status;
- epistemic status;
- source actor;
- privacy scope;
- event time;
- state time;
- record time;
- source evidence;
- limitations;
- semantic tags;
- optional predecessor/supersession link.

## Verification versus currentness

Verification outcome and currentness are separate axes.

A datum may be:

- verified but historical;
- current but not yet verified;
- superseded but still historically important;
- rejected as a present claim while retained as provenance.

Do not overload one status field to carry all of these meanings.

## Promotion boundary

Promotion from current memory into deep memory should require an explicit operation that preserves provenance and lifecycle context.

Suggested flow:

```text
current observation
-> bounded interpretation
-> verification / corroboration as needed
-> admission decision
-> durable deep-memory record
```

Promotion must not imply that an imported or externally sourced event was personally experienced by the instantiated system.

## Retrieval relevance

Retrieval metadata such as tags and last-reference timestamps can improve access, but retrieval salience must not become epistemic authority. Frequently retrieved records are not therefore more true.

## Failure modes

- stale current state mistaken for present truth;
- unverified model output treated as fact;
- source actor lost during summarization;
- permissions or boundaries silently treated as permanent;
- old preference reactivated merely because it was retrieved;
- current context promoted into durable identity state without admission;
- private context exported beyond its declared scope.
