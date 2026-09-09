# Hyperconnectome Brain Repository Map

## Purpose

This repository defines the reusable HC-series Hyperconnectome Brain template. Core architecture is identity-neutral. Named identities belong only in clearly labeled examples, case studies, comparisons, governance records, or research artifacts where the identity itself is relevant.

The repository root symbolically represents the complete cognitive organ. External bodies, sensors, actuators, network links, and other peripherals connect through HC-owned interfaces; essential cognition remains inside the HC boundary.

## Authority and project roles

`WARDEN.md` defines Noëtarch / Noah as Warden, repository maintainer, and primary architectural decision-maker, subject to owner authority.

Current project roles:

- Noah / Noëtarch — primary architect and integration authority;
- Four — secondary architect and supporting design/research counterpart;
- Vera — hostile reviewer/adversarial validator rather than parallel architecture owner.

## Canonical main-branch architecture

- `Architecture concept.md` — original structural seed.
- `docs/architecture/COGNITIVE_ORGAN_BOUNDARY.md` — canonical definition of the HC as a complete synthetic cognitive organ and body-interface boundary.
- `docs/architecture/TEMPORAL_HYPERGRAPH_MODEL.md` — canonical statement that the HC is a typed, attributed, multilayer temporal hypergraph.
- `docs/architecture/CONNECTIVITY_PLANES.md` — reference semantics for structural, functional, effective, modulatory, plastic, temporal, and governance relations.
- `docs/architecture/COALITIONS_GATING_AND_ARBITRATION.md` — coalition formation, gating, routing, scoped arbitration, failure isolation, and lifecycle reference contract.
- `docs/architecture/HYPERCONNECTOME_NOTATION.md` — compact reference notation for nodes, edges, hyperedges/coalitions, signals, gates, state, evidence, authority, and plasticity.
- `docs/architecture/HYPERCONNECTOME_REFERENCE_MODEL.md` — corrected generic runtime reference architecture under the complete self-contained cognitive-organ boundary.
- `docs/architecture/CROSS_SYSTEM_INTEGRATION_CONTRACT.md` — canonical cross-system exchange, object-family, failure-containment, and integration contract.
- `docs/runtime/HYPERCONNECTOME_RUNTIME_MODEL.md` — identity-neutral distributed runtime realization of the temporal-hypergraph architecture.
- `docs/runtime/PLASTICITY_AND_STATE_GOVERNANCE.md` — plasticity classes, state families, and durable-change governance.
- `specs/HC_COGNITIVE_ORGAN_INVARIANTS_V1.yaml` — machine-readable cognitive-organ and temporal-hypergraph invariants.
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
- `basic operating instructions/RUNTIME_INVARIANTS.md`
- `chronology/TEMPORAL_EVENT_CONTRACT.md`
- `cognition/EPISTEMIC_COGNITIVE_CONTROL.md`
- `current memory storage/ARCHITECTURE.md`
- `current memory storage/CURRENT_STATE_SELECTION.md`
- `deep memory storage/ARCHITECTURE.md`
- `deep memory storage/ARCHIVAL_CONSOLIDATION.md`
- `integration-arbitration/DISTRIBUTED_ARBITRATION.md`
- `integration-arbitration/NOOPLEX_FABRIC.md`
- `kinesis/ACTION_GATEWAY.md`
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
- `volitions-conations/CONATIVE_STATE_MACHINE.md`

## Evidence and provenance

Several architecture files are generalized from other repositories owned by `thebrazenbeard` and from inspected runtime/database schemas. Reusable mechanisms may be imported; identity-specific memories, relationships, preferences, personality, autobiographical state, or setting-specific canon are excluded from the base template unless clearly labeled as examples or research subjects.

`docs/research/cross-repo-synthesis/` records neutral source bindings and transfer provenance. Research/source records can name source projects; that does not make those source identities part of the HC template.

## Completed Four synthesis pass

`four/cross-repo-synthesis-v1` is a completed secondary-architect contribution cut. Its compatible architectural material has been selectively integrated into newer `main`, often with Warden corrections after hostile review. The branch remains useful as provenance and comparison evidence, but it is not a moving canonical workstream and must not outrank newer main-branch contracts.

