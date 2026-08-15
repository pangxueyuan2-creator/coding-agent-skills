# coding-agent-skills

Copy-paste skills and checklists for AI coding agents (Cursor, Claude Code, Codex, etc.).
Focus: security, testing, docs, and not skipping the boring checks.
English and 中文 where it helps.

MIT.

## Why

Agents often skip security review, leave weak tests, or ignore repo conventions.
These files are short instructions you can drop into rules / AGENTS.md / system prompts.

## Quick start

1. Copy a skill into your agent rules or project prompt.
2. Or paste the checklist before asking for a change.
3. Use the bilingual ones if the team or codebase mixes 中文 and English.

## Skills

| Skill | What it does | Lang |
|-------|----------------|------|
| [security-review](skills/security-review.md) | Security review for a change or PR | EN + 中文 |
| [test-first](skills/test-first.md) | Push for tests before implementation | EN + 中文 |
| [safe-refactor](skills/safe-refactor.md) | Safer large refactors with verification | EN |
| [docs-and-readme](skills/docs-and-readme.md) | README / docs that stay honest | EN + 中文 |
| [chinese-codebase](skills/chinese-codebase.md) | Notes for 中文 comments / local practices | 中文 |
| [agent-self-check](skills/agent-self-check.md) | Quick self-check before claiming done | EN |

## Usage tips

- Cursor / Claude Code: put the skill text in project rules.
- AGENTS.md: paste under a clear heading.
- Checklist mode: paste the list and say “follow this; don’t skip items.”

## Related

- [PatchWitness](https://github.com/pangxueyuan2-creator/patchwitness) — evidence for what a change actually did
- [GuardSpec](https://github.com/pangxueyuan2-creator/guardspec) — preflight against explicit agent rules
- [TaskToPR](https://github.com/pangxueyuan2-creator/tasktopr) — Issue → branch + tests + optional PR

Issues and PRs welcome if a skill is unclear or missing something real.
