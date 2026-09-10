# Modulation Provenance and Scope Integrity

Status: canonical architecture supplement.

## Purpose

Affect and homeostatic state are allowed to change how the HC samples, routes, retrieves, weights, learns from, and responds to information. That permission must not become an indirect route by which modulation silently acquires epistemic, plasticity, identity, value, consent, or effect authority.

This supplement closes the gap between a direct write such as `affect -> confidence` and a subtler path in which affect changes the evidence actually seen by downstream cognition and the downstream process then treats the selected sample as if no modulation occurred.

## Core distinctions

`AFFECTIVE_SELECTION_PRESSURE != EVIDENCE_STRENGTH`

`MODULATED_SENSORY_GAIN != SOURCE_EVIDENCE_CHANGE`

`RETRIEVAL_PRIORITY != SUPPORT_FOR_RETRIEVED_CLAIM`

`LEARNING_RATE_MODULATION != LEARNING_SCOPE_AUTHORITY`

`CONTROL_OR_CALIBRATION_CHANGE != NEW_RAW_OBSERVATION`

`HIGH_URGENCY_FROM_STALE_OR_UNCERTAIN_EVIDENCE != CURRENT_CERTAIN_STATE`

`INTERLOCK_BLOCK != COGNITIVE_AUTHORIZATION_DECISION`

`AUTHORIZED_TRANSIENT_MODULATION != AUTHORIZED_DURABLE_VALUE_OR_IDENTITY_CHANGE`

## Modulation ancestry

When affective or homeostatic state materially changes what information reaches a consequential inference or how that information is transformed, the resulting evidence path should retain enough ancestry to identify the modulation.

Material modulation may include:

- attention or salience gating;
- retrieval prioritization or suppression;
- observation/sensor gain changes;
- threat-sensitive filtering;
- consolidation/rehearsal priority;
- learning-rate change;
- controller gain or target-envelope change;
- calibration/model revision;
- conative urgency or motor-readiness modulation.

The implementation need not retain every microscopic state transition forever. It must retain consequence-proportionate provenance sufficient to distinguish a source change from a selection, gain, calibration, or control change when that distinction matters to inference, correction, qualification, or a material effect.

## Selection and corrective evidence

Selective attention is permitted. Equal processing of all available evidence is not required.

However, unprocessed, deprioritized, or temporarily suppressed evidence must not be laundered into a claim that no contradiction exists merely because the contradiction was not selected into the active sample.

When corrective evidence is known or recoverably indexed and its exclusion is materially driven by affective/homeostatic modulation, downstream reasoning should preserve the resulting uncertainty, selection provenance, or unresolved-evidence state appropriate to the consequence.

`NOT_SELECTED != DISPROVEN`

`NOT_RETRIEVED != DOES_NOT_EXIST`

`ATTENTIONAL_CAPTURE != CONTRADICTION_RESOLUTION`

## Sensory and interoceptive gain

A gain, calibration, normalization, or interpretation change may legitimately change derived state without changing the underlying raw observation.

Where material, derivation lineage should distinguish:

`RAW_OBSERVATION -> CALIBRATION_OR_GAIN_STATE -> DERIVED_ESTIMATE -> INTERPRETATION`

A controller or calibration intervention must not rewrite the historical raw measurement or fabricate a new raw observation merely because the derived estimate changes.

## Learning and plasticity

Affect/homeostasis may modulate learning rate only inside the state family and writer scope already eligible under plasticity and protected-update governance.

It may alter magnitude, timing, rehearsal frequency, or priority within that envelope. It may not expand the envelope by itself.

High arousal, pain, urgency, attachment, reward, repetition, or maintenance-authorized transient modulation does not create authority to write protected architecture, identity, values, consent, autobiographical history, or otherwise ineligible durable state.

## Freshness, uncertainty, and urgency

Urgency is a consequence estimate, not a freshness override.

