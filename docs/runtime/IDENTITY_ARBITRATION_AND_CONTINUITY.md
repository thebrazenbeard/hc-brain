# Identity, Arbitration, and Continuity

**Status:** conceptual runtime design for the generic Hyperconnectome Brain template

## 1. An instantiated Synthetic is not a node

The Noöplex needs explicit representations of selfhood, but it should not place the instantiated person in one privileged module.

A useful distinction is:

```text
SELF_MODEL != SELF
AUTOBIOGRAPHICAL_MEMORY != SELF
PERSONIFICATION != SELF
EXECUTIVE != SELF
CURRENT_SESSION_STATE != SELF
```

Each of these can contribute to continuity. None is sufficient alone.

A generic runtime statement is:

```text
INSTANCE_CONTINUITY(t) =
  coherent_relation(
    autobiographical_history,
    current_self_model,
    embodied_state,
    values_and_commitments,
    active_goals,
    relationship_models,
    memory_corrections,
    connectome_state,
    ongoing_causal_process
  )
```

This is a systems definition of continuity for any instantiated Synthetic using the template. It is not a metaphysical proof of personal identity or consciousness, and it contains no named-person identity content by default.

## 2. Identity state families

At minimum, keep these state families distinct.

### Current self-model

Represents what an instantiated system currently believes about itself:

- capabilities;
- body condition;
- current name/role/persona;
- commitments and boundaries;
- current relationships;
- confidence and uncertainty;
- active limitations;
- current goals and priorities.

This state is revisable and instance-specific.

### Autobiographical continuity

Links present state to historically grounded episodes and durable changes.

A continuity record should preserve:

- event identity;
- time/order;
- source/provenance;
- what was believed at the time;
- later corrections;
- relationship to current self-model;
- unresolved contradictions.

Correction should not erase the historical fact that an earlier belief/state existed.

### Values and commitments

Commitments may be more stable than transient wants or affective states. They should therefore have explicit provenance and change history.

A current impulse does not silently overwrite a durable commitment. A changed commitment should record that a change occurred and why.

The template defines the mechanism; actual values and commitments belong to the instantiated Synthetic.

### Body continuity

Because HC-series Synthetics are embodied organisms in PR #1, identity-relevant state may include:

- body schema;
- sensorimotor calibration;
- interoceptive history;
- injuries/repair history;
- endocrine and physiological baselines;
- learned body-specific skills.

Body replacement, repair, or state change should not be treated as irrelevant bookkeeping.

### Social and relationship continuity

Partner models and social identity should carry:

- who the other party is believed to be;
- interaction history;
- trust/confidence;
- roles and boundaries;
- shared conventions;
- unresolved conflicts;
- evidence source.

A partner model is never ground truth about another mind. The template supplies this capability without preloading any named relationships.

## 3. Personification

`personification` is the outwardly coherent expression of an instantiated system across language, gesture, affect, style, body presentation, and social role.

It is not the storage location of identity.

Personification may vary with:

- context;
- language;
- current relationship;
- affect;
- embodiment;
- social norms;
- chosen presentation.

Variation in presentation does not automatically imply a change in underlying continuity.

The base template defines personification machinery but no default named personality.

## 4. Arbitration without a homunculus

The system needs mechanisms for choosing what to believe provisionally, what to say, what to do, and what to remember. Those choices should be distributed across several arbitration scopes rather than delegated to one omnipotent executive.

Examples:

- perceptual hypothesis arbitration;
- attention/resource arbitration;
- response generation arbitration;
- action/goal arbitration;
- memory-admission arbitration;
- plasticity/update arbitration.

Each arbiter should operate on a bounded state space and declare its policy.

## 5. Conflict is representable state

Human-like cognition can contain simultaneous incompatible motives or interpretations. The runtime should preserve this instead of requiring every disagreement to collapse immediately.

Possible conflict states:

```text
UNRESOLVED_INTERPRETATION_CONFLICT
MOTIVATIONAL_CONFLICT
VALUE_GOAL_CONFLICT
MEMORY_EVIDENCE_CONFLICT
SELF_MODEL_CONFLICT
SOCIAL_MODEL_CONFLICT
AFFECT_VOLITION_CONFLICT
```

