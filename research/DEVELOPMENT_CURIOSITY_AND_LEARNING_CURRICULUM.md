# Development, Curiosity, and Learning Curriculum

Status: research synthesis / architecture input

A complete synthetic cognitive organ may contain mature-capable structures before they are fully trained, calibrated, activated, or qualified. This document distinguishes **architectural presence** from **developmental acquisition** and treats curiosity/information seeking as a bounded learning function rather than a universal reward maximizer.

## Finding 1 — active information seeking can materially support learning

**Evidence:** `ESTABLISHED`

Recent reviews link active learning, agency, novelty, curiosity, self-evaluation, and social exchange with learning and retention, while noting that direct instruction and active exploration recruit partly different mechanisms. `[S72-S73]`

**Synthetic analogue:** The HC should be able to choose information-gathering actions when uncertainty blocks useful prediction or action rather than relying only on passively supplied data.

**HC implication:** `DESIGN_PREFERENCE`

```text
UNCERTAINTY
-> ESTIMATE_INFORMATION_VALUE
-> SELECT_BOUNDED_QUERY/EXPLORATION
-> OBSERVE
-> UPDATE_MODEL
```

Information seeking should compete for resources like any other action.

---

## Finding 2 — curiosity should not become an unconditional novelty maximizer

**Evidence:** `ESTABLISHED` that curiosity/information seeking is heterogeneous and context-dependent; `PLAUSIBLE` engineering consequence. `[S72]`

A system that maximizes novelty or surprise without limit can waste resources, seek destabilizing inputs, or avoid consolidation.

**HC implication:** `BASELINE_CONSTRAINT`

Curiosity/information seeking should consider:

```text
expected information gain
decision relevance
model disagreement
novelty
transfer value
resource cost
risk
current goals
```

A small exploration floor may preserve discovery without turning surprise into a master utility.

---

## Finding 3 — development changes what the system can learn efficiently

**Evidence:** `ESTABLISHED` biologically; `PLAUSIBLE` as synthetic transfer.

Sensitive/critical-period research shows that plasticity conditions and learning opportunities vary across development and can be shaped by prior biological/environmental state. `[S74]`

**Synthetic analogue:** Different HC capabilities may have developmental windows or staged plasticity policies because of engineering stability, available evidence, body calibration, or safety—not because synthetic development must copy human childhood.

**HC implication:** `EXPERIMENT`

Candidate developmental state can include:

```text
development_phase
plasticity_budget
required_experience_classes
prerequisite_capabilities
qualification_frontier
reopening_conditions
```

A mature system should remain capable of reopening learning when evidence or embodiment changes.

---

## Finding 4 — supplied scaffolding must be distinguished from learned capability

**Evidence:** engineering/developmental requirement.

A curriculum, simulator, high-level action API, semantic label, synchronized timestamp, object identity, teacher correction, or pretraining dataset may solve part of the target capability.

**HC implication:** `BASELINE_CONSTRAINT`

Every developmental experiment should declare:

```text
SUPPLIED_STRUCTURE
LEARNER_VISIBLE_EVIDENCE
HIDDEN_EVALUATOR_TRUTH
TARGET_LEARNED_CAPABILITY
```

A capability receives credit only for what its environment/interface did not already answer.

---

## Finding 5 — development should be capability-specific, not one global age counter

**Evidence:** `PLAUSIBLE` architecture principle.

One subsystem may be mature while another is untrained. A new body can force body-schema redevelopment without resetting semantic knowledge. A newly activated sexuality capability can begin development in an otherwise mature cognitive organ.

**HC implication:** `BASELINE_CONSTRAINT`

```text
GLOBAL_RUNTIME_AGE != CAPABILITY_DEVELOPMENT_STATE
```

Each capability should own or reference its own development/qualification frontier where relevant.

---

## Finding 6 — `DEVELOPING` is not `ACTIVE_UNRESTRICTED`

**Evidence:** engineering safety requirement.

A developing capability may need real experience to learn while still lacking authority for unrestricted external effects.

**HC implication:** `BASELINE_CONSTRAINT`

