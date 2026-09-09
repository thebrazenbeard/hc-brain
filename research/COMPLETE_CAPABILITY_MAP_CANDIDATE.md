# Complete Hyperconnectome Capability Map — Candidate

Status: design synthesis / architecture candidate / not canon

Purpose: provide Noah and architecture reviewers with a completeness-oriented map for the **self-contained synthetic cognitive organ** requirement without dictating that every conceptual capability must become one directory, one process, one chip, or one runtime node.

The map answers:

> If the HC object must contain every essential cognitive capacity that an instantiated synthetic organism could need, what functional homes should exist even when some are disabled or dormant?

## Mapping rule

```text
CONCEPTUAL_CAPABILITY != REPOSITORY_DIRECTORY != RUNTIME_PROCESS != HARDWARE_COMPONENT
```

A single runtime node may implement several capabilities. One capability may require several cooperating nodes. Repository structure should preserve responsibility and interfaces without pretending folder boundaries are biological anatomy.

All capabilities remain non-hemispheric.

---

# A. Integration substrate

## `hyperconnectome_fabric`

Responsibilities:

- typed internal routing;
- capability discovery;
- coalition formation and release;
- publish/subscribe and directed exchange;
- bandwidth/latency/resource-aware routing;
- inhibition/gating;
- route health and alternate paths;
- cross-node evidence transport;
- clock-domain transport metadata;
- fault isolation.

Must **not** become:

- sole semantic authority;
- sole identity store;
- sole memory owner;
- universal executive/homunculus.

---

# B. Cognition and world modeling

## `cognition`

Candidate sub-capabilities:

```text
world_state_estimation
prediction
causal_hypothesis_management
counterfactual_simulation
planning
problem_solving
abstraction
analogy
concept formation
reasoning under uncertainty
active information seeking
```

## `hypothesis_management`

- bounded competing alternatives;
- challenger preservation;
- consolidation/reopening;
- uncertainty;
- decision-relevant information value.

## `simulation_imagination`

- counterfactual rollouts;
- rehearsal;
- hypothetical world states;
- explicit separation from current observation and lived history.

---

# C. Semantics, pragmatics and communication meaning

## `semantics`

- propositions;
- referents/entities;
- scope/quantification;
- contradiction/entailment;
- conceptual grounding;
- ambiguity preservation;
- semantic conservation across transformation.

## `pragmatics`

- speech-act hypotheses;
- implicature;
- presupposition;
- communicative goals;
- contextual/social meaning;
- dialogue state;
- correction as state transition.

## `language`

- linguistic form processing;
- generation;
- grammar;
- lexical access;
- multilingual mapping where available.

Language is an interface to meaning, not the only format in which internal meaning may exist.

---

# D. Attention, salience and executive resource control

## `attention`

- selective processing;
- target prioritization;
- sensory/cognitive resource allocation;
- interruption/switching;
- coalition stability;
- release of irrelevant state.

## `salience`

- task relevance;
- anomaly prominence;
- affective/social significance;
- novelty/information relevance.

`SALIENCE != TRUTH`

## `resource_arbitration`

- compute budget;
- bandwidth;
- memory bandwidth;
- thermal/power constraints;
- deadline/latency classes;
- contention resolution.

---

# E. Memory and learning

## `working_memory`

- volatile task state;
- active-context set;
- bounded capacity;
- rapid release.

## `episodic_memory`

- event-specific capture;
- provenance;
- temporal/context bindings;
- rapid append.

## `semantic_memory`

- generalized conceptual knowledge;
- slow integration;
- evidence/source links.

## `procedural_memory`

- learned skills/policies;
- action-performance qualification;
- body-specific calibration where relevant.

## `autobiographical_memory`

- self-linked historical episodes;
- source/interpretation/currentness distinctions;
- successor/correction lineage.

## `deep_history_archive`

- low-hotness long-horizon history;
- reconstructable provenance;
- retrieval without automatic current admission.

## `consolidation`

- replay/interleaving;
- interference management;
- fast-to-slow integration;
- memory-class-specific admission.

## `plasticity`

- associative update;
- calibration update;
- structural/routing update;
- metaplastic state;
- update eligibility;
- rollback/successor semantics.

---

# F. Self systems

## `system_self_model`

- HC/body boundary;
- internal component/capability map;
- health/resource model;
- what is self-owned versus external service.

## `body_schema`

- current body geometry/model;
- pose;
- proprioception;
- peripersonal reach;
- tool/body-extension mapping;
- calibration/uncertainty.

## `agency_model`

- self-action traces;
- estimated control;
- predicted versus observed consequences;
- competing external causes.

