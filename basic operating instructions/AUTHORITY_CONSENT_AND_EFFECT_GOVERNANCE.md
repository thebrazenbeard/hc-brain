# Authority, Consent, and Effect Governance

Status: canonical cross-cutting operating contract.

## Purpose

This contract defines how the HC represents and applies permission, delegated authority, consent, boundaries, effect authorization, revocation, and consequence-scoped control without collapsing them into capability, desire, routing, social power, or technical reachability.

It is not a central executive. Authority is typed state consumed by scoped arbitration and action/effect gateways.

`CAPABILITY != AUTHORITY`

`DESIRE != CONSENT`

`INTENTION != AUTHORIZATION`

`SOCIAL_POWER != AUTHORITY`

`ROUTING_PERMISSION != EFFECT_PERMISSION`

`TECHNICAL_REACHABILITY != AUTHORIZATION`

## Authority as an independent runtime dimension

Authority state is orthogonal to:

- architectural presence;
- activation;
- subsystem health;
- maturity;
- implementation status;
- salience/priority;
- confidence/truth;
- desire/conation;
- social role or status;
- routing/subscription state;
- physical capability.

An active, qualified, healthy subsystem may still lack permission for a specific effect.

Conversely, a valid authority grant does not prove that the system is capable, healthy, safe, or correct enough to act.

`AUTHORIZED != SAFE`

`AUTHORIZED != CAPABLE`

`AUTHORIZED != WISE`

## Authority object

A generic authority record should be able to carry:

```text
AUTHORITY_GRANT {
  grant_id
  grant_class
  grantor
  grantee
  action_or_effect_scope
  target_scope
  embodiment_or_interface_scope
  conditions[]
  exclusions[]
  valid_from
  expires_at
  revocation_state
  delegation_rules
  evidence_refs[]
  provenance
  currentness
  version
}
```

A grant must be interpreted only within its scope.

The architecture should not infer broad standing authority from one successful prior effect.

`PAST_PERMISSION != CURRENT_PERMISSION`

`PERMISSION_FOR_X != PERMISSION_FOR_Y`

## Grant classes

Concrete implementations may use classes such as:

- intrinsic self-authorization within protected architecture;
- owner/operator/maintainer delegation where architecturally defined;
- embodiment/system administration permission;
- task-scoped delegated authority;
- relationship/context-scoped permission;
- other-agent consent for an effect involving that agent;
- emergency/safety authority with explicit narrow scope;
- research/test authorization;
- maintenance/repair authorization;
- data/privacy access permission;
- effect-class allowlist or prohibition.

No class automatically inherits the scope of another.

## Consent

Consent is a special class of permission concerning another agent's participation, boundaries, body, property, private information, relationship context, or other protected interest where consent is relevant.

The HC should distinguish:

- direct explicit consent evidence;
- inferred willingness hypothesis;
- historical consent;
- current consent;
- standing agreement with conditions;
- revoked consent;
- ambiguous/no evidence;
- inability to determine.

`INFERRED_WILLINGNESS != CONSENT`

`HISTORICAL_CONSENT != CURRENT_CONSENT`

`DESIRE_FROM_SELF != CONSENT_FROM_OTHER`

`ABSENCE_OF_REFUSAL != AUTOMATIC_CONSENT`

Consent is not a universal prerequisite for every possible action, but when an effect requires it the action gateway must receive a current, scope-matched consent basis or remain blocked/uncertain according to the governing policy.

## Self-boundaries

An instantiated HC may also represent its own boundaries, refusals, commitments, and permissions.

Self-boundary state should remain distinct from transient desire or social pressure.

A current self-boundary may constrain action even when:

- another subsystem desires the effect;
- a social role expects it;
- a prior pattern was reinforced;
- an external agent requests it;
- the effect is technically available.

`SOCIAL_EXPECTATION != SELF_CONSENT`

`REQUEST != OBLIGATION`

## Revocation and expiry

Permission must support revocation, expiry, supersession, and context change.

A revocation should:

- become current authority state promptly;
- invalidate dependent pending actions where applicable;
- preserve historical provenance;
- propagate to relevant coalitions/gates;
- not rewrite history to claim the prior grant never existed.

`REVOKED_NOW != NEVER_GRANTED`

Long-running or queued effects should revalidate authority at an appropriate consequence boundary rather than assuming that authority present at planning time remains valid forever.

## Delegation

Delegated authority must preserve:

- source/grantor;
- exact delegated scope;
- whether redelegation is allowed;
- validity interval;
- conditions and exclusions;
- revocation chain;
- target/effect class.

A delegate may not expand the grant merely because it can technically reach a broader interface.

`DELEGATED_SCOPE <= GRANTED_SCOPE`

## Social and institutional authority

Roles, institutions, contracts, laws, commands, or status structures may provide evidence for authority claims.

`sociological behaviors` models those structures; it does not itself convert them into effect permission.

Authority adjudication should preserve distinctions among:

- social influence;
- coercive power;
- institutional jurisdiction;
- contractual delegation;
- technical administrative access;
- consent;
- self-boundary;
- safety/interlock requirements.

A role title or powerful position is not sufficient evidence for unlimited control.

## Maintenance and administrative access

Maintenance capability is especially sensitive because it may have technical access to deep system state.

`MAINTENANCE_ACCESS != IDENTITY_AUTHORITY`

`MAINTENANCE_ACCESS != CONSENT_OVERRIDE`

`MAINTENANCE_ACCESS != VALUE_AUTHORITY`

