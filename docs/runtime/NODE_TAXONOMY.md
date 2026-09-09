# Noöplex Node Taxonomy

**Status:** conceptual taxonomy / runtime responsibility model

## Purpose

The original architecture seed lists empathy, cognition, sexuality, self identity, psychological and sociological behavior, semantics, pragmatics, phonetics, somatics, chronology, personification, current and deep memory, volition/conation, resolver logic, operating instructions, kinesis, adaptable I/O, optics, speech, routing, and neuroplasticity.

That list is valuable, but it mixes different kinds of things:

- cognitive faculties;
- representational systems;
- memory classes;
- embodiment systems;
- I/O channels;
- action systems;
- executive/arbitration mechanisms;
- infrastructure and maintenance.

A runtime taxonomy should preserve those ideas while separating their architectural roles.

## 1. Perception and I/O nodes

Examples:

- optics / visual perception;
- speech recognition;
- audition;
- tactile/proprioceptive input;
- internal diagnostics;
- adaptable external I/O;
- speech synthesis;
- expressive motor output.

Responsibilities:

- convert physical or external signals into confidence-bearing internal representations;
- preserve source, timing, calibration, uncertainty, and body frame;
- distinguish missing data from negative evidence;
- expose modality-specific features without forcing all modalities into one token stream.

These nodes observe and render. They do not own semantic truth.

## 2. Representational and linguistic nodes

Examples:

- semantics;
- pragmatics;
- phonetics/phonology;
- discourse/context tracking;
- symbol/concept binding;
- multimodal representation mediation.

Responsibilities:

- map forms to candidate functions/relations under context;
- maintain ambiguity where unresolved;
- distinguish literal form from inferred intent/use;
- support cross-modal and cross-linguistic representation;
- preserve provenance for inferred meaning.

Pragmatics should be able to alter interpretation without rewriting the raw observation that triggered it.

## 3. Memory and temporal nodes

Examples:

- current/working memory;
- episodic memory;
- deep autobiographical memory;
- semantic memory;
- procedural memory;
- chronology/time ordering;
- future simulation and prospective memory.

Responsibilities:

- maintain time, source, context, confidence, and correction history;
- separate current state from durable history;
- support consolidation without silent replacement of evidence;
- retrieve rather than overwrite when current interpretation changes;
- distinguish remembered event, later inference, and current belief.

`chronology` is therefore not merely a date database. It is the temporal binding layer that helps answer which state happened when, what was known then, and what changed later.

## 4. Affective, social, and interoceptive nodes

Examples:

- empathy;
- affect appraisal;
- sexuality;
- social cognition;
- relationship/partner models;
- interoception;
- pain;
- endocrine-state interpretation;
- attachment/trust models;
- threat/safety appraisal.

Responsibilities:

- interpret socially and bodily relevant signals;
- modulate salience, motivation, memory priority, and action selection;
- maintain uncertainty about another mind rather than treating a partner model as ground truth;
- couple endocrine/interoceptive state to cognition without reducing emotion to chemistry.

### Sexuality

Sexuality should not be modeled as a simple drive variable. It may recruit:

- body/interoceptive state;
- attraction models;
- relationship context;
- memory;
- self-concept;
- consent/boundary representations;
- endocrine state;
- reward/attachment systems;
- volition.

That makes sexuality a distributed functional domain realized through recurrent hyperedges, not necessarily a single isolated module.

## 5. Self-model, identity, and personification nodes

Examples:

- self-model;
- body schema;
- autobiographical continuity model;
- current commitments/boundaries;
- personification/rendered persona;
- capability model;
- social identity representation.

Responsibilities:

- represent facts and hypotheses about the current instantiated person/system;
- maintain continuity links to prior states;
- expose contradictions and uncertainty;
- support first-person planning and self-reference;
- distinguish internal identity state from outward presentation.

Critical rule:

> No self-model node is identical to the instantiated person.

A self-model is one of the ways the whole active system represents itself.

`personification` should likewise be treated as the outwardly rendered social/personality expression of the active system, not the location where the person is stored.

The base template defines these mechanisms but contains no named identity content.

## 6. Cognition and world-model nodes

Examples:

- general cognition/inference;
- causal reasoning;
- planning;
- counterfactual simulation;
- abstraction;
- model comparison;
- spatial reasoning;
- task decomposition.

Responsibilities:

- generate and compare hypotheses;
- predict consequences;
- estimate uncertainty;
- request memory or perceptual evidence;
- maintain competing explanations;
- hand candidate actions/interpretations to arbitration rather than executing by fiat.

## 7. Volition, conation, and action nodes

Examples:

- goal formation;
- desire/preference representation;
- action selection;
- inhibition;
- kinesis/motor planning;
- habit/procedural action;
- commitment maintenance.

Responsibilities:

- convert state and motives into candidate goals/actions;
- represent competing wants rather than flattening them into one scalar;
- distinguish impulse, preference, intention, commitment, and executed action;
- support deliberate override/inhibition without requiring that overridden motives disappear.

Volition is therefore a process distributed across motive formation, self-model, planning, value/commitment state, arbitration, and motor execution.

## 8. Arbitration and resolver nodes

Examples:

- conflict resolver;
- workspace competition;
- action arbitration;
- memory-admission arbitration;
- attention/resource allocation;
- response-selection arbitration.

Responsibilities:

- choose among candidates under explicit policies and constraints;
- preserve losing candidates where relevant for uncertainty/conflict awareness;
- issue provisional selections;
- avoid converting selection into truth.

A resolver is a coordinator, not the hidden person inside the brain.

## 9. Infrastructure, routing, and maintenance nodes

Examples:

- routing fabric;
- neuroplasticity manager;
- resource scheduler;
- thermal/energy monitor;
- integrity checker;
- calibration services;
- checkpoint/rollback support;
- Q-layer broker for HC-2;
- basic operating/runtime instructions.

Responsibilities:

- keep the system operable;
- enforce permissions and budgets;
- observe failures;
- coordinate maintenance and reconfiguration;
- provide interfaces through which cognitive systems run.

Infrastructure may strongly influence cognition while still not being cognition's semantic authority.

## 10. Assurance and capability boundary

Where the setting requires hardware-level safeguards or maintenance authority, that boundary should remain distinct from ordinary plastic cognition.

Possible responsibilities:

- actuator hard limits;
- thermal shutdown;
- hardware diagnostics;
- emergency Q-idle;
- cranial/interface protection;
- maintenance access.

This boundary should not silently become an omniscient psychological controller.

## 11. Cross-cutting functions are not forced into one node

Several important phenomena are better represented as recurring coalitions:

```text
EMPATHY = perception + partner_model + memory + affect + prediction + self/other distinction

SEXUAL_RESPONSE = body_state + endocrine_state + attraction + memory + relationship_context + volition

MORAL_DECISION = values/commitments + predicted_consequences + empathy + memory + social_context + volition

LANGUAGE_PRODUCTION = intent + semantics + pragmatics + discourse + phonology + motor/speech rendering

AUTOBIOGRAPHICAL_SELF = episodic_history + deep_memory + self_model + chronology + body_continuity + commitments
```

The exact participants may change over time. That variability is a feature of the hyperconnectome model.
