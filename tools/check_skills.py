#!/usr/bin/env python3
"""Validate the coding-agent-skills repository without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
README = ROOT / "README.md"
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
README_SKILL_RE = re.compile(r"\]\((skills/[^)#?]+\.md)(?:[?#][^)]*)?\)")


def markdown_files() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)


def check_relative_links() -> list[str]:
    errors: list[str] = []
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            parsed = urlparse(target)
            if parsed.scheme or parsed.netloc or target.startswith("#"):
                continue
            relative = unquote(parsed.path)
            if not relative:
                continue
            resolved = (path.parent / relative).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {target}")
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing link target: {target}")
    return errors


def check_skill_index() -> list[str]:
    errors: list[str] = []
    skill_files = {
        path.relative_to(ROOT).as_posix()
        for path in SKILLS_DIR.glob("*.md")
        if path.is_file()
    }
    readme_text = README.read_text(encoding="utf-8")
    indexed = set(README_SKILL_RE.findall(readme_text))

    missing = sorted(skill_files - indexed)
    stale = sorted(indexed - skill_files)
    if missing:
        errors.append("README is missing skill entries: " + ", ".join(missing))
    if stale:
        errors.append("README references missing skills: " + ", ".join(stale))

    for path in sorted(SKILLS_DIR.glob("*.md")):
        if not path.read_text(encoding="utf-8").strip():
            errors.append(f"empty skill file: {path.relative_to(ROOT)}")
    return errors


def main() -> int:
    errors = check_relative_links() + check_skill_index()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    skill_count = len(list(SKILLS_DIR.glob("*.md")))
    print(f"OK: validated {skill_count} skills and repository Markdown links")
    return 0


if __name__ == "__main__":
    sys.exit(main())
