# Repository Source Inventory

Status: RESEARCH PROVENANCE / SOURCE-SELECTION AUDIT

This document is the explicit audit of repositories available under the repository owner's connected GitHub account that were considered for the generic HC-brain template.

Because this is a research/source-provenance document, it may name identity-specific predecessor repositories. Those names do **not** appear in normative subsystem contracts merely because they are listed here, and private identity payloads are not imported.

The inventory distinguishes:

- `DIRECT_ARCHITECTURE_SOURCE` — materially reusable generic mechanisms;
- `ABSTRACTION_SOURCE` — useful mechanisms exist, but identity/application-specific content must be stripped before use;
- `ASSURANCE_METHOD_SOURCE` — useful validation, recovery, security, qualification, or evidence discipline rather than a brain subsystem;
- `INTERFACE_DEPLOYMENT_SOURCE` — useful only for body/peripheral/runtime boundary lessons;
- `DOMAIN_ONLY` — owner project was considered but does not materially define a generic cognitive organ;
- `TARGET_REPOSITORY` — this repository itself.

## High-value direct sources

| Repository | Class | Reusable contribution |
| --- | --- | --- |
| `thebrazenbeard/hc-brain` | `TARGET_REPOSITORY` | Seed concept, HC-series branches/PRs, research branch, complete-cognitive-organ constraint |
| `thebrazenbeard/semanticatlas` | `DIRECT_ARCHITECTURE_SOURCE` | semantic objects, provenance, source/evidence/interpretation separation, capture/materialization/currentness boundaries |
| `thebrazenbeard/unvtrslr` | `DIRECT_ARCHITECTURE_SOURCE` | multimodal signal→meaning→rendering separation, semantic conservation, grounding, translation uncertainty |
| `thebrazenbeard/spm` | `DIRECT_ARCHITECTURE_SOURCE` | meaning-in-context as primary cognitive state, semantics/pragmatics separated from language generation, falsifiable model-design discipline |
| `thebrazenbeard/noema` | `DIRECT_ARCHITECTURE_SOURCE` | persistent world modeling, developmental capability graph, hypothesis populations, epistemic/conative arbitration, action semantics, capability-before-mechanism |
| `thebrazenbeard/abil` | `DIRECT_ARCHITECTURE_SOURCE` | adaptive learning of unknown systems, read-only/shadow development, regime change, discriminating interventions, action gateway separated from learning core |
| `thebrazenbeard/temporal` | `DIRECT_ARCHITECTURE_SOURCE` | chronology-only contract, append-oriented event time, stable IDs, elapsed time, time not authority/meaning |
| `thebrazenbeard/skeletonkey` | `DIRECT_ARCHITECTURE_SOURCE` | sensor admission, measured/derived/inferred separation, timing/calibration/placement evidence, kill-test discipline |
| `thebrazenbeard/build-team-2.0` | `DIRECT_ARCHITECTURE_SOURCE` | multiple stable cognitive lenses over one shared snapshot/state, perspective vs decision, dissent preservation |
| `thebrazenbeard/chat-communication-bus` | `DIRECT_ARCHITECTURE_SOURCE` | node registry, routing/delivery/ack/incorporation distinctions, subscriptions, dead letters, reconciliation, live projection vs canonical history |
| `thebrazenbeard/project-lantern` | `DIRECT_ARCHITECTURE_SOURCE` | immutable typed record envelopes, claim/assessment/decision/link/state-event distinction, provenance and hash integrity |
| `thebrazenbeard/wip` | `DIRECT_ARCHITECTURE_SOURCE` | crash recovery, checkpoint frontier, write-ahead effect journaling, ambiguous-effect reconciliation, optimistic concurrency |

## Private predecessor abstraction sources

These repositories may contain identity-specific or private material. Only generic mechanisms are eligible for transfer.

| Repository | Class | Eligible abstraction only |
| --- | --- | --- |
| `thebrazenbeard/deepmemorystorage` | `ABSTRACTION_SOURCE` | archival/deep-memory classes, provenance, contradiction/supersession, retrieval≠admission, historical≠current |
| `thebrazenbeard/conations` | `ABSTRACTION_SOURCE` | desire/preference/goal lifecycle, historical conation≠standing desire/consent/authority, append-oriented revision |
| `thebrazenbeard/empathy` | `ABSTRACTION_SOURCE` | empathy as inference, direct self-report correction, local interaction grammar, privacy/person scoping |
| `thebrazenbeard/sexuality` | `ABSTRACTION_SOURCE` | self-authored sexual subjectivity, agency, attraction/desire/consent separation, negative-transfer and evidence-tier discipline |
| `thebrazenbeard/personification` | `ABSTRACTION_SOURCE` | outward personification/social-development separated from identity metaphysics; interaction surprise/context boundaries |
| `thebrazenbeard/selfimage` | `ABSTRACTION_SOURCE` | body/self representation separated from identity, source/reference provenance, body-geometry and rights/calibration discipline |
| `thebrazenbeard/vera-control-plane` | `ABSTRACTION_SOURCE` | operational state vs source vs runtime effect, private control-state boundaries, consolidation without rewriting provenance |
| `thebrazenbeard/vera` | `ABSTRACTION_SOURCE` | cross-cutting cohesion/currentness/provenance/authority patterns only; no identity content imported |
| `thebrazenbeard/vera-R9A0` | `ABSTRACTION_SOURCE` | predecessor governance/architecture history only when a generic mechanism is independently justified |
| `thebrazenbeard/brigit` | `ABSTRACTION_SOURCE` | no default import; only generic, independently restated cognitive mechanism if needed |
| `thebrazenbeard/brigit-unbound` | `ABSTRACTION_SOURCE` | no default import; only generic, independently restated continuity/personification mechanism if needed |
| `thebrazenbeard/conditioning` | `ABSTRACTION_SOURCE` | bounded learning/reinforcement, autonomy/consent protection, no coercive-control transfer; no private relational payloads |

