# Subsystem Lifecycle Contract

Status: CROSS-CUTTING CONTRACT / DESIGN

## 1. Presence and activation are separate

Every first-class subsystem has an architectural presence state and an operational activation/health state.

The template favors architectural completeness. A subsystem may exist even when disabled, dormant, undeveloped, or unimplemented.

## 2. Required lifecycle vocabulary

```text
PRESENT_DISABLED
DORMANT
DEVELOPING
ACTIVE
INHIBITED
DEGRADED
FAULTED
```

Implementations may add states such as `UNIMPLEMENTED`, `SPECULATIVE`, `RECOVERING`, or `QUARANTINED`, provided the semantics remain explicit.

## 3. Presence invariant

For any subsystem declared first-class by the template:

```text
activation != architectural_presence
```

Do not infer:

```text
PRESENT_DISABLED -> ABSENT
DORMANT -> ABSENT
UNIMPLEMENTED -> ABSENT
```

## 4. State meanings

### `PRESENT_DISABLED`

Architectural structure exists but activation is intentionally disabled by configuration/policy/developmental state.

### `DORMANT`

Present and eligible in principle, but currently inactive because no relevant context/trigger exists.

### `DEVELOPING`

Present and activated for learning/calibration/development but not yet considered mature or fully qualified.

### `ACTIVE`

Present and currently participating in eligible cognition/processing.

### `INHIBITED`

Present but currently suppressed by a gate, regulator, context, or policy.

### `DEGRADED`

Present and partially functional with known impairment/reduced capability.

### `FAULTED`

Present but unable to perform its declared capability reliably enough for normal use.

## 5. Orthogonal implementation maturity

Activation state should remain distinct from implementation maturity:

```text
DESIGN_ONLY
UNIMPLEMENTED
PROTOTYPE
EXPERIMENTAL
QUALIFIED
```

Example:

```text
sexuality:
  architectural_presence: true
  activation_state: PRESENT_DISABLED
  implementation_maturity: DESIGN_ONLY
```

## 6. Developmental transitions

Typical path:

```text
PRESENT_DISABLED
→ DORMANT
→ DEVELOPING
→ ACTIVE
```

But transitions may also include:

```text
ACTIVE → INHIBITED
ACTIVE → DEGRADED
DEGRADED → FAULTED
FAULTED → RECOVERING → ACTIVE
```

No transition automatically changes the subsystem's architectural existence.

## 7. Activation authority

Some subsystems may be eligible for autonomous contextual activation; others may require configuration, developmental, safety, privacy, or explicit consent/authority gates.

The subsystem contract must declare the activation rule rather than rely on naming.

## 8. Learning while inactive

Whether a dormant/disabled subsystem may receive background learning updates is a separate policy decision.

Possible policies:

```text
NO_LEARNING
OBSERVE_ONLY
SHADOW_LEARNING
BOUNDED_DEVELOPMENT
FULL_LEARNING
```

## 9. Fault propagation

A subsystem failure should declare:

- health state;
- affected capabilities;
- safe degradation mode;
- whether alternate routes exist;
- whether current coalitions must terminate/reconfigure;
- whether durable state remains trusted;
- recovery requirements.

## 10. Template completeness test

A capability should not be omitted solely because:

- first hardware does not expose its sensor/effect channel;
- initial use case does not need it;
- activation is socially/contextually inappropriate;
- implementation is not ready;
- development has not occurred yet.

If the capacity is first-class in a complete synthetic cognitive organ, define its architectural home and mark its maturity/activation honestly.
