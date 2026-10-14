# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


DCO_CHECK = Path(__file__).resolve().parents[1] / "scripts" / "check_dco.py"


class DCOTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
        self.env.update(GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1")
        self.git("init", "--quiet")
        self.commit("Initial", signoff=True)
        self.base = self.git("rev-parse", "HEAD").strip()

    def git(self, *args):
        return subprocess.check_output(
            ["git", "-c", "user.name=Contributor", "-c", "user.email=author@example.org",
             "-c", "core.hooksPath=/dev/null", *args],
            cwd=self.root, env=self.env, text=True,
        )

    def commit(self, message, signoff=False, author=None):
        args = ["commit", "--quiet", "--allow-empty", "-m", message]
        if signoff:
            args.append("--signoff")
        if author:
            args.extend(["--author", author])
        self.git(*args)

    def check(self):
        return subprocess.run(
            [sys.executable, str(DCO_CHECK), self.base, "HEAD"],
            cwd=self.root, env=self.env, text=True, capture_output=True,
        )

    def test_signed_commit(self):
        self.commit("Change", signoff=True)
        self.assertEqual(self.check().returncode, 0)

    def test_unsigned_commit_fails(self):
        self.commit("Change")
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing Signed-off-by", result.stdout)

    def test_wrong_author_signoff_fails(self):
        self.commit("Change\n\nSigned-off-by: Someone Else <other@example.org>")
        self.assertNotEqual(self.check().returncode, 0)

    def test_body_text_does_not_count_as_trailer(self):
        self.commit("Change\n\nSigned-off-by: Contributor <author@example.org>\n\nMore body text.")
        self.assertNotEqual(self.check().returncode, 0)

    def test_earlier_unsigned_commit_is_not_hidden(self):
        self.commit("Unsigned change")
        self.commit("Signed change", signoff=True)
        self.assertNotEqual(self.check().returncode, 0)

    def test_coauthor_must_sign(self):
        self.commit("Change\n\nCo-authored-by: Other Person <other@example.org>", signoff=True)
        self.assertNotEqual(self.check().returncode, 0)
        self.commit("Unrelated signed change", signoff=True)
        self.assertNotEqual(self.check().returncode, 0)

    def test_signed_coauthor(self):
        self.commit(
            "Change\n\nCo-authored-by: Other Person <other@example.org>\n"
            "Signed-off-by: Other Person <other@example.org>", signoff=True,
        )
        self.assertEqual(self.check().returncode, 0)

    def test_nvskills_service_account(self):
        self.commit(
            "Attach NVSkills validation signatures\n\n"
            "Signed-off-by: nvskills-svc-account <svc-nvskills-signing@nvidia.com>",
            author="nvskills-svc-account <svc-nvskills-signing@nvidia.com>",
        )
        self.assertEqual(self.check().returncode, 0)

    def test_unsigned_bot_is_not_exempt(self):
        self.commit("Attach NVSkills validation signatures", author="Bot <bot@example.org>")
        self.assertNotEqual(self.check().returncode, 0)


class AttributionTests(unittest.TestCase):
    def lint(self, root):
        return subprocess.run(
            [sys.executable, "-m", "reuse", "--root", str(root), "lint"],
            text=True, capture_output=True,
        )

    def test_undeclared_new_file_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "new-document.md").write_text("New content\n")
            result = self.lint(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("new-document.md", result.stdout + result.stderr)

    def test_third_party_license_text_required(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "third_party").mkdir()
            # REUSE-IgnoreStart
            (root / "third_party" / "example.py").write_text(
                "# SPDX-FileCopyrightText: 2026 Example Author\n"
                "# SPDX-License-Identifier: MIT\nprint('example')\n"
            )
            # REUSE-IgnoreEnd
            result = self.lint(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("MIT", result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
