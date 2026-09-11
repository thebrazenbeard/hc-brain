from datetime import datetime, timedelta, timezone
import hashlib, json, os, subprocess, sys, tempfile, unittest
from pathlib import Path
from durable_kernel import DurableReferenceKernel, JournalIntegrityError, ReadOnlyInspectionError
from hc_kernel import EpistemicClass, EffectState, ProjectionStatus
UTC=timezone.utc

class DurableReferenceKernelTests(unittest.TestCase):
    def setUp(self):
        self.tempdir=tempfile.TemporaryDirectory(); self.journal=Path(self.tempdir.name)/"hc.jsonl"; self.now=datetime(2026,9,10,19,0,tzinfo=UTC)
    def tearDown(self): self.tempdir.cleanup()
    def _kernel(self,mode="recover"): return DurableReferenceKernel(self.journal,mode=mode,clock=lambda:self.now)
    def _grant(self,k): return k.register_grant(grantor="authority-fixture",grantee="kinesis",action_scope="MOTOR_EFFECT",target_scope="arm",basis_refs=("fixture-basis",),provenance=("durable-test",),valid_from=self.now-timedelta(minutes=1),expires_at=self.now+timedelta(minutes=10))
    @staticmethod
    def _rehash(e):
        body={k:v for k,v in e.items() if k!="entry_hash"}; e["entry_hash"]=hashlib.sha256(json.dumps(body,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest(); return e
    def _rewrite_line(self,index,mutator):
        lines=self.journal.read_text().splitlines(); e=json.loads(lines[index]); mutator(e); self._rehash(e); lines[index]=json.dumps(e,ensure_ascii=False,sort_keys=True,separators=(",",":")); self.journal.write_text("\n".join(lines)+"\n")

    def test_memory_and_ambiguity_survive_reopen(self):
        first=self._kernel(); key=("world","object-1","state","shared"); a=first.memory.append(logical_key=key,payload={"state":"A"},epistemic_class=EpistemicClass.OBSERVATION); b=first.memory.append(logical_key=key,payload={"state":"B"},epistemic_class=EpistemicClass.OBSERVATION); self.assertEqual(first.memory.current(key).status,ProjectionStatus.AMBIGUOUS)
        second=self._kernel(); p=second.memory.current(key); self.assertEqual(p.status,ProjectionStatus.AMBIGUOUS); self.assertEqual(set(p.head_ids),{a.record_id,b.record_id})
    def test_derived_evidence_lineage_survives_reopen(self):
        first=self._kernel(); obs=first.observe(producer="optics",payload={"object":"ball"},source_refs=("camera-1",)); pred=first.derive(producer="cognition",epistemic_class=EpistemicClass.PREDICTION,payload={"next":"move"},parent_ids=(obs.evidence_id,),influence_roles=("WORLD_MODEL_INPUT",)); second=self._kernel(); r=second.evidence[pred.evidence_id]; self.assertEqual(r.epistemic_class,EpistemicClass.PREDICTION); self.assertEqual(r.parent_ids,(obs.evidence_id,)); self.assertIn("camera-1",r.source_refs)
    def test_requested_effect_becomes_unresolved_on_reopen_and_is_not_redispatched(self):
        first=self._kernel(); g=self._grant(first); c=first.plan_effect(origin="kinesis",action_scope="MOTOR_EFFECT",target_scope="arm",payload={"command":"move"},authority_grant_id=g.grant_id); r=first.request_effect(c); self.assertEqual(r.state,EffectState.REQUESTED); self.assertEqual(r.dispatch_attempts,1)
        second=self._kernel(); restored=second.effect_receipts[c.action_id]; self.assertEqual(restored.state,EffectState.UNRESOLVED_AFTER_RESTART); replay=second.request_effect(c); self.assertIs(replay,restored); self.assertEqual(replay.dispatch_attempts,1)
        fresh=second.plan_effect(origin="kinesis",action_scope="MOTOR_EFFECT",target_scope="arm",payload={"command":"other"},authority_grant_id=g.grant_id); old=second.request_effect(fresh); self.assertEqual(old.state,EffectState.BLOCKED); self.assertEqual(old.reason,"STALE_AUTHORITY_EPOCH")
    def test_confirmed_effect_remains_confirmed_after_reopen(self):
        first=self._kernel(); g=self._grant(first); c=first.plan_effect(origin="kinesis",action_scope="MOTOR_EFFECT",target_scope="arm",payload={"command":"move"},authority_grant_id=g.grant_id); first.request_effect(c); obs=first.observe(producer="somatics",payload={"arm_position":"moved"},source_refs=("proprioception",),effect_action_id=c.action_id); first.confirm_effect(c.action_id,succeeded=True,confirmation_evidence_id=obs.evidence_id); second=self._kernel(); restored=second.effect_receipts[c.action_id]; self.assertEqual(restored.state,EffectState.CONFIRMED); self.assertEqual(restored.confirmation_evidence_id,obs.evidence_id)
    def test_corrupted_entry_hash_fails_closed(self):
        k=self._kernel(); k.observe(producer="optics",payload={"x":1}); lines=self.journal.read_text().splitlines(); e=json.loads(lines[-1]); e["data"]["payload"]["x"]=2; lines[-1]=json.dumps(e,sort_keys=True,separators=(",",":")); self.journal.write_text("\n".join(lines)+"\n")
        with self.assertRaises(JournalIntegrityError): self._kernel("inspect")
    def test_sequence_discontinuity_fails_closed_even_if_entry_rehashed(self):
        k=self._kernel(); k.observe(producer="optics",payload={"x":1}); self._rewrite_line(-1,lambda e:e.__setitem__("seq",9))
        with self.assertRaises(JournalIntegrityError): self._kernel("inspect")
    def test_epoch_mismatch_fails_closed_even_if_entry_rehashed(self):
        k=self._kernel(); k.observe(producer="optics",payload={"x":1}); self._rewrite_line(-1,lambda e:e.__setitem__("epoch",1))
        with self.assertRaises(JournalIntegrityError): self._kernel("inspect")
    def test_grant_without_basis_fails_replay_even_if_entry_rehashed(self):
        k=self._kernel(); self._grant(k); self._rewrite_line(-1,lambda e:e["data"].__setitem__("basis_refs",[]))
        with self.assertRaises(JournalIntegrityError): self._kernel("inspect")
    def test_missing_derived_parent_fails_replay_even_if_entry_rehashed(self):
        k=self._kernel(); obs=k.observe(producer="optics",payload={"x":1}); k.derive(producer="cognition",epistemic_class=EpistemicClass.PREDICTION,payload={"x":2},parent_ids=(obs.evidence_id,)); self._rewrite_line(-1,lambda e:e["data"].__setitem__("parent_ids",["missing-parent"]))
        with self.assertRaises(JournalIntegrityError): self._kernel("inspect")
    def test_confirmed_receipt_rejects_wrong_bound_evidence_on_replay(self):
        k=self._kernel(); g=self._grant(k); c=k.plan_effect(origin="kinesis",action_scope="MOTOR_EFFECT",target_scope="arm",payload={"command":"move"},authority_grant_id=g.grant_id); k.request_effect(c); unrelated=k.observe(producer="somatics",payload={"temperature":37}); bound=k.observe(producer="somatics",payload={"arm_position":"moved"},effect_action_id=c.action_id); k.confirm_effect(c.action_id,succeeded=True,confirmation_evidence_id=bound.evidence_id); self._rewrite_line(-1,lambda e:e["data"].__setitem__("confirmation_evidence_id",unrelated.evidence_id))
        with self.assertRaises(JournalIntegrityError): self._kernel("inspect")
    def test_unserializable_payload_rejected_before_state_mutation(self):
        k=self._kernel()
        with self.assertRaises(ValueError): k.observe(producer="optics",payload={1,2,3})
        self.assertEqual(k.evidence,{}); self.assertFalse(self.journal.exists())
    def test_inspection_mode_is_nonmutating_and_read_only(self):
        k=self._kernel(); k.observe(producer="optics",payload={"x":1}); before=self.journal.read_bytes(); inspection=self._kernel("inspect"); self.assertEqual(inspection.epoch,k.epoch); self.assertEqual(self.journal.read_bytes(),before)
        with self.assertRaises(ReadOnlyInspectionError): inspection.observe(producer="optics",payload={"x":2})
        self.assertEqual(self.journal.read_bytes(),before)
    def test_reconciled_outcome_is_durable(self):
        first=self._kernel(); g=self._grant(first); c=first.plan_effect(origin="kinesis",action_scope="MOTOR_EFFECT",target_scope="arm",payload={"command":"move"},authority_grant_id=g.grant_id); first.request_effect(c); second=self._kernel(); obs=second.observe(producer="somatics",payload={"arm_position":"moved"},source_refs=("proprioception",),effect_action_id=c.action_id); second.reconcile_after_restart(c.action_id,confirmed_outcome=True,confirmation_evidence_id=obs.evidence_id); third=self._kernel("inspect"); self.assertEqual(third.effect_receipts[c.action_id].state,EffectState.CONFIRMED)
    def test_separate_process_reopen_marks_inflight_effect_unresolved(self):
        kernel_dir=Path(__file__).resolve().parent
        writer="""
import sys
from datetime import datetime,timedelta,timezone
from durable_kernel import DurableReferenceKernel
now=datetime(2026,9,10,19,0,tzinfo=timezone.utc)
k=DurableReferenceKernel(sys.argv[1],clock=lambda:now)
g=k.register_grant(grantor='fixture',grantee='kinesis',action_scope='MOTOR_EFFECT',target_scope='arm',basis_refs=('basis',),valid_from=now-timedelta(minutes=1),expires_at=now+timedelta(minutes=10))
c=k.plan_effect(origin='kinesis',action_scope='MOTOR_EFFECT',target_scope='arm',payload={'command':'move'},authority_grant_id=g.grant_id)
r=k.request_effect(c)
print(c.action_id)
"""
        result=subprocess.run([sys.executable,"-c",writer,str(self.journal)],cwd=kernel_dir,text=True,capture_output=True,check=True,env=os.environ.copy()); action_id=result.stdout.strip(); self.assertTrue(action_id)
        reader="""
import sys
from datetime import datetime,timezone
from durable_kernel import DurableReferenceKernel
now=datetime(2026,9,10,19,0,tzinfo=timezone.utc)
k=DurableReferenceKernel(sys.argv[1],clock=lambda:now)
r=k.effect_receipts[sys.argv[2]]
print(r.state.value,r.dispatch_attempts,k.epoch)
"""
        result=subprocess.run([sys.executable,"-c",reader,str(self.journal),action_id],cwd=kernel_dir,text=True,capture_output=True,check=True,env=os.environ.copy()); state,attempts,epoch=result.stdout.strip().split(); self.assertEqual(state,EffectState.UNRESOLVED_AFTER_RESTART.value); self.assertEqual(int(attempts),1); self.assertEqual(int(epoch),1)

if __name__=="__main__": unittest.main()
