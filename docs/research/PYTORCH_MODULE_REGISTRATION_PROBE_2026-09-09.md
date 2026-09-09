# PyTorch Module Registration Probe — 2026-09-09

Status: OBSERVED LOCAL VALIDATION / RESEARCH PROVENANCE

## Purpose

Validate the generic framework behavior underlying the GSR-Net static finding: whether an `nn.Module` placed only inside an ordinary Python list owned by a parent `nn.Module` is managed by the parent's normal parameter/state/device mechanisms.

This is a minimal local probe, not execution of BASIRA GSR-Net.

## Environment

Python execution environment available to the Warden on 2026-09-09, with installed PyTorch.

Exact package version was not recorded in this probe, so the result is scoped to the executed environment plus separately documented current PyTorch semantics.

## Probe

Two parent modules were instantiated:

1. `PlainList`: creates `self.layers = []` and appends `nn.Linear(2, 2)`.
2. `ProperModuleList`: creates `self.layers = nn.ModuleList([nn.Linear(2, 2)])`.

The probe inspected `named_parameters()`, `state_dict()`, and parent-level `.to(dtype=torch.float64)` behavior.

## OBSERVED results

Plain Python list parent:

```text
named_parameters: []
state_dict keys: []
child dtype before parent .to: torch.float32
child dtype after parent .to:  torch.float32
```

`nn.ModuleList` parent:

```text
named_parameters: ['layers.0.weight', 'layers.0.bias']
state_dict keys: ['layers.0.weight', 'layers.0.bias']
child dtype after parent .to: torch.float64
```

## Result

**PASS** for the tested generic capability: the probe reproduces the distinction asserted by current PyTorch documentation. A child `nn.Module` stored only in an ordinary Python list was callable as an object but was not exposed through the parent's standard parameter/state enumeration and did not follow the parent's dtype migration. The `ModuleList` child was registered and did follow those mechanisms.

## Transfer to GSR-Net finding

The inspected BASIRA GSR-Net `GraphUnet` creates ordinary Python lists for several collections of child modules and appends `GCN`, `GraphPool`, and `GraphUnpool` instances.

The generic registration mechanism behind the Warden's concern is therefore directly reproduced in a minimal test.

However:

`GENERIC_FRAMEWORK_PROBE != EXECUTION_OF_GSR_NET`

The probe does not establish which GSR-Net parameters actually changed during a published training run, what checkpoints were used, or the quantitative effect on reported results. Those remain implementation-specific questions requiring direct execution/instrumentation.

## Authoritative documentation cross-check

Current PyTorch documentation states that modules held in `nn.ModuleList` are properly registered and visible to `Module` methods. PyTorch module documentation also describes registered parameters as the parameters exposed through parent module methods such as `parameters()` and moved through module conversion/device operations.

Documentation URLs used during the Warden review:

- https://docs.pytorch.org/docs/stable/generated/torch.nn.ModuleList
- https://docs.pytorch.org/docs/stable/notes/modules.html

## HC lesson status

The canonical HC transfer remains:

`CALLED_IN_FORWARD != MANAGED_BY_LIFECYCLE`

`LEARNABLE_PARAMETER_EXISTS != PLASTICITY_PATH_CAN_REACH_PARAMETER`

`COMPUTES_OUTPUT != STATE_IS_DURABLY_CUSTODIED`

The local probe strengthens the implementation pattern behind `docs/architecture/RUNTIME_COMPONENT_REGISTRATION_AND_STATE_CUSTODY.md` without converting a generic framework result into a claim about a complete HC implementation.
