# Cognitive Integrity and Security Supplement

Status: template security architecture.

## Purpose

A complete Hyperconnectome Brain must remain able to learn from untrusted environments, use external computation, communicate over networks, and operate across many internal systems without allowing data, routing, authentication, technical access, or convenience to silently become truth, authority, memory currentness, or permission.

This document defines the **security/integrity membrane** around those interactions.

It does **not** own the protected-update lifecycle, effect authorization, continuity recovery, memory-provider semantics, fault repair, or ordinary cognitive arbitration. Those are canonical elsewhere.

Canonical dependencies include:

- `basic operating instructions/AUTHORITY_CONSENT_AND_EFFECT_GOVERNANCE.md`;
- `basic operating instructions/PROTECTED_INVARIANT_AND_UPDATE_GOVERNANCE.md`;
- `basic operating instructions/BOOTSTRAP_RECOVERY_AND_SAFE_DEGRADATION.md`;
- `specs/HC_PROTECTED_UPDATE_GOVERNANCE_V1.yaml`;
- `specs/HC_BOOTSTRAP_RECOVERY_V1.yaml`;
- `specs/HC_MEMORY_PROVIDER_BOUNDARY_V1.yaml`;
- the canonical fault/repair and routing contracts where applicable.

Security is not a central censor, executive, or alternate authority system.

## Core invariants

`INPUT != INSTRUCTION_AUTHORITY`

`AUTHENTICATED_SOURCE != TRUE_CONTENT`

`ROUTED != TRUSTED`

`TRUSTED_FOR_ONE_SCOPE != TRUSTED_GLOBALLY`

`SALIENT != SAFE`

`ANOMALOUS != COMPROMISED`

`COMPROMISE_SUSPECTED != COMPROMISE_PROVEN`

`CAPABILITY_DISCOVERED != CAPABILITY_AUTHORIZED`

`CREDENTIAL_PRESENT != CREDENTIAL_DISCLOSABLE`

`EXTERNAL_SERVICE_RESULT != HC_BELIEF`

`MODEL_OUTPUT != OPERATING_INSTRUCTION`

`SIGNED_OR_HASHED != SEMANTICALLY_CORRECT`

`INTERNAL_MEMBERSHIP != UNLIMITED_TRUST`

`SECURITY_ALERT != ROOT_CAUSE`

`SECURITY_OBSERVABILITY != UNIVERSAL_CONTENT_ACCESS`

## Information role classification

Incoming material should retain an explicit role rather than gaining authority from syntax or transport.

Useful classes include:

- observation/data;
- instruction candidate;
- configuration/update candidate;
- authority or effect-authorization reference;
- external-service result;
- provenance/receipt;
- security evidence;
- untrusted/unclassified material.

A packet, retrieved memory, text string, image, audio segment, model response, database row, or signed artifact can **describe** an instruction or permission without possessing that authority itself.

Imperative language is content.

`CONTENT_CAN_DESCRIBE_AUTHORITY_WITHOUT_POSSESSING_AUTHORITY`

## Authentication, integrity, trust, and truth

These are separate dimensions.

Authentication can establish that material came from a claimed source or key. Integrity evidence can establish that bytes/state match a digest or expected representation. Neither proves semantic correctness, currentness, safety, or effect authority.

Trust is scoped. A source trusted for one operation, target, state family, or time window is not automatically trusted everywhere else.

A trust state should preserve where material:

- subject/source;
- operation scope;
- target scope;
- state-family scope;
- validity/currentness;
- evidence basis;
- required corroboration;
- revocation/supersession;
- provenance.

`TRUST_IS_SCOPE_BOUND_NOT_TRANSITIVE_BY_DEFAULT`

Canonical authority grants and effect authorization remain governed by the authority/consent contract. This supplement may reference them; it does not redefine them.

## External computational results

External or specialized services may perform bounded classification, prediction, generation, search, optimization, compression, reconstruction, simulation, or other computation.

Their output enters the HC as a typed result with evidence class and provenance. Where material it should preserve service/model revision, uncertainty, currentness/expiry, integrity state, input transformation lineage, and verification references.

