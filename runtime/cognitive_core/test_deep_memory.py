import unittest

from runtime.reference_kernel.hc_kernel import EpistemicClass, ReferenceKernel
from runtime.cognitive_core.deep_memory import (
    DeepMemoryRuntime,
    DurabilityClass,
    MemoryClass,
    MemoryLifecycle,
)


class DeepMemoryRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.kernel = ReferenceKernel()
        self.runtime = DeepMemoryRuntime(self.kernel)
        self.obs = self.kernel.observe(
            producer="sensor:event",
            payload={"event": "door opened"},
        )

    def test_internal_admission_requires_basis_and_verified_internal_durability(self):
        with self.assertRaises(ValueError):
            self.runtime.admit(
                memory_id="memory:1",
                memory_class=MemoryClass.EPISODIC,
                payload={"event": "door opened"},
                source_evidence_ids=(self.obs.evidence_id,),
                basis_refs=(),
                durability=DurabilityClass.HC_INTERNAL,
            )
        record = self.runtime.admit(
            memory_id="memory:1",
            memory_class=MemoryClass.EPISODIC,
            payload={"event": "door opened"},
            source_evidence_ids=(self.obs.evidence_id,),
            basis_refs=("policy:memory-admission",),
            durability=DurabilityClass.HC_INTERNAL,
        )
        self.assertEqual(record.lifecycle, MemoryLifecycle.DURABLE)
        self.assertTrue(record.readback_verified)

    def test_external_replica_cannot_satisfy_essential_durable_admission(self):
        with self.assertRaises(ValueError):
            self.runtime.admit(
                memory_id="memory:external-only",
                memory_class=MemoryClass.AUTOBIOGRAPHICAL,
                payload={"event": "important"},
                source_evidence_ids=(self.obs.evidence_id,),
                basis_refs=("policy:memory-admission",),
                durability=DurabilityClass.EXTERNAL_REPLICA,
                essential=True,
            )

    def test_retrieval_is_candidate_not_truth_or_currentness(self):
        self.runtime.admit(
            memory_id="memory:1",
            memory_class=MemoryClass.EPISODIC,
            payload={"event": "door opened"},
            source_evidence_ids=(self.obs.evidence_id,),
            basis_refs=("policy:memory-admission",),
            durability=DurabilityClass.HC_INTERNAL,
        )
        candidate = self.runtime.retrieve("memory:1", purpose="context")
        self.assertEqual(candidate.status, "RETRIEVAL_CANDIDATE")
        self.assertFalse(candidate.admitted_as_true)
        self.assertFalse(candidate.current)

    def test_consolidation_preserves_source_lineage(self):
        obs2 = self.kernel.observe(
            producer="sensor:event",
            payload={"event": "door opened again"},
        )
        for mid, evidence_id, payload in (
            ("memory:1", self.obs.evidence_id, {"event": "door opened"}),
            ("memory:2", obs2.evidence_id, {"event": "door opened again"}),
        ):
            self.runtime.admit(
                memory_id=mid,
                memory_class=MemoryClass.EPISODIC,
                payload=payload,
                source_evidence_ids=(evidence_id,),
                basis_refs=("policy:memory-admission",),
                durability=DurabilityClass.HC_INTERNAL,
            )
        consolidated = self.runtime.consolidate(
            memory_id="memory:door-pattern",
            memory_class=MemoryClass.SEMANTIC,
            payload={"generalization": "door openings recur"},
            source_memory_ids=("memory:1", "memory:2"),
            basis_refs=("evaluation:recurrent-pattern",),
        )
        self.assertEqual(consolidated.memory_class, MemoryClass.SEMANTIC)
        self.assertEqual(consolidated.source_memory_ids, ("memory:1", "memory:2"))
        self.assertIn("memory:1", self.runtime.memories)
        self.assertIn("memory:2", self.runtime.memories)

    def test_contradiction_preserves_both_historical_records(self):
        first = self.runtime.admit(
            memory_id="memory:state-a",
            memory_class=MemoryClass.SEMANTIC,
            payload={"door": "open"},
            source_evidence_ids=(self.obs.evidence_id,),
            basis_refs=("policy:memory-admission",),
            durability=DurabilityClass.HC_INTERNAL,
        )
        obs2 = self.kernel.observe(producer="sensor:event", payload={"door": "closed"})
        second = self.runtime.admit(
            memory_id="memory:state-b",
            memory_class=MemoryClass.SEMANTIC,
            payload={"door": "closed"},
            source_evidence_ids=(obs2.evidence_id,),
            basis_refs=("policy:memory-admission",),
            durability=DurabilityClass.HC_INTERNAL,
        )
        conflict = self.runtime.record_contradiction(
            first.memory_id,
            second.memory_id,
            basis_refs=("evidence:conflict",),
        )
        self.assertEqual(conflict.status, "UNRESOLVED_CONTRADICTION")
        self.assertEqual(self.runtime.memories[first.memory_id].lifecycle, MemoryLifecycle.DURABLE)
        self.assertEqual(self.runtime.memories[second.memory_id].lifecycle, MemoryLifecycle.DURABLE)

    def test_privacy_scope_blocks_ineligible_retrieval(self):
        self.runtime.admit(
            memory_id="memory:private",
            memory_class=MemoryClass.EPISODIC,
            payload={"private": True},
            source_evidence_ids=(self.obs.evidence_id,),
            basis_refs=("policy:memory-admission",),
            durability=DurabilityClass.HC_INTERNAL,
            privacy_scopes=("scope:self",),
        )
        with self.assertRaises(PermissionError):
            self.runtime.retrieve(
                "memory:private",
                purpose="social",
                access_scope="scope:public",
            )
        candidate = self.runtime.retrieve(
            "memory:private",
            purpose="self-reflection",
            access_scope="scope:self",
        )
        self.assertEqual(candidate.memory_id, "memory:private")

    def test_consolidation_inherits_private_source_scope(self):
        public_observation = self.kernel.observe(
            producer="sensor:event", payload={"event": "another door opened"}
        )
        for mid, evidence_id, scopes in (
            ("memory:private", self.obs.evidence_id, ("scope:self",)),
            ("memory:public", public_observation.evidence_id, ()),
        ):
            self.runtime.admit(
                memory_id=mid,
                memory_class=MemoryClass.EPISODIC,
                payload={"event": "door opened"},
                source_evidence_ids=(evidence_id,),
                basis_refs=("policy:memory-admission",),
                durability=DurabilityClass.HC_INTERNAL,
                privacy_scopes=scopes,
            )

        derived = self.runtime.consolidate(
            memory_id="memory:derived",
            memory_class=MemoryClass.SEMANTIC,
            payload={"generalization": "door openings recur"},
            source_memory_ids=("memory:private", "memory:public"),
            basis_refs=("evaluation:recurrent-pattern",),
        )
        self.assertEqual(derived.privacy_scopes, ("scope:self",))
        with self.assertRaises(PermissionError):
            self.runtime.retrieve("memory:derived", purpose="publish", access_scope="scope:public")
        self.runtime.retrieve("memory:derived", purpose="self", access_scope="scope:self")

    def test_memory_derivation_cannot_widen_private_parent_scope(self):
        self.runtime.admit(
            memory_id="memory:private",
            memory_class=MemoryClass.EPISODIC,
            payload={"private": True},
            source_evidence_ids=(self.obs.evidence_id,),
            basis_refs=("policy:memory-admission",),
            durability=DurabilityClass.HC_INTERNAL,
            privacy_scopes=("scope:self",),
        )
        with self.assertRaisesRegex(ValueError, "broaden"):
            self.runtime.admit(
                memory_id="memory:broadened",
                memory_class=MemoryClass.SEMANTIC,
                payload={"derived": True},
                source_evidence_ids=(self.obs.evidence_id,),
                source_memory_ids=("memory:private",),
                basis_refs=("evaluation:derivation",),
                durability=DurabilityClass.HC_INTERNAL,
                privacy_scopes=("scope:self", "scope:public"),
            )
        self.assertNotIn("memory:broadened", self.runtime.memories)

    def test_private_memory_scope_persists_across_multiple_derivations(self):
        private = self.runtime.admit(
            memory_id="memory:private",
            memory_class=MemoryClass.EPISODIC,
            payload={"observation": "personal detail"},
            source_evidence_ids=(self.obs.evidence_id,),
            basis_refs=("policy:memory-admission",),
            durability=DurabilityClass.HC_INTERNAL,
            privacy_scopes=("scope:self",),
        )
        first = self.runtime.admit(
            memory_id="memory:first-derived",
            memory_class=MemoryClass.SEMANTIC,
            payload={"summary": "personal detail"},
            source_evidence_ids=private.source_evidence_ids,
            source_memory_ids=(private.memory_id,),
            basis_refs=("evaluation:first-derivation",),
            durability=DurabilityClass.HC_INTERNAL,
        )
        second = self.runtime.admit(
            memory_id="memory:second-derived",
            memory_class=MemoryClass.SEMANTIC,
            payload={"summary": "generalized personal detail"},
            source_evidence_ids=first.source_evidence_ids,
            source_memory_ids=(first.memory_id,),
            basis_refs=("evaluation:second-derivation",),
            durability=DurabilityClass.HC_INTERNAL,
        )
        self.assertEqual(first.privacy_scopes, ("scope:self",))
        self.assertEqual(second.privacy_scopes, ("scope:self",))
        with self.assertRaises(PermissionError):
            self.runtime.retrieve(second.memory_id, purpose="publish", access_scope="scope:public")

    def test_disjoint_private_source_scopes_cannot_be_consolidated(self):
        for mid, scope in (
            ("memory:self", "scope:self"),
            ("memory:other", "scope:other"),
        ):
            self.runtime.admit(
                memory_id=mid,
                memory_class=MemoryClass.EPISODIC,
                payload={"event": "door opened"},
                source_evidence_ids=(self.obs.evidence_id,),
                basis_refs=("policy:memory-admission",),
                durability=DurabilityClass.HC_INTERNAL,
                privacy_scopes=(scope,),
            )
        with self.assertRaisesRegex(ValueError, "disjoint"):
            self.runtime.consolidate(
                memory_id="memory:incompatible",
                memory_class=MemoryClass.SEMANTIC,
                payload={"derived": True},
                source_memory_ids=("memory:self", "memory:other"),
                basis_refs=("evaluation:derivation",),
            )
        self.assertNotIn("memory:incompatible", self.runtime.memories)

    def test_archived_memory_does_not_auto_enter_current_memory(self):
        before = len(self.kernel.memory.records)
        self.runtime.admit(
            memory_id="memory:1",
            memory_class=MemoryClass.EPISODIC,
            payload={"event": "door opened"},
            source_evidence_ids=(self.obs.evidence_id,),
            basis_refs=("policy:memory-admission",),
            durability=DurabilityClass.HC_INTERNAL,
        )
        self.assertEqual(len(self.kernel.memory.records), before)

    def test_imported_prediction_cannot_be_admitted_as_observed_episode(self):
        pred = self.kernel.derive(
            producer="cognition:world-model",
            epistemic_class=EpistemicClass.PREDICTION,
            payload={"future": "door opens"},
            parent_ids=(self.obs.evidence_id,),
        )
        with self.assertRaises(ValueError):
            self.runtime.admit(
                memory_id="memory:false-episode",
                memory_class=MemoryClass.EPISODIC,
                payload={"event": "door opened"},
                source_evidence_ids=(pred.evidence_id,),
                basis_refs=("policy:memory-admission",),
                durability=DurabilityClass.HC_INTERNAL,
                require_observed_episode=True,
            )


if __name__ == "__main__":
    unittest.main()
