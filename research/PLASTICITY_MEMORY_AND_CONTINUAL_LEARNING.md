# Plasticity, Memory, and Continual Learning

Status: research synthesis / architecture input

## Finding 1 — one learning system is a poor fit for both rapid episodic capture and slow generalization

**Evidence:** `ESTABLISHED` as a strong computational/neuroscience principle.

Complementary Learning Systems research argues that rapid storage of individual episodes and slow integration of statistical structure create conflicting requirements. Fast learning with overlapping representations risks interference; slower interleaved learning supports integration. `[S10-S14]`

**Synthetic analogue:** Separate at least two learning regimes:

```text
FAST_EPISODIC_ACQUISITION
SLOW_INTEGRATIVE_LEARNING
```

They need not reproduce hippocampus/neocortex anatomy. The transferable principle is different learning rates, representation overlap, replay/integration rules, and interference tolerances.

**HC implication:** `BASELINE_CONSTRAINT`

Do not use one uniform learning rate or one undifferentiated memory store for every type of learning.

---

## Finding 2 — replay/interleaving is a strong strategy for reducing interference

**Evidence:** `ESTABLISHED` within complementary-learning-system theory and supported by a large body of memory research. `[S10-S13]`

**Synthetic analogue:** Newly acquired episodes may be replayed or sampled alongside older representative memories during slow integration.

**HC implication:** `DESIGN_PREFERENCE`

A consolidation service should be able to:

- sample recent episodes;
- sample older representative material;
- detect contradiction/interference;
- update slow models incrementally;
- retain provenance linking integrated knowledge back to source episodes.

Replay is not proof that the replayed event is currently true; it is a learning operation.

---

## Finding 3 — memories are not necessarily immutable after storage

**Evidence:** `ESTABLISHED` that reactivated memories can enter labile states under some conditions; boundary conditions remain important. `[S15]`

**Synthetic analogue:** Retrieval and modification must be separate operations even if some retrieval pathways can produce reconsolidation candidates.

**HC implication:** `BASELINE_CONSTRAINT`

Use explicit state transitions such as:

```text
STORED
-> RETRIEVED
-> RECONSOLIDATION_ELIGIBLE
-> MODIFIED_CANDIDATE
-> VALIDATED_SUCCESSOR
```

not an invisible in-place rewrite.

---

## Finding 4 — correction should preserve history

**Evidence:** `PLAUSIBLE` engineering consequence of reconsolidation/provenance requirements.

A system that simply overwrites an old memory loses the ability to distinguish “what happened,” “what was believed then,” and “what was corrected later.”

**HC implication:** `BASELINE_CONSTRAINT`

Prefer successor records with correction links:

```text
old_record
-> correction_evidence
-> successor_record
```

The older record can be marked superseded without being deleted from historical provenance.

---

## Finding 5 — metaplasticity is required for stable long-term learning

**Evidence:** `ESTABLISHED` biologically. `[S06]`

Plasticity mechanisms themselves adapt based on prior activity, helping prevent saturation and runaway modification.

**Synthetic analogue:** Learning rules should expose stability state and change thresholds.

**HC implication:** `BASELINE_CONSTRAINT`

A node that may modify durable state should expose at least:

```text
update_scope
learning_rate_state
recent_update_load
eligibility_state
stability_margin
rollback_or_successor_rule
```

---

## Finding 6 — memory classes should have different admission rules

**Evidence:** `PLAUSIBLE`, strongly supported by distinct biological memory systems and computational tradeoffs.

**HC implication:** `DESIGN_PREFERENCE`

Candidate memory classes:

- `WORKING_CONTEXT` — fast, volatile, capacity-limited;
- `EPISODIC` — event-specific, provenance-rich, rapid append;
- `SEMANTIC` — generalized, slowly integrated;
- `PROCEDURAL` — skill/action policy with performance validation;
- `AUTOBIOGRAPHICAL` — event + self/context continuity, provenance-critical;
- `BODY_CALIBRATION` — sensorimotor mappings and baselines;
- `CONNECTOME_STATE` — routing/plasticity topology checkpoints.

One write permission should not imply permission across all classes.

---

## Finding 7 — catastrophic forgetting is an architecture problem, not merely a training bug

**Evidence:** `ESTABLISHED` that sequential learning can interfere destructively in neural networks; `PLAUSIBLE` that complementary learning/replay is an appropriate general mitigation pattern. `[S10-S14]`

**HC implication:** `BASELINE_CONSTRAINT`

Any lifelong-learning path should be tested for:

- retention of old skills;
- retention of old semantic knowledge;
- interference with autobiographical memory;
- cross-domain negative transfer;
- rollback/supersession behavior;
- stability after repeated updates.

A system that learns new material but unpredictably destroys old competence is not qualified for unrestricted continual learning.

---

## Finding 8 — imported knowledge is not lived experience

**Evidence:** `SPECULATIVE` as identity architecture, but a necessary provenance distinction.

A model/knowledge import can add semantic content without establishing that an embodied event occurred to the instantiated system.

**HC implication:** `BASELINE_CONSTRAINT`

Memory provenance should distinguish at minimum:

```text
DIRECT_EXPERIENCE
INTERNAL_INFERENCE
EXTERNAL_KNOWLEDGE_IMPORT
SUPERVISED_TRAINING
SIMULATION
REPLAY
CORRECTION
MAINTENANCE
```

---

## Suggested consolidation pipeline

```text
experience / import / training event
-> classify source + memory candidate type
-> rapid store where appropriate
-> interference check
-> replay/interleave candidate
-> slow integration
-> validation
-> provenance-preserving successor links
-> release temporary learning context
```

The pipeline is conceptual; different memory classes may skip stages.

---

## Hostile tests

1. **One-shot semantic corruption:** inject one anomalous episode; slow semantic state should not universalize it automatically.
2. **Catastrophic forgetting:** train a new skill after old skills stabilize; measure old-skill degradation.
3. **Replay provenance:** replay an old event; ensure it is not re-dated as a new lived event.
4. **Correction chain:** correct a false memory claim; verify historical record remains inspectable and successor is current.
5. **Reconsolidation guard:** retrieval alone should not silently mutate durable memory.
6. **Cross-class write:** give a procedural learner access to skill updates; verify it cannot rewrite autobiographical history.
7. **Plasticity saturation:** repeated high-intensity learning must trigger stability mechanisms rather than unlimited update magnitude.

## Sources

See `[S06]` and `[S10-S15]` in `SOURCES.md`.
