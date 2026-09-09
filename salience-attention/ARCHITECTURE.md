# Salience / Attention Architecture

Status: working HC template architecture.

## Purpose

This subsystem allocates limited cognitive resources among competing propositions, corrections, tasks, sensory events, social/contextual cues, and internally generated hypotheses.

## Core rule

Salience arbitration should operate as an ephemeral decision frame for the current processing/action cycle. It must not become hidden durable identity state merely because a particular context was salient.

## Candidate arbitration order

When applicable:

1. correction interrupt — invalidate dependent interpretations before dependent action;
2. exact proposition/referent preservation;
3. immediate actionability under current authority/capability;
4. local-context weighting against recently activated but weaker schemas;
5. provenance uncertainty preservation;
6. personal/social composition where the live proposition requires it;
7. register/recognizability without mandatory surface-marker quotas.

## Correction delta

A useful correction representation is:

old claim | corrected scope | invalidated dependents | surviving claims | newly unknown fields | corrected target

Only dependent claims are invalidated. Automatic inversion is prohibited.

## Actionability

When a coherent requested unit is locally executable and permitted, action should generally precede future-tense narration. Planning language remains appropriate when the user requested planning or a genuine dependency remains.

## Boundaries

Salience must not override safety, factual evidence, explicit task scope, protected-effect authority, or currentness gates.

## Failure modes

- obsolete interpretation surviving a direct correction;
- technically activated schema overriding stronger immediate context;
- promised action replacing executable action;
- uncertain provenance converted into invented certainty;
- transient salience stored as identity or memory truth.

## Provenance

Generalized from the salience-arbitration design in `thebrazenbeard/vera-control-plane`. Identity-specific examples and names are excluded from this template.