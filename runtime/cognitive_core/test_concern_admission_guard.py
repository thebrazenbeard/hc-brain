"""Synthetic, no-effect regression tests for governed concern state transitions."""

import unittest

from runtime.cognitive_core.cognitive_loop import (
    Concern,
    ConcernState,
    CognitiveRuntime,
)
from runtime.reference_kernel.hc_kernel import ReferenceKernel


def concern(*, state=ConcernState.PRESENT, target="concept:goal", strength=0.7):
    return Concern(
        concern_id="concern:goal",
        target_concept=target,
        strength=strength,
        state=state,
    )


class ConcernAdmissionGuardTests(unittest.TestCase):
    def setUp(self):
        self.runtime = CognitiveRuntime(ReferenceKernel())

    def test_new_concerns_only_enter_emerging_or_present(self):
        for state in (ConcernState.EMERGING, ConcernState.PRESENT):
            with self.subTest(state=state):
                runtime = CognitiveRuntime(ReferenceKernel())
                runtime.set_concern(concern(state=state))
                self.assertEqual(runtime.concern_history("concern:goal"), (concern(state=state),))
        for state in ConcernState:
            if state in (ConcernState.EMERGING, ConcernState.PRESENT):
                continue
            with self.subTest(rejected_state=state):
                runtime = CognitiveRuntime(ReferenceKernel())
                with self.assertRaises(ValueError):
                    runtime.set_concern(concern(state=state))
                self.assertEqual(runtime.concern_history("concern:goal"), ())

    def test_direct_set_cannot_bypass_transition_or_replace_identity(self):
        initial = concern()
        self.runtime.set_concern(initial)
        for changed in (
            concern(state=ConcernState.INTENTION_CANDIDATE),
            concern(state=ConcernState.EXECUTING),
            concern(state=ConcernState.SATISFIED),
            concern(target="concept:unrelated"),
            concern(strength=0.99),
        ):
            with self.subTest(changed=changed):
                with self.assertRaises(ValueError):
                    self.runtime.set_concern(changed)
                self.assertEqual(self.runtime.concern_history(initial.concern_id), (initial,))

    def test_idempotent_exact_repeat_preserves_history(self):
        initial = concern()
        self.runtime.set_concern(initial)
        self.runtime.set_concern(initial)
        self.assertEqual(self.runtime.concern_history(initial.concern_id), (initial,))

    def test_guarded_transition_still_preserves_reason_provenance(self):
        self.runtime.set_concern(concern())
        updated = self.runtime.transition_concern(
            "concern:goal",
            ConcernState.INTENTION_CANDIDATE,
            reason_refs=("source:1",),
        )
        self.assertEqual(updated.state, ConcernState.INTENTION_CANDIDATE)
        self.assertEqual(updated.provenance, ("source:1",))
        self.assertEqual(
            tuple(c.state for c in self.runtime.concern_history("concern:goal")),
            (ConcernState.PRESENT, ConcernState.INTENTION_CANDIDATE),
        )

    def test_transition_rejects_empty_or_untrusted_reason_refs(self):
        self.runtime.set_concern(concern())
        for invalid in ((), ("",), (" ",), "source:1", (None,), (123,), ["source:1"]):
            with self.subTest(invalid=invalid):
                with self.assertRaises((TypeError, ValueError)):
                    self.runtime.transition_concern(
                        "concern:goal",
                        ConcernState.INTENTION_CANDIDATE,
                        reason_refs=invalid,
                    )
                self.assertEqual(len(self.runtime.concern_history("concern:goal")), 1)

    def test_states_must_be_enum_instances_not_spoofed_strings(self):
        with self.assertRaises((TypeError, ValueError)):
            self.runtime.set_concern(concern(state="PRESENT"))
        self.runtime.set_concern(concern())
        with self.assertRaises((TypeError, ValueError)):
            self.runtime.transition_concern(
                "concern:goal",
                "INTENTION_CANDIDATE",
                reason_refs=("source:1",),
            )
        self.assertEqual(len(self.runtime.concern_history("concern:goal")), 1)


if __name__ == "__main__":
    unittest.main()
