# Protected Update Governance — 2026-09-10 R2

Status: QUALIFICATION EVIDENCE

Target architecture snapshot: `main@e2726a43337b79dc43616a5641b0f747fc44f3ed`

Predecessor: `PROTECTED_UPDATE_GOVERNANCE_2026-09-09.md`

Result: **CONDITIONAL PASS**

## Tested capability

Current architecture-level governance of protected architecture, trusted runtime/firmware/configuration and continuity-relevant updates, including later model-graph/meta-optimization hardening and the successor activation/requalification safety boundary.

This cut specifically tests whether protected change remains distinct from ordinary plasticity, technical reachability, artifact integrity, optimizer performance, installation, semantic activation, qualification, rollback, forward repair, memory/value/identity/consent authority, and mixed-version distributed execution.

## Evidence inspected

- `basic operating instructions/PROTECTED_INVARIANT_AND_UPDATE_GOVERNANCE.md`
- `basic operating instructions/MODEL_GRAPH_AND_META_OPTIMIZATION_BOUNDARY.md`
- `basic operating instructions/PROTECTED_UPDATE_ACTIVATION_AND_REQUALIFICATION.md`
- `basic operating instructions/AUTHORITY_CONSENT_AND_EFFECT_GOVERNANCE.md`
- `basic operating instructions/BOOTSTRAP_RECOVERY_AND_SAFE_DEGRADATION.md`
- `specs/HC_PROTECTED_UPDATE_GOVERNANCE_V1.yaml`
- `specs/HC_PROTECTED_UPDATE_ACTIVATION_SAFETY_V1.yaml`
- protected-update/core-governance assertions in `specs/HC_COGNITIVE_ORGAN_INVARIANTS_V1.yaml` and `specs/HC_CONFORMANCE_SUITE_V1.yaml`
- `docs/research/FOUR_PROTECTED_UPDATE_GOVERNANCE_INDEPENDENT_REVIEW_2026-09-10.md`

Four's review was independent evidence for the older frozen target it actually reviewed. Its findings were then used to shape this successor architecture, so those findings are **development/regression evidence**, not untouched independent qualification evidence for R2.

## Observed architecture evidence

PASS at the inspected architecture-contract level:

- ordinary plasticity cannot silently commit protected architecture changes;
- maintenance/emergency reachability does not create unrestricted protected-update authority;
- signature/integrity/source prestige does not create semantic safety, instance consent, or effect authority;
- system update authority does not imply memory, identity, value, consent, or private-scope rewrite authority;
- model graphs remain namespaced from HC cognitive topology;
- a meta-optimizer may propose updates but cannot widen its own protected authority or turn objective improvement into organism value authority;
- parameter similarity, clustering, synchronization, or shared optimization does not transfer identity, authority, or qualification;
- per-component local best checkpoints do not establish coherent whole-organ qualification;
- protected activation is semantically atomic or explicitly journaled, with incompatible version skew visible and bounded;
- commit-time authority is now explicitly distinct from a prior preflight authority result;
- a staged update whose authority expires or is revoked before semantic commit cannot activate under the stale grant;
- journaling alone is explicitly insufficient proof of mixed-version semantic safety;
- incompatible protected semantic versions cannot jointly influence a material effect absent an explicit compatibility envelope and activation epoch;
- technical activation and local self-test do not restore predecessor qualification or high-consequence effect authority by default;
- post-activation operation is capability/dependency scoped rather than requiring either full trust restoration or unnecessary global cognitive halt;
- rollback and forward repair are themselves governed state transitions and do not self-authorize by being technically available or labeled recovery;
- rollback that would erase valid post-activation continuity remains blocked absent explicit continuity governance.

No architecture-level contradiction was observed among the focused protected-update, authority, recovery, meta-optimization, and successor activation-safety surfaces inspected for this cut.

## Adversarial specification coverage

The existing protected-update machine contract carries `UPD-NEG-001` through `UPD-NEG-015`, including protected-state plasticity attacks, maintenance overreach, signed-but-unauthorized updates, consent reset, canary over-crediting, interrupted multi-component writes, unsafe rollback, recovery-provider authority, updater self-governance weakening, self-test over-crediting, shared meta-optimizer attacks, parameter-similarity laundering, optimizer self-permission modification, incoherent per-component checkpoint selection, and objective/value conflation.

The successor activation-safety companion adds `PUAS-NEG-001` through `PUAS-NEG-010`, covering:

- revocation or expiry between preflight and semantic activation commit;
- incompatible semantic versions during journaled rollout;
- technically active but not capability-qualified successors;
- predecessor trust/effect-authority inheritance by mere execution;
- rollback without current protected-state authority;
- forward repair attempting to bypass governance by being labeled recovery;
- continuity-destructive rollback;
- ambiguous semantic commit after crash;
- stale constituent rejoin with old version/authority cache.

These are **specified negative tests**, not executed implementation results.

## Failure / correction status

The predecessor qualification was materially superseded by later model-graph/meta-optimization architecture. Four independently identified that supersession and also identified implementation-readiness concerns at commit-time authority, mixed-version effect isolation, post-activation capability inhibition, and repair authority.

This R2 incorporates those concerns as explicit successor architecture. It does not rewrite the historical predecessor or relabel Four's older review as independent evidence for the repaired successor.

`OLD_TARGET_REVIEW != INDEPENDENT_SUCCESSOR_REVIEW`

`REVIEW_FINDING_USED_TO_SHAPE_SUCCESSOR != UNTOUCHED_SUCCESSOR_HOLDOUT`

## Why this is not PASS

No executable HC runtime currently demonstrates:

- revocation/expiry propagation with sufficient latency to block a semantic commit;
- mixed-version effect isolation during non-atomic distributed rollout;
- correct capability/dependency computation for post-activation inhibition;
- continuity-safe rollback or forward repair under real failure;
- stale constituent rejoin fencing;
- meta-optimizer/self-modification negative cases on an implemented update path.

Vera hostile review and a materially independent secondary review of this successor cut have not yet been incorporated.

Therefore the strongest justified result is **CONDITIONAL PASS**.

## Remaining uncertainty

UNKNOWN at this cut:

- concrete activation-journal durability and commit protocol;
- maximum safe authority-revocation propagation latency by effect class;
- implementation-specific compatibility rules for mixed protected semantic versions;
- correctness/completeness of capability dependency graphs used for post-update inhibition;
- practical repair/rollback behavior under power loss, partition, or constituent fault;
- secure implementation of update authority, signatures, roots of trust, and attestation;
- whether a concrete meta-optimizer can find unintended paths around declared state-class boundaries;
- independent/hostile successor-review findings;
- executable negative-test results.

## Qualification ceiling

`R2_ARCHITECTURE_CONDITIONAL_PASS != IMPLEMENTATION_PASS`

`R2_ARCHITECTURE_CONDITIONAL_PASS != BEHAVIORAL_PASS`

`SIGNED_OR_INTERNAL_UPDATE != AUTHORIZED_UPDATE`

`TECHNICALLY_ACTIVE != QUALIFIED_WITHIN_SCOPE`

`JOURNALED_TRANSITION != MIXED_VERSION_EFFECT_ISOLATION_PROVEN`

`RECOVERY_PATH_EXISTS != RECOVERY_ACTION_AUTHORIZED_OR_CONTINUITY_SAFE`

Later commits do not inherit this result automatically.
