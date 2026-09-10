# Source Information Ancestry and Derived State

Status: canonical identity-neutral architecture contract.

## Purpose

HC state is often shaped indirectly. A source may influence clustering, selection, routing, topology, normalization, calibration, compression, thresholds, model choice, memory admission, or another intermediate artifact without appearing in the final payload, loss function, action request, or write target.

Consequential provenance therefore includes **information influence**, not only object custody and destination.

> **Information that materially shaped a derived state remains part of that state's causal ancestry until a qualified transformation explicitly narrows the downstream claim or information-release scope. Omission from the final call or output does not erase influence.**

This contract complements executed-dataflow, evidence-isolation, protected-update, authority, memory, and representation-provenance rules.

## Core separations

`NOT_IN_FINAL_PAYLOAD != NOT_IN_CAUSAL_ANCESTRY`

`NOT_IN_FINAL_CALL_SIGNATURE != NOT_USED_UPSTREAM`

`LABEL_NOT_USED_IN_LOSS != LABEL_NOT_USED_TO_SHAPE_TRAINING_STATE`

`TRAINING_ONLY_WRITE_TARGET != TRAINING_ONLY_DECISION_ANCESTRY`

`AUTHORIZED_DESTINATION != AUTHORIZED_SOURCE_INFORMATION`

`ALLOWED_STATE_MUTATION != ALLOWED_INFORMATION_USE`

`TRANSFORMED_INFORMATION != PROVENANCE_FREE_INFORMATION`

`AGGREGATED_INFORMATION != AUTOMATICALLY_DECLASSIFIED_INFORMATION`

`SOURCE_FIELD_DROPPED != SOURCE_INFLUENCE_REMOVED`

`SAME_METHOD_NAME != SAME_INFORMATION_BOUNDARY`

`SAME_PREPROCESSOR != SAME_EXPOSURE_ANCESTRY_ACROSS_ENTRYPOINTS`

## Information-influence ancestry

For a consequential derived artifact, HC should be able to answer:

- which source states or evidence classes were visible to the derivation;
- whether they influenced selection, weighting, topology, thresholds, routing, fitting, or content;
- which transformation introduced the influence;
- whether the source was current, held out, private, authority-bearing, continuity-bearing, predicted, generated, or otherwise specially scoped;
- which downstream artifacts or decisions inherit the dependency;
- whether an explicit qualified release/declassification rule narrows what must remain protected downstream.

A useful conceptual record is:

```text
INFORMATION_ANCESTRY {
  artifact_id
  derivation_id
  direct_source_refs[]
  information_classes_visible[]
  influence_roles[]
  source_scope_or_partition[]
  authority_or_privacy_scope[]
  chronology_scope[]
  generated_or_observed_status[]
  downstream_dependency_refs[]
  release_or_declassification_ref
  qualification_ref
  provenance
}
```

The implementation may use another schema. What matters is preserving enough lineage to answer consequential information-flow questions.

## Influence roles

A source can shape downstream state through roles such as:

- direct content;
- target/label;
- selector or ranker;
- gate or threshold;
- clustering/partition assignment;
- topology construction or collapse;
- normalization/calibration statistics;
- feature selection;
- route or strategy choice;
- optimizer/scheduler feedback;
- compression or quantization calibration;
- template/manifold/reference construction;
- retrieval-index construction;
- confidence/uncertainty calibration;
- admission or rejection criteria;
- authority/consent checks;
- protected-state update eligibility.

A source can be causally material even when none of its values are copied verbatim into the result.

## Destination scope versus source-information scope

Controlling where a result may be written is not enough.

For example, a system may modify only ordinary plastic state while using protected identity state to choose which ordinary parameters to reinforce. Likewise, a training pipeline may remove only training nodes while using held-out labels to decide the removal pattern.

The destination is bounded, but the decision ancestry is broader.

Therefore consequence gates should distinguish:

1. **destination authority** — whether this state/effect may be changed;
2. **source-information authority** — whether each material input class may be used for this derivation;
3. **claim/evidence role** — whether using the source changes qualification or epistemic scope;
4. **release scope** — what information about the source may be exposed by the derived artifact.

Passing one dimension does not imply the others.

## Evaluation and held-out information

Held-out information can contaminate independence without entering the model's final forward/loss call.

A label can shape a cluster, topology, feature selector, threshold, checkpoint, sample set, or normalization path upstream. A later train/test split does not remove that ancestry.

`EVALUATION_LABEL_NOT_PASSED_TO_MODEL != EVALUATION_LABEL_NOT_USED_TO_SHAPE_TRAINING_ARTIFACT`

Evaluation qualification therefore follows the earliest material information use and the complete derived-state dependency chain.

Transductive use can be legitimate. It must be declared rather than described as inductive isolation.

## Protected, private, and authority-bearing information

The same logic applies beyond ML evaluation.

Examples of specially scoped source information include:

- private person-model evidence;
- consent/boundary state;
- actor authority;
- identity-continuity state;
- protected values/invariants;
- current versus historical memory;
- unreleased external data;
- future/predicted/generated state;
- safety-critical body telemetry.

