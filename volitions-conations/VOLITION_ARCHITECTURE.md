# Volition Architecture

Status: RECONCILED FOCUSED CONTRACT / DESIGN / NOT IMPLEMENTED

## Purpose

Within `volitions-conations/`, volition represents choosing, intending, committing, revising, withholding, and selecting action candidates among motivationally and cognitively available options.

Volition is not a metaphysical proof of free will and is not represented as one scalar `will` variable.

## Candidate chain

A useful semantic chain is:

```text
motive formation
→ candidate goals
→ predicted consequences
→ values/commitment compatibility
→ resource/body/context constraints
→ scoped arbitration
→ choice
→ intention
→ action candidate
→ authority/effect gate where applicable
→ execution
→ consequence observation
```

Every arrow is a typed temporal transition that may fail, reverse, defer, be inhibited, or remain unresolved.

## Choice object

A choice may preserve:

- candidate set;
- selected candidate or `NO_ACTION`;
- supporting motives;
- competing motives;
- evidence and predictions;
- expected consequences;
- values/commitments;
- uncertainty/conflict;
- temporal context;
- reversibility/revision window;
- provenance.

## Change of mind

The HC must be able to represent these as distinct states:

```text
wanted
considered
chose
intended
committed
acted
withheld
regretted
revised
revoked
```

A later revision should preserve the historical transition rather than pretend the earlier state never existed.

## No-action and withholding

`NO_ACTION` may be a valid selected outcome. A system may also preserve an active motive or intention while withholding action because of values, risk, body/resource state, authority, social context, or competing motives.

```text
INHIBITED_ACTION != ABSENT_MOTIVE
WITHHELD_ACTION != ABSENT_INTENTION
```

## Consent and authority

Where consent is relevant, it is an explicit scoped state. It is not inferred from desire, role, history, silence, or behavior alone.

An internally selected action may still be externally unauthorized.

```text
CHOSEN_ACTION != AUTHORIZED_EFFECT
```

Likewise, authorization for one effect does not imply authorization for every related effect.

## Interaction with integration-arbitration

Volition does not require a permanent executive node. Scoped arbitration within a temporal coalition can compare candidate goals/actions using current conative state, cognition, values, body/resource state, salience, and evidence.

Selection is an output of that bounded process, not proof that the selected option was the only active motive.

## Consequence revision

Observed consequences may trigger:

- satisfaction/completion;
- regret;
- goal revision;
- commitment strengthening or weakening;
- new conflict;
- procedural learning;
- conative reweighting;
- world-model correction.

These are separate candidate updates and should not be silently collapsed into one reward scalar unless an implementation explicitly justifies that representation.

## Failure modes

- strongest desire automatically wins;
- prior commitment treated as impossible to revise;
- prior consent treated as perpetual;
- chosen action bypasses required effect gate;
- inhibition rewritten as no desire;
- failure to act rewritten as no intention;
- selected candidate erases competing motives;
- action result assumed without consequence evidence.

## Provenance

Reconciled from PR #4 `volition/README.md` into the canonical `volitions-conations/` root and aligned with current distributed arbitration and kinesis/action-selection contracts.