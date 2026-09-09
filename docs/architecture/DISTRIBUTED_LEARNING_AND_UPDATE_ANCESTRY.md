# Distributed Learning and Update Ancestry

Status: canonical identity-neutral architecture contract.

## Purpose

The HC may learn across multiple internal subsystems, physically distributed HC-owned constituents, model branches, embodiments, experiments, replicas, or externally supplied learning artifacts. When learned state is averaged, exchanged, distilled, copied, perturbed, merged, or otherwise transferred, the resulting state must retain enough ancestry to distinguish shared parameter/source history from independent evidence and to preserve protected-update boundaries.

This contract does **not** require federated learning. It governs provenance whenever distributed or multi-source learning is used.

## Core distinctions

`LOCAL_MODEL_AFTER_GLOBAL_AGGREGATION != INDEPENDENT_LOCAL_MODEL`

`MODEL_COUNT != INDEPENDENT_MODEL_ANCESTRY_COUNT`

`SEVERAL_PARTICIPANTS_WITH_SHARED_WEIGHTS != SEVERAL_INDEPENDENT_CORROBORATORS`

`REPLICA_COUNT != INDEPENDENT_SOURCE_COUNT`

`PERTURBED_OR_SUBSET_COPY != NEW_OBSERVATION_SOURCE`

`MULTIPLE_REPLICA_VOTES != MULTIPLE_INDEPENDENT_OBSERVERS`

`RECEIVED_MODEL_UPDATE != OBSERVED_REMOTE_DATA`

`PARAMETER_UPDATE_ANCESTRY != OBSERVATION_ANCESTRY`

`MODEL_KNOWLEDGE_TRANSFER != SOURCE_EVIDENCE_TRANSFER`

`MISSING_TIMEPOINT != OBSERVED_NO_CHANGE`

`SELF_ENCODING_OBJECTIVE != EVIDENCE_OF_TEMPORAL_STASIS`

`PREDICTED_BRIDGE_ACROSS_MISSING_TIMEPOINT != OBSERVED_INTERMEDIATE_STATE`

`AGGREGATION_ELIGIBILITY != UPDATE_AUTHORITY`

`PARTICIPANT_STRENGTH_SCORE != PROTECTED_UPDATE_AUTHORITY`

`GLOBAL_MODEL != COGNITIVE_EXECUTIVE`

`CENTRAL_COORDINATOR != SEMANTIC_AUTHORITY`

`NUMERICALLY_MERGED_STATE != PROVENANCE_FREE_STATE`

`DECLARED_WEIGHT != EFFECTIVE_INFLUENCE_WITHOUT_EXECUTION_TRACE`

## Parameter ancestry versus evidence ancestry

A learned model can inherit information from data it never directly exposes to another subsystem or participant. The receiving subsystem may legitimately use the transferred model/update while still lacking observation-level evidence from the original training cases.

Therefore HC records should distinguish:

- **observation ancestry** — which observations/events directly support a claim or state;
- **learning ancestry** — which training/adaptation episodes influenced learned state;
- **parameter ancestry** — which prior parameter/model states contributed to the current state;
- **evaluation ancestry** — which tests, holdouts, canaries, or feedback influenced selection/tuning;
- **authority ancestry** — which authorization allowed the update to be accepted and activated.

These can overlap but are not interchangeable.

A received model update must not fabricate observation records for private, unavailable, or otherwise unreceived source cases.

## Replicas, perturbations, and synthetic descendants

A replica, bootstrap sample, augmentation, perturbation, synthetic variant, or resampled descendant can add useful diversity without adding a new independent source ancestor.

If several descendants originate from one participant, one observation set, one pretrained model, one seed artifact, or one generated parent, that common ancestry remains recoverable when independence matters.

`GENERATED_OR_PERTURBED_VARIANTS != INDEPENDENT_SOURCE_OBSERVATIONS`

`MODEL_DIVERSITY != EVIDENCE_INDEPENDENCE`

Stochastic divergence, different hardware, distinct replica IDs, different excluded subsets, or different local optimizers do not erase shared ancestry.

Qualification and corroboration should count independence at the axis relevant to the claim. Several replica models may constitute several computational probes while still being one correlated evidence family.

## Distributed update record

A consequential distributed update should be representable as:

```text
DISTRIBUTED_UPDATE {
  update_id
  target_state_class
  contributor_ids[]
  contributor_model_versions[]
  contributor_parameter_ancestry[]
  contributor_learning_ancestry[]
  contributor_evaluation_ancestry[]
  source_ancestor_groups[]
  aggregation_or_transfer_method
  declared_contribution_weights[]
  measured_or_effective_influence[]
  ordering_or_pairing
  missingness_or_domain_conditions[]
  shared_ancestor_groups[]
  resulting_model_version
  activation_scope
  authority_basis
  qualification_status
  provenance
}
```

Not every implementation needs a heavyweight object for every low-consequence update. The architecture requires enough information to resolve independence, custody, correction, rollback, qualification, and authority questions proportional to consequence.

## Shared ancestry and independence

Two models that were once trained independently can become parameter relatives after averaging, copying, distillation, or weight exchange.

A later ensemble or multi-participant vote must not count the models as fully independent merely because they execute on different hardware or retain different participant IDs.

Independence is claim-relative. Examples:

- models may share parameters but be evaluated on genuinely independent observations;
- models may have independent parameters but be trained on overlapping data;
- models may share both parameter ancestry and evaluation sets;
- independently deployed models may still descend from one common pretrained ancestor;
- replicas may use different perturbed subsets while still descending from one client dataset.

`SHARED_PARAMETER_ANCESTRY != NO_USEFUL_DIVERSITY`

The rule is not to discard correlated contributors; it is to avoid laundering correlation into independent corroboration.

## Aggregation and transfer semantics

Permitted mechanisms may include:

- averaging;
- weighted averaging;
- pairwise exchange;
- distillation;
- merge/interpolation;
- adapter transfer;
- low-rank update transfer;
- gradient/update exchange;
- learned routing transfer;
- state-specific reconciliation.

The numerical transfer operator does not define semantic authority.

A declared coefficient or comment does not prove effective contribution weight after all scaling, averaging, clipping, normalization, repeated aggregation, sparsification, or routing steps. Consequential updates should permit basis/sentinel or equivalent influence tests at the actual mutation boundary.

`NAMED_EQUAL_WEIGHT_AGGREGATION != VERIFIED_EFFECTIVE_WEIGHT_SEMANTICS`

Before consequential activation, HC must know whether the transferred state is:

- ordinary plasticity;
- calibration;
- task/session adaptation;
- durable learned state;
- continuity-bearing memory/identity state;
- protected architecture/state.

Protected state cannot be smuggled through an update channel merely because ordinary learned parameters are allowed through it.

## Missingness and self-supervision

When an expected observation is missing, the HC may use self-supervision, interpolation, imputation, reconstruction, forecast chaining, or other learned priors. The provenance class remains explicit.

Missingness does not establish that the underlying state stayed the same.

A self-encoding or identity objective is a training constraint, not an observation of temporal stasis.

If generated states bridge a missing interval and then feed later prediction, forecast-lineage rules apply to every descendant.

## Evaluation feedback

Distributed learning often evaluates participants repeatedly and may use those scores to control learning-rate schedules, contributor weighting, ordering, stopping, model selection, transfer direction, or aggregation eligibility.

Any such use is adaptation/selection feedback.

`EVALUATION_FEEDBACK_USED_TO_MODIFY_OPTIMIZATION != UNTOUCHED_HOLDOUT_EVIDENCE`

This includes indirect control changes such as scheduler steps, contributor ranks, thresholds, routing, or model-exchange order—not only direct gradient updates.

Qualification evidence roles must be updated accordingly.

## Executed strategy and target binding

A selected aggregation strategy, supplied target argument, contributor list, mask, or state class must be traced to the operation that actually changes learned state or computes the qualification metric.

`CONFIGURED_STRATEGY != EXECUTED_STRATEGY_WITHOUT_PATH_VERIFICATION`

`TARGET_ARGUMENT_PRESENT != TARGET_DATA_EXECUTED`

`METHOD_SIGNATURE != DATAFLOW_PROOF`

The caller passing the intended object does not establish that the callee or downstream transform consumes that object. Distributed-learning qualification inherits the repository-wide executed-dataflow and referential-lineage rules.

## Internal distributed HC versus external contributors

Physically distributed HC-owned constituents can participate in one cognitive organ if they satisfy HC membership, lifecycle, state-custody, recovery, and continuity rules.

External contributors, services, or training systems remain outside the cognitive-organ boundary unless explicitly incorporated as HC constituents under the physical-membership contract.

