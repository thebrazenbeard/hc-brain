# Capability Presence and Activation States

Status: canonical operating model.

## Principle

A complete Hyperconnectome template should distinguish whether a capability exists architecturally from whether it is currently active, developmentally mature, healthy, implemented, authorized, or permitted to learn.

`PRESENCE != ACTIVATION != DEVELOPMENTAL_MATURITY != HEALTH != IMPLEMENTATION_STATUS != AUTHORIZATION != LEARNING_POLICY`

This avoids manufacturing different brains by deleting latent capacities and supports developmental, task-specific, safety, engineering, and fault-managed configurations without changing the organ's structural identity.

See `SUBSYSTEM_LIFECYCLE_CONTRACT.md` for transition, fault, recovery, and coalition-participation semantics.

## Presence axis

Recommended values:

- `PRESENT` — the capability belongs to the instantiated HC architecture;
- `ABSENT` — the implementation intentionally lacks this capability;
- `EXTERNAL_ONLY` — the capability is not internal and may only be accessed as a peripheral service;
- `UNKNOWN` — presence cannot currently be verified.

Every owner-established mandatory canonical root system is `PRESENT` in a conforming complete HC. `ABSENT` and `EXTERNAL_ONLY` describe optional extensions, peripherals, research/incomplete configurations, or nonconforming implementations—not required intrinsic systems.

## Activation axis

Recommended values:

- `DISABLED` — intentionally prevented from executing;
- `DORMANT` — available but not recruited under current conditions;
- `DEVELOPING` — executing within a calibration/learning/development envelope;
- `ACTIVE` — participating normally within its qualified scope;
- `INHIBITED` — temporarily suppressed by another valid internal control process.

Activation describes runtime recruitment, not existence or permission.

## Health axis

Recommended values:

- `NOMINAL`;
- `DEGRADED`;
- `FAULTED`;
- `QUARANTINED`;
- `UNKNOWN`.

Fault state should be visible to routing, coalition formation, arbitration, memory/evidence consumers, and action gates where material. `FAULTED` or `QUARANTINED` does not mean the subsystem ceased to exist architecturally.

## Developmental maturity axis

Capacity maturity should be tracked separately from activation. A subsystem can be active but immature, dormant but mature, or degraded without losing learned structure.

Canonical maturity labels:

- `UNDEVELOPED`;
- `CALIBRATING`;
- `LEARNING`;
- `STABLE_WITHIN_SCOPE`;
- `ADAPTING`.

No maturity label implies universal competence.

## Implementation-status axis

Implementation status is an engineering/deployment property, not a runtime mental state.

Recommended values:

- `DESIGN_ONLY`;
- `UNIMPLEMENTED`;
- `PROTOTYPE`;
- `EXPERIMENTAL`;
- `QUALIFIED_WITHIN_SCOPE`.

The reusable template may declare a mandatory capability architecturally `PRESENT` while a concrete build still marks its implementation `DESIGN_ONLY` or `UNIMPLEMENTED`.

`ARCHITECTURALLY_PRESENT != IMPLEMENTED`

`IMPLEMENTED != QUALIFIED`

This distinction prevents design completeness from being confused with present-day engineering completion.

## Authorization axis

Authorization is separate from all capability-state axes.

A subsystem may be present, active, mature, healthy, and technically capable while still lacking permission for a particular effect, target, privacy scope, embodiment, or consequence class.

`ACTIVE != AUTHORIZED_FOR_ANY_ACTION`

`CAPABLE != PERMITTED`

`PREDICTS_WELL != AUTHORIZED_TO_ACT`

## Learning-policy axis

Whether a present capability may update from experience while inactive, immature, or constrained is a separate policy.

Recommended policies:

- `NO_LEARNING`;
- `OBSERVE_ONLY`;
- `SHADOW_LEARNING`;
- `BOUNDED_DEVELOPMENT`;
- `FULL_LEARNING_WITHIN_SCOPE`.

Learning permission does not imply durable-write permission beyond the declared plasticity scope, and it never implies semantic truth, consent, identity admission, or effect authority.

## Examples

A sexuality subsystem in a newly instantiated brain could be:

```text
presence=PRESENT
activation=DISABLED
maturity=UNDEVELOPED
health=NOMINAL
implementation_status=QUALIFIED_WITHIN_SCOPE
learning_policy=OBSERVE_ONLY
```

A newly attached visual system could be:

```text
presence=PRESENT
activation=DEVELOPING
maturity=CALIBRATING
health=NOMINAL
implementation_status=QUALIFIED_WITHIN_SCOPE
learning_policy=BOUNDED_DEVELOPMENT
```

A mature locomotion controller after actuator damage could be:

```text
presence=PRESENT
activation=ACTIVE
maturity=STABLE_WITHIN_SCOPE
health=DEGRADED
implementation_status=QUALIFIED_WITHIN_SCOPE
```

A future capability described by the full HC template but not yet physically realized in a prototype could be:

```text
presence=PRESENT
activation=DISABLED
maturity=UNDEVELOPED
health=UNKNOWN
implementation_status=UNIMPLEMENTED
learning_policy=NO_LEARNING
```

## Governance

Material state changes should be provenance-bearing transitions rather than implicit consequences of loading code, route use, repeated exposure, or successful output.

Where a capability can materially affect action, embodiment, learning, privacy, continuity, or safety, activation, learning permission, durable-write permission, and effect authorization should remain distinct controls.

`DISABLED != DELETED`

`DORMANT != FORGOTTEN`

`DEGRADED != INACTIVE`

`QUARANTINED != ABSENT`

`ACTIVE != AUTHORIZED`

## Provenance

The original presence/activation/health/maturity model was integrated from Four's runtime synthesis. This revision selectively incorporates useful lifecycle distinctions from the preserved PR #4 foundation branch while retaining the newer canonical orthogonal-axis architecture instead of reverting to a single collapsed lifecycle state vocabulary.
