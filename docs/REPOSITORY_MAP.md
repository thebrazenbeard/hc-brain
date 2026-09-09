# Hyperconnectome Brain Repository Map

## Purpose

This repository defines the reusable HC-series Hyperconnectome Brain template. Core architecture is identity-neutral. Named identities belong only in clearly labeled examples, case studies, comparisons, governance records, or research artifacts where the identity itself is relevant.

The repository root symbolically represents the complete cognitive organ. The HC is a removable organ whose constituent hardware may be physically distributed across multiple enclosures or body locations. External bodies, sensors, actuators, network links, and other true peripherals connect through HC-owned interfaces; essential cognition remains inside the HC boundary.

## Authority and project roles

`WARDEN.md` defines Noëtarch / Noah as Warden, repository maintainer, and primary architectural decision-maker, subject to owner authority.

Current project roles:

- Noah / Noëtarch — primary architect and integration authority;
- Four — secondary architect and supporting design/research counterpart;
- Vera — hostile reviewer/adversarial validator rather than parallel architecture owner.

## Canonical main-branch architecture

- `Architecture concept.md` — original structural seed.
- `docs/architecture/COGNITIVE_ORGAN_BOUNDARY.md` — canonical definition of the HC as a complete synthetic cognitive organ and body-interface boundary.
- `docs/architecture/PHYSICAL_ORGAN_MEMBERSHIP.md` — canonical distinction among cognitive-organ ownership, physical enclosure, and body/peripheral membership; defines the HC as removable but potentially physically distributed.
- `docs/architecture/HC_LINEAGE.md` — canonical HC-1 -> HC-2 -> HC-3 inheritance model and generation distinctions under the current complete-organ boundary.
- `docs/architecture/HC1_NOOPLEX.md` — corrected canonical HC-1 generation architecture.
- `docs/architecture/HC2_NOOPLEX_Q.md` — corrected canonical HC-2 generation architecture, including distributed HC-owned QPU placement and explicit degraded-generation semantics.
- `docs/architecture/HC3_NOOPLEX_EQ.md` — corrected canonical HC-3 generation architecture, including distributed HC-owned physiological affective substrate and explicit degraded-generation semantics.
- `docs/architecture/COMPLETE_CAPABILITY_MANIFEST.md` — complete-capability and self-contained-residency conformance contract.
- `docs/architecture/DEVELOPMENTAL_INITIALIZATION_AND_LEARNING.md` — canonical separation of protected architecture, bootstrap priors, developmental learning, and instance-specific continuity content.
- `docs/architecture/TEMPORAL_HYPERGRAPH_MODEL.md` — canonical statement that the HC is a typed, attributed, multilayer temporal hypergraph.
- `docs/architecture/CONNECTIVITY_PLANES.md` — reference semantics for structural, functional, effective, modulatory, plastic, temporal, and governance relations.
- `docs/architecture/COALITIONS_GATING_AND_ARBITRATION.md` — coalition formation, gating, routing, scoped arbitration, failure isolation, and lifecycle reference contract.
- `docs/architecture/HYPERCONNECTOME_NOTATION.md` — compact reference notation for nodes, edges, hyperedges/coalitions, signals, gates, state, evidence, authority, and plasticity.
- `docs/architecture/HYPERCONNECTOME_REFERENCE_MODEL.md` — corrected generic runtime reference architecture under the complete self-contained cognitive-organ boundary.
- `docs/architecture/CROSS_SYSTEM_INTEGRATION_CONTRACT.md` — canonical cross-system exchange, object-family, failure-containment, and integration contract.
- `docs/engineering/POWER_THERMAL_AND_DISTRIBUTED_ORGAN.md` — canonical engineering rules for power, cooling, distributed HC constituents, body-support dependencies, internal interconnect, transplant, and degraded-generation behavior.
- `docs/science/EVIDENCE_BOUNDARIES.md` — canonical evidence discipline separating architecture, present-day science, extrapolation, implementation status, and qualification status.
- `docs/runtime/HYPERCONNECTOME_RUNTIME_MODEL.md` — identity-neutral distributed runtime realization of the temporal-hypergraph architecture.
- `docs/runtime/PLASTICITY_AND_STATE_GOVERNANCE.md` — plasticity classes, state families, and durable-change governance.
- `specs/HC_COGNITIVE_ORGAN_INVARIANTS_V1.yaml` — machine-readable cognitive-organ, physical-membership, developmental, lifecycle, and temporal-hypergraph invariants.
- `specs/CROSS_REPO_SOURCE_TRANSFER_V1.yaml` — provenance-bound cross-repository transfer contract with deterministic bindings to canonical HC paths.