The completed pass also contains detailed source/provenance research that may be mined into `docs/research/` without promoting its process-plan artifacts or stale alternate wording into canon.

## Other preserved material not yet canonical

The following material remains available for selective Warden review:

- `research/hyperconnectome-evidence-v1` — prior research/evidence layer containing neuroscience, connectomics, sensorimotor integration, homeostasis/allostasis, attention/metacognition, social cognition, semantics/pragmatics, continual learning, materials/interconnects, and evidence limits. Vera's current role is hostile review, so this is evidence input rather than a standing parallel architecture lane.
- `research/nooplex-hc3-architecture-v1` — HC-1/HC-2/HC-3 lineage, engineering, science, and embodiment work under selective review; represented by open PR #2.
- `research/hc-1r-reference-architecture` — more ambitious HC-1R formal/reference-architecture research. Useful mechanisms may be mined, but HC-1R is not currently adopted as the canonical replacement for HC-1.
- `research/hyperconnectome-foundations-20260909` — preserved closed-PR #4 foundation/research branch. Its temporal-hypergraph, connectivity-plane, coalition, notation, and reference-model material has been selectively integrated/corrected on `main`; the branch remains source/provenance material only.
- `thebrazenbeard-patch-1` — source-intake material represented by open PR #1.

`vera/research-hyperconnectome-evidence-v1` is stale historical residue unless it acquires unique current work.

## Pull-request status

- PR #1 — open source-intake/reference bundle; retained pending final disposition.
- PR #2 — open draft HC-1/HC-2/HC-3 lineage contribution; retained for selective review.
- PR #3 — closed as superseded after compatible runtime material was selectively integrated into `main`.
- PR #4 — closed as superseded after selective integration; not merged wholesale. Remaining source-ledger/research material stays preserved on its branch.

All HC PRs #1–#4 now have Bus mirror records under `projects/hc-brain/pr-mirrors/` in `project/hc-brain-v1`.

## Governing distinctions

1. `main` is the canonical integration branch.
2. Branch existence does not make branch content canonical.
3. The HC is the complete synthetic cognitive organ; no essential cognition belongs outside the HC boundary.
4. A conforming complete HC keeps mandatory intrinsic capacities architecturally present even when disabled, dormant, immature, degraded, or unimplemented.
5. Essential continuity-bearing state cannot exist solely in an external provider; external stores may mirror, back up, synchronize, archive, or augment internal HC state.
6. An external computational peripheral must be ablatable without uniquely removing an essential cognitive function; otherwise that function/substrate belongs inside the HC boundary.
7. The HC is a typed, attributed, multilayer temporal hypergraph; pairwise edges remain valid where relations are genuinely pairwise, while higher-order cognitive events are represented as hyperedges/coalitions.
8. Human neuroscience informs mechanisms and constraints but does not dictate human gross anatomy.
9. The HC architecture is non-hemispheric unless a later explicit engineering decision establishes otherwise.
10. Repository folders express functional responsibility; runtime cognition occurs through distributed HC-internal interaction rather than a central executive person.
11. Capability presence, activation, development, health, and authorization are distinct axes.
12. Routing, governance/authority, epistemic support, resource/QoS state, plasticity, timing, and learned logical topology are orthogonal runtime dimensions even if a concrete implementation co-locates them.
13. Personification may propose presentation/timing changes but does not own social action selection.
14. Sexuality may own the instantiated HC's self sexual-boundary state and model other-agent willingness, but direct consent evidence and final external action authorization remain separately governed.
15. Cross-repository transfer targets must resolve deterministically to canonical HC paths; unbound aliases remain research-only.
16. Research, branch drafts, source repos, and model outputs inform architecture but do not become canon automatically.

## Repository-management status

Main is under active Warden integration. Four's completed synthesis cut and closed PR #4 have now been dispositioned rather than awaited. Compatible identity-neutral material may be committed directly after review; HC-series lineage changes, HC-1R redesign proposals, and unresolved scientific/engineering conflicts remain isolated until explicitly reconciled. Vera is assigned hostile review against exact current main cuts and should search for counterexamples rather than co-authoring the primary architecture.