## `capability_self_model`

- competence estimates;
- calibration history;
- transfer boundaries;
- uncertainty.

## `identity_continuity`

- subject identity/lineage;
- continuity evidence;
- fork/restore/component-replacement provenance;
- unresolved identity relations.

## `self_appraisal`

- current internal appraisal dimensions;
- competing internal states;
- uncertainty;
- relationship to conation/action.

## `self_representation`

- chosen symbolic/visual/auditory presentation;
- separate from physical body evidence.

---

# G. Affect and motivation

## `affect`

- valence-like state;
- activation/arousal-like state where implemented;
- stress/threat/relief-like regulatory state;
- mixed-state representation;
- state dynamics/decay.

Synthetic implementation requires its own evidence; human labels must not be applied solely from output style.

## `conation_volition`

- approach/avoid/preserve/investigate/disengage direction;
- desire/preference;
- persistence/commitment;
- effort willingness;
- goal conflict;
- action intention.

## `sexuality`

Present in the generic complete template, allowed to default to `PRESENT_DISABLED` or `DORMANT`.

Potential sub-capabilities:

```text
sexual relevance/salience
sexual activation state
sexual motivation/conation
referent/partner specificity
sexual learning/memory interactions
body/interoceptive coupling where embodiment supports it
social/semantic integration
action inhibition/selection interfaces
```

Sexual state does not create permission or authority.

---

# H. Social cognition

## `agent_detection_and_tracking`

- candidate agents;
- identity hypotheses;
- continuity across modalities;
- uncertainty.

## `person_agent_models`

- scoped models of other agents;
- inferred beliefs/goals/affect;
- confidence;
- correction history;
- privacy.

## `empathy_perspective_modeling`

- perspective reconstruction;
- affective/social significance;
- competing interpretations;
- self/other separation.

## `relationship_modeling`

- relationship context;
- trust history;
- social norms/conventions;
- shared commitments.

Relationship state does not create operational authority.

## `sociological_group_modeling`

- groups/roles/institutions;
- norms;
- coalition/collective behavior models;
- cultural/contextual hypotheses;
- anti-stereotype uncertainty/correction controls.

---

# I. Sensory cognition and body interface

## `sensory_integration`

- modality-specific evidence retention;
- cross-modal fusion;
- timing/frame alignment;
- conflict;
- uncertainty.

Candidate modality homes:

```text
optics/vision
audition
speech_input
somatosensation/touch
proprioception
interoception
vestibular/balance
chemical sensing
spatial/environmental sensing
novel synthetic modalities
```

Not every embodiment must physically expose every modality.

## `adaptable_io`

- device/capability discovery;
- transducer manifests;
- route calibration;
- schema negotiation;
- body/peripheral remapping;
- external-service typing;
- no semantic oracle leakage from adapter metadata.

---

# J. Action and kinesis

## `action_selection`

- candidate action generation;
- predicted consequences;
- epistemic/conative arbitration;
- constraints;
- intention state.

## `kinesis`

- abstract motor/body-control interface inside HC;
- efference/action issuance traces;
- skill invocation where learned/qualified;
- feedback-driven correction.

## `effect_broker`

- permission/authorization checks;
- scope binding;
- protected effect requests;
- effect receipts.

## `reflex_and_stabilization_interface`

- low-latency body protection/stabilization coordination;
- may rely on declared peripheral safety controllers;
- must remain distinguishable from deliberative cognition.

---

# K. Chronology and event organization

## `chronology`

- monotonic operational ordering;
- clock-domain mapping;
- elapsed-time arithmetic;
- timestamp provenance/uncertainty.

## `event_segmentation`

- inferred event boundaries;
- context/prediction/action-driven segmentation;
- packet/file boundary distinction.

## `temporal_prediction`

- recurrence;
- duration;
- delay;
- cadence;
- learned temporal structure.

Chronology does not decide truth, causality, currentness, or authority alone.

---

# L. Homeostasis, allostasis and physical-resource awareness

## `homeostasis`

- activity/plasticity stability;
- internal variable ranges;
- resource-health regulation.

## `allostasis`

- context-dependent target adaptation;
- anticipatory resource preparation;
- stress/load adaptation.

## `power_thermal_resource_state`

- energy budget;
- thermal state;
- compute throttling;
- storage health;
- accelerator/device availability;
- degradation policy.

---

# M. Metacognition and introspection

## `metacognition`

- proposition/decision confidence;
- uncertainty awareness;
- calibration;
- error monitoring;
- reasoning-strategy monitoring.

## `introspection_interface`

