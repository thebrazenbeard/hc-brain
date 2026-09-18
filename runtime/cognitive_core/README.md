# HC Cognitive Core

Status: reference implementation / integrated cognitive slice.

This package is the first executable cross-system cognition layer above the HC invariant/reference kernel.

It is deliberately not a language model wrapper, not a complete cognitive organ, and not a consciousness implementation.

## Implemented loop

The primary path is:

`observation -> semantic interpretation -> salience/attention -> transient coalition -> current memory -> optional memory/action/plasticity/self-model candidates`

The implementation composes `runtime/reference_kernel/hc_kernel.py` so evidence, memory, routing, authority, and effect boundaries remain shared with the hardened kernel.

## Implemented subsystem interactions

The current slice materially exercises:

- cognition;
- semantics;
- salience/attention;
- current memory;
- explicit deep-memory admission;
- affect modulation and decay;
- volition/conation concern state;
- self-model candidate/admission separation;
- distributed coalition formation and expiry;
- integration/arbitration;
- typed routing;
- plasticity proposal and explicit consolidation;
- developmental capability state.

## Preserved invariants

`OBSERVATION != INTERPRETATION`

`SALIENCE != TRUTH`

`WANTING_X != EVIDENCE_THAT_X_IS_TRUE`

`ACTION_CANDIDATE != ACTION_AUTHORIZATION`

`MEMORY_CANDIDATE != DEEP_MEMORY_ADMISSION`

`SELF_MODEL_CANDIDATE != IDENTITY_MUTATION`

`ROUTE_USED_NOW != ROUTE_LEARNED_FOR_FUTURE`

`CAPABILITY_PRESENCE != DEVELOPMENTAL_MATURITY`

Temporary coalitions have bounded lifetime. Affect changes scheduling/valuation pressure without changing evidence confidence. Repeated routing creates a plasticity candidate but does not alter durable routing until an explicit basis-bearing commit occurs.

## Semantic ambiguity

`process_competing_interpretations` preserves competing inferred meanings when the confidence margin is insufficient. It does not manufacture certainty for downstream convenience.

A clear winner can be selected for the current scope while remaining `INFERRED`, not `OBSERVATION` or canonical truth.

## Development

Relevant capabilities begin as:

`presence=PRESENT`

`activation=DEVELOPING`

`maturity=LEARNING`

`health=NOMINAL`

Explicit qualification evidence can move a capability to `ACTIVE / STABLE_WITHIN_SCOPE`. The transition and basis remain in local history.

## Test surface

`test_cognitive_loop.py` currently covers the integrated loop, epistemic/conative separation, authority separation, coalition expiry, memory/identity admission gates, plasticity consolidation, affect decay, concern lifecycle, semantic ambiguity, and developmental qualification state.

## Claim ceiling

This package demonstrates executable interaction among a subset of HC cognitive contracts.

It does not establish:

- complete cognition;
- autonomous open-world competence;
- complete deep-memory consolidation/retrieval;
- full world modelling or planning;
- empathy/social cognition;
- embodiment;
- general intelligence;
- consciousness or phenomenal experience;
- biological equivalence.
