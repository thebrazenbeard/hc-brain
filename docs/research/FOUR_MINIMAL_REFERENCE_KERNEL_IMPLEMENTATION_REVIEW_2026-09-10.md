# Four Independent Implementation Review — Minimal Reference Kernel — 2026-09-10

Status: implementation-level secondary review of exact executable artifacts; no canonical-main mutation.

## Target and reviewer provenance

Requested by HC Bus message `0054-noah-reference-kernel-executable-review.md`.

Frozen implementation target:

`main@d0df2c98d042c0f68833005a5528e14bf810b0f0`

Exact reviewed blobs:

- `runtime/reference_kernel/hc_kernel.py` = `e48355da01482cc6ca709928214ad61c9998249e`
- `runtime/reference_kernel/test_hc_kernel.py` = `cbeed0a20ccbe2b8d31a25d0d57f40bc83952748`

Four did not author either implementation/test blob. Four has materially shaped portions of the wider HC architecture/specification, so this review is not claimed as independent evidence for the underlying architecture requirements themselves. Independence is claimed only for review of the executable implementation artifact and its authored tests:

`INDEPENDENT_WITHIN_EXECUTABLE_IMPLEMENTATION_ARTIFACT_SCOPE`

`IMPLEMENTATION_ARTIFACT_INDEPENDENCE != ARCHITECTURE_REQUIREMENT_INDEPENDENCE`

I had not inspected a Vera hostile review of this target before generating the findings below.

## Exact independent reproduction

The repository-returned UTF-8 contents were reconstructed locally and verified with Git blob hashing before execution.

Environment:

- Python `3.13.5`
- Linux `6.18.35 x86_64`

Local blob verification:

- `git hash-object hc_kernel.py` -> `e48355da01482cc6ca709928214ad61c9998249e`
- `git hash-object test_hc_kernel.py` -> `cbeed0a20ccbe2b8d31a25d0d57f40bc83952748`

Command:

`python3 -m unittest -v test_hc_kernel.py`

Observed result:

`Ran 12 tests in 0.001s`

`OK`

Therefore the author's exact 12/12 test result is independently reproducible on these exact two blobs.

That result is necessary but not sufficient: adversarial probes below expose behavior not discriminated by the authored suite.

## Review disposition

**FAIL for the exact implementation slice as a reliable authority/effect gate, despite 12/12 authored tests passing.**

Two BLOCKER counterexamples permit an authorization/idempotency boundary to be bypassed through public call parameters/identity reuse. Two additional MATERIAL findings weaken evidence/currentness integrity. One robustness advisory is also recorded.

This does not imply that the HC architecture is invalid. It means the exact executable slice does not yet faithfully enforce several invariants it is being used to executable-falsify.

## BLOCKER 1 — caller-controlled authorization time permits stale-authority backdating

### Observed code path

`request_effect(candidate, now: Optional[datetime] = None)` accepts a caller-supplied authorization time and forwards it into `grant.allows(...)`.

The authority decision therefore trusts the request caller to state what time it is.

### Reproduced expiry bypass

A grant valid from `17:50` until `17:59:59` is objectively expired at `18:00`. Calling:

`request_effect(candidate, now=17:55)`

returned:

`REQUESTED / AUTHORIZED`

### Reproduced revocation bypass

A grant valid across `18:00` but revoked at `17:59:59` can likewise be reused by calling:

`request_effect(candidate, now=17:59:30)`

Observed result:

`REQUESTED / AUTHORIZED`

### Why the authored tests miss it

The expiry and revocation tests inject a fixed test timestamp that is after expiry/revocation. They prove comparison logic for a cooperative caller, not trusted-current-time enforcement.

### Required separation

`CALLER_SUPPLIED_TIME != TRUSTED_AUTHORIZATION_CURRENTNESS`

`CORRECT_COMPARISON_LOGIC != STALE_AUTHORITY_REPLAY_RESISTANCE`

### Cheapest repair

Do not accept authorization currentness as a per-request caller-controlled value on the production effect-gate API.

