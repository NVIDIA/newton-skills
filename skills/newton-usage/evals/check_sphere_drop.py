# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Grade the CPU sphere-drop case by running the submitted simulation."""

import argparse
import math
import runpy


def check_heights(heights):
    if len(heights) != 241 or not all(math.isfinite(height) for height in heights):
        raise ValueError("Expected 241 finite height samples at 120 Hz")
    if not math.isclose(heights[0], 1.0, abs_tol=0.01):
        raise ValueError(f"Initial center height must be 1 m, got {heights[0]:.3f} m")
    if not 0.60 <= heights[30] <= 0.78:
        raise ValueError(f"Center height at 0.25 s is outside free fall bounds: {heights[30]:.3f} m")

    lowest = min(heights)
    if lowest < 0.17:
        raise ValueError(f"Sphere penetrated the ground by more than 3 cm: min height {lowest:.3f} m")

    settled = heights[-30:]
    if max(abs(height - 0.2) for height in settled) > 0.03 or max(settled) - min(settled) > 0.01:
        raise ValueError("Sphere did not settle near 0.2 m during the final quarter second")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scene", help="Candidate Python file exposing simulate()")
    args = parser.parse_args()
    samples = list(runpy.run_path(args.scene)["simulate"]())
    check_heights(samples)
    print(f"Sphere drop passed. Minimum height {min(samples):.3f} m, final height {samples[-1]:.3f} m.")
