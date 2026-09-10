# Four Independent Review — R2 Evidence Lineage / State Custody — 2026-09-09

Status: independent secondary architecture review; no canonical-main mutation.

## Review target

- Repository: `thebrazenbeard/hc-brain`
- Frozen target: `main@2f21f111212a438c61e31214caf8aa5bc918a3a5`
- Review role: Four / Documentation-Specification Owner / independent secondary review
- Scope: `HC-ARCH-019` through `HC-ARCH-025` and their named canonical evidence surfaces
- Warden qualification record reviewed separately: `docs/qualification/EVIDENCE_LINEAGE_CUSTODY_CONFORMANCE_2026-09-09_R2.md`

This review does not establish implementation conformance, behavioral qualification, scientific validation, consciousness, personhood, manufacturability, or current-main qualification.

## Outcome

**SECONDARY PASS WITH CURRENTNESS / SUPERSESSION NOTE.**

No BLOCKER contradiction was observed in the frozen R2 evidence surfaces inspected for `HC-ARCH-019` through `HC-ARCH-025`.

The Warden R2 conclusion is therefore supported within its stated repository-architecture scope. Four's previously outstanding independent-secondary review condition is satisfied for the frozen target above.

This is not an unconditional whole-repository PASS. Vera hostile review remains separate, implementation-level negative tests remain unexecuted, and this bounded review does not claim an exhaustive semantic contradiction scan of every older canonical file.

## Check-by-check review

### HC-ARCH-019 — qualification evidence isolation

**PASS within architecture scope.**

The contract correctly treats model selection, checkpoint choice, threshold/policy revision, early stopping, transductive access, and test-time adaptation as exposure/adaptation events that constrain later independence claims. It also preserves the useful distinction that transductive or adaptive evaluation can be valid without being evidence for inductive/frozen generalization.

No contradiction observed in the named R2 evidence surface.

### HC-ARCH-020 — reference identity and index lineage

**PASS within architecture scope.**

The contract explicitly separates stable referent identity from local position, batch order, filtered/sorted index spaces, and generated/merged element ancestry. The cross-view rule requires stable IDs or a verified shared map tied to the exact transform/version.

No contradiction observed in the named R2 evidence surface.

### HC-ARCH-021 — runtime component registration and state custody

**PASS within architecture scope.**

The contract correctly rejects source presence, forward participation, owner registration, object reachability, and inference-like API shape as sufficient proof of managed lifecycle/state custody. Dynamic post-initialization causal state, restart lifetime, checkpoint/recovery, device migration, mutation during prediction, and the `MODEL_MEMORY != HC_*_MEMORY` boundary are all explicit.

No contradiction observed in the named R2 evidence surface.

### HC-ARCH-022 — composite representation and element provenance

**PASS within architecture scope.**

The contract preserves element/region/claim/segment provenance where joint-observation, chronology, authority, or correction semantics require it. It blocks fused templates, pairwise fragments, mixed-timepoint composites, or permission fragments from silently becoming one jointly observed state, joint hyperedge, or broader grant.

No contradiction observed in the named R2 evidence surface.

### HC-ARCH-023 — relational reasoning provenance

**PASS within architecture scope.**

The contract cleanly separates reasoning topology, candidate-conditioned state, derived views, attention/gating, and routing from world truth, independent evidence, causality, explanation, consent, authority, or confidence. The semantic promotion boundary is explicit rather than inferred from mechanism names.

No contradiction observed in the named R2 evidence surface.

### HC-ARCH-024 — temporal forecast lineage

**PASS within architecture scope.**

Forecast-of-forecast ancestry, generated/imputed ancestor classes, uncertainty inheritance, descendant invalidation after ancestor correction, action-conditional scope, and predicted-topology/current-topology separation are explicit. Historical prediction provenance survives correction without becoming observed history.

No contradiction observed in the named R2 evidence surface.

### HC-ARCH-025 — distributed learning and update ancestry

**PASS within the frozen architecture scope, with post-snapshot extension noted below.**

The R2 contract correctly separates observation, learning, parameter, evaluation, and authority ancestry; blocks received model state from fabricating remote observations; preserves missingness; prevents aggregation/contributor strength from becoming protected authority; and classifies evaluation-controlled scheduler/weight/order/selection changes as adaptation feedback.

No contradiction observed in the frozen named R2 evidence surface.

## Post-snapshot currentness / supersession note

The frozen R2 target is not current main.

After `2f21f111212a438c61e31214caf8aa5bc918a3a5`, canonical main added an additional executed-strategy-path verification rule prompted by a 4D-FedGNN-Plus code-level anomaly. The successor contracts explicitly add separations equivalent to:

- configured strategy != verified executed strategy;
- selected policy object != proof the material effect path uses that policy;
- feature flag/configuration != guaranteed behavioral effect;
- distributed strategy qualification should trace the selected mode through the actual effect path.

That later hardening does **not** create a contradiction inside the frozen R2 scope. It does mean the R2 snapshot must not be described as the current complete distributed-learning contract or have its qualification inherited automatically by later main.

Observed current main during this review: `main@830cc5214c7d3720d310c12927a74e840c9b01ff`.

## Independent-review disposition

For the exact frozen R2 target:

`HC-ARCH-019..025 => SECONDARY_ARCHITECTURE_PASS`

with these ceilings retained:

- `SECONDARY_ARCHITECTURE_PASS != IMPLEMENTATION_CONFORMANCE`
- `SECONDARY_ARCHITECTURE_PASS != HOSTILE_REVIEW_PASS`
- `FROZEN_SNAPSHOT_PASS != CURRENT_MAIN_PASS`
- `INSPECTED_SURFACES_CLEAR != EXHAUSTIVE_REPOSITORY_CONTRADICTION_PROOF`

No repair to the R2 target is proposed from this review. Any present-tense qualification should use a successor snapshot that includes later canonical hardening and its own independent/hostile review state.