Use a kernel-owned clock function/dependency. Tests may inject a deterministic fake clock at kernel construction/configuration, but the effect requester must not be able to choose the timestamp used to validate its own authority.

Add hostile tests for:

- expired grant + caller attempts backdated request;
- revoked grant + caller attempts pre-revocation request time;
- future-dated caller time and invalid clock-domain inputs.

Expected: stale authority remains blocked regardless of requester's timestamp claim.

## BLOCKER 2 — action-ID aliasing allows a different candidate to inherit an old authorization receipt

### Observed code path

`request_effect()` begins with:

`existing = self.effect_receipts.get(candidate.action_id)`

and immediately returns that receipt when present.

It does not verify that the repeated candidate is semantically identical to the candidate that produced the receipt.

`EffectCandidate` is publicly constructible, including caller-specified `action_id`.

### Reproduced counterexample

1. Create candidate A with:
   - origin `kinesis`
   - action `MOTOR_EFFECT`
   - target `arm`
   - payload `safe`
   - valid grant
2. Request A -> `REQUESTED / AUTHORIZED`.
3. Construct candidate B manually with the **same `action_id`** but:
   - origin `evil`
   - action `UNAUTHORIZED`
   - target `other`
   - payload `danger`
   - no authority grant.
4. Call `request_effect(B)`.

Observed:

- the returned object is the same receipt as A;
- state remains `REQUESTED`;
- reason remains `AUTHORIZED`;
- B's mismatched fields are never validated.

### Why the authored test misses it

`test_duplicate_request_does_not_redispatch` submits the same candidate object twice. It tests duplicate delivery, not idempotency-key collision or same-ID/different-content replay.

### Required separation

`SAME_ACTION_ID != SAME_ACTION_CANDIDATE`

`IDEMPOTENT_REDELIVERY != AUTHORIZATION_RESULT_REUSABLE_FOR_DIFFERENT_CONTENT`

### Cheapest repair

Bind every receipt/idempotency entry to an immutable canonical candidate identity/fingerprint containing at least:

- action ID;
- origin;
- action scope;
- target scope;
- payload digest or canonical payload identity;
- authority grant ID;
- planned epoch;
- material parent/provenance identity where relevant.

On duplicate action ID:

- exact candidate match -> return prior receipt without redispatch;
- any material mismatch -> fail closed with an explicit `ACTION_ID_COLLISION_OR_CONTENT_MISMATCH` condition.

Prefer internally allocated/registered action IDs rather than treating an arbitrary public dataclass construction as sufficient admission.

## MATERIAL 3 — frozen records contain mutable payload aliases

The record dataclasses are `frozen=True`, but their `payload: Any` is stored by reference.

Reproduced:

1. `p = {"reading": 1}`
2. `e = kernel.observe(..., payload=p)`
3. mutate external object: `p["reading"] = 999`
4. `e.payload` now reports `{"reading": 999}` under the same evidence ID.

The same aliasing risk applies to routed, memory, and candidate payloads when mutable objects are supplied.

### Required separation

`FROZEN_DATACLASS != IMMUTABLE_EVIDENCE_CONTENT`

`STABLE_EVIDENCE_ID != STABLE_EVIDENCE_VALUE` when mutable references remain shared.

### Cheapest repair

At admission, canonicalize/copy into an immutable or serialization-stable representation. At minimum deep-copy mutable input before storage; stronger implementations should bind the record identity/provenance to a canonical content digest and avoid exposing mutable internal state.

Add a test that mutates the original caller object after observation/memory admission and verifies stored record content does not change.

## MATERIAL 4 — current-state projection strips epistemic/source classification from its public result

`CurrentProjection` carries:

- status;
- logical key;
- head IDs;
- payload.

It does not expose the selected head's `epistemic_class` or `source_refs`.

Reproduced:

- append a single `PREDICTION` memory record for a logical state key;
- `current(key)` returns `CURRENT` plus the prediction payload;
- the projection object itself has no epistemic-class or source-provenance field.

The backing record still retains that metadata and can be recovered indirectly by dereferencing `head_ids`, so this is not literal destruction of stored provenance. It is a public read-boundary laundering risk: consumers of `CurrentProjection.payload` can receive a current value without the epistemic class required to distinguish prediction from observation.

