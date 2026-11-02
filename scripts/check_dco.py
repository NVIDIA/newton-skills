# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Require author and co-author DCO sign-offs on every contributed commit."""

import argparse
import re
import subprocess


def git(*args):
    return subprocess.check_output(["git", *args], text=True).rstrip("\n")


def identity(value):
    match = re.fullmatch(r"\s*(.+?)\s+<([^<>\s@]+@[^<>\s@]+)>\s*", value)
    if not match:
        raise ValueError(f"Invalid name/email identity: {value!r}")
    return match[1].strip(), match[2].casefold()


def trailers(commit, key):
    value = git("show", "-s", f"--format=%(trailers:key={key},valueonly,unfold,separator=%x00)", commit)
    return [identity(item) for item in value.split("\0") if item.strip()]


def check(base, head):
    # Resolve revision arguments before constructing a range; never pass options through.
    base = git("rev-parse", "--verify", "--end-of-options", f"{base}^{{commit}}")
    head = git("rev-parse", "--verify", "--end-of-options", f"{head}^{{commit}}")
    commits = git("rev-list", f"{base}..{head}").splitlines()
    failures = []
    for commit in commits:
        try:
            author = identity(git("show", "-s", "--format=%an <%ae>", commit))
            required = {author, *trailers(commit, "Co-authored-by")}
            signed = set(trailers(commit, "Signed-off-by"))
            for name, email in sorted(required - signed):
                failures.append(f"{commit}: missing Signed-off-by: {name} <{email}>")
        except ValueError as error:
            failures.append(f"{commit}: {error}")
    for failure in failures:
        print(failure)
    print(f"Checked {len(commits)} contributed commit(s); {len(failures)} DCO failure(s).")
    return not failures


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("base")
    parser.add_argument("head")
    args = parser.parse_args()
    return 0 if check(args.base, args.head) else 1


if __name__ == "__main__":
    raise SystemExit(main())
