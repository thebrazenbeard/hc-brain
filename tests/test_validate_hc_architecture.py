from __future__ import annotations

import unittest

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
                ),
            ]
        }
        self.assertEqual(validate_state_family_profiles(document), [])


class ReviewReceiptTests(unittest.TestCase):
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
            "admitted_context_refs": ["design:public-subject-only"],
            "verdict": "PASS",
            "evidence_refs": ["test-run:001"],
            "issued_at": "2026-09-17T12:00:00-04:00",
            "supersedes": [],
        }
        receipt.update(overrides)
        return receipt

    def test_stale_subject_head_is_rejected(self) -> None:
        errors = validate_review_receipt(
            self._receipt(subject_head="b" * 40),
            expected_repo="thebrazenbeard/hc-brain",
            expected_head="a" * 40,
        )
        self.assertTrue(any("subject_head" in error for error in errors))

    def test_empty_review_scope_is_rejected(self) -> None:
        errors = validate_review_receipt(
            self._receipt(reviewed_scope=[]),
            expected_repo="thebrazenbeard/hc-brain",
            expected_head="a" * 40,
        )
        self.assertTrue(any("reviewed_scope" in error for error in errors))

    def test_independent_claim_with_shaping_ancestry_is_rejected(self) -> None:
        errors = validate_review_receipt(
            self._receipt(shaping_or_diagnostic_refs=["finding:used-to-build-successor"]),
            expected_repo="thebrazenbeard/hc-brain",
            expected_head="a" * 40,
        )
        self.assertTrue(any("independence" in error.lower() for error in errors))

    def test_unknown_verdict_is_rejected(self) -> None:
        errors = validate_review_receipt(
            self._receipt(verdict="SUPER_PASS"),
            expected_repo="thebrazenbeard/hc-brain",
            expected_head="a" * 40,
        )
        self.assertTrue(any("verdict" in error for error in errors))

    def test_receipt_cannot_grant_merge_authority(self) -> None:
        errors = validate_review_receipt(
            self._receipt(merge_authority=True),
            expected_repo="thebrazenbeard/hc-brain",
            expected_head="a" * 40,
        )
        self.assertTrue(any("merge authority" in error.lower() for error in errors))

    def test_open_review_can_be_valid_without_claiming_independence(self) -> None:
        receipt = self._receipt(
            verdict="COMMENT",
            independence_state="MATERIALLY_SHAPED_TARGET",
            shaping_or_diagnostic_refs=["design:v2"],
        )
        self.assertEqual(
            validate_review_receipt(
                receipt,
                expected_repo="thebrazenbeard/hc-brain",
                expected_head="a" * 40,
            ),
            [],
        )


if __name__ == "__main__":
    unittest.main()
