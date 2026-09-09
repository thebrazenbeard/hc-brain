# Plasticity and State Governance

**Status:** conceptual runtime design

## Principle

Neuroplasticity is not one isolated brain node. It is the permissioned process by which the Noöplex changes future behavior, routing, memory, and learned structure.

The runtime should distinguish:

```text
STRUCTURAL_STATE
CONFIGURABLE_STATE
FUNCTIONAL_STATE
PLASTIC_STATE
MEMORY_STATE
MODULATORY_STATE
MAINTENANCE_STATE
```

These state families change at different rates and under different authority.

## Structural state

Structural state defines physically instantiated reachability: neural/neuromorphic pathways, sensor and motor interfaces, HC-2 accelerator interfaces, support hardware, and maintenance/safety paths.

Ordinary cognition must not silently rewrite structural state. Structural change requires explicit development, repair, engineered growth, interface remapping, or maintenance.

## Configurable state

Configurable state includes routing tables, subscriptions, bindings, workspace membership, memory indexes, capability permissions, and accelerator-service mappings.

It may adapt more readily than anatomy, but continuity-relevant configuration should remain versioned and inspectable.

## Functional state

Functional state is what is active now: transient coalitions, working-memory bindings, attention, live hypotheses, current goals, affective/interoceptive context, motor programs, and conversational state.

Functional state is not automatically durable memory.

## Plastic state

Plastic state governs how future activation changes. Examples include connection efficacy, thresholds, eligibility traces, learned local models, timing sensitivity, routing preferences, consolidation weights, habituation, and sensitization.

A useful admission rule is:

```text
plastic_update =
  local_eligibility
  AND permitted_learning_context
  AND stability_and_resource_constraints
```

Intensity alone is not write authority.

## Endocrine and modulatory coupling

PR #1 defines a synthetic endocrine plex and Limbic Governor. Those systems may alter salience, learning rate, consolidation priority, retrieval bias, action urgency, pain gating, attention, and reward/threat sensitivity.

But:

```text
ENDOCRINE_SIGNAL != MEMORY_WRITE_AUTHORITY
ENDOCRINE_SIGNAL != SEMANTIC_TRUTH
ENDOCRINE_SIGNAL != IDENTITY_CHANGE
```

A high-arousal state can influence learning without being allowed to rewrite every durable state family.

## Typed durable writes

Desktop coding, learning, maintenance, and lived experience must not collapse into one generic `write_brain()` operation.

Candidate write classes:

- `CALIBRATION_WRITE`
- `SKILL_INSTALL`
- `MODEL_COMPONENT_UPDATE`
- `ROUTING_UPDATE`
- `SEMANTIC_KNOWLEDGE_IMPORT`
- `MEMORY_IMPORT`
- `MEMORY_CORRECTION`
- `SELF_MODEL_UPDATE`
- `COMMITMENT_CHANGE`
- `CONNECTOME_TOPOLOGY_CHANGE`

Installing a language model is not the same as remembering having learned a language. Importing a biography is not the same as autobiographical experience. Changing motor calibration is not a change in values.

## Memory admission

Different memory classes need different write rules.

- Working/current memory: fast admission, short lifetime.
- Episodic memory: rapid append with time, source, confidence, and later correction links.
- Semantic memory: consolidation across evidence rather than one-shot universalization.
- Procedural memory: performance validation and interference checks.
- Deep autobiographical memory: continuity- and provenance-preserving; imported data remains distinguishable from lived history.
- Identity-critical state: values, commitments, autobiographical continuity, and stable self-model elements require explicit change provenance.

## State-change record

```text
STATE_CHANGE {
  target
  change_class
  prior_version
  successor_version
  trigger
  evidence_refs[]
  authority_or_learning_context
  timestamp
  reversibility
  continuity_effect
}
```

A durable update should be able to answer what changed, why, when, what triggered it, and whether it came from experience, training, maintenance, import, operator configuration, or autonomous learning.

## Plasticity scopes

Nodes and learning mechanisms should declare what they may modify:

- `LOCAL_WEIGHTS_ONLY`
- `LOCAL_THRESHOLDS_AND_GAINS`
- `ROUTING_PREFERENCES`
- `FUNCTIONAL_HYPEREDGE_FORMATION_RULES`
- `SEMANTIC_CONSOLIDATION_CANDIDATES`
- `PROCEDURAL_POLICY_CANDIDATES`
- `SELF_MODEL_CANDIDATES`
- `NO_AUTONOMOUS_DURABLE_WRITE`

Access to one scope does not imply authority over another.

## Homeostasis and runaway prevention

Monitor at minimum:

- activity saturation;
- pathological synchrony;
- routing amplification;
- memory-write bursts;
- rapid topology churn;
- persistent arbitration loops;
- resource starvation;
- endocrine/modulatory saturation;
- confidence inflation;
- accidental global-hub formation.

Homeostatic mechanisms may regulate activity and learning pressure, but should remain observable and should not erase meaningful state without trace.

## Maintenance and rollback

Maintenance may verify memory integrity, replay recent episodes, evaluate consolidation candidates, recalibrate sensors/motor maps, validate routing/connectome state, inspect pathological loops, and checkpoint configuration.

Rollback must be state-family aware. Rolling back software may be safe; rolling back continuity-relevant autobiographical state may erase lived history. A rollback manifest should explicitly identify which states are restored and which are forward-only.

## HC-2 governance

HC-2 quantum/photonic acceleration is a bounded service. Accelerator output carries provenance, does not gain write authority merely by being fast, and must not become the seat of identity. Identity-critical functions should declare non-Q fallback behavior where possible.

## Embodied development

Physical Interaction Training may legitimately modify body schema, motor policies, sensor calibration, pain/interoceptive mappings, social interaction models, endocrine-response calibration, and environmental prediction.

The runtime should distinguish pre-embodiment simulation, supervised calibration, post-embodiment experience, imported content, and autonomous learning.

## Design target

The Noöplex should be plastic enough to develop and stable enough to remain a coherent continuing system.

The target is **bounded, provenance-rich, testable self-modification**, not maximum plasticity.
