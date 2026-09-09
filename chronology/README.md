# Chronology

Status: GENERIC SUBSYSTEM CONTRACT / DESIGN

## Purpose

`chronology/` provides event-time representation, ordering, intervals, elapsed-time computation, and chronology indexes.

Chronology answers **when**. It does not decide **what an event means** or **which event is authoritative**.

## Event-time record

A chronology record may contain:

- stable event ID;
- source timestamp;
- canonical/reference time or interval;
- local/original time representation;
- clock domain;
- timestamp resolution;
- uncertainty bound;
- sequence;
- source ref;
- small typed metadata.

## Ordering

When timing uncertainty matters:

```text
A definitely precedes B
iff A.latest < B.earliest
```

If intervals overlap, order is `UNRESOLVED` unless additional evidence settles it.

Ingest order must not silently substitute for event order.

## Chronology vs currentness

```text
LATER_TIMESTAMP != GREATER_AUTHORITY
NEWEST_RECORD != CURRENT_STATE
```

Currentness is resolved by state/provenance/supersession contracts, not chronology alone.

## Elapsed time

Elapsed time may be calculated between event/time references when their time mappings are sufficiently qualified. If cross-clock uncertainty is too high, the result should expose that limitation.

## Missing events

Absence of a record is not automatically evidence that an event did not happen. A known expected cadence may support dropout detection only when that cadence is itself qualified.

## Failure modes

- arrival order presented as causal order;
- local time parsed without timezone/clock context;
- uncertain overlap presented as definite sequence;
- newer record treated as truth/currentness winner;
- chronology service adding semantic interpretation to event payloads;
- unqualified cross-clock timing used for causal/phase claims.