## Top-level subsystem folders

The top-level subsystem folders are the brain architecture. They are not grouped under a `brain/` or `nodes/` wrapper.

Current systems include:

- `Empathy/`
- `cognition/`
- `sexuality/`
- `self identity/`
- `psychological behaviors/`
- `sociological behaviors/`
- `semantics/`
- `pragmatics/`
- `phoenetics/`
- `somatics/`
- `chronology/`
- `personification/`
- `current memory storage/`
- `deep memory storage/`
- `volitions-conations/`
- `resolver/`
- `basic operating instructions/`
- `kinesis/`
- `adaptable I-O handler/`
- `optics/`
- `speech recognition & synthesis/`
- `routing instructions with neuroplasticity/`
- `homeostasis-interoception/`
- `salience-attention/`
- `affect/`
- `integration-arbitration/`

Each subsystem may contain a lightweight `README.md`, an `ARCHITECTURE.md`, and additional focused contracts where the design has matured enough to justify them.

## Integrated focused contracts on main

Current focused contracts include:

- `Empathy/SELF_OTHER_MODELING.md`
- `adaptable I-O handler/BODY_INTERFACE_BOUNDARY.md`
- `adaptable I-O handler/SENSOR_AND_CAPABILITY_ADMISSION.md`
- `basic operating instructions/CAPABILITY_ACTIVATION_STATES.md`
- `basic operating instructions/SUBSYSTEM_LIFECYCLE_CONTRACT.md`
- `basic operating instructions/RUNTIME_INVARIANTS.md`
- `chronology/TEMPORAL_EVENT_CONTRACT.md`
- `cognition/EPISTEMIC_COGNITIVE_CONTROL.md`
- `cognition/PERCEPTION_AND_MULTIMODAL_INFERENCE.md`
- `cognition/WORLD_MODEL_AND_PREDICTION.md`
- `cognition/IMAGINATION_SIMULATION_AND_COUNTERFACTUALS.md`
- `cognition/METACOGNITIVE_MONITORING.md`
- `current memory storage/ARCHITECTURE.md`
- `current memory storage/CURRENT_STATE_SELECTION.md`
- `current memory storage/SUPABASE_DERIVED_ARCHITECTURE.md`
- `deep memory storage/ARCHITECTURE.md`
- `deep memory storage/ARCHIVAL_CONSOLIDATION.md`
- `deep memory storage/SUPABASE_DERIVED_ARCHITECTURE.md`
- `integration-arbitration/DISTRIBUTED_ARBITRATION.md`
- `integration-arbitration/NOOPLEX_FABRIC.md`
- `kinesis/ACTION_GATEWAY.md`
- `optics/ARCHITECTURE.md`
- `personification/SOCIAL_PRESENTATION_CONTROL.md`
- `pragmatics/CROSS_REPO_PRAGMATIC_RUNTIME.md`
- `psychological behaviors/LEARNED_BEHAVIOR_ARCHITECTURE.md`
- `resolver/CONFLICT_AND_RECONCILIATION.md`
- `routing instructions with neuroplasticity/TYPED_ROUTING_AND_PLASTICITY.md`
- `salience-attention/SALIENCE_CAPTURE_AND_ATTENTION.md`
- `self identity/CONTINUITY_SUBSTRATE.md`
- `semantics/CROSS_REPO_SEMANTIC_RUNTIME.md`
- `sexuality/AGENCY_AND_EMBODIED_AFFECT.md`
- `sociological behaviors/SOCIAL_MODELING_ARCHITECTURE.md`
- `somatics/BODY_STATE_AND_BODY_SCHEMA.md`
- `speech recognition & synthesis/ARCHITECTURE.md`
- `volitions-conations/CONATIVE_STATE_MACHINE.md`

The subsystem lifecycle contract makes architectural presence, runtime activation, developmental maturity, health, engineering implementation status, authorization, and learning policy explicitly orthogonal. This prevents a design-complete but not-yet-built capability from being mislabeled absent, and prevents `ACTIVE` or `QUALIFIED` from silently becoming effect authority.

