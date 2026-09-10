from __future__ import annotations

from pathlib import Path
import tempfile
import unittest
from unittest import mock

from tools import check_skills


class MarkdownLinkValidationTests(unittest.TestCase):
    def test_angle_bracket_destination_keeps_spaces(self) -> None:
        self.assertEqual(
            "docs/guide with spaces.md",
            check_skills._markdown_link_destination(
                '<docs/guide with spaces.md> "Installation guide"'
            ),
        )

    def test_spaced_angle_bracket_link_resolves_existing_file(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            docs = root / "docs"
            docs.mkdir()
            (docs / "guide with spaces.md").write_text("# Guide\n", encoding="utf-8")
            (root / "README.md").write_text(
                "[guide](<docs/guide with spaces.md>)\n", encoding="utf-8"
            )

            with mock.patch.object(check_skills, "ROOT", root):
                self.assertEqual([], check_skills.check_relative_links())

    def test_regular_destination_with_title_still_resolves(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            docs = root / "docs"
            docs.mkdir()
            (docs / "guide.md").write_text("# Guide\n", encoding="utf-8")
            (root / "README.md").write_text(
                '[guide](docs/guide.md "Installation guide")\n', encoding="utf-8"
            )

            with mock.patch.object(check_skills, "ROOT", root):
                self.assertEqual([], check_skills.check_relative_links())

    def test_missing_spaced_target_reports_complete_destination(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "README.md").write_text(
                "[missing](<docs/missing guide.md>)\n", encoding="utf-8"
            )

            with mock.patch.object(check_skills, "ROOT", root):
                errors = check_skills.check_relative_links()

            self.assertEqual(
                ["README.md: missing link target: docs/missing guide.md"], errors
            )


if __name__ == "__main__":
    unittest.main()
