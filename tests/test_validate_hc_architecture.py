from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

from tools.validate_hc_architecture import (
    validate_review_receipt,
    validate_state_family_profiles,
)


class StateFamilyConsistencyPolicyTests(unittest.TestCase):
    def _profile(self, **overrides):
        profile = {
            "family_id": "authority_state",
            "semantic_owner": "authority-governance",
            "consistency_class": "SINGLE_WRITER_EPOCH",
            "protected": True,
            "continuity_bearing": False,
            "partition_write_policy": "BLOCK",
            "partition_read_policy": "CURRENT_ONLY",
            "merge_or_reconciliation_rule": "NO_AUTOMATIC_MERGE",
            "stale_state_policy": "FAIL_CLOSED",
            "recovery_fence_policy": "EPOCH_REVALIDATION",
            "effect_dependency_policy": "REVALIDATE_BEFORE_EFFECT",
            "qualification_refs": ["specs/HC_BOOTSTRAP_RECOVERY_V1.yaml"],
            "provenance": ["test-fixture"],
            "safety_invariants": ["NO_SPLIT_BRAIN_AUTHORITY"],
            "coordination_basis": "COORDINATION_REQUIRED_TO_PRESERVE_AUTHORITY_INVARIANT",
            "mechanical_evidence_refs": ["runtime/reference_kernel/test_vera_adversarial_kernel_v2.py"],
        }
        profile.update(overrides)
        return profile

    def test_duplicate_family_id_is_rejected(self) -> None:
        document = {"profiles": [self._profile(), self._profile()]}
        errors = validate_state_family_profiles(document)
        self.assertTrue(any("duplicate family_id" in error for error in errors))

    def test_unknown_consistency_class_is_rejected(self) -> None:
        document = {"profiles": [self._profile(consistency_class="MAGIC")]}
        errors = validate_state_family_profiles(document)
        self.assertTrue(any("unknown consistency_class" in error for error in errors))

    def test_protected_family_cannot_omit_partition_write_policy(self) -> None:
        document = {"profiles": [self._profile(partition_write_policy="")]}
        errors = validate_state_family_profiles(document)
        self.assertTrue(any("partition_write_policy" in error for error in errors))

    def test_merge_candidates_requires_reconciliation_rule(self) -> None:
        document = {
            "profiles": [
                self._profile(
                    protected=False,
                    consistency_class="MERGEABLE_CONCURRENT",
                    partition_write_policy="MERGE_CANDIDATES_ONLY",
                    merge_or_reconciliation_rule="",
                )
            ]
        }
        errors = validate_state_family_profiles(document)
        self.assertTrue(any("reconciliation" in error.lower() for error in errors))

    def test_continuity_bearing_family_requires_recovery_fence_policy(self) -> None:
        document = {
            "profiles": [
                self._profile(
                    protected=False,
                    continuity_bearing=True,
                    recovery_fence_policy="",
                )
            ]
        }
        errors = validate_state_family_profiles(document)
        self.assertTrue(any("recovery_fence_policy" in error for error in errors))

    def test_profile_requires_explicit_safety_invariants(self) -> None:
        profile = self._profile()
        profile.pop("safety_invariants")
        errors = validate_state_family_profiles({"profiles": [profile]})
        self.assertTrue(any("safety_invariants" in error for error in errors))

    def test_profile_requires_coordination_basis(self) -> None:
        profile = self._profile(coordination_basis="")
        errors = validate_state_family_profiles({"profiles": [profile]})
        self.assertTrue(any("coordination_basis" in error for error in errors))

    def test_profile_requires_mechanical_evidence_refs(self) -> None:
        profile = self._profile()
        profile.pop("mechanical_evidence_refs")
        errors = validate_state_family_profiles({"profiles": [profile]})
        self.assertTrue(any("mechanical_evidence_refs" in error for error in errors))

    def test_distinct_strong_and_weak_profiles_can_coexist(self) -> None:
        document = {
            "profiles": [
                self._profile(),
                self._profile(
                    family_id="coalition_scratch",
                    semantic_owner="integration-arbitration",
                    consistency_class="LOCAL_EPHEMERAL",
                    protected=False,
                    partition_write_policy="BOUNDED_ISLAND",
                    partition_read_policy="LOCAL_ALLOWED",
                    merge_or_reconciliation_rule="DISCARD_ON_SCOPE_EXIT",
                    stale_state_policy="TTL_BOUNDED",
                    recovery_fence_policy="DISCARD_ON_RESTART",
                    effect_dependency_policy="NOT_EFFECT_AUTHORITY",
                    safety_invariants=["LOCAL_SCRATCH_NE_GLOBAL_AUTHORITY"],
                    coordination_basis="GLOBAL_COORDINATION_NOT_REQUIRED_WHILE_SCOPE_REMAINS_LOCAL_AND_NONAUTHORITATIVE",
                    mechanical_evidence_refs=["runtime/reference_kernel/test_hc_kernel.py"],
                ),
            ]
        }
        self.assertEqual(validate_state_family_profiles(document), [])

    def test_reference_kernel_state_family_registry_exists_and_validates(self) -> None:
        root = Path(__file__).resolve().parents[1]
        registry = json.loads(
            (root / "specs/HC_STATE_FAMILY_CONSISTENCY_REGISTRY_V1.yaml").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(validate_state_family_profiles(registry), [])


class ReviewReceiptTests(unittest.TestCase):
    TRUSTED_VERIFIERS = {"verifier:hc-independent-reviewer"}
    TRUSTED_POLICIES = {"policy:hc-exact-head-review-v1"}
    TRUSTED_ROOTS = {"trust-root:github-review-surface-v1"}

    def _receipt(self, **overrides):
        receipt = {
            "receipt_id": "review-001",
            "subject_repo": "thebrazenbeard/hc-brain",
            "subject_head": "a" * 40,
            "reviewed_scope": ["runtime/reference_kernel"],
            "reviewer_execution_subject": "worker:independent-01",
            "reviewer_role": "HOSTILE_OR_ADVERSARIAL_REVIEW",
            "independence_state": "INDEPENDENT_WITHIN_DECLARED_SCOPE",
            "authored_artifact_refs": [],
            "shaping_or_diagnostic_refs": [],
            "prior_adjudication_refs": [],
            "material_shaping_within_reviewed_scope": False,
            "admitted_context_refs": ["design:public-subject-only"],
            "verdict": "PASS",
            "evidence_refs": ["test-run:001"],
            "issued_at": "2026-09-17T12:00:00-04:00",
            "supersedes": [],
            "attestation_location": "OUT_OF_SUBJECT_TREE",
        }
        receipt.update(overrides)
        return receipt

    @staticmethod
    def _receipt_sha256(receipt) -> str:
        canonical = json.dumps(receipt, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        return hashlib.sha256(canonical.encode("utf-8")).hexdigest()

    def _observation(self, receipt, **overrides):
        observation = {
            "observed_location": "OUT_OF_SUBJECT_TREE",
            "surface_type": "PULL_REQUEST_REVIEW",
            "attestation_uri": "github://thebrazenbeard/hc-brain/pull/19/reviews/123",
            "attestation_sha256": self._receipt_sha256(receipt),
            "subject_repo": "thebrazenbeard/hc-brain",
            "subject_head": "a" * 40,
            "verifier_id": "verifier:hc-independent-reviewer",
            "verification_policy_id": "policy:hc-exact-head-review-v1",
            "trust_root_id": "trust-root:github-review-surface-v1",
            "observed_at": "2026-09-17T12:01:00-04:00",
        }
        observation.update(overrides)
        return observation

    def _validate(self, receipt, *, observation=None):
        if observation is None:
            observation = self._observation(receipt)
        return validate_review_receipt(
            receipt,
            expected_repo="thebrazenbeard/hc-brain",
            expected_head="a" * 40,
            attestation_observation=observation,
            trusted_verifier_ids=self.TRUSTED_VERIFIERS,
            trusted_policy_ids=self.TRUSTED_POLICIES,
            trusted_root_ids=self.TRUSTED_ROOTS,
        )

    def test_stale_subject_head_is_rejected(self) -> None:
        receipt = self._receipt(subject_head="b" * 40)
        errors = self._validate(receipt, observation=self._observation(receipt, subject_head="b" * 40))
        self.assertTrue(any("subject_head" in error for error in errors))

    def test_non_commit_subject_head_is_rejected_even_if_expected_matches(self) -> None:
        receipt = self._receipt(subject_head="not-a-commit")
        errors = validate_review_receipt(
            receipt,
            expected_repo="thebrazenbeard/hc-brain",
            expected_head="not-a-commit",
            attestation_observation=self._observation(receipt, subject_head="not-a-commit"),
            trusted_verifier_ids=self.TRUSTED_VERIFIERS,
            trusted_policy_ids=self.TRUSTED_POLICIES,
            trusted_root_ids=self.TRUSTED_ROOTS,
        )
        self.assertTrue(any("40-character hexadecimal" in error for error in errors))

    def test_empty_review_scope_is_rejected(self) -> None:
        receipt = self._receipt(reviewed_scope=[])
        errors = self._validate(receipt)
        self.assertTrue(any("reviewed_scope" in error for error in errors))

    def test_independent_claim_with_material_in_scope_shaping_is_rejected(self) -> None:
        receipt = self._receipt(
            shaping_or_diagnostic_refs=["finding:used-to-build-successor"],
            material_shaping_within_reviewed_scope=True,
        )
        errors = self._validate(receipt)
        self.assertTrue(any("independence" in error.lower() for error in errors))

    def test_unrelated_shaping_history_does_not_destroy_scoped_independence(self) -> None:
        receipt = self._receipt(
            shaping_or_diagnostic_refs=["unrelated-subsystem:old-work"],
            material_shaping_within_reviewed_scope=False,
        )
        self.assertEqual(self._validate(receipt), [])

    def test_exact_head_receipt_must_be_out_of_subject_tree(self) -> None:
        receipt = self._receipt(attestation_location="SUBJECT_TREE")
        errors = self._validate(receipt, observation=self._observation(receipt, observed_location="SUBJECT_TREE"))
        self.assertTrue(any("out of subject tree" in error.lower() for error in errors))

    def test_self_declared_location_cannot_override_observed_subject_tree_location(self) -> None:
        receipt = self._receipt(attestation_location="OUT_OF_SUBJECT_TREE")
        errors = self._validate(receipt, observation=self._observation(receipt, observed_location="SUBJECT_TREE"))
        self.assertTrue(any("observed attestation location" in error.lower() for error in errors))

    def test_observation_subject_head_must_match_expected_subject(self) -> None:
        receipt = self._receipt()
        errors = self._validate(receipt, observation=self._observation(receipt, subject_head="b" * 40))
        self.assertTrue(any("observation subject_head" in error for error in errors))

    def test_observation_subject_repo_must_match_expected_subject(self) -> None:
        receipt = self._receipt()
        errors = self._validate(receipt, observation=self._observation(receipt, subject_repo="attacker/other"))
        self.assertTrue(any("observation subject_repo" in error for error in errors))

    def test_attestation_digest_must_bind_exact_receipt(self) -> None:
        receipt = self._receipt()
        errors = self._validate(receipt, observation=self._observation(receipt, attestation_sha256="0" * 64))
        self.assertTrue(any("attestation_sha256" in error for error in errors))

    def test_attestation_digest_must_be_sha256_hex(self) -> None:
        receipt = self._receipt()
        errors = self._validate(receipt, observation=self._observation(receipt, attestation_sha256="not-a-digest"))
        self.assertTrue(any("64-character hexadecimal" in error for error in errors))

    def test_untrusted_verifier_is_rejected(self) -> None:
        receipt = self._receipt()
        errors = self._validate(receipt, observation=self._observation(receipt, verifier_id="verifier:unknown"))
        self.assertTrue(any("verifier_id is not trusted" in error for error in errors))

    def test_untrusted_verification_policy_is_rejected(self) -> None:
        receipt = self._receipt()
        errors = self._validate(receipt, observation=self._observation(receipt, verification_policy_id="policy:unknown"))
        self.assertTrue(any("verification_policy_id is not trusted" in error for error in errors))

    def test_untrusted_root_is_rejected(self) -> None:
        receipt = self._receipt()
        errors = self._validate(receipt, observation=self._observation(receipt, trust_root_id="trust-root:unknown"))
        self.assertTrue(any("trust_root_id is not trusted" in error for error in errors))

    def test_missing_attestation_locator_is_rejected(self) -> None:
        receipt = self._receipt()
        errors = self._validate(receipt, observation=self._observation(receipt, attestation_uri=""))
        self.assertTrue(any("attestation_uri" in error for error in errors))

    def test_unknown_verdict_is_rejected(self) -> None:
        receipt = self._receipt(verdict="SUPER_PASS")
        errors = self._validate(receipt)
        self.assertTrue(any("verdict" in error for error in errors))

    def test_receipt_cannot_grant_merge_authority(self) -> None:
        receipt = self._receipt(merge_authority=True)
        errors = self._validate(receipt)
        self.assertTrue(any("merge authority" in error.lower() for error in errors))

    def test_open_review_can_be_valid_without_claiming_independence(self) -> None:
        receipt = self._receipt(
            verdict="COMMENT",
            independence_state="MATERIALLY_SHAPED_TARGET",
            shaping_or_diagnostic_refs=["design:v2"],
            material_shaping_within_reviewed_scope=True,
        )
        self.assertEqual(self._validate(receipt), [])

    def test_valid_receipt_requires_trusted_external_attestation_context(self) -> None:
        receipt = self._receipt()
        self.assertEqual(self._validate(receipt), [])


if __name__ == "__main__":
    unittest.main()
