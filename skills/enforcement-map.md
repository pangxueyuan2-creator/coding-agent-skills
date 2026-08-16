# Enforcement map: which tools actually back these skills

These skills are prompt text. Prompts do not enforce themselves — the agent can skip any
checklist item. This map separates the parts that ARE mechanically enforced by the
[PatchWitness](https://github.com/pangxueyuan2-creator/patchwitness) /
[GuardSpec](https://github.com/pangxueyuan2-creator/guardspec) /
[TaskToPR](https://github.com/pangxueyuan2-creator/tasktopr) toolchain from the parts
that rely on the agent complying. If a row says "prompt-only", treat it as guidance, not
a guarantee.

| Skill | Enforced by | What is enforced | Prompt-only (not enforced) |
|---|---|---|---|
| security-review | PatchWitness | Secret-scan findings on captured changed files; protected-path violations block the gate | "Stop and report" behavior, input validation, authz, injection review, logging hygiene |
| security-review | repo-privacy-guard | Whole-repository secret / privacy scan before making a repo public | PII heuristics beyond the pattern list |
| security-review | GuardSpec | Deny rules and protected paths from instructions when you wire `guardspec check` into preflight | Anything not written as an explicit rule |
| test-first | TaskToPR | Runs the discovered test commands and records results before commit/PR | Writing good tests in the first place |
| test-first | PatchWitness | `require_tests` policy and CI-check requirements fail the gate when configured | Test quality and coverage targets |
| safe-refactor | PatchWitness | Scope findings: only planned files changed, protected paths untouched | Rollback planning, behavior preservation |
| safe-refactor | Worktree Sheriff | Overlapping edits across parallel worktrees surfaced as collisions | Merging discipline |
| docs-and-readme | oss-readme-studio | README structure / completeness score | Honesty of the content itself |
| chinese-codebase | — | — | All of it (conventions) |
| agent-self-check | PatchWitness | `verify` proves the recorded evidence matches the payload | The self-check narrative itself |

## Wiring it up

1. Write the rules you care about into an AGENTS.md (GuardSpec scans it).
2. Run `patchwitness capture --policy-ref <trusted-revision>` after the agent finishes, or
   use the GitHub Action as a gate.
3. Run TaskToPR for Issue-driven work so tests run inside the pipeline.
4. Run Worktree Sheriff before parallel agents start editing.