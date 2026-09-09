# BASIRA DynGNN Dynamic-Memory Custody Study — 2026-09-09

Status: NON-CANONICAL RESEARCH / SOURCE STUDY

## Source cut

Repository: `basiralab/DynGNN`

Inspected default branch: `main`

Primary artifacts:

- `README.md` blob `2d6f710bda7afc229e64d05c1c702a73f45ea24b`
- `models/echo.py` blob `45d880b03738cd7ccc64e08d1bff016925fc2b78`
- `models/tagnet.py` blob `4a51f75c89fef26795ff7c4fa9706981c7df6044`

## Documented source intent

DOCUMENTED from the README: DynGNN is described as a dynamic memory-enhanced generative GNN architecture for predicting temporal brain connectivity.

The source repository is used here as a computational-pattern study, not as evidence that HC should copy its model architecture.

## Observed dynamic-state behavior

OBSERVED in `models/echo.py`:

1. `EchoStateNetwork` is an `nn.Module` that keeps an input matrix `W_in` as a normal tensor attribute rather than declaring it as a parameter or registered buffer.
2. `forward(W_res, X)` receives a reservoir matrix, normalizes it, and assigns the resulting tensor to `self.W_res` during forward execution.
3. `get_states(X)` recursively computes reservoir state from the previous state using `self.W_res`.
4. `train_output_weights(states, targets)` computes a pseudoinverse solution and assigns the learned output matrix to `self.W_out` after initialization.
5. `predict(X)` later depends on `self.W_out` and the recursively generated reservoir states.

OBSERVED in `models/tagnet.py`:

6. `DeepTAGNet` owns `self.esn = EchoStateNetwork(...)` as a registered child module.
7. During a forward call with training signals, `self.esn(out, train_sig_input)` computes dynamic states, `train_output_weights(...)` mutates `self.esn.W_out`, and `predict(test_sig_input)` uses that newly fitted output state in the same high-level computation.

## Transfer finding: registered owner does not guarantee registered dynamic state

A parent component may be correctly registered while material tensors created or assigned later remain outside the runtime's normal parameter/buffer/checkpoint machinery.

HC transfer:

`REGISTERED_COMPONENT != ALL_CAUSAL_STATE_REGISTERED`

`DYNAMIC_ATTRIBUTE_EXISTS != DURABLE_STATE_CUSTODY`

`LEARNED_DURING_FORWARD != AUTOMATICALLY_CHECKPOINTED`

`CHILD_MODULE_REGISTERED != CHILD_DYNAMIC_STATE_GOVERNED`

This strengthens the existing HC runtime-component/state-custody contract: qualification must inspect the **material state surface**, not stop after proving that the owning component appears in a component registry.

## Ephemeral versus durable learned state

Dynamic state is not automatically defective. Some state may intentionally be:

- per-request scratch state;
- transient working memory;
- task-local adaptation;
- session-local calibration;
- durable learned state;
- protected continuity-bearing state.

The defect arises when the claimed lifecycle and the actual custody path disagree.

For each material dynamically created or mutated state item, HC should be able to establish:

- state family and intended lifetime;
- whether loss on restart is allowed;
- whether it must migrate with its owner;
- whether checkpoint/restore is required;
- whether update is ordinary plasticity, bounded adaptation, calibration, or protected mutation;
- whether replay/recomputation is sufficient and deterministic enough for the claim;
- whether its absence changes capability, identity, memory, values, authority, or current behavior materially.

`EPHEMERAL_BY_DESIGN != ACCIDENTALLY_UNCHECKPOINTED`

## Forward-time fitting boundary

The inspected `DeepTAGNet.forward` can both fit output weights from supplied training signals and immediately predict from them.

That exposes a second architectural distinction:

`INFERENCE_CALL != NECESSARILY_STATE_PURE`

HC interfaces should declare whether an operation may mutate learned/calibration state while producing an answer. A read-looking API must not be assumed side-effect-free merely because it returns a prediction.

Material state mutation during an inference-like call requires normal learning/update provenance and, where applicable, qualification-evidence isolation.

`PREDICTION_RETURNED != NO_LEARNING_OCCURRED`

## Memory terminology boundary

The source calls the architecture memory-enhanced, but HC must not infer autobiographical/current/deep-memory semantics from that label. Reservoir/recurrent computational state is a mechanism-level memory form.

`MODEL_MEMORY != HC_CURRENT_MEMORY`

`MODEL_MEMORY != HC_DEEP_MEMORY`

`RECURRENT_STATE != AUTOBIOGRAPHICAL_CONTINUITY`

The source is useful precisely because it shows why memory family and custody semantics need explicit typing.

## Suggested HC negative tests

1. Register a component normally, create a new causal tensor attribute after initialization, checkpoint the parent, and verify qualification catches omission if durability was claimed.
2. Move a component across device/substrate after dynamic state exists; verify every state item either migrates, is recomputed under declared rules, or triggers explicit failure.
3. Run an inference-like operation twice with identical observation input but different training/adaptation side inputs; verify state mutation is recorded rather than misclassified as pure inference.
4. Restart between fitting dynamic output state and prediction; verify behavior matches the declared lifetime—restore if durable, explicit reset/recalibration if ephemeral.
5. Label recurrent/reservoir state as `MODEL_WORKING_STATE` and verify it cannot be queried or promoted as autobiographical current/deep memory merely because the source mechanism is called memory.
6. Use holdout examples as forward-time adaptation data and verify they cease to qualify as untouched independent evidence for the adapted successor.

## Transfer decision

PROMOTE AS A STRENGTHENING OF EXISTING STATE-CUSTODY AND QUALIFICATION RULES; DO NOT CREATE A PARALLEL MEMORY SUBSYSTEM.

The source exposes two reusable implementation hazards:

- component registration can coexist with unregistered dynamically assigned causal state;
- prediction/inference interfaces can conceal stateful fitting/adaptation.

## Evidence boundary

DOCUMENTED: source project description from README.

OBSERVED: tensor assignment, recurrent state computation, output-weight fitting, and prediction flow in the inspected code.

INFERRED: HC state-custody and interface-semantics requirements.

UNKNOWN from static inspection: whether external training scripts separately serialize `W_in`, `W_res`, or `W_out`; whether loss of those values is intentionally accepted; and the exact persistence claims of the published DynGNN method.
