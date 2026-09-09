# BASIRA EvoGraphNet Forecast-Lineage Study — 2026-09-09

Status: NON-CANONICAL RESEARCH / SOURCE STUDY

## Source cut

Repository: `basiralab/EvoGraphNet`

Inspected default branch: `master`

Primary source artifacts:

- `README.md` blob `142490dc023c601c927355085a26b6efbe936cb0`
- `code/EvoGraphNet.py` blob `ab89476d0e4186b5dce93d827a2fdb4c84b7b77f`

This note records source behavior and HC transfer lessons. It does not make EvoGraphNet part of HC and does not treat source-model claims as evidence that HC implements the same capability.

## Documented architecture claim

DOCUMENTED from the repository README: EvoGraphNet predicts longitudinal graph evolution from one baseline timepoint using a cascade of time-dependent graph GANs. Each generator's predicted graph at one timepoint is passed to the next generator for a later timepoint.

The README therefore makes prediction ancestry part of the intended architecture rather than an incidental implementation detail.

## Observed implementation

OBSERVED in `code/EvoGraphNet.py`:

1. A first generator predicts `fake_y` from the source data and constructs `fake_data` for the first predicted follow-up state.
2. Before the second-stage generator is trained/evaluated, `fake_data.x` is detached and supplied to `generator2`.
3. `generator2(fake_data)` produces the second predicted follow-up state. The comment explicitly describes this as creating fake data for `t2` from fake data for `t1`.
4. Ground-truth `data.y` and `data.y2` are used for stage-specific loss/evaluation, but stage 2's input state remains the generated stage-1 state rather than replacing it with the real stage-1 observation.
5. The first and second stages compute topology-like loss by comparing row/connection-strength sums of generated versus ground-truth graphs.
6. The validation path preserves the same chained ancestry: generated `t1` becomes the input to the second generator used to obtain generated `t2`.

## Primary transfer finding: forecast descendants inherit forecast ancestry

A later forecast produced from an earlier forecast is not equivalent to a forecast produced directly from a fresh observation.

HC transfer:

`FORECAST_FROM_FORECAST != FORECAST_FROM_OBSERVATION`

`DESCENDANT_FORECAST_INHERITS_ANCESTOR_UNCERTAINTY`

`PREDICTED_PARENT != OBSERVED_PARENT`

A forecast object must retain whether each causal/input parent was observed, reconstructed, imputed, simulated, or itself forecast.

## Temporal state classes needed

The source pattern exposes a practical need to distinguish at least:

- `OBSERVED` — supported by a source observation at the represented time;
- `IMPUTED` — estimated to fill a missing value/timepoint using surrounding or correlated evidence;
- `RECONSTRUCTED` — estimated representation of a state believed to have existed, typically from incomplete/indirect evidence;
- `FORECAST` — predicted future state relative to the prediction origin;
- `SIMULATED_COUNTERFACTUAL` — state produced under hypothetical conditions not asserted to occur;
- `MISSING_OR_UNKNOWN` — absent evidence without silently filling it.

These are provenance/epistemic classes, not merely file names or visualization labels.

`MISSING != IMPUTED`

`IMPUTED != OBSERVED`

`RECONSTRUCTED != OBSERVED`

`FORECAST != FUTURE_FACT`

`SIMULATED_COUNTERFACTUAL != FORECAST`

## Forecast ancestry object

A useful HC forecast record should carry:

```text
FORECAST_STATE {
  forecast_id
  target_time_or_horizon
  prediction_origin_time
  model_snapshot
  parent_state_ids[]
  parent_state_classes[]
  forecast_depth
  assumptions[]
  intervention_or_scenario_scope
  uncertainty
  calibration_scope
  provenance
  superseded_by_observation_id?
}
```

`forecast_depth` is the number of forecast-derived transitions between the nearest observation-supported ancestor and the current forecast. It is not a universal proxy for error, but it is essential provenance for judging possible error accumulation.

## Uncertainty propagation

A cascade can introduce uncertainty at every step. The HC must not simply copy the stage-1 confidence to stage 2 or treat later predicted states as having the same epistemic footing as observations.

At minimum, later forecast uncertainty should be computed from or bounded by:

- uncertainty in all parent states;
- model uncertainty/error at the current transition;
- dependence among errors across transitions;
- regime/drift uncertainty;
- scenario/assumption uncertainty;
- calibration evidence for the relevant forecast horizon/depth.

