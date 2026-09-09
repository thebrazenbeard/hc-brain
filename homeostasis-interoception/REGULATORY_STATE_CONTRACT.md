# Regulatory State Contract

Status: template architecture.

## Purpose

This contract defines how the HC represents internal-body evidence, physiological/resource estimates, regulatory targets, errors/needs, protective control, and slower allostatic adaptation without collapsing those layers into one health score or allowing internal state to masquerade as truth, identity, consent, or unrestricted action authority.

## Core separations

`INTERNAL_SENSOR_READING != PHYSIOLOGICAL_TRUTH`

`PHYSIOLOGICAL_ESTIMATE != HOMEOSTATIC_ERROR`

`HOMEOSTATIC_ERROR != AFFECT`

`HOMEOSTATIC_ERROR != CONATIVE_COMMITMENT`

`URGENCY != AUTHORITY`

`REGULATORY_REQUEST != EXTERNAL_ACTION_AUTHORIZATION`

`MODULATION != EVIDENCE`

Internal origin does not make a signal infallible. Interoceptive and regulatory objects retain source, calibration, uncertainty, timing, and disagreement state.

## Object families

### InteroceptiveObservation

Represents measured or derived internal-body evidence.

Conceptual fields may include:

- variable/channel identity;
- sensor/interface identity;
- observation time and clock uncertainty;
- measured/derived class;
- value/range;
- unit/encoding;
- calibration state;
- reliability/confidence;
- saturation/fault state;
- embodiment/body-region binding;
- provenance.

### PhysiologicalEstimate

Represents an inferred or fused estimate of internal condition.

Conceptual fields may include:

- variable/state identity;
- supporting observations;
- estimate/range/distribution;
- expected operating range;
- confidence;
- trend/rate of change;
- competing estimates;
- anomaly state;
- provenance;
- currentness/expiry.

Multiple estimates may coexist when redundant sensors disagree.

### RegulatoryTarget

Represents a desired operating range or context-dependent control target.

A target should carry:

- variable/state identity;
- target range/distribution;
- target source or policy;
- valid context;
- valid time window;
- protected minimum/maximum if applicable;
- authority/provenance for target modification.

Targets are not always fixed set points. Allostatic or workload-dependent targets may vary with context, but target changes must remain explicit and attributable.

### RegulatoryError

Represents the discrepancy between estimated state and applicable target.

Useful fields include:

- estimate reference;
- target reference;
- error magnitude/direction;
- urgency;
- predicted consequence if unresolved;
- time-to-risk estimate where available;
- confidence;
- affected capability/resource scope.

### RegulatoryRequest

Represents a proposed internal correction.

Examples include thermal regulation, resource throttling, fluid/energy management, autonomic/endocrine-like modulation, posture/load change, rest/recovery, or local actuator protection.

A request is not automatically an authorized external behavior.

## Regulatory timescales

The HC should support interacting control loops at multiple timescales:

1. `FAST_PROTECTIVE` — immediate bounded damage-prevention/reflex control;
2. `SHORT_REGULATORY` — autonomic/resource regulation over seconds to minutes;
3. `SLOW_MODULATORY` — endocrine-like/metabolic adaptation over longer intervals;
4. `RECOVERY_AND_PLASTICITY` — recalibration, repair, and durable adaptation.

Slow cognitive deliberation must not be a single point of failure for pre-authorized protective minima.

## Protective authority boundary

Fast protective regulation may hold narrowly scoped standing authority over internal protective effects when the embodiment requires hard real-time control.

That authority must be:

- local to declared protective effect scopes;
- bounded by safety envelopes;
- observable/auditable;
- revocable or supersedable through explicit governance where technically safe;
- unable to silently expand into general external action authority.

Examples include thermal throttling, actuator current limiting, emergency pressure/flow correction, or damage-prevention shutdown.

`PREAUTHORIZED_PROTECTIVE_EFFECT != GENERAL_ACTION_PERMISSION`

## Sensor disagreement and uncertainty

Internal measurements may be wrong, stale, saturated, biased, disconnected, or mutually inconsistent.

Explicit states should include, where useful:

- `AGREEMENT`;
- `SENSOR_CONFLICT`;
- `CALIBRATION_SUSPECT`;
- `SOURCE_UNAVAILABLE`;
- `STALE_STATE`;
- `SATURATED`;
- `FAULTED`;
- `UNRESOLVED`.

No single internal sensor gains truth authority merely because it is physically inside the organism.

## Coupling to affect and salience

Regulatory error and interoceptive state may influence affective dimensions, salience, learning rate, memory access, fatigue, pain, action urgency, and conative priority.

The coupling must preserve direction and provenance. A body-state estimate can change how evidence is processed without changing the evidential truth status of a proposition.

## Coupling to cognition and action

Cognition may forecast future regulatory needs, compare strategies, and propose anticipatory/allostatic action. Affect and conation may influence regulation targets or gain within permitted ranges.

Material external action still uses the appropriate action-selection and authorization path unless it falls inside an explicitly pre-authorized protective scope.

## Homeostatic stability of the HC itself

The same architecture can represent internal computational-resource stability, including:

- power/energy reserve;
- thermal load;
- communication bandwidth;
- synchronization pressure;
- memory/storage pressure;
- accelerator saturation;
- error/fault burden;
- plasticity/update load.

These resource variables remain typed; avoid one global `health` scalar as the sole control state.

## Failure controls

The system should detect or bound:

- runaway control gain;
- oscillatory correction;
- chronic target drift;
- target changes without authority/provenance;
- stale or contradictory interoceptive estimates;
- protective controller capture of general action authority;
- unbounded resource demand;
- thermal/energy collapse;
- modulatory saturation;
- regulatory action whose observed effect contradicts the expected effect.

## Evidence boundary

This contract generalizes current HC homeostasis/interoception architecture and research on homeostatic/allostatic regulation, active stability, multimodal internal sensing, and bounded protective control. Exact embodiment sensors, chemistry, setpoints, and physical realization remain implementation-dependent.