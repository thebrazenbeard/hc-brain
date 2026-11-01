"""Synthetic adversarial checks of HC concern registration and transitions.

No model, host, canonical memory, external capability, or persistent I/O.
"""

import unittest

from runtime.cognitive_core.cognitive_loop import (
    Concern,
    ConcernState,
    CognitiveRuntime,
)
from runtime.reference_kernel.hc_kernel import ReferenceKernel


def make_concern(*, state=ConcernState.PRESENT, target="concept:task", provenance=("evidence:task",), strength=0.5):
    return Concern("concern:task", target, strength, state, provenance)


class ConcernHostileTests(unittest.TestCase):
    def setUp(self):
        self.runtime = CognitiveRuntime(ReferenceKernel())

    def test_noninitial_states_cannot_be_registered_directly(self):
        for state in ConcernState:
            if state in (ConcernState.EMERGING, ConcernState.PRESENT):
                continue
            with self.subTest(state=state):
                before = self.runtime.concern_history("concern:task")
                with self.assertRaises(ValueError):
                    self.runtime.set_concern(make_concern(state=state))
                self.assertEqual(self.runtime.concern_history("concern:task"), before)

    def test_forged_state_string_fails_at_registration(self):
        with self.assertRaises(ValueError):
            self.runtime.set_concern(make_concern(state="PRESENT"))
        self.assertEqual(self.runtime.concern_history("concern:task"), ())

    def test_direct_shortcut_cannot_overwrite_valid_state(self):
        first = make_concern()
        self.runtime.set_concern(first)
        with self.assertRaises(ValueError):
            self.runtime.set_concern(make_concern(state=ConcernState.SATISFIED))
        self.assertEqual(self.runtime.concern_history("concern:task"), (first,))

    def test_direct_retarget_cannot_rewrite_concern_identity(self):
        first = make_concern()
        self.runtime.set_concern(first)
        with self.assertRaises(ValueError):
            self.runtime.set_concern(make_concern(target="concept:other"))
        self.assertEqual(self.runtime.concern_history("concern:task"), (first,))

    def test_invalid_transition_does_not_mutate_state_or_history(self):
        first = make_concern()
        self.runtime.set_concern(first)
        with self.assertRaises(ValueError):
            self.runtime.transition_concern(
                "concern:task", ConcernState.EXECUTING, reason_refs=("reason:skip",)
            )
        self.assertEqual(self.runtime.concern_history("concern:task"), (first,))

    def test_invalid_transition_reason_values_are_rejected_without_history(self):
        for refs in (("",), (" ",), (None,), (123,), ("valid", None), "raw-string"):
            with self.subTest(refs=refs):
                runtime = CognitiveRuntime(ReferenceKernel())
                first = make_concern()
                runtime.set_concern(first)
                with self.assertRaises(ValueError):
                    runtime.transition_concern(
                        "concern:task",
                        ConcernState.INTENTION_CANDIDATE,
                        reason_refs=refs,
                    )
                self.assertEqual(runtime.concern_history("concern:task"), (first,))

    def test_untyped_transition_state_does_not_masquerade_as_enum(self):
        first = make_concern()
        self.runtime.set_concern(first)
        with self.assertRaises(ValueError):
            self.runtime.transition_concern(
                "concern:task", "INTENTION_CANDIDATE", reason_refs=("reason:valid",)
            )
        self.assertEqual(self.runtime.concern_history("concern:task"), (first,))

    def test_mutable_or_string_provenance_must_not_enter_history(self):
        for provenance in (["evidence:mutable"], "evidence:plain-string"):
            with self.subTest(provenance=provenance):
                with self.assertRaises(ValueError):
                    self.runtime.set_concern(make_concern(provenance=provenance))
                self.assertEqual(self.runtime.concern_history("concern:task"), ())

    def test_forged_or_blank_identity_fails_before_mutating_history(self):
        class EqSpoof:
            def __eq__(self, _other):
                return True

            def __hash__(self):
                return hash("concern:task")

        for ident, target in (
            (EqSpoof(), "concept:task"),
            (" ", "concept:task"),
            ("concern:task", EqSpoof()),
            ("concern:task", " "),
        ):
            with self.subTest(identity=repr(ident), target=repr(target)):
                with self.assertRaises(ValueError):
                    self.runtime.set_concern(
                        Concern(ident, target, 0.5, ConcernState.PRESENT)
                    )
                self.assertEqual(self.runtime.concern_history("concern:task"), ())

    def test_valid_transition_appends_exactly_one_event(self):
        first = make_concern()
        self.runtime.set_concern(first)
        updated = self.runtime.transition_concern(
            "concern:task", ConcernState.INTENTION_CANDIDATE, reason_refs=("reason:valid",)
        )
        self.assertEqual(self.runtime.concern_history("concern:task"), (first, updated))
        self.assertEqual(updated.provenance, ("evidence:task", "reason:valid"))


if __name__ == "__main__":
    unittest.main()
