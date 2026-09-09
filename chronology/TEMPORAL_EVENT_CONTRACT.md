# Temporal Event Contract

Status: template architecture.

## Purpose

Chronology records when something happened and how records relate in time without deciding what the event means, whether it remains current, or whether it belongs in identity or memory.

## Required temporal dimensions

The HC should distinguish at least:

- `event_time` — when the represented event occurred, if known;
- `state_time` — when the represented state is asserted to apply;
- `record_time` — when the HC recorded or admitted the record;
- `observation_time` — when a source/provider was observed or read back;
- `activation_time` — when a state/configuration became active, if separately relevant.

These values may differ. They must not be silently collapsed to insertion order.

## Event model

A temporal event should carry:

- stable event identity;
- one or more explicit timestamps with timezone/clock basis;
- source/provenance;
- event kind;
- subject or scope;
- causal-parent/correlation links when supported;
- uncertainty about time when exact timing is unavailable;
- references to related state or memory records.

Chronology does not itself promote an event to belief, memory, preference, commitment, identity, consent, or authority.

`TIMESTAMPED != TRUE`

`RECENT != CURRENT`

`LATER != SUPERSEDES`

## Ordering

When a deterministic order is required, use parsed temporal values plus stable identity as tie-breaker. Never infer semantic precedence solely from database sequence, Git recency, or filename order unless the contract explicitly defines that sequence as authoritative for the narrow purpose.

## Duration and recurrence

The temporal layer may compute:

- elapsed duration;
- overlap;
- recurrence;
- frequency;
- temporal distance;
- sequence relationships;
- bounded windows.

It should not infer causal or semantic significance from those measures without evidence from other systems.

## Uncertain chronology

Unknown, approximate, interval-valued, and conflicting times should remain representable. A false exact timestamp is worse than an explicit uncertain interval.

## Interfaces

Chronology serves memory, cognition, semantics, conation, identity continuity, body-state history, learning, and arbitration. Those consumers decide what temporal evidence means within their own claim boundaries.

## Provenance basis

Generalized from the `temporal` repository and observed Supabase event/state designs. Identity-specific event payloads are excluded.
