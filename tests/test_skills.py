# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
TESTED_NEWTON_VERSION = "1.7.0"
EXPECTED_SKILLS = {
    "newton-build-simulation",
    "newton-debug-simulation",
    "newton-migrate-simulation",
    "newton-optimize-simulation",
    "newton-usage",
    "newton-verify-simulation",
}
REQUIRED_HEADINGS = (
    "# ",
)


def frontmatter(text):
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise AssertionError("SKILL.md has no YAML frontmatter")
    values = {}
    for line in match.group(1).splitlines():
        field = re.match(r"^([a-z][a-z0-9_-]*):\s*(.*)$", line)
        if field:
            values[field.group(1)] = field.group(2)
    return values


class SkillContractTests(unittest.TestCase):
    def skill_directories(self):
        return sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir())

    def test_expected_skill_set(self):
        self.assertEqual({path.name for path in self.skill_directories()}, EXPECTED_SKILLS)

    def test_skill_structure_and_scope(self):
        for directory in self.skill_directories():
            with self.subTest(skill=directory.name):
                text = (directory / "SKILL.md").read_text()
                metadata = frontmatter(text)
                self.assertEqual(metadata.get("name"), directory.name)
                self.assertTrue(metadata.get("description"))
                self.assertLessEqual(len(metadata["description"]), 200)
                self.assertIn("author: Anthony Angeles <aangeles@nvidia.com>", text)
                self.assertIn("tags:", text)
                self.assertIn(
                    f"Supported Newton version: {TESTED_NEWTON_VERSION} only",
                    text,
                )
                for heading in REQUIRED_HEADINGS:
                    self.assertIn(heading, text)
                self.assertNotRegex(text, r"https?://[^/]*(?:nvidia\.com|google\.com)")

    def test_evaluation_contract(self):
        all_ids = set()
        cross_skill_routes = set()
        for directory in self.skill_directories():
            with self.subTest(skill=directory.name):
                guidance = directory / "evals" / "EVAL.md"
                dataset_path = directory / "evals" / "evals.json"
                self.assertTrue(guidance.is_file())
                self.assertTrue(dataset_path.is_file())
                dataset = json.loads(dataset_path.read_text())
                self.assertEqual(dataset.get("skill_name"), directory.name)
                cases = dataset.get("evals")
                self.assertIsInstance(cases, list)
                self.assertGreaterEqual(len(cases), 3)
                expected_skills = []
                for case in cases:
                    self.assertTrue(
                        {"id", "prompt", "expected_skill", "expected_script",
                         "expected_output", "assertions"}.issubset(case)
                    )
                    self.assertNotIn(case["id"], all_ids)
                    all_ids.add(case["id"])
                    self.assertTrue(case["prompt"].strip())
                    self.assertTrue(case["expected_output"].strip())
                    self.assertTrue(case["assertions"])
                    expected_skills.append(case["expected_skill"])
                    self.assertIn(case["expected_skill"], EXPECTED_SKILLS | {None})
                    if case["expected_skill"] not in {None, directory.name}:
                        cross_skill_routes.add(case["expected_skill"])
                self.assertIn(directory.name, expected_skills)
                self.assertIn(None, expected_skills)
        self.assertTrue(cross_skill_routes)

    def test_displayport_coverage(self):
        optimize = json.loads(
            (SKILLS_ROOT / "newton-optimize-simulation" / "evals" / "evals.json").read_text()
        )
        verify = json.loads(
            (SKILLS_ROOT / "newton-verify-simulation" / "evals" / "evals.json").read_text()
        )
        self.assertIn(
            "newton-optimize-displayport-coupled-sweep",
            {case["id"] for case in optimize["evals"]},
        )
        self.assertIn(
            "newton-verify-displayport-invalid-success",
            {case["id"] for case in verify["evals"]},
        )


if __name__ == "__main__":
    unittest.main()
