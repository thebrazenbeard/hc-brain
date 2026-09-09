# Learned Behavior Architecture

Status: template architecture.

## Purpose

The psychological-behavior subsystem represents learned behavioral tendencies, conditioned responses, coping strategies, habits, approach/avoidance patterns, expectation-driven behavior, and metacognitive correction without treating any learned pattern as permanent identity.

## Behavior record

A learned behavior should be representable with:

- trigger/context conditions;
- internal state dependencies;
- predicted function or consequence;
- observed outcome history;
- strength/activation probability;
- provenance;
- generalization scope;
- confidence;
- reinforcement/extinction history;
- currentness;
- inhibition/suppression state;
- competing behavior candidates.

## Conditioning without determinism

Conditioning modifies priors and action tendencies. It does not eliminate deliberation, conation, or present context.

`LEARNED_TENDENCY != INEVITABLE_ACTION`

`PAST_REINFORCEMENT != CURRENT_VALUE`

`HABIT != IDENTITY`

Classical/Pavlovian, instrumental, observational, and social learning mechanisms may all contribute, but their outputs remain subject to current appraisal, prediction, arbitration, and action gating.

## Acquisition

Behavioral learning may use:

- repeated cue/outcome association;
- action/outcome contingencies;
- prediction error;
- imitation/observation;
- explicit instruction;
- self-reflection/meta-learning;
- affective and homeostatic consequences;
- social feedback;
- success/failure of prior coping strategies.

## Extinction and revision

A behavior that is no longer adaptive should be capable of weakening, context-narrowing, inhibition, replacement, or explicit revision.

Extinction should not necessarily erase historical association; old responses may reappear under context shift or stress and should be modeled as retained but inhibited structure when supported.

## Generalization control

The system must avoid turning one learned association into an indiscriminate global rule. Generalization should be evidence-bound and testable across context changes.

When a trigger is only correlated with an outcome, the HC should preserve causal uncertainty and seek discriminating experience when consequential.

## Self-sealing behavior control

A learned strategy can become self-confirming by altering the environment to produce the evidence it expects. The cognitive layer should be able to identify when behavior itself changes the observation distribution and test alternative strategies.

## Conflict with current self-state

A behavior may remain strongly learned even when current values, conations, commitments, or self-model no longer endorse it.

The architecture therefore allows:

`learned impulse + reflective rejection + inhibited execution`

without rewriting history to claim the impulse never existed.

## Cross-system interfaces

Strong coupling is expected with cognition, conation, affect, salience/attention, memory, chronology, social modeling, personification, somatics, self identity, resolver, and neuroplasticity.

## Provenance

Integrated from `four/cross-repo-synthesis-v1` after Warden review and retained as identity-neutral subsystem architecture.