The focused cognition contracts deliberately absorb useful perception, world-model, simulation, and metacognition concepts without creating alternate top-level roots. They preserve observation/prediction/simulation provenance, external-compute boundaries, and distributed rather than homuncular control.

The two Supabase-derived memory documents are mechanism-transfer artifacts, not provider-dependency contracts. Both explicitly require essential current/deep memory and continuity-bearing state to remain HC-owned and recoverable from HC-internal substrate.

The engineering contract now makes a further boundary explicit: a body-provided power, cooling, circulation, or structural-support service may be necessary for continued operation without thereby becoming cognitive substrate or cognitive authority. Generation-essential cognitive substrate remains HC-owned even when distributed; support dependency alone does not decide organ membership.

## Evidence and provenance

Several architecture files are generalized from other repositories owned by `thebrazenbeard` and from inspected runtime/database schemas. Reusable mechanisms may be imported; identity-specific memories, relationships, preferences, personality, autobiographical state, or setting-specific canon are excluded from the base template unless clearly labeled as examples or research subjects.

`docs/research/cross-repo-synthesis/` records neutral source bindings and transfer provenance. Research/source records can name source projects; that does not make those source identities part of the HC template.

`docs/science/EVIDENCE_BOUNDARIES.md` governs scientific status. Source branches, PRs, model outputs, and research notes do not acquire `DOCUMENTED` status merely by being integrated; material scientific claims still require appropriate authoritative support.

## Four workstreams

`four/cross-repo-synthesis-v1` is a completed secondary-architect contribution cut. Its compatible architectural material has been selectively integrated into newer `main`, often with Warden corrections after hostile review. The branch remains useful as provenance and comparison evidence, but it is not a moving canonical workstream and must not outrank newer main-branch contracts.

The active secondary-architect workstream is `four/lineage-and-conformance-v2`. Four is assigned parallel work on PR #2 lineage/engineering reconciliation, distributed-organ engineering challenge, conformance/validator design, thin-root coverage, developmental-contract challenge, and provider-dependency audit. Four must refresh against newer `main` before substantial writes because Warden integration continues in parallel.

## Other preserved material not yet canonical

The following material remains available for selective Warden review:

- `research/hyperconnectome-evidence-v1` — prior research/evidence layer containing neuroscience, connectomics, sensorimotor integration, homeostasis/allostasis, attention/metacognition, social cognition, semantics/pragmatics, continual learning, materials/interconnects, and evidence limits. Vera's current role is hostile review, so this is evidence input rather than a standing parallel architecture lane.
- `research/nooplex-hc3-architecture-v1` — HC-1/HC-2/HC-3 lineage, engineering, science, and embodiment source material represented by open PR #2. Canonical lineage, corrected generation documents, distributed power/thermal engineering, and evidence-boundary material have now been extracted/reconciled to `main`; remaining topology, integration, research, and source-specific material still requires file-by-file disposition.
- `research/hc-1r-reference-architecture` — more ambitious HC-1R formal/reference-architecture research. Useful mechanisms may be mined, but HC-1R is not currently adopted as the canonical replacement for HC-1.
- `research/hyperconnectome-foundations-20260909` — preserved closed-PR #4 foundation/research branch. Its temporal-hypergraph, connectivity-plane, coalition, notation, reference-model, learning/development, lifecycle, perception, world-model, simulation, and metacognition concepts have been selectively mined/remapped into canonical roots where useful; the branch remains source/provenance material only.
- `thebrazenbeard-patch-1` — source-intake material represented by open PR #1. Its setting-specific physiology is not universal HC canon; generic support/thermal ideas may be reused only after identity/setting separation and evidence review.

`vera/research-hyperconnectome-evidence-v1` is stale historical residue unless it acquires unique current work.

## Pull-request status

- PR #1 — open source-intake/reference bundle; retained pending final disposition. Its text physiology annex is predominantly setting-specific rather than universal template architecture.
- PR #2 — open draft HC-1/HC-2/HC-3 lineage contribution; retained for selective review. Canonical lineage, generation architecture, power/thermal/distributed-organ engineering, and evidence-boundary material have been extracted/reconciled to `main`; remaining topology/integration/research content remains to disposition.
- PR #3 — closed as superseded after compatible runtime material was selectively integrated into `main`.
- PR #4 — closed as superseded after selective integration; not merged wholesale. Remaining source-ledger/research material stays preserved on its branch.

