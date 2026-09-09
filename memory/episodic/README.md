# Episodic Memory

Status: GENERIC SUBSYSTEM CONTRACT / DESIGN

## Purpose

`memory/episodic/` stores provenance-rich traces of specific events/episodes with enough temporal and contextual identity to distinguish one occurrence from another.

The design is inspired by fast episodic capture in complementary-learning research, but does not require biological hippocampal anatomy.

## Episodic record

A candidate episodic trace should support:

- stable episode/event ID;
- observed time or bounded interval;
- recorded time;
- participants/entities as represented at capture time;
- context/task/location refs where available;
- event/proposition payload;
- evidence/source refs;
- confidence/uncertainty;
- privacy scope;
- encoding state;
- correction/supersession links;
- salience/novelty metadata where used;
- content digest where integrity matters.

## Capture

Fast capture favors preserving specificity over immediate generalization.

```text
salient_or_relevant_event
→ episodic candidate
→ admission/privacy/provenance gate
→ episodic trace
```

Not every transient observation must become a durable episode.

## Historical fidelity

Later correction may change how an episode is interpreted now without rewriting what was recorded/believed at the time.

Preferred pattern:

```text
original trace
→ later correction/reinterpretation trace
→ current reading rule
```

not destructive replacement.

## Replay

Replay may reactivate episode content for:

- retrieval;
- planning;
- prediction;
- semantic generalization;
- procedural learning;
- self/social-model update;
- conflict reconciliation.

Replay does not grant automatic consolidation authority.

## Pattern separation

Implementations should preserve event identity strongly enough that similar episodes are not silently collapsed merely because their semantic content overlaps.

## Failure modes

- reconstructed/inferred details presented as measured original event;
- semantic similarity merging distinct episodes;
- later knowledge retroactively written into the original trace;
- episodic salience treated as truth/authority;
- private episode used outside scope;
- replay treated as proof of current state.