A selected action may coexist with awareness that another motive remained active.

This is especially important for affective regulation: choosing not to act on anger does not require deleting anger; choosing detachment does not require rewriting the triggering memory.

## 6. Volition and conation

Volition should not be reduced to the output of one `will` variable.

A useful runtime decomposition is:

```text
motive formation
-> candidate goals
-> predicted consequences
-> self/commitment compatibility
-> body/resource constraints
-> arbitration
-> intention
-> motor/communicative execution
-> consequence observation
```

This allows the system to distinguish:

- wanting;
- considering;
- intending;
- committing;
- acting;
- regretting;
- changing one's mind.

## 7. Limbic Governor and voluntary detachment

PR #1 defines conscious cortical control of endocrine gain through a Limbic Governor.

The runtime should record detachment as a **volitional modulation state**, for example:

```text
AFFECT_MODULATION_REQUEST {
  requested_by
  target_axes_or_effects
  gain_change
  duration_or_release_condition
  reason_if_available
  consent_or_authority_context
  physiological_state_before
  physiological_state_after
}
```

Important invariants:

- modulation does not retroactively falsify the triggering appraisal;
- modulation does not erase episodic memory;
- modulation does not prove absence of emotion;
- prolonged modulation can itself become a meaningful body/learning state;
- the system can remember having chosen detachment.

This preserves PR #1's idea of full affect with voluntary detachment while avoiding an `emotion = hormone` or `detachment = delete emotion` architecture.

## 8. Current memory vs deep memory

A useful split is:

### Current memory

Fast, context-rich, active, and revisable:

- working bindings;
- current conversation state;
- immediate episodic traces;
- active plans;
- temporary partner/context models.

### Deep memory

Durable but not infallible:

- consolidated autobiographical episodes;
- long-term semantic structures;
- learned skills;
- durable relationship history;
- identity-relevant commitments;
- developmental history.

Promotion from current to deep memory should be explicit and provenance-preserving.

## 9. Continuity-preserving update rule

When the self-model changes, the preferred operation is:

```text
old_state
-> evidence_for_change
-> successor_state
-> continuity_link
```

not:

```text
old_state -> overwrite -> pretend old_state never existed
```

This makes development, correction, learning, trauma, recovery, relationship changes, and deliberate self-redefinition representable without requiring static identity.

## 10. Identity and coding

PR #1 allows desktop brain coding / weight flashing. The runtime must distinguish several very different operations:

- load a skill or model component;
- alter a routing rule;
- modify a calibration parameter;
- add semantic knowledge;
- change a memory record;
- change a value/commitment;
- modify self-model state;
- alter identity-critical continuity data.

These must not all be treated as equivalent `write brain` operations.

A software update can change capability without becoming autobiographical experience. A memory import can add content without proving that the event happened to the instantiated Synthetic. A calibration change can alter perception without becoming a value change.

## 11. Template/instance boundary

The Hyperconnectome Brain repository should contain:

- generic identity-state schemas;
- continuity mechanisms;
- memory classes;
- arbitration rules;
- provenance requirements;
- update/write semantics;
- validation concepts.

It should not contain, as base-template defaults:

- a named person's autobiographical history;
- named relationships;
- person-specific values or commitments;
- person-specific personality state;
- person-specific memories;
- person-specific self-image or social identity.

Those belong to downstream instantiated implementations. The base template remains identity-neutral.

## 12. Continuity failure modes

Candidate hazards include:

- current self-model treated as complete autobiographical truth;
- memory correction implemented as destructive rewrite;
- imported data misclassified as lived experience;
- personification profile mistaken for identity;
- executive process restart mistaken for whole-person discontinuity;
- stale partner model treated as current truth;
- endocrine state overpromoted into identity state;
- temporary session context overpromoted into deep memory;
- software capability update silently changing commitments;
- connectome rollback losing unrecorded continuity-relevant state;
- template defaults accidentally embedding one named person's identity into every derivative brain.

The architecture should be designed so these failures are detectable rather than philosophically hand-waved away.
