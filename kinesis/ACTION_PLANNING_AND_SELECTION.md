# Action Planning and Selection

Status: RECONCILED FOCUSED CONTRACT / DESIGN / NOT IMPLEMENTED

## Purpose

Within the canonical HC root, `kinesis/` owns the transition from an internally selected action candidate into a motor/action plan suitable for an HC-owned output gateway. Deliberative candidate generation may recruit cognition, volitions-conations, memory, affect, prediction, and integration-arbitration, but a separate `action/` root is not required.

## Core separation

```text
GOAL
!= ACTION_CANDIDATE
!= SELECTED_ACTION
!= AUTHORIZED_EFFECT
!= MOTOR_PLAN
!= MOTOR_COMMAND
!= VERIFIED_EFFECT
```

These are distinct temporal states in the HC. A plan or selection can exist without being authorized or executed.

## Action candidate

A candidate may carry:

- goal/referent;
- proposed action sequence or policy;
- predicted consequences;
- body/effector requirements;
- resource cost;
- uncertainty;
- reversible/irreversible classification;
- safety/authority requirements;
- alternatives;
- evidence/model references;
- fallback/abort criteria;
- temporal validity window.

## Planning inputs

Action planning may recruit:

- procedural memory;
- world-model/predictive cognition;
- current body schema;
- temporal constraints;
- social consequences;
- affective state;
- volitions/conations;
- values/commitments;
- salience/attention;
- assurance requirements.

Simulated consequences remain hypothetical until supported by observed outcome evidence.

## Selection and arbitration

Integration/arbitration may choose among currently eligible action candidates. Selection does not itself create external-effect authority.

```text
candidate set
-> scoped arbitration
-> selected action candidate
-> capability / safety / authority / resource gates
-> kinesis motor planning
-> HC-owned output gateway
-> external effect
-> observed consequence
```

An implementation may order or recur through these operations differently, but the semantic boundaries must remain representable.

## Abort and revision

An action plan should support explicit:

- precondition failure;
- abort condition;
- interruption;
- replan trigger;
- actuator degradation/fault;
- changed body state;
- changed world state;
- revoked/expired authority where applicable.

A selected plan must not become irrevocable merely because execution has begun.

## Consequence loop

Observed effects return through HC-owned sensory/body interfaces as evidence for:

- prediction-error evaluation;
- motor correction;
- procedural learning;
- world-model revision;
- episodic/current-memory update;
- future action-selection calibration.

`EXPECTED_CONSEQUENCE != OBSERVED_CONSEQUENCE`.

## Failure modes

- internal plan treated as external execution;
- procedural fluency bypasses authority or safety constraints;
- simulation output stored as observed consequence;
- stale body capabilities used for planning;
- irreversible/high-consequence action lacks appropriate assurance;
- abort/fault signals ignored during execution;
- selected candidate treated as automatically permitted;
- external actuator success assumed without consequence readback.

## Provenance

Reconciled from PR #4 `action/README.md` into the owner-established `kinesis/` root and aligned with current `kinesis/ARCHITECTURE.md`, the HC cognitive-organ boundary, and distributed integration/arbitration semantics.