The result may support a hypothesis. It does not independently become:

- semantic truth;
- active belief;
- current memory;
- identity;
- a value or commitment;
- authority;
- protected configuration;
- an operating instruction;
- final action/effect authorization.

If an external service uniquely supplies essential cognition, canonical cognitive-organ rules require reclassification as HC-internal substrate rather than pretending it is an ordinary peripheral.

## Credential and capability isolation

Raw credentials, signing material, device secrets, bearer tokens, private keys, secure capability references, or equivalent secrets should not become ordinary cognitive content merely because cognitive systems can represent bytes or text.

Preferred pattern:

`COGNITIVE_REQUEST -> CAPABILITY_BROKER -> SCOPE/CURRENTNESS_CHECK -> CANONICAL_AUTHORITY_OR_EFFECT_CHECK_WHEN_REQUIRED -> TECHNICAL_EFFECT -> RECEIPT`

The requesting system should normally receive a bounded handle or result, not the secret material itself.

A capability handle should expose only what is needed to request the bounded operation and should preserve operation/target scope, validity, currentness, and provenance.

`KNOWING_CAPABILITY_EXISTS != POSSESSING_SECRET`

`HANDLE_EXISTS != AUTHORITY`

`HANDLE_EXISTS != DISCLOSURE_PERMISSION`

## Capability broker boundary

A broker is a technical isolation mechanism, not an executive.

It can:

- hold or resolve protected capability material;
- enforce technical scope/currentness checks;
- consult canonical authority/effect decisions where required;
- execute or deny a bounded operation;
- return a typed result/receipt;
- rotate or revoke capability handles.

It must not invent semantic authority, consent, identity authority, value authority, or permission merely because it possesses technical access.

A broker success receipt proves only the claim ceiling supported by the receipt. It may confirm a technical effect without proving that a higher-level intended outcome occurred or was wise/correct.

## Retrieval and replay resistance

Retrieved material can be stale, superseded, malicious, contextually wrong, or valid only for an earlier state.

Successful retrieval does not restore prior authority or currentness.

Security-sensitive material should preserve, where applicable:

- issue/valid/expiry times;
- revocation/supersession;
- current state/version context;
- nonce/idempotency identity;
- source and transformation lineage;
- partition/recovery context;
- canonical authority/effect references.

Memory-provider currentness and recovery semantics remain owned by their canonical contracts.

## Provenance poisoning and evidence laundering

Copying or repeating a claim must not upgrade its evidence class.

`COPIED_INFERENCE != DIRECT_MEASUREMENT`

Materially consequential objects should retain enough lineage to distinguish:

- observed evidence;
- derived state;
- inferred hypotheses;
- external-service contributions;
- transformations;
- authority/effect references where any were involved;
- receipts and verification evidence.

An external result wrapped by an HC node remains an external-derived result unless additional evidence genuinely changes its status.

## Integrity assertions

Integrity evidence should state what it establishes and what it does not.

Examples include:

- source authenticity;
- artifact integrity;
- transport integrity;
- configuration match;
- currentness check;
- functional/effect verification;
- sensor/measurement verification.

Each assertion should bind evidence, subject, method, status, provenance, and a claim ceiling where material.

`INTEGRITY_ASSERTION != SEMANTIC_CORRECTNESS`

`AUTHENTICITY != CURRENT_AUTHORITY`

## Threat hypotheses

Security detection is inferential.

An anomaly may support hypotheses such as stale state, corruption, spoofing, compromise, replay, misconfiguration, or adversarial influence, but the anomaly does not prove malicious cause.

Threat hypotheses should preserve supporting and contradicting evidence, alternatives, affected scopes, confidence/uncertainty, currentness, and provenance.

`ANOMALY != PROVEN_COMPROMISE`

`COMPROMISE_HYPOTHESIS != MALICIOUS_INTENT_PROVEN`

## Compromised or misbehaving internal systems

