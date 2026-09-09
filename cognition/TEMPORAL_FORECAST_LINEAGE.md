# Temporal Forecast Lineage

Status: canonical focused cognition contract.

## Purpose

The HC may generate forecasts over future world state, body state, topology, internal resource state, social consequences, action outcomes, or other modeled variables. When one forecast is used as input to a later forecast, the resulting chain must preserve ancestry rather than presenting every predicted horizon as if it arose independently from direct observation.

The governing rule is:

> **A forecast derived from a forecast inherits the epistemic and provenance limitations of its ancestors.**

## Core separations

`PREDICTED_TIMEPOINT != OBSERVED_TIMEPOINT`

`FORECAST_OF_FORECAST != FORECAST_FROM_OBSERVED_STATE`

`DESCENDANT_FORECAST != INDEPENDENT_CORROBORATION`

`LATER_HORIZON != NEW_EVIDENCE`

`FORECAST_CHAIN_DEPTH != EVIDENCE_STRENGTH`

`DESCENDANT_CONFIDENCE != FRESH_INDEPENDENT_CONFIDENCE`

`FORECAST != HISTORY`

`FORECAST_ERROR != AUTOMATIC_CAUSAL_EXPLANATION`

## Forecast lineage object

A material forecast should be representable with enough information to recover its prediction ancestry, for example:

```text
FORECAST_NODE {
  forecast_id
  target_state_or_event
  target_time_or_interval
  horizon
  parent_state_ids[]
  observed_ancestor_ids[]
  generated_ancestor_ids[]
  model_or_algorithm
  model_version_or_digest
  assumptions[]
  source_evidence_ids[]
  uncertainty
  calibration_state
  domain_or_regime_state
  generated_at
  validity_or_expiry
  contradicted_by_observation_ids[]
  superseding_forecast_ids[]
  provenance
}
```

The exact implementation schema may differ. The semantic requirements do not.

## Ancestry

A prediction chain can contain different kinds of ancestors:

- directly observed state;
- calibrated or transformed observation;
- inferred current state;
- simulated counterfactual state;
- generated intermediate state;
- earlier forecast;
- imputed missing timepoint;
- population/reference prior;
- action-conditional predicted state.

Those classes must not be flattened into one generic `input_state` label when the distinction affects reliability or interpretation.

`GENERATED_ANCESTOR != OBSERVED_ANCESTOR`

`IMPUTED_ANCESTOR != OBSERVED_ANCESTOR`

`COUNTERFACTUAL_ANCESTOR != HISTORY`

## Uncertainty propagation

Later predictions should account for uncertainty inherited from earlier generated states where material.

HC does not require one universal mathematical uncertainty-propagation algorithm, but a conforming implementation must not silently reset uncertainty merely because another predictor stage began.

Relevant contributors may include:

- source observation uncertainty;
- model uncertainty;
- calibration error;
- transform/alignment uncertainty;
- uncertainty introduced by generated intermediate state;
- domain/regime shift;
- missing-data imputation;
- compounding horizon error;
- branching assumptions or unresolved rival models.

If an implementation reports a confidence value for a descendant forecast, the claimed calibration scope should state whether ancestor uncertainty was incorporated.

## Correction and invalidation

If an observed event later contradicts or materially revises an ancestor forecast, dependent descendants must be reconsidered.

Possible outcomes include:

- invalidate descendant forecast;
- mark stale or contradicted;
- recompute from the newly observed state;
- retain historical prediction for audit while issuing a successor;
- preserve multiple branches if uncertainty remains unresolved.

A correction should not erase the historical fact that the earlier prediction was made.

`ANCESTOR_CORRECTION != HISTORY_REWRITE`

`ANCESTOR_CORRECTION -> DEPENDENCY_REEVALUATION`

## Branching futures

HC may preserve several candidate futures rather than committing to one trajectory.

Branches should preserve:

- assumptions;
- action conditions;
- model/hypothesis identity;
- probability/confidence if used;
- parentage;
- pruning/rejection reason;
- observation that later confirmed or contradicted the branch.

A branch being discarded for planning efficiency does not mean its earlier existence should vanish from provenance if consequential decisions depended on it.

## Action-conditional forecasts

Predictions made under candidate actions must remain explicitly conditional.

`PREDICTED_IF_ACTION_A != PREDICTION_THAT_ACTION_A_WILL_OCCUR`

`HIGH_EXPECTED_VALUE_BRANCH != ACTION_AUTHORIZATION`

`PREDICTED_SUCCESS != EFFECT_PERMISSION`

Consequence forecasts can inform conation and arbitration without becoming authority.

## Temporal-hypergraph interaction

Forecasts may participate in temporary higher-order coalitions and may themselves refer to predicted future hypergraph configurations.

A predicted future coalition or edge is not current topology.

`PREDICTED_H_f(t+n) != CURRENT_H_f(t)`

`FORECASTED_ROUTE != CONFIGURED_ROUTE`

`FORECASTED_PLASTIC_STATE != PLASTICITY_COMMIT`

Predicted topology follows the topology-evidence and plasticity-admission rules before it can alter actual HC state.

## Observation reconciliation

When target time arrives, HC should compare forecast to observation where material and preserve:

- prediction identity;
- actual observation;
- residual/error;
- calibration implications;
- affected descendant predictions;
- model revision candidates;
- provenance.

The observation becomes evidence about the forecast/model. It does not make the earlier forecast retrospectively observed.

## Missing and imputed timepoints

`MISSING_OBSERVATION != NO_CHANGE`

`IMPUTED_TIMEPOINT != OBSERVED_TIMEPOINT`

An imputed state used as an ancestor must carry that origin into descendants. If the missing interval is later filled by observation, descendants that materially depended on the imputation should be re-evaluated.

## External predictors

An external forecast service may return candidate predictions, but the HC owns:

- forecast lineage admission;
- provenance;
- uncertainty/currentness interpretation;
- dependency invalidation;
- comparison with observation;
- durable model revision;
- action selection and authorization.

External service outputs do not become history, current world state, or authority by provider confidence.

## Failure modes

- t2 forecast presented as independent although it consumes generated t1;
- confidence reset at each cascade stage;
- predicted future graph recorded as actual topology;
- forecast descendants retained after ancestor contradiction without re-evaluation;
- imputed timepoint silently converted to observed history;
- several descendants of the same forecast counted as independent corroboration;
- model/version change inside the chain omitted from provenance;
- action-conditional prediction interpreted as selected intent;
- forecast branch pruning silently erases provenance relevant to a consequential decision;
- repeated self-generated predictions inflate confidence without new evidence.

## Conformance questions

1. Which ancestors of this forecast were directly observed?
2. Which ancestors were inferred, generated, simulated, imputed, or forecast?
3. What model/version produced each material stage?
4. Was ancestor uncertainty propagated or explicitly excluded from the confidence claim?
5. Has an ancestor since been contradicted, superseded, or observed?
6. Does the descendant require recomputation after that change?
7. Is this forecast conditional on an action, assumption, or rival model branch?
8. Is any predicted topology being incorrectly treated as current or committed topology?
9. Could several descendants be mistaken for independent evidence despite shared ancestry?
10. When the target time arrives, how will observation/error be reconciled without rewriting prediction history?

## Provenance

Promoted from the general temporal-prediction problem already present in HC and strengthened through code-level study of `basiralab/EvoGraphNet`, where a generated first future graph is observed to become input to a second future generator. Source-specific implementation choices are not imported as HC requirements.

See `docs/research/BASIRA_TEMPORAL_FORECAST_LINEAGE_2026-09-09.md`.
