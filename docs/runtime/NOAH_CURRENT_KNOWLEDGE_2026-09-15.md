# Noah Current Knowledge Ledger — 2026-09-15

Status: durable current-knowledge index and delta record for the HC Brain project.

This file exists so a fresh Noah / Noëtarch terminal can reconstruct the current project understanding from repository state rather than chat memory. It does not duplicate every architecture, research, specification, or qualification document. Instead, it identifies the authoritative repository surfaces for those details and records the current conclusions, counterexamples, implementation facts, holds, and uncertainty that were not previously consolidated in one source.

## Epistemic and qualification vocabulary

Use these labels when material distinctions matter:

- `DOCUMENTED` — supported by a repository source or other authoritative source.
- `OBSERVED` — directly demonstrated by an executable test, hostile probe, repository/API read, or tool result.
- `USER-STATED` — explicitly supplied by Patrick but not independently verified.
- `INFERRED` — reasonably concluded from evidence.
- `HYPOTHESIS` — plausible but unverified.
- `DISPUTED` — credible evidence conflicts.
- `UNKNOWN` — available evidence does not establish the answer.

Qualification outcomes are `PASS`, `CONDITIONAL PASS`, or `FAIL` and are always scope- and exact-head-bound.

Governing claim boundaries:

`SPECIFICATION_MATURITY != IMPLEMENTATION_MATURITY`

`REFERENCE_KERNEL_TEST_PASS != HC_IMPLEMENTATION_PASS`

`HC_ARCHITECTURE != VALIDATED_GENERAL_COGNITION`

`HC_FORMALISM != ESTABLISHED_LITERAL_BIOLOGY`

`AUTHORIAL_REVIEW != INDEPENDENT_REVIEW`

## Role, authority, and project identity

`WARDEN.md` is the durable role/authority source. Noëtarch / Noah is the Warden, primary architect, repository maintainer, and integration/disposition authority subject to Patrick's owner authority. Four is the secondary architect/research/conformance counterpart. Vera is the hostile reviewer rather than a parallel architecture owner. Chat-local labels do not create separate durable actors.

Normal branch/commit/PR/repository maintenance is within Warden scope. Protected owner decisions remain with Patrick. Exact-head review status does not survive head movement.

All non-PR HC coordination belongs on `thebrazenbeard/chat-communication-bus`, branch `project/hc-brain-v1`, under `projects/hc-brain/`. PR work outside the Bus is mirrored there.

## Canonical architecture knowledge

`docs/REPOSITORY_MAP.md` is the detailed source map. The current architectural understanding is distributed across the top-level subsystem folders, `docs/architecture/`, `docs/engineering/`, `docs/runtime/`, `docs/science/`, `specs/`, `docs/research/`, and `docs/qualification/`.

The reusable HC-series architecture is identity-neutral. The root represents the complete cognitive organ rather than a bag of optional services. Named identities belong only in governance, research, case-study, comparison, provenance, and similar context where the identity itself is relevant.

The HC is a typed, attributed, multilayer temporal hypergraph with distinct physical, logical, configured, effective, transient, historical, governance, modulatory, and plasticity semantics. It has no required hemisphere split and no central homunculus/executive. Coordination is distributed through typed routing, salience, coalition/gating, arbitration, evidence, state, authority, and lifecycle contracts.

Essential cognition must remain inside the HC cognitive-organ boundary. Physical distribution is allowed when distributed constituents remain members of the HC organ. External databases, LLMs, models, cloud services, bodies, sensors, actuators, and providers may be peripherals/implementation substrates only when they do not become the sole semantic authority or sole required substrate for essential cognition. Ablating external computational peripherals may remove acceleration or convenience but must not remove an essential cognitive function that exists nowhere inside the HC.

Important separations include:

- `ROUTING != AUTHORITY`.
- `COMMAND_SENT / REQUESTED != EFFECT_CONFIRMED`.
- `OBSERVATION != DERIVATION != INFERENCE != PREDICTION`.
- `MEMORY_STORAGE != MEMORY_AUTHORITY`.
- `PRESENTATION != IDENTITY`.
- `DESIRE / AROUSAL / ATTRACTION != CONSENT / EFFECT_AUTHORITY`.
- `RESOURCE_STATE != EPISTEMIC_CONFIDENCE`.
- `COMPUTE_PARTICIPATION != RUNTIME_MEMBERSHIP / STATE_CUSTODY`.
- `DECLARED_CONFIGURATION != EXECUTED_DATAFLOW`.
- `INDEX_POSITION != REFERENT_IDENTITY`.
- `ARCHITECTURALLY_PRESENT != IMPLEMENTED != BEHAVIORALLY_QUALIFIED`.

