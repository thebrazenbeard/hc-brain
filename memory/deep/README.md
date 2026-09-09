# Deep / Durable Memory

Status: GENERIC SUBSYSTEM CONTRACT / DESIGN

## Purpose

`memory/deep/` defines durable archival persistence and retrieval boundaries for long-lived state that must survive ordinary runtime/coalition turnover.

It is a storage/lifecycle role, not a claim that all durable content is current, true, identity-defining, or authorized.

## Core rule

```text
DURABLE != CURRENT != AUTHORITATIVE != TRUE
```

## Durable classes

A deep-memory implementation may persist:

- episodic history;
- semantic knowledge;
- procedural state;
- autobiographical/self-model lineage for an instantiated system;
- relationship/social-model history;
- values/commitment history;
- configuration/governance history;
- plasticity/consolidation traces;
- source/evidence ledgers.

These remain typed; “deep” does not flatten them into one memory class.

## Append-oriented history

Where historical integrity matters, corrections should create later linked records rather than silently altering prior evidence.

Recommended lifecycle relations:

```text
ADD
REVISE
CONTRADICT
SUPERSEDE
REVOKE
COMPLETE
REVIEW
```

## Retrieval

Retrieval should return content plus the metadata needed to judge present eligibility:

- memory class;
- provenance;
- time;
- privacy scope;
- currentness rule;
- contradiction/supersession state;
- confidence/evidence ceiling;
- source integrity.

## Admission to live cognition

A retrieved durable record becomes live only after the consuming coalition applies appropriate currentness, relevance, privacy, and authority rules.

## Archival truth boundary

The archive can faithfully preserve that a proposition/state was recorded without proving that proposition was objectively true.

## Failure modes

- archival persistence treated as present truth;
- newest record always treated as authoritative without supersession semantics;
- source and interpretation merged;
- private history exported automatically;
- missing contradiction interpreted as persistence;
- retrieved state silently promoted into current self/goal/consent state.
