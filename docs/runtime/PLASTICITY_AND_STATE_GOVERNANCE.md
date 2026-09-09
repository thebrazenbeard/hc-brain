# Plasticity and State Governance

Status: conceptual runtime design

## Principle

Neuroplasticity is not one isolated subsystem. It is the permissioned process by which the Hyperconnectome changes future behavior, routing, memory, learned structure, and calibration.

The runtime should distinguish:

- `STRUCTURAL_STATE`
- `CONFIGURABLE_STATE`
- `FUNCTIONAL_STATE`
- `PLASTIC_STATE`
- `MEMORY_STATE`
- `MODULATORY_STATE`
- `MAINTENANCE_STATE`

These state families change at different rates and under different rules.

## Structural state

Structural state defines physically instantiated reachability: neural or neuromorphic pathways, support hardware, sensor and motor interfaces, accelerator interfaces, and maintenance paths.

Ordinary cognition must not silently rewrite structural state. Structural change requires explicit development, repair, engineered growth, remapping, or maintenance.

## Configurable state

Configurable state includes routing tables, subscriptions, bindings, workspace membership, memory indexes, capability permissions, and service mappings.

It may adapt more readily than anatomy, but continuity-relevant configuration should remain versioned and inspectable.

## Functional state

Functional state is what is active now: transient coalitions, working-memory bindings, attention, live hypotheses, current goals, affective/interoceptive context, motor programs, and conversational state.

Functional state is not automatically durable memory.

## Plastic state

Plastic state governs how future activation changes. Examples include connection efficacy, thresholds, eligibility traces, learned local models, timing sensitivity, routing preferences, consolidation weights, habituation, and sensitization.

A useful admission rule is:

`plastic_update = local_eligibility AND permitted_learning_context AND stability_and_resource_constraints`

Intensity alone is not write authority.

## Typed durable writes

Training, maintenance, lived experience, imported knowledge, and direct configuration must not collapse into one generic brain-write operation.

Candidate write classes include:

- calibration write;
- skill installation;
- model-component update;
- routing update;
- semantic knowledge import;
- memory import;
- memory correction;
- self-model update;
- commitment change;
- topology change.

Installing or importing information is not the same as remembering having learned or experienced it. Different state classes require different provenance.

## Memory admission

Different memory classes require distinct write rules.

- current/working memory: fast admission, short lifetime;
- episodic memory: rapid append with time, source, confidence, and later correction links;
- semantic memory: consolidation across evidence rather than one-shot universalization;
- procedural memory: performance validation and interference checks;
- deep autobiographical memory in a downstream identity implementation: continuity- and provenance-preserving, with imported material distinguishable from lived history;
- identity-critical state in a downstream implementation: explicit change provenance.

The template defines the mechanisms; identity-specific content lives outside the base repository.

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

A durable update should answer what changed, why, when, what triggered it, and whether it came from experience, training, maintenance, import, configuration, or autonomous learning.

## Plasticity scopes

Learning mechanisms should declare what they may modify, for example:

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

Monitor at minimum for activity saturation, pathological synchrony, routing amplification, memory-write bursts, topology churn, persistent arbitration loops, resource starvation, modulatory saturation, confidence inflation, and accidental global-hub formation.

Homeostatic mechanisms may regulate activity and learning pressure but should remain observable and should not erase meaningful state without trace.

## Maintenance and rollback

Maintenance may verify memory integrity, replay recent episodes, evaluate consolidation candidates, recalibrate sensors or motor maps, validate routing state, inspect pathological loops, and checkpoint configuration.

Rollback must be state-family aware. Restoring software or configuration may be safe while rolling back continuity-relevant lived state can erase valid history. Any rollback manifest should identify which state families are restored and which are forward-only.

## Design target

The Hyperconnectome should be plastic enough to learn and develop while remaining stable enough to preserve coherent operation.

The target is bounded, provenance-rich, testable self-modification—not maximum plasticity.

## Provenance

Adapted from `four/runtime-hyperconnectome-v1/docs/runtime/PLASTICITY_AND_STATE_GOVERNANCE.md` after Warden review. Identity-specific and setting-specific material was removed; the surviving content is mechanism-level template architecture.