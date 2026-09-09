# Runtime Component Registration and State Custody

Status: canonical architecture contract.

## Purpose

A complete HC architecture is not implemented merely because a component exists in source code or is invoked during computation. Stateful cognitive components must also be under explicit HC lifecycle, durability, update, fault, resource, and ownership management.

A component can influence output while being absent from parent-level registration, checkpointing, migration, optimizer/plasticity control, health accounting, or recovery. A registered component can also create or mutate material causal state after initialization that is itself outside the claimed custody path. HC therefore distinguishes computational participation and owner registration from managed state membership.

## Core separations

`DECLARED_COMPONENT != REGISTERED_RUNTIME_COMPONENT`

`CALLED_IN_FORWARD != MANAGED_BY_LIFECYCLE`

`REGISTERED_COMPONENT != ALL_CAUSAL_STATE_REGISTERED`

`LEARNABLE_PARAMETER_EXISTS != PLASTICITY_PATH_CAN_REACH_PARAMETER`

`COMPUTES_OUTPUT != STATE_IS_DURABLY_CUSTODIED`

`OBJECT_REACHABLE != CHECKPOINTED`

`DYNAMIC_ATTRIBUTE_EXISTS != DURABLE_STATE_CUSTODY`

`LEARNED_DURING_FORWARD != AUTOMATICALLY_CHECKPOINTED`

`INFERENCE_CALL != NECESSARILY_STATE_PURE`

`PREDICTION_RETURNED != NO_LEARNING_OCCURRED`

`CHECKPOINTED != RESTORED_AND_REQUALIFIED`

`DEVICE_REACHABLE != HC_MEMBER`

`RUNTIME_MEMBER != EFFECT_AUTHORITY`

`RECURRENT_STATE_PRESENT != CROSS_ENTITY_CARRYOVER_AUTHORIZED`

`PREVIOUS_FORWARD_STATE != CURRENT_ENTITY_CONTEXT`

## Managed-component record

A consequential stateful component should be representable by a record such as:

```text
RUNTIME_COMPONENT {
  component_id
  architecture_role
  owner_subsystem
  registration_scope
  state_families[]
  state_owner_or_referent_scope
  learning_or_update_path
  durability_or_checkpoint_path
  substrate_or_device_assignment
  health_and_fault_reporting
  resource_accounting
  recovery_behavior
  compatibility_version
  authority_scope
  provenance
}
```

Not every component requires all fields to be complex. The system must be able to establish whether each material stateful component is actually governed by the mechanisms claimed for it.

## State custody

State that can materially influence cognition must have an explicit custody path.

For mutable/learned state this includes, where applicable:

- who may update it;
- which referent, sequence, task, coalition, session, body, or organism scope owns it;
- what learning or update mechanism can reach it;
- intended state family and lifetime;
- whether loss on restart is allowed;
- how it is serialized or otherwise made durable when durability is claimed;
- how it migrates across distributed HC constituents;
- how it is restored after failure;
- how version compatibility is checked;
- how corruption, omission, and partial restore are surfaced;
- whether replay/recomputation is a permitted substitute for storage and under what determinism/provenance assumptions;
- whether it participates in protected-update, ordinary-plasticity, bounded-adaptation, calibration, or ephemeral-working-state governance.

A tensor/parameter/object being reachable in memory is not evidence that these lifecycle guarantees exist.

Likewise, registering the owner component does not prove that dynamically assigned state created after initialization participates in checkpointing, migration, device/substrate movement, update governance, or recovery.

## State lifetime classes

Implementations may use finer taxonomies, but material mutable state should make its intended lifetime recoverable. Useful classes include:

- `REQUEST_EPHEMERAL` — scratch state disposable after one bounded operation;
- `TASK_EPHEMERAL` — state retained for one task/coalition but not across durable restart;
- `SESSION_ADAPTIVE` — learned/calibrated state intentionally scoped to a session or embodiment episode;
- `DURABLE_LEARNED` — state expected to survive normal restart and migration;
- `CONTINUITY_BEARING` — durable state relevant to memory/identity/currentness continuity;
- `PROTECTED_STATE` — state whose mutation requires protected-update or equivalent high-consequence governance.

