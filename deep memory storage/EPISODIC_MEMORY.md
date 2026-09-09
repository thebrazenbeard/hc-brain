# Episodic Memory

Status: RECONCILIATION CANDIDATE / NOT CANON / NOT IMPLEMENTED

Source provenance: remapped from PR #4 `memory/episodic/README.md` into canonical `deep memory storage/`.

## Purpose

Store provenance-rich traces of specific events/episodes with enough temporal and contextual identity to distinguish one occurrence from another.

The fast-capture design is inspired by complementary-learning research; it does not require biological hippocampal anatomy.

## Episodic trace

A trace should be able to preserve:

- stable event/episode identity;
- observed time or bounded interval plus recorded time;
- represented participants/entities and context;
- event/proposition payload;
- evidence/source refs;
- confidence/uncertainty;
- privacy/access scope;
- encoding/admission state;
- correction/supersession links;
- salience/novelty metadata where used;
- integrity digest where relevant.

## Admission

```text
observation/event
→ episodic candidate
→ provenance/privacy/relevance gate
→ admitted episodic trace | reject | defer | unresolved
```

Not every observation becomes a durable episode.

## Historical fidelity

Later correction may change the supported interpretation without destructively rewriting what was recorded or believed at the time.

```text
original trace
→ later correction/reinterpretation
→ current reading rule
```

## Replay

Replay may support retrieval, planning, prediction, semantic generalization, procedural learning, self/social-model update, or reconciliation. Replay does not create currentness or automatic consolidation authority.

## Event identity

Similar events must not be silently merged merely because semantic content overlaps. Episode identity and provenance survive similarity-based retrieval.

## Failure modes

- inferred/reconstructed detail presented as original observation;
- semantic similarity merging distinct episodes;
- later knowledge retroactively written into original trace;
- salience treated as truth/authority;
- private episode used outside scope;
- replay treated as current state or a new lived event.
