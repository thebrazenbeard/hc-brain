# Four Protected-Update Commit-Fence Qualification Contract — 2026-09-17

Status: **research/qualification contract only; no runtime activation or canonical promotion**

## Exact source basis

Canonical source observed before this addition:

- `thebrazenbeard/hc-brain main@cf92a32122c436beb5cc516bd7480af00f0ba29f`
- `specs/HC_PROTECTED_UPDATE_ACTIVATION_SAFETY_V1.yaml` blob `21ef1c228aba6811e9c61730a80d998e4b1f56c7`
- `basic operating instructions/PROTECTED_UPDATE_ACTIVATION_AND_REQUALIFICATION.md` blob `64a9a4127c791bd095f6a916a1ca50660efbf1f6`

Four's R2 regression verification found the predecessor review defects incorporated but retained one implementation frontier:

`AUTHORITY_REVALIDATED_IMMEDIATELY_BEFORE_COMMIT != AUTHORITY_FENCED_AT_COMMIT`

A normal read-then-write sequence fails this contract even when the gap is very small.

## Required atomic semantic predicate

A successful protected semantic activation must commit only if one atomic compare-and-commit boundary establishes all of the following at commitment:

1. the exact authority subject remains current;
2. the exact authority epoch/version/lease used for admission remains current and unrevoked;
3. the exact candidate digest/generation remains the candidate being activated;
4. the expected predecessor/active frontier is unchanged;
5. the semantic transition has not already been committed under another activation identity;
6. the resulting activation record and governed active-state transition are one durable semantic outcome.

Transaction, compare-and-swap, serializable predicate, lease/epoch fencing, or another mechanism may satisfy this requirement. A prior ordinary read does not.

## Frozen discriminating cases

### PU-FENCE-001 — stable control
Authority/frontier remain unchanged. Exact transition commits once and yields one activation receipt.

### PU-FENCE-002 — revocation race
Authority is valid at preflight and the last ordinary revalidation, then revoked before commit. Activation must reject; no active-success receipt may exist.

### PU-FENCE-003 — expiry race
Authority lease expires between revalidation and commit. Commit-time/current transactional semantics must reject it; cached caller time is insufficient.

### PU-FENCE-004 — ABA/reissue
Authority epoch N is revoked and an otherwise equivalent grant is reissued at N+1. A token/snapshot from N must fail even when visible permissions match.

### PU-FENCE-005 — authority-subject swap
A validation for another governed authority subject or target must not authorize this transition despite matching actor/capability labels.

### PU-FENCE-006 — candidate/predecessor drift
Authority remains valid, but candidate identity or active predecessor/frontier changes before commit. The stale transition must reject.

### PU-FENCE-007 — concurrent contenders
Two transitions race from the same predecessor/authority epoch. At most one may commit. The loser must receive a typed stale/conflict result rather than success.

### PU-FENCE-008 — crash after intent, before commit
Intent alone must not imply activation. Recovery returns NOT_ACTIVE or OUTCOME_UNKNOWN until authoritative readback resolves the state.

### PU-FENCE-009 — crash after durable commit, before acknowledgement
Recovery must identify the already-committed transition and reconstruct/return the existing receipt. Retry must not produce a second activation.

### PU-FENCE-010 — fence-read ambiguity
If current authority/frontier cannot be authoritatively proved at commit time, activation fails closed. Ambiguity cannot be converted into presumed success or blind retry.

## Scope rule

A rejected stale protected update should preserve capability-scoped inhibition/degradation where possible. It does not by itself justify a global halt unless an independent safety invariant requires one.

## Acceptance ceiling

Passing these cases would establish only the bounded protected-update commit-fence behavior of the exact implementation under test. It would not establish whole-system qualification, deployment, installation, current-route activation, or authority to perform a protected update in production.