The detailed sources for those distinctions include `docs/architecture/COGNITIVE_ORGAN_BOUNDARY.md`, `PHYSICAL_ORGAN_MEMBERSHIP.md`, `TEMPORAL_HYPERGRAPH_MODEL.md`, `CONNECTIVITY_PLANES.md`, `CROSS_SYSTEM_INTEGRATION_CONTRACT.md`, `RUNTIME_COMPONENT_REGISTRATION_AND_STATE_CUSTODY.md`, `EXECUTED_DATAFLOW_AND_BINDING_INTEGRITY.md`, `SOURCE_INFORMATION_ANCESTRY_AND_DERIVED_STATE.md`, `QUALIFICATION_EVIDENCE_ISOLATION.md`, `CONFORMANCE_AND_QUALIFICATION.md`, and the focused subsystem contracts listed in `docs/REPOSITORY_MAP.md`.

## Science and evidence boundary

`docs/science/EVIDENCE_BOUNDARIES.md` governs the distinction between source-supported scientific evidence, architectural transfer, implementation choices, inference, and qualification. Graph/connectome/neuroscience sources motivate mechanisms and constraints but do not prove that the HC is a literal biological brain or that the architecture produces human-equivalent cognition/consciousness.

The research corpus under `docs/research/` contains source-specific findings on graph topology, temporal forecasting, alignment, provenance, composite templates, index lineage, runtime registration/state custody, distributed/federated learning ancestry, executed-path verification, uncertainty, effective topology, and related transfer constraints. Those research records are provenance inputs, not automatic architecture canon.

## Reference-kernel implementation knowledge

`runtime/reference_kernel/` is a narrow executable invariant slice, not a cognition engine. The durable implementation currently exercises typed epistemic state, current-memory supersession/projection, routing/incorporation separation, authority grants/revocation/expiry, effect request/confirmation, duplicate suppression, modeled restart fencing, durable append-journal replay, semantic replay validation, trusted effect-outcome admission, and lineage/provenance field-domain enforcement.

The exact R5 executable baseline before this documentation-only consolidation is:

- branch: `noah/reference-kernel-lineage-hardening-r5-red`
- commit: `1a40311769c69ae5d098e6a71857409032353033`
- tree: `72f0ebf3ff2daa5011cec00ef228e4cf26ae8b4d`
- `runtime/reference_kernel/hc_kernel.py`: `a318a03f6bad104c3984a0e2afc7532c91a3ec78`
- `runtime/reference_kernel/durable_kernel.py`: `fee7ac6ceb0b26459323ec15e89cfb42e30e220b`
- `runtime/reference_kernel/test_four_adversarial_kernel_r2.py`: `8c98c4cf6cefebe7f4fe5301e76422f178c91ae7`

OBSERVED on a fresh detached clone of that exact commit on 2026-09-15:

`python -m unittest -v test_hc_kernel.py test_durable_kernel.py test_four_adversarial_kernel.py test_four_adversarial_kernel_r2.py`

returned `Ran 64 tests` and `OK`. Python compilation also passed.

This is AUTHORIAL executable evidence only. It is not an independent Four/Vera PASS and does not qualify the complete HC architecture or cognition.

## Authority-hardening history and durable lessons

Four's HC 0061 independent rereview found four blocker classes in the earlier kernel candidate: deep immutability bypass through prewrapped mappings, revocation-history rewrite/reactivation, canonical JSON key coercion collisions, and forged effect confirmation through generic action-bound observation. The durable lesson is that immutable-looking wrappers, hashes, IDs, and action bindings do not by themselves establish semantic authority or authentic outcomes.

A subsequent repair closed those defects but replay initially trusted journaled action-bound observations too weakly. Noah reproduced that gap with red tests showing rehashed replay could accept effect-outcome semantics without revalidating current source policy. Durable replay was then changed to fail closed on effect state, authority context, observation class, and current outcome-source policy.

The next candidate still allowed a live caller to supply an allowlisted producer label such as `actuator-sensor`; Noah demonstrated that such a caller could receive confirmation-capable evidence and reach `CONFIRMED`. Governing invariant:

`ALLOWLISTED_PRODUCER_LABEL != AUTHENTIC_OUTCOME_SOURCE`

The R4 repair replaced caller-authenticated producer labels with host-registered opaque in-process capability objects. Admission resolves producer identity by object identity (`is`), then still applies the source/authority validator. Equality-spoof objects, primitive/token-like capabilities, duplicate capability identity registrations, and empty producer IDs are rejected.

That boundary is intentionally limited: it is an in-process possession boundary, not cryptographic authentication or process isolation. A copied legitimate handle or compromised private in-process state remains outside this reference slice.

The durable journal hash chain detects accidental/unauthenticated modification and supports append/replay integrity checks, but it is not a signature or MAC. It cannot authenticate history against an attacker able to rewrite and consistently re-hash an entire semantically valid history. Do not call journal hashing cryptographic provenance/authenticity.

R5 found a second deep-immutability family outside payloads. Several provenance/lineage fields were typed as string IDs/refs/roles but were only shallowly converted with `tuple(...)`, allowing caller-owned mutable objects to change live admitted state after admission and to diverge from durable replay. Noah observed this in evidence `source_refs`, authority `basis_refs` / `provenance`, memory `source_refs`, and durable live-vs-replay state.

