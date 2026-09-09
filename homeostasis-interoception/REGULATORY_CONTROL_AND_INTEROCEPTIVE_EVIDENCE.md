# Regulatory Control and Interoceptive Evidence Contract

Status: canonical template contract.

## Purpose

This contract defines how internal-body signals become HC-owned interoceptive evidence, how homeostatic error and urgency are represented, how regulation is requested and confirmed, and how protective peripheral mechanisms remain distinct from cognition.

The HC owns interpretation of bodily state, homeostatic estimation, regulatory policy, learned body expectations, and cognition-facing meaning. True body peripherals may provide measurements and execute bounded protective effects without becoming an external cognitive controller.

## Core distinctions

`RAW_TELEMETRY != INTEROCEPTIVE_STATE`

`INTEROCEPTIVE_STATE != SEMANTIC_TRUTH`

`HOMEOSTATIC_ERROR != ACTION_AUTHORITY`

`URGENCY != PERMISSION`

`REQUESTED_REGULATION != ACHIEVED_REGULATION`

`PROTECTIVE_INTERLOCK != COGNITIVE_EXECUTIVE`

`BODY_SUPPORT_DEPENDENCY != COGNITIVE_OWNERSHIP`

## Interoceptive evidence pipeline

A generic signal path is:

`body sensor -> observation envelope -> calibration/normalization -> physiological estimate -> interoceptive interpretation -> homeostatic error/need -> salience/conation/arbitration`

Each stage may add derived state, uncertainty, latency, calibration status, or confidence. Downstream consumers should be able to distinguish measured observations from derived and inferred state.

An interoceptive record should preserve where material:

- source sensor or body subsystem;
- modality/channel;
- units and expected range;
- timestamp and freshness;
- calibration state;
- uncertainty/reliability;
- body-location or functional scope;
- raw/derived/inferred classification;
- associated health/fault state;
- causal/provenance links to regulatory actions.

## Homeostatic state

Homeostatic control should represent more than a single scalar "need." Multiple partially competing regulated variables may coexist, including thermal, perfusion, energy, hydration/osmotic, respiratory/gas-exchange, chemical, endocrine, damage, fatigue/load, and implementation-specific resource states.

For a regulated variable `r`, implementations may track concepts such as:

- current estimate `x_r(t)`;
- acceptable operating envelope `B_r(t)`;
- predicted trajectory;
- error or deviation;
- urgency/consequence estimate;
- control confidence;
- available corrective actions;
- achieved response.

No particular numeric controller is mandated by the architecture.

## Multiple timescales

Regulation may occur on several timescales:

1. immediate hardware/tissue protection;
2. fast reflex or stabilization control;
3. short-timescale autonomic regulation;
4. slower endocrine/metabolic adaptation;
5. behavioral action and planning;
6. longer calibration, recovery, and plasticity.

A slower cognitive process must not be a single point of failure for hard real-time protection.

## Peripheral protective mechanisms

Body-local controllers may perform bounded low-level functions such as current limiting, thermal cutoff, collision interruption, pump stabilization, pressure relief, withdrawal-like actuator interruption, or other implementation-specific protective actions.

Such mechanisms are permitted outside the HC cognitive-organ boundary only when they remain noncognitive protective peripherals rather than seats of interpretation, learning, memory, values, identity, or general action selection.

A protective peripheral may:

- interrupt or limit a dangerous effect;
- hold a safe local setpoint;
- emit telemetry/fault state;
- request higher-level HC regulation.

It must not silently become an external deliberative controller.

`LOCAL_SAFETY_INTERLOCK_ALLOWED`

`EXTERNAL_GENERAL_HOMEOSTATIC_REASONING_NOT_ALLOWED`

## Regulation path

A cognition-facing regulatory path is:

`state estimate -> error/need -> predicted consequence -> regulatory candidate -> arbitration/authorization -> effect request -> body response -> outcome observation -> state update`

Where hard real-time protection is required, a peripheral interlock may interrupt this path but must report the event and resulting state back to the HC when communication is available.

## Coupling to affect and conation

Homeostatic and interoceptive state may influence:

- arousal;
- salience;
- threat/safety appraisal;
- fatigue and pain burden;
- motivational pressure;
- attention allocation;
- learning rate within policy;
- action urgency;
- affective state.

These influences do not convert physiological pressure into truth, consent, values, or unrestricted authority.

`NEED != VALUE`

`PAIN != COMMAND`

`THREAT_SIGNAL != CERTAINTY_OF_THREAT`

## Body swap and recalibration

A new embodiment may change sensor ranges, latencies, actuator characteristics, support requirements, and physiological baselines. Those changes require recalibration and possibly relearning of the body-state model without implying identity replacement.

Old calibration state should be invalidated or quarantined when incompatible with the new embodiment.

## Faults and disagreement

The subsystem should surface:

- sensor disagreement;
- stale telemetry;
- implausible rate-of-change;
- saturation;
- calibration drift;
- failed control response;
- actuator/controller disagreement;
- oscillatory correction;
- depleted correction capacity;
- thermal/perfusion/resource runaway;
- conflicting regulatory objectives;
- local interlock activation;
- communication loss to a body-support subsystem.

When internal-state evidence conflicts, the HC should preserve the conflict and adjust confidence rather than silently manufacture a single clean state.

## HC-3 relationship

HC-1 already requires body-state sensing and homeostatic integration sufficient for complete cognition and embodiment. HC-3 adds richer HC-owned neuroendocrine, autonomic, interoceptive, and physiological affective substrate.

Physical distribution does not alter ownership. HC-owned physiological modules may reside outside the skull while remaining part of the removable cognitive organ under `docs/architecture/PHYSICAL_ORGAN_MEMBERSHIP.md`.

## Evidence boundary

Biological interoception and homeostasis motivate this architecture, but exact synthetic sensors, control laws, chemistry, setpoints, and subjective consequences remain implementation-specific. The contract specifies functional ownership and state separation rather than asserting a particular biological reproduction.

## Related contracts

- `homeostasis-interoception/ARCHITECTURE.md`
- `somatics/BODY_STATE_AND_BODY_SCHEMA.md`
- `adaptable I-O handler/BODY_INTERFACE_BOUNDARY.md`
- `affect/AFFECTIVE_STATE_AND_MODULATION.md`
- `kinesis/ACTION_GATEWAY.md`
- `docs/architecture/HC3_NOOPLEX_EQ.md`
- `docs/engineering/POWER_THERMAL_AND_DISTRIBUTED_ORGAN.md`
