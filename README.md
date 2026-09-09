# Hyperconnectome Brain

The canonical repository for the reusable HC-series Hyperconnectome brain template.

This repository symbolically represents the **entire synthetic cognitive organ**. If manufactured as a self-contained physical object and installed into an otherwise inert compatible synthetic body, the HC should contain everything intrinsically necessary for that body to become and remain a synthetic cognitive lifeform. Cameras, microphones, motors, network transceivers, environmental sensors, circulation, cooling, and other body hardware may exist outside the organ, but they connect through HC-owned interfaces.

> **No essential cognition occurs outside the Hyperconnectome Brain.**

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

The HC template should describe a complete organ rather than produce different brains by deleting unused capacities. Presence, activation, development, health, and authorization are separate axes.

A major intrinsic capability may therefore be architecturally `PRESENT` while its activation is `DISABLED`, `DORMANT`, `DEVELOPING`, `ACTIVE`, or `INHIBITED`; its health and maturity are tracked separately. A capability can exist in the organ before it is trained, used, or connected to a compatible peripheral.

See `basic operating instructions/CAPABILITY_ACTIVATION_STATES.md` for the current state model.

## Temporal-hypergraph architecture

The Hyperconnectome Brain **is a typed, attributed, multilayer temporal hypergraph**. Hypergraph theory is not merely a visualization aid or optional analogy here; it is the formal mapping language for an architecture whose higher-order relations, coalition membership, effective connectivity, modulation, synchronization, and plasticity change over time.

Ordinary pairwise edges remain valid where the relationship is genuinely pairwise. Higher-order cognitive events are represented as hyperedges, and dynamically instantiated task/context coalitions are operational temporal hyperedges with bounded lifetime and state.

See `docs/architecture/TEMPORAL_HYPERGRAPH_MODEL.md` for the canonical mapping semantics.

## Internal integration

The HC is not an ordinary left/right cerebral architecture and is not a flat all-to-all graph. Top-level systems are functional responsibility domains participating in the temporal hypergraph.

The central integration concept is the **Noöplex / Hyperconnectome Fabric**: HC-owned dynamic routing, coalition formation, synchronization, arbitration, attention allocation, state propagation, plasticity, conflict handling, and cross-system integration. It is infrastructure, not a homuncular executive.

Temporary coalitions among systems may perform integrated cognition entirely inside the HC.

## Body and computational peripherals

Physical sensors and actuators may reside outside the HC. Cognitive interpretation, calibration, learned body schema, memory, goals, values, identity/self-model continuity, and executive arbitration remain inside.

A model, accelerator, retrieval service, database, or other computational resource must either be inside the HC cognitive-organ boundary or be treated as an external bounded peripheral whose output enters as evidence/service results. External computation does not become the seat of the organism.

The architecture should support embodiment portability: the same HC may adapt to different compatible bodies by relearning sensorimotor and interoceptive mappings rather than becoming a different brain.

See:

- `Architecture concept.md` — original structural seed.
- `docs/architecture/COGNITIVE_ORGAN_BOUNDARY.md` — canonical cognitive-organ boundary and capability-presence rule.
- `docs/architecture/TEMPORAL_HYPERGRAPH_MODEL.md` — canonical temporal-hypergraph mapping semantics.
- `docs/REPOSITORY_MAP.md` — repository map and folder contract.
- `docs/runtime/HYPERCONNECTOME_RUNTIME_MODEL.md` — interaction/runtime model.
- `docs/runtime/PLASTICITY_AND_STATE_GOVERNANCE.md` — state-family and learning-governance model.
- `WARDEN.md` — repository wardenship and architectural governance.

## Evidence discipline

Material should distinguish established science from design inference and speculative implementation when that distinction matters. A source repo, model output, branch, or research draft is input to architectural reasoning; it is not automatically canonical merely because it exists.

Useful states include DOCUMENTED, OBSERVED, USER-STATED, INFERRED, HYPOTHESIS, DISPUTED, and UNKNOWN.

## Cross-repository synthesis

Several subsystem documents are generalized from other repositories owned by `thebrazenbeard`, plus inspected database/runtime schemas. Reusable mechanisms may be imported; identity-specific facts, memories, preferences, relationships, personality, autobiographical state, or embodiment-specific canon are excluded from the universal template unless explicitly presented as examples or research subjects.

Each generalized architecture file should preserve provenance sufficient to identify its source material.

## Warden

Noëtarch (Noah) is the repository Warden and primary architectural decision-maker under the owner’s authority. Routine maintenance, integration, research synthesis, conflict resolution, and non-disruptive architectural completion may be performed directly on `main`. Material redesigns of the core architecture should be surfaced to the owner before adoption.