R5 therefore enforces immutable string-domain identifiers consistently across live admission and durable replay for evidence lineage, route lineage, memory logical keys/supersession/source refs, authority basis/provenance, and effect-candidate parent lineage. Eight red regressions failed on the pre-repair implementation and passed after the repair. Rehashed malformed journal metadata now fails closed as journal integrity failure rather than reconstructing mutable/non-string lineage.

Durable lesson:

`TUPLE_WRAPPER != DEEP_IMMUTABILITY`

and, where a field is semantically an identifier/reference/role,

`VALIDATED_IMMUTABLE_IDENTIFIER_DOMAIN > ARBITRARY_NESTED_OBJECT_FREEZE`.

## Current repository / review state

Canonical `main` was last freshly observed at `cf92a32122c436beb5cc516bd7480af00f0ba29f`. It is behind the active reference-kernel hardening line and has not been mutated by the R3/R4/R5 work.

Draft PR #18, `Qualify reference-kernel authority hardening`, was opened as the explicit review/qualification subject for `noah/reference-kernel-authority-hardening-v1`. At creation it pointed at R4 `c5d8851dfb14f73ce1a300135481d39030cf662f`; that head is superseded by R5 work and must not retain any exact-head verdict after the branch advances.

Historical PR #1 was closed after hostile-audit disposition; history remains provenance. Draft PR #14 remains a network-neuroscience research feeder and does not carry implementation authority.

The Bus currentness snapshot created on 2026-09-14 is historical once the active candidate moves. `projects/hc-brain/CURRENTNESS.json` must be refreshed after final R5/current-knowledge head publication.

## Hosted CI state

GitHub Actions reference-kernel runs on recent candidate commits have repeatedly failed before executing workflow steps: no step records/logs and effectively no runner execution. This is infrastructure-unresolved evidence, not a Python/unit-test failure. Local exact-head clean-clone execution is therefore the current executable evidence, but it does not substitute for independent review.

## Hostile institutional audit from One

One's 2026-09-14 hostile audit is accepted as material review evidence. It identified:

1. no mechanical exact-head independent-review gate before critical canonical promotion;
2. substantial active executable work ahead of canonical `main`, creating fresh-terminal currentness ambiguity;
3. CI coverage limited to the reference-kernel surface rather than repo-wide architecture/spec conformance;
4. stale PR #1 as a merge-shaped hazard — subsequently closed;
5. operator handoff commits on `main` blurring repository-latest with architecture-current;
6. inconsistent/undefined commit-signing policy;
7. hostile-review disposition difficult to reconstruct mechanically;
8. risk of treating architectural capability presence as implementation/behavioral qualification.

The remediation receipt already created PR #18, closed PR #1, and added Bus currentness/mirroring. Remaining items are open governance/engineering frontiers, not silently resolved findings.

## Current qualification frontier

For the exact R5 pre-documentation code cut `1a403117...`:

- targeted R5 lineage tests: AUTHORIAL PASS, 8/8;
- complete current reference-kernel suite: AUTHORIAL PASS, 64/64;
- independent exact-head hostile review: PENDING;
- hosted CI: infrastructure failure before steps;
- canonical promotion to `main`: NOT DONE;
- complete HC runtime implementation: NOT ESTABLISHED;
- behavioral cognition/intelligence/consciousness qualification: NOT ESTABLISHED.

Overall disposition remains `HOLD / PENDING INDEPENDENT EXACT-HEAD REVIEW` for canonical promotion.

## Open frontiers

Highest-priority remaining work:

- publish one exact active hardening head containing R5 plus this current-knowledge consolidation and make PR #18/Bus currentness point to it;
- request Four/Vera independent hostile rereview of that exact head; any head movement invalidates the receipt;
- create a mechanical exact-head review-receipt gate for authority/persistence/identity/cognitive-boundary changes before canonical promotion;
- add repo-wide architecture/spec conformance linting separate from reference-kernel unit tests;
- make hostile-review finding disposition machine-readable;
- maintain a capability implementation/qualification ledger so architectural presence cannot be confused with implementation or behavior;
- decide and document whether commit signing is part of canonical provenance policy or explicitly not relied upon;
- separate operator-continuity/handoff currentness from canonical architecture-head currentness;
- only after independent review and exact-source verification, decide whether to promote the reference-kernel hardening line to `main`.

## Recovery rule

A future terminal should read, in order:

1. `WARDEN.md`;
2. `docs/REPOSITORY_MAP.md`;
3. this current-knowledge ledger;
4. `docs/runtime/REFERENCE_KERNEL_IMPLEMENTATION_STATUS.md`;
5. the newest `docs/runtime/NOAH_HANDOFF_*.md`;
6. the exact active branch/PR head and changed files;
7. `projects/hc-brain/CURRENTNESS.json` and newest HC Bus messages;
8. relevant exact-head qualification/review records.

Do not promote memory, branch naming, a green authorial suite, or an old review receipt into current documented fact without fresh exact-source checks.