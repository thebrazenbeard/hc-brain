from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

ALLOWED_CONSISTENCY_CLASSES = {"SINGLE_WRITER_EPOCH", "QUORUM_COMMITTED", "LINEARIZABLE_REQUIRED", "CAUSALLY_ORDERED", "MERGEABLE_CONCURRENT", "LOCAL_EPHEMERAL", "READ_ONLY_REPLICA"}
ALLOWED_PARTITION_WRITE_POLICIES = {"BLOCK", "BOUNDED_ISLAND", "MERGE_CANDIDATES_ONLY", "READ_ONLY"}
ALLOWED_PARTITION_READ_POLICIES = {"CURRENT_ONLY", "LOCAL_ALLOWED", "STALE_WITH_LABEL", "READ_ONLY"}
ALLOWED_REVIEW_VERDICTS = {"PASS", "FAIL", "COMMENT", "CONDITIONAL_PASS"}
ALLOWED_INDEPENDENCE_STATES = {"INDEPENDENT_WITHIN_DECLARED_SCOPE", "MATERIALLY_AUTHORED_TARGET", "MATERIALLY_SHAPED_TARGET", "PRE_ADJUDICATED_TARGET_OR_EVIDENCE", "INDEPENDENCE_UNKNOWN"}
ALLOWED_REVIEWER_ROLES = {"PRIMARY_ARCHITECT_OR_WARDEN_REVIEW", "AUTHORIAL_SECONDARY_OR_IMPLEMENTATION_READINESS_REVIEW", "INDEPENDENT_SECONDARY_REVIEW", "HOSTILE_OR_ADVERSARIAL_REVIEW", "IMPLEMENTATION_TEST_EVIDENCE"}
ALLOWED_ATTESTATION_LOCATIONS = {"OUT_OF_SUBJECT_TREE"}
ALLOWED_ATTESTATION_SURFACES = {"PULL_REQUEST_REVIEW", "EXTERNAL_CHECK_ATTESTATION", "GOVERNED_BUS_RECEIPT"}

STATE_PROFILE_REQUIRED_FIELDS = ("family_id", "semantic_owner", "consistency_class", "protected", "continuity_bearing", "partition_write_policy", "partition_read_policy", "merge_or_reconciliation_rule", "stale_state_policy", "recovery_fence_policy", "effect_dependency_policy", "qualification_refs", "provenance", "safety_invariants", "coordination_basis", "mechanical_evidence_refs")
REVIEW_RECEIPT_REQUIRED_FIELDS = ("receipt_id", "subject_repo", "subject_head", "reviewed_scope", "reviewer_execution_subject", "reviewer_role", "independence_state", "authored_artifact_refs", "shaping_or_diagnostic_refs", "prior_adjudication_refs", "material_shaping_within_reviewed_scope", "admitted_context_refs", "verdict", "evidence_refs", "issued_at", "supersedes", "attestation_location")
ATTESTATION_OBSERVATION_REQUIRED_FIELDS = ("observed_location", "surface_type", "attestation_uri", "attestation_sha256", "subject_repo", "subject_head", "verifier_id", "verification_policy_id", "trust_root_id", "observed_at")
_COMMIT_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


def _is_nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _is_string_list(value: Any, *, allow_empty: bool = True) -> bool:
    return isinstance(value, list) and (allow_empty or bool(value)) and all(_is_nonempty_string(item) for item in value)


def _canonical_sha256(value: Any) -> str:
    canonical = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _is_aware_iso_datetime(value: Any) -> bool:
    if not _is_nonempty_string(value):
        return False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed.tzinfo is not None and parsed.utcoffset() is not None


def _trusted_identity_set(values: Iterable[str], field: str) -> tuple[set[str], list[str]]:
    errors: list[str] = []
    if isinstance(values, str):
        return set(), [f"{field} must be a collection of trusted IDs, not one string"]
    try:
        normalized = set(values)
    except TypeError:
        return set(), [f"{field} must be an iterable of trusted IDs"]
    if not normalized or not all(_is_nonempty_string(value) for value in normalized):
        errors.append(f"{field} must contain at least one non-empty trusted ID")
    return normalized, errors