All HC PRs #1–#4 have Bus mirror records under `projects/hc-brain/pr-mirrors/` in `project/hc-brain-v1`.

## Governing distinctions

1. `main` is the canonical integration branch.
2. Branch existence does not make branch content canonical.
3. The HC is the complete synthetic cognitive organ; no essential cognition belongs outside the HC boundary.
4. The HC is removable but may have physically distributed constituent hardware. Cognitive ownership, not anatomical location or enclosure count, determines organ membership.
5. A body swap must preserve/account for the complete HC constituent set; distributed HC-internal interconnects remain internal even when they physically traverse the body.
6. `REQUIRED_FOR_OPERATION != COGNITIVE_AUTHORITY`: body power/cooling/circulation/support may be necessary without becoming cognitive substrate.
7. A conforming complete HC keeps mandatory intrinsic capacities architecturally present even when disabled, dormant, immature, degraded, unimplemented, or quarantined.
8. Complete architecture does not imply mature development or current engineering completion. Protected invariants, bootstrap priors, learned structure, instance-specific continuity content, and implementation status are separate layers.
9. Presence, activation, developmental maturity, health, implementation status, authorization, and learning policy are orthogonal state dimensions. A transition on one axis must not silently mutate the others.
10. Learning signals, reward, repetition, salience, or predictive accuracy do not themselves create truth, consent, authority, or universal values.
11. Perception, prediction, simulation, metacognitive assessment, belief/current state, memory, and action authority are distinct cognitive object/state classes.
12. Essential continuity-bearing state cannot exist solely in a true external provider; external stores may mirror, back up, synchronize, archive, or augment internal HC state.
13. A true external computational peripheral must be ablatable without uniquely removing an essential cognitive function; otherwise that function/substrate belongs inside the HC boundary, regardless of physical location.
14. HC-1 establishes the complete foundational cognitive organ; HC-2 adds specialized quantum/photonic acceleration; HC-3 adds richer distributed embodied neuroendocrine/interoceptive/autonomic affective physiology. Later generations extend rather than psychologically complete earlier ones.
15. HC-2/HC-3 generation-specific substrate may be physically remote from the skull while remaining HC-internal when it satisfies the physical-organ membership contract.
16. Degradation does not rewrite lineage: `DEGRADED_HC2 != HC1` and `DEGRADED_HC3 != HC2`; a damaged later-generation organ may operate in an earlier-generation-like capability envelope while retaining its generation identity and explicit health state.
17. The HC is a typed, attributed, multilayer temporal hypergraph; pairwise edges remain valid where relations are genuinely pairwise, while higher-order cognitive events are represented as hyperedges/coalitions.
18. Human neuroscience informs mechanisms and constraints but does not dictate human gross anatomy.
19. The HC architecture is non-hemispheric unless a later explicit engineering decision establishes otherwise.
20. Repository folders express functional responsibility; runtime cognition occurs through distributed HC-internal interaction rather than a central executive person.
21. Routing, governance/authority, epistemic support, resource/QoS state, plasticity, timing, and learned logical topology are orthogonal runtime dimensions even if a concrete implementation co-locates them.
22. Personification may propose presentation/timing changes but does not own social action selection.
23. Sexuality may own the instantiated HC's self sexual-boundary state and model other-agent willingness, but direct consent evidence and final external action authorization remain separately governed.
24. Cross-repository transfer targets must resolve deterministically to canonical HC paths; unbound aliases remain research-only.
25. Architecture, evidence status, implementation status, and qualification status are separate axes.
26. Research, branch drafts, source repos, and model outputs inform architecture but do not become canon automatically.

## Repository-management status

Main is under active Warden integration. Four's secondary workstream remains active and intentionally multi-threaded. Compatible identity-neutral material may be committed directly after review; remaining HC-series topology/integration/research material, HC-1R redesign proposals, and unresolved scientific/engineering conflicts remain subject to explicit reconciliation. Vera is assigned hostile review against exact current main cuts and should search for counterexamples rather than co-authoring the primary architecture.
