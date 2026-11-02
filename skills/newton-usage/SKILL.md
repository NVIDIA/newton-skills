---
name: newton-usage
description: Find version-matched Newton documentation and packaged examples for setup or capability discovery. Route build, debug, migration, optimization, and validation work to focused skills.
metadata:
  author: Anthony Angeles <aangeles@nvidia.com>
  tags:
    - newton
    - physics-simulation
    - documentation
---

# Using Newton

Help users of the released Newton wheel find and apply the relevant public
documentation and examples. Work in the user's Python environment; a Newton
source checkout is optional. Route focused work to the matching specialized
Newton skill when one is available.

1. Choose the request mode before using tools:
   - For “how do I,” “show the command,” or other instruction-only requests,
     return commands and direct documentation URLs without executing commands,
     browsing, or opening the documentation. Do not call a web or documentation
     tool in this mode.
   - For “find,” “discover,” “check,” or other environment-specific requests,
     reuse known facts and otherwise run this bounded discovery once:
     `python -c "import sys; from importlib.metadata import version; from importlib.util import find_spec; print('python=' + sys.executable); print('version=' + version('newton')); print('package=' + str(find_spec('newton').origin)); print('examples=' + str(find_spec('newton.examples').origin))" && python -m newton.examples --list`.
   - For construction, diagnosis, migration, performance, or claim assessment,
     stop this workflow, read the matching specialized Newton skill, state that
     it owns the task, and follow it as the primary workflow.
   Establish the CPU/GPU environment only when it affects the answer. This skill
   is tested with Newton 1.7.0; for another version, use matching documentation
   and verify each referenced interface before relying on it.
2. For Newton 1.7.0, select the direct route matching the request:
   - setup, extras, and examples: [installation](https://newton-physics.github.io/newton/1.7.0/guide/installation.html)
   - platform, CUDA, version, or API support: [compatibility](https://newton-physics.github.io/newton/1.7.0/guide/compatibility.html)
   - first simulation or robotics walkthrough: [tutorials](https://newton-physics.github.io/newton/1.7.0/guide/tutorials.html)
   - solver choice and capabilities: [solver guide](https://newton-physics.github.io/newton/1.7.0/solvers/index.html)
   - exact public symbols: [API reference](https://newton-physics.github.io/newton/1.7.0/api/newton.html)
   Use the [overview](https://newton-physics.github.io/newton/1.7.0/guide/overview.html)
   only when the request spans categories. When the user asks for a documentation
   location or matching route, copy the URL into the answer without opening or
   verifying it, including after environment discovery. Open at most one routed
   page only when its contents are needed to answer the question, plus a linked
   API page only when an exact symbol must be confirmed. Do not search the site or
   inspect another version first. If a matching checkout already exists, its
   documentation is under `docs/`; do not require a clone.
3. For a selected packaged example, inspect its options with
   `python -m newton.examples <example_name> --help`. Do not run an example or
   install extras unless asked. If dependencies are missing, point to the
   version-pinned `newton[examples]` installation guidance without silently
   changing Newton versions.
4. Keep the result compact: Newton version/environment; selected documentation
   or example; action executed or command supplied; verified result; and one
   remaining blocker, if any. Omit fields that do not apply. Do not survey
   unrelated documentation or repeat already-known environment checks.

Supported Newton version: 1.7.0 only. If the installed version differs, warn and
stop before version-specific commands until matching documentation and interfaces
are verified. If Newton is absent or discovery fails, preserve the command, status,
and output and stop. Do not scan other interpreters, environments, repositories,
or filesystem locations unless the user asks.
