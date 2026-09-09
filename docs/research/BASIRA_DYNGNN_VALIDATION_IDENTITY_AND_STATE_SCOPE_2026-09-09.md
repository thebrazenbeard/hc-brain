# BASIRA DynGNN Validation Identity and State-Scope Study — 2026-09-09

Status: NON-CANONICAL RESEARCH / SOURCE STUDY

## Source cut

Repository: `basiralab/DynGNN`, default branch `main`.

Primary inspected artifacts:

- `README.md` blob `2d6f710bda7afc229e64d05c1c702a73f45ea24b`
- `demo.py` blob `cd1635eb33d09ffdd4aa7a0acc636130b4b07aff`
- `models/model_rbgm.py` blob `f1972a78edbf0f43d34cb7278a799645cf2397e6`

This note records implementation patterns relevant to HC index lineage, temporal-state scope, and qualification discipline. It does not establish that the published method or reported results are invalid.

## DOCUMENTED source framing

The README describes DynGNN as a dynamic memory-enhanced GNN for temporal brain-connectivity prediction. The implementation uses longitudinal subject graphs and reports graph-prediction and memory-capacity losses.

## OBSERVED validation-index anomaly

In `demo.py`, training data and memory-capacity labels are split into training and validation portions.

The subject split is:

```text
validation_subjects = train_data[validation_split:]
```

but the corresponding validation memory-capacity slice is:

```text
validation_mem_cap_subjects = train_mem_cap[:validation_split]
```

The validation function then indexes `mem_cap_data[n_subject, t + 1]` using the local position of each validation subject.

Therefore the inspected implementation does not demonstrate that validation subject position `n_subject` is bound to the memory-capacity record for that same subject. The slices originate from different portions of the parent arrays.

This is a concrete instance of:

`PARALLEL_ARRAY_POSITION != PROVEN_SAME_ENTITY`

`SAME_LOCAL_POSITION != SAME_SOURCE_REFERENT`

`SAME_SHAPE_OR_INDEX_RANGE != VERIFIED_CORRESPONDENCE`

The exact quantitative effect on reported results is UNKNOWN without execution against the released data and result pipeline. The source-level mismatch should not be inflated into a publication-level validity claim.

## HC transfer: parallel-view identity binding

Whenever two arrays, tensors, tables, graphs, labels, masks, forecasts, or metadata views are expected to describe the same entities, positional parallelism is insufficient after any independent split, filter, shuffle, sort, crop, batching operation, or reconstruction.

HC should preserve one of:

- stable referent IDs carried in both views;
- one verified shared index lineage tied to the exact transform;
- an explicit correspondence map whose scope/version is recoverable.

A useful invariant is:

`PARALLEL_VIEW_BINDING_REQUIRES_SHARED_REFERENTIAL_LINEAGE`

If the entity binding cannot be established, the relation between feature/state and label/metadata is UNKNOWN rather than guessed from matching position.

## Recurrent-state scope observation

`models/model_rbgm.py` defines an `RNNCell` with mutable `hidden_state`; each forward call reads the prior hidden state and replaces it with `y.detach()`.

This demonstrates that an inference call can carry forward causal state that is not represented by the explicit input argument alone.

The HC transfer is not that recurrent state is bad. The requirement is that state lifetime and referent scope be explicit.

`RECURRENT_STATE_PRESENT != CROSS_ENTITY_CARRYOVER_AUTHORIZED`

`PREVIOUS_FORWARD_STATE != CURRENT_ENTITY_CONTEXT`

A recurrent state may be validly scoped to a sequence, task, coalition, subject, conversation, sensor stream, or persistent learned process. It must not silently leak across unrelated referents merely because the same runtime object is reused.

## Sequence-boundary requirement

For mutable temporal state, a conforming implementation should be able to answer:

- which referent or sequence owns the state;
- whether state persists across timepoints within that referent;
- when reset is required;
- whether a new entity/episode inherits prior state;
- how batching or reordered evaluation affects state;
- whether checkpoint/restart preserves or resets it;
- whether state is ephemeral context, learned parameter state, current memory, or deep memory.

This strengthens but does not replace the existing runtime-state-custody contract.

## Adversarial tests suggested

1. Split features and labels with intentionally different index ranges but equal lengths; require an identity-lineage failure rather than positional acceptance.
2. Shuffle only one of two supposedly parallel views; require mismatch detection before evaluation.
3. Permute subject order while preserving stable IDs; require the metric result to remain bound to the same entities.
4. Reuse one recurrent model object across two unrelated subjects without reset; require the state-scope contract to declare whether carryover is permitted.
5. Evaluate identical subject data in two different subject orders; if output changes because of hidden carryover, require the dependency to be surfaced and qualified.
6. Restart the runtime mid-sequence; require the declared recurrent-state lifetime to determine whether restore or reset is correct.
7. Rename a recurrent tensor `memory`; verify it does not thereby become HC autobiographical/current/deep memory.

## Transfer decision

PROMOTE GENERAL PARALLEL-VIEW REFERENTIAL BINDING AND RECURRENT-STATE SCOPE RULES; DO NOT PROMOTE THE SOURCE ANOMALY INTO A CLAIM ABOUT PUBLICATION VALIDITY.

Useful canonical rules:

- positional alignment across independently transformed views is not identity proof;
- same local index in two slices does not establish same source referent;
- recurrent causal state has an explicit owner/scope/lifetime;
- cross-entity recurrent carryover requires an explicit contract;
- validation metrics require verified feature/target referential alignment.

## Evidence boundary

DOCUMENTED: DynGNN framing from repository README.

OBSERVED: validation-subject versus validation-memory-capacity slice mismatch and mutable recurrent hidden state from inspected source files.

INFERRED: HC index-lineage and recurrent-state-scope requirements.

UNKNOWN: quantitative effect of the validation mismatch, whether unretrieved revisions correct it, and whether published experiments used exactly this source cut.
