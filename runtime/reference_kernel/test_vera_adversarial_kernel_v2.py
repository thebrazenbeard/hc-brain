from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from governed_kernel_v2 import GovernedDurableReferenceKernelV2, GovernedReferenceKernelV2

TEST_POLICY_ID = "test-move-policy-v1"


def allow_test_move_grants(request):
    return request.principal == "operator-A" and request.grantee.startswith("planner") and request.action_scope == "MOVE" and request.target_scope.startswith("arm") and bool(request.basis_refs)


class VeraAuthorityMutationV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.now = datetime(2026, 9, 17, 12, 0, tzinfo=timezone.utc)
        self.issuer_a = object()
        self.issuer_b = object()

    def kernel(self) -> GovernedReferenceKernelV2:
        return GovernedReferenceKernelV2(clock=lambda: self.now, authority_issuer_capabilities=((self.issuer_a, "operator-A"), (self.issuer_b, "operator-B")), authority_issuance_validator=allow_test_move_grants, authority_issuance_policy_id=TEST_POLICY_ID)

    def test_unregistered_handle_cannot_mint_authority(self) -> None:
        with self.assertRaisesRegex(ValueError, "authority issuer capability is not registered"):
            self.kernel().register_grant(source_capability=object(), grantee="planner", action_scope="MOVE", target_scope="arm", basis_refs=("basis:explicit",), valid_from=self.now, expires_at=self.now + timedelta(minutes=5))

    def test_grantor_is_derived_from_opaque_capability(self) -> None:
        grant = self.kernel().register_grant(source_capability=self.issuer_a, grantee="planner", action_scope="MOVE", target_scope="arm", basis_refs=("basis:explicit",), valid_from=self.now, expires_at=self.now + timedelta(minutes=5))
        self.assertEqual(grant.grantor, "operator-A")

    def test_foreign_principal_cannot_revoke_grant(self) -> None:
        kernel = self.kernel()
        grant = kernel.register_grant(source_capability=self.issuer_a, grantee="planner", action_scope="MOVE", target_scope="arm", basis_refs=("basis:explicit",), valid_from=self.now, expires_at=self.now + timedelta(minutes=5))
        with self.assertRaisesRegex(ValueError, "authority revoker does not own this grant"):
            kernel.revoke_grant(grant.grant_id, source_capability=self.issuer_b, revoked_at=self.now + timedelta(seconds=30))
        self.assertIsNone(kernel.authority_grants[grant.grant_id].revoked_at)

    def test_scalar_capability_registration_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "opaque object handles"):
            GovernedReferenceKernelV2(authority_issuer_capabilities=(("spoofable-token", "operator-A"),), authority_issuance_validator=allow_test_move_grants, authority_issuance_policy_id=TEST_POLICY_ID)

    def test_authenticated_issuer_still_requires_scope_policy(self) -> None:
        def policy(request):
            return request.principal == "operator-A" and request.grantee == "planner" and request.action_scope == "MOVE" and request.target_scope == "arm" and bool(request.basis_refs)
        kernel = GovernedReferenceKernelV2(clock=lambda: self.now, authority_issuer_capabilities=((self.issuer_a, "operator-A"),), authority_issuance_validator=policy, authority_issuance_policy_id="bounded-arm-policy-v1")
        self.assertEqual(kernel.register_grant(source_capability=self.issuer_a, grantee="planner", action_scope="MOVE", target_scope="arm", basis_refs=("basis:explicit",), valid_from=self.now, expires_at=self.now + timedelta(minutes=5)).grantor, "operator-A")
        with self.assertRaisesRegex(ValueError, "authority issuance policy denied grant"):
            kernel.register_grant(source_capability=self.issuer_a, grantee="planner", action_scope="IDENTITY_REWRITE", target_scope="self", basis_refs=("basis:explicit",), valid_from=self.now, expires_at=self.now + timedelta(minutes=5))

    def test_issuance_policy_receives_temporal_and_epoch_context(self) -> None:
        captured = {}

        def temporal_policy(*args):
            if len(args) != 1:
                raise AssertionError("authority issuance policy must receive one immutable request context")
            request = args[0]
            captured["request"] = request
            return (
                request.principal == "operator-A"
                and request.grantee == "planner"
                and request.action_scope == "MOVE"
                and request.target_scope == "arm"
                and request.basis_refs == ("basis:explicit",)
                and request.valid_from == self.now
                and request.expires_at == self.now + timedelta(minutes=5)
                and request.observed_at == self.now
                and request.current_epoch == 0
            )

        kernel = GovernedReferenceKernelV2(
            clock=lambda: self.now,
            authority_issuer_capabilities=((self.issuer_a, "operator-A"),),
            authority_issuance_validator=temporal_policy,
            authority_issuance_policy_id="temporal-arm-policy-v1",
        )
        kernel.register_grant(
            source_capability=self.issuer_a,
            grantee="planner",
            action_scope="MOVE",
            target_scope="arm",
            basis_refs=("basis:explicit",),
            valid_from=self.now,
            expires_at=self.now + timedelta(minutes=5),
        )
        self.assertEqual(captured["request"].current_epoch, 0)

    def test_missing_issuance_policy_fails_closed(self) -> None:
        kernel = GovernedReferenceKernelV2(clock=lambda: self.now, authority_issuer_capabilities=((self.issuer_a, "operator-A"),))
        with self.assertRaisesRegex(ValueError, "authority issuance policy is not configured"):
            kernel.register_grant(source_capability=self.issuer_a, grantee="planner", action_scope="MOVE", target_scope="arm", basis_refs=("basis:explicit",), valid_from=self.now, expires_at=self.now + timedelta(minutes=5))

    def test_validator_without_policy_identity_is_rejected_before_use(self) -> None:
        with self.assertRaisesRegex(ValueError, "policy ID must be configured"):
            GovernedReferenceKernelV2(authority_issuer_capabilities=((self.issuer_a, "operator-A"),), authority_issuance_validator=allow_test_move_grants)

    def test_issuance_policy_identity_is_kernel_bound_into_grant_provenance(self) -> None:
        grant = self.kernel().register_grant(source_capability=self.issuer_a, grantee="planner", action_scope="MOVE", target_scope="arm", basis_refs=("basis:explicit",), valid_from=self.now, expires_at=self.now + timedelta(minutes=5), provenance=("caller-context",))
        self.assertIn("caller-context", grant.provenance)
        self.assertIn(f"authority-issuance-policy:{TEST_POLICY_ID}", grant.provenance)

    def test_caller_cannot_forge_reserved_authority_policy_provenance(self) -> None:
        with self.assertRaisesRegex(ValueError, "reserved authority issuance policy provenance"):
            self.kernel().register_grant(source_capability=self.issuer_a, grantee="planner", action_scope="MOVE", target_scope="arm", basis_refs=("basis:explicit",), valid_from=self.now, expires_at=self.now + timedelta(minutes=5), provenance=("authority-issuance-policy:forged",))


