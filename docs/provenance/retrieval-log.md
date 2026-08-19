# Retrieval Log

## 2026-08-19 recovery pass

This log records attempts, retries, alternate routes, and bounded failures. A failed call is not treated as evidence that the target does not exist.

| Target | Route | Result | Retry or alternate | Final classification |
|---|---|---|---|---|
| Current GitHub repository | GitHub repository metadata | Success | README, initial commit, permissions, and branch search independently checked | Available |
| Existing HC-1R branch | GitHub branch search | No matching branch | Clean branch created from `main`; creation confirmed | Newly created |
| Repository clone | HTTPS Git through the bundled local client | Failed because the local Git installation lacked the HTTPS remote helper | GitHub repository API/connector used to fetch and write repository objects instead | Local clone route unavailable; repository route available |
| Project-local Noöplex sources | Recursive file listing and targeted text search under synced project `sources/` | No Noöplex or HC document found | Current ChatGPT conversation readback used as alternate | Not present in current project mirror |
| Noöplex PDF attachment | Recent conversation readback | Attachment existence and name confirmed, contents omitted by the interface | Paginated readback, local source search, and task index inspection attempted | Artifact bytes unavailable; indirect readback available |
| Archived conversation | Readback of current conversation's prior recovery report | Archived locator title and cited descriptions recovered indirectly | Older-page readback and current task index inspection attempted | Underlying archive unavailable; indirect readback available |
| Conversation pagination | `turnLimit=20` | Rejected because interface maximum is 10 | Retried with `turnLimit=10` and succeeded | Available within interface bounds |
| Conversation item size | Requested 30,000 characters | Rejected because interface maximum is 20,000 | Retried at 20,000 and succeeded | Available within interface bounds |
| Current task index | Requested 100 entries | Rejected because interface maximum is 50 | Retried at 50 and succeeded | Available within interface bounds; archived locator not surfaced |

## Retry policy

For read operations:

1. Retry the same route after correcting a transient or schema-bound failure.
2. Try an independent route against the same target.
3. Record exactly what failed and what remains observable.
4. Use `UNAVAILABLE` only for the requested route or artifact, not as a universal nonexistence claim.

For writes:

1. Do not blindly retry a non-idempotent operation.
2. Read back the branch or object state first.
3. Retry only if the intended state is absent and the operation identity is understood.
4. Never use force updates to make an uncertain write “work.”


