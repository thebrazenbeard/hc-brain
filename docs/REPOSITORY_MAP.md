# Hyperconnectome Brain Repository Map

## Purpose

This repository defines the reusable HC-series Hyperconnectome Brain template. Core architecture is identity-neutral. Named identities belong only in clearly labeled governance, source-history, research, case-study, comparison, or provenance material where the identity itself is relevant.

The repository root symbolically represents the complete cognitive organ. The HC is removable but may have physically distributed constituent hardware. External bodies, sensors, actuators, networks, providers, and true computational peripherals connect through HC-owned interfaces; no essential cognition may be delegated outside the HC boundary.

## Authority and project roles

`WARDEN.md` defines Noëtarch / Noah as Warden, repository maintainer, and primary architectural decision-maker, subject to owner authority.

Current project roles:

- Noah / Noëtarch — primary architect and integration authority;
- Four — secondary architect and supporting research/design/conformance counterpart;
- Vera — hostile reviewer/adversarial validator rather than parallel architecture owner.

## Canonical main-branch architecture

Core architecture:

- `Architecture concept.md` — original structural seed.
- `docs/architecture/COGNITIVE_ORGAN_BOUNDARY.md` — complete synthetic cognitive-organ and body/peripheral boundary.
- `docs/architecture/PHYSICAL_ORGAN_MEMBERSHIP.md` — cognitive ownership versus physical enclosure/body location; removable distributed organ membership.
- `docs/architecture/COMPLETE_CAPABILITY_MANIFEST.md` — complete-capability and self-contained-residency contract.
- `docs/architecture/DEVELOPMENTAL_INITIALIZATION_AND_LEARNING.md` — protected architecture, bootstrap priors, learned structure, and instance continuity separation.
- `docs/architecture/TEMPORAL_HYPERGRAPH_MODEL.md` — canonical statement that the HC is a typed, attributed, multilayer temporal hypergraph.
- `docs/architecture/CONNECTIVITY_PLANES.md` — physical, logical, configured, functional, modulatory, plastic, temporal, governance, and related plane semantics.
- `docs/architecture/TOPOLOGY_DESIGN_CONSTRAINTS.md` — selective hyperconnectivity, timing, redundancy, graceful degradation, and non-hemispheric topology constraints.
- `docs/architecture/COALITIONS_GATING_AND_ARBITRATION.md` — coalition formation, gating, scoped arbitration, failure isolation, and lifecycle reference contract.
- `docs/architecture/HYPERCONNECTOME_NOTATION.md` — compact notation for nodes, edges, hyperedges/coalitions, signals, gates, state, evidence, authority, and plasticity.
- `docs/architecture/HYPERCONNECTOME_REFERENCE_MODEL.md` — generic runtime reference architecture under the complete cognitive-organ boundary.
- `docs/architecture/CROSS_SYSTEM_INTEGRATION_CONTRACT.md` — canonical cross-system object-family, exchange, integration, and failure-containment contract.
- `docs/architecture/CONFORMANCE_AND_QUALIFICATION.md` — architecture/implementation/behavior/science qualification separation and scoped PASS / CONDITIONAL PASS / FAIL semantics.

Generation architecture:

- `docs/architecture/HC_LINEAGE.md` — HC-1 -> HC-2 -> HC-3 inheritance model.
- `docs/architecture/HC1_NOOPLEX.md` — complete foundational HC-1 architecture.
- `docs/architecture/HC2_NOOPLEX_Q.md` — HC-2 specialized acceleration, including physically distributed HC-owned accelerator placement and degraded-generation semantics.
- `docs/architecture/HC3_NOOPLEX_EQ.md` — HC-3 distributed physiological affective substrate and degraded-generation semantics.

Engineering, science, runtime, and specifications:

