import argparse
import json
import re
import sys
from pathlib import Path

SCHEMA_ID = "HC_INDEPENDENT_REVIEW_RECEIPT_V1"
ALLOWED_RESULTS = {"PASS", "CONDITIONAL_PASS", "FAIL"}
HEX40 = re.compile(r"^[0-9a-f]{40}$")

def _nonempty_string(value):
    return isinstance(value, str) and bool(value.strip())

def validate_receipt(data, expected_repository=None, expected_commit=None):
    errors = []

    if data.get("schema_id") != SCHEMA_ID:
        errors.append(f"schema_id must equal {SCHEMA_ID}")

    subject = data.get("subject")
    if not isinstance(subject, dict):
        errors.append("subject must be an object")
        subject = {}
    repository = subject.get("repository")
    commit = subject.get("commit")
    scope = subject.get("scope")
    if not _nonempty_string(repository):
        errors.append("subject.repository must be a non-empty string")
    if not isinstance(commit, str) or not HEX40.fullmatch(commit):
        errors.append("subject.commit must be a 40-character lowercase hex commit")
    if not _nonempty_string(scope):
        errors.append("subject.scope must be a non-empty string")
    if expected_repository is not None and repository != expected_repository:
        errors.append(
            f"subject.repository {repository!r} does not match expected repository {expected_repository!r}"
        )
    if expected_commit is not None and commit != expected_commit:
        errors.append(
            f"subject.commit {commit!r} does not match expected commit {expected_commit!r}"
        )

    reviewer = data.get("reviewer")
    if not isinstance(reviewer, dict):
        errors.append("reviewer must be an object")
        reviewer = {}
    for field in ("id", "role"):
        if not _nonempty_string(reviewer.get(field)):
            errors.append(f"reviewer.{field} must be a non-empty string")
    if reviewer.get("independence") != "INDEPENDENT":
        errors.append("reviewer.independence must be INDEPENDENT for this receipt type")
    if reviewer.get("shaping_ancestry") is not False:
        errors.append(
            "reviewer.shaping_ancestry must be false for an independent exact-head receipt"
        )

    if data.get("result") not in ALLOWED_RESULTS:
        errors.append("result must be PASS, CONDITIONAL_PASS, or FAIL")
    if not _nonempty_string(data.get("reviewed_at")):
        errors.append("reviewed_at must be a non-empty timestamp string")

    evidence = data.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        errors.append("evidence must be a non-empty list")
    else:
        for i, item in enumerate(evidence):
            if not isinstance(item, dict):
                errors.append(f"evidence[{i}] must be an object")
                continue
            if not _nonempty_string(item.get("kind")):
                errors.append(f"evidence[{i}].kind must be a non-empty string")
            if not _nonempty_string(item.get("reference")):
                errors.append(f"evidence[{i}].reference must be a non-empty string")

    uncertainty = data.get("remaining_uncertainty")
    if not isinstance(uncertainty, list):
        errors.append("remaining_uncertainty must be a list")

    claim_ceiling = data.get("claim_ceiling")
    if not isinstance(claim_ceiling, list) or not claim_ceiling:
        errors.append("claim_ceiling must be a non-empty list")

    return errors

def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Validate an HC independent exact-head review receipt."
    )
    parser.add_argument("receipt")
    parser.add_argument("--expected-repository")
    parser.add_argument("--expected-commit")
    args = parser.parse_args(argv)

    try:
        data = json.loads(Path(args.receipt).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"receipt: {exc}", file=sys.stderr)
        return 2

    errors = validate_receipt(
        data,
        expected_repository=args.expected_repository,
        expected_commit=args.expected_commit,
    )
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("VALID")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
