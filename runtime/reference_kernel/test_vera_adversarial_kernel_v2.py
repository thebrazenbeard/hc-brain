from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from governed_kernel_v2 import (
    GovernedDurableReferenceKernelV2,
    GovernedReferenceKernelV2,
)


class VeraAuthorityMutationV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.now = datetime(2026, 9, 17, 12, 0, tzinfo=timezone.utc)
        self.issuer_a = object()
        self.issuer_b = object()

    def kernel(self) -> GovernedReferenceKernelV2:
        return GovernedReferenceKernelV2(
            clock=lambda: self.now,
            authority_issuer_capabilities=(
                (self.issuer_a, "operator-A"),
                (self.issuer_b, "operator-B"),
            ),
        )

    def test_unregistered_handle_cannot_mint_authority(self) -> None:
        kernel = self.kernel()
        with self.assertRaisesRegex(
            ValueError, "authority issuer capability is not registered"
        ):
            kernel.register_grant(
                source_capability=object(),
                grantee="planner",
                action_scope="MOVE",
                target_scope="arm",
                basis_refs=("basis:explicit",),
                valid_from=self.now,
                expires_at=self.now + timedelta(minutes=5),
            )

    def test_grantor_is_derived_from_opaque_capability(self) -> None:
        kernel = self.kernel()
        grant = kernel.register_grant(
            source_capability=self.issuer_a,
            grantee="planner",
            action_scope="MOVE",
            target_scope="arm",
            basis_refs=("basis:explicit",),
            valid_from=self.now,
            expires_at=self.now + timedelta(minutes=5),
        )
        self.assertEqual(grant.grantor, "operator-A")

    def test_foreign_principal_cannot_revoke_grant(self) -> None:
        kernel = self.kernel()
        grant = kernel.register_grant(
            source_capability=self.issuer_a,
            grantee="planner",
            action_scope="MOVE",
            target_scope="arm",
            basis_refs=("basis:explicit",),
            valid_from=self.now,
            expires_at=self.now + timedelta(minutes=5),
        )
        with self.assertRaisesRegex(
            ValueError, "authority revoker does not own this grant"
        ):
            kernel.revoke_grant(
                grant.grant_id,
                source_capability=self.issuer_b,
                revoked_at=self.now + timedelta(seconds=30),
            )
        self.assertIsNone(kernel.authority_grants[grant.grant_id].revoked_at)

    def test_scalar_capability_registration_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "opaque object handles"):
            GovernedReferenceKernelV2(
                authority_issuer_capabilities=(("spoofable-token", "operator-A"),)
            )


class VeraAtomicRecoveryFenceV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.now = datetime(2026, 9, 17, 12, 0, tzinfo=timezone.utc)
        self.issuer = object()

    def _make_kernel(self, path: Path) -> GovernedDurableReferenceKernelV2:
        return GovernedDurableReferenceKernelV2(
            path,
            clock=lambda: self.now,
            authority_issuer_capabilities=((self.issuer, "operator-A"),),
        )

    def _requested_action(self, kernel: GovernedDurableReferenceKernelV2, suffix: str):
        grant = kernel.register_grant(
            source_capability=self.issuer,
            grantee=f"planner-{suffix}",
            action_scope="MOVE",
            target_scope=f"arm-{suffix}",
            basis_refs=(f"basis:{suffix}",),
            valid_from=self.now,
            expires_at=self.now + timedelta(minutes=5),
        )
        candidate = kernel.plan_effect(
            origin=f"planner-{suffix}",
            action_scope="MOVE",
            target_scope=f"arm-{suffix}",
            payload={"suffix": suffix},
            authority_grant_id=grant.grant_id,
        )
        receipt = kernel.request_effect(candidate)
        self.assertEqual(receipt.state.value, "REQUESTED")
        return candidate.action_id

    def test_restart_persists_one_semantic_recovery_fence(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "journal.jsonl"
            kernel = self._make_kernel(path)
            action_a = self._requested_action(kernel, "a")
            action_b = self._requested_action(kernel, "b")
            before = len(path.read_text(encoding="utf-8").splitlines())

            self.assertEqual(kernel.restart(), 1)

            lines = [
                json.loads(line)
                for line in path.read_text(encoding="utf-8").splitlines()
            ]
            appended = lines[before:]
            self.assertEqual(len(appended), 1)
            self.assertEqual(appended[0]["event_type"], "RECOVERY_FENCE")
            self.assertEqual(
                appended[0]["data"]["requested_action_ids"],
                sorted([action_a, action_b]),
            )
            self.assertEqual(kernel.effect_receipts[action_a].state.value, "UNRESOLVED_AFTER_RESTART")
            self.assertEqual(kernel.effect_receipts[action_b].state.value, "UNRESOLVED_AFTER_RESTART")

    def test_replay_rejects_recovery_fence_with_incomplete_requested_set(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "journal.jsonl"
            kernel = self._make_kernel(path)
            self._requested_action(kernel, "a")
            self._requested_action(kernel, "b")

            with self.assertRaisesRegex(
                ValueError, "recovery fence requested_action_ids must exactly match"
            ):
                kernel._validate_recovery_fence(
                    {
                        "from_epoch": 0,
                        "to_epoch": 1,
                        "requested_action_ids": [
                            next(iter(kernel.effect_receipts))
                        ],
                    },
                    event_epoch=0,
                )

    def test_replay_rejects_noncontiguous_recovery_epoch(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "journal.jsonl"
            kernel = self._make_kernel(path)
            with self.assertRaisesRegex(ValueError, "recovery fence epoch is not contiguous"):
                kernel._validate_recovery_fence(
                    {
                        "from_epoch": 0,
                        "to_epoch": 2,
                        "requested_action_ids": [],
                    },
                    event_epoch=0,
                )


if __name__ == "__main__":
    unittest.main()
