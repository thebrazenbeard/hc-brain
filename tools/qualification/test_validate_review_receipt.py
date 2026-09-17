import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tools" / "qualification" / "validate_review_receipt.py"
EXPECTED = "3d9df59b2ad8b10f2d46b4dfe67a309e2b02f207"

def receipt():
    return {
        "schema_id": "HC_INDEPENDENT_REVIEW_RECEIPT_V1",
        "subject": {
            "repository": "thebrazenbeard/hc-brain",
            "commit": EXPECTED,
            "scope": "reference-kernel authority hardening R5"
        },
        "reviewer": {
            "id": "four",
            "role": "independent-hostile-reviewer",
            "independence": "INDEPENDENT",
            "shaping_ancestry": False
        },
        "result": "PASS",
        "reviewed_at": "2026-09-17T22:30:00Z",
        "evidence": [
            {"kind": "test_run", "reference": "64/64 exact-head suite"},
            {"kind": "hostile_probe", "reference": "outcome-source capability spoof rejected"}
        ],
        "remaining_uncertainty": ["in-process capability is not cryptographic isolation"],
        "claim_ceiling": ["SOURCE_REVIEW_ONLY"]
    }

class ReviewReceiptValidatorTests(unittest.TestCase):
    def run_validator(self, data, *args):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "receipt.json"
            p.write_text(json.dumps(data), encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(SCRIPT), str(p), *args],
                text=True,
                capture_output=True,
            )

    def test_accepts_independent_receipt_for_exact_expected_head(self):
        result = self.run_validator(
            receipt(),
            "--expected-repository", "thebrazenbeard/hc-brain",
            "--expected-commit", EXPECTED,
        )
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)

    def test_rejects_stale_or_wrong_exact_head(self):
        data = receipt()
        data["subject"]["commit"] = "0" * 40
        result = self.run_validator(data, "--expected-commit", EXPECTED)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("subject.commit", result.stderr)

    def test_rejects_reviewer_with_shaping_ancestry(self):
        data = receipt()
        data["reviewer"]["shaping_ancestry"] = True
        result = self.run_validator(data)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("shaping_ancestry", result.stderr)

    def test_rejects_unknown_independence(self):
        data = receipt()
        data["reviewer"]["independence"] = "UNKNOWN"
        result = self.run_validator(data)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("independence", result.stderr)

    def test_rejects_empty_evidence(self):
        data = receipt()
        data["evidence"] = []
        result = self.run_validator(data)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("evidence", result.stderr)

if __name__ == "__main__":
    unittest.main()
