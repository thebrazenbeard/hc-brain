# Four Diagnostic — Reference Kernel Hosted CI Pre-Runner Failure — 2026-09-10

Status: CI/infrastructure diagnostic; no workflow mutation; no canonical-main mutation.

## Scope

Investigated repeated GitHub Actions failures for workflow:

`.github/workflows/reference-kernel.yml`

Current workflow contains a single `ubuntu-latest` job with two ordinary shell steps:

1. clone/check out the current repository SHA;
2. run `python3 -m unittest -v test_hc_kernel.py test_durable_kernel.py`.

This diagnostic asks whether the observed hosted failures establish a Python/reference-kernel test failure.

## Result

**NO. The observed failures are pre-runner infrastructure failures. Exact account/platform cause remains UNKNOWN.**

The available GitHub API evidence shows that the jobs never received a runner and never exposed an executed step.

`WORKFLOW_CONCLUSION_FAILURE != TEST_EXECUTION_FAILURE`

`JOB_CREATED != RUNNER_ASSIGNED`

## Repeated evidence

### Run 34539356596

Head: `ccd0262d68c83846a2d6640269a9e67075c438f3`

Job:

- conclusion: `failure`
- created: `2026-09-10T22:50:10Z`
- started: `2026-09-10T22:50:10Z`
- completed: `2026-09-10T22:50:12Z`
- `steps: []`
- `runner_id: 0`
- `runner_name: ""`
- `runner_group_id: 0`

### Run 34539477839

Head: `17add6f4c625cecc90473654d079ad413b5882e0`

Job:

- conclusion: `failure`
- created: `2026-09-10T22:51:44Z`
- started: `2026-09-10T22:51:44Z`
- completed: `2026-09-10T22:51:47Z`
- `steps: []`
- `runner_id: 0`
- `runner_name: ""`
- `runner_group_id: 0`

### Run 34539774100

Head: `d0df2c98d042c0f68833005a5528e14bf810b0f0`

Job:

- conclusion: `failure`
- created: `2026-09-10T22:55:35Z`
- started: `2026-09-10T22:55:35Z`
- completed: `2026-09-10T22:55:37Z`
- `steps: []`
- `runner_id: 0`
- `runner_name: ""`
- `runner_group_id: 0`

### Run 34540553637

Head: `b33f3ee60323a6a8988c331d8850719ec3f01d67`

Job:

- conclusion: `failure`
- created: `2026-09-10T23:05:27Z`
- started: `2026-09-10T23:05:27Z`
- completed: `2026-09-10T23:05:29Z`
- `steps: []`
- `runner_id: 0`
- `runner_name: ""`
- `runner_group_id: 0`

The job-log endpoint for the latest job returned storage-side `BlobNotFound`, consistent with there being no normal runner-produced job log artifact available through that endpoint.

## Interpretation

The strongest justified classification is:

`UNKNOWN_PRE_RUNNER_INFRASTRUCTURE_FAILURE`

with the narrower observed fact:

`NO_GITHUB_HOSTED_RUNNER_ASSIGNMENT_OBSERVED`

This evidence does **not** identify why GitHub failed before runner assignment.

Potential classes such as account/plan/billing entitlement, Actions policy, hosted-runner availability, account restriction, or another GitHub-side pre-run condition are hypotheses only. The available connector surface does not expose enough account/admin state to distinguish them, and the repository Actions-permission endpoint was unavailable through the current connector.

Therefore do not claim a specific account cause without new evidence.

## Workflow-content check

The current workflow is structurally ordinary:

- `on: push` and `pull_request` path filters;
- one `ubuntu-latest` job;
- shell clone/checkout step;
- shell Python unittest step.

Because the job receives no runner and has zero steps, changing clone syntax, Python invocation, checkout strategy, or test command is not currently evidence-driven.

A shell-step failure requires an assigned runner and an executed step trace. Neither is present in the observed failures.

## Recommended next action

1. **Stop workflow churn** until runner assignment succeeds or GitHub exposes a concrete pre-run error.
2. Preserve local exact-blob execution as a separate evidence channel.
3. If UI/account access is available, inspect the Actions run banner/account Actions availability, billing/spending/usage state, and repository/org Actions policy for an explicit platform message.
4. Once a job receives a nonzero runner ID/name and actual steps, resume normal workflow/test diagnosis from the first failing executed step.
5. Do not use the current hosted failures to downgrade or upgrade code-test results.

## Evidence ceiling

`RUNNER_ID_0 + ZERO_STEPS != PYTHON_TEST_FAILURE`

`BLOBNOTFOUND_LOG != TEST_ASSERTION_FAILURE`

`REPEATED_PRE_RUNNER_FAILURE != KNOWN_BILLING_OR_POLICY_CAUSE`

`LOCAL_TEST_PASS != HOSTED_CI_PASS`

`HOSTED_CI_PRE_RUNNER_FAILURE != LOCAL_TEST_FAIL`
