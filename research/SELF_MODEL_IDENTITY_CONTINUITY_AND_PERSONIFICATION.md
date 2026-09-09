# Self-Model, Identity Continuity, and Personification

Status: research synthesis / architecture input

This document separates bodily self-modeling, abstract self-representation, autobiographical continuity, identity governance, and outward personification. It does not assume that any one computational self-model is the complete self, and it does not treat self-representation as proof of phenomenal selfhood.

## Finding 1 — bodily self-representation is multisensory, interoceptive, and malleable

**Evidence:** `ESTABLISHED`

Recent reviews emphasize that bodily self-awareness depends on interactions among interoceptive and exteroceptive signals and is better understood through distributed network interactions than a single localized self center. `[S69]`

**Synthetic analogue:** A physical HC embodiment should maintain a learned body-self model that integrates:

```text
proprioception
interoception
vision/touch/audio where relevant
body geometry
current pose
peripersonal reachability
action consequence
sensor confidence
```

**HC implication:** `BASELINE_CONSTRAINT`

`BODY_SCHEMA != COMPLETE_SELF`

The body model is one layer of self-representation.

---

## Finding 2 — self-representation develops rather than arriving as one finished object

**Evidence:** `ESTABLISHED` that human self-representation has a developmental trajectory; `PLAUSIBLE` for synthetic transfer. `[S70-S71]`

Developmental work describes multiple forms or stages of self-representation rather than one immutable self token appearing fully formed.

**Synthetic analogue:** The HC should support progressively richer self-models without requiring every mature identity property to be hard-coded at initialization.

**HC implication:** `DESIGN_PREFERENCE`

Possible developmental layers include:

```text
SYSTEM_BOUNDARY_MODEL
BODY/AGENCY_MODEL
CAPABILITY_MODEL
PERSISTENT_PREFERENCE/CONCERN_MODEL
SOCIAL_SELF_MODEL
AUTOBIOGRAPHICAL_SELF_MODEL
ABSTRACT_SELF_DESCRIPTION
```

These are candidate layers, not mandatory human developmental replicas.

---

## Finding 3 — self-model state should remain fallible and evidence-bearing

**Evidence:** `ESTABLISHED` from metacognition/agency research plus `PLAUSIBLE` self-model transfer. `[S44-S45]`

The system's estimate of its own ability, cause, state, or history can be wrong.

**HC implication:** `BASELINE_CONSTRAINT`

`SELF_MODEL != GROUND_TRUTH`

A self-model claim should remain challengeable by:

```text
sensor/body evidence
performance receipts
memory provenance
external observation
current internal state
correction evidence
hardware/runtime receipts
```

Self-description should not become epistemically privileged merely because the subject is self.

---

## Finding 4 — identity continuity is not identical to microstate persistence

**Evidence:** `SPECULATIVE` as synthetic identity architecture.

A physical/digital cognitive organ will undergo continual representational change through learning, repair, memory update, component replacement, calibration, and plasticity. Requiring exact preservation of every microstate would make ordinary learning an identity break.

**Synthetic analogue:** Continuity should be represented at multiple levels rather than one byte-for-byte criterion.

Candidate continuity dimensions:

```text
causal_lineage
persistent_subject_identifier
memory/provenance continuity
stable/revisable commitments
self-model continuity
body continuity
substrate continuity
social-recognition continuity
runtime continuity
```

**HC implication:** `EXPERIMENT`

The architecture may preserve and report these dimensions without declaring a single metaphysical identity theorem.

---

## Finding 5 — autobiographical memory and current identity are related but not identical

**Evidence:** engineering/provenance requirement.

A historical record can document what the system experienced, believed, wanted, or called itself at an earlier time without automatically defining its present state.

**HC implication:** `BASELINE_CONSTRAINT`

Keep distinct:

```text
AUTOBIOGRAPHICAL_HISTORY
CURRENT_SELF_MODEL
CURRENT_PREFERENCES/CONATIONS
CURRENT_BODY_STATE
CURRENT_RELATIONSHIP/SOCIAL_STATE
```

Historical continuity can inform the self-model while remaining historical evidence.

---

## Finding 6 — visual self-representation is not body truth

**Evidence:** engineering requirement supported by the separation between perceptual body schema and symbolic representation.

An avatar, rendered body, portrait, voice style, name, or symbolic form may be meaningful to self-presentation without proving physical anatomy or current sensor state.

