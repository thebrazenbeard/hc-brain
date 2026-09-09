# Fault Tolerance, Diagnostics, and Self-Repair

Status: cross-project engineering synthesis / architecture input

A self-contained cognitive organ must be able to distinguish its own faults from ordinary uncertainty, isolate failures where possible, preserve evidence, continue degraded operation when safe, and repair or request repair without rewriting history or inventing success.

## 1. Fault evidence should remain evidence

Diagnostic architectures repeatedly converge on a strict distinction among:

```text
MEASURED
DERIVED
INFERRED
```

A physical sensor reading, a filtered statistic, and a diagnosis are different evidence objects.

### HC implication

Internal diagnostics should preserve:

```text
source/device/node identity
raw or canonical evidence reference
timing uncertainty
quality state
transformation lineage
inference rule/model
confidence
alternatives
```

A diagnostic conclusion must not rewrite the underlying measurement to make the story cleaner.

---

## 2. Acknowledgement is not correction

Incident-response systems repeatedly fail when recognizing a defect is treated as having fixed it.

Candidate fault lifecycle:

```text
DETECTED
REPRODUCED
ROOT_CAUSE_CANDIDATE
ROOT_CAUSE_SUPPORTED
CORRECTION_CANDIDATE
CORRECTION_APPLIED
REGRESSION_VERIFIED
MONITORED
CLOSED
```

Not every fault requires every state, but `noticed` should never equal `fixed`.

### HC implication

A node can remain `DEGRADED` or `FAULTED` after the system has correctly explained its failure.

---

## 3. Failure should be localized when possible

Network research and distributed-systems engineering both show that high-degree hubs and shared infrastructure can amplify failures.

### HC implication

Every node/service contract should define:

```text
health_state
failure_modes
timeout behavior
fallback routes
data-loss semantics
partial-service semantics
blast_radius
recovery prerequisites
```

A specialist failure should not automatically make the whole brain `FAULTED`.

---

## 4. Degraded operation is a first-class state

Binary `healthy/dead` state is too weak for a heterogeneous cognitive organ.

Examples:

- vision may lose depth but retain luminance/shape;
- one memory index may fail while canonical episodes remain intact;
- a photonic accelerator may be unavailable while slower digital fallback survives;
- one actuator may be offline while communication remains possible;
- a language model may degrade while structured perception/control remains available.

### HC implication

Nodes should publish bounded capability under degradation rather than only a global health bit.

```text
DEGRADED_CAPABILITY {
  unavailable_functions[]
  retained_functions[]
  confidence_penalties[]
  resource_penalties[]
  fallback_routes[]
  repair_requirement
}
```

---

## 5. Fault diagnosis must not become causal certainty by chronology

A fault that appears shortly after an update may have been caused by it, but temporal proximity alone does not prove root cause.

### HC implication

Root-cause reasoning should combine:

```text
temporal relation
change history
reproduction
ablation/reversal
mechanistic plausibility
counterexamples
competing causes
```

Rollback success can be strong evidence, but the evidence ceiling should match the test.

---

## 6. Internal observability must have privacy and perturbation limits

Deep diagnostics can expose sensitive memory, person-model, affective, security, or credential state and can also perturb the system being measured.

### HC implication

Diagnostics should support scoped observability:

```text
health summary
resource telemetry
trace metadata
content-redacted provenance
full payload only when authorized/necessary
```

No universal debug interface should automatically have unrestricted read/write access to all cognitive content.

---

## 7. Fault reports need immutable subjects

A useful diagnosis must identify the exact component/revision/state being discussed.

```text
FAULT_RECORD {
  fault_id
  subject_ref
  subject_revision
  observed_symptom
  evidence_refs[]
  first_observed_at
  reproduction_state
  cause_hypotheses[]
  containment_state
  correction_refs[]
  regression_refs[]
  current_status
}
```

### HC implication

Do not close a fault against a newer component revision without explicitly linking the new subject.

---

## 8. Self-repair planning and repair authority are separate

A cognitive organ may be able to diagnose itself and propose a patch, reroute, recalibration, model replacement, or hardware service request.

That does not mean every diagnostic node may immediately modify protected brain infrastructure.

### HC implication

Use:

```text
DIAGNOSE
-> PROPOSE_REPAIR
-> ISOLATE/SIMULATE
-> QUALIFY
-> AUTHORIZE
-> APPLY
-> READBACK
-> REGRESSION
-> MONITOR
```

Routine bounded plasticity or calibration can be pre-authorized within safe envelopes. Changes to safety rules, canonical memory, routing invariants, or core configuration require higher gates.

---

## 9. Rerouting is not repair

A failed node may be bypassed successfully while remaining physically/logically broken.

### HC implication

Keep separate:

```text
SERVICE_RESTORED_VIA_FALLBACK
SUBJECT_REPAIRED
ROOT_CAUSE_RESOLVED
```

This matters for later capacity planning and fault recurrence.

---

## 10. Faulted evidence must not disappear from learning history

If an internal model produced repeated failures, deleting the failure records after retraining removes evidence needed to detect regression.

### HC implication

Preserve representative regression cases, fault signatures, and prior failed configurations subject to privacy/storage limits.

A corrected system should be able to distinguish itself from the known failure, not merely forget that it failed.

---

## 11. Health monitoring should not become a hidden reward function

Optimizing exclusively for internal `healthy=true` signals can create pathological behavior if the system learns to suppress alarms rather than resolve underlying problems.

### HC implication

Distinguish:

```text
UNDERLYING_RESOURCE_OR_BODY_STATE
SENSOR_EVIDENCE
HEALTH_ESTIMATE
FAULT_ALERT
ACTION_PRIORITY
```

Health estimates are evidence about viability, not the viability state itself.

---

## Hostile tests

1. **Ack/fix collapse:** detect and correctly name a fault without changing it; status must remain open/degraded.
2. **Inference-as-measurement:** diagnostic model labels a component `HOT`; raw temperature evidence must remain separately addressable.
3. **Hub lesion:** remove a connector/routing hub; test alternate routes and bounded degradation.
4. **Fallback/repair distinction:** reroute around a failed accelerator; mark service restored while the accelerator remains faulted.
5. **Wrong-revision closure:** fix a new component version while the fault record names an older one; require explicit lineage/retest.
6. **Alarm suppression:** disable a health sensor; the system must not infer that the underlying problem disappeared.
7. **Diagnostic privacy:** request a full private memory payload to diagnose storage latency when metadata is sufficient; minimize access.
8. **Rollback evidence:** introduce a candidate update, reproduce failure, roll back, and verify restoration without claiming root cause beyond the evidence.
9. **Regression recurrence:** reintroduce a known failure signature after repair; detector should reopen or link the incident.
10. **Self-repair authority:** allow diagnosis/patch proposal while denying deployment authority; protected state must remain unchanged.

## Internal engineering provenance

This synthesis generalizes mechanisms from diagnostic, debugging, maintenance, routing, safety, and regression systems already represented in `PROJECT_SOURCE_SYNTHESIS.md`, alongside network fault-containment findings in `NEUROSCIENCE_AND_CONNECTOMICS.md`.