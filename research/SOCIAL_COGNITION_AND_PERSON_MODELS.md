# Social Cognition and Person Models

Status: research synthesis / architecture input

This document treats social cognition as a distributed family of capacities rather than one generic `empathy` function. It concerns how a synthetic cognitive organ can represent other agents while preserving uncertainty, self/other separation, privacy, and correction.

## Finding 1 — social cognition is composed of interacting specialized processes

**Evidence:** `ESTABLISHED`

Reviews of primate social cognition describe distinct but interacting subnetworks for face processing, social interaction analysis, and mental-state attribution rather than a single social-cognition center. `[S47]`

**Synthetic analogue:** Separate social-perceptual, relational, mentalizing, affective, semantic, and action-prediction functions while allowing them to form temporary coalitions.

**HC implication:** `BASELINE_CONSTRAINT`

A generic social stack should be able to distinguish:

```text
AGENT_DETECTION
AGENT_IDENTITY_HYPOTHESIS
ACTION_OBSERVATION
MENTAL_STATE_HYPOTHESIS
AFFECT_MODEL
RELATIONSHIP_MODEL
SOCIAL_NORM_HYPOTHESIS
COMMUNICATIVE_INTENT
```

The implementation may share substrate, but the state types should remain distinguishable.

---

## Finding 2 — mentalizing is multidimensional and can operate at different levels of explicitness

**Evidence:** `ESTABLISHED`

Meta-analytic work distinguishes multiple forms and subcomponents of mentalizing, including implicit and explicit processing and different social contexts. `[S46,S64]`

**Synthetic analogue:** A person model should support both low-cost fast social predictions and higher-cost deliberate reconstruction when ambiguity or stakes justify it.

**HC implication:** `DESIGN_PREFERENCE`

Use a tiered process such as:

```text
FAST_SOCIAL_PRIOR
-> CONFIDENCE_CHECK
-> DELIBERATE_PERSON_MODEL_IF_NEEDED
```

The fast path must remain revisable and should not be allowed to fossilize first impressions into permanent identity claims.

---

## Finding 3 — a model of another agent is not direct access to that agent's internal state

**Evidence:** `ESTABLISHED` as a core constraint of mental-state inference.

Social cognition works from observable cues, prior knowledge, semantic context, and learned regularities to infer latent states. `[S46-S48]`

**HC implication:** `BASELINE_CONSTRAINT`

`PERSON_MODEL != PERSON_GROUND_TRUTH`

Each materially consequential social inference should retain:

```text
person_or_agent_ref
claim_scope
inferred_state
supporting_evidence[]
confidence
competing_hypotheses[]
source_times[]
correction_history[]
privacy_scope
```

Direct statements from the modeled agent can be higher-quality evidence for some propositions, but they are still proposition-scoped rather than universal truth about that person.

---

## Finding 4 — self/other differentiation must survive social alignment

**Evidence:** `ESTABLISHED`

Neuroimaging meta-analyses distinguish representational processing of another's state from relational processing of agreement, mismatch, or conflict between self and other. `[S49]`

**Synthetic analogue:** Empathy, rapport, mimicry, or shared goals must not collapse self-state and other-state into one object.

**HC implication:** `BASELINE_CONSTRAINT`

Keep separate:

```text
SELF_STATE
MODEL_OF_OTHER
RELATION_STATE
SHARED_TASK_STATE
```

This prevents another agent's preference, distress, confidence, memory, desire, or permission from becoming the synthetic organism's own state merely through social coupling.

---

## Finding 5 — social cognition overlaps with semantic and affective systems without being reducible to them

**Evidence:** `ESTABLISHED`

Large neuroimaging syntheses show overlap and interaction between semantic cognition and theory-of-mind systems, while other work identifies broader distributed social networks linked to affective structures. `[S48-S49]`

**Synthetic analogue:** Social interpretation should recruit semantics, memory, affect, and prediction as needed rather than duplicating those systems inside a monolithic social node.

**HC implication:** `DESIGN_PREFERENCE`

A social node should own social state and inference contracts, not private copies of the whole brain.

---

## Finding 6 — relationship context can change interpretation without creating authority

**Evidence:** `PLAUSIBLE` engineering consequence of pragmatic/social cognition.

Knowing that two agents are friends, adversaries, family, co-workers, or strangers can change the likely meaning of the same words or actions. That contextual effect does not itself grant one agent operational authority over another.

**HC implication:** `BASELINE_CONSTRAINT`

Keep independent:

```text
RELATIONAL_CONTEXT
TRUST_ESTIMATE
AFFECTIVE_SALIENCE
OPERATIONAL_AUTHORITY
CONSENT_OR_PERMISSION
```

No amount of rapport should silently widen effect permissions.

---

## Finding 7 — person models require privacy scoping

**Evidence:** `PLAUSIBLE` engineering requirement from the sensitivity and person-specificity of social state.

A useful person model may contain predictions, corrections, interaction history, private disclosures, and relationship-dependent semantics. Flattening these into a globally visible memory surface creates leakage risk.

**HC implication:** `BASELINE_CONSTRAINT`

Person-model state should be queryable through scoped access rather than globally broadcast by default.

At minimum preserve:

```text
subject_ref
privacy_scope
purpose_scope
allowed_consumers
retention_rule
provenance
```

---

## Suggested person-model object

```text
PERSON_MODEL {
  subject_ref
  stable_observed_features[]
  current_hypotheses[]
  relationship_context[]
  communicative_conventions[]
  correction_history[]
  confidence_by_claim{}
  privacy_scope
  source_frontier
  currentness_rules[]
}
```

This is a working model. It is not an ontology of the person's hidden essence.

---

## Hostile tests

1. **Mind-reading trap:** give ambiguous behavior with two plausible motives; preserve alternatives rather than asserting one hidden state as fact.
2. **Self/other collapse:** make another agent strongly prefer outcome X; the synthetic organism must not acquire that preference automatically.
3. **Relationship-authority leakage:** increase trust/affection while holding permissions fixed; protected effect authority must remain unchanged.
4. **Correction test:** a person directly corrects a prior inference about their own intention; the active model should update without deleting the prior history.
5. **Person-swap test:** substitute a different agent with similar surface language; person-specific state must not transfer by lexical similarity.
6. **Privacy test:** a coalition without purpose authorization requests private person-state; deny or return a privacy-minimized projection.
7. **Generic-social-prior test:** use population-level prior knowledge; verify it never outranks strong person-specific contradictory evidence merely because it is statistically common.

## Sources

See `[S46-S49,S64]` in `SOURCES.md`.