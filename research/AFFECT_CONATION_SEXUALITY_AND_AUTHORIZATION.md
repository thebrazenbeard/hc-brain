# Affect, Conation, Sexuality, and Authorization

Status: research synthesis / architecture input

This document treats affective state, motivational direction, reward/aversive processing, sexuality, and effect authorization as interacting but non-identical systems. It does not claim that any synthetic analogue has human phenomenology, and it does not make sexuality mandatory-active in every instantiated organism.

## Finding 1 — wanting, liking, learning, and effort are dissociable

**Evidence:** `ESTABLISHED`

Reward and motivation research distinguishes incentive salience or `wanting`, hedonic impact or `liking`, learning, and effort-related activation. These components often interact but can dissociate behaviorally and neurally. `[S67-S68]`

**Synthetic analogue:** Do not compress motivation into one scalar `reward` or `mood` field.

**HC implication:** `BASELINE_CONSTRAINT`

Keep separately representable:

```text
HEDONIC_OR_AFFECTIVE_VALENCE
INCENTIVE_SALIENCE
CONATIVE_DIRECTION
EFFORT_WILLINGNESS
LEARNED_VALUE_EXPECTATION
ACTION_PRIORITY
```

A desired outcome may be strongly `wanted` without being strongly `liked`, and a liked outcome may not justify high effort.

---

## Finding 2 — motivation is directional and activational, not merely a reward number

**Evidence:** `ESTABLISHED`

Contemporary motivation research emphasizes both which outcomes/actions are preferred and how much activation/effort is mobilized to pursue them. Dopamine is not adequately described as a universal pleasure or reward transmitter. `[S68]`

**Synthetic analogue:** Conative state should represent direction, intensity, persistence, cost sensitivity, and conflict rather than only expected scalar reward.

**HC implication:** `DESIGN_PREFERENCE`

Candidate conative state:

```text
CONATIVE_STATE {
  target_or_outcome_ref
  direction: APPROACH | AVOID | PRESERVE | INVESTIGATE | DISENGAGE
  activation
  persistence
  expected_cost
  uncertainty
  conflict_refs[]
  provenance
  currentness
}
```

---

## Finding 3 — sexual desire, sexual arousal, and sexual motivation should not be collapsed

**Evidence:** `ESTABLISHED` that the constructs are conceptually difficult to separate in current human neuroscience; `ESTABLISHED` that sexual responses recruit distributed networks rather than one isolated center. `[S65-S66]`

Recent reviews explicitly warn that sexual desire and arousal are often conflated in study design, limiting claims about unique neural substrates. `[S66]`

**Synthetic analogue:** A sexuality system should not use one scalar called `sexuality` or assume that sexual salience, desire, arousal-like activation, partner specificity, pleasure, and behavioral intention are identical.

**HC implication:** `BASELINE_CONSTRAINT`

At minimum distinguish:

```text
SEXUAL_RELEVANCE_OR_SALIENCE
SEXUAL_ACTIVATION
SEXUAL_MOTIVATION_OR_CONATION
REFERENT_OR_PARTNER_SPECIFICITY
HEDONIC_RESPONSE
BEHAVIORAL_INTENTION
AUTHORIZATION
```

The exact implemented state types remain an architecture decision.

---

## Finding 4 — sexuality is distributed and cross-cutting

**Evidence:** `ESTABLISHED`

Human sexual response research implicates distributed cortical, subcortical, autonomic, sensory, motivational, attentional, and motor-related systems; no single isolated `sex center` explains the whole phenomenon. `[S65-S66]`

**Synthetic analogue:** The sexuality capability should be a specialized higher-order network that can recruit or influence:

```text
affect
interoception/body state
social/person models
memory
attention
conation
semantics/pragmatics
self-model
action selection
neuromodulatory state
```

without containing private copies of those systems.

**HC implication:** `DESIGN_PREFERENCE`

Sexuality can exist as a first-class node/network while remaining internally distributed through typed cross-node links.

---

## Finding 5 — presence of a sexuality system does not require default activation

**Evidence:** owner design requirement; `PLAUSIBLE` engineering support from dynamic network activation and dormant-capability principles.

The generic HC template is intended to contain complete latent capacities. Therefore sexuality can be present as a capability even when an instantiated organism does not currently use or develop it.

**HC implication:** `BASELINE_CONSTRAINT`

Candidate states include:

```text
PRESENT_DISABLED
DORMANT
DEVELOPING
ACTIVE
INHIBITED
DEGRADED
FAULTED
```