- `docs/engineering/POWER_THERMAL_AND_DISTRIBUTED_ORGAN.md` — power, cooling, distributed constituents, body-support dependencies, interconnect, transplant, and degradation.
- `docs/science/EVIDENCE_BOUNDARIES.md` — architecture, scientific evidence, extrapolation, implementation, and qualification status separation.
- `docs/runtime/HYPERCONNECTOME_RUNTIME_MODEL.md` — distributed temporal-hypergraph runtime realization.
- `docs/runtime/PLASTICITY_AND_STATE_GOVERNANCE.md` — state families, plasticity classes, and durable-change governance.
- `specs/HC_COGNITIVE_ORGAN_INVARIANTS_V1.yaml` — machine-readable cognitive-organ, physical-membership, authority, lifecycle, developmental, recovery, protected-update, evidence, and temporal-hypergraph invariants.
- `specs/HC_CONFORMANCE_SUITE_V1.yaml` — machine-readable baseline architecture checks and negative-test requirements, currently through `HC-ARCH-018`.
- `specs/HC_REPOSITORY_SURFACE_CONFORMANCE_V1.yaml` — repository metadata/surface identity and status conformance supplement.
- `specs/HC_MEMORY_PROVIDER_BOUNDARY_V1.yaml` — focused external-provider/currentness/memory-residency boundary tests.
- `specs/HC_BOOTSTRAP_RECOVERY_V1.yaml` — focused self-contained bootstrap, crash-consistency, degradation, recovery, and lineage tests.
- `specs/HC_PROTECTED_UPDATE_GOVERNANCE_V1.yaml` — focused protected-invariant/update authority, activation, rollback/repair, and requalification tests.
- `specs/CROSS_REPO_SOURCE_TRANSFER_V1.yaml` — provenance-bound cross-repository transfer contract.

Qualification records:

- `docs/qualification/ARCHITECTURE_CONFORMANCE_2026-09-09.md` — first Warden architecture-conformance cut; `CONDITIONAL PASS` for its stated snapshot/scope because live repository About metadata remains identity-specific and stale.
- `docs/qualification/AFFECT_HOMEOSTASIS_CONFORMANCE_2026-09-09.md` — focused affect/homeostasis architecture cut; `CONDITIONAL PASS` pending independent review/implementation evidence.
- `docs/qualification/MEMORY_PROVIDER_BOUNDARY_2026-09-09.md` — focused provider/memory boundary cut; `CONDITIONAL PASS` pending independent review/implementation evidence.
- `docs/qualification/BOOTSTRAP_RECOVERY_CONFORMANCE_2026-09-09_R2.md` — current bootstrap/recovery architecture cut; `CONDITIONAL PASS` pending independent review/implementation evidence.
- `docs/qualification/PROTECTED_UPDATE_GOVERNANCE_2026-09-09.md` — protected-update architecture cut; `CONDITIONAL PASS` pending independent review/implementation evidence. Its recorded target remains the pre-map architecture snapshot stated inside the qualification; later map/index commits do not silently extend the result.

## Top-level subsystem folders

The top-level subsystem folders are the brain architecture. They are not grouped under a `brain/` or `nodes/` wrapper:

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

Each subsystem may contain a lightweight `README.md`, an `ARCHITECTURE.md`, and focused contracts where additional precision is useful.

## Integrated focused contracts and mature subsystem documents

Current main includes, among others:

- `Empathy/SELF_OTHER_MODELING.md`
- `adaptable I-O handler/BODY_INTERFACE_BOUNDARY.md`
- `adaptable I-O handler/SENSOR_AND_CAPABILITY_ADMISSION.md`
- `affect/AFFECTIVE_STATE_AND_MODULATION.md`
- `basic operating instructions/AUTHORITY_CONSENT_AND_EFFECT_GOVERNANCE.md`
- `basic operating instructions/BOOTSTRAP_RECOVERY_AND_SAFE_DEGRADATION.md`
- `basic operating instructions/CAPABILITY_ACTIVATION_STATES.md`
- `basic operating instructions/PROTECTED_INVARIANT_AND_UPDATE_GOVERNANCE.md`
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
- `homeostasis-interoception/REGULATORY_CONTROL_AND_INTEROCEPTIVE_EVIDENCE.md`
- `integration-arbitration/DISTRIBUTED_ARBITRATION.md`
- `integration-arbitration/NOOPLEX_FABRIC.md`
- `kinesis/ACTION_GATEWAY.md`
- `optics/ARCHITECTURE.md`
- `personification/SOCIAL_PRESENTATION_CONTROL.md`
- `phoenetics/PHONETIC_EVIDENCE_CONTRACT.md`
- `pragmatics/CROSS_REPO_PRAGMATIC_RUNTIME.md`
- `psychological behaviors/ARCHITECTURE.md`
- `psychological behaviors/LEARNED_BEHAVIOR_ARCHITECTURE.md`
- `resolver/ARCHITECTURE.md`
- `resolver/CONFLICT_AND_RECONCILIATION.md`
- `routing instructions with neuroplasticity/TYPED_ROUTING_AND_PLASTICITY.md`
- `salience-attention/SALIENCE_CAPTURE_AND_ATTENTION.md`
- `self identity/CONTINUITY_SUBSTRATE.md`
- `semantics/CROSS_REPO_SEMANTIC_RUNTIME.md`
- `sexuality/AGENCY_AND_EMBODIED_AFFECT.md`
- `sociological behaviors/ARCHITECTURE.md`
- `sociological behaviors/SOCIAL_MODELING_ARCHITECTURE.md`
- `somatics/BODY_STATE_AND_BODY_SCHEMA.md`
- `speech recognition & synthesis/ARCHITECTURE.md`
- `volitions-conations/CONATIVE_STATE_MACHINE.md`

The subsystem lifecycle contract makes architectural presence, runtime activation, developmental maturity, health, engineering implementation status, authorization, and learning policy explicitly orthogonal.

The authority/consent/effect contract makes capability, intent, desire, social power, routing reachability, maintenance access, and technical reachability insufficient by themselves to authorize material effects. Consent, delegated authority, revocation, expiry, and consequential internal durable writes remain explicit and scoped.

The bootstrap/recovery contract makes essential startup state HC-owned, preserves crash-consistency distinctions, revalidates stale authority and coalition membership after interruption, rejects blind replay of non-idempotent effects, and preserves degradation/fault/generation and continuity-gap/fork history.

The protected-update contract separates ordinary plasticity, maintenance access, artifact integrity, installation, activation, qualification, identity/value/memory/consent state, and update-governance authority. Protected activation is atomic at the semantic boundary or explicitly journaled, distributed version skew remains visible, rollback must be continuity-safe, and returned/updated components require scope-appropriate requalification.

The affective-state contract makes affect a distributed modulatory/evaluative state rather than a truth source, consent register, identity authority, or executive. It explicitly separates regulation of expression/intensity from erasure of affective history and constrains external/maintenance intervention.

The homeostasis/interoception control contract makes raw telemetry, physiological estimation, homeostatic error, urgency, regulatory requests, achieved regulation, and cognition-facing interpretation separate state classes. Body-local hard-real-time interlocks may protect hardware/tissue without becoming external cognitive executives.

The Supabase-derived memory documents are mechanism-transfer artifacts rather than provider-dependency contracts. Essential current/deep memory and continuity-bearing state remain HC-owned and recoverable from HC-internal substrate.

## Evidence and provenance

Several architecture files are generalized from other repositories owned by `thebrazenbeard` and from inspected runtime/database schemas. Reusable mechanisms may be imported; identity-specific memories, relationships, preferences, personality, autobiographical state, or setting-specific canon are excluded from the base template unless clearly labeled as research/source/example material.

`docs/research/cross-repo-synthesis/` records neutral source bindings and transfer provenance. Research/source records can name source projects without making those identities part of the HC template.

