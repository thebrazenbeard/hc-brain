# Adaptable I/O

Status: GENERIC INTERFACE SUBSYSTEM / DESIGN

## Purpose

`interfaces/adaptable-io/` allows the HC to discover, classify, calibrate, and learn novel sensor/effector interfaces without changing the core brain architecture.

This subsystem is central to body portability.

## Discovery contract

A new interface should expose or allow the HC to infer safely:

- stable interface/device identity;
- direction: sense / effect / duplex;
- channel count/types;
- units/representation;
- ranges/resolution;
- update/cadence/timing semantics;
- error/quality signals;
- calibration procedure;
- safe-state/effect limits;
- authority requirements;
- transport/protocol metadata.

Unknown fields remain unknown.

## Learning sequence

```text
DISCOVERED
→ capability inventory
→ calibration hypotheses
→ bounded calibration/test
→ qualification evidence
→ body-schema / semantic mapping
→ ACTIVE
```

For hazardous effectors, calibration does not authorize unrestricted actuation.

## Semantic mapping

A channel starts as a typed signal channel, not an assumed meaning.

Example:

```text
channel 17 = 0.42 V
```

may later be learned/qualified as part of a pressure, chemical, joint-angle, or other sensor mapping. The early raw value should remain provenance-linked.

## Novel embodiments

Adaptable I/O should support:

- extra limbs;
- wheels/tracks;
- wings;
- distributed cameras;
- remote manipulators;
- unusual environmental sensors;
- detachable tools;
- virtual/simulated bodies;
- mixed local/remote effectors.

## Failure modes

- guessing units/ranges to satisfy a schema;
- using marketing/nominal capability as qualified limit;
- assigning semantic meaning before calibration;
- treating discovered effector as authorized;
- silently inheriting another body's mappings.
