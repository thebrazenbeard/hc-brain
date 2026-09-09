# Subsystem Lifecycle Contract

Status: canonical operating contract.

## Purpose

This contract defines how first-class HC subsystems exist, activate, develop, fail, recover, and learn without collapsing distinct state dimensions into one lifecycle label.

A subsystem's architectural existence is not the same thing as whether it is active, mature, healthy, implemented, authorized, or currently learning.

The governing separation is:

`PRESENCE != ACTIVATION != DEVELOPMENTAL_MATURITY != HEALTH != IMPLEMENTATION_STATUS != AUTHORIZATION != LEARNING_POLICY`

No single axis may silently stand in for another.

## 1. Presence

Presence answers whether the capability belongs to the instantiated HC architecture.

Canonical values:

- `PRESENT`
- `ABSENT`
- `EXTERNAL_ONLY`
- `UNKNOWN`

Every mandatory canonical HC root system is `PRESENT` in a conforming complete HC. `ABSENT` and `EXTERNAL_ONLY` are valid for optional extensions, peripherals, research configurations, or explicitly incomplete/nonconforming implementations, not for required intrinsic systems.

`DISABLED != ABSENT`

`UNIMPLEMENTED != ABSENT`

`FAULTED != ABSENT`

## 2. Activation

Activation answers whether a present capability is currently allowed or recruited to execute.

Canonical values:

- `DISABLED`
- `DORMANT`
- `DEVELOPING`
- `ACTIVE`
- `INHIBITED`

Activation is runtime state, not architectural existence.

An implementation should record why an activation transition occurred and which gate, condition, developmental rule, or operator/process authorized it where materially relevant.

## 3. Developmental maturity

Maturity answers how developed or calibrated the capability is within its declared scope.

Canonical values:

- `UNDEVELOPED`
- `CALIBRATING`
- `LEARNING`
- `STABLE_WITHIN_SCOPE`
- `ADAPTING`

Maturity never implies universal competence. A capability can be active while immature, dormant while mature, or adapting while nominally healthy.

## 4. Health

Health answers whether the present capability is functioning within its currently qualified envelope.

Canonical values:

- `NOMINAL`
- `DEGRADED`
- `FAULTED`
- `QUARANTINED`
- `UNKNOWN`

A fault must not be represented merely as deactivation if the distinction matters to diagnosis, coalition behavior, memory trust, action safety, or recovery.

## 5. Implementation status

Implementation status is an engineering/deployment axis, not a runtime cognitive state.

Recommended values:

- `DESIGN_ONLY`
- `UNIMPLEMENTED`
- `PROTOTYPE`
- `EXPERIMENTAL`
- `QUALIFIED_WITHIN_SCOPE`

A subsystem may be architecturally `PRESENT` in the complete template while a particular implementation is still `DESIGN_ONLY` or `UNIMPLEMENTED`.

This is how the repository can describe the complete eventual organ without pretending every current prototype already physically realizes every capability.

`ARCHITECTURALLY_PRESENT != IMPLEMENTED`

`IMPLEMENTED != QUALIFIED`

## 6. Authorization

Authorization answers what a subsystem or coalition may actually do with its capability.

Activation does not confer authority.

`ACTIVE != AUTHORIZED`

`CAPABLE != PERMITTED`

`PREDICTS_WELL != AUTHORIZED_TO_ACT`

Authorization may be scoped by effect class, embodiment, target, privacy boundary, consent state, maintenance mode, developmental qualification, resource state, or other governing contracts.

## 7. Learning policy while inactive or immature

Whether a present but inactive capability may learn is an independent policy decision.

Recommended policies:

- `NO_LEARNING`
- `OBSERVE_ONLY`
- `SHADOW_LEARNING`
- `BOUNDED_DEVELOPMENT`
- `FULL_LEARNING_WITHIN_SCOPE`

Examples:

- a dormant mature capability may receive no background learning;
- a disabled high-risk capability may observe but not alter durable state;
- a developing capability may perform shadow prediction and accumulate evaluation evidence;
- an active qualified capability may learn only within explicitly permitted plasticity scopes.

Learning permission does not imply effect authority, memory authority, semantic truth, consent, or identity admission.

