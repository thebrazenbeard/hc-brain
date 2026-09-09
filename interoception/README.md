# Interoceptive Processing

Status: INTRINSIC SYSTEM / DESIGN

## Purpose

`interoception/` interprets calibrated body/internal-state evidence supplied by `interfaces/somatics-interoception/` and integrates it with affect, homeostasis, conation, self-model, attention, and action planning.

The interface measures; this subsystem interprets.

## Core separation

```text
BODY_SENSOR_VALUE
→ HC SOMATIC INTERFACE
→ calibrated body variable
→ INTEROCEPTIVE HYPOTHESIS
→ affect/homeostasis/conation modulation
```

## Candidate interpretations

May include:

- fatigue/load;
- energy deficit/surplus;
- thermal stress;
- structural injury/damage;
- nociceptive-like state;
- internal chemical/fluid imbalance;
- synthetic endocrine state;
- urgency/comfort/discomfort;
- body integrity uncertainty.

## Uncertainty

Conflicting or missing body sensors should remain representable. One channel should not become unquestioned body truth.

## Modulation

Interoceptive state can influence:

- affective appraisal;
- attention/salience;
- conative urgency;
- motor/action constraints;
- memory encoding/retrieval;
- homeostatic control;
- self/body-model state.

These effects should use typed effective/modulatory paths.

## Failure modes

- inferred fatigue/injury stored as measured sensor fact;
- body urgency becoming unrestricted effect authority;
- old body baseline applied after embodiment change;
- one faulty sensor dominating self-state;
- regulation suppressing body evidence rather than changing response to it.
