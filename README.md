# Hyperconnectome Brain

The canonical repository for the reusable HC-series Hyperconnectome brain template.

This repository defines architecture, subsystem contracts, runtime organization, research constraints, and engineering principles for a non-hemispheric, distributed Hyperconnectome system. It is not the brain of any named identity. Identity-specific implementations belong in downstream derivatives, examples, case studies, or clearly labeled research artifacts—not in the base template.

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

## Runtime model

The HC is not an ordinary left/right cerebral architecture and is not a flat all-to-all graph. Top-level systems are functional responsibility domains participating in a dynamically composed, multilayer, temporally reconfigurable network.

See:

- `Architecture concept.md` — original structural seed.
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
