# Minimal Reference Kernel Vertical Slice — 2026-09-10

Status: QUALIFICATION EVIDENCE

Target repository snapshot: `main@17add6f4c625cecc90473654d079ad413b5882e0`

Result: **CONDITIONAL PASS**

## Tested capability

First executable architecture-to-code vertical slice for selected HC invariants. The target is `runtime/reference_kernel/`; it is not a claim that the HC cognitive architecture as a whole has been implemented.

The slice attempts to make the following distinctions executable rather than prose-only:

- observation versus derived/predicted evidence;
- routed versus incorporated state;
- priority versus authority;
- latest/append order versus current-state projection;
- explicit supersession versus chronological replacement;
- action planning versus current effect authority;
- requested effect versus confirmed effect;
- pre-restart plan/authority versus post-restart currentness;
- unresolved in-flight effect versus safe blind retry.

## Evidence snapshot

Repository artifacts:

- `runtime/reference_kernel/hc_kernel.py`
- `runtime/reference_kernel/test_hc_kernel.py`
- `runtime/reference_kernel/README.md`
- `.github/workflows/reference-kernel.yml`

Governing architecture inspected during implementation:

- `docs/runtime/HYPERCONNECTOME_RUNTIME_MODEL.md`
- `routing instructions with neuroplasticity/TYPED_ROUTING_AND_PLASTICITY.md`
- `current memory storage/CURRENT_STATE_SELECTION.md`
- `basic operating instructions/AUTHORITY_CONSENT_AND_EFFECT_GOVERNANCE.md`
- `kinesis/ACTION_GATEWAY.md`
- `docs/architecture/SOURCE_INFORMATION_ANCESTRY_AND_DERIVED_STATE.md`

## Observed execution evidence

A local isolated Python 3 execution of the pre-commit reference-kernel candidate ran eight `unittest` cases and returned:

`Ran 8 tests ... OK`

The cases exercised competing current-memory heads, cross-scope supersession rejection, prediction-versus-observation typing, high-priority routing without effect authority, revocation after planning, requested-versus-confirmed effect state, restart handling of in-flight effects, and stale pre-restart plans.

This local execution is useful development evidence, but it is not treated as independent review or as proof that every repository byte later committed was exercised by that run.

## Repository CI attempt

Two GitHub Actions runs were triggered after the repository implementation was committed:

- run `34539356596` at `ccd0262d68c83846a2d6640269a9e67075c438f3`;
- run `34539477839` at `17add6f4c625cecc90473654d079ad413b5882e0` after removing dependencies on `actions/checkout` and `actions/setup-python`.

Both runs concluded `failure`, but the GitHub job surface reported **zero executed steps** for each job. Therefore these results are classified as CI execution/infrastructure failure, not as evidence that a reference-kernel unit test failed.

`WORKFLOW_FAILURE_WITH_NO_EXECUTED_TEST_STEP != UNIT_TEST_FAILURE`

Repository-exact CI execution remains unresolved.

## Architecture/code observations

At this cut, direct code inspection shows:

- `derive()` rejects relabeling derived state as `OBSERVATION` and requires known evidence parents;
- derived evidence preserves causal parent identifiers and inherited source references;
- `route()` records delivery metadata without automatically marking the event incorporated or authorized;
- current memory is append-oriented and returns `AMBIGUOUS` when more than one unsuperseded head exists in a logical scope;
- supersession cannot cross the declared logical record key;
- effect requests fail closed without a grant and re-check grant scope/currentness at request time;
- a revoked, expired, scope-mismatched, or stale-epoch grant cannot authorize the request;
- successful effect request is represented as `REQUESTED`, not `CONFIRMED`;
- restart advances an epoch, marks requested-but-unconfirmed effects unresolved, and prevents stale pre-restart plans/grants from silently becoming current.

## Known implementation limitations

The current slice is intentionally small and has material limitations:

- state is in-memory only; `restart()` is a modeled recovery epoch, not a real process crash/durable restore;
- it does not implement the full temporal hypergraph, coalition formation, distributed arbitration, plasticity, salience, semantics, deep memory, embodiment, affect/homeostasis, or protected updates;
- authority-grant issuance is a prototype fixture interface rather than a qualified authority-admission system;
- effect confirmation currently trusts an explicitly supplied evidence identifier without yet proving that the evidence is causally bound to the effect being confirmed;
- no schema registry or typed payload validation is implemented;
- random UUID identities make exact deterministic replay unavailable at this cut;
- there is no concurrency, partition, resource-pressure, or multi-constituent execution model;
- no performance, safety, security, or behavioral claims are established.

These limitations are not hidden TODOs; several are deliberate hostile-review targets for the next implementation cut.

## Qualification decision

**CONDITIONAL PASS** for the narrow claim that HC now has an executable reference slice whose code structure implements several central distinctions and whose pre-commit candidate passed the stated local tests.

The following stronger claims are not supported:

`REFERENCE_KERNEL_CONDITIONAL_PASS != HC_IMPLEMENTATION_PASS`

`REFERENCE_KERNEL_CONDITIONAL_PASS != GENERAL_COGNITION`

`LOCAL_DEVELOPMENT_TEST_PASS != REPOSITORY_CI_PASS`

`MODELED_RESTART_EPOCH != DURABLE_CRASH_RECOVERY`

`GRANT_FIXTURE != QUALIFIED_AUTHORITY_ADMISSION`

`EFFECT_CONFIRMATION_API != PHYSICAL_OUTCOME_PROOF`

## Required next evidence

Before raising this slice above CONDITIONAL PASS:

1. execute the exact committed files in a functioning runner or equivalent repository-exact environment;
2. add causal binding requirements for effect-confirmation evidence;
3. replace or constrain prototype grant minting so the kernel cannot be mistaken for a self-authorizing authority source;
4. independently review current-memory head selection and restart/effect semantics;
5. hostile-test provenance laundering, stale authority, replay, false confirmation, and namespace confusion;
6. add a durable crash/reload test before making recovery claims beyond modeled epoch fencing.

Evaluator: Noëtarch / Noah, Warden.

Reviewer provenance: primary implementation author/evaluator; **not independent**.