No one formula is mandated by this study.

`DESCENDANT_CONFIDENCE_CANNOT_IGNORE_PARENT_UNCERTAINTY`

`LONGER_FORECAST_CHAIN != AUTOMATICALLY_LOWER_CONFIDENCE`

The second distinction matters: forecast depth should trigger uncertainty accounting, not a simplistic monotonic penalty when empirical calibration says otherwise.

## Observation arrival and forecast reconciliation

When a real observation later arrives for a forecasted timepoint, it must not erase the historical forecast. The system should preserve both:

- what was predicted at the earlier decision time;
- what was later observed;
- prediction error or compatibility;
- descendants that depended on the earlier forecast;
- whether descendants need recomputation, weakening, or preservation as historical scenario products.

`OBSERVATION_ARRIVED != FORECAST_NEVER_EXISTED`

`FORECAST_ERROR != HISTORY_REWRITE`

If a later forecast was causally derived from the now-disconfirmed forecasted parent, the correction system should be able to identify and reassess that descendant lineage.

## Rolling forecast versus fixed-origin forecast

HC should distinguish:

- `FIXED_ORIGIN_FORECAST` — all future states derive from the original evidence/model snapshot, possibly through chained generated states;
- `ROLLING_FORECAST` — newly observed states are incorporated and future forecasts recomputed from the updated evidence boundary;
- `SCENARIO_TRAJECTORY` — hypothetical path conditional on explicit assumptions/actions;
- `MIXED_ANCESTRY_FORECAST` — combines observed, imputed, reconstructed, and predicted parents.

Comparing these modes without preserving ancestry can make later forecasts look commensurate when they were conditioned on different evidence.

## Topology-loss boundary

OBSERVED: EvoGraphNet's topology-like term compares generated and target graph row/connection-strength sums.

INFERRED transfer: satisfying that objective cannot by itself establish complete topological equivalence, causal fidelity, temporal-dynamics fidelity, or semantic correctness of the forecast.

This reinforces existing HC metric-scoped fidelity rules:

`TOPOLOGY_METRIC_MATCH != COMPLETE_TOPOLOGY_EQUIVALENCE`

## Possible implementation defect noted but not generalized

OBSERVED in the inspected second-stage training/validation loss code: the identity-loss expression for the second stage calls `generator(swapped_data2)` rather than `generator2(swapped_data2)`.

This is recorded as an implementation-level anomaly for independent review, not as a claim that the paper's method is invalid. It may be a bug, legacy choice, or undocumented design decision; this inspection does not establish which.

Status: HYPOTHESIS / REVIEW NEEDED.

## Proposed HC canonical transfer

Create a focused forecast-lineage contract requiring:

- temporal-state class preservation;
- parent ancestry and forecast depth;
- uncertainty inheritance/accounting;
- fixed-origin versus rolling/scenario distinctions;
- correction propagation when an observed state supersedes a forecast as current evidence;
- historical retention of the original forecast and the decisions that used it.

## Adversarial tests suggested

1. Generate `t1` from observation `t0`, then `t2` from forecast `t1`; verify `t2` retains forecast ancestry depth 2 rather than appearing observation-derived.
2. Replace forecast `t1` with an actual observation and recompute `t2`; verify the rolling forecast is a distinct object/lineage, not an in-place rewrite of the fixed-origin forecast.
3. Introduce high uncertainty at stage 1 and a highly confident stage-2 transition; verify final confidence cannot silently ignore the uncertain parent.
4. Produce several generated future states with excellent degree/strength match but wrong higher-order structure; verify metric-scoped fidelity is not promoted to complete topology equivalence.
5. Allow a forecast to influence an action, then later observe the forecast was wrong; verify the historical decision context remains reconstructable.
6. Disconfirm an ancestor forecast and verify dependent descendants are identified for reassessment rather than remaining silently current.

## Evidence boundary

DOCUMENTED: cascade intent and source claims from the repository README.

OBSERVED: specific generated-state chaining and loss/evaluation paths in the inspected source file.

INFERRED: HC forecast-lineage requirements.

HYPOTHESIS: the second-stage identity-loss generator choice is an implementation defect.

UNKNOWN: empirical error accumulation across horizons, calibration quality, and whether another unretrieved source revision corrects the noted anomaly.
