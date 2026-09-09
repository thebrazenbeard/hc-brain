# Fault Diagnosis, Repair, and Partition-Safety Supplement

Status: template operating architecture.

## Purpose

A complete Hyperconnectome Brain needs a durable way to detect internal faults, preserve evidence, form competing cause hypotheses, describe bounded capability loss, contain dangerous local failures, propose repair, distinguish repair application from verification, retain regression evidence, and represent internal network partitions.

This supplement owns those **fault/repair evidence semantics**.

It does not redefine the canonical startup/recovery sequence, generic safe-degradation policy, subsystem lifecycle axes, protected-update activation, memory-currentness rules, or authority/effect governance.

Canonical dependencies include:

- `BOOTSTRAP_RECOVERY_AND_SAFE_DEGRADATION.md` and `HC_BOOTSTRAP_RECOVERY_V1.yaml`;
- `SUBSYSTEM_LIFECYCLE_CONTRACT.md`;
- `AUTHORITY_CONSENT_AND_EFFECT_GOVERNANCE.md`;
- `HC_PROTECTED_UPDATE_GOVERNANCE_V1.yaml`;
- canonical memory/currentness and resolver contracts.

## Core separations

`FAULT_DETECTED != ROOT_CAUSE_KNOWN`

`FAULT_ACKNOWLEDGED != FAULT_CORRECTED`

`SERVICE_RESTORED_VIA_FALLBACK != SUBJECT_REPAIRED`

`CORRECTION_APPLIED != CORRECTION_VERIFIED`

`REPAIR_RECEIPT != REPAIR_VERIFICATION`

`REPAIR_VERIFIED != FULL_REQUALIFICATION`

`ALARM_SUPPRESSED != UNDERLYING_FAULT_RESOLVED`

`DIAGNOSTIC_INFERENCE != MEASUREMENT`

`REPAIR_PLAN != REPAIR_AUTHORIZATION`

`CURRENTLY_REACHABLE != HEALTHY`

`PARTITIONED_HC_CONSTITUENT != EXTERNAL_PERIPHERAL`

## Exact fault subject

Every material fault should bind to an exact subject rather than a vague subsystem label.

A fault subject may be a constituent, service, interconnect, model/revision, memory structure, sensor/actuator interface, calibration state, routing configuration, plasticity state, resource domain, or physically distributed HC component.

A repair applied to a successor revision does not silently close a fault recorded against an earlier subject revision. Lineage and retest remain explicit.

## Fault record

A fault record should preserve where material:

- fault identity;
- exact subject and revision;
- first-observed time;
- observed symptom;
- raw/derived/inferred evidence;
- reproduction state;
- competing cause hypotheses;
- blast-radius estimate;
- containment state;
- bounded degraded-capability profile;
- fallback/workaround refs;
- repair candidates;
- authority/effect refs;
- repair receipts;
- repair-verification refs;
- regression/requalification refs;
- current status/currentness;
- supersession/reopen lineage;
- provenance.

Fault history is append-oriented. Recovery does not rewrite the record to imply that the fault never happened.

## Diagnostic lifecycle

A useful nonmandatory sequence is:

`DETECTED -> TRIAGED -> REPRODUCED_OR_BOUNDED -> CAUSE_HYPOTHESES -> CONTAINED -> REPAIR_CANDIDATE -> QUALIFIED -> AUTHORIZED_IF_REQUIRED -> APPLIED -> EFFECT_RECEIPT -> VERIFIED_OR_NOT -> REGRESSION -> REQUALIFICATION_WHERE_REQUIRED -> MONITOR`

This is not a monotonic ladder. Immediate containment may precede diagnosis. Some faults cannot be reproduced. Some remain degraded indefinitely. Recurrence may reopen an earlier record.

Useful statuses include:

- `DETECTED`;
- `UNDER_INVESTIGATION`;
- `CONTAINED`;
- `DEGRADED_SERVICE`;
- `SERVICE_RESTORED_VIA_FALLBACK`;
- `REPAIR_PENDING`;
- `CORRECTION_APPLIED_UNVERIFIED`;
- `REPAIR_VERIFIED`;
- `REGRESSION_VERIFIED`;
- `REQUALIFICATION_PENDING`;
- `MONITORING`;
- `CLOSED`;
- `REOPENED`;
- `UNKNOWN`.

## Degraded capability profile

Canonical lifecycle health remains authoritative. This supplement adds a more detailed functional description of what a degraded system can still do.

A degraded-capability profile may include:

- retained functions;
- unavailable functions;
- confidence penalties;
- latency/throughput penalties;
- resource penalties;
- fallback routes;
- unavailable effect/authority scopes;
- affected dependents;
- repair prerequisites;
- expected duration;
- currentness/provenance.

`DEGRADED != ABSENT`

This profile informs canonical safe-degradation/recovery logic; it does not define another global recovery state machine.

## Failure containment

Containment should be local unless evidence shows wider consequence.

Possible actions include route isolation, node inhibition, capability downgrade, read-only fallback, redundant-path selection, workload migration, quarantine, rate limiting, resource throttling, and blocking a faulted protected writer.

Containment should record retained and sacrificed functions where material.

Containment capability does not create its own authority. Authority/effect references resolve to canonical governance.

A requested rollback also does not bypass canonical protected-update or continuity rules.

## Distributed HC partition safety

