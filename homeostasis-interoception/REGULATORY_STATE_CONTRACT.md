# Regulatory State Contract

Status: canonical focused runtime contract, reconciled 2026-09-18.

## Purpose

HC regulatory state separates internal sensing, physiological estimation, target state, homeostatic error, urgency, modulation, protective control, and external action requests.

The governing separations are:

`INTERNAL_SENSOR_READING != PHYSIOLOGICAL_TRUTH`

`PHYSIOLOGICAL_ESTIMATE != HOMEOSTATIC_ERROR`

`HOMEOSTATIC_ERROR != AFFECT`

`URGENCY != AUTHORITY`

`REGULATORY_REQUEST != EXTERNAL_ACTION_AUTHORIZATION`

`PREAUTHORIZED_PROTECTIVE_EFFECT != GENERAL_ACTION_PERMISSION`

## Runtime object families

The reference runtime may represent:

- interoceptive observation with source, units, reliability, and evidence identity;
- physiological estimate with observation lineage, confidence, and sensor-conflict state;
- regulatory target with explicit basis and supersession;
- regulatory error with magnitude, direction, urgency, and estimate/target identity;
- regulatory modulation that may influence affect/salience while retaining causal lineage;
- regulatory request that remains an action candidate;
- local protective scope bounded to declared internal target/effect envelopes;
- protective decisions with reason references and audit history.

## Sensor disagreement

Internal origin does not grant truth authority.

Where redundant internal observations diverge materially, the runtime preserves a conflict state and reduces confidence rather than arbitrarily selecting one source.

## Protective control

Standing protective control is limited to explicitly registered internal effect/target scopes and declared value envelopes.

It cannot be reused as authority for external effects or unrelated targets.

## Affect coupling

Regulatory pressure may raise arousal/threat modulation and influence salience.

It must not raise semantic confidence merely because physiological urgency is high.

## Somatic coupling

Body calibration requires observed somatic evidence. Simulated or predicted state cannot masquerade as lived calibration.

Reachability and other affordance outputs remain predictions and carry their observed/generated ancestry into downstream world-model forecasts.

## Provenance

Recovered from the historical `four/affect-homeostasis-v1` regulatory contract/spec and reconciled against current canonical `homeostasis-interoception/ARCHITECTURE.md`, `somatics/ARCHITECTURE.md`, current affect contracts, the hardened reference kernel, and the executable cognitive core.

The historical branch itself is not treated as current authority.
