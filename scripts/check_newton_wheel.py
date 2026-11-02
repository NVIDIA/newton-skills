# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Check the released Newton wheel interfaces relied on by the user skills."""

import argparse
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
import subprocess
import sys


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected-version", required=True)
    arguments = parser.parse_args()

    try:
        installed_version = version("newton")
    except PackageNotFoundError:
        print("Newton is not installed.", file=sys.stderr)
        return 1

    if installed_version != arguments.expected_version:
        print(
            f"Expected Newton {arguments.expected_version}, found {installed_version}.",
            file=sys.stderr,
        )
        return 1

    import newton

    package_path = Path(newton.__file__).resolve()
    result = subprocess.run(
        [sys.executable, "-m", "newton.examples", "--list"],
        text=True,
        capture_output=True,
        timeout=120,
    )
    if result.returncode != 0:
        print(result.stdout, end="")
        print(result.stderr, end="", file=sys.stderr)
        return result.returncode
    if not result.stdout.strip():
        print("Newton returned an empty packaged-example list.", file=sys.stderr)
        return 1

    print(f"Newton version: {installed_version}")
    print(f"Newton package: {package_path}")
    print("Packaged example discovery: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