A complete HC may span multiple physical locations. Loss of an HC-internal interconnect is therefore an **internal organ partition**, not an ordinary cloud/provider outage.

`PHYSICALLY_UNREACHABLE != NO_LONGER_HC_OWNED`

A partition state should identify:

- affected constituents and links;
- reachable sets;
- retained local functions;
- prohibited writes/effects;
- continuity policy/epoch where applicable;
- reconciliation refs;
- currentness/provenance.

Useful states include:

- `FULLY_CONNECTED`;
- `DEGRADED_LINK`;
- `PARTITION_DETECTED`;
- `CONTINUITY_WRITES_RESTRICTED`;
- `ISLAND_MODE_BOUNDED`;
- `REJOIN_PENDING`;
- `RECONCILING`;
- `REJOINED`;
- `UNRESOLVED_SPLIT`.

A partitioned fragment may retain bounded sensing/regulation or other predeclared functions without thereby becoming an independently authoritative successor organism.

The architecture does not mandate one distributed-systems algorithm. Implementations may use leases/epochs, quorum/consensus, a designated continuity core, fail-closed protected writes, or mergeable-state-only island operation. The requirement is that each continuity-bearing protected state family have a declared policy compatible with canonical currentness/recovery rules.

Fork/rejoin identity and continuity semantics remain owned by canonical recovery/memory rules.

## Diagnostic evidence discipline

Diagnostics preserve:

`MEASURED != DERIVED != INFERRED`

A sensor measurement, a filtered trend, and a cause hypothesis are different objects.

Cause confidence should consider temporal relation, change history, reproduction, intervention/reversal where available, mechanistic plausibility, counterexamples, and competing causes.

Temporal proximity alone does not prove causation.

## Observability and privacy

Diagnosis should use the minimum information needed for the fault question.

Preferred surfaces include health summaries, resource telemetry, trace metadata, content-redacted provenance, and full cognitive payload only where specifically authorized and necessary.

`OBSERVABILITY != WRITE_AUTHORITY`

Diagnostic access does not imply authority over identity, autobiographical memory, values, consent, private person models, credentials, or protected governance state.

## Repair candidate

The HC may propose recalibration, rerouting, replacement, retraining, rollback, patching, hardware service, or another repair.

A repair candidate should bind:

- exact subject;
- proposed change;
- expected effect;
- evidence basis;
- risk/continuity impact;
- qualification evidence;
- authority/effect requirements;
- rollback or forward-repair plan where material;
- provenance.

`REPAIR_CANDIDATE != AUTHORIZED_REPAIR`

Protected or continuity-relevant repair hands off to canonical protected-update governance. Routine bounded calibration/repair may use a declared preauthorized envelope only where canon permits it.

## Repair receipt versus repair verification

Application and verification are separate objects.

A `RepairReceipt` records what was applied, to which exact subject, when, and under which authority/effect decision where required. It may legitimately exist while status remains `CORRECTION_APPLIED_UNVERIFIED`.

A later `RepairVerification` binds the exact receipt/subject to:

- verification method;
- evidence refs;
- verification status;
- verified revision/time where meaningful;
- uncertainty/contradictions;
- regression refs;
- claim ceiling;
- provenance.

`APPLIED != VERIFIED`

`VERIFIED != REQUALIFIED`

The repair receipt also does not override canonical update activation or qualification state.

## Verification modality

Verification must fit the repaired subject.

A software/configuration repair may support direct state readback. A thermal, optical, mechanical, electrical, calibration, biological/biohybrid, distributed, or other physical repair may instead require measurement, inspection, functional testing, redundant-path comparison, calibration testing, or another declared method.

`READBACK_AVAILABLE != READBACK_UNIVERSALLY_REQUIRED`

## Rerouting is not repair

A fallback may restore service while the original subject remains faulted.

Keep separate:

- service availability;
- subject health;
- root-cause status;
- repair status;
- recovery/requalification status.

`ALTERNATE_ROUTE_SUCCESS != ORIGINAL_FAULT_CLOSED`

## Regression and recurrence

Representative fault signatures and regression cases should remain available subject to privacy/storage policy.

After repair, regression should target the original failure and material adjacent failures. A recurring signature should reopen/link the earlier fault rather than create a provenance-free story.

## Health-signal firewall

A system must not learn that suppressing alarms is equivalent to becoming healthy.

Preserve:

`UNDERLYING_STATE != SENSOR_EVIDENCE != HEALTH_ESTIMATE != FAULT_ALERT != ACTION_PRIORITY`

Muting an alert or losing a sensor does not establish recovery.

## Canonical handoffs

Canonical bootstrap/recovery owns startup, minimum safe operating envelope, interrupted-operation recovery, and return-to-service requalification.

Canonical protected-update governance owns protected architecture/runtime/firmware/configuration activation, continuity-safe rollback/forward repair, and update qualification.

Canonical authority/effect governance owns repair/containment permission.

Canonical subsystem lifecycle owns presence/activation/health/maturity/implementation axes.

This supplement supplies fault evidence, cause hypotheses, repair receipts/verifications, bounded degradation detail, and partition state to those systems.

## Evidence boundary

This is an architecture contract for fault reasoning and repair evidence. It does not prove an implementation is self-healing, guarantee recovery from arbitrary physical destruction, or prescribe one redundancy, consensus, diagnostic, or repair technology.

## Machine contract

The machine-readable companion is:

`specs/HC_FAULT_REPAIR_OBJECTS_V1.yaml`.