from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from enum import Enum
from typing import Any, Iterable, Tuple

from runtime.reference_kernel.hc_kernel import EpistemicClass, ReferenceKernel


def _strings(values: Iterable[str], field: str) -> Tuple[str, ...]:
    result = tuple(values)
    if any(not isinstance(value, str) or not value for value in result):
        raise ValueError(f"{field} must contain non-empty strings")
    return result


def _canonical_copy(payload: Any) -> tuple[Any, str, int]:
    try:
        encoded = json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise ValueError("memory payload must be canonically JSON-serializable") from exc
    return json.loads(encoded.decode("utf-8")), hashlib.sha256(encoded).hexdigest(), len(encoded)


class DurabilityClass(str, Enum):
    HC_INTERNAL = "HC_INTERNAL"
    HC_DISTRIBUTED_CONSTITUENT = "HC_DISTRIBUTED_CONSTITUENT"
    EXTERNAL_REPLICA = "EXTERNAL_REPLICA"
    EXTERNAL_ARCHIVE = "EXTERNAL_ARCHIVE"


class MemoryClass(str, Enum):
    EPISODIC = "EPISODIC"
    SEMANTIC = "SEMANTIC"
    PROCEDURAL = "PROCEDURAL"
    COMMITMENT = "COMMITMENT"
    AUTOBIOGRAPHICAL = "AUTOBIOGRAPHICAL"
    SOURCE_ARCHIVE = "SOURCE_ARCHIVE"
    UNRESOLVED = "UNRESOLVED"


class MemoryLifecycle(str, Enum):
    DURABLE = "DURABLE"
    CONTRADICTED = "CONTRADICTED"
    SUPERSEDED = "SUPERSEDED"
    INHIBITED = "INHIBITED"
    ARCHIVED = "ARCHIVED"


@dataclass(frozen=True)
class DurableMemoryRecord:
    memory_id: str
    memory_class: MemoryClass
    payload: Any
    source_evidence_ids: Tuple[str, ...]
    source_memory_ids: Tuple[str, ...]
    basis_refs: Tuple[str, ...]
    durability: DurabilityClass
    privacy_scopes: Tuple[str, ...]
    content_digest: str
    byte_length: int
    readback_verified: bool
    lifecycle: MemoryLifecycle = MemoryLifecycle.DURABLE


@dataclass(frozen=True)
class RetrievalCandidate:
    retrieval_id: str
    memory_id: str
    payload: Any
    memory_class: MemoryClass
    source_evidence_ids: Tuple[str, ...]
    purpose: str
    access_scope: str | None
    status: str = "RETRIEVAL_CANDIDATE"
    admitted_as_true: bool = False
    current: bool = False


@dataclass(frozen=True)
class MemoryConflict:
    conflict_id: str
    memory_ids: Tuple[str, str]
    basis_refs: Tuple[str, ...]
    status: str = "UNRESOLVED_CONTRADICTION"


