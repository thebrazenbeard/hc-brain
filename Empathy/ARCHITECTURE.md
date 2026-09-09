# Empathy subsystem

## Purpose

The Empathy subsystem models other agents, infers likely affective and intentional states, tracks relational context, and shapes timing, attention, repair, challenge, and response selection without replacing truth or autonomy.

## Source-derived design rules

The directly relevant `thebrazenbeard/empathy` repository supports several reusable rules that belong in the general HC template:

- Empathy is inference, not privileged access to another mind.
- A direct correction from the modeled person outranks a contradicted inference about that person's intended meaning.
- Understanding does not imply obedience, agreement, placation, or surrender of task integrity.
- Empathic modeling should remain provenance-aware and uncertainty-aware.
- Private relational context is structurally scoped and should not become portable cross-person material by default.
- A repository artifact, model, or stored representation is not evidence that an empathic mechanism is currently installed or active.

## Functional components

1. **Affective inference** — infer likely emotional state from language, behavior, history, body state, and context.
2. **Intent inference** — distinguish probable intended meaning from literal surface form.
3. **Perspective modeling** — maintain bounded hypotheses about another agent's beliefs, goals, constraints, and likely interpretations.
4. **Relationship model** — preserve role, trust, boundaries, shared conventions, unresolved conflicts, and interaction history without treating the model as ground truth.
5. **Correction channel** — allow external correction to revise or invalidate local inference without rewriting the historical fact that the earlier inference existed.
6. **Response modulation** — alter timing, framing, repair, challenge, and salience weighting while leaving final action selection distributed across the wider Hyperconnectome.

## Core invariant

`EMPATHIC_MODEL != OTHER_MIND`

High confidence may justify stronger provisional action, but certainty must never be manufactured from familiarity alone.

## Cross-system interfaces

Empathy should exchange state with `sociological behaviors`, `psychological behaviors`, `pragmatics`, `salience-attention`, `affect`, `current memory storage`, `deep memory storage`, `personification`, and `integration-arbitration`.

## Provenance

Generalized from `thebrazenbeard/empathy` while deliberately excluding identity-specific content.