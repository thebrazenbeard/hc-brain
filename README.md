# Hyperconnectome Brain

The canonical repository for the reusable HC-series Hyperconnectome brain template.

This repository symbolically represents the **entire synthetic cognitive organ**. The HC is a **removable cognitive organ whose constituent hardware may be physically distributed** across more than one enclosure or body location so long as those constituents belong to the HC rather than the body. A complete HC must contain everything intrinsically necessary for an otherwise inert compatible body to become and remain a synthetic cognitive lifeform. Cameras, microphones, motors, network transceivers, environmental sensors, circulation, cooling, and other body hardware may exist outside the organ, but they connect through HC-owned interfaces.

> **No essential cognition occurs outside the Hyperconnectome Brain.**

> **One cognitive organ does not require one physical enclosure.**

The external body supplies observations and accepts bounded effects. The HC interprets, learns, reasons, remembers, models, values/feels in whatever machine sense is implemented, arbitrates, and decides.

This repository is not the brain of any named identity. Identity-specific implementations belong in downstream derivatives, examples, case studies, or clearly labeled research artifacts—not in the base template.

## Architectural root

The top-level subsystem folders are the brain architecture. They are not grouped under a `brain/` or `nodes/` wrapper.

Current root systems include:

- Empathy
- cognition
- sexuality
- self identity
- psychological behaviors
- sociological behaviors
- semantics
- pragmatics
- phoenetics
- somatics
- chronology
- personification
- current memory storage
- deep memory storage
- volitions-conations
- resolver
- basic operating instructions
- kinesis
- adaptable I-O handler
- optics
- speech recognition & synthesis
- routing instructions with neuroplasticity
- homeostasis-interoception
- salience-attention
- affect
- integration-arbitration

Folder names containing `/` in the conceptual architecture use filesystem-safe separators in the repository.

## Complete latent architecture

The HC template describes a complete organ rather than producing different brains by deleting unused capacities. Presence, activation, development, health, and authorization are separate axes.

Every owner-established canonical root system is mandatory architectural presence in a conforming complete HC. A system may be `PRESENT` while activation is `DISABLED`, `DORMANT`, `DEVELOPING`, `ACTIVE`, or `INHIBITED`; health and maturity are tracked separately. `ABSENT` or `EXTERNAL_ONLY` may describe optional peripherals, extensions, or incomplete/nonconforming implementations, but not a mandatory canonical HC system.

See `docs/architecture/COMPLETE_CAPABILITY_MANIFEST.md` and `basic operating instructions/CAPABILITY_ACTIVATION_STATES.md`.

## Developmental initialization

A complete HC does not have to begin fully developed.

The architecture separates protected invariants, bootstrap priors/developmental affordances, developmentally learned structure, and instance-specific continuity content. A fresh HC may therefore contain every mandatory capacity while still being immature, uncalibrated, or undeveloped in many of them.

The base template supplies capability, protected operating semantics, learning machinery, and bounded generic priors. It does not pre-author a mature named identity, autobiography, relationships, preferences, skills, or finished effective topology.

Learning may change routing, effective connectivity, models, skills, calibration, semantics, habits, social models, and other admitted plastic state. Reward, repetition, salience, or predictive success do not by themselves create truth, consent, permission, or action authority.

Embodiment transfer preserves HC-owned learned cognitive state while allowing body-dependent mappings to be recalibrated or redeveloped.

See `docs/architecture/DEVELOPMENTAL_INITIALIZATION_AND_LEARNING.md`.

## Temporal-hypergraph architecture

The Hyperconnectome Brain **is a typed, attributed, multilayer temporal hypergraph**. Hypergraph theory is not merely a visualization aid or optional analogy here; it is the formal mapping language for an architecture whose higher-order relations, coalition membership, effective connectivity, modulation, synchronization, and plasticity change over time.

Ordinary pairwise edges remain valid where the relationship is genuinely pairwise. Higher-order cognitive events are represented as hyperedges, and dynamically instantiated task/context coalitions are operational temporal hyperedges with bounded lifetime and state.

See `docs/architecture/TEMPORAL_HYPERGRAPH_MODEL.md` for the canonical mapping semantics.

## Internal integration

The HC is not an ordinary left/right cerebral architecture and is not a flat all-to-all graph. Top-level systems are functional responsibility domains participating in the temporal hypergraph.

