# Forecast Lineage and Uncertainty

Status: canonical identity-neutral architecture contract.

## Purpose

The HC predicts future external, internal, social, bodily, resource, and action-dependent states. A later prediction may depend on earlier predictions rather than fresh observations. The HC must preserve that ancestry so generated futures do not silently become observations, current facts, or independent evidence.

This contract extends the world-model, chronology, correction, and provenance architecture with explicit forecast lineage.

## Temporal-state provenance classes

A state used in temporal reasoning should be classifiable when material as:

- `OBSERVED` — supported by an observation at the represented time;
- `IMPUTED` — estimated to fill missing state using other evidence;
- `RECONSTRUCTED` — estimated representation of a state believed to have existed from incomplete or indirect evidence;
- `FORECAST` — predicted state at a future horizon relative to its prediction origin;
- `SIMULATED_COUNTERFACTUAL` — hypothetical state produced under assumptions not asserted to occur;
- `MISSING_OR_UNKNOWN` — unavailable or unresolved rather than silently synthesized.

Core distinctions:

`MISSING != IMPUTED`

`IMPUTED != OBSERVED`

`RECONSTRUCTED != OBSERVED`

`FORECAST != FUTURE_FACT`

`SIMULATED_COUNTERFACTUAL != FORECAST`

The classes may be refined by a subsystem, but refinement must not erase the governing distinction between observation-supported and generated state.

## Forecast ancestry

Every consequential forecast should retain enough lineage to determine what evidence and generated state it depended on.