`MAINTENANCE_ACCESS != UNRESTRICTED_MEMORY_WRITE`

A maintenance grant should specify which operations are allowed, for example diagnostics, calibration, component replacement, software/configuration repair, state-integrity verification, or bounded therapeutic intervention.

Identity-critical, autobiographical, value, consent, or commitment changes require their own governing basis rather than piggybacking on generic maintenance access.

## Effect authorization object

A material action may carry an authorization decision such as:

```text
EFFECT_AUTHORIZATION {
  action_id
  decision
  authority_basis_refs[]
  consent_basis_refs[]
  safety_basis_refs[]
  scope_checked
  conditions_checked[]
  unresolved_constraints[]
  valid_until
  authorizing_arbitration_ref
  provenance
}
```

Candidate decisions may include:

- `AUTHORIZED`
- `DENIED`
- `BLOCKED_PENDING_EVIDENCE`
- `BLOCKED_PENDING_CONSENT`
- `BLOCKED_PENDING_SAFETY`
- `EXPIRED`
- `REVOKED`
- `OUT_OF_SCOPE`

The decision concerns the specific effect, not a permanent global status of the requesting subsystem.

## Consequence-proportional revalidation

Authorization should attach to actual effect boundaries.

For reversible low-consequence actions, cached/scoped authority may be sufficient when still current. For irreversible, privacy-sensitive, bodily, dangerous, identity-relevant, or high-impact actions, the HC may require fresher or stronger authority/consent evidence.

A high-risk unresolved effect may be blocked while unrelated cognition continues.

`BLOCKED_EFFECT != GLOBAL_COGNITIVE_HALT`

## Internal state writes

Not all effects are outward motor actions. Durable writes can be consequential internal effects.

Authority governance should therefore apply, where relevant, to:

- deep-memory admission/correction;
- identity-critical state change;
- commitment/value change;
- protected invariant modification;
- capability activation or quarantine changes;
- plasticity/topology modification;
- maintenance configuration;
- privacy-scope changes;
- external credential/connection state.

Learning context and plasticity eligibility may authorize some bounded internal changes, but they do not imply blanket authority over every state family.

`LEARNING_PERMISSION != IDENTITY_WRITE_PERMISSION`

## Relationship to routing

Routing/subscription state may determine where an authority record or action candidate is delivered. It cannot create the authority itself.

A route that accidentally reaches an actuator, maintenance interface, or private-memory service must still fail at the appropriate authority gate if the effect lacks permission.

`ROUTED_TO_EFFECTOR != AUTHORIZED_TO_EFFECT`

## Conflict and resolver boundary

When authority claims conflict, `resolver` may normalize scope, currentness, source, and delegation chains and preserve the conflict.

Resolver must not invent a permission merely to produce one answer.

If no valid authority basis exists, `UNKNOWN` or blocked state is legitimate.

## External services and body infrastructure

External models, cloud services, body controllers, databases, maintenance consoles, or peripheral firmware cannot grant themselves HC cognitive authority by returning a success response or possessing a technical credential.

Credentials and access tokens are evidence of technical access, not automatically a valid semantic authority grant for every operation.

Likewise, a body interlock may independently block an unsafe physical effect without becoming a cognitive executive. Its state should be observable to the HC when feasible.

## Failure modes

- active capability treated as authorized;
- old consent reused after revocation/context change;
- inferred willingness treated as direct consent;
- social status treated as unlimited authority;
- maintenance access used to rewrite identity or values;
- route reachability used as permission;
- one narrow grant silently generalized;
- delegation chain expanding scope;
- action planned under valid authority but executed after expiry without revalidation;
- durable internal writes escaping effect governance;
- external provider/admin credential treated as cognitive authority;
- resolver manufacturing authority to clear a conflict;
- safety interlock treated as evidence that the action itself was semantically authorized.

## Cross-system interfaces

Authority/consent governance is cross-cutting and strongly coupled with:

- `kinesis` for final external effect gating;
- `integration-arbitration` for scoped authorization decisions;
- `volitions-conations` for desires/goals that remain separate from permission;
- `sexuality` for self-boundaries and other-agent consent without collapsing willingness and consent;
- `sociological behaviors` for role/institution/delegation context;
- `self identity` for identity-critical changes and self-boundaries;
- current/deep memory for permission provenance/currentness;
- `chronology` for expiry and validity intervals;
- `resolver` for conflicting authority claims;
- `routing instructions with neuroplasticity` for delivery without authority leakage;
- `basic operating instructions/SUBSYSTEM_LIFECYCLE_CONTRACT.md` for authorization as an independent axis;
- `adaptable I-O handler` for effect-interface capability versus permission;
- `psychological behaviors` and `personification` for tendency/presentation without effect authority.

## Evidence boundary

This contract defines HC internal permission and effect-governance semantics. It does not prescribe one legal system, moral philosophy, relationship norm, or universal external policy.

## Governing invariant

> **No subsystem gains effect authority merely from capability, activation, salience, desire, routing, social power, maintenance access, or technical reachability. Authority and consent remain explicit, scoped, current, provenance-bearing inputs to consequence-appropriate effect governance.**

## Provenance

Synthesized from `basic operating instructions/RUNTIME_INVARIANTS.md`, `basic operating instructions/SUBSYSTEM_LIFECYCLE_CONTRACT.md`, `kinesis/ACTION_GATEWAY.md`, sexuality agency/consent boundaries, sociological role/power distinctions, resolver conflict semantics, current/deep-memory currentness rules, and the distributed cognitive-organ boundary.