The central integration concept is the **Noöplex / Hyperconnectome Fabric**: HC-owned dynamic routing, coalition formation, synchronization, arbitration, attention allocation, state propagation, plasticity, conflict handling, and cross-system integration. It is infrastructure, not a homuncular executive.

Temporary coalitions among systems may perform integrated cognition entirely inside the HC.

## Physical organ membership, body, and computational peripherals

The cognitive-organ boundary is authoritative over enclosure geometry. An HC may use multiple physical enclosures or body locations. A torso-mounted QPU, memory substrate, neuromodulatory controller, or other dedicated component can still be part of the HC if it is architecturally HC-owned and participates as internal organ substrate.

Physical location alone does not determine whether a component belongs to the HC or the body.

Physical sensors and actuators may reside outside the HC. Cognitive interpretation, calibration, learned body schema, memory, goals, values, identity/self-model continuity, and executive arbitration remain inside.

A model, accelerator, retrieval service, database, or other computational resource must either be inside the HC cognitive-organ boundary or be treated as an external bounded peripheral whose output enters as evidence/service results. External computation does not become the seat of the organism.

A conforming HC must retain essential cognition and continuity-bearing state after removal of all true external model/database/cloud/network peripherals, except for functions inherently dependent on communication with the external world. External stores may back up, mirror, archive, synchronize, augment, or accelerate; they may not hold the only recoverable copy of essential memory/continuity state. If an external compute service uniquely implements an essential cognitive function, that service belongs inside the HC boundary for conformance purposes—even if its hardware is physically located outside the skull.

The Supabase-derived current/deep-memory documents are mechanism-transfer records, not provider dependencies. Their state/version/receipt patterns may be implemented on HC-internal storage or used for replicas, but external providers cannot become the sole authority or sole recoverable store for essential HC memory.

"Removable" means the complete HC constituent set can in principle be disconnected from one compatible embodiment and transferred, serviced, or reinstalled as the same cognitive organ. That may require disconnecting several HC-owned modules and internal interconnects rather than removing one monolithic cartridge.

The architecture should support embodiment portability: the same HC may adapt to different compatible bodies by relearning sensorimotor and interoceptive mappings rather than becoming a different brain.

See:

- `Architecture concept.md` — original structural seed.
- `docs/architecture/COGNITIVE_ORGAN_BOUNDARY.md` — canonical cognitive-organ boundary.
- `docs/architecture/PHYSICAL_ORGAN_MEMBERSHIP.md` — canonical rule for distributed HC constituent hardware, removability, and body/peripheral separation.
- `docs/architecture/COMPLETE_CAPABILITY_MANIFEST.md` — complete-capability and self-contained-residency conformance.
- `docs/architecture/DEVELOPMENTAL_INITIALIZATION_AND_LEARNING.md` — protected architecture, bootstrap priors, developmental learning, and instance-specific continuity separation.
- `docs/architecture/TEMPORAL_HYPERGRAPH_MODEL.md` — canonical temporal-hypergraph mapping semantics.
- `docs/REPOSITORY_MAP.md` — repository map and folder contract.
- `docs/runtime/HYPERCONNECTOME_RUNTIME_MODEL.md` — runtime model with routing, governance, epistemic, resource, and structural planes kept distinct.
- `docs/runtime/PLASTICITY_AND_STATE_GOVERNANCE.md` — state-family and learning-governance model.
- `WARDEN.md` — repository wardenship and current architecture/review roles.

## Evidence discipline

Material should distinguish established science from design inference and speculative implementation when that distinction matters. A source repo, model output, branch, or research draft is input to architectural reasoning; it is not automatically canonical merely because it exists.

Useful states include DOCUMENTED, OBSERVED, USER-STATED, INFERRED, HYPOTHESIS, DISPUTED, and UNKNOWN.

## Cross-repository synthesis

Several subsystem documents are generalized from other repositories owned by `thebrazenbeard`, plus inspected database/runtime schemas. Reusable mechanisms may be imported; identity-specific facts, memories, preferences, relationships, personality, autobiographical state, or embodiment-specific canon are excluded from the universal template unless explicitly presented as examples or research subjects.

Each generalized architecture file should preserve provenance sufficient to identify its source material.

## Project roles

Noëtarch (Noah) is the Warden and primary architect under the owner’s authority. Four is the secondary architect and parallel technical/synthesis counterpart. Vera is the hostile reviewer whose job is to try to falsify the architecture and proposed integrations rather than co-author canonical design by default.