def validate_state_family_profiles(document: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    profiles = document.get("profiles")
    if not isinstance(profiles, list) or not profiles:
        return ["profiles must be a non-empty list"]
    seen: set[str] = set()
    for index, profile in enumerate(profiles):
        label = f"profile[{index}]"
        if not isinstance(profile, dict):
            errors.append(f"{label} must be an object")
            continue
        for field in STATE_PROFILE_REQUIRED_FIELDS:
            if field not in profile:
                errors.append(f"{label} missing {field}")
        family_id = profile.get("family_id")
        if not _is_nonempty_string(family_id):
            errors.append(f"{label}.family_id must be non-empty")
        elif family_id in seen:
            errors.append(f"{label} duplicate family_id: {family_id}")
        else:
            seen.add(family_id)
        if not _is_nonempty_string(profile.get("semantic_owner")):
            errors.append(f"{label}.semantic_owner must be non-empty")
        if profile.get("consistency_class") not in ALLOWED_CONSISTENCY_CLASSES:
            errors.append(f"{label} unknown consistency_class: {profile.get('consistency_class')!r}")
        if not isinstance(profile.get("protected"), bool):
            errors.append(f"{label}.protected must be boolean")
        if not isinstance(profile.get("continuity_bearing"), bool):
            errors.append(f"{label}.continuity_bearing must be boolean")
        write_policy = profile.get("partition_write_policy")
        if write_policy not in ALLOWED_PARTITION_WRITE_POLICIES:
            errors.append(f"{label}.partition_write_policy is missing or unknown")
        if profile.get("partition_read_policy") not in ALLOWED_PARTITION_READ_POLICIES:
            errors.append(f"{label}.partition_read_policy is missing or unknown")
        merge_rule = profile.get("merge_or_reconciliation_rule")
        if not _is_nonempty_string(merge_rule):
            errors.append(f"{label}.merge_or_reconciliation_rule must be non-empty")
        if write_policy == "MERGE_CANDIDATES_ONLY" and not _is_nonempty_string(merge_rule):
            errors.append(f"{label} MERGE_CANDIDATES_ONLY requires reconciliation rule")
        for field in ("stale_state_policy", "effect_dependency_policy"):
            if not _is_nonempty_string(profile.get(field)):
                errors.append(f"{label}.{field} must be non-empty")
        recovery_policy = profile.get("recovery_fence_policy")
        if (profile.get("protected") or profile.get("continuity_bearing")) and not _is_nonempty_string(recovery_policy):
            errors.append(f"{label}.recovery_fence_policy required for protected/continuity-bearing family")
        elif not _is_nonempty_string(recovery_policy):
            errors.append(f"{label}.recovery_fence_policy must be non-empty")
        if not _is_string_list(profile.get("qualification_refs"), allow_empty=True):
            errors.append(f"{label}.qualification_refs must be a string list")
        if not _is_string_list(profile.get("provenance"), allow_empty=False):
            errors.append(f"{label}.provenance must be a non-empty string list")
        if not _is_string_list(profile.get("safety_invariants"), allow_empty=False):
            errors.append(f"{label}.safety_invariants must be a non-empty string list")
        if not _is_nonempty_string(profile.get("coordination_basis")):
            errors.append(f"{label}.coordination_basis must be non-empty")
        if not _is_string_list(profile.get("mechanical_evidence_refs"), allow_empty=False):
            errors.append(f"{label}.mechanical_evidence_refs must be a non-empty string list")
    return errors


def validate_review_receipt(
    receipt: dict[str, Any],
    *,
    expected_repo: str,
    expected_head: str,
    attestation_observation: dict[str, Any],
    trusted_verifier_ids: Iterable[str],
    trusted_policy_ids: Iterable[str],
    trusted_root_ids: Iterable[str],
) -> list[str]:
    errors: list[str] = []
    if not isinstance(receipt, dict):
        return ["receipt must be an object"]

    for field in REVIEW_RECEIPT_REQUIRED_FIELDS:
        if field not in receipt:
            errors.append(f"receipt missing {field}")
    if receipt.get("subject_repo") != expected_repo:
        errors.append("receipt subject_repo does not match expected_repo")
    subject_head = receipt.get("subject_head")
    if subject_head != expected_head:
        errors.append("receipt subject_head does not match expected_head")
    if not isinstance(subject_head, str) or not _COMMIT_SHA_RE.fullmatch(subject_head):
        errors.append("receipt subject_head must be a 40-character hexadecimal commit SHA")
    if not _is_string_list(receipt.get("reviewed_scope"), allow_empty=False):
        errors.append("receipt reviewed_scope must be a non-empty string list")
    if not _is_nonempty_string(receipt.get("reviewer_execution_subject")):
        errors.append("receipt reviewer_execution_subject must be non-empty")
    if receipt.get("reviewer_role") not in ALLOWED_REVIEWER_ROLES:
        errors.append("receipt reviewer_role is unknown")
    independence_state = receipt.get("independence_state")
    if independence_state not in ALLOWED_INDEPENDENCE_STATES:
        errors.append("receipt independence_state is unknown")
    for field in ("authored_artifact_refs", "shaping_or_diagnostic_refs", "prior_adjudication_refs", "admitted_context_refs", "evidence_refs", "supersedes"):
        if not _is_string_list(receipt.get(field), allow_empty=True):
            errors.append(f"receipt {field} must be a string list")
    material_overlap = receipt.get("material_shaping_within_reviewed_scope")
    if not isinstance(material_overlap, bool):
        errors.append("receipt material_shaping_within_reviewed_scope must be boolean")
    if receipt.get("verdict") not in ALLOWED_REVIEW_VERDICTS:
        errors.append("receipt verdict is unknown")
    if not _is_aware_iso_datetime(receipt.get("issued_at")):
        errors.append("receipt issued_at must be an offset-aware ISO datetime")
    if independence_state == "INDEPENDENT_WITHIN_DECLARED_SCOPE" and material_overlap is True:
        errors.append("receipt independence claim conflicts with material shaping within reviewed scope")

    declared_location = receipt.get("attestation_location")
    if declared_location not in ALLOWED_ATTESTATION_LOCATIONS:
        errors.append("receipt declared attestation location must be out of subject tree")

    trusted_verifiers, trust_errors = _trusted_identity_set(trusted_verifier_ids, "trusted_verifier_ids")
    errors.extend(trust_errors)
    trusted_policies, trust_errors = _trusted_identity_set(trusted_policy_ids, "trusted_policy_ids")
    errors.extend(trust_errors)
    trusted_roots, trust_errors = _trusted_identity_set(trusted_root_ids, "trusted_root_ids")
    errors.extend(trust_errors)

    if not isinstance(attestation_observation, dict):
        errors.append("attestation_observation must be a trusted external observation object")
    else:
        for field in ATTESTATION_OBSERVATION_REQUIRED_FIELDS:
            if field not in attestation_observation:
                errors.append(f"attestation_observation missing {field}")

        observed_location = attestation_observation.get("observed_location")
        if observed_location not in ALLOWED_ATTESTATION_LOCATIONS:
            errors.append("observed attestation location must be out of subject tree")
        if declared_location != observed_location:
            errors.append("receipt declared attestation location does not match observed attestation location")

        surface_type = attestation_observation.get("surface_type")
        if surface_type not in ALLOWED_ATTESTATION_SURFACES:
            errors.append("attestation_observation surface_type is unknown")
        if not _is_nonempty_string(attestation_observation.get("attestation_uri")):
            errors.append("attestation_observation attestation_uri must be non-empty")

        observed_digest = attestation_observation.get("attestation_sha256")
        if not isinstance(observed_digest, str) or not _SHA256_RE.fullmatch(observed_digest):
            errors.append("attestation_observation attestation_sha256 must be a 64-character hexadecimal SHA-256")
        elif observed_digest != _canonical_sha256(receipt):
            errors.append("attestation_observation attestation_sha256 does not bind the exact receipt")

        if attestation_observation.get("subject_repo") != expected_repo:
            errors.append("attestation observation subject_repo does not match expected_repo")
        observation_head = attestation_observation.get("subject_head")
        if observation_head != expected_head:
            errors.append("attestation observation subject_head does not match expected_head")
        if not isinstance(observation_head, str) or not _COMMIT_SHA_RE.fullmatch(observation_head):
            errors.append("attestation observation subject_head must be a 40-character hexadecimal commit SHA")

        verifier_id = attestation_observation.get("verifier_id")
        if not _is_nonempty_string(verifier_id):
            errors.append("attestation_observation verifier_id must be non-empty")
        elif verifier_id not in trusted_verifiers:
            errors.append("attestation_observation verifier_id is not trusted")

        policy_id = attestation_observation.get("verification_policy_id")
        if not _is_nonempty_string(policy_id):
            errors.append("attestation_observation verification_policy_id must be non-empty")
        elif policy_id not in trusted_policies:
            errors.append("attestation_observation verification_policy_id is not trusted")

        trust_root_id = attestation_observation.get("trust_root_id")
        if not _is_nonempty_string(trust_root_id):
            errors.append("attestation_observation trust_root_id must be non-empty")
        elif trust_root_id not in trusted_roots:
            errors.append("attestation_observation trust_root_id is not trusted")

        if not _is_aware_iso_datetime(attestation_observation.get("observed_at")):
            errors.append("attestation_observation observed_at must be an offset-aware ISO datetime")

    if "merge_authority" in receipt:
        errors.append("review receipt cannot grant or encode merge authority")
    return errors


def _load_json_compatible_yaml(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path} must contain JSON-compatible YAML: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{path} root must be an object")
    return value


def _validate_file_references(document: dict[str, Any], *, root: Path, source: Path) -> list[str]:
    errors: list[str] = []
    refs: list[str] = []
    if isinstance(document.get("references"), list):
        refs.extend(document["references"])
    for profile in document.get("profiles", []) if isinstance(document.get("profiles"), list) else []:
        if isinstance(profile, dict):
            for field in ("qualification_refs", "provenance", "mechanical_evidence_refs"):
                values = profile.get(field)
                if isinstance(values, list):
                    refs.extend(values)
    for ref in refs:
        if isinstance(ref, str) and "://" not in ref and not (root / ref).is_file():
            errors.append(f"{source.relative_to(root)} references missing file: {ref}")
    return errors


def validate_repository(root: Path) -> list[str]:
    errors: list[str] = []
    machine_paths = (
        root / "specs/HC_STATE_FAMILY_CONSISTENCY_POLICY_V1.yaml",
        root / "specs/HC_STATE_FAMILY_CONSISTENCY_REGISTRY_V1.yaml",
        root / "specs/HC_REVIEW_RECEIPT_V1.yaml",
    )
    required_paths = (
        root / "docs/architecture/CAUSAL_AUTHORITY_RECOVERY_HARDENING_V2.md",
        root / "docs/architecture/STATE_FAMILY_CONSISTENCY_AND_CAUSAL_FRONTIER.md",
        *machine_paths,
        root / "runtime/reference_kernel/governed_kernel_v2.py",
        root / "runtime/reference_kernel/test_vera_adversarial_kernel_v2.py",
    )
    for path in required_paths:
        if not path.is_file():
            errors.append(f"missing required V2 path: {path.relative_to(root)}")
    for path in machine_paths:
        if not path.is_file():
            continue
        try:
            document = _load_json_compatible_yaml(path)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        for field in ("schema_version", "status", "scope"):
            if not _is_nonempty_string(document.get(field)):
                errors.append(f"{path.relative_to(root)} missing {field}")
        if path.name == "HC_STATE_FAMILY_CONSISTENCY_REGISTRY_V1.yaml":
            errors.extend(f"{path.name}: {error}" for error in validate_state_family_profiles(document))
        errors.extend(_validate_file_references(document, root=root, source=path))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    errors = validate_repository(Path(args.root).resolve())
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("HC architecture conformance: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