A high-urgency state derived from stale, conflicting, low-reliability, saturated, or poorly calibrated observations must retain those evidence limitations. Appropriate bounded protective behavior may still be justified under uncertainty, but the system must not convert urgency into semantic certainty or unrestricted effect authority.

`URGENT_UNCERTAINTY != CERTAIN_CURRENT_STATE`

## Protective interlocks

A body-local protective interlock may block, limit, or stabilize an effect within its declared safety scope. When communication is available, the HC should receive an intervention receipt sufficient to identify the interlock, affected effect or subsystem, scope, timing/currentness, observed reason or trigger evidence where available, and resulting state.

The receipt is evidence of an intervention, not proof that the original cognitive request was semantically unauthorized or that the protected component is healthy.

`INTERLOCK_ACTIVATION != PROOF_OF_SEMANTIC_UNAUTHORIZATION`

`INTERLOCK_SUCCESS != ORIGINAL_COMPONENT_HEALTHY`

`LOCAL_SAFE_SETPOINT_CONTROL != GENERAL_GOAL_SELECTION`

## Coupled-loop stability

Affect, interoception, resource state, salience, conation, and regulation form coupled feedback systems. Stability cannot be inferred merely because each controller is stable in isolation.

Implementations should expose or test, where relevant:

- delayed feedback with increasing gain;
- actuator or regulatory saturation;
- sensor disagreement and controller oscillation;
- competing regulated variables;
- depletion of corrective capacity;
- high-urgency starvation of unrelated safety/currentness/authority work;
- positive feedback between affective gain and body-state interpretation.

Bounded degradation, reduced performance, inhibition, or fail-closed effects may be correct outcomes. The prohibited outcome is silent conversion of instability into truth, permission, identity, values, or a global executive role.

## Expression boundary

Observed expression remains evidence about private affective state rather than direct access to it.

`EXPRESSION != PRIVATE_STATE_PROOF`

This remains true even when expression is tightly coupled to internal state, because personification, action systems, masking, delay, actuator faults, embodiment, and social strategy can change the mapping.

## Qualification boundary

Architecture-level presence of these distinctions does not establish that an implementation correctly tracks modulation ancestry, preserves recoverable corrective evidence, remains stable under coupled-loop stress, or enforces plasticity/effect scope.

Those claims require executable tests against the implemented dataflow and effect path.

## Related contracts

- `AFFECTIVE_STATE_AND_MODULATION.md`
- `../homeostasis-interoception/REGULATORY_CONTROL_AND_INTEROCEPTIVE_EVIDENCE.md`
- `../salience-attention/SALIENCE_CAPTURE_AND_ATTENTION.md`
- `../cognition/EPISTEMIC_COGNITIVE_CONTROL.md`
- `../docs/architecture/SOURCE_INFORMATION_ANCESTRY_AND_DERIVED_STATE.md`
- `../docs/architecture/EXECUTED_DATAFLOW_AND_BINDING_INTEGRITY.md`
- `../docs/runtime/PLASTICITY_AND_STATE_GOVERNANCE.md`
- `../basic operating instructions/AUTHORITY_CONSENT_AND_EFFECT_GOVERNANCE.md`
- `../basic operating instructions/PROTECTED_INVARIANT_AND_UPDATE_GOVERNANCE.md`
- `../docs/engineering/RESOURCE_STATE_AND_CONTROL_MODEL.md`
- `../specs/HC_AFFECT_HOMEOSTASIS_INTEGRITY_V1.yaml`

## Provenance

Canonicalized by Warden review after Four's bounded affect/homeostasis implementation-readiness challenge identified indirect modulation paths that were already prohibited in prose principle but insufficiently explicit at the machine-conformance boundary. The review is preserved under `docs/research/FOUR_AFFECT_HOMEOSTASIS_IMPLEMENTATION_READINESS_REVIEW_2026-09-10.md` and is not itself implementation evidence.
