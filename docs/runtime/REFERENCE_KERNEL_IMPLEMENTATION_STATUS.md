# Reference Kernel Implementation Status

Status: current implementation-status note.

The canonical HC runtime architecture remains substantially unimplemented. The existence of `runtime/reference_kernel/` changes only one narrower statement: selected cross-cutting invariants now have an executable reference slice.

Current executable scope includes:

- typed observation versus derived/predicted evidence;
- causal/source references for derived evidence;
- routing state distinct from incorporation and effect authority;
- fail-closed unique-head current-memory projection;
- explicit same-scope supersession;
- scoped/current authority checks at effect request;
- action-bound outcome-confirmation evidence;
- duplicate request suppression inside one process instance;
- modeled restart-epoch fencing and unresolved in-flight-effect state.

Current executable scope does **not** include the complete temporal hypergraph, subsystem runtime contracts, coalition formation/dissolution, distributed arbitration, semantics, planning, learning/plasticity, deep-memory consolidation, affect/homeostasis dynamics, resource scheduling, embodiment, multi-constituent fault behavior, or protected-update activation.

Accordingly:

`REFERENCE_KERNEL_PRESENT != COMPLETE_HC_RUNTIME_PRESENT`

`EXECUTABLE_INVARIANT_SLICE != EXECUTABLE_COGNITIVE_ORGAN`

`UNIT_TESTED_CONTROL_PATH != DEMONSTRATED_INTELLIGENCE`

The governing implementation qualification is `docs/qualification/MINIMAL_REFERENCE_KERNEL_VERTICAL_SLICE_2026-09-10_R2.md`.

The next implementation objective is to replace modeled restart semantics with a durable append journal and real process-reload recovery test, then build the first small evidence -> arbitration -> authorized effect -> observed outcome -> current-memory closed loop without introducing a central executive.
