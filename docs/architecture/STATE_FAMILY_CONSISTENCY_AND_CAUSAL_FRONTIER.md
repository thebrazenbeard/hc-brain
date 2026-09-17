# State-Family Consistency and Causal Frontier

Status: DESIGN CANDIDATE / NOT CANONICAL / NOT QUALIFIED

## Purpose

A distributed Hyperconnectome Brain cannot safely answer every partition, replica, write, and merge question with one global consistency model. Authority state, continuity-bearing memory, append-only evidence, effect receipts, telemetry, and temporary coalition scratch state have different semantic costs when they diverge.

The architecture therefore requires each material distributed state family to declare its own consistency and partition contract.

`DISTRIBUTED != EVENTUALLY_CONSISTENT_BY_DEFAULT`

`AVAILABLE_DURING_PARTITION != AUTHORIZED_TO_WRITE_PROTECTED_STATE`

`REPLICA_REACHABLE != REPLICA_CURRENT`

`LATER_WALL_CLOCK != CAUSAL_SUCCESSOR`

## State-family profile

A material state family should be able to expose a profile equivalent to:

```text
STATE_FAMILY_CONSISTENCY_PROFILE {
  family_id
  semantic_owner
  consistency_class
  protected
  continuity_bearing
  partition_write_policy
  partition_read_policy
  merge_or_reconciliation_rule
  stale_state_policy
  recovery_fence_policy
  effect_dependency_policy
  qualification_refs[]
  provenance
}
```

The machine-readable companion is `specs/HC_STATE_FAMILY_CONSISTENCY_POLICY_V1.yaml`.

## Consistency classes are semantic contracts

The allowed class vocabulary describes the guarantees a family needs, not the implementation technology used to provide them.

### `SINGLE_WRITER_EPOCH`

One active writer lineage is authoritative inside a current epoch/generation. A stale writer cannot become current merely because it remained reachable.

Useful for state where split-brain writers would be more dangerous than temporary unavailability.

### `QUORUM_COMMITTED`

A material write becomes committed only after the implementation-specific quorum condition is satisfied. The architecture does not prescribe majority quorum, witness layout, or one consensus protocol.

### `LINEARIZABLE_REQUIRED`

Operations in the declared scope must behave as if there were one real-time-respecting total order. This is intentionally expensive and should not become the default for unrelated cognitive state.

### `CAUSALLY_ORDERED`

The system preserves dependency ordering without asserting one total order for independent concurrent events.

### `MERGEABLE_CONCURRENT`

Concurrent candidates may be admitted during partition only when the state family has an explicit merge/reconciliation rule that preserves conflicts and provenance where required.

### `LOCAL_EPHEMERAL`

State is intentionally local and disposable at the end of its declared request/task/coalition/session scope. It must not silently become durable continuity or authority state.

### `READ_ONLY_REPLICA`

A replica may serve observations within declared staleness/currentness rules but cannot originate writes for the family.

## Partition write policies

`BLOCK` means no state-family write is admitted while the required consistency/currentness condition cannot be established.

`BOUNDED_ISLAND` permits local writes only inside an explicitly predeclared island envelope. The records remain island-scoped until rejoin/reconciliation and cannot silently claim global currentness.

`MERGE_CANDIDATES_ONLY` permits partition-local candidate production but not automatic promotion into one current head. Reconciliation is mandatory.

`READ_ONLY` permits no writes.

These are semantic policy classes. A concrete implementation may use leases, epochs, consensus, quorum, CRDT-like structures, deterministic merge, designated continuity cores, or another mechanism if the observed guarantees match the declared policy.

## Partition read policies

`CURRENT_ONLY` fails closed if the implementation cannot justify currentness for the requested scope.

`LOCAL_ALLOWED` permits local state where the family contract says locality is the intended scope.

`STALE_WITH_LABEL` permits explicitly stale data when consumers receive enough metadata to avoid promoting it into current state.

`READ_ONLY` describes a family whose serving replicas cannot mutate the family.

## Causal frontier

Wall-clock metadata remains useful for chronology, latency, expiry, and observation timing, but it does not establish semantic succession under replay, clock skew, partition, or independent concurrency.

Where ordering materially changes authority, continuity, protected state, effect eligibility, or reconciliation, a state family should carry enough causal metadata to reconstruct its relevant predecessor relation.

A generic form is:

```text
CAUSAL_FRONTIER {
  epoch
  predecessor_ids[]
  local_sequence_or_generation
  observed_clock_metadata
}
```

This is a semantic minimum, not a mandatory wire format. A single-writer state may need only `(epoch, generation)`. A concurrent mergeable family may need a richer predecessor set or equivalent vector/dotted-version representation.

Crucially:

`CAUSALLY_LATER != MORE_TRUE`

`CAUSALLY_LATER != MORE_AUTHORIZED`

`CAUSALLY_LATER != MORE_IDENTITY_RELEVANT`

Causality says what depends on what. Epistemic support, authority, consent, salience, identity relevance, and quality remain separate axes.

## Protected and continuity-bearing families

A protected or continuity-bearing family may not omit its recovery-fence policy.

Examples of questions the policy must answer:

- What invalidates a pre-restart writer?
- How is a previous epoch fenced?
- Can a partitioned replica write candidates, or only read?
- What evidence is required before rejoin?
- How are concurrent candidates preserved?
- Does an effect depending on this state require revalidation after epoch/partition change?

`READABLE_AFTER_RESTART != CURRENT_AFTER_RESTART`

`REJOINED_NETWORK != RECONCILED_STATE`

## Examples without canonicalizing one implementation

Authority state might reasonably choose a strong single-writer/epoch or quorum-committed policy because a split-brain authority writer is dangerous.

Append-only evidence could permit causally ordered multi-writer admission if producer identity, lineage, duplicate handling, and later projection rules preserve conflict.

Telemetry may permit stale labeled reads or bounded local writes because temporary divergence is not itself authority or continuity corruption.

Coalition scratch state may be local ephemeral and discarded at restart.

These are examples of appropriate policy *shape*, not canonical profile assignments. Concrete HC generations/implementations must qualify the choices they actually make.

## Hostile controls

A valid conformance suite should reject at least:

- a protected family with no declared partition write policy;
- a continuity-bearing family with no recovery-fence policy;
- a mergeable family with no reconciliation rule;
- a currentness selector that uses newest wall-clock timestamp alone;
- a partitioned fragment that continues global protected writes merely because it has local technical capability;
- a temporary local state family relabeled as durable memory because it survived in RAM;
- a single global consistency flag that erases materially different state-family semantics;
- causal order promoted into truth, consent, authority, or identity.

## Relationship to temporal hypergraph execution

The temporal hypergraph remains the cognitive representation. State-family consistency profiles govern durability/currentness/reconciliation semantics of state that may be distributed across HC-owned constituents. They do not turn every cognitive relation into a database transaction.

A temporary hyperedge may remain purely execution-local. A durable plasticity change, authority grant, continuity-bearing memory record, or effect receipt has stronger custody requirements because its consequences survive the transient coalition that produced it.

## Evidence boundary

This contract is an architectural hardening proposal. It does not establish that one specific distributed implementation satisfies any listed consistency class, nor does it prove the physical feasibility of a distributed HC cognitive organ.