## 8. State transition record

Material lifecycle transitions should be provenance-bearing.

A generic transition record should be able to carry:

```text
SUBSYSTEM_STATE_TRANSITION {
  subsystem
  prior_state_vector
  successor_state_vector
  changed_axes[]
  trigger
  authority_or_policy_basis
  evidence_refs[]
  timestamp
  expected_prior_version
  transition_version
  reason
  recovery_or_review_requirements[]
}
```

The state vector may include presence, activation, maturity, health, implementation status, authorization scopes, and learning policy as applicable.

A transition that changes one axis must not silently mutate the others.

## 9. Typical developmental and operational transitions

A developmental path may resemble:

```text
presence=PRESENT
activation=DISABLED
maturity=UNDEVELOPED
->
activation=DORMANT
->
activation=DEVELOPING, maturity=CALIBRATING
->
activation=DEVELOPING, maturity=LEARNING
->
activation=ACTIVE, maturity=STABLE_WITHIN_SCOPE
```

Operational transitions may include:

```text
ACTIVE/NOMINAL -> ACTIVE/DEGRADED
ACTIVE/DEGRADED -> INHIBITED/DEGRADED
DEGRADED -> FAULTED
FAULTED -> QUARANTINED
QUARANTINED -> DEVELOPING or DORMANT after bounded recovery/requalification
```

No such transition deletes the subsystem's architectural presence.

## 10. Fault propagation contract

A subsystem entering `DEGRADED`, `FAULTED`, `QUARANTINED`, or `UNKNOWN` health should expose enough state for distributed reconfiguration rather than forcing downstream systems to infer failure from silence.

At minimum, fault state should declare where applicable:

- affected capabilities;
- confidence in the diagnosis;
- safe degradation mode;
- whether alternate HC-internal routes exist;
- whether current coalitions must terminate, re-form, or continue with reduced weight;
- whether outputs remain admissible as evidence and at what trust level;
- whether durable state remains trusted;
- action/effect restrictions;
- recovery and requalification requirements.

Local failure should remain local when possible. Whole-organ inhibition is reserved for faults whose consequence genuinely crosses protected system boundaries.

## 11. Coalition participation

Coalition membership is runtime-effective topology, not subsystem lifecycle state.

A subsystem can be `ACTIVE` without participating in a particular coalition. A `DORMANT` subsystem may be recruited and activated when a valid trigger and gate exist. A degraded subsystem may participate with explicit reduced reliability if the relevant arbitration and safety rules allow it.

`ACTIVE != MEMBER_OF_EVERY_RELEVANT_COALITION`

`ROUTED != HEALTHY`

`RECRUITED != AUTHORIZED`

## 12. Recovery and requalification

Recovery is not assumed merely because a fault disappears.

Depending on subsystem class, recovery may require:

- self-test;
- calibration;
- replay/evaluation;
- state-integrity verification;
- interface re-registration;
- body-schema remapping;
- confidence recalibration;
- bounded shadow operation;
- action-authority requalification.

A recovered subsystem may therefore move from `FAULTED` or `QUARANTINED` to `DEVELOPING` or `DORMANT` before returning to unrestricted `ACTIVE` use.

## 13. Template completeness rule

A mandatory capability is not removed from the architecture merely because:

- the first hardware revision does not implement it;
- the current body lacks its sensor/effect channel;
- current use does not require it;
- development has not occurred;
- activation is contextually inappropriate;
- it is temporarily faulted or quarantined.

The complete template should define the capability's architectural home and represent its actual implementation, maturity, activation, health, learning, and authorization state honestly.

## Evidence boundary

This is an HC architecture/state-management contract. It defines implementation semantics and does not establish consciousness, personhood, subjective experience, or biological equivalence.

## Provenance

Selectively generalized from the preserved `contracts/SUBSYSTEM_LIFECYCLE.md` on `research/hyperconnectome-foundations-20260909`, then reconciled against the canonical orthogonal capability axes, complete-organ manifest, developmental-learning contract, runtime invariants, action-authority boundaries, and distributed temporal-hypergraph model. The source branch's collapsed lifecycle vocabulary was not adopted where it conflicted with the canonical orthogonal-axis model.
