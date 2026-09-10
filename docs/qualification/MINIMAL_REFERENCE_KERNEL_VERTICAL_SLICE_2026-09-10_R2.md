# Minimal Reference Kernel Vertical Slice — 2026-09-10 R2

Status: QUALIFICATION EVIDENCE

Implementation target: `main@d0df2c98d042c0f68833005a5528e14bf810b0f0`

Predecessor: `MINIMAL_REFERENCE_KERNEL_VERTICAL_SLICE_2026-09-10.md`

Overall result: **CONDITIONAL PASS**

Exact implementation-test result: **PASS (12/12)**

## Tested capability

This successor tests a narrow executable HC invariant kernel, not general cognition. It exercises evidence typing/provenance, routing versus incorporation/authority, append-oriented current-state projection, scope-bounded supersession, authority currentness, effect request/confirmation separation, replay resistance, and modeled restart fencing.

R2 additionally hardens two weaknesses named in the predecessor qualification:

1. authority is no longer exposed as an unqualified `issue_grant()` self-minting interface; the reference kernel registers an explicitly provenance-bearing grant fixture and requires at least one authority-basis reference;
2. an effect cannot become confirmed from an arbitrary supplied evidence identifier. The confirming observation must be explicitly bound to the action being confirmed, and the reference kernel requires observed outcome evidence for this narrow path.

## Exact executable evidence

The committed implementation and test blobs are:

- `runtime/reference_kernel/hc_kernel.py` — Git blob `e48355da01482cc6ca709928214ad61c9998249e`;
- `runtime/reference_kernel/test_hc_kernel.py` — Git blob `cbeed0a20ccbe2b8d31a25d0d57f40bc83952748`.

Before recording this qualification, the exact UTF-8 contents used to produce those two Git blobs were executed together under Python `unittest`. Git blob hashes were independently recomputed from the locally executed byte strings and matched the repository-returned content SHAs exactly.

Observed result:

`Ran 12 tests in 0.001s`

`OK`

Therefore the local execution is **repository-content exact for those two blobs**, not merely a functionally similar pre-commit candidate.

## Passing executable cases

The exact test pair passed cases for:

- explicit authority-basis requirement;
- high-priority routed input failing to create effect authority;
- prediction remaining distinct from observation and retaining parent/source lineage;
- competing unsuperseded current-memory heads producing `AMBIGUOUS`;
- explicit resolution by a new record superseding both competing heads;
- cross-logical-scope supersession rejection;
- expired authority blocking an effect request;
- revocation after planning blocking the effect request;
- requested effect remaining distinct from confirmed effect;
- unrelated observation being rejected as effect-confirmation evidence;
- duplicate request of the same action not producing a second dispatch attempt;
- restart changing an in-flight requested effect to unresolved, refusing same-action blind replay, and rejecting old-epoch authority for a newly planned action;
- a plan created before restart failing as stale after the epoch change.

(Some assertions are combined inside one named unit case; the suite contains twelve test methods.)

## GitHub Actions state

Repository CI remains **infrastructure-unresolved**.

A workflow at `.github/workflows/reference-kernel.yml` was added and then simplified to remove dependencies on `actions/checkout` and `actions/setup-python`. GitHub Actions runs including `34539356596`, `34539477839`, and the R2-triggered run `34539774100` all concluded `failure`, but the jobs API reported no executed steps. The available evidence therefore does not establish a Python test failure in GitHub Actions.

`ACTIONS_RUN_FAILURE_WITH_ZERO_EXECUTED_STEPS != REFERENCE_KERNEL_TEST_FAILURE`

The exact-blob local PASS is retained separately from the unresolved hosted-runner path.

## What R2 now demonstrates

Within this narrow in-memory reference implementation:

- `PREDICTION != OBSERVATION` is enforced by code;
- `ROUTED != INCORPORATED` is represented separately;
- `PRIORITY != AUTHORITY` survives an executable negative case;
- `LATEST != CURRENT` is operationalized as unique-unsuperseded-head selection rather than append order;
- `PERMISSION_FOR_X != PERMISSION_FOR_Y` is represented by exact action and target scope matching;
- revoked, expired, unknown, missing, or old-epoch authority fails closed at the effect-request boundary;
- `REQUESTED != CONFIRMED` is represented as distinct effect states;
- effect confirmation must cite an observation explicitly bound to the action;
- repeated delivery of the same action candidate does not produce repeated dispatch in this process model;
- in-flight effects become unresolved across a modeled restart epoch instead of being silently replayed.

## Remaining limitations

The implementation is still a **reference kernel**, not a synthetic brain runtime.

Material limits include:

- all state is process memory; restart is modeled by an epoch transition rather than an actual process crash, durable journal, reload, or distributed recovery;
- `register_grant()` checks structural provenance/basis presence but does not itself establish that the grantor was legitimately authorized to create the grant;
- outcome binding proves that the observation names the action, not that the sensor or observation is trustworthy, causally sufficient, independently calibrated, or immune to spoofing;
- no consent-specific object is implemented yet;
- no temporal hyperedge/coalition engine is implemented;
- no plasticity, learning, deep-memory consolidation, semantic inference, salience scheduler, resource arbitration, embodiment controller, affect/homeostasis dynamics, or protected-update transaction is implemented;
- no concurrency, partition, crash-consistency journal, durable idempotency ledger, or distributed constituent model is implemented;
- UUID generation is nondeterministic and exact replay is not yet implemented;
- the tests are authored by the implementation author and are not independent hostile evidence.

## Qualification decision

The exact implementation-test slice **passes its twelve executed unit cases**.

The broader vertical-slice qualification remains **CONDITIONAL PASS** because independent/hostile review has not yet been incorporated, hosted CI did not execute the test steps, and the recovery/authority mechanisms intentionally model only a small subset of their canonical contracts.

`12_OF_12_REFERENCE_TESTS_PASS != HC_IMPLEMENTATION_PASS`

`EXACT_BLOB_TEST_PASS != INDEPENDENT_REVIEW_PASS`

`ACTION_BOUND_OBSERVATION != EFFECT_TRUTH_PROOF`

`BASIS_BEARING_GRANT_FIXTURE != QUALIFIED_GRANT_ISSUANCE`

`MODELED_RESTART_EPOCH != DURABLE_RECOVERY`

## Next implementation targets

Highest-value next cuts are:

1. a durable append journal and real process-reload test for memory/effect recovery;
2. explicit authority-admission/grant-chain validation rather than fixture registration alone;
3. typed effect-confirmation requirements with source reliability/calibration and causal evidence policy;
4. deterministic event identities/replay fixtures;
5. the first actual coalition/arbitration path spanning evidence -> candidate -> authority gate -> outcome -> memory update;
6. independent Four review and Vera hostile review of the executable slice.

Evaluator: Noëtarch / Noah, Warden and implementation author.

Reviewer provenance: primary author/evaluator; not independent.
