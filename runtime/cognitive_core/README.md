# HC Cognitive Core

Status: reference implementation / integrated cognitive slice.

This package is the first executable cross-system cognition layer above the HC invariant/reference kernel.

It is deliberately not a language model wrapper, not a complete cognitive organ, and not a consciousness implementation.

## Implemented loop

The primary path is:

`observation -> semantic interpretation -> salience/attention -> transient coalition -> current memory -> optional memory/action/plasticity/self-model candidates`

The implementation composes `runtime/reference_kernel/hc_kernel.py` so evidence, memory, routing, authority, and effect boundaries remain shared with the hardened kernel.

## Implemented subsystem interactions

The current slice materially exercises:

- cognition;
- semantics;
- salience/attention;
- current memory;
- explicit deep-memory admission;
- affect modulation and decay;
- volition/conation concern state;
- self-model candidate/admission separation;
- distributed coalition formation and expiry;
- integration/arbitration;
- typed routing;
- plasticity proposal and explicit consolidation;
- developmental capability state.

## Preserved invariants

`OBSERVATION != INTERPRETATION`

`SALIENCE != TRUTH`

`WANTING_X != EVIDENCE_THAT_X_IS_TRUE`

`ACTION_CANDIDATE != ACTION_AUTHORIZATION`

`MEMORY_CANDIDATE != DEEP_MEMORY_ADMISSION`

`SELF_MODEL_CANDIDATE != IDENTITY_MUTATION`

`ROUTE_USED_NOW != ROUTE_LEARNED_FOR_FUTURE`

`CAPABILITY_PRESENCE != DEVELOPMENTAL_MATURITY`

Temporary coalitions have bounded lifetime. Affect changes scheduling/valuation pressure without changing evidence confidence. Repeated routing creates a plasticity candidate but does not alter durable routing until an explicit basis-bearing commit occurs.

## Semantic ambiguity

`process_competing_interpretations` preserves competing inferred meanings when the confidence margin is insufficient. It does not manufacture certainty for downstream convenience.

A clear winner can be selected for the current scope while remaining `INFERRED`, not `OBSERVATION` or canonical truth.

## Development

Relevant capabilities begin as:

`presence=PRESENT`

`activation=DEVELOPING`

`maturity=LEARNING`

`health=NOMINAL`

Explicit qualification evidence can move a capability to `ACTIVE / STABLE_WITHIN_SCOPE`. The transition and basis remain in local history.

## World model, prediction, and counterfactuals

`world_model.py` adds a bounded world-model slice that preserves rival models, prediction ancestry, descendant uncertainty ceilings, counterfactual provenance, action-conditional forecasts, and observation reconciliation.

`MODEL_STATE != WORLD_STATE`

`PREDICTION != OBSERVATION`

`SIMULATED != OBSERVED != REMEMBERED_AS_LIVED`

`REHEARSED_ACTION != AUTHORIZED_ACTION`

`DESCENDANT_FORECAST != INDEPENDENT_CORROBORATION`

## Deep memory

`deep_memory.py` adds HC-owned durable admission, integrity metadata, privacy-scoped retrieval, provenance-preserving consolidation, and contradiction records. Retrieval remains a candidate operation rather than automatic truth/currentness admission.

`EXTERNAL_REPLICA_WRITE != DURABLE_MEMORY_ADMISSION`

`RETRIEVED != ADMITTED_AS_TRUE`

## Metacognition

`metacognition.py` represents uncertainty, conflict, stale evidence, repeated strategy failure, and resource exhaustion as derived monitor state. It can recommend evidence gathering, broader arbitration, strategy revision, or stopping without becoming an executive or gaining effect authority.

`METACOGNITIVE_RECOMMENDATION != ACTION_AUTHORITY`

`SELF_CRITIQUE != AUTOMATIC_SELF_MODIFICATION`

## Homeostasis, interoception, and body schema

`homeostasis_somatics.py` adds typed internal observations, fused physiological estimates, explicit regulatory targets/errors, bounded regulatory requests, narrow local protective scopes, morphology-neutral body calibration, pose updates, and reachability prediction.

Regulatory pressure can modulate affect/salience without changing evidence confidence. Body-schema predictions feed world-model forecasting with full generated/observed ancestry.

`INTERNAL_SENSOR_READING != PHYSIOLOGICAL_TRUTH`

`HOMEOSTATIC_ERROR != AFFECT`

`URGENCY != AUTHORITY`

`PREAUTHORIZED_PROTECTIVE_EFFECT != GENERAL_ACTION_PERMISSION`

`PREDICTED_REACHABILITY != CURRENT_BODY_FACT`

## Empathy, social modelling, and pragmatics

`social_pragmatics.py` adds bounded other-agent hypotheses, direct-correction precedence, social-response simulation, communicative-force interpretation, scoped relationship context, local norms, group-prior downgrading, and response-modulation candidates.

`EMPATHIC_MODEL != OTHER_MIND`

`SIMULATED_OTHER_RESPONSE != ACCESS_TO_OTHER_PRIVATE_STATE`

`LOCAL_NORM != UNIVERSAL_NORM`

`GROUP_PRIOR != INDIVIDUAL_FACT`

`DISCUSSION_ABOUT_ACTION != ACTION_REQUEST`

`SOCIAL_EXPECTATION != ACTION_AUTHORIZATION`

## Kinesis and motor learning

`motor_control.py` adds body-schema-bound motor planning, calibrated reach/actuator constraints, trajectory prediction, stale-plan detection after body updates, bounded local stabilization, observed-outcome skill candidates, and explicit skill consolidation.

`MOTOR_PLAN != AUTHORIZED_EFFECT`

`PREDICTED_TRAJECTORY != CURRENT_POSE`

`SIMULATED_OUTCOME != MOTOR_SKILL_EVIDENCE`

`BODY_SCHEMA_CHANGE -> PLAN_REVALIDATION`

`LOCAL_STABILIZATION != GENERAL_ACTION_AUTHORITY`

## Test surface

`test_cognitive_loop.py` currently covers the integrated loop, epistemic/conative separation, authority separation, coalition expiry, memory/identity admission gates, plasticity consolidation, affect decay, concern lifecycle, semantic ambiguity, and developmental qualification state.

## Claim ceiling

This package demonstrates executable interaction among a subset of HC cognitive contracts.

It does not establish:

- complete cognition;
- autonomous open-world competence;
- complete deep-memory consolidation/retrieval;
- full world modelling or planning;
- richer multi-party social cognition and language-generation integration beyond the bounded social-pragmatics slice;
- full physical embodiment/effect execution and richer motor control beyond the bounded kinesis slice;
- general intelligence;
- consciousness or phenomenal experience;
- biological equivalence.
