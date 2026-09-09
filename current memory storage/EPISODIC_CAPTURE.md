# Episodic Capture

Status: RECONCILED FOCUSED CONTRACT / DESIGN / NOT IMPLEMENTED

## Purpose

Within `current memory storage/`, episodic capture preserves provenance-rich traces of specific events with enough temporal and contextual identity to distinguish one occurrence from another before or during durable consolidation.

Fast episodic capture is inspired by complementary-learning research but does not require biological hippocampal anatomy.

## Episodic candidate

A candidate trace should support:

- stable episode/event ID;
- observed time or bounded interval;
- recorded time;
- participants/entities as represented at capture time;
- task/context/location references where available;
- event/proposition payload;
- evidence/source references;
- confidence/uncertainty;
- privacy scope;
- encoding state;
- correction/supersession links;
- salience/novelty metadata where used;
- content digest where integrity matters.

## Capture boundary

Fast capture favors preserving specificity over premature generalization.

```text
salient_or_relevant_event
→ episodic candidate
→ admission / privacy / provenance gate
→ current episodic trace
```

Not every transient observation must become a durable episode.

## Event identity

Similar events must remain distinguishable when their individual occurrence matters. Semantic similarity alone is not permission to merge episode identity.

An episode may reference shared entities/concepts while preserving its own event ID, temporal interval, source state, and capture context.

## Historical fidelity

Later correction may change how an episode is interpreted now without rewriting what was represented at capture time.

Preferred pattern:

```text
original trace
→ later correction / reinterpretation trace
→ current reading rule
```

not destructive replacement.

## Replay candidate

A current episodic trace may later be replayed or retrieved for:

- planning;
- prediction;
- semantic generalization;
- procedural learning;
- self/social-model update;
- conflict reconciliation;
- durable episodic consolidation.

Replay does not grant automatic consolidation or current-state authority.

## Failure modes

- reconstructed/inferred details presented as measured original event;
- semantic similarity merges distinct episodes;
- later knowledge is retroactively written into the original trace;
- episodic salience is treated as truth/authority;
- private episode crosses scope without policy;
- replay is treated as proof of current state;
- ingestion order is substituted for event order.

## Provenance

Reconciled from PR #4 `memory/episodic/README.md` into the canonical current/deep memory split. This file owns fast capture and current episodic traces; durable archival consolidation belongs under `deep memory storage/`.