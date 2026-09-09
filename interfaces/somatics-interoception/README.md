# Somatics and Interoception Interface

Status: GENERIC INTERFACE SUBSYSTEM / DESIGN

## Purpose

`interfaces/somatics-interoception/` connects the HC to signals about its current body/internal physiological condition and maintains calibrated mappings into body-state evidence.

External sensors may measure temperature, current draw, pressure, force, joint state, damage, energy reserves, fluid/chemical state, synthetic endocrine signals, thermal limits, or other internal variables.

## Interoception is rich state

The interface should not collapse the body into one `health=good/bad` scalar.

Possible dimensions include:

- energy availability;
- thermal state;
- structural strain/damage;
- actuator fatigue/load;
- fluid/chemical balance;
- pain/nociceptive-like channels if implemented;
- synthetic endocrine/neuromodulatory state;
- respiratory/gas-exchange analogues where applicable;
- internal fault signals;
- uncertainty/quality.

## Evidence layers

```text
MEASURED: sensor value
DERIVED: normalized/filtered body variable
INFERRED: fatigue, injury, threat, comfort, urgency, etc.
```

## Body schema

Somatic channels contribute to the learned body model, including:

- segment/effector topology;
- joint/pose state;
- sensor location;
- expected dynamics;
- self/non-self boundaries for attached devices;
- current capability limits.

## Interaction with affect/conation

Interoceptive evidence may modulate affect, salience, motivation, memory, and action urgency through typed modulatory paths. Those downstream appraisals remain distinct from raw measurements.

## Failure modes

- body fault inference stored as sensor fact;
- sensor dropout interpreted as normal state;
- changed body topology retaining stale mappings;
- one sensor becoming sole unquestioned truth for body condition;
- interoceptive urgency bypassing action authority/safety constraints.
