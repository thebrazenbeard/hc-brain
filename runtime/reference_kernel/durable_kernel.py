from __future__ import annotations

from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
from typing import Any

from hc_kernel import (
    AuthorityGrant, CurrentMemory, EffectCandidate, EffectReceipt, EffectState,
    EpistemicClass, EvidenceRecord, MemoryRecord, ReferenceKernel, RoutedEvent,
)

JOURNAL_SCHEMA_VERSION=2
GENESIS_HASH="0"*64
VALID_OPEN_MODES={"recover","inspect"}

class JournalIntegrityError(RuntimeError): pass
class ReadOnlyInspectionError(RuntimeError): pass

def _iso(value: datetime)->str:
    if value.tzinfo is None or value.utcoffset() is None: raise ValueError("journaled datetimes must be timezone-aware")
    return value.isoformat()

def _parse_dt(value:str)->datetime:
    parsed=datetime.fromisoformat(value)
    if parsed.tzinfo is None or parsed.utcoffset() is None: raise JournalIntegrityError("journal contains timezone-naive datetime")
    return parsed

class JournaledCurrentMemory(CurrentMemory):
    def __init__(self,owner): super().__init__(); self._owner=owner
    def append(self,*,logical_key,payload,epistemic_class,supersedes=(),source_refs=()):
        self._owner._ensure_writable(); self._owner._ensure_jsonable(payload)
        record=super().append(logical_key=logical_key,payload=payload,epistemic_class=epistemic_class,supersedes=supersedes,source_refs=source_refs)
        try: self._owner._record("MEMORY_RECORD_UPSERT",self._owner._memory_data(record))
        except Exception:
            self._records.pop(record.record_id,None); raise
        return record