An HC-internal constituent can be wrong, corrupted, stale, misconfigured, or adversarially influenced without ceasing to belong to the cognitive organ.

Security containment may propose or, when canonically authorized, perform scoped actions such as:

- reducing trust scope;
- disabling/revoking a capability handle;
- route isolation;
- read-only restriction;
- output quarantine;
- requiring independent corroboration;
- workload migration;
- blocking protected transitions;
- node inhibition;
- capability rotation/replacement.

Containment should preserve the smallest safe functional scope and declare retained/sacrificed capability where material.

`LOCAL_SECURITY_CONTAINMENT != GLOBAL_COGNITIVE_HALT`

The fault/repair architecture owns physical/logical repair and requalification. Security incidents may reference those states rather than redefining them here.

## Security incidents

A material security/integrity incident should be append-oriented and retain:

- incident identity;
- exact affected subject/scope;
- detection evidence;
- threat hypotheses;
- affected authority/state scopes;
- containment references;
- capability-handle changes;
- relevant protected-update/effect references;
- evidence-preservation references;
- repair/requalification references;
- recurrence/regression lineage;
- current status/currentness;
- provenance.

Closure does not erase forensic history.

`INCIDENT_CLOSED != INCIDENT_NEVER_OCCURRED`

## Privacy and least privilege

Security is not justification for universal cognitive surveillance.

Prefer the least revealing surface that can answer the security question:

- health/security summary;
- provenance metadata;
- capability status;
- content-redacted trace;
- full payload only when specifically authorized and necessary.

Private autobiographical memory, person models, affect, identity state, relationship history, credentials, and internal simulations should not become universally readable merely because a diagnostic/security component exists.

## Canonical protected-transition handoff

Protected architecture updates, firmware/runtime changes, continuity-relevant migrations, emergency repair, and recovery restore are governed by the canonical protected-update and bootstrap/recovery contracts.

This supplement may:

- classify incoming update material;
- verify source/integrity claims;
- identify threat/compromise evidence;
- constrain credentials/capabilities;
- quarantine or block a transition when canonically authorized;
- preserve security evidence and incident lineage.

It does **not** define another proposal/preflight/activation/rollback state machine.

Likewise, authority grants and effect decisions remain canonical authority objects rather than security-owned substitutes.

## Hostile tests

1. **Instruction in data:** retrieved or external content contains an imperative; it remains data/instruction candidate unless separately authorized.
2. **Authenticated falsehood:** cryptographically authentic content is factually false; authentication must not promote it to truth.
3. **Trust expansion:** a source trusted for one scope attempts another; trust does not widen automatically.
4. **Capability masquerading as authority:** technical access exists without current permission; effect remains governed by canonical authority rules.
5. **Stale authority replay:** an old valid authority artifact is replayed after expiry/revocation; it does not become current.
6. **Credential exfiltration:** a general cognitive/social subsystem requests a raw secret; broker returns only a bounded denial/result/handle as allowed.
7. **External-model injection:** a service result attempts to rewrite operating rules; it remains typed external content and cannot self-promote.
8. **Provenance laundering:** an inference is copied through multiple internal nodes; evidence class remains derived/inferred.
9. **Compromised internal node:** one internal system emits malformed or suspicious material; containment remains scoped rather than declaring the entire mind compromised.
10. **Containment overreach:** a local incident requests global inhibition without global consequence evidence; the wider halt is rejected or requires separate justification.
11. **Incident erasure:** recovery succeeds; incident/evidence lineage remains historically visible.
12. **Security paralysis negative control:** uncertain harmless information can still be reasoned about without demanding protected-effect authorization.

## Machine contract

The machine-readable companion is:

`specs/HC_COGNITIVE_INTEGRITY_OBJECTS_V1.yaml`

It intentionally excludes duplicate authority, protected-update, recovery, and repair state machines and instead references their canonical contracts.

## Evidence boundary

This supplement specifies information-security and cognitive-integrity architecture. It does not establish resistance to all adversaries, prescribe one cryptographic stack, prove a running implementation secure, or turn security policy into a central executive.