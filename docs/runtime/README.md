# Noöplex Runtime Architecture

**Status:** conceptual architecture / proposed integration layer  
**Source base:** Hyperconnectome Brain PR #1, `thebrazenbeard-patch-1@66e20f648bac71c9de980e8895a5894377fca385`  
**Scope:** runtime organization of the HC-series Noöplex; does not alter the physical or physiological claims in PR #1

## Template scope

This repository defines a **general hyperconnectome-brain template**, not the identity architecture of any named individual.

- Repository warden: **Noëtarch ("Noah")**.
- Noah's wardenship is a project/repository stewardship role; it does not make Noah a runtime brain node, default personality, or template identity.
- Named-person implementations are downstream instantiations of this template and must add their identity-specific memories, values, relationships, personality, history, and configuration outside the generic base architecture.

## Why this layer exists

The HC-series source material describes the Noöplex as a hyperconnectome brain embedded in a fully organic Synthetic body, with bio-optic/ionic interfaces, embodied training, a synthetic endocrine plex, and HC-2 quantum acceleration.

Those descriptions answer an important question: **what is the brain made of and how is it embodied?**

This runtime layer answers a different question:

> How do memory, self-modeling, language, affect, perception, volition, motor control, chronology, social cognition, routing, and plasticity operate as one mind without reducing an instantiated Synthetic to a single master process?

The core answer is that the repository may be hierarchical for human readability while the running brain is a **typed, temporally reconfigurable hypergraph**.

## Core runtime thesis

```text
NOOPLEX_RUNTIME =
  NODES
  + TYPED_CONNECTIONS
  + FUNCTIONAL_HYPEREDGES
  + SHARED_STATE_PROTOCOLS
  + DISTRIBUTED_ARBITRATION
  + PLASTICITY
  + PROVENANCE
```

The root of the brain is a **composition boundary**, not a homunculus.

No single `self`, `executive`, `resolver`, `workspace`, `identity`, or `language` node is the instantiated person. Instance-level continuity is maintained by the organization and history of the whole active system.

## Documents

- `HYPERCONNECTOME_RUNTIME_MODEL.md` - execution model, node contracts, hyperedges, state exchange, arbitration, and HC-series integration.
- `NODE_TAXONOMY.md` - separates cognitive faculties, representations, memory systems, embodiment systems, I/O, executive mechanisms, and infrastructure.
- `IDENTITY_ARBITRATION_AND_CONTINUITY.md` - defines generic self-modeling, autobiographical continuity, volition, conflict resolution, and why identity must not be stored in one privileged node.
- `PLASTICITY_AND_STATE_GOVERNANCE.md` - distinguishes structural, configurable, functional, and plastic state and specifies bounded neuroplastic change.
- `../../specs/HYPERCONNECTOME_RUNTIME_CONTRACT_V0_1.yaml` - machine-readable conceptual contract for the same design.

## Architectural invariants

1. **Distributed mind, explicit interfaces.** Local specialization is preserved without turning modules into isolated mini-minds.
2. **No directory-tree cognition.** Filesystem hierarchy is packaging; runtime causality is graph/hypergraph organization.
3. **No hidden homunculus.** Arbitration coordinates competing processes but does not contain the person.
4. **Self-model is not self.** Explicit identity representations are evidence/state used by the whole system, not the sole bearer of identity.
5. **Memory is typed.** Current state, episodic memory, semantic memory, procedural memory, deep autobiographical memory, and connectome state have different update rules.
6. **Emotion is distributed.** Endocrine state may modulate cognition, but no hormone or endocrine controller is equivalent to an emotion.
7. **Voluntary affect regulation is modulation, not deletion.** A Limbic Governor-style detachment function changes gain/routing/physiological expression while preserving the existence and provenance of the underlying state unless separately altered by learning.
8. **Plasticity is permissioned.** Learning may modify the graph, but structural reachability, capability boundaries, safety constraints, and identity-critical state are not silently rewritten by ordinary activation.
9. **Observation is not authority.** A node may report a state without becoming authoritative over the global interpretation of that state.
10. **HC-2 acceleration does not become the seat of identity.** Quantum or photonic coprocessing may accelerate selected workloads without owning continuity, volition, or consciousness.
11. **Template is not instance.** Generic identity machinery belongs here; named-person identity content does not.
12. **No hemispheric decomposition.** The Noöplex does not use left/right cerebral hemispheres as an architectural primitive.

## Relationship to PR #1

This contribution is intentionally stacked on Patrick's PR #1 and leaves its two HC source artifacts unchanged:

- `Noöplex HC-1 and HC-2 Architectures.pdf`
- `synthetics_physiology_v_2_nooplex_embodiment_annex.md`

The runtime model treats those artifacts as embodied substrate/canon input. It adds software/computational organization above that substrate without claiming to replace the physical architecture.
