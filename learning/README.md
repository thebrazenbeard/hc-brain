# Learning and Development

Status: CROSS-CUTTING COGNITIVE SYSTEM / DESIGN

## Purpose

`learning/` coordinates how experience, instruction, observation, simulation, feedback, and practice generate candidate changes to knowledge, skills, models, preferences, calibration, routing, and other plastic state.

Learning proposes durable change; `plasticity/` and subsystem-specific admission policies govern how that change is physically/logically realized and stabilized.

## Learning modes

The template should support multiple learning regimes rather than one universal update rule:

- supervised/instructional;
- self-supervised/predictive;
- reinforcement/credit assignment;
- episodic capture;
- semantic generalization;
- imitation/social learning;
- procedural practice;
- active experimentation;
- counterfactual/simulation learning;
- calibration/body learning;
- shadow/observe-only development.

## Developmental progression

A latent subsystem may move:

```text
PRESENT_DISABLED
→ DORMANT
→ DEVELOPING
→ ACTIVE
```

while its learned competence evolves separately from architectural presence.

## Evidence boundary

A training event, demonstration, or reward is evidence/input to a learning process. It is not automatically semantic truth, personal value, consent, or action authority.

## Shadow learning

For high-risk new capabilities, support:

```text
OBSERVE_ONLY
→ SHADOW_PREDICTION
→ offline/replay evaluation
→ bounded supervised use
→ qualified active use
```

This mirrors evidence from adaptive-system design where prediction can be validated before write authority is granted.

## Credit assignment

Credit/blame signals should preserve uncertainty about causal contribution. Correlated co-activation alone should not always strengthen every participating pathway.

## Negative transfer

Learning should be tested for inappropriate generalization:

- context-specific social behavior leaking into unrelated tasks;
- one body's calibration applied to another body;
- one relationship convention generalized to all agents;
- reward shaping eroding refusal/authority boundaries;
- stylistic success overriding truthfulness;
- domain procedure applied outside qualified regime.

## Reversibility

New learning may be provisional, decaying, versioned, or revertible before consolidation.

## Failure modes

- reward becomes truth;
- repeated exposure becomes consent;
- training performance treated as deployed competence;
- one experience overgeneralized;
- no protected invariants/homeostatic brakes;
- learning silently mutates current identity-critical state.