class VeraAtomicRecoveryFenceV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.now = datetime(2026, 9, 17, 12, 0, tzinfo=timezone.utc)
        self.issuer = object()

    def _make_kernel(self, path: Path) -> GovernedDurableReferenceKernelV2:
        return GovernedDurableReferenceKernelV2(path, clock=lambda: self.now, authority_issuer_capabilities=((self.issuer, "operator-A"),), authority_issuance_validator=allow_test_move_grants, authority_issuance_policy_id=TEST_POLICY_ID)

    def _requested_action(self, kernel: GovernedDurableReferenceKernelV2, suffix: str):
        grant = kernel.register_grant(source_capability=self.issuer, grantee=f"planner-{suffix}", action_scope="MOVE", target_scope=f"arm-{suffix}", basis_refs=(f"basis:{suffix}",), valid_from=self.now, expires_at=self.now + timedelta(minutes=5))
        candidate = kernel.plan_effect(origin=f"planner-{suffix}", action_scope="MOVE", target_scope=f"arm-{suffix}", payload={"suffix": suffix}, authority_grant_id=grant.grant_id)
        receipt = kernel.request_effect(candidate)
        self.assertEqual(receipt.state.value, "REQUESTED")
        return candidate.action_id

    def test_restart_persists_one_semantic_recovery_fence(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "journal.jsonl"
            kernel = self._make_kernel(path)
            action_a, action_b = self._requested_action(kernel, "a"), self._requested_action(kernel, "b")
            before = len(path.read_text(encoding="utf-8").splitlines())
            self.assertEqual(kernel.restart(), 1)
            appended = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()][before:]
            self.assertEqual(len(appended), 1)
            self.assertEqual(appended[0]["event_type"], "RECOVERY_FENCE")
            self.assertEqual(appended[0]["data"]["requested_action_ids"], sorted([action_a, action_b]))
            self.assertEqual(kernel.effect_receipts[action_a].state.value, "UNRESOLVED_AFTER_RESTART")
            self.assertEqual(kernel.effect_receipts[action_b].state.value, "UNRESOLVED_AFTER_RESTART")

    def test_replay_rejects_recovery_fence_with_incomplete_requested_set(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            kernel = self._make_kernel(Path(tmp) / "journal.jsonl")
            self._requested_action(kernel, "a"); self._requested_action(kernel, "b")
            with self.assertRaisesRegex(ValueError, "requested_action_ids must exactly match"):
                kernel._validate_recovery_fence({"from_epoch": 0, "to_epoch": 1, "requested_action_ids": [next(iter(kernel.effect_receipts))]}, event_epoch=0)

    def test_replay_rejects_duplicate_requested_ids(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            kernel = self._make_kernel(Path(tmp) / "journal.jsonl")
            action = self._requested_action(kernel, "a")
            with self.assertRaisesRegex(ValueError, "unique canonical order"):
                kernel._validate_recovery_fence({"from_epoch": 0, "to_epoch": 1, "requested_action_ids": [action, action]}, event_epoch=0)

    def test_replay_rejects_noncontiguous_recovery_epoch(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            kernel = self._make_kernel(Path(tmp) / "journal.jsonl")
            with self.assertRaisesRegex(ValueError, "recovery fence epoch is not contiguous"):
                kernel._validate_recovery_fence({"from_epoch": 0, "to_epoch": 2, "requested_action_ids": []}, event_epoch=0)

    def test_failed_recovery_append_does_not_promote_epoch_or_receipts(self) -> None:
        class FailingFenceKernel(GovernedDurableReferenceKernelV2):
            fail_fence = False
            def _record(self, event_type, data):
                if self.fail_fence and event_type == "RECOVERY_FENCE":
                    raise OSError("injected fence append failure")
                return super()._record(event_type, data)
        with tempfile.TemporaryDirectory() as tmp:
            kernel = FailingFenceKernel(Path(tmp) / "journal.jsonl", clock=lambda: self.now, authority_issuer_capabilities=((self.issuer, "operator-A"),), authority_issuance_validator=allow_test_move_grants, authority_issuance_policy_id=TEST_POLICY_ID)
            action = self._requested_action(kernel, "a")
            kernel.fail_fence = True
            with self.assertRaisesRegex(OSError, "injected fence append failure"):
                kernel.restart()
            self.assertEqual(kernel.epoch, 0)
            self.assertEqual(kernel.effect_receipts[action].state.value, "REQUESTED")


if __name__ == "__main__":
    unittest.main()
