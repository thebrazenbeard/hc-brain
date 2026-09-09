# Volition

Status: INTRINSIC SYSTEM / DESIGN

## Purpose

`volition/` represents choosing, intending, committing, revising, withholding, and selecting action candidates among motivationally and cognitively available options.

Volition is not a metaphysical proof of free will and not one scalar `will` variable.

## Candidate chain

```text
motive formation
→ candidate goals
→ predicted consequences
→ values/commitment compatibility
→ resource/body/context constraints
→ arbitration
→ choice
→ intention
→ action candidate
→ authority/effect gate
→ execution
→ consequence observation
```

Every arrow is a typed transition that may fail, reverse, defer, or remain unresolved.

## Choice object

A choice may preserve:

- candidate set;
- selected candidate or `NO_ACTION`;
- supporting motives;
- competing motives;
- evidence/predictions;
- expected consequences;
- values/commitments;
- uncertainty;
- context/time;
- reversibility window;
- provenance.

## Change of mind

The system must be able to represent:

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

without flattening them.

## Consent and authority

Where consent is relevant, it is an explicit scoped permission state; it is not inferred from desire, role, history, silence, or behavior alone.

An internally selected action can still be externally unauthorized.

```text
CHOSEN_ACTION != AUTHORIZED_EFFECT
```

## Inhibition

A motive or action can remain active while inhibited by values, safety, context, authority, or another motive. Inhibition does not prove absence of the underlying state.

## Failure modes

- strongest desire automatically wins;
- prior commitment treated as impossible to revise;
- prior consent treated as perpetual;
- chosen action bypasses effect gate;
- inhibition rewritten as no desire;
- failure to act rewritten as no intention.