class DurableReferenceKernel(ReferenceKernel):
    def __init__(self,journal_path:str|os.PathLike[str],*,mode:str="recover",clock=None):
        if mode not in VALID_OPEN_MODES: raise ValueError(f"mode must be one of {sorted(VALID_OPEN_MODES)}")
        super().__init__(clock=clock)
        self.journal_path=Path(journal_path); self.open_mode=mode; self.memory=JournaledCurrentMemory(self); self._next_seq=0; self._last_hash=GENESIS_HASH
        had_events=self._load_existing()
        if had_events and mode=="recover": self._advance_recovery_epoch()

    @property
    def read_only(self): return self.open_mode=="inspect"
    def _ensure_writable(self):
        if self.read_only: raise ReadOnlyInspectionError("inspect mode is read-only; reopen in recover mode to mutate state")
    @staticmethod
    def _ensure_jsonable(payload):
        try: json.dumps(payload,ensure_ascii=False,sort_keys=True,allow_nan=False)
        except (TypeError,ValueError) as exc: raise ValueError("durable reference-kernel payload must be JSON-serializable") from exc
    @staticmethod
    def _canonical_bytes(body):
        return json.dumps(body,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False).encode("utf-8")
    def _record(self,event_type,data):
        self._ensure_writable(); self._ensure_jsonable(data)
        body={"schema_version":JOURNAL_SCHEMA_VERSION,"seq":self._next_seq,"event_type":event_type,"epoch":self.epoch,"data":data,"prev_hash":self._last_hash}
        digest=hashlib.sha256(self._canonical_bytes(body)).hexdigest(); envelope=dict(body); envelope["entry_hash"]=digest
        self.journal_path.parent.mkdir(parents=True,exist_ok=True)
        line=json.dumps(envelope,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False)
        with self.journal_path.open("a",encoding="utf-8",newline="\n") as h:
            h.write(line+"\n"); h.flush(); os.fsync(h.fileno())
        self._last_hash=digest; self._next_seq+=1

    def _load_existing(self):
        if not self.journal_path.exists(): return False
        text=self.journal_path.read_text(encoding="utf-8")
        if not text: return False
        expected_seq=0; expected_prev=GENESIS_HASH
        for ln,raw in enumerate(text.splitlines(),start=1):
            try: env=json.loads(raw)
            except json.JSONDecodeError as exc: raise JournalIntegrityError(f"invalid JSON at journal line {ln}") from exc
            required={"schema_version","seq","event_type","epoch","data","prev_hash","entry_hash"}
            if set(env)!=required: raise JournalIntegrityError(f"journal line {ln} has unexpected/missing fields")
            if env["schema_version"]!=JOURNAL_SCHEMA_VERSION: raise JournalIntegrityError(f"unsupported journal schema at line {ln}: {env['schema_version']!r}")
            if not isinstance(env["epoch"],int) or env["epoch"]<0: raise JournalIntegrityError(f"invalid event epoch at journal line {ln}")
            if env["seq"]!=expected_seq: raise JournalIntegrityError(f"journal sequence discontinuity at line {ln}")
            if env["prev_hash"]!=expected_prev: raise JournalIntegrityError(f"journal hash-chain predecessor mismatch at line {ln}")
            body={k:env[k] for k in required if k!="entry_hash"}; digest=hashlib.sha256(self._canonical_bytes(body)).hexdigest()
            if digest!=env["entry_hash"]: raise JournalIntegrityError(f"journal entry hash mismatch at line {ln}")
            self._apply_event(event_type=env["event_type"],data=env["data"],event_epoch=env["epoch"])
            expected_prev=digest; expected_seq+=1
        self._last_hash=expected_prev; self._next_seq=expected_seq; return True

    def _apply_event(self,*,event_type,data,event_epoch):
        if event_type=="EPOCH_SET":
            new_epoch=data.get("epoch")
            if not isinstance(new_epoch,int): raise JournalIntegrityError("epoch transition is not an integer")
            if new_epoch!=event_epoch: raise JournalIntegrityError("epoch envelope/data mismatch")
            if new_epoch!=self.epoch+1: raise JournalIntegrityError("epoch transition is not contiguous")
            self.epoch=new_epoch; return
        if event_epoch!=self.epoch: raise JournalIntegrityError("non-transition journal event does not match current replay epoch")
        if event_type=="EVIDENCE_RECORD_UPSERT":
            evidence_id=data["evidence_id"]
            if evidence_id in self.evidence: raise JournalIntegrityError("evidence identity rewritten in append journal")
            ec=EpistemicClass(data["epistemic_class"]); parents=tuple(data["parent_ids"])
            if ec==EpistemicClass.OBSERVATION:
                if parents: raise JournalIntegrityError("raw observation cannot replay with causal evidence parents")
            else:
                if not parents: raise JournalIntegrityError("derived/inferred/predicted evidence has no causal parent")
                missing=[p for p in parents if p not in self.evidence]
                if missing: raise JournalIntegrityError(f"evidence replay references unknown parents: {missing}")
            effect_action_id=data.get("effect_action_id")
            if effect_action_id is not None and effect_action_id not in self.effect_receipts: raise JournalIntegrityError("effect-linked observation references unknown requested effect")
            r=EvidenceRecord(evidence_id=evidence_id,producer=data["producer"],epistemic_class=ec,payload=data["payload"],event_time=_parse_dt(data["event_time"]),record_time=_parse_dt(data["record_time"]),parent_ids=parents,source_refs=tuple(data["source_refs"]),influence_roles=tuple(data["influence_roles"]),effect_action_id=effect_action_id)
            self.evidence[r.evidence_id]=r; return
        if event_type=="ROUTED_EVENT_UPSERT":
            eid=data["event_id"]
            if eid in self.routed_events: raise JournalIntegrityError("routed event identity rewritten in append journal")
            ev=RoutedEvent(event_id=eid,source=data["source"],audience=data["audience"],payload=data["payload"],priority=int(data["priority"]),parent_ids=tuple(data["parent_ids"]),authority_ref=data.get("authority_ref")); self.routed_events[eid]=ev; return
        if event_type=="ROUTED_EVENT_INCORPORATED":
            eid=data["event_id"]
            if eid not in self.routed_events: raise JournalIntegrityError("incorporation references unknown routed event")
            self.incorporated_event_ids.add(eid); return
        if event_type=="MEMORY_RECORD_UPSERT":
            rid=data["record_id"]
            if rid in self.memory._records: raise JournalIntegrityError("memory record identity rewritten in append journal")
            r=MemoryRecord(record_id=rid,logical_key=tuple(data["logical_key"]),payload=data["payload"],epistemic_class=EpistemicClass(data["epistemic_class"]),supersedes=tuple(data["supersedes"]),source_refs=tuple(data["source_refs"]))
            for pred in r.supersedes:
                prior=self.memory._records.get(pred)
                if prior is None: raise JournalIntegrityError("memory supersession references unknown record")
                if prior.logical_key!=r.logical_key: raise JournalIntegrityError("journaled supersession crosses logical scope")
            self.memory._records[r.record_id]=r; return
        if event_type=="AUTHORITY_GRANT_UPSERT":
            basis=tuple(data["basis_refs"])
            if not basis: raise JournalIntegrityError("authority grant has no explicit basis")
            vf=_parse_dt(data["valid_from"]); ex=_parse_dt(data["expires_at"])
            if ex<=vf: raise JournalIntegrityError("authority grant has invalid validity interval")
            issued=int(data["issued_epoch"])
            if issued<0 or issued>event_epoch: raise JournalIntegrityError("authority grant has impossible issued epoch")
            revoked=_parse_dt(data["revoked_at"]) if data.get("revoked_at") is not None else None
            g=AuthorityGrant(grant_id=data["grant_id"],grantor=data["grantor"],grantee=data["grantee"],action_scope=data["action_scope"],target_scope=data["target_scope"],basis_refs=basis,provenance=tuple(data["provenance"]),issued_epoch=issued,valid_from=vf,expires_at=ex,revoked_at=revoked)
            prior=self.authority_grants.get(g.grant_id)
            if prior is not None:
                old=(prior.grantor,prior.grantee,prior.action_scope,prior.target_scope,prior.basis_refs,prior.provenance,prior.issued_epoch,prior.valid_from,prior.expires_at)
                new=(g.grantor,g.grantee,g.action_scope,g.target_scope,g.basis_refs,g.provenance,g.issued_epoch,g.valid_from,g.expires_at)
                if old!=new: raise JournalIntegrityError("authority upsert rewrites immutable grant semantics")
                if prior.revoked_at is not None and g.revoked_at!=prior.revoked_at: raise JournalIntegrityError("revocation history was rewritten")
                if prior.revoked_at is None and g.revoked_at is None: raise JournalIntegrityError("authority upsert makes no valid state transition")
            self.authority_grants[g.grant_id]=g; return
        if event_type=="EFFECT_RECEIPT_UPSERT":
            r=EffectReceipt(action_id=data["action_id"],state=EffectState(data["state"]),reason=data["reason"],epoch=int(data["epoch"]),authority_grant_id=data.get("authority_grant_id"),candidate_fingerprint=data.get("candidate_fingerprint"),dispatch_attempts=int(data["dispatch_attempts"]),confirmation_evidence_id=data.get("confirmation_evidence_id"))
            if r.epoch<0 or r.epoch>event_epoch: raise JournalIntegrityError("effect receipt has impossible originating epoch")
            prior=self.effect_receipts.get(r.action_id)
            if prior is None:
                if r.state not in {EffectState.BLOCKED,EffectState.REQUESTED}: raise JournalIntegrityError("effect receipt begins in impossible state")
                if r.candidate_fingerprint is None: raise JournalIntegrityError("effect receipt has no candidate semantic binding")
                if r.state==EffectState.REQUESTED:
                    if r.dispatch_attempts!=1: raise JournalIntegrityError("requested effect must have exactly one request/dispatch handoff marker")
                    if r.authority_grant_id is None: raise JournalIntegrityError("requested effect has no authority reference")
                    if r.authority_grant_id not in self.authority_grants: raise JournalIntegrityError("requested effect references unknown grant")
                elif r.dispatch_attempts!=0: raise JournalIntegrityError("blocked effect cannot claim dispatch attempt")
            else:
                allowed={EffectState.REQUESTED:{EffectState.CONFIRMED,EffectState.FAILED_CONFIRMED,EffectState.UNRESOLVED_AFTER_RESTART},EffectState.UNRESOLVED_AFTER_RESTART:{EffectState.CONFIRMED,EffectState.FAILED_CONFIRMED}}
                if r.state not in allowed.get(prior.state,set()): raise JournalIntegrityError(f"invalid effect transition {prior.state.value}->{r.state.value}")
                if r.authority_grant_id!=prior.authority_grant_id: raise JournalIntegrityError("effect transition rewrites authority reference")
                if r.candidate_fingerprint!=prior.candidate_fingerprint: raise JournalIntegrityError("effect transition rewrites candidate semantic binding")
                if r.epoch!=prior.epoch: raise JournalIntegrityError("effect transition rewrites originating epoch")
                if r.dispatch_attempts!=prior.dispatch_attempts: raise JournalIntegrityError("effect transition rewrites attempt count")
            if r.state in {EffectState.CONFIRMED,EffectState.FAILED_CONFIRMED}:
                evidence_id=r.confirmation_evidence_id
                if evidence_id is None: raise JournalIntegrityError("confirmed effect has no outcome evidence")
                ev=self.evidence.get(evidence_id)
                if ev is None: raise JournalIntegrityError("confirmed effect references unknown evidence")
                if ev.epistemic_class!=EpistemicClass.OBSERVATION: raise JournalIntegrityError("confirmed effect is not based on observation")
                if ev.effect_action_id!=r.action_id: raise JournalIntegrityError("confirmed effect evidence is not bound to the action")
            elif r.confirmation_evidence_id is not None: raise JournalIntegrityError("non-confirmed effect unexpectedly carries confirmation evidence")
            self.effect_receipts[r.action_id]=r; return
        raise JournalIntegrityError(f"unknown journal event type: {event_type}")

    @staticmethod
    def _evidence_data(r): return {"evidence_id":r.evidence_id,"producer":r.producer,"epistemic_class":r.epistemic_class.value,"payload":r.payload,"event_time":_iso(r.event_time),"record_time":_iso(r.record_time),"parent_ids":list(r.parent_ids),"source_refs":list(r.source_refs),"influence_roles":list(r.influence_roles),"effect_action_id":r.effect_action_id}
    @staticmethod
    def _route_data(e): return {"event_id":e.event_id,"source":e.source,"audience":e.audience,"payload":e.payload,"priority":e.priority,"parent_ids":list(e.parent_ids),"authority_ref":e.authority_ref}
    @staticmethod
    def _memory_data(r): return {"record_id":r.record_id,"logical_key":list(r.logical_key),"payload":r.payload,"epistemic_class":r.epistemic_class.value,"supersedes":list(r.supersedes),"source_refs":list(r.source_refs)}
    @staticmethod
    def _grant_data(g): return {"grant_id":g.grant_id,"grantor":g.grantor,"grantee":g.grantee,"action_scope":g.action_scope,"target_scope":g.target_scope,"basis_refs":list(g.basis_refs),"provenance":list(g.provenance),"issued_epoch":g.issued_epoch,"valid_from":_iso(g.valid_from),"expires_at":_iso(g.expires_at),"revoked_at":_iso(g.revoked_at) if g.revoked_at else None}
    @staticmethod
    def _receipt_data(r): return {"action_id":r.action_id,"state":r.state.value,"reason":r.reason,"epoch":r.epoch,"authority_grant_id":r.authority_grant_id,"candidate_fingerprint":r.candidate_fingerprint,"dispatch_attempts":r.dispatch_attempts,"confirmation_evidence_id":r.confirmation_evidence_id}

    def observe(self,**kwargs):
        self._ensure_writable(); self._ensure_jsonable(kwargs.get("payload")); r=super().observe(**kwargs)
        try: self._record("EVIDENCE_RECORD_UPSERT",self._evidence_data(r))
        except Exception: self.evidence.pop(r.evidence_id,None); raise
        return r
    def derive(self,**kwargs):
        self._ensure_writable(); self._ensure_jsonable(kwargs.get("payload")); r=super().derive(**kwargs)
        try: self._record("EVIDENCE_RECORD_UPSERT",self._evidence_data(r))
        except Exception: self.evidence.pop(r.evidence_id,None); raise
        return r
    def route(self,**kwargs):
        self._ensure_writable(); self._ensure_jsonable(kwargs.get("payload")); e=super().route(**kwargs)
        try: self._record("ROUTED_EVENT_UPSERT",self._route_data(e))
        except Exception: self.routed_events.pop(e.event_id,None); raise
        return e
    def incorporate_routed_event(self,event_id):
        self._ensure_writable(); already=event_id in self.incorporated_event_ids; super().incorporate_routed_event(event_id)
        if already: return
        try: self._record("ROUTED_EVENT_INCORPORATED",{"event_id":event_id})
        except Exception: self.incorporated_event_ids.discard(event_id); raise
    def register_grant(self,**kwargs):
        self._ensure_writable(); g=super().register_grant(**kwargs)
        try: self._record("AUTHORITY_GRANT_UPSERT",self._grant_data(g))
        except Exception: self.authority_grants.pop(g.grant_id,None); raise
        return g
    def revoke_grant(self,grant_id,**kwargs):
        self._ensure_writable(); g=self.authority_grants[grant_id]; previous=g.revoked_at; super().revoke_grant(grant_id,**kwargs)
        try: self._record("AUTHORITY_GRANT_UPSERT",self._grant_data(g))
        except Exception: g.revoked_at=previous; raise
    def request_effect(self,candidate:EffectCandidate):
        self._ensure_writable(); existed=candidate.action_id in self.effect_receipts; r=super().request_effect(candidate)
        if existed: return r
        try: self._record("EFFECT_RECEIPT_UPSERT",self._receipt_data(r))
        except Exception: self.effect_receipts.pop(candidate.action_id,None); raise
        return r
    def confirm_effect(self,action_id,**kwargs):
        self._ensure_writable(); r=self.effect_receipts[action_id]; previous=(r.state,r.reason,r.confirmation_evidence_id); result=super().confirm_effect(action_id,**kwargs)
        try: self._record("EFFECT_RECEIPT_UPSERT",self._receipt_data(result))
        except Exception: r.state,r.reason,r.confirmation_evidence_id=previous; raise
        return result
    def reconcile_after_restart(self,action_id,**kwargs):
        self._ensure_writable(); r=self.effect_receipts[action_id]; previous=(r.state,r.reason,r.confirmation_evidence_id); result=super().reconcile_after_restart(action_id,**kwargs)
        if previous==(result.state,result.reason,result.confirmation_evidence_id): return result
        try: self._record("EFFECT_RECEIPT_UPSERT",self._receipt_data(result))
        except Exception: r.state,r.reason,r.confirmation_evidence_id=previous; raise
        return result
    def _advance_recovery_epoch(self):
        self._ensure_writable(); prior=self.epoch; self.epoch+=1
        try: self._record("EPOCH_SET",{"epoch":self.epoch})
        except Exception: self.epoch=prior; raise
        for r in list(self.effect_receipts.values()):
            if r.state==EffectState.REQUESTED:
                old=(r.state,r.reason); r.state=EffectState.UNRESOLVED_AFTER_RESTART; r.reason="OUTCOME_REQUIRES_RECONCILIATION"
                try: self._record("EFFECT_RECEIPT_UPSERT",self._receipt_data(r))
                except Exception: r.state,r.reason=old; raise
        return self.epoch
    def restart(self): return self._advance_recovery_epoch()
