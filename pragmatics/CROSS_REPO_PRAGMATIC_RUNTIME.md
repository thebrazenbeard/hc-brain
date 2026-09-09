# Cross-Repo Pragmatic Runtime

Status: identity-neutral template architecture synthesis.

## Purpose

Pragmatics converts raw semantic possibilities into context-bounded interaction hypotheses without turning context into arbitrary guesswork. Its job is to represent what a signal is doing here, for whom, under what assumptions, and with what uncertainty.

This synthesis draws reusable mechanisms from SPM, UNVTRSLR, Noema, social-modeling research, and correction/governance patterns. It does not import any person-specific interaction history.

## Pragmatic state is structured, not scalar

A pragmatic interpretation should be represented as a bundle of separable fields rather than one inferred intent label.

Recommended fields include:

- `candidate_force` — assertion, question, request, warning, correction, refusal, invitation, joke, repair, etc.;
- `target_scope` — what part of the world, discourse, or action space is affected;
- `referential_scope` — candidate referents and confidence;
- `temporal_scope` — now, past, future, hypothetical, recurring, unknown;
- `deontic_force` — suggestion, preference, permission, obligation claim, prohibition, unknown;
- `social_function` — coordination, reassurance, challenge, face-saving, play, status negotiation, disclosure, etc.;
- `interaction_context` — current task/mode/relationship/setting variables that are actually observed or admitted;
- `local_convention` — learned interaction-specific mapping, if any;
- `repair_state` — whether an interpretation has been corrected, contradicted, superseded, or remains open;
- `uncertainty_profile` — referential, pragmatic, causal, social, temporal, affective, and action-scope uncertainty separately.

## Context without omniscience

The subsystem must not assume access to hidden mental state. Context is assembled from admissible signals such as:

- current observation;
- prior interaction evidence;
- explicit correction;
- persistent but separately governed learned conventions;
- world state;
- task state;
- known capabilities and constraints;
- uncertainty-bearing social-model hypotheses.

Inferred speaker/listener state remains a hypothesis, not a privileged truth source.

## Correction precedence

A direct correction about intended local meaning should invalidate dependent pragmatic hypotheses before downstream action proceeds.

Recommended transition:

`candidate_interpretation -> correction_received -> dependent_hypotheses_invalidated -> revised_local_model -> downstream_re-evaluation`

The correction updates the relevant local model. It does not automatically become a universal language rule, personality law, or permanent convention.

## Form, function, and consequence

Pragmatics should distinguish:

1. signal form;
2. literal/structural semantic content;
3. interaction function;
4. downstream consequence.

A system that jumps from form directly to consequence risks learning shallow policy shortcuts. A system that freezes at literal semantics risks missing ordinary communicative function.

The runtime should therefore be able to state separately:

`WHAT_WAS_EXPRESSED`

`WHAT_FUNCTION_IT_APPEARS_TO_SERVE`

`WHAT_ACTION_IF_ANY_IS_AUTHORIZED`

The third statement requires its own authority/action gate.

## Local convention lifecycle

Local interaction conventions should have an explicit lifecycle:

- `DISCOVERED_CANDIDATE`
- `NEGOTIATED`
- `ADAPTED_EXISTING_CONVENTION`
- `CONFIRMED_WITHIN_SCOPE`
- `CONTEXT_BOUND`
- `DRIFT_SUSPECTED`
- `REVISED`
- `RETIRED`
- `UNRESOLVED`

Convention persistence should depend on later evidence, not mere absence of contradiction.

## Mode residue

Research, emergency, precision, playful, reflective, diagnostic, and planning modes can alter interpretation priors. Those modes must not silently become permanent personality or global pragmatic policy.

Every temporary mode should carry:

- entry condition;
- scope;
- affected priors;
- expiry/release condition;
- retained learning that may persist after the mode ends;
- state that must not persist.

## Social-model hypotheses

A pragmatic runtime benefits from self/other modeling but must preserve epistemic modesty.

For each socially relevant inference, record:

- evidence basis;
- model target;
- confidence;
- alternative explanations;
- contradiction/correction handling;
- privacy scope;
- action relevance.

`EMPATHIC_INFERENCE != OTHER_PERSON_TRUTH`

`SOCIAL_MODEL != AUTHORITY`

## Pragmatic uncertainty and abstention

When action depends on an unresolved pragmatic fork, the subsystem should surface the fork instead of silently selecting the most convenient interpretation.

Possible outputs:

- `ACTION_SCOPE_CLEAR`
- `INTERPRETATION_CLEAR_ACTION_SCOPE_UNCLEAR`
- `MULTIPLE_PLAUSIBLE_INTERPRETATIONS`
- `CORRECTION_REQUIRED`
- `SAFE_TO_PROCEED_WITH_BOUNDED_ACTION`
- `NO_ACTION_IMPLIED`

## Cross-system interfaces

Pragmatics consumes and emits typed state with:

- `semantics` for content candidates and conservation;
- `cognition` for hypotheses/world model;
- `Empathy` and `sociological behaviors` for social inference;
- `chronology` for event timing and discourse order;
- `current memory storage` for active context;
- `volitions-conations` for internally generated goals without conflating them with external instruction;
- `resolver` for ambiguity/conflict;
- `kinesis` only through explicit action authorization;
- modality systems for prosody, gesture, timing, spatial form, and nonverbal interaction.

## Failure modes

- mind-reading presented as fact;
- treating mention of an action as instruction to act;
- persisting a temporary conversational mode indefinitely;
- overgeneralizing one local convention;
- treating politeness, dominance, affection, humor, or social style as consent/authority;
- interpreting successful coordination as proof of exact semantic equivalence;
- allowing downstream behavior to retroactively justify the interpretation that caused it;
- collapsing local uncertainty into global confusion.

## Evidence boundary

This file specifies reusable runtime structure. It does not claim that any particular social-pragmatic theory is universally correct or that one representation captures all communicative systems.
