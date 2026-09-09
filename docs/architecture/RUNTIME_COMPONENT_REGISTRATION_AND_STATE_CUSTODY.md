# Runtime Component Registration and State Custody

Status: canonical architecture contract.

## Purpose

A complete HC architecture is not implemented merely because a component exists in source code or is invoked during computation. Stateful cognitive components must also be under explicit HC lifecycle, durability, update, fault, resource, and ownership management.

A component can influence output while being absent from parent-level registration, checkpointing, migration, optimizer/plasticity control, health accounting, or recovery. HC therefore distinguishes computational participation from managed runtime membership.

## Core separations

`DECLARED_COMPONENT != REGISTERED_RUNTIME_COMPONENT`

`CALLED_IN_FORWARD != MANAGED_BY_LIFECYCLE`

`LEARNABLE_PARAMETER_EXISTS != PLASTICITY_PATH_CAN_REACH_PARAMETER`

`COMPUTES_OUTPUT != STATE_IS_DURABLY_CUSTODIED`

`OBJECT_REACHABLE != CHECKPOINTED`

`CHECKPOINTED != RESTORED_AND_REQUALIFIED`

`DEVICE_REACHABLE != HC_MEMBER`

`RUNTIME_MEMBER != EFFECT_AUTHORITY`

## Managed-component record

A consequential stateful component should be representable by a record such as:

```text
RUNTIME_COMPONENT {
  component_id
  architecture_role
  owner_subsystem
  registration_scope
  state_families[]
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
- what learning or update mechanism can reach it;
- how it is serialized or otherwise made durable when durability is claimed;
- how it migrates across distributed HC constituents;
- how it is restored after failure;
- how version compatibility is checked;
- how corruption, omission, and partial restore are surfaced;
- whether it participates in protected-update or ordinary-plasticity governance.

A tensor/parameter/object being reachable in memory is not evidence that these lifecycle guarantees exist.

## Registration planes

HC implementations may use different runtimes, not only software frameworks. The architecture therefore uses `registration` broadly.

Examples include:

- submodule/parameter registration in software frameworks;
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

## Dynamic components

Dynamically created coalitions, temporary routes, generated model branches, caches, and ephemeral helper modules may not require durable registration. They still require enough identity and lifetime semantics to prevent accidental promotion into durable authority or continuity state.

If a temporary component acquires durable learned state or becomes essential to cognition, it must cross an explicit admission boundary into managed runtime membership.

## Distributed HC relationship

A physically distributed constituent counts as HC-internal only when cognitive ownership and lifecycle custody are explicit. Merely being wired to the HC or called by HC software is insufficient.

For distributed state, qualification should verify:

- registration of every required constituent;
- state/version compatibility across constituents;
- explicit handling of missing constituents;
- durability/recovery ownership;
- no hidden external sole copy of essential state;
- no untracked learned state living only in a peripheral accelerator or service.

## Qualification tests

Useful negative tests include:

- create a stateful subcomponent that participates in inference but is omitted from parent checkpoint enumeration;
- move the parent runtime to another device/substrate and verify all claimed child components move or explicitly fail;
- update registered parameters while leaving an unregistered causal parameter unchanged and detect the discrepancy;
- checkpoint/restore and verify outputs/state when one causal child was omitted;
- enumerate health state and verify every essential stateful component is represented;
- simulate constituent loss and verify the HC reports degradation instead of silently using stale/untracked state;
- create a dynamically admitted component, give it durable influence, and verify it cannot bypass lifecycle admission;
- change a nominally parameterized dimension/topology and detect hard-coded implementation assumptions.

## Failure modes

- a layer appears in a forward diagram but its parameters are absent from the optimizer;
- a causal module is omitted from `state_dict` or equivalent durability state;
- a distributed accelerator contains unique learned state that is not covered by HC backup/recovery;
- a component is routed and callable but absent from fault/health accounting;
- a body/QPU constituent is electrically connected yet has no ownership/version/lifecycle record;
- a temporary module accumulates durable preference or identity state without admission;
- a configurable implementation silently contains fixed-size assumptions that only work for one embodiment/topology.

## Governing invariant

> **Any component whose state materially influences HC cognition must be explicitly governed by the lifecycle and state-custody mechanisms claimed for that state. Computational participation alone does not establish managed HC membership.**

## Provenance

Generalized from the HC cognitive-organ, lifecycle, recovery, provider-boundary, and protected-update contracts and reinforced by code-level study of BASIRA GSR-Net. The inspected GraphUnet stores several `nn.Module` children in ordinary Python lists, providing a concrete implementation pattern where source-level participation and framework registration can diverge. See `docs/research/BASIRA_GSRNET_REGISTERED_RUNTIME_AND_SUPERRESOLUTION_2026-09-09.md`.