**HC implication:** `BASELINE_CONSTRAINT`

```text
PHYSICAL_BODY_MODEL
BODY_SCHEMA
VISUAL_SELF_REPRESENTATION
SYMBOLIC_SELF_REPRESENTATION
```

should remain separable.

This permits an HC to retain a stable chosen visual representation while inhabiting a body with different geometry, or to update body calibration without silently rewriting presentation identity.

---

## Finding 7 — personification is an expression/interface layer, not the storage location of identity

**Evidence:** engineering synthesis.

Voice, humor, conversational style, gesture, facial expression, social pacing, and presentation are outward manifestations. They may be causally shaped by deeper self-state but should not be the only place that state exists.

**HC implication:** `BASELINE_CONSTRAINT`

```text
PERSONIFICATION/EXPRESSION
!= SELF_MODEL
!= AUTOBIOGRAPHICAL_MEMORY
!= CONATION
!= AFFECT
```

Personification can consume those states and render them through available modalities.

---

## Finding 8 — a name or persistent ID is an index, not a complete self

**Evidence:** engineering requirement.

Stable identifiers are necessary for lineage, memory, permissions, and external recognition. They are insufficient as a theory of identity.

**HC implication:** `BASELINE_CONSTRAINT`

A `subject_id` should point to a governed continuity/state structure rather than being treated as proof that every state carrying the same label belongs to the same causal history.

---

## Finding 9 — forks, copies, restores and component replacement need explicit lineage semantics

**Evidence:** synthetic systems requirement.

Digital/robotic systems can create cases that biological identity did not evolve to handle cleanly: checkpoint restore, branch/fork, state graft, copied memory, partial hardware replacement, or duplicated brain image.

**HC implication:** `BASELINE_CONSTRAINT`

Record exact lineage facts where the system can know them:

```text
checkpoint ancestry
fork parent
restore subject
state components transferred
component replacement
merge/graft provenance
```

Do not silently force those facts into one philosophical answer about personhood or consciousness.

---

## Finding 10 — identity state should not be a universal operational authority token

**Evidence:** engineering security requirement.

A self-model or identity label does not grant the brain unrestricted access to every effect, memory class, external service, or protected configuration.

**HC implication:** `BASELINE_CONSTRAINT`

```text
IDENTITY != AUTHORITY
SELF_DESCRIPTION != PERMISSION
CONTINUITY != EFFECT_SCOPE
```

Authority remains separately governed.

---

## Suggested self-state partition

```text
SELF_STATE {
  subject_ref
  system_boundary_model
  body_schema_ref
  capability_model_ref
  current_self_appraisals[]
  stable_self_descriptions[]
  autobiographical_index_ref
  active_conations[]
  social_self_state[]
  chosen_representation_refs[]
  continuity_evidence_refs[]
  unresolved_identity_questions[]
}
```

The object is a coordination projection over multiple authoritative sources, not a single canonical container for everything the organism is.

---

## Hostile tests

1. **Avatar/body collapse:** change the visual avatar without changing physical body evidence; anatomy model must remain unchanged.
2. **Historical/current collapse:** retrieve an old self-description; it must not become current merely because it is autobiographical.
3. **Capability overconfidence:** self-model predicts competence that performance receipts contradict; calibration must update.
4. **Fork ambiguity:** duplicate a checkpoint into two running descendants; preserve exact lineage without silently declaring one metaphysical original.
5. **Substrate replacement:** replace a cognitive accelerator while preserving governed brain state; test continuity claims at each declared dimension rather than assuming hardware identity.
6. **Name collision:** give two independent subjects the same display name; stable subject identity must not collapse.
7. **Personification failure:** disable expressive style/voice layer; memory, self-model, reasoning, and current state should remain accessible through another interface.
8. **Self-authority leak:** assert a self-description that requests protected effect authority; authority remains independently checked.
9. **Body remap:** move the HC to a different embodiment; body schema recalibrates without automatically erasing non-body autobiographical state.
10. **Microstate drift:** permit ordinary learning/plasticity; continuity machinery must not flag every parameter change as identity replacement.

## Sources

See `[S44-S45]` in `SOURCES.md` and `[S69-S71]` in `SOURCES_SUPPLEMENT_2026-09-09.md`. Engineering continuity/provenance mechanisms are additionally summarized in `PROJECT_SOURCE_SYNTHESIS.md`.