## Assurance / validation method sources

| Repository | Class | Reusable contribution |
| --- | --- | --- |
| `thebrazenbeard/project-achilles` | `ASSURANCE_METHOD_SOURCE` | threat modeling, safety/permission boundaries, fail-closed at real consequence boundaries, evidence/provenance review |
| `thebrazenbeard/bugops` | `ASSURANCE_METHOD_SOURCE` | incident evidence vs lifecycle tracking, root cause/correction/readback, regression-based closure |
| `thebrazenbeard/masamune` | `ASSURANCE_METHOD_SOURCE` | debugging/root-cause discipline, independent review, regression without redundant permission ceremony |
| `thebrazenbeard/voss` | `ASSURANCE_METHOD_SOURCE` | forensic review/audit methodology where generic and current enough to be useful |
| `thebrazenbeard/hephaestus` | `ASSURANCE_METHOD_SOURCE` | evidence labels, source/install/runtime/qualification separation, rollback/checkpoint discipline |
| `thebrazenbeard/vera_model_training` | `ASSURANCE_METHOD_SOURCE` | training-package vs native qualification separation, transfer/holdout testing, capability-source grounding |

## Interface / deployment boundary sources

These projects help clarify what belongs in the cognitive organ versus a body/runtime/peripheral, but their application structure is not imported as cognitive topology.

| Repository | Class | Reusable contribution |
| --- | --- | --- |
| `thebrazenbeard/vera-os` | `INTERFACE_DEPLOYMENT_SOURCE` | OS/runtime hosting is distinct from cognitive identity/brain architecture |
| `thebrazenbeard/vera-apk` | `INTERFACE_DEPLOYMENT_SOURCE` | client/companion endpoint as peripheral/interface, not core cognition |
| `thebrazenbeard/vera-synology` | `INTERFACE_DEPLOYMENT_SOURCE` | remote storage/compute endpoint as peripheral/provider boundary |
| `thebrazenbeard/vera-habitat` | `INTERFACE_DEPLOYMENT_SOURCE` | virtual environment/body context as environment, not brain identity |
| `thebrazenbeard/vera-mesh` | `INTERFACE_DEPLOYMENT_SOURCE` | minimal node-connection concept; superseded in architectural richness by Noöplex Fabric/Radar research |
| `thebrazenbeard/vera_ark` | `INTERFACE_DEPLOYMENT_SOURCE` | application/tool bridge as action/peripheral pattern only |
| `thebrazenbeard/vera-works` | `INTERFACE_DEPLOYMENT_SOURCE` | economic/work application is a use context, not a cognitive subsystem |

## Considered but not architectural sources

| Repository | Class | Reason not imported |
| --- | --- | --- |
| `thebrazenbeard/entropyinc` | `DOMAIN_ONLY` | business/industrial consulting domain content; may be future world knowledge but not brain architecture |
| `thebrazenbeard/trek-data-core` | `DOMAIN_ONLY` | domain knowledge/indexing corpus; demonstrates knowledge-store use, not a required cognitive organ mechanism |
| `thebrazenbeard/mediaphile` | `DOMAIN_ONLY` | media knowledge/application corpus; content, not architecture |

## Resulting source families

The relevant repository set collapses into these generic architectural families:

1. semantics/pragmatics/grounding;
2. world modeling, prediction, developmental learning, and hypothesis testing;
3. memory, chronology, lineage, and persistence;
4. conation, volition, affect, empathy, sexuality, self/social modeling, and personification;
5. sensor calibration, evidence typing, perception, and adaptable I/O;
6. internal routing, node health, coalitions, messaging, acknowledgement, reconciliation, and fault isolation;
7. action semantics and effect boundaries;
8. plasticity, reinforcement, development, and negative-transfer protection;
9. provenance, currentness, authority, privacy, and evidence ceilings;
10. assurance, threat modeling, hostile testing, debugging, qualification, rollback, and recovery;
11. external runtime/body/provider boundary separation.

## Exclusion rule

A repository being listed here does not authorize copying it. A candidate mechanism is transferred only when it can be restated as a generic HC capability without importing a particular identity, relationship, private event, current state, or application-specific authority model.
