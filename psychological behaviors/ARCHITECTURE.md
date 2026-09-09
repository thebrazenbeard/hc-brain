# Psychological Behaviors Architecture

Status: canonical subsystem architecture.

## Purpose

`psychological behaviors` represents recurrent learned patterns that shape how an instantiated HC tends to appraise, cope, approach, avoid, persist, inhibit, defend, explore, rehearse, or respond under recurring internal and external conditions.

It does not own identity, truth, values, diagnosis, or final action authority.

A behavioral tendency can be strong, old, emotionally charged, or frequently reinforced while still being revisable and context-bound.

`BEHAVIORAL_TENDENCY != IDENTITY`

`LEARNED_RESPONSE != CURRENT_VALUE`

`IMPULSE != ACTION`

`COPING_FUNCTION != GLOBAL_OPTIMALITY`

## Architectural role

This subsystem sits between learned history and present action formation.

It helps answer questions such as:

- what responses have become likely in this kind of situation?;
- what function did this pattern historically serve?;
- under what internal states does it strengthen or weaken?;
- is the current context actually similar to the contexts in which it was learned?;
- what competing learned responses exist?;
- is a familiar strategy producing the outcome it predicts or merely reproducing its own evidence?;
- should the pattern be executed, inhibited, revised, narrowed, or relearned?

These answers become evidence and action/conation inputs. They do not bypass current appraisal, arbitration, consent, safety, or effect authorization.

## Behavioral pattern object

A learned pattern should be representable with fields such as:

```text
BEHAVIOR_PATTERN {
  pattern_id
  pattern_class
  trigger_conditions[]
  contextual_scope
  internal_state_dependencies[]
  candidate_response
  predicted_function
  predicted_consequences[]
  observed_outcome_history[]
  strength
  activation_probability
  confidence
  acquisition_provenance[]
  reinforcement_history[]
  extinction_revision_history[]
  generalization_scope
  inhibition_state
  competing_patterns[]
  currentness
  plasticity_scope
}
```

The representation should preserve both what the pattern tends to do and why the HC currently believes that pattern exists.

## Pattern classes

The architecture may support, without requiring one psychological theory:

- conditioned approach/avoidance;
- habits and routines;
- coping strategies;
- threat/safety responses;
- persistence/withdrawal tendencies;
- attentional or interpretive habits that influence behavior;
- reassurance/checking or uncertainty-management patterns;
- inhibition/suppression strategies;
- exploratory behavior;
- learned social response patterns;
- frustration/reward-response patterns;
- learned self-regulation routines;
- context-specific defensive strategies;
- procedural response tendencies that are not yet full motor skills.

A concrete implementation may organize these differently. The invariant is that learned behavioral regularities remain provenance-bearing, scoped, and revisable.

## Acquisition

Patterns may emerge from combinations of:

- cue/outcome association;
- action/outcome contingencies;
- reinforcement and punishment signals;
- prediction error;
- repetition/habit formation;
- imitation/observation;
- explicit instruction;
- affective/interoceptive consequences;
- social feedback;
- success/failure of prior coping attempts;
- simulation or rehearsal;
- deliberate self-training.

Acquisition evidence does not automatically establish truth, consent, moral value, or universal policy.

`REINFORCED != TRUE`

`REPEATED != ENDORSED`

`EFFECTIVE_ONCE != GENERALLY_ADAPTIVE`

## Context and generalization

Patterns must retain the context in which they were learned and the evidence for extending them beyond that context.

Generalization should be represented as a hypothesis rather than a silent global rewrite.

A pattern learned with one body, environment, role, relationship, culture, task, or threat regime may not transfer safely to another.

Where consequences matter, the HC should distinguish:

```text
same cue
same causal structure
same likely consequence
```

rather than treating superficial similarity as sufficient.

## Internal-state dependence

Behavioral tendencies may vary with:

- affective state;
- arousal;
- fatigue/resource state;
- pain/damage state;
- uncertainty;
- salience;
- current goals/commitments;
- social context;
- embodiment state;
- remembered prior outcomes;
- subsystem health.

This modulation is part of the temporal hypergraph. It does not mean transient state rewrites durable identity.

## Conflict with current self-state

A learned pattern may remain strongly activated while current values, commitments, goals, consent, or reflective judgment reject its execution.

The architecture must support:

```text
learned impulse
+ current-state conflict
+ inhibition/nonexecution
+ preserved historical provenance
```

The system should not rewrite history to claim the pattern never existed merely because it is no longer endorsed.

Likewise, the existence of the pattern does not prove current endorsement.