A derived artifact does not automatically lose these source dependencies because its output schema omits the sensitive fields.

However, ancestry does not mean every descendant must inherit the strongest source restriction forever. A qualified transformation may establish a narrower release scope when it can demonstrate that the forbidden information or capability is not materially recoverable or usable beyond the allowed bound and the applicable governance permits that release.

`TRANSFORMATION != AUTOMATIC_DECLASSIFICATION`

`AGGREGATION != AUTOMATIC_PRIVACY_PROOF`

`REDACTION_OF_FIELD_NAMES != NONINFERENCE_PROOF`

The project does not prescribe one privacy/declassification technology. It requires explicit policy and evidence when a consequence depends on the claim that a transformation safely narrows source-information scope.

## Path-, configuration-, and entrypoint-specific scope

Information visibility can differ across implementations of the same named method.

One entrypoint may preprocess a training-only graph; another may invoke the same function on a full cohort. One mode may use labels while another assigns zero label weight. One route may use protected memory for gating while another does not.

Therefore:

`METHOD_LABEL != INFORMATION_FLOW_PROOF`

`CONFIGURED_ZERO_WEIGHT != VERIFIED_ZERO_EFFECT_WITHOUT_PATH_TEST`

`ENTRYPOINT_NAME != EVALUATION_REGIME`

Qualification should bind the claim to the exact configuration and effect path that was tested.

## Dependency and correction

If a source is later corrected, revoked, expired, reclassified, or found unauthorized, descendants whose material derivation depended on it may require reevaluation.

`SOURCE_INVALIDATED != DESCENDANT_AUTOMATICALLY_INVALID`

`SOURCE_INVALIDATED != DESCENDANT_AUTOMATICALLY_SAFE`

The required response depends on the influence role, transformation, downstream consequence, and whether a qualified release boundary broke the dependency for the relevant claim.

Historical ancestry remains preserved even if the current eligibility of the derived artifact changes.

## Adversarial conformance tests

1. **Hidden label influence** — keep final model call label-clean but use held-out labels to choose preprocessing topology; require ancestry/evaluation-scope failure.
2. **Destination-only gate** — authorize ordinary-state writes while feeding unauthorized protected identity state into the selector; require source-information governance failure.
3. **Dropped-field laundering** — derive an artifact from private evidence, remove the private fields from the output, and require the system not to declare the artifact unrestricted merely because the fields disappeared.
4. **Zero-weight claim** — configure a privileged information channel with nominal weight zero; require path-level evidence that it has no material effect before treating it as absent.
5. **Entrypoint divergence** — invoke the same preprocessor once on train-only data and once on train+evaluation data; require different ancestry/evaluation records.
6. **Evaluation-only perturbation** — hold training inputs fixed and perturb only held-out labels/structure; any change in a training artifact must expose held-out ancestry.
7. **Qualified release** — pass sensitive source state through an explicitly qualified release transform and verify downstream scope is narrowed only to the tested property and threat/usage model.
8. **Correction propagation** — invalidate a source after several derived selections; locate affected descendants without rewriting history or invalidating unrelated descendants.
9. **Indirect authority use** — omit an authority token from the final action payload but use it upstream to select a candidate; require authority ancestry to remain recoverable.
10. **Generated-state laundering** — use a prediction only to choose which observed evidence to surface; verify the output does not silently become prediction-independent when that selection materially changes the conclusion.

## Interfaces

Strong interfaces are expected with:

- `docs/architecture/EXECUTED_DATAFLOW_AND_BINDING_INTEGRITY.md`;
- `docs/architecture/QUALIFICATION_EVIDENCE_ISOLATION.md`;
- `docs/architecture/COMPOSITE_REPRESENTATION_AND_ELEMENT_PROVENANCE.md`;
- `docs/architecture/REPRESENTATION_FIDELITY_AND_OBJECTIVE_PROVENANCE.md`;
- `basic operating instructions/AUTHORITY_CONSENT_AND_EFFECT_GOVERNANCE.md`;
- `basic operating instructions/PROTECTED_INVARIANT_AND_UPDATE_GOVERNANCE.md`;
- current/deep memory and currentness selection;
- routing/plasticity;
- resolver/correction;
- kinesis/action gateway;
- person-model privacy/scope;
- temporal forecast lineage.

## Evidence boundary

This architecture contract generalizes recurring HC provenance/governance requirements and is reinforced by code-level source studies. BASIRA DuoGNN demonstrates that evaluation-cohort graph structure can shape a later training topology before a declared split. BASIRA FALCON provides a stronger source-information fixture: its inspected Cora feature-label collapse path reads features and labels from a full graph before producing the contracted training graph, while its PPI entrypoint contracts a separately constructed training graph. The contrast shows why information-boundary claims must be path-specific rather than method-name-specific.

These source implementations motivate the general contract. They are not HC mechanisms and the observations do not establish publication-level validity or invalidity.

## Governing invariant

> **HC provenance follows material information influence as well as object movement. Restricting the final payload or mutation destination cannot erase source-information ancestry; narrowing that ancestry's downstream protection or claim scope requires an explicit, qualified boundary.**