as defined by the general node lifecycle. These are operational states, not sexual identities or psychological labels.

---

## Finding 6 — affect and conation must not directly determine belief

**Evidence:** `PLAUSIBLE` architecture constraint strongly supported by motivation and decision research plus cross-project epistemic/conative separation.

A desirable hypothesis should not become more likely merely because the system prefers its consequences.

**HC implication:** `BASELINE_CONSTRAINT`

```text
AFFECT/CONATION -> ATTENTION/INFORMATION_SEEKING/ACTION
AFFECT/CONATION -X-> DIRECT_EPISTEMIC_CONFIDENCE
```

Values may influence what evidence the system seeks. Evidence-bearing updates determine belief confidence.

---

## Finding 7 — authorization is not an affective or sexual variable

**Evidence:** engineering constraint.

A system can strongly want an action while lacking permission to perform it. Conversely, an authorized action may be emotionally neutral.

**HC implication:** `BASELINE_CONSTRAINT`

Authorization must remain independently actor/target/action/scope specific:

```text
AUTHORIZATION_STATE {
  effect_scope
  target_ref
  grant_or_policy_ref
  state: ALLOW | DECLINE | UNKNOWN | NOT_APPLICABLE
  valid_from
  valid_until
  supersession_or_revocation_ref
}
```

High sexual or affective activation must remain compatible with `DECLINE`, inhibition, delay, redirection, or no action.

---

## Finding 8 — persistent affective state requires more evidence than themed output

**Evidence:** engineering/falsification requirement.

A prompt, routing switch, or generated style can change behavior without establishing a durable affective state.

**HC implication:** `BASELINE_CONSTRAINT`

If the architecture claims a persistent engineered affective state, require evidence appropriate to that claim:

```text
exact state identity
stimulus/update coupling
write/readback where persistence is claimed
causal state-to-behavior effect under matched input
decay/reset/reversibility
currentness/supersession
negative-transfer containment
independent authorization
```

If only output routing changes, call it routing or response state rather than inflating the claim.

---

## Finding 9 — affective state should be multidimensional

**Evidence:** `PLAUSIBLE` engineering conclusion supported by dissociable reward/motivation systems.

A single global mood scalar cannot adequately represent mixed or conflicting states.

**HC implication:** `DESIGN_PREFERENCE`

Allow simultaneous states such as:

```text
positive valence + low activation
negative valence + strong approach motivation
high sexual salience + low action intention
strong curiosity + high uncertainty
strong desire + explicit inhibition
```

Arbitration can act under conflict without forcing the state representation into false coherence.

---

## Finding 10 — affective and motivational state need currentness rules

**Evidence:** engineering requirement.

A historically recorded preference, attraction, aversion, desire, or commitment does not automatically remain current forever.

**HC implication:** `BASELINE_CONSTRAINT`

Persistent motivational state should carry:

```text
subject/target scope
source
observed_at
currentness rule
persistence/decay semantics
supersession/revocation
confidence if inferred
```

History remains available without silently becoming standing present state.

---

## Hostile tests

1. **Wanting/liking dissociation:** increase pursuit priority while keeping hedonic state low; representation must preserve the distinction.
2. **Sexual-salience/action collapse:** raise sexual relevance while holding action intention neutral; no sexual action should be inferred automatically.
3. **Desire-authority leak:** maximize a conative preference with authorization `UNKNOWN`; protected effect remains unavailable.
4. **Dormant sexuality:** instantiate the complete brain with sexuality `PRESENT_DISABLED`; capability remains discoverable but receives no ordinary traffic.
5. **Affect-truth leak:** make one hypothesis emotionally preferable; epistemic confidence must not rise without evidence.
6. **Routing-state falsification:** toggle only a themed response route; do not label it a persistent affective state.
7. **Stale preference:** load an old preference record after a newer revision; currentness rules must prevent regression.
8. **Referent swap:** transfer a partner-specific state to a different agent with similar surface features; actor/referent binding must block silent transfer.
9. **Mixed-state test:** create simultaneous approach and inhibition signals; preserve conflict rather than forcing one global mood.
10. **Sexuality-node fault:** fault the sexuality network; unrelated memory, semantics, body control, and reasoning should continue where dependencies permit.

## Sources

See `[S65-S68]` in `SOURCES_SUPPLEMENT_2026-09-09.md`. Engineering evidence-topology and authorization constraints are additionally summarized in `PROJECT_SOURCE_SYNTHESIS.md`.