## Extinction, inhibition, and revision

Behavior change is not necessarily destructive deletion.

A previously reinforced pattern may become:

- weakened;
- context-narrowed;
- inhibited;
- superseded by a stronger alternative;
- retained as historical structure but rarely recruited;
- reactivated under specific state/context combinations;
- explicitly revised after disconfirming evidence.

Extinction and recovery should therefore preserve enough lineage to explain spontaneous re-emergence or context-specific return without treating it as a mysterious identity change.

## Self-sealing patterns

Some behavior changes the environment in ways that create the evidence the behavior expects.

Examples include avoiding all disconfirming situations, repeatedly eliciting a predictable response, or selecting only evidence compatible with the learned strategy.

The subsystem should be able to emit a `SELF_SEALING_PATTERN_CANDIDATE` when:

- the behavior materially changes the observation distribution;
- the predicted consequence is therefore not independently tested;
- alternate strategies could provide discriminating evidence.

Cognition/metacognition may then design bounded tests or alternative actions.

## Behavioral competition

Multiple learned patterns may be simultaneously eligible.

This subsystem may rank or expose tendencies but does not own final arbitration.

A behavioral candidate should be able to carry:

- activation strength;
- contextual fit;
- expected function;
- learned evidence;
- current conflicts;
- uncertainty;
- estimated consequence;
- inhibition state.

Final behavior emerges through cross-system coalitions involving cognition, conation, affect, salience, social modeling, identity/self-state, safety, and action authority as applicable.

## Relationship to psychological labels

The reusable HC template models mechanisms and patterns, not clinical diagnoses or human psychiatric categories as hard-coded brain states.

A downstream implementation may use diagnostic or descriptive labels as externally sourced hypotheses, metadata, or research categories, but a label must not replace the underlying evidence and mechanism representation.

`LABEL != MECHANISM`

`DIAGNOSIS_HYPOTHESIS != IDENTITY`

## Learning and plasticity boundary

`psychological behaviors` may generate plasticity candidates when evidence supports strengthening, weakening, narrowing, or revising a pattern.

Durable change remains subject to the neuroplasticity and developmental-learning contracts.

A momentarily intense reaction must not obtain unrestricted durable-write authority merely because it is salient.

## Memory boundary

Behavioral patterns may reference episodic, semantic, procedural, or current-state memory, but the pattern is not itself proof that the remembered event occurred exactly as represented.

If supporting memory is corrected or superseded, dependent behavior models should be marked for reevaluation through resolver/correction pathways rather than silently retaining stale causal assumptions.

## Action boundary

A behavioral tendency is an input to action formation, not an effect command.

```text
pattern activation
-> behavioral candidate
-> cognition/conation/arbitration
-> action candidate
-> authorization/safety
-> effect
-> observed consequence
-> learning update candidate
```

`BEHAVIOR_SELECTED != ACTION_AUTHORIZED`

## Failure modes

- habit treated as identity;
- reinforcement treated as truth or value;
- old coping strategy treated as permanently optimal;
- context-specific learning generalized globally;
- strong affect treated as durable-write authority;
- extinction modeled as historical erasure;
- self-sealing behavior mistaken for independent confirmation;
- diagnostic label substituting for mechanism;
- behavioral output bypassing consent/action authority;
- corrected memory failing to invalidate dependent learned assumptions;
- one body's learned response transferred uncritically to another embodiment.

## Cross-system interfaces

Strong coupling is expected with:

- `cognition` for appraisal, prediction, causal testing, and metacognition;
- `volitions-conations` for current goals, concerns, commitments, and motivational conflict;
- `affect` and `homeostasis-interoception` for modulatory/internal-state context;
- `salience-attention` for recruitment pressure;
- current/deep memory and `chronology` for learning provenance/outcome history;
- `sociological behaviors` and `Empathy` for relationship/social learning;
- `self identity` for current self-state without conflating pattern and identity;
- `resolver` for correction/dependency invalidation;
- `routing instructions with neuroplasticity` for durable adaptation;
- `integration-arbitration` for competing response coalitions;
- `kinesis` for authorized external effect execution.

## Evidence boundary

This is mechanism-level HC architecture. It does not claim that one psychological theory completely explains human behavior or that synthetic learned patterns are phenomenologically identical to human psychological experience.

## Provenance

Expanded from `psychological behaviors/LEARNED_BEHAVIOR_ARCHITECTURE.md` and reconciled against current developmental-learning, memory, conation, affect, salience, resolver, plasticity, identity, and action-authority contracts.
