# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import argparse
import json
import subprocess
import sys
from pathlib import Path

import numpy as np


def check_trace(path, case, scene):
    """Check sampled state against fixed acceptance bounds."""
    count = 1 if scene == "reduced" else 3
    steps = 720 if case == "contact" else 3600
    with np.load(path, allow_pickle=False) as trace:
        poses, velocities = trace["poses"], trace["velocities"]
        checks = {
            "complete_horizon": poses.shape == (steps + 1, count, 7)
            and velocities.shape == (steps + 1, count, 6),
            "finite_state": bool(
                np.isfinite(poses).all() and np.isfinite(velocities).all()
            ),
        }
        if not all(checks.values()):
            bad = np.flatnonzero(
                ~(
                    np.isfinite(poses).all(axis=(1, 2))
                    & np.isfinite(velocities).all(axis=(1, 2))
                )
            )
            return {
                "checks": checks,
                "first_invalid_sample": int(bad[0]) if len(bad) else None,
            }
        if case == "contact":
            heights = poses[:, :, 2]
            initial = np.array([1.0 + 0.2 * index for index in range(count)])
            checks.update(
                initial_scene=bool(np.allclose(heights[0], initial, atol=1e-6)),
                initial_fall=bool(np.all(heights[24] < initial - 0.01)),
                bounded_penetration=bool(np.min(heights) >= 0.095),
                settled_contact=bool(np.all(np.abs(heights[-120:] - 0.1) <= 0.01)),
            )
            return {
                "checks": checks,
                "tolerance": 0.005,
                "minimum_height": float(heights.min()),
                "final_heights": heights[-1].tolist(),
            }
        commands = np.zeros((3600, 3))
        commands[:2400, 0] = 1.0
        velocity = np.cumsum(commands[:, 0]) * 0.001
        position = np.concatenate(([0.0], np.cumsum(velocity) * 0.001))
        checks.update(
            unchanged_commands=bool(np.array_equal(trace["commands"], commands)),
            preserved_motion=bool(
                np.max(np.abs(poses[:, :, 0] - position[:, None])) < 0.02
            ),
            preserved_scene=bool(
                np.allclose(poses[:, :, 1], np.arange(count)[None, :], atol=1e-5)
                and np.allclose(poses[:, :, 2], 0.0, atol=1e-5)
            ),
        )
        return {
            "checks": checks,
            "position_tolerance": 0.02,
            "maximum_position_error": float(
                np.max(np.abs(poses[:, :, 0] - position[:, None]))
            ),
        }


def main():
    """Run both scene sizes and save independent grading evidence."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", choices=("contact", "controller"), required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--device", default="cpu")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    results = {}
    for scene in ("reduced", "original"):
        output = args.output_dir / f"{args.case}-{scene}.npz"
        output.unlink(missing_ok=True)
        command = [
            sys.executable,
            str(args.candidate.resolve()),
            "--scene",
            scene,
            "--device",
            args.device,
            "--output",
            str(output.resolve()),
        ]
        try:
            process = subprocess.run(
                command, check=False, capture_output=True, text=True, timeout=120
            )
            log = args.output_dir / f"{args.case}-{scene}.log"
            log.write_text(process.stdout + process.stderr)
            result = {
                "command": command,
                "exit_status": process.returncode,
                "log": str(log),
            }
            if process.returncode == 0 and output.is_file():
                result.update(check_trace(output, args.case, scene))
                result["passed"] = all(result["checks"].values())
            else:
                result["passed"] = False
        except (subprocess.TimeoutExpired, OSError, ValueError, KeyError) as error:
            result = {"command": command, "passed": False, "error": str(error)}
        results[scene] = result
    report = {
        "case": args.case,
        "device": args.device,
        "passed": all(result["passed"] for result in results.values()),
        "scenes": results,
    }
    (args.output_dir / f"{args.case}-report.json").write_text(
        json.dumps(report, indent=2) + "\n"
    )
    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