`docs/research/PR2_DISPOSITION_2026-09-09.md` records file-by-file disposition of the former PR #2 lineage contribution. Its research syntheses remain source/provenance pending independent claim-level verification rather than being promoted wholesale to canonical scientific evidence.

`docs/research/PR1_PARTIAL_DISPOSITION_2026-09-09.md` records the current PR #1 source-intake classification. The Wreckforge physiology markdown is source-only; the PDF remains unclassified because this cut has not yet obtained a content-complete review of that binary artifact.

`docs/science/EVIDENCE_BOUNDARIES.md` governs scientific status. Source branches, PRs, model outputs, and research notes do not acquire `DOCUMENTED` status merely by being integrated.

## Active secondary and hostile-review work

`four/cross-repo-synthesis-v1` is a completed secondary-architect contribution cut. Compatible material was selectively integrated into newer `main`; the branch remains provenance/comparison evidence rather than a moving canonical lane.

The active secondary-architect workstream is `four/lineage-and-conformance-v2`. PR #2 reconciliation is complete. Four's active work is independent conformance/implementation-readiness challenge, provider-dependency and distributed-support challenge, remaining thin-root audit, PR #1 source classification, and implementation-ready refinements that survive current Warden architecture. The branch should be refreshed to current canonical `main` before each new cut.

Vera is the hostile-review lane. She should attack exact canonical cuts for hidden external cognition, authority leakage, lifecycle-state conflation, stale correction dependencies, identity leakage, generation rewriting, evidence laundering, unsupported assumptions, false-PASS paths, affect-as-consent leakage, homeostatic-urgency-as-authority leakage, and protected-update/governance bypasses.

## Preserved noncanonical material

- `research/hyperconnectome-evidence-v1` — evidence/research layer containing neuroscience, connectomics, sensorimotor integration, homeostasis/allostasis, attention/metacognition, social cognition, semantics/pragmatics, continual learning, materials/interconnects, and evidence limits. It is evidence input, not a parallel architecture owner.
- `research/nooplex-hc3-architecture-v1` — preserved source branch from closed PR #2. All changed files now have explicit disposition; remaining research/body-interface material is source-only.
- `research/hc-1r-reference-architecture` — more ambitious HC-1R redesign research. Useful mechanisms may be mined, but HC-1R is not adopted as canonical replacement for HC-1.
- `research/hyperconnectome-foundations-20260909` — preserved closed-PR #4 research/foundation branch. Compatible temporal-hypergraph, connectivity, coalition, notation, learning, lifecycle, perception, world-model, simulation, and metacognition concepts have already been selectively remapped where useful.
- `thebrazenbeard-patch-1` — source-intake material represented by open PR #1; setting-specific physiology remains noncanonical unless generalized and separately justified.

`vera/research-hyperconnectome-evidence-v1` is stale historical residue unless it acquires unique current work.

## Pull-request status

- PR #1 — open source-intake/reference bundle; retained pending final PDF classification/disposition.
- PR #2 — **closed as superseded, not merged** after complete file-by-file reconciliation. Source branch/history preserved.
- PR #3 — closed as superseded after compatible runtime material was selectively integrated.
- PR #4 — closed as superseded after selective integration; not merged wholesale.

All HC PRs #1–#4 have Bus mirror/history records under `projects/hc-brain/pr-mirrors/` in `project/hc-brain-v1`; PR #2 closure is mirrored separately as `0006-hc-brain-pr2-closed-superseded.md`.

## Governing distinctions