class DeepMemoryRuntime:
    """HC-owned durable memory reference slice.

    Durable admission, retrieval, and consolidation remain separate from current
    memory projection and semantic truth.
    """

    INTERNAL_DURABILITY = {
        DurabilityClass.HC_INTERNAL,
        DurabilityClass.HC_DISTRIBUTED_CONSTITUENT,
    }

    def __init__(self, kernel: ReferenceKernel) -> None:
        self.kernel = kernel
        self.memories: dict[str, DurableMemoryRecord] = {}
        self.conflicts: dict[str, MemoryConflict] = {}
        self._serial = 0

    def _id(self, prefix: str) -> str:
        self._serial += 1
        return f"{prefix}:{self._serial}"

    def _evidence_ids(self, values: Iterable[str]) -> Tuple[str, ...]:
        ids = _strings(values, "source_evidence_ids")
        if not ids:
            raise ValueError("durable memory requires source evidence")
        missing = [eid for eid in ids if eid not in self.kernel.evidence]
        if missing:
            raise ValueError(f"unknown source evidence: {missing}")
        return ids

    def admit(
        self,
        *,
        memory_id: str,
        memory_class: MemoryClass,
        payload: Any,
        source_evidence_ids: Iterable[str],
        basis_refs: Iterable[str],
        durability: DurabilityClass,
        essential: bool = True,
        privacy_scopes: Iterable[str] = (),
        require_observed_episode: bool = False,
        source_memory_ids: Iterable[str] = (),
    ) -> DurableMemoryRecord:
        if not memory_id:
            raise ValueError("memory_id is required")
        if memory_id in self.memories:
            raise ValueError("duplicate memory_id")
        sources = self._evidence_ids(source_evidence_ids)
        basis = _strings(basis_refs, "basis_refs")
        if not basis:
            raise ValueError("durable-memory admission requires basis_refs")
        privacy = _strings(privacy_scopes, "privacy_scopes")
        parent_memories = _strings(source_memory_ids, "source_memory_ids")
        missing_memories = [mid for mid in parent_memories if mid not in self.memories]
        if missing_memories:
            raise ValueError(f"unknown source memories: {missing_memories}")
        if essential and durability not in self.INTERNAL_DURABILITY:
            raise ValueError(
                "essential durable memory requires HC-internal or distributed-constituent durability"
            )
        if require_observed_episode:
            non_observed = [
                eid for eid in sources
                if self.kernel.evidence[eid].epistemic_class != EpistemicClass.OBSERVATION
            ]
            if non_observed:
                raise ValueError(
                    "observed episodic admission cannot be sourced from predicted/derived state"
                )
        frozen_payload, digest, byte_length = _canonical_copy(payload)
        record = DurableMemoryRecord(
            memory_id=memory_id,
            memory_class=memory_class,
            payload=frozen_payload,
            source_evidence_ids=sources,
            source_memory_ids=parent_memories,
            basis_refs=basis,
            durability=durability,
            privacy_scopes=privacy,
            content_digest=digest,
            byte_length=byte_length,
            readback_verified=durability in self.INTERNAL_DURABILITY,
        )
        self.memories[memory_id] = record
        return record

    def retrieve(
        self,
        memory_id: str,
        *,
        purpose: str,
        access_scope: str | None = None,
    ) -> RetrievalCandidate:
        record = self.memories.get(memory_id)
        if record is None:
            raise ValueError("unknown memory")
        if not purpose:
            raise ValueError("retrieval purpose is required")
        if record.privacy_scopes:
            if access_scope is None or access_scope not in record.privacy_scopes:
                raise PermissionError("retrieval scope is not eligible for this memory")
        return RetrievalCandidate(
            retrieval_id=self._id("retrieval"),
            memory_id=record.memory_id,
            payload=_canonical_copy(record.payload)[0],
            memory_class=record.memory_class,
            source_evidence_ids=record.source_evidence_ids,
            purpose=purpose,
            access_scope=access_scope,
        )

    def consolidate(
        self,
        *,
        memory_id: str,
        memory_class: MemoryClass,
        payload: Any,
        source_memory_ids: Iterable[str],
        basis_refs: Iterable[str],
        durability: DurabilityClass = DurabilityClass.HC_INTERNAL,
        privacy_scopes: Iterable[str] = (),
    ) -> DurableMemoryRecord:
        source_ids = _strings(source_memory_ids, "source_memory_ids")
        if len(source_ids) < 2:
            raise ValueError("consolidation requires at least two source memories")
        sources = []
        for memory_id_source in source_ids:
            record = self.memories.get(memory_id_source)
            if record is None:
                raise ValueError(f"unknown source memory: {memory_id_source}")
            sources.extend(record.source_evidence_ids)
        return self.admit(
            memory_id=memory_id,
            memory_class=memory_class,
            payload=payload,
            source_evidence_ids=tuple(dict.fromkeys(sources)),
            source_memory_ids=source_ids,
            basis_refs=basis_refs,
            durability=durability,
            privacy_scopes=privacy_scopes,
        )

    def record_contradiction(
        self,
        first_memory_id: str,
        second_memory_id: str,
        *,
        basis_refs: Iterable[str],
    ) -> MemoryConflict:
        if first_memory_id == second_memory_id:
            raise ValueError("a memory cannot contradict itself")
        if first_memory_id not in self.memories or second_memory_id not in self.memories:
            raise ValueError("contradiction requires known memory records")
        basis = _strings(basis_refs, "basis_refs")
        if not basis:
            raise ValueError("contradiction record requires basis_refs")
        conflict = MemoryConflict(
            conflict_id=self._id("memory-conflict"),
            memory_ids=(first_memory_id, second_memory_id),
            basis_refs=basis,
        )
        self.conflicts[conflict.conflict_id] = conflict
        return conflict