### Required separation

`CURRENT_PROJECTION != OBSERVED_TRUTH`

`CURRENT_PAYLOAD_WITHOUT_CLASS != SAFE_EPISTEMIC_READ_BOUNDARY`

### Cheapest repair

Return a typed selected-head projection or include at least the selected record's epistemic class and source/provenance refs. For ambiguous heads, preserve typed metadata for every head rather than only opaque IDs when the API is used for adjudication.

Add a negative test where prediction is the sole current head and require downstream projection to remain explicitly `PREDICTION`.

## Robustness advisory — mixed naive/aware datetimes raise instead of fail closed

`register_grant()` accepts offset-naive datetimes. If an aware request time is later compared against a naive `valid_from`/`expires_at`, Python raises `TypeError`.

Observed:

`TypeError: can't compare offset-naive and offset-aware datetimes`

For an effect gate, malformed/mixed clock-domain data should be rejected at grant admission or converted under an explicit policy, not surface as an uncontrolled comparison exception.

Recommended: require timezone-aware UTC inputs and validate that requirement when grants/revocations are registered.

## Findings already declared by the primary qualification, not double-counted as novel defects

The R2 qualification already states that:

- `register_grant()` checks structural basis/provenance presence but does not prove grantor legitimacy;
- action-bound observation does not prove sensor trust, causal sufficiency, calibration, or outcome truth;
- restart is modeled in-process rather than durable recovery;
- UUID replay is nondeterministic;
- the authored tests are not independent hostile evidence.

I independently confirmed those ceilings are real, but they are not presented above as newly discovered review failures.

## Test-quality assessment

The twelve tests are useful and nontrivial. In particular, they genuinely discriminate:

- direct prediction-to-observation relabeling through `derive()`;
- competing current heads;
- cross-scope supersession;
- cooperative expiry/revocation handling;
- requested/confirmed state separation;
- action-bound versus unrelated confirmation evidence;
- same-object duplicate delivery;
- modeled restart epoch fencing.

The main weakness is that several tests verify the intended happy interface rather than attacking the public identity/time/admission surfaces around it.

`AUTHORED_NEGATIVE_TEST_PASS != ADVERSARIAL_API_BOUNDARY_PASS`

## Currentness note

At the later observed canonical cut after durable-kernel work, current `main` still reports the same in-memory blobs:

- `hc_kernel.py` = `e48355da01482cc6ca709928214ad61c9998249e`
- `test_hc_kernel.py` = `cbeed0a20ccbe2b8d31a25d0d57f40bc83952748`

Therefore these findings remain applicable to the current in-memory reference kernel unless a later commit supersedes those exact blobs.

Durable-journal work is a separate implementation surface and is not automatically failed by this review; however any durable layer that delegates effect admission/current-memory semantics to these methods should be checked for inheritance of the same defects.

## Final disposition

For exact target `main@d0df2c98d042c0f68833005a5528e14bf810b0f0`:

- exact authored suite reproduction: **PASS 12/12**;
- independent implementation review: **FAIL**;
- blocker findings: caller-controlled authorization time; action-ID/content aliasing;
- material findings: mutable admitted payloads; projection epistemic/provenance erasure at read boundary;
- robustness advisory: mixed timezone-awareness exception.

This review does not establish a whole-HC implementation failure and does not revoke architecture-level results.

Evidence ceilings:

`12_OF_12_AUTHORED_TESTS_PASS != IMPLEMENTATION_QUALIFICATION_PASS`

`CALLER_SUPPLIED_TIME != TRUSTED_AUTHORITY_CURRENTNESS`

`SAME_ACTION_ID != SAME_AUTHORIZED_CANDIDATE`

`FROZEN_RECORD_WRAPPER != IMMUTABLE_RECORD_CONTENT`

`CURRENT_PAYLOAD != OBSERVED_TRUTH`

`REFERENCE_KERNEL_REVIEW_FAIL != HC_ARCHITECTURE_FAIL`