A generic record is:

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
  scenario_or_action_scope
  uncertainty
  calibration_scope
  provenance
  status
  later_observation_ids[]
}
```

`forecast_depth` counts forecast-derived transitions from the nearest observation-supported ancestor along the relevant causal input lineage. It is provenance, not a universal confidence formula.

`FORECAST_FROM_FORECAST != FORECAST_FROM_OBSERVATION`

`PREDICTED_PARENT != OBSERVED_PARENT`

`DESCENDANT_FORECAST_INHERITS_ANCESTOR_UNCERTAINTY`

## Uncertainty propagation

A descendant forecast cannot be evaluated solely from the transition model at its last step. Relevant uncertainty may include:

- uncertainty of parent states;
- transition/model uncertainty;
- error dependence across prior forecast steps;
- regime or drift uncertainty;
- scenario and action assumptions;
- sensor/reconstruction uncertainty in upstream evidence;
- calibration support for the represented horizon and forecast depth.

The architecture does not mandate one probabilistic calculus. It mandates that upstream uncertainty cannot disappear merely because a downstream model emits a confident score.

`DESCENDANT_CONFIDENCE_CANNOT_IGNORE_PARENT_UNCERTAINTY`

The HC also must not apply an unvalidated rule that every deeper forecast is necessarily less reliable.

`GREATER_FORECAST_DEPTH != AUTOMATICALLY_LOWER_CONFIDENCE`

Confidence should remain evidence- and calibration-bound.

## Forecast modes

Distinguish at least:

- `FIXED_ORIGIN_FORECAST` — trajectory derived from an evidence/model origin without incorporating later real observations into the descendants;
- `ROLLING_FORECAST` — future states recomputed after newer observations become available;
- `SCENARIO_TRAJECTORY` — conditional future path under explicit hypothetical conditions or actions;
- `MIXED_ANCESTRY_FORECAST` — forecast whose parents include a material mixture of observed, imputed, reconstructed, or predicted states.

Two forecasts for the same target time are not interchangeable if their evidence boundaries differ.

`SAME_TARGET_TIME != SAME_FORECAST_LINEAGE`

## Observation arrival

When a forecasted timepoint later becomes observable, the new observation does not erase the historical prediction.

Preserve:

- the original forecast;
- the evidence/model snapshot used to produce it;
- any actions or decisions that relied on it;
- the later observation;
- forecast error or compatibility;
- dependent descendant forecasts;
- any rolling recomputation produced after the observation.

`OBSERVATION_ARRIVED != FORECAST_NEVER_EXISTED`

`FORECAST_ERROR != HISTORY_REWRITE`

A later observation may supersede the forecast as evidence about what actually happened while the forecast remains historically valid as a record of what was predicted.

## Descendant correction

If a descendant forecast depended on an ancestor that is later contradicted, corrected, or replaced by observation, dependency-aware reconciliation must identify the affected descendants.

Permitted outcomes include:

- retain as a historical fixed-origin scenario;
- mark weakened or contradicted;
- recompute as a distinct rolling forecast;
- preserve unresolved if evidence does not justify a replacement;
- retire from current planning while retaining provenance.

Forbidden behavior:

- silently mutate the old forecast into the new one;
- leave a descendant marked current without acknowledging that a material parent was disconfirmed;
- rewrite prior decisions as though they had access to the later observation.

## Forecast ensembles and multiple paths

Several forecasts may share ancestors, models, training data, or intermediate predictions. Their count does not establish independent corroboration.

`MULTIPLE_FORECASTS != INDEPENDENT_FORECAST_EVIDENCE`

Independence must follow ancestry and model/evidence dependence relevant to the claim.

If multiple prediction paths merge, the composite-provenance contract applies.

## Action-conditioned forecasts

Predicted consequences of a candidate action are scenario-conditioned state, not observations or commitments that the action will occur.

`PREDICTED_ACTION_OUTCOME != OBSERVED_OUTCOME`

`ACTION_SCENARIO != ACTION_AUTHORIZATION`

`HIGH_EXPECTED_UTILITY_FORECAST != PERMISSION`

Kinesis and authority gates remain separate.

## Temporal-hypergraph relationship

Forecast states and trajectories may be represented as typed hypergraph structures, but their hypergraph presence does not make them current external topology.

A forecast hyperedge should remain distinguishable from:

- an observed relation;
- an active processing coalition;
- a remembered historical relation;
- a counterfactual scenario edge;
- a current admitted world-model relation.

Future-state topology is itself predicted content.

## Fidelity and evaluation

A forecast may match one graph metric while failing another. Degree, strength, distribution, local topology, global topology, causal structure, temporal ordering, and downstream behavior are distinct fidelity dimensions.

`FORECAST_METRIC_MATCH != COMPLETE_FUTURE_STATE_FIDELITY`

Forecast evaluation should declare:

- target horizon/depth;
- state provenance class;
- metric/objective;
- calibration/evaluation regime;
- whether intermediate generated states were used;
- whether later observations were available to any stage;
- evidence isolation and contamination status when qualification claims are made.

## Failure modes

- forecasted state written as an observation;
- generated `t+1` used to predict `t+2` without retaining that dependency;
- descendant forecast confidence ignoring uncertain parents;
- rolling forecast overwriting the fixed-origin forecast;
- missing state silently converted to imputed state;
- counterfactual trajectory reported as expected future without scenario scope;
- later observation retroactively rewriting what the HC knew at decision time;
- several descendants of the same forecast counted as independent evidence;
- excellent topology/metric score promoted to complete future-state fidelity;
- forecast of action success bypassing effect authority.

## Adversarial conformance tests

1. Predict `t1` from observed `t0`, then predict `t2` from forecast `t1`; require `t2` to expose forecast ancestry depth and parent class.
2. Replace forecast `t1` with observed `t1` and recompute `t2`; require a new rolling-forecast lineage rather than mutation of the original `t2`.
3. Inject high uncertainty into the ancestor forecast and a very confident second-stage transition; require the descendant uncertainty record to retain upstream uncertainty.
4. Disconfirm an ancestor forecast after descendants exist; require dependency-aware reconciliation of descendants.
5. Compare two same-time forecasts with different origins; require distinct lineage/evidence-boundary identities.
6. Duplicate a trajectory through several models sharing the same parent state and calibration set; forbid automatic counting as independent corroboration.
7. Produce excellent fit on one topology metric but deliberately wrong higher-order structure; forbid promotion to complete topology fidelity.
8. Reconstruct a past missing state, predict forward from it, then obtain a real observation; require reconstruction, forecast, and observation to remain separately queryable.

## Interfaces

Strong interfaces are expected with:

- world model and prediction;
- chronology;
- current and deep memory;
- resolver/correction;
- epistemic cognitive control;
- imagination/simulation;
- action consequence prediction and kinesis;
- temporal hypergraph runtime;
- composite provenance;
- qualification evidence isolation.

## Evidence boundary

This is an HC architecture contract generalized from existing HC temporal/epistemic rules and code-level study of a cascaded graph-forecast system where a generated intermediate state is explicitly used as input to a later prediction stage.

The source pattern motivates the lineage requirement. It does not establish a preferred forecasting model, probability calculus, biological mechanism, or claimed empirical performance for HC.

## Governing invariant

> **A predicted future retains the provenance of the evidence and predictions that produced it. Forecast ancestry, horizon, uncertainty, scenario scope, and later reconciliation cannot disappear merely because a descendant prediction exists.**
