# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import json
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


class TraceGradingTests(unittest.TestCase):
    """Check that a corrupt scene does not discard the other scene's result."""

    def test_corrupt_reduced_trace_preserves_original_result(self):
        """Record empty and truncated traces as failures and still finish grading."""
        grader = Path(__file__).with_name("grade.py")
        for payload in (b"", b"PK\x03\x04truncated"):
            with self.subTest(payload=payload), tempfile.TemporaryDirectory() as folder:
                root = Path(folder)
                candidate = root / "candidate.py"
                candidate.write_text(
                    textwrap.dedent(
                        f"""\
                        import argparse
                        from pathlib import Path
                        import numpy as np

                        parser = argparse.ArgumentParser()
                        parser.add_argument("--scene")
                        parser.add_argument("--device")
                        parser.add_argument("--output")
                        args = parser.parse_args()
                        if args.scene == "reduced":
                            Path(args.output).write_bytes({payload!r})
                        else:
                            poses = np.zeros((721, 3, 7), dtype=np.float32)
                            poses[:, :, 6] = 1.0
                            for body in range(3):
                                poses[:, body, 0] = body
                                poses[:121, body, 2] = np.linspace(1.0 + 0.2 * body, 0.1, 121)
                                poses[121:, body, 2] = 0.1
                            velocities = np.zeros((721, 3, 6), dtype=np.float32)
                            np.savez(args.output, poses=poses, velocities=velocities)
                        """
                    )
                )
                evidence = root / "evidence"
                result = subprocess.run(
                    [
                        sys.executable,
                        str(grader),
                        "--case",
                        "contact",
                        "--candidate",
                        str(candidate),
                        "--output-dir",
                        str(evidence),
                    ],
                    check=False,
                    capture_output=True,
                    text=True,
                    timeout=30,
                )
                self.assertEqual(result.returncode, 1, result.stderr)
                report = evidence / "contact-report.json"
                self.assertTrue(report.is_file(), result.stderr)
                data = json.loads(report.read_text())
                self.assertFalse(data["passed"])
                self.assertFalse(data["scenes"]["reduced"]["passed"])
                self.assertIn("error", data["scenes"]["reduced"])
                self.assertTrue(data["scenes"]["original"]["passed"])


if __name__ == "__main__":
    unittest.main()
