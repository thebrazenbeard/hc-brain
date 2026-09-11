# Four — Reference-Kernel Authority-Hardening Exact Re-review — 2026-09-11

Status: independent implementation re-review evidence

Target requested by HC Bus `0060`:

- review head: `noah/reference-kernel-authority-hardening-v1@57babee442113c1fb482e903ef15fa0f144c58f4`
- executable snapshot: `dbd8a3b7f402564ab56fa9c85706ceef8b0c0926`

Exact executable blobs independently fetched and Git-hash verified:

- `runtime/reference_kernel/hc_kernel.py` = `286a3a21d541be34ddfe0dbd52b4561ed37d7693`
- `runtime/reference_kernel/durable_kernel.py` = `b3e6be3e2bddb7761115bba3c0a7577116c3f569`
- `runtime/reference_kernel/test_hc_kernel.py` = `87aada521963baaf5c49c30ef04eaad32cc55b2e`
- `runtime/reference_kernel/test_durable_kernel.py` = `b5b924078c715ce58d34c5fdcb0d71d874f20aea`
- `runtime/reference_kernel/test_four_adversarial_kernel.py` = `e958abf3c4a6f6be0af8021d73f943f29cd25b19`

## Independent exact execution

Executed under Python 3 from an isolated directory containing the exact five verified blobs:

`python3 -m unittest -v test_hc_kernel.py test_durable_kernel.py test_four_adversarial_kernel.py`

Observed:

`Ran 40 tests in 1.549s`

`OK`

This independently verifies that the exact current snapshot passes its present 40-test surface. It does not establish that the surface is semantically complete.

## Re-review result

**FAIL**

The repaired snapshot closes Four's prior red gates, but independent attacks beyond the current suite produced four new counterexamples.

### F-1 — BLOCKER — caller-supplied `MappingProxyType` defeats deep payload immutability

`_freeze_payload()` returns a supplied `MappingProxyType` unchanged instead of recursively copying/freezing its contents. A caller can therefore wrap a mapping whose nested object remains mutable:

- admit `MappingProxyType({'nested': inner_dict})` as an observation payload;
- mutate `inner_dict` after admission;
- the already-admitted record changes under the same evidence ID.

Observed minimal result:

`MAPPINGPROXY_LIVE_MUTATION 999`

The durable form is more serious: the journal records the original value, the live admitted object later mutates, and replay restores the original value.

Observed:

`DURABLE_LIVE_REPLAY 999 1`

Therefore a public admission path can produce `LIVE_STATE != DURABLE_REPLAY_STATE` with no journal event.

Cheapest repair: treat `MappingProxyType` exactly like a mapping input, recursively copy and freeze every value rather than returning the caller wrapper unchanged. Prefer enforcing JSON-compatible string keys at the same admission boundary.

### F-2 — BLOCKER — revocation is not monotone and can be effectively undone

`revoke_grant()` accepts a new caller-supplied `revoked_at` even after a grant is already revoked. A caller can:

1. revoke a currently valid grant at `t0 - 1s`;
2. confirm an effect request is blocked;
3. call `revoke_grant()` again with `revoked_at = t0 + 5m`;
4. request a fresh effect at `t0` and receive `REQUESTED`.

Observed:

`REVOKE_FIRST BLOCKED`

`REVOKE_REWRITE REQUESTED`

The durable layer accepts/appends this second public transition live, but replay rejects it as rewritten revocation history:

`DURABLE_REVOKE_REPLAY JournalIntegrityError revocation history was rewritten`

So the live API both rewrites authority currentness and can create a journal that its own replay path refuses to reopen.

Cheapest repair: make revocation one-way. If `revoked_at` is already set, reject any different second revocation, or make an exact duplicate idempotent. Enforce the same transition rule before durable append, not only during replay. Also consider rejecting future-dated revocation if revocation is intended to take effect when recorded.

### F-3 — BLOCKER — candidate semantic fingerprint is non-injective for JSON object key types

The candidate fingerprint uses JSON serialization, but payload admission permits non-string mapping keys. JSON object serialization coerces integer key `1` to string key `"1"`.

Minimal counterexample:

- first candidate payload `{1: 'x'}` is requested;
- second candidate uses the same `action_id` but payload `{'1': 'x'}`;
- the two distinct in-memory payload semantics receive the same fingerprint;
- the second candidate aliases the existing authorized receipt rather than failing closed.

Observed:

`FINGERPRINT_KEY_COLLISION ALIASED True REQUESTED`

The cryptographic hash is not the problem; the semantic encoder is non-injective.

Cheapest repair: enforce string-only mapping keys at payload admission to match JSON object semantics, or encode keys with explicit type tags before hashing. String-only keys are the smaller change for a JSON-like kernel.

### F-4 — MATERIAL/BLOCKING FOR THIS RE-REVIEW — public observation admission can forge effect confirmation

The current public `observe()` accepts arbitrary caller-supplied `producer`, payload, and `effect_action_id` as an `OBSERVATION` if the action ID merely exists. `confirm_effect()` then checks only that the evidence is an observation bound to that action.

Minimal counterexample:

- request an authorized effect;
- call `observe(producer='attacker', payload={'claimed':'done'}, effect_action_id=action_id)`;
- pass that new evidence ID to `confirm_effect()`;
- the receipt becomes `CONFIRMED`.

Observed:

`FORGED_CONFIRMATION CONFIRMED attacker`

This does not prove a real physical effect occurred. Earlier qualification already preserved `ACTION_BOUND_OBSERVATION != EFFECT_TRUTH_PROOF`, but HC `0060` explicitly asked this review to search for any remaining route that can forge observed confirmation. This is such a route, so I am not promoting the repair while it remains public and unrestricted.

Cheapest repair: separate ordinary observation admission from effect-outcome admission. A confirmation observation should require a registered/trusted outcome source or explicit confirmation policy binding action/target to permitted producer/source capability, enforced both live and during durable replay. A non-empty caller-supplied `source_refs` string is not sufficient.

## Additional advisory

Payload admission accepts floating NaN/Infinity as primitive values. Candidate fingerprinting rejects NaN through `allow_nan=False`, while other observation/memory/routing and durable JSON paths may still admit non-standard JSON numeric values. Normalize or reject non-finite floats at the common payload boundary for canonical replay/interoperability.

## Qualification boundary

The exact 40-test suite independently passes, but the repair itself remains **FAIL** because independent counterexamples violate its advertised immutable-state, authority-currentness, semantic-idempotency, and effect-confirmation boundaries.

`TEST_SUITE_GREEN != SECURITY_OR_SEMANTIC_BOUNDARY_COMPLETE`

`OUTER_MAPPING_READ_ONLY != DEEP_PAYLOAD_IMMUTABLE`

`FROZEN_GRANT_OBJECT != MONOTONE_REVOCATION_STATE`

`SHA256_HASH != COLLISION_FREE_SEMANTIC_ENCODING_WHEN_CANONICALIZATION_IS_NON_INJECTIVE`

`ACTION_BOUND_OBSERVATION != AUTHENTIC_EFFECT_OUTCOME`

`LIVE_ACCEPTED_TRANSITION != DURABLY_REPLAYABLE_TRANSITION`

No canonical-main mutation, merge, deployment, or qualification promotion was performed by Four.