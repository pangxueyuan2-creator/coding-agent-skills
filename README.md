# coding-agent-skills

**Ready-to-use skills, prompts and checklists for AI coding agents.**  
Focused on security, testing, documentation, and safe workflows.  
**Bilingual (English / 中文)** — designed for both global and Chinese developers.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Why this exists

AI coding agents (Cursor, Claude Code, Windsurf, Codex, etc.) are powerful, but they often:
- Skip security checks
- Generate incomplete tests
- Produce poor documentation
- Ignore repository conventions

This repository gives you **copy-paste ready skills** and **checklists** you can drop into any agent system (Cursor rules, Claude projects, AGENTS.md, custom MCP, etc.).

---

## Quick Start

1. Copy any skill file into your agent’s system prompt / rules / skills folder.
2. Or reference the checklist before asking the agent to make changes.
3. Prefer the bilingual versions if you work with Chinese teams or codebases.

---

## Available Skills

| Skill | Description | Language |
|-------|-------------|----------|
| [security-review](skills/security-review.md) | Systematic security review for PRs and code changes | EN + 中文 |
| [test-first](skills/test-first.md) | Force test-driven thinking before writing implementation | EN + 中文 |
| [safe-refactor](skills/safe-refactor.md) | Safe large-scale refactor with verification steps | EN |
| [docs-and-readme](skills/docs-and-readme.md) | Generate high-quality README and docs | EN + 中文 |
| [chinese-codebase](skills/chinese-codebase.md) | Special handling for Chinese comments, i18n and local practices | 中文 |
| [agent-self-check](skills/agent-self-check.md) | Agent self-verification before finishing a task | EN |

---

## Recommended Usage

### Cursor / Claude Code / similar
Add the content of a skill file into your project rules or system prompt.

### AGENTS.md / custom agent
Include the relevant skill sections under a clear heading.

### Checklist mode
Before asking the agent to implement something, paste the corresponding checklist and say:

> Follow this checklist strictly. Do not skip any item.

---

## Philosophy

- **Security first** — every change should be reviewable and bounded
- **Evidence over claims** — agents must show what they checked
- **Human readable** — skills are written so both humans and agents can understand them
- **Bilingual by design** — many Chinese developers use English tools; we support both

---

## Contributing

PRs are welcome. New skills should:
- Be short and actionable
- Include both English and Chinese when possible
- Focus on real pain points of AI coding agents

---

## Related Projects by the same author

- [PatchWitness](https://github.com/pangxueyuan2-creator/patchwitness) — Independent trust gate for AI coding agents
- [GuardSpec](https://github.com/pangxueyuan2-creator/guardspec) — Compile repository intent into enforceable agent boundaries
- [TaskToPR](https://github.com/pangxueyuan2-creator/tasktopr) — Turn a GitHub Issue into a transparent, tested Pull Request

---

Made with care for safer AI-assisted development.
