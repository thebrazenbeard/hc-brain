# BASIRA Temporal Forecast Lineage Scour — 2026-09-09

Status: RESEARCH / SOURCE PROVENANCE / NON-CANONICAL FINDINGS

## Scope

Primary source inspected:

- `basiralab/EvoGraphNet`
- repository tree at commit/tree rooted by `f49131c3ed0eb792524904e46ad436571c0a5811`
- `README.md`
- `code/EvoGraphNet.py` blob `ab89476d0e4186b5dce93d827a2fdb4c84b7b77f`

The source is used as a computational-pattern study. It does not establish HC architecture, biological mechanism, or complete cognitive-organ feasibility.

## DOCUMENTED source claim

The EvoGraphNet README describes a cascade of time-dependent graph-generative adversarial networks in which the predicted graph at one timepoint is communicated to the next generator, enabling multiple future graph predictions from one initial timepoint.

Transfer implication: chained prediction is materially different from independent prediction at each horizon because later predictions inherit dependence on earlier predicted state.

## OBSERVED code behavior

In `code/EvoGraphNet.py`:

1. The first generator computes a synthetic first future graph:

```text
fake_y = generator(data)
```

2. That predicted graph is wrapped as `fake_data`.

3. Before the second stage, `fake_data.x` is detached and passed to the second generator:

```text
fake_y2 = generator2(fake_data)
```

4. Training and validation metrics for the second-stage prediction compare `generator2(fake_data)` against the real later target `data.y2`.

Therefore the second forecast is not conditionally independent of the first forecast. Its input lineage includes the generated t1 state.

## INFERRED HC lesson

A forecast derived from a previous forecast should inherit the complete prediction ancestry needed to determine:

- which ancestors were observed versus generated;
- which model/version produced each ancestor;
- the horizon and step index;
- uncertainty and calibration state inherited from prior stages;
- whether any ancestor has since been contradicted by observation;
- whether the chain crosses a material domain or regime shift;
- whether later predictions were recomputed after an observed correction.

This supports the invariant:

`CASCADED_FORECAST_DESCENDANT_INHERITS_ANCESTOR_PROVENANCE`

and the separations:

`FORECAST_OF_FORECAST != FORECAST_FROM_OBSERVED_STATE`

`PREDICTED_TIMEPOINT != OBSERVED_TIMEPOINT`

`DESCENDANT_CONFIDENCE != FRESH_INDEPENDENT_CONFIDENCE`

`LATER_HORIZON != NEW_EVIDENCE`

## HYPOTHESIS requiring execution-level verification

The inspected second-stage identity-loss expression uses:

```text
identity_loss(generator(swapped_data2), data.y2)
```

rather than an obvious `generator2(swapped_data2)` call. Static inspection alone cannot establish whether this is intentional parameter sharing logic, a benign artifact, or a defect affecting training. It should not be generalized into a claim about the paper or reported results without execution and author/context verification.

This is retained as an adversarial source-code fixture for HC qualification discipline:

`IMPLEMENTATION_IDENTIFIER_MISMATCH -> INSPECT / TEST; DO_NOT SILENTLY INFER INTENT`

## Forecast ancestry object candidate

A useful HC object could carry:

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

The object is a candidate architectural transfer, not source-native EvoGraphNet terminology.

## Failure modes exposed by the source pattern

- treating t2 prediction as if it were generated directly from observed t0 state when it actually depends on generated t1;
- presenting a multi-step chain as multiple independent pieces of supporting evidence;
- resetting uncertainty/confidence at each predicted horizon;
- recording predicted t1/t2 as historical events before observation;
- correcting t1 without invalidating/recomputing descendant t2 forecasts;
- hiding model/version changes between forecast stages;
- using forecast-chain depth as evidence strength;
- treating distribution alignment/adversarial success as observation.

## Transfer decision

PROMOTE THE GENERAL FORECAST-LINEAGE SEMANTICS, NOT THE SOURCE MODEL.

EvoGraphNet supplies concrete evidence that chained graph forecasting is an implemented computational pattern. HC should preserve forecast ancestry and uncertainty/currentness boundaries whenever one predicted state becomes an input to another prediction.