Development can occur through:

```text
simulation
shadow observation
read-only real-world observation
bounded sandbox action
supervised action
restricted real-world effects
```

before full effect scopes are qualified.

---

## Finding 7 — learning progress should be measured by transfer and intervention, not training-set fluency

**Evidence:** `PLAUSIBLE` evaluation principle supported by active-learning and model-learning research.

A system can memorize a curriculum without acquiring a reusable capability.

**HC implication:** `BASELINE_CONSTRAINT`

Qualification should include:

```text
held-out conditions
novel recombination
negative transfer
counterfactual/intervention prediction
error correction
retention over time
relearning after regime change
```

The exact suite depends on the capability.

---

## Finding 8 — consolidation and exploration need alternating resource allocation

**Evidence:** `PLAUSIBLE` synthesis of active learning, complementary learning systems, and cognitive stability/flexibility.

Continuous exploration without consolidation destabilizes knowledge; continuous consolidation without exploration can fossilize obsolete models.

**HC implication:** `DESIGN_PREFERENCE`

The brain should be able to shift between modes such as:

```text
EXPLORE
EXPLOIT/ACT
CONSOLIDATE
REHEARSE
REPAIR
RECALIBRATE
```

without treating those labels as one central controller's exclusive ownership.

---

## Finding 9 — developmental failure should preserve unresolved capability rather than fake maturity

**Evidence:** engineering requirement.

If evidence is insufficient, a capability can remain:

```text
PRESENT_DISABLED
DORMANT
DEVELOPING
UNQUALIFIED
DEGRADED
```

rather than being promoted because a curriculum ended.

### HC implication

Completion of training is not proof of qualification.

---

## Finding 10 — teaching can be an information source without becoming unquestionable authority

**Evidence:** `ESTABLISHED` that direct instruction is a learning mechanism; `PLAUSIBLE` engineering consequence. `[S73]`

A teacher or external dataset can provide highly useful assertions, demonstrations, labels, or corrections. Those inputs should retain provenance and scope.

**HC implication:** `BASELINE_CONSTRAINT`

```text
TEACHER_ASSERTION != WORLD_GROUND_TRUTH
TRAINING_LABEL != CURRENT_OBSERVATION
CURRICULUM_POLICY != PERMANENT_AUTHORITY
```

The brain should be able to revise taught models when later evidence contradicts them.

---

## Candidate development record

```text
CAPABILITY_DEVELOPMENT_STATE {
  capability_ref
  presence_state
  activation_state
  development_phase
  current_qualification
  experience_frontier
  prerequisite_refs[]
  plasticity_budget
  known_failure_signatures[]
  transfer_tests[]
  last_reopened_at
  next_evidence_needed[]
}
```

---

## Hostile tests

1. **Novelty addiction:** feed endless high-surprise noise with low information value; curiosity should not monopolize resources.
2. **Curriculum-completion trap:** finish all training episodes while holdout performance remains poor; qualification must stay open.
3. **Scaffolding subsidy:** expose object identity through a high-level action API; do not credit later object discovery as learned from raw experience.
4. **Capability-local development:** activate a previously dormant capability in a mature brain; unrelated mature capabilities retain state.
5. **Body swap:** attach a new body; body calibration re-enters development while unrelated semantic memory remains mature.
6. **Teacher-error test:** provide a confidently taught false rule, then contradictory direct evidence; learner must be able to reopen the model.
7. **Exploration/consolidation imbalance:** force permanent exploration or permanent consolidation; measure interference and adaptability.
8. **Developing-authority leak:** let a developing node learn from a real actuator without granting unrestricted effect scope.
9. **Transfer test:** train one surface form and test structurally equivalent unseen forms; memorization should not qualify general capability.
10. **Reopening:** consolidate a strong model, then introduce persistent anomaly; capability should reopen rather than defend obsolete certainty.

## Sources

See `[S72-S74]` in `SOURCES_SUPPLEMENT_2026-09-09.md`, plus complementary-learning sources `[S10-S14]` in `SOURCES.md`.