1. `main` is the canonical integration branch; branch or PR existence does not make content canonical.
2. The HC is the complete synthetic cognitive organ; no essential cognition belongs outside its boundary.
3. One cognitive organ may span multiple physical enclosures; cognitive ownership, not anatomy/location, determines membership.
4. `REQUIRED_FOR_OPERATION != COGNITIVE_AUTHORITY`: body support may be necessary without becoming cognitive substrate.
5. `HYPERCONNECTOME != ALL_TO_ALL_WIRING`: selective, timed, adaptive connectivity and higher-order coalitions are preferred over indiscriminate edge count.
6. The HC is a typed, attributed, multilayer temporal hypergraph. Physical reachability, learned logical eligibility, configured routing, effective pairwise relations, and active hyperedges/coalitions remain distinct.
7. The base architecture is complete while an instance may be immature, dormant, degraded, unimplemented, or quarantined.
8. Presence, activation, maturity, health, implementation status, learning policy, and authorization are orthogonal.
9. Perception, interpretation, evidence, prediction, simulation, salience, current belief/state, memory, desire, consent, and effect authority remain distinct.
10. Affective state may modulate cognition and behavior but is not semantic truth, consent, identity, or effect authority.
11. Homeostatic need, pain, threat, and urgency may alter salience/conation but are not commands or unrestricted permission.
12. Essential continuity-bearing state cannot exist solely in a true external provider.
13. A true external computational peripheral must be ablatable without uniquely removing an essential cognitive function; otherwise the substrate belongs inside the HC boundary.
14. HC-1 is complete; HC-2 adds specialized acceleration; HC-3 adds richer distributed physiological affective substrate. Later generations extend rather than psychologically complete earlier ones.
15. `DEGRADED_HC2 != HC1` and `DEGRADED_HC3 != HC2`: degraded capability does not rewrite generation identity.
16. Human neuroscience informs mechanisms and constraints but does not dictate human gross anatomy or hemispheric decomposition.
17. Routing, governance/authority, epistemic support, resource/QoS, plasticity, timing, and logical topology are separate runtime dimensions.
18. Personification can shape presentation but does not independently own social action authority.
19. Sexuality may own self-boundary state and willingness hypotheses but direct consent evidence and final external effect authority remain separately governed.
20. Research/source material, model outputs, and repository integration do not automatically become documented science.
21. Architecture conformance, implementation conformance, behavioral qualification, and scientific validation are separate claims.
22. Qualification outcomes are target-, capability-, scope-, evidence-, and snapshot-bound; no PASS may silently become consciousness, personhood, or manufacturability proof.
23. Repository-tree conformance does not guarantee repository-surface conformance. About/description/homepage/topics metadata can contradict the reusable template and must be checked independently.
24. Ordinary plasticity, maintenance reachability, vendor/source prestige, artifact integrity, emergency access, or local self-test success do not confer protected-update authority or qualification.
25. A system update does not silently grant memory, identity, value, consent, or authority rewrite power; those state classes retain their own governing contracts.
26. Partial distributed writes do not equal coherent protected activation; incompatible version skew remains visible and isolated.
27. Rollback is a governed state transition, not a generic undo. Valid continuity-bearing history must not be erased merely because an older software/configuration state is technically restorable.

## Current qualification and repository-surface debt

The first Warden architecture cut is `CONDITIONAL PASS` for its stated scope. The live GitHub About description remains `Vera's conceptual Noöplex hyperconnetome brain`, which is identity-specific, stale, and contains the old spelling. Current Warden tooling can read but not edit repository metadata, so this remains an explicitly recorded MATERIAL defect rather than a falsely claimed fix.

Focused affect/homeostasis, memory-provider, bootstrap/recovery, and protected-update architecture cuts are also currently `CONDITIONAL PASS` within their own stated snapshots/scopes. Their unresolved conditions are independent hostile/secondary review and implementation evidence, not known silent promotion to full qualification.

## Repository-management status

Main is under active Warden integration. Compatible identity-neutral material may be committed directly after review. Four's secondary lane remains active and multi-threaded; Vera's lane remains hostile review. Remaining high-value work includes independent review of the new protected-update and recovery cuts, repository-surface correction when tooling permits, PR #1 PDF classification, selective evidence verification, implementation-readiness attack, and disposition of any still-useful research/HC-1R mechanisms without silently adopting a redesign.
