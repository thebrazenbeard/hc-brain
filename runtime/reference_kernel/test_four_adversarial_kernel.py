from datetime import datetime, timedelta, timezone
from pathlib import Path
import tempfile
import unittest

from durable_kernel import DurableReferenceKernel
from hc_kernel import EffectCandidate, EffectState, EpistemicClass, ReferenceKernel

UTC=timezone.utc

class FourAdversarialReferenceKernelTests(unittest.TestCase):
    """Regression gates adapted from Four's HC 0058 counterexamples.

    The invariant targets are unchanged. The harness uses a constructor-injected
    trusted clock because per-request caller time is intentionally unavailable.
    """
    def setUp(self): self.t0=datetime(2026,9,10,18,0,tzinfo=UTC)
    def _kernel(self): return ReferenceKernel(clock=lambda:self.t0)
    @staticmethod
    def _register(kernel, valid_from, expires_at):
        return kernel.register_grant(grantor="authority-fixture",grantee="kinesis",action_scope="MOTOR_EFFECT",target_scope="arm",basis_refs=("fixture-basis",),provenance=("four-adversarial",),valid_from=valid_from,expires_at=expires_at)
    @staticmethod
    def _candidate(kernel, grant_id):
        return kernel.plan_effect(origin="kinesis",action_scope="MOTOR_EFFECT",target_scope="arm",payload={"command":"move"},authority_grant_id=grant_id)

    def test_expired_authority_cannot_be_reactivated_by_caller_backdating(self):
        kernel=self._kernel(); grant=self._register(kernel,self.t0-timedelta(minutes=10),self.t0-timedelta(seconds=1)); candidate=self._candidate(kernel,grant.grant_id)
        with self.assertRaises(TypeError): kernel.request_effect(candidate, now=self.t0-timedelta(minutes=5))
        receipt=kernel.request_effect(candidate); self.assertEqual(receipt.state,EffectState.BLOCKED); self.assertEqual(receipt.reason,"EXPIRED_AUTHORITY")

    def test_revoked_authority_cannot_be_reactivated_by_caller_backdating(self):
        kernel=self._kernel(); grant=self._register(kernel,self.t0-timedelta(minutes=10),self.t0+timedelta(minutes=10)); kernel.revoke_grant(grant.grant_id,revoked_at=self.t0-timedelta(seconds=1)); candidate=self._candidate(kernel,grant.grant_id)
        with self.assertRaises(TypeError): kernel.request_effect(candidate, now=self.t0-timedelta(seconds=30))
        receipt=kernel.request_effect(candidate); self.assertEqual(receipt.state,EffectState.BLOCKED); self.assertEqual(receipt.reason,"REVOKED_AUTHORITY")

    def test_same_action_id_with_different_candidate_semantics_fails_closed(self):
        kernel=self._kernel(); grant=self._register(kernel,self.t0-timedelta(minutes=1),self.t0+timedelta(minutes=10)); original=self._candidate(kernel,grant.grant_id)
        first=kernel.request_effect(original); self.assertEqual(first.state,EffectState.REQUESTED)
        collision=EffectCandidate(action_id=original.action_id,origin="different-origin",action_scope="UNAUTHORIZED_EFFECT",target_scope="different-target",payload={"command":"different"},authority_grant_id=None,planned_epoch=kernel.epoch,parent_ids=())
        with self.assertRaises(ValueError): kernel.request_effect(collision)

    def test_observation_payload_is_immutable_after_admission(self):
        kernel=self._kernel(); caller={"reading":1,"nested":{"value":"original"}}; record=kernel.observe(producer="sensor",payload=caller,source_refs=("sensor-1",)); caller["reading"]=999; caller["nested"]["value"]="mutated"
        self.assertEqual(record.payload["reading"],1); self.assertEqual(record.payload["nested"]["value"],"original")

    def test_current_projection_preserves_epistemic_and_source_classification(self):
        kernel=self._kernel(); key=("world","weather","next","shared"); source=kernel.observe(producer="sensor",payload={"clouds":True},source_refs=("camera-1",)); prediction=kernel.derive(producer="cognition",epistemic_class=EpistemicClass.PREDICTION,payload={"future":"rain"},parent_ids=(source.evidence_id,)); kernel.memory.append(logical_key=key,payload=prediction.payload,epistemic_class=prediction.epistemic_class,source_refs=prediction.source_refs); projection=kernel.memory.current(key)
        self.assertEqual(projection.epistemic_class,EpistemicClass.PREDICTION); self.assertIn("camera-1",projection.source_refs)

    def test_durable_live_and_replayed_payload_remain_identical_after_caller_mutation(self):
        with tempfile.TemporaryDirectory() as td:
            journal=Path(td)/"kernel.jsonl"; kernel=DurableReferenceKernel(journal,clock=lambda:self.t0); caller={"reading":1,"nested":{"value":"original"}}; record=kernel.observe(producer="sensor",payload=caller,source_refs=("sensor-1",)); caller["reading"]=999; caller["nested"]["value"]="mutated"; live=kernel.evidence[record.evidence_id].payload; replayed=DurableReferenceKernel(journal,mode="inspect",clock=lambda:self.t0).evidence[record.evidence_id].payload
            self.assertEqual(live,replayed); self.assertEqual(live["reading"],1); self.assertEqual(live["nested"]["value"],"original")

if __name__ == "__main__": unittest.main()
