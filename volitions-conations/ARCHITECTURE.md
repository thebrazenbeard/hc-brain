# Volitions / conations subsystem

## Purpose

The Volitions / Conations subsystem represents wants, candidate goals, intentions, commitments, revisions, reversals, and completed or abandoned aims across time.

## Source-derived design rules

The directly relevant `thebrazenbeard/conations` repository supports reusable constraints:

- A stored conation is evidence of a state at a particular time, not automatic proof of current desire.
- Historical `PRESENT` state does not imply persistence when current evidence is absent.
- Absence of a later record does not imply disappearance.
- Later evidence may ADD, REVISE, CONTRADICT, REVOKE, COMPLETE, or REVIEW a prior conative record.
- History should remain append-oriented; later evidence should not silently rewrite earlier state.
- A conation is not automatically consent, obligation, promise, authority, or future task.
- Another person's praise, permission, preference, or assignment must not be silently converted into self-authored desire.

## State model

A conative record should preserve at minimum:

- stable record identity;
- timestamp / temporal scope;
- source and provenance;
- object of desire or intended action;
- strength / salience when available;
- currentness state;
- authorship / origin;
- links to predecessor records;
- successor relationship such as revise, revoke, complete, contradict;
- confidence and unresolved ambiguity.

## Runtime chain

`motive formation -> candidate goals -> consequence prediction -> self/commitment compatibility -> body/resource constraints -> arbitration -> intention -> execution -> outcome observation -> update`

This subsystem should keep distinctions between wanting, considering, intending, committing, acting, regretting, and changing one's mind.

## Cross-system interfaces

Strong coupling is expected with `cognition`, `affect`, `salience-attention`, `self identity`, `current memory storage`, `deep memory storage`, `chronology`, `resolver`, and `integration-arbitration`.

## Provenance

Generalized from `thebrazenbeard/conations`; identity-specific historical content is intentionally excluded.