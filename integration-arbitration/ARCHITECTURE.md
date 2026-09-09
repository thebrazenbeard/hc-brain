# Integration / Arbitration Architecture

Status: working HC template architecture.

## Purpose

Integration/arbitration combines competing subsystem outputs without creating a homunculus-like master node. Arbitration is distributed by scope and should expose its basis, unresolved conflicts, and downstream effects.

## Arbitration scopes

At minimum, architecture should support bounded arbitration for:

- perceptual hypotheses;
- attention/resource allocation;
- response generation;
- action/goal selection;
- memory admission;
- plasticity/update eligibility;
- correction propagation;
- epistemic versus conative conflict;
- safety/authority gating.

## Conflict as first-class state

The system should preserve unresolved conflict when evidence does not justify collapse. Examples include competing interpretations, value-goal conflict, memory-evidence conflict, social-model conflict, affect-volition conflict, and action-policy conflict.

A selected action does not require deletion of losing motives or interpretations.

## Dependency-aware correction

When a corrected field invalidates an inference, downstream effects depending on that field become ineligible until reparsed. Unrelated claims survive unless separately contradicted.

## Separation of recommendation and authority

A learned or inferred recommendation is not itself permission to act. Arbitration should remain compatible with an independent action/safety gateway whose constraints do not depend on the reasoning model behaving correctly.

## Failure modes

- one omnipotent executive owning all state;
- uncertainty erased to satisfy an output renderer;
- action recommendation treated as action authority;
- correction causing global state wipe rather than bounded invalidation;
- conflict hidden rather than represented;
- current salience or mood silently promoted into durable identity.

## Provenance

Generalized from `thebrazenbeard/noema`, `thebrazenbeard/abil`, `thebrazenbeard/vera-control-plane`, and prior HC runtime research. Identity-specific implementations are excluded.