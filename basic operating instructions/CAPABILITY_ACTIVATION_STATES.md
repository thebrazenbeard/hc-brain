# Capability Presence and Activation States

Status: template operating model.

## Principle

A complete Hyperconnectome template should distinguish whether a capability exists architecturally from whether it is currently active, mature, available, or healthy.

`PRESENCE != ACTIVATION != DEVELOPMENT != HEALTH`

This avoids manufacturing different brains by deleting latent capacities and supports developmental, task-specific, safety, and fault-managed configurations without changing the organ's structural identity.

## Presence axis

Recommended values:

- `PRESENT` — architecture and implementation support exist in the instantiated HC;
- `ABSENT` — implementation intentionally lacks this capability;
- `EXTERNAL_ONLY` — capability is not internal and may only be accessed as a peripheral service;
- `UNKNOWN` — presence cannot currently be verified.

For the general template, major intrinsic capacities should normally be specified as architecturally `PRESENT` even when an early prototype leaves them unimplemented.

## Activation axis

Recommended values:

- `DISABLED` — intentionally prevented from executing;
- `DORMANT` — available but not recruited under current conditions;
- `DEVELOPING` — undergoing calibration/learning before full use;
- `ACTIVE` — participating normally;
- `INHIBITED` — temporarily suppressed by another internal control process.

## Health axis

Recommended values:

- `NOMINAL`;
- `DEGRADED`;
- `FAULTED`;
- `QUARANTINED`;
- `UNKNOWN`.

## Development axis

Capacity maturity should be tracked separately from activation. A subsystem can be active but immature, dormant but mature, or degraded without losing its learned structure.

Possible maturity labels:

- `UNDEVELOPED`;
- `CALIBRATING`;
- `LEARNING`;
- `STABLE_WITHIN_SCOPE`;
- `ADAPTING`.

No maturity label implies universal competence.

## Examples

A sexuality subsystem in a newly instantiated brain could be:

`presence=PRESENT, activation=DISABLED, maturity=UNDEVELOPED, health=NOMINAL`

A newly attached visual system could be:

`presence=PRESENT, activation=DEVELOPING, maturity=CALIBRATING, health=NOMINAL`

A mature locomotion controller after actuator damage could be:

`presence=PRESENT, activation=ACTIVE, maturity=STABLE_WITHIN_SCOPE, health=DEGRADED`

## Governance

Activation changes should be provenance-bearing state transitions rather than implicit consequences of loading code. Where a capability can materially affect action, embodiment, learning, privacy, or safety, activation and authorization should remain distinct controls.

`ACTIVE != AUTHORIZED_FOR_ANY_ACTION`

`DISABLED != DELETED`

`DORMANT != FORGOTTEN`
