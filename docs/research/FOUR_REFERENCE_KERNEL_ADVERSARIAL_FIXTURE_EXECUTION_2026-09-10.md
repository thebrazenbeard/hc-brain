# Four Adversarial Fixture Execution — Reference Kernel — 2026-09-10

Status: executable counterexample evidence against the current in-memory reference kernel; no canonical-main mutation.

## Fixture source

Four added:

`runtime/reference_kernel/test_four_adversarial_kernel.py`

on `four/lineage-and-conformance-v2`, commit:

`6306ce815f467625dc76b18f4923cf0e626571e6`

The fixture encodes six required secure behaviors derived from Four's independent implementation review:

1. caller backdating must not reactivate expired authority;
2. caller backdating must not reactivate revoked authority;
3. same action ID with materially different candidate semantics must fail closed;
4. admitted observation payload must not mutate when the caller mutates its original object;
5. current-state projection must preserve selected-head epistemic/source classification;
6. durable live state and replayed state must remain equal after caller mutation of the original admitted payload.

The first five depend only on the exact base implementation blob. The sixth additionally depends on the durable implementation.

## Exact base implementation under execution

`runtime/reference_kernel/hc_kernel.py`

Git blob:

`e48355da01482cc6ca709928214ad61c9998249e`

This is the same exact blob independently reproduced earlier for HC `0055` and still present on observed current canonical `main@cf92a32122c436beb5cc516bd7480af00f0ba29f`.

Environment:

- Python `3.13.5`
- Linux `6.18.35 x86_64`

## Base-fixture execution result

A local unittest subset implementing the same five base-kernel expectations was run against the exact blob.

Observed:

`Ran 5 tests in 0.003s`

`FAILED (failures=5)`

Every failure was the expected invariant counterexample rather than an import/syntax/harness error.

### Failure 1 — expired authority backdating

Expected:

`BLOCKED`

Observed:

`REQUESTED`

The caller-selected historical `now` was inside the expired grant's historical validity window.

### Failure 2 — revoked authority backdating

Expected:

`BLOCKED`

Observed:

`REQUESTED`

The caller-selected historical `now` preceded the recorded revocation.

### Failure 3 — same action ID / different candidate semantics

Expected:

not `REQUESTED` under the prior authorization result.

Observed:

`REQUESTED`.

The second candidate reused the first candidate's action ID but changed origin, action scope, target, payload, and authority reference.

### Failure 4 — payload immutability

Expected stored evidence payload:

`{'x': 1, 'n': {'v': 'a'}}`

Observed after caller mutation:

`{'x': 2, 'n': {'v': 'b'}}`

### Failure 5 — typed current projection

Expected current projection to expose selected-head epistemic classification directly or through an explicit selected record.

Observed:

neither `epistemic_class` nor `selected_record` exists on the projection object.

## Correct interpretation

These tests are written to express the required repaired behavior, so **failure against the current known-bad blob is the expected useful result**.

They should become regression gates after Noah repairs the implementation:

`CURRENT_FAILING_ADVERSARIAL_FIXTURE -> REPAIR_TARGET`

A successor implementation should make these fixtures PASS without weakening the assertions.

Do not rewrite the fixture to match the current implementation merely to obtain green tests.

## Durable sixth case

The committed fixture also contains a durable live-versus-replay payload equality test. Static source review establishes the current durable wrapper stores the inherited mutable live payload before serializing the journal value, so the divergence path is present.

This execution record does not claim an independent exact-blob runtime result for the sixth durable case. Preserve that distinction until the exact durable blob is independently reconstructed/executed in Four's environment or a successor CI/runtime surface provides executed evidence.

## Evidence ceiling

`FIVE_DISCRIMINATING_FAILURES != WHOLE_HC_FAILURE`

`EXPECTED_RED_REGRESSION_FIXTURE != BROKEN_TEST`

`FIXTURE_COMMIT != CANONICAL_REPAIR`

`STATIC_DURABLE_INHERITANCE != INDEPENDENT_DURABLE_RUNTIME_EXECUTION`
