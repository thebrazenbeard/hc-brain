# Hyperconnectome Brain Repository Map

## Purpose

This repository defines the reusable HC-series Hyperconnectome Brain template. Core architecture is identity-neutral. Named identities belong only in clearly labeled examples, case studies, comparisons, or research artifacts where the identity itself is relevant.

The repository root symbolically represents the complete cognitive organ. External bodies, sensors, actuators, network links, and other peripherals connect through HC-owned interfaces; essential cognition remains inside the HC boundary.

## Authority

`WARDEN.md` defines Noëtarch / Noah as Warden, repository maintainer, primary architectural decision-maker, and project-facing voice of the HC brain, subject to owner authority.

## Canonical main-branch architecture

- `Architecture concept.md` — original structural seed.
- `docs/architecture/COGNITIVE_ORGAN_BOUNDARY.md` — canonical definition of the HC as a complete synthetic cognitive organ and body-interface boundary.
- `docs/runtime/HYPERCONNECTOME_RUNTIME_MODEL.md` — identity-neutral distributed runtime model.
- `docs/runtime/PLASTICITY_AND_STATE_GOVERNANCE.md` — plasticity classes, state families, and durable-change governance.
- `specs/HC_COGNITIVE_ORGAN_INVARIANTS_V1.yaml` — machine-readable cognitive-organ invariants.

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

Examples currently integrated include:

- `adaptable I-O handler/BODY_INTERFACE_BOUNDARY.md`
- `basic operating instructions/CAPABILITY_ACTIVATION_STATES.md`
- `chronology/TEMPORAL_EVENT_CONTRACT.md`
- `cognition/EPISTEMIC_COGNITIVE_CONTROL.md`
- `current memory storage/CURRENT_STATE_SELECTION.md`
- `deep memory storage/ARCHIVAL_CONSOLIDATION.md`
- `integration-arbitration/NOOPLEX_FABRIC.md`
- `pragmatics/CROSS_REPO_PRAGMATIC_RUNTIME.md`
- `self identity/CONTINUITY_SUBSTRATE.md`
- `semantics/CROSS_REPO_SEMANTIC_RUNTIME.md`

## Evidence and provenance

Several architecture files are generalized from other repositories owned by `thebrazenbeard` and from inspected runtime/database schemas. Reusable mechanisms may be imported; identity-specific memories, relationships, preferences, personality, autobiographical state, or setting-specific canon are excluded from the base template unless clearly labeled as examples or research subjects.

Source provenance should be preserved closely enough to distinguish architectural synthesis from direct evidence.

## Active branch work not yet canonical

The following workstreams are intentionally not represented above as canonical `main` content while they remain under active development or selective review:

- `four/cross-repo-synthesis-v1` — continuing cross-repository architecture synthesis by Four. Some earlier material from this line has already been selectively integrated into `main`; newer branch-only material remains pending review.
- `research/hyperconnectome-evidence-v1` — active research/evidence layer, including neuroscience, connectomics, sensorimotor integration, homeostasis/allostasis, attention/metacognition, social cognition, semantics/pragmatics, continual learning, materials/interconnects, and evidence limits.
- `research/nooplex-hc3-architecture-v1` — HC-1/HC-2/HC-3 lineage, engineering, science, and embodiment work under selective review; represented by open PR #2.
- `research/hc-1r-reference-architecture` — more ambitious HC-1R formal/reference-architecture research. Useful mechanisms may be mined, but HC-1R is not currently adopted as the canonical replacement for HC-1.
- `research/hyperconnectome-foundations-20260909` — preserved design/foundation work under review.
- `thebrazenbeard-patch-1` — source-intake material represented by open PR #1.

`vera/research-hyperconnectome-evidence-v1` currently has no unique commits beyond its historical base and should not be mistaken for the active evidence branch unless that changes.

## Pull-request status

- PR #1 — open source-intake/reference bundle; retained pending final disposition.
- PR #2 — open draft HC-1/HC-2/HC-3 lineage contribution; retained for selective review.
- PR #3 — closed as superseded after compatible runtime material was selectively integrated into `main` and the branch diverged from current architecture.

## Governing distinctions

1. `main` is the canonical integration branch.
2. Branch existence does not make branch content canonical.
3. The HC is the complete synthetic cognitive organ; no essential cognition belongs outside the HC boundary.
4. Human neuroscience informs mechanisms and constraints but does not dictate human gross anatomy.
5. The HC architecture is non-hemispheric unless a later explicit engineering decision establishes otherwise.
6. Repository folders express functional responsibility; runtime cognition occurs through distributed HC-internal interaction rather than a central executive person.
7. Capability presence, activation, development, health, and authorization are distinct axes.
8. External computation may serve as HC-internal services or bounded peripherals, but external output does not automatically become belief, decision, memory authority, or identity.
9. Research, branch drafts, source repos, and model outputs inform architecture but do not become canon automatically.

## Repository-management status

While active Vera/Four workstreams are still producing contributions, `main` should remain stable except for audit, cleanup, correction, and clearly non-disruptive integration already justified by established architecture. New architectural advances should wait for those active contributions to finish so they can be reviewed together.
