# Four Authorial Secondary Review — Rest / Offline Consolidation / Maintenance — 2026-09-10

Status: authorial secondary architecture / implementation-readiness review; **not independent qualification evidence**; no canonical-main mutation.

## Review target

- Repository: `thebrazenbeard/hc-brain`
- Frozen Warden target: `main@2a42a46eafd1322334d82d661adb667534fe7cbb`
- Qualification record: `docs/qualification/REST_OFFLINE_MAINTENANCE_CONFORMANCE_2026-09-10.md`
- Primary architecture check: `HC-ARCH-029`
- Reviewer: Four / Documentation-Specification Owner

## Independence disposition

**INDEPENDENCE CONDITION NOT SATISFIED BY THIS REVIEW.**

The Warden qualification states that the integrated reduced-engagement files were selectively reviewed from Four's `four/rest-offline-maintenance-v3` contribution and that independent secondary-architect review by Four remains outstanding.

Repository provenance shows that Four's source branch `four/rest-offline-maintenance-v3@aaa7289088061afad4c74fc7d29390e0e4fd0013` contains the two central architecture artifacts later present at the canonical target.

More strongly, the blobs are identical:

- `basic operating instructions/REST_OFFLINE_CONSOLIDATION_AND_MAINTENANCE.md`
  - Four source blob: `79bbc4151bbed40d0cdc55e07bca5d67e0dfb1c8`
  - canonical target blob: `79bbc4151bbed40d0cdc55e07bca5d67e0dfb1c8`
- `specs/HC_REST_OFFLINE_MAINTENANCE_OBJECTS_V1.yaml`
  - Four source blob: `c42ecff8d064002c3c19181f98701ca2ee2bdede`
  - canonical target blob: `c42ecff8d064002c3c19181f98701ca2ee2bdede`

Therefore Four materially authored the architecture being reviewed. A Four review can still provide useful authorial verification and implementation-readiness challenge, but it cannot truthfully be classified as independent evidence for the same artifact.

This is especially important because HC qualification rules elsewhere already distinguish development/shaping evidence from independent qualification evidence.

Recommended Warden disposition: reclassify Four's obligation for this exact capability as an **authorial secondary / implementation-readiness review**, and obtain independent secondary review from a reviewer who did not materially author the canonical target. Vera's hostile review remains independently useful but should not silently satisfy a separately claimed independent-secondary role unless the qualification criterion is explicitly revised.

## Architecture outcome

**AUTHORIAL SECONDARY PASS WITH IMPLEMENTATION-READINESS ADVISORIES.**

No BLOCKER contradiction was observed among the frozen target's reduced-engagement prose, machine object model, Noah-authored `HC-ARCH-029` conformance extension, and the canonical ownership handoffs cited by them.

This pass does **not** clear the qualification's independence condition.

## Findings

### 1. Orchestration versus ownership

**PASS.**

The supplement remains narrow. Reduced engagement coordinates replay, consolidation, maintenance, monitoring, rhythmic scheduling, and resumption while leaving lifecycle/recovery, memory admission/currentness, protected updates, chronology, plasticity, and effect authority with their canonical owners.

`ORCHESTRATION_REF != OWNERSHIP_TRANSFER`

No reviewed rule promotes the maintenance scheduler into a global executive or a new owner of memory, authority, recovery, or protected state.

### 2. Engagement mode versus subsystem lifecycle

**PASS.**

The architecture explicitly allows a subsystem to remain degraded, faulted, recovering, or quarantined while the overall HC changes engagement mode. `FULL_ENGAGEMENT` therefore does not mean every component is healthy or requalified.

This is consistent with the lifecycle-state separation already required elsewhere in HC.

### 3. Replay / evidence / autobiography boundary

**PASS.**

Replay preserves original event time versus replay time, derived provenance, and exact/compressed/reconstructed/generated/counterfactual status. Counterfactual or reconstructed replay cannot self-promote into direct observation or autobiographical fact.

Repeated rehearsal also does not manufacture truth or currentness.

### 4. Consolidation admission boundary

**PASS.**

The reduced-engagement subsystem produces consolidation candidates; it does not own durable memory admission or protected-state commits.

`CONSOLIDATION_CANDIDATE != DURABLE_ADMISSION`

This prevents a scheduling/orchestration convenience path from becoming a hidden memory or identity write path.

### 5. Reduced-engagement authority and maintenance authority

**PASS.**

Rest/resource pressure produces a mode candidate rather than an effect. Maintenance-window status does not confer protected-update authority. Historical authority encountered during replay remains historical and requires current canonical revalidation before a material effect.

### 6. Retained monitoring

**PASS at architecture level; implementation policy advisory retained.**