An external coordinator may propose or compute an update. It cannot become the seat of cognition, current memory, identity, values, consent, or protected-update authority.

`EXTERNAL_AGGREGATOR != HC_EXECUTIVE`

`EXTERNAL_UPDATE_PROVIDER != PROTECTED_STATE_AUTHORITY`

If an external service is unavailable, the HC's essential cognitive continuity must remain conforming within the scope required by the cognitive-organ boundary.

## Correction, rollback, and lineage

If a contributor or upstream model is later found corrupted, poisoned, miscalibrated, unauthorized, incorrectly bound to target data, or based on invalid evidence, ancestry must permit affected descendants to be located.

Possible outcomes include:

- mark affected descendants for requalification;
- recompute without the contributor;
- roll forward from a clean ancestor;
- revert only non-continuity-bearing state where safe;
- preserve historical parameter ancestry while removing current eligibility;
- quarantine uncertain descendants pending adjudication.

`CONTRIBUTOR_INVALIDATED != HISTORY_ERASED`

`ROLLBACK_TARGET != AUTOMATICALLY_SAFE_CURRENT_STATE`

Rollback remains subject to continuity-safe update governance.

## Adversarial conformance tests

1. **Shared-weight vote** — aggregate several participant models and then ask for a multi-model vote; verify parameter ancestry prevents naive counting as fully independent model evidence.
2. **Replica inflation** — derive many perturbed/subset replicas from one participant and verify independent source/support count does not rise merely with replica count.
3. **Remote-update provenance** — transfer a learned model update without source observations; verify the receiver gains update ancestry but no fabricated observation-level evidence.
4. **Missing follow-up** — train with self-reconstruction or generated bridging across an absent timepoint; verify missing state is not relabeled as observed no-change.
5. **Protected-state smuggling** — combine ordinary learned parameters with a protected state field in one update payload; require typed rejection or separate authorized handling.
6. **Strength-score authority** — rank contributors by data completeness/performance; verify the strongest contributor does not thereby gain identity/value/consent/protected-update authority.
7. **Evaluation-controlled aggregation** — use held-out scores to change scheduler, contributor weight, transfer order, or selection; require reclassification of those scores from untouched holdout evidence.
8. **Common-ancestor ensemble** — fork many descendants from one model and aggregate/vote them; verify independence accounting preserves common ancestry.
9. **Effective-weight probe** — configure known contributor weights and basis-vector parameter fixtures; verify the measured output coefficients match the declared aggregation semantics after every transform.
10. **Target-binding probe** — supply source and target sentinel fixtures whose values cannot be confused; verify the actual learning/evaluation path consumes the declared target rather than a source-derived surrogate.
11. **Contributor invalidation** — invalidate one upstream contributor after downstream merges; verify affected descendants can be identified without rewriting historical lineage.
12. **External aggregator outage** — remove a true external aggregation service; verify essential HC cognition and continuity do not disappear solely because the service is unavailable.

## Interfaces

Strong interfaces are expected with:

- runtime component registration/state custody;
- reference identity/index lineage;
- representation fidelity and executed-path verification;
- plasticity and state governance;
- protected update governance;
- qualification evidence isolation;
- temporal forecast lineage;
- composite representation provenance;
- current/deep memory;
- resolver/correction;
- cognitive-organ and physical-membership boundaries;
- distributed arbitration and routing.

## Evidence boundary

This is an HC architecture contract generalized from existing HC provenance, qualification, forecast, and protected-update rules plus code-level study of distributed longitudinal and replica-based graph-learning systems.

The source studies motivate ancestry, target-binding, missingness, evaluation-feedback, and effective-influence distinctions. They do not establish that federated learning, model averaging, replicas, or any specific participant-ordering scheme is required or optimal for HC.

See:

- `docs/research/BASIRA_4D_FED_GNN_DISTRIBUTED_LEARNING_2026-09-09.md`
- `docs/research/BASIRA_REPFL_REPLICA_ANCESTRY_AND_TARGET_DATAFLOW_2026-09-09.md`

## Governing invariant

> **Learned state may move, replicate, and merge without moving or multiplying the underlying observations or authority. Parameter/source ancestry, evidence ancestry, missingness, target binding, effective contributor influence, evaluation feedback, and protected-update permission remain explicit across every distributed learning transfer.**