`EPHEMERAL_BY_DESIGN != ACCIDENTALLY_UNCHECKPOINTED`

A state item may change class only through the relevant admission/promotion process. A cache or task-local adaptation cannot silently become durable preference, value, identity, memory authority, or protected architecture.

## Referent and sequence scope

Mutable temporal state may validly persist across several calls, but persistence has to be attached to a declared scope.

Possible scopes include:

- one request;
- one temporary coalition;
- one perceptual stream;
- one body-control episode;
- one conversation/task;
- one modeled external agent;
- one subject/entity sequence;
- one organism session;
- organism-wide durable learned state.

A runtime object being reused does not itself authorize state carryover between those scopes.

`OBJECT_REUSE != STATE_SCOPE_CONTINUITY`

`SAME_MODEL_INSTANCE != SAME_REFERENT`

`NEXT_CALL != NEXT_EVENT_IN_SAME_SEQUENCE`

When a component uses hidden/recurrent/reservoir state, its contract should specify reset, retain, fork, merge, transfer, checkpoint, and invalidation behavior at sequence boundaries. If a batch, ordering, or referent switch can alter outputs through hidden carryover, that dependency must be surfaced rather than treated as pure function behavior.

Cross-entity carryover may be intentional in some architectures, but then it is a modeled shared-state mechanism and requires provenance/authority appropriate to that role. Silent leakage is not equivalent to intentional shared context.

## Registration planes

HC implementations may use different runtimes, not only software frameworks. The architecture therefore uses `registration` broadly.

Examples include:

- submodule/parameter/buffer registration in software frameworks;
- service/component registration in HC runtime fabric;
- hardware constituent enumeration;
- routing/subscription registration;
- memory-segment custody registration;
- endocrine/interoceptive constituent registration;
- QPU/accelerator ownership and compatibility registration;
- body-interface capability registration.

Each registration plane has different semantics. Registration in one plane does not automatically imply registration in another.

`ROUTED_COMPONENT != CHECKPOINTED_COMPONENT`

`CHECKPOINTED_COMPONENT != HEALTH_MONITORED_COMPONENT`

`HEALTH_MONITORED_COMPONENT != UPDATE_AUTHORIZED_COMPONENT`

`CHILD_COMPONENT_REGISTERED != CHILD_DYNAMIC_STATE_GOVERNED`

## Dynamic components and dynamic state

Dynamically created coalitions, temporary routes, generated model branches, caches, and ephemeral helper modules may not require durable registration. They still require enough identity and lifetime semantics to prevent accidental promotion into durable authority or continuity state.

If a temporary component or dynamically created state item acquires durable learned influence or becomes essential to cognition, it must cross an explicit admission boundary into managed runtime membership/state custody.

An implementation must also declare when an operation that appears to be inference, retrieval, scoring, or prediction may fit parameters, calibrate state, update a reservoir/recurrent state, alter routing, or otherwise mutate material learned state.

Read-like API shape is not sufficient evidence of state purity.

Where an inference-like call can adapt from supplied examples or outcomes, that mutation must preserve normal learning provenance and qualification-evidence isolation.

## Memory terminology boundary

Mechanism-level recurrent, reservoir, cache, attention, or hidden state may legitimately provide computational memory. That does not make it HC current-memory, deep-memory, or autobiographical continuity state.

`MODEL_MEMORY != HC_CURRENT_MEMORY`

`MODEL_MEMORY != HC_DEEP_MEMORY`

`RECURRENT_STATE != AUTOBIOGRAPHICAL_CONTINUITY`

Memory-family labels must follow semantic role and custody, not source-library terminology.

## Distributed HC relationship

A physically distributed constituent counts as HC-internal only when cognitive ownership and lifecycle custody are explicit. Merely being wired to the HC or called by HC software is insufficient.

For distributed state, qualification should verify:

- registration of every required constituent;
- enumeration of every material causal state family inside each constituent;
- state/version compatibility across constituents;
- explicit handling of missing constituents;
- durability/recovery ownership;
- no hidden external sole copy of essential state;
- no untracked learned state living only in a peripheral accelerator or service.

## Qualification tests

Useful negative tests include:

- create a stateful subcomponent that participates in inference but is omitted from parent checkpoint enumeration;
- register a parent/child component correctly, then create a new causal tensor/state attribute after initialization and verify durability qualification catches it when persistence is claimed;
- move the parent runtime to another device/substrate and verify all claimed child components and material dynamic state move, are recomputed under declared rules, or explicitly fail;
- update registered parameters while leaving an unregistered causal parameter unchanged and detect the discrepancy;
- checkpoint/restore and verify outputs/state when one causal child or dynamic state item was omitted;
- restart between fitting dynamic output/adaptation state and prediction and verify behavior matches the declared lifetime;
- run an inference-like interface with adaptation side input and verify the state mutation is recorded rather than classified as pure inference;
- reuse one recurrent runtime object across two unrelated referents and verify reset/retention follows declared state scope;
- reorder independent entity sequences and detect any output change caused by unauthorized hidden-state carryover;
- enumerate health state and verify every essential stateful component is represented;
- simulate constituent loss and verify the HC reports degradation instead of silently using stale/untracked state;
- create a dynamically admitted component, give it durable influence, and verify it cannot bypass lifecycle admission;
- relabel recurrent/reservoir state as model-working state and verify it cannot silently acquire autobiographical current/deep-memory semantics;
- change a nominally parameterized dimension/topology and detect hard-coded implementation assumptions.

## Failure modes

- a layer appears in a forward diagram but its parameters are absent from the optimizer;
- a causal module is omitted from `state_dict` or equivalent durability state;
- a registered component creates learned causal tensors later that are absent from checkpoint/migration/recovery;
- an inference-like function performs fitting or adaptation without declaring state mutation;
- recurrent hidden state from one entity silently influences another because the model object was reused without a scope transition;
- evaluation order changes outputs because state carryover is undeclared;
- a distributed accelerator contains unique learned state that is not covered by HC backup/recovery;
- a component is routed and callable but absent from fault/health accounting;
- a body/QPU constituent is electrically connected yet has no ownership/version/lifecycle record;
- a temporary module accumulates durable preference or identity state without admission;
- mechanism-level `memory` terminology is mistaken for HC autobiographical/current/deep memory;
- a configurable implementation silently contains fixed-size assumptions that only work for one embodiment/topology.

## Governing invariant

> **Any component or dynamically created state whose content materially influences HC cognition must be explicitly governed by the lifecycle, referent-scope, and state-custody mechanisms claimed for that state. Component registration and computational participation alone do not establish complete managed HC membership.**

## Provenance

Generalized from the HC cognitive-organ, lifecycle, recovery, provider-boundary, and protected-update contracts and reinforced by code-level studies of BASIRA GSR-Net and DynGNN.

GSR-Net supplies a concrete pattern where `nn.Module` children can participate in forward computation while being stored outside ordinary framework registration. DynGNN supplies complementary patterns where a registered child module dynamically assigns recurrent/learned causal tensors after initialization, an inference-like high-level call can fit output state before prediction, and recurrent hidden state persists across forward calls. These source mechanisms motivate custody and scope tests; source-specific implementation choices are not imported as HC design requirements.

See:

- `docs/research/BASIRA_GSRNET_REGISTERED_RUNTIME_AND_SUPERRESOLUTION_2026-09-09.md`
- `docs/research/PYTORCH_MODULE_REGISTRATION_PROBE_2026-09-09.md`
- `docs/research/BASIRA_DYNGNN_DYNAMIC_MEMORY_CUSTODY_2026-09-09.md`
- `docs/research/BASIRA_DYNGNN_VALIDATION_IDENTITY_AND_STATE_SCOPE_2026-09-09.md`