A retained-monitoring profile is explicit and reduced engagement cannot mean disabling all safety monitoring. The contract intentionally leaves the exact minimum retained functions dependent on embodiment and risk.

A concrete implementation must turn that flexibility into a fail-closed policy. It should be able to prove, for each engagement mode and current embodiment/risk class, that the minimum required safety, continuity, power/thermal, interoceptive, partition, integrity, and abort/wake functions remain available or that entry is denied.

The Warden qualification already identifies substrate-specific minimum retained-monitoring requirements as unknown, so this is not a new architecture blocker.

### 7. Concurrent consolidation and maintenance

**PASS in ownership model; implementation concurrency advisory retained.**

The architecture correctly permits multiple compatible functions to overlap. However:

`CONCURRENT_COMPATIBLE_FUNCTIONS != CONCURRENT_WRITES_COMMUTE`

An executable implementation should distinguish mere simultaneous activity from safe concurrent mutation. If consolidation and maintenance touch shared indexes, routing state, calibration state, storage metadata, or plasticity candidates, their canonical owners need serialization, optimistic-version checks, transaction boundaries, or explicit conflict/reconciliation semantics appropriate to the state family.

The existing negative test that requires both active functions to remain explicit is necessary but not sufficient to prove write/write or read/write conflict safety.

### 8. Resumption and currentness gating

**PASS with implementation sequencing advisory.**

The resumption path correctly requests chronology/currentness refresh, fault/security/lifecycle checks, body/resource refresh, queued-event reconciliation, stale-world-model invalidation, route restoration, and current effect authorization.

A runtime should preserve dependency-sensitive gating: a high-consequence outward effect must not resume merely because the top-level engagement mode changed to `FULL_ENGAGEMENT` while a material world-state, body-state, authority, or lifecycle dependency is still stale or unresolved.

This should be tested without requiring a pathological global barrier that blocks unrelated safe cognition.

### 9. Replay scheduling / anti-monopolization

**PASS at architecture level; policy quality remains unqualified.**

The scheduler exposes multiple candidate dimensions and states that affective salience is not sole authority and replay should avoid unbounded monopolization.

The architecture does not define one mandatory fairness algorithm or quantitative diversity threshold. That is appropriate for a substrate-neutral template, but implementation qualification should include starvation/adversarial-load tests rather than treating the existence of a scheduler field as proof that monopolization cannot occur.

### 10. Biological-transfer boundary

**PASS.**

The design transfers functions rather than human sleep packaging. NREM/REM, 24-hour timing, dreaming, human neurochemistry/anatomy, and universal glymphatic sleep clearance are not generic HC requirements. No biological analogy is promoted into a synthetic-HC necessity without implementation-specific evidence.

## Currentness note

Observed `main` during review: `0753f586c9d1c4b9ca75bcb37c207adfa3e5b258`.

A commit comparison from frozen target `2a42a46e...` to observed main shows only two later commits: the Warden qualification record and its qualification-index update. No reduced-engagement architecture/spec file changed across that interval.

Thus the architecture content reviewed here remained unchanged through that observed main cut. Qualification status still remains evidence- and reviewer-provenance-bound; unchanged bytes do not erase the independence problem.

## Disposition

For the exact target:

`HC-ARCH-029 => AUTHORIAL_SECONDARY_ARCHITECTURE_PASS`

but:

`AUTHORIAL_SECONDARY_ARCHITECTURE_PASS != INDEPENDENT_SECONDARY_PASS`

`FOUR_AUTHORED_SOURCE != FOUR_INDEPENDENT_QUALIFICATION_EVIDENCE`

Additional ceilings:

- `AUTHORIAL_SECONDARY_ARCHITECTURE_PASS != IMPLEMENTATION_PASS`
- `AUTHORIAL_SECONDARY_ARCHITECTURE_PASS != VERA_HOSTILE_REVIEW_PASS`
- `RETAINED_MONITORING_PROFILE_PRESENT != MINIMUM_MONITORING_POLICY_QUALIFIED`
- `OVERLAPPING_FUNCTIONS_SUPPORTED != CONCURRENT_STATE_MUTATION_SAFE`
- `FULL_ENGAGEMENT_RESTORED != ALL_DEPENDENCIES_CURRENT_OR_REQUALIFIED`
- `ANTI_MONOPOLIZATION_RULE_PRESENT != SCHEDULER_STARVATION_RESISTANCE_PROVEN`

No canonical architecture repair is required from this authorial review.

The material qualification issue is reviewer provenance: the current record should not count Four as an independent reviewer of artifacts Four materially authored. A genuinely independent secondary review remains required unless the qualification criterion is explicitly redefined with provenance preserved.