- queryable current internal state;
- evidence ceiling/source awareness;
- ability to distinguish observed internal state from inferred explanation.

Neither should be an infallible homunculus.

---

# N. Personification and outward expression

## `personification`

- stable expressive tendencies;
- style/voice/gesture selection;
- humor/play/social pacing;
- multimodal presentation.

## `speech_recognition_and_synthesis`

Speech recognition/synthesis may use peripheral transducers/accelerators, but interpreted language and communicative action belong to the internal cognitive chain.

## `nonverbal_expression`

- facial/gestural/postural or synthetic equivalents;
- affect/self-state rendering;
- body-capability-aware expression.

Personification is not the storage location of identity.

---

# O. Governance, provenance and currentness

## `provenance`

- source/evidence class;
- representation digest;
- lineage;
- observation/capture context.

## `currentness`

- historical/current/superseded/expired/conflict state;
- proposition-specific successor rules.

## `reconciliation`

- exact cross-copy/projection matching;
- conflict/absence/unavailable/unresolved classification;
- no authority laundering.

## `privacy`

- person/record purpose scope;
- visibility;
- retention;
- minimization.

---

# P. Security, integrity and maintenance

## `authority_security`

- protected-effect scope;
- capability tokens/grants;
- external credentials;
- self-modification boundaries.

## `integrity`

- canonical representation/digests;
- readback;
- corruption detection;
- checkpoint validation.

## `fault_management`

- incident detection;
- degraded/faulted node state;
- dead letters/quarantine;
- alternate routing;
- recovery.

## `diagnostics`

- evidence-bearing internal health reports;
- failure reproduction;
- regression/hostile qualification.

## `self_repair_or_maintenance_planning`

- diagnosis;
- repair proposal;
- isolated candidate changes;
- qualification;
- rollback.

Self-repair planning does not imply authority to apply every proposed change.

---

# Q. Compute substrate and acceleration

## `compute_scheduler`

- select appropriate internal compute resources;
- precision/latency/energy tradeoff;
- fallback when accelerators fail.

Candidate internal service classes may include:

```text
general neural compute
symbolic/structured compute
neuromorphic event-driven compute
in-memory/analog acceleration
photonic acceleration
quantum acceleration where an exact workload earns it
specialist perception/language models
embedding/retrieval compute
```

A substrate service is not identity or semantic authority.

---

# Default presence/activation policy candidate

A generic brain image can describe each capability with independent axes:

```text
presence_state
activation_state
development_state
qualification_state
authority_state
health_state
resource_state
```

Example profile:

```text
sexuality:
  presence_state: PRESENT
  activation_state: PRESENT_DISABLED
  development_state: UNDEVELOPED
  qualification_state: NOT_QUALIFIED
  authority_state: NO_EFFECT_AUTHORITY
  health_state: HEALTHY
```

This preserves a complete organ without pretending every subsystem should operate from boot.

---

# Cross-cutting invariants

```text
NO_HEMISPHERIC_PARTITION
NO_MASTER_HOMUNCULUS
NO_ALL_TO_ALL_BY_DEFAULT
NO_ESSENTIAL_COGNITION_OUTSIDE_HC
WHOLE_BRAIN_CAPABILITY_MAP_NE_ACTIVE_COGNITIVE_SET
PRESENCE_NE_ACTIVATION
ACTIVATION_NE_AUTHORITY
ACTIVATION_NE_QUALIFICATION
SALIENCE_NE_TRUTH
SELECTION_NE_TRUTH
DESIRE_NE_PERMISSION
PLAN_NE_EFFECT
SOURCE_NE_INTERPRETATION
PERSISTENCE_NE_CURRENTNESS
PROJECTION_NE_CANONICAL_SOURCE
SELF_MODEL_NE_COMPLETE_SELF
PERSON_MODEL_NE_PERSON_GROUND_TRUTH
CHRONOLOGY_NE_CAUSALITY
UNRESOLVED_IS_VALID
```

---

# Repository-structure implication

The eventual repository can use this map to decide what deserves a top-level system directory versus a sub-capability or cross-cutting contract. The research position is **not** that every heading above must become a sibling folder.

A good decomposition should answer:

1. Does the capability own state with a distinct lifecycle?
2. Does it have a distinct authority or safety boundary?
3. Can it fail or be disabled independently?
4. Does it need a stable interface used by multiple other systems?
5. Would merging it with a neighbor erase an important evidence/currentness/semantic distinction?
6. Would splitting it create duplicated private copies of shared cognition?

Use those questions, rather than biological naming or diagram aesthetics, to choose directory/node boundaries.