# BASIRA 4D-FED-GNN Distributed-Learning Study — 2026-09-09

Status: NON-CANONICAL RESEARCH / SOURCE STUDY

## Source cuts

Repositories:

- `basiralab/4D-FED-GNN`, default branch `main`
  - `README.md` blob `9e5dd5ad85ce56828b73e19a098db3d0deedf1b8`
  - `demo.py` blob `330af257ea735f1923416e6a569019b29b2fb49a`
- `basiralab/4D-FedGNN-Plus`, default branch `main`
  - `README.md` blob `f344571511be33afcc7911e0398afb8ad5848fff`
  - `demo.py` blob `d3b738c3ac1450ae4a1a139f60cc08a1921a9549`

These repositories are studied as distributed-learning and temporal-missingness patterns. They do not establish a requirement that HC use federated learning or any external hospital/server architecture.

## Documented source intent

DOCUMENTED from both READMEs: the framework predicts longitudinal graph evolution across decentralized datasets with different/missing acquisition timepoints. The described strategy combines local GNN learning with central layer/weight averaging and model-weight exchange. The ++ variant additionally orders participants from their incomplete sequential patterns; later experiments describe transfer from stronger to weaker participants based on data availability, sample quality, and model performance.

The README also describes a model acting as a graph self-encoder when a next local timepoint is missing and a graph generator when follow-up data is locally available.

## Observed aggregation and exchange

OBSERVED in `4D-FED-GNN/demo.py`:

1. Each hospital owns timepoint-specific models and optimizers.
2. `update_main_by_average` copies model state dictionaries, averages each float32 state entry with equal coefficient `1 / len(hospitals)`, and loads the resulting shared state into every hospital model for that timepoint.
3. `exchange_models` rotates copied model state dictionaries among hospitals.
4. Validation predicts the first future state from baseline, then feeds each prediction into the next timepoint-specific model, preserving a forecast-of-forecast chain.

OBSERVED in `4D-FedGNN-Plus/demo.py`:

5. `update_main_by_average_gnns` likewise averages model state dictionaries across hospitals and broadcasts the resulting state to every hospital.
6. `exchange_models_based_on_order_gnns` transfers whole model states along a participant order.
7. `get_order_gnns` ranks hospitals using count of available timepoints and gaps between available timepoints.
8. During training, if the next timepoint is missing, the model may recursively predict through missing positions until a later available timepoint is reached; the eventual available state supplies loss.
9. The validation-during-training path uses a fold variable named `test_data`, computes participant validation losses every configured interval, and feeds each participant's mean validation loss to its scheduler with `scheduler.step(l)`.

Item 9 establishes feedback from the held-out/evaluation path into training-control state in the inspected implementation. Whether the publication treats this exact fold as final test evidence requires claim-level review; the HC transfer is the narrower rule that evaluation feedback used to modify optimization state is not untouched independent evidence for the modified successor.

## Distributed update ancestry

Once model states are averaged or transferred, the resulting participants no longer have independent parameter ancestry.

`LOCAL_MODEL_AFTER_GLOBAL_AGGREGATION != INDEPENDENT_LOCAL_MODEL`

`MODEL_COUNT != INDEPENDENT_MODEL_ANCESTRY_COUNT`

`SEVERAL_PARTICIPANTS_WITH_SHARED_WEIGHTS != SEVERAL_INDEPENDENT_CORROBORATORS`

A post-aggregation model can still be evaluated separately at several sites or datasets, but independence must be assessed at the level relevant to the claim. Shared parameter ancestry and independent evaluation evidence are different axes.

## Weight transfer versus evidence transfer

A remote model update can encode information learned from remote data without exposing those source observations directly. That does not make the receiving participant an observer of the remote cases.

`RECEIVED_MODEL_UPDATE != OBSERVED_REMOTE_DATA`

`PARAMETER_UPDATE_ANCESTRY != OBSERVATION_ANCESTRY`

`MODEL_KNOWLEDGE_TRANSFER != SOURCE_EVIDENCE_TRANSFER`

If a learned update affects HC beliefs or policy, its provenance should identify the update source/training lineage without fabricating source observations the HC never received.

## Missing-timepoint semantics

A missing timepoint is absence of an observation, not evidence that the system was unchanged.

`MISSING_TIMEPOINT != OBSERVED_NO_CHANGE`

`SELF_ENCODING_OBJECTIVE != EVIDENCE_OF_TEMPORAL_STASIS`

`PREDICTED_BRIDGE_ACROSS_MISSING_TIMEPOINT != OBSERVED_INTERMEDIATE_STATE`

A self-reconstruction objective can be a regularizer, prior, or local adaptation strategy. A recursively generated bridge can support prediction. Neither changes the epistemic class of the missing interval into observation.

This reinforces temporal forecast lineage: if a later forecast consumes generated states across a missing interval, all descendants retain that generated ancestry.

## Aggregation authority and protected state

The inspected source intentionally broadcasts averaged or exchanged model state. HC may use analogous distributed update mechanisms internally, but the mechanism itself cannot define update authority.

`AGGREGATION_ELIGIBILITY != UPDATE_AUTHORITY`

`PARTICIPANT_STRENGTH_SCORE != PROTECTED_UPDATE_AUTHORITY`

`GLOBAL_MODEL != COGNITIVE_EXECUTIVE`

`CENTRAL_COORDINATOR != SEMANTIC_AUTHORITY`

A distributed HC implementation must separately determine which state classes may be aggregated, which are protected, whether updates can cross identity/value/consent/memory boundaries, how conflicts are handled, and whether the update remains within the cognitive-organ boundary.

## Contribution provenance

For consequential distributed updates, a composite update should retain enough lineage to answer:

- which participants contributed;
- participant/model versions;
- aggregation/exchange algorithm and ordering;
- contribution weights or effective influence when known;
- source training/evaluation scope;
- missingness/domain conditions;
- whether contributors already shared ancestry before this round;
- validation/tuning evidence used to select or schedule the update;
- protected-update classification and authority basis when applicable.

Averaging can numerically erase participant labels while provenance still needs to preserve causal contribution history.

`NUMERICALLY_MERGED_STATE != PROVENANCE_FREE_STATE`

## Static implementation anomaly: strategy selector versus executed ordering function

OBSERVED in the inspected `train_gnns_final` path: the code assigns a local `get_order` function based on `args.mode` (`get_order_weighted` for weighted exchange, otherwise `get_order_gnns`), but the training loop later sets `ordered_hospitals = get_order_gnns(table)` directly instead of calling the selected `get_order` variable.

This means the visible strategy-selection assignment does not, in that path, prove that the selected ordering function governs the executed ordering computation.

`CONFIGURED_STRATEGY != EXECUTED_STRATEGY_WITHOUT_PATH_VERIFICATION`

Status: OBSERVED static control-flow mismatch; quantitative effect and intended semantics are UNKNOWN without execution/author confirmation.

HC transfer: configuration claims, feature flags, selected policy objects, and declared modes should be checked at the effect path. Merely assigning/selecting a strategy is not proof that the strategy actually controls the resulting update.

## Evaluation-feedback contamination

The inspected ++ training path provides a concrete implementation pattern where evaluation loss can modify a learning-rate scheduler during training.

HC qualification transfer:

`EVALUATION_FEEDBACK_USED_TO_MODIFY_OPTIMIZATION != UNTOUCHED_HOLDOUT_EVIDENCE`

This remains true whether the feedback changes weights directly, changes a scheduler, selects checkpoints, changes stopping time, changes routing, or selects among update strategies.

## Suggested adversarial tests

1. Train four participants independently, aggregate them, then ask whether four post-aggregation predictions are four independent model votes; require ancestry accounting to reject naive independence.
2. Send only a model update from participant A to B; verify B does not gain fabricated observation records for A's private source cases.
3. Train through a missing intermediate timepoint by recursive prediction; verify the intermediate state and descendants remain generated rather than observed.
4. Use a self-encoding loss when follow-up is absent; verify the system does not infer `no change` as a factual temporal observation.
5. Rank contributors by performance or data completeness; verify rank cannot confer authority to change protected identity/value/consent/memory state.
6. Average a mixture of ordinary-plasticity and protected-state parameters; require rejection or typed separation before activation.
7. Feed evaluation loss into a scheduler, threshold, routing rule, or update-selection process; require that evaluation evidence be reclassified as tuning/selection evidence for the changed successor.
8. Aggregate participants that already share a recent ancestor; verify the provenance graph records common ancestry instead of counting them as independent contributors.
9. Select two distinct ordering strategies through configuration and verify the executed ordering function changes accordingly; fail if a hard-coded path silently bypasses the selected strategy.

## Transfer decision

PROMOTE GENERAL DISTRIBUTED-LEARNING ANCESTRY AND MISSINGNESS SEMANTICS; DO NOT PROMOTE FEDERATED LEARNING AS AN HC REQUIREMENT.

Useful canonical rules:

- shared/aggregated model ancestry is explicit;
- model-update provenance is distinct from source-observation provenance;
- missing follow-up is not temporal stasis;
- generated bridging states retain forecast ancestry;
- aggregation/participant strength does not confer protected authority;
- evaluation feedback that changes optimization state contaminates untouched-holdout status;
- configured strategy is verified at the executed effect path when the distinction is material.

## Evidence boundary

DOCUMENTED: framework goals and high-level strategies from repository READMEs.

OBSERVED: state-dict averaging, model-state exchange, recursive missing-timepoint prediction, participant ordering, evaluation-loss scheduler feedback, and the strategy-selector/executed-ordering mismatch from inspected source files.

INFERRED: HC distributed-learning provenance and authority requirements.

UNKNOWN: whether every published result uses the exact inspected demo paths, the privacy properties of a deployed implementation, the quantitative contribution of any one federation mechanism, and whether the ordering mismatch is intentional or corrected elsewhere.
