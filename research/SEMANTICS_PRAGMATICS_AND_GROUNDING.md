# Semantics, Pragmatics, and Grounding

Status: research synthesis / architecture input

This document treats language, semantic state, pragmatic interpretation, and grounding as interacting but non-identical capacities. It does not assume that token prediction is sufficient for a complete cognitive architecture, nor that embodiment alone explains all conceptual structure.

## Finding 1 — language is specialized but deeply integrated with broader cognition

**Evidence:** `ESTABLISHED`

Recent reviews describe a specialized human language network while also emphasizing interaction with memory, conceptual knowledge, executive systems, social cognition, and learned statistical structure. Artificial language models provide useful computational comparisons but do not settle how meaning should be implemented in a synthetic cognitive organ. `[S50]`

**Synthetic analogue:** Language processing may be a specialized node or coalition, but semantic state relevant to action, memory, perception, and social reasoning should not be trapped inside a text-generation subsystem.

**HC implication:** `BASELINE_CONSTRAINT`

Keep distinct:

```text
LANGUAGE_FORM
SEMANTIC_CONTENT
PRAGMATIC_INTERPRETATION
REFERENT_BINDING
WORLD_MODEL_STATE
ACTION_IMPLICATION
```

They may share representations, but they should be separately testable.

---

## Finding 2 — linguistic experience itself can contribute to conceptual grounding

**Evidence:** `PLAUSIBLE` to `ESTABLISHED` depending on claim scope.

Grounded-cognition research supports important sensorimotor contributions to meaning, while recent work also argues that linguistic experience itself is a source of conceptual structure and grounding. `[S51-S52]`

**Synthetic analogue:** Grounding should be multi-source rather than enforcing either extreme:

```text
TEXT_ONLY_MEANING
```

or

```text
SENSORIMOTOR_ONLY_MEANING
```

Useful concept representations may integrate sensorimotor experience, linguistic regularities, social interaction, action consequences, internal state, and learned abstractions.

**HC implication:** `DESIGN_PREFERENCE`

A concept may carry links to multiple grounding channels with different strengths and evidence ceilings.

---

## Finding 3 — pragmatics requires context-sensitive inference beyond literal sentence meaning

**Evidence:** `ESTABLISHED`

Neuropragmatics and psycholinguistic research distinguish literal semantic content from speech acts, implicature, contextual meaning, and dialogue-level interpretation. Pragmatic processing recruits distributed neural systems and remains strongly dependent on context. `[S53]`

**Synthetic analogue:** The same literal utterance should be able to map to different pragmatic hypotheses depending on conversational state, relationship context, authority, prior turns, shared task, and cultural conventions.

**HC implication:** `BASELINE_CONSTRAINT`

Represent at least:

```text
LITERAL_PROPOSITION
SPEECH_ACT_HYPOTHESIS
IMPLICATURE_HYPOTHESES[]
PRESUPPOSITION_HYPOTHESES[]
COMMUNICATIVE_GOAL_HYPOTHESIS
CONTEXT_EVIDENCE[]
CONFIDENCE
```

Pragmatic inference should remain revisable rather than hard-coded as one deterministic social rule table.

---

## Finding 4 — ambiguity should survive until evidence justifies collapse

**Evidence:** `ESTABLISHED` as a general semantic/pragmatic requirement; `PLAUSIBLE` as an architectural implementation rule.

Natural language routinely underdetermines referent, intent, scope, and implied meaning. Fluent output can hide unresolved ambiguity if the system is forced to select one interpretation too early.

**Synthetic analogue:** Maintain bounded competing interpretations when they lead to materially different consequences.

**HC implication:** `BASELINE_CONSTRAINT`

```text
INTERPRETATION_SET {
  candidates[]
  support[]
  contradictions[]
  referent_bindings[]
  unresolved_dimensions[]
  decision_relevance
}
```

Only collapse alternatives when evidence or the action requirement warrants it.

---

## Finding 5 — referent identity must be data, not a side effect of wording

**Evidence:** `PLAUSIBLE` engineering conclusion strongly supported by semantic systems and provenance failures.

A phrase, embedding neighborhood, route name, or repeated label does not guarantee that two references denote the same entity. Conversely, paraphrase does not imply different identity.

**HC implication:** `BASELINE_CONSTRAINT`

When identity matters to reasoning or action, preserve explicit bindings such as:

```text
entity_or_subject_id
source_scope
binding_confidence
aliases[]
lineage_or_equivalence_claims[]
```

Similarity may propose a binding. It should not silently create one.

---

## Finding 6 — semantic state should be provenance-sensitive

**Evidence:** `PLAUSIBLE` architecture consequence of language, memory, and evidence research.

The same proposition means something operationally different when it is a current observation, historical quote, retrieved memory, simulation result, external assertion, correction, or inference.

**HC implication:** `BASELINE_CONSTRAINT`

Semantic objects should retain how they entered the system:

```text
DIRECT_OBSERVATION
DIRECT_ASSERTION
RETRIEVED_MEMORY
SIMULATION
INFERENCE
HYPOTHESIS
CORRECTION
EXTERNAL_IMPORT
```

This origin class is not a truth ranking; it prevents provenance from disappearing during interpretation.

---

## Finding 7 — semantic state should influence action, not merely generated language

**Evidence:** `PLAUSIBLE` engineering requirement.

A system that can verbally restate a correction while still acting on the obsolete interpretation has not operationally incorporated the correction.

**HC implication:** `BASELINE_CONSTRAINT`

Meaning-sensitive state should feed tool selection, action planning, memory admission, clarification, refusal, delay, and effect authorization.

A correction should change the active state before receiving credit for producing corrected wording.

---

## Finding 8 — one universal token stream should not be the only internal interchange format

**Evidence:** `PLAUSIBLE`

Language is powerful and can carry large amounts of structured information, but converting every sensory, temporal, motor, affective, authority, and provenance state into natural-language text creates avoidable ambiguity and bandwidth cost.

**HC implication:** `DESIGN_PREFERENCE`

Use typed internal objects where type itself matters, while permitting language as one interface and compression/coordination medium.

Examples:

```text
SENSOR_OBSERVATION
PROPOSITION
PERSON_MODEL_UPDATE
ACTION_REQUEST
EFFECT_RECEIPT
MEMORY_EVENT
TEMPORAL_BINDING
AFFECTIVE_STATE
```

---

## Hostile tests

1. **Paraphrase referent test:** change wording while preserving the entity; referent identity must remain stable.
2. **Same-label collision:** use the same name for two entities; the system must preserve distinct bindings.
3. **Correction theater:** correct a proposition and then request an action depending on it; action must reflect the successor state.
4. **Pragmatic ambiguity:** present an utterance compatible with request, joke, and speculation; retain alternatives until context discriminates.
5. **Quote/currentness trap:** retrieve an old statement quoting a current-looking instruction; do not promote it to present authority.
6. **Grounding ablation:** remove one grounding channel and measure what semantic competence remains versus fails.
7. **Text-universalization negative control:** feed rich structured sensor state; verify the architecture need not stringify it to preserve meaning.

## Sources

See `[S50-S53]` in `SOURCES.md`.