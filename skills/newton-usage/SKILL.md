---
name: newton-usage
description: Install or use the released Newton Python package to find examples, build physics simulations, choose solvers, or diagnose failures.
metadata:
  author: Anthony Angeles <aangeles@nvidia.com>
---

# Using Newton

1. **Identify the task and release.** Reuse supplied facts. Use the same verified
   interpreter or required wrapper for all Newton commands, preserving its
   environment variables and project context. Keep discovery read-only. For an
   inactive or ambiguous uv environment, see [environment selection](references/environment.md).
   Get the interpreter and version without importing Newton with
   `python -c "import sys; from importlib.metadata import version; print(sys.executable, flush=True); print(version('newton'))"`.
   For a version-only request, stop there. If needed and permitted, locate Newton
   separately with `python -c "import newton; print(newton.__file__)"`. Retain
   the metadata if import fails.
2. **Find matching guidance.** Use the [Newton documentation](https://newton-physics.github.io/newton/),
   a supplied matching checkout, or the wheel's `python -m newton.docs` when
   available and imports are permitted. Flag version mismatches. Consult the
   installation guide if Newton is missing, or the relevant solver, importer,
   or troubleshooting guide for an existing scene. A checkout is optional.
3. **Start from an example.** List examples with `python -m newton.examples --list`
   or look in the installed package's `examples/` directory. Use
   `python -m newton.examples <name> --help` for options and run the example
   with `python -m newton.examples <name>` when execution is requested. If
   dependencies are missing, point to the installation guide for
   `newton[examples]` pinned to the installed version. Get authorization before
   changing dependencies.
4. **Build or diagnose.** Define the motion, horizon, observables, and physical
   bounds before building. Choose the simplest documented solver that supports
   the required interactions. Use coupling only if one solver cannot represent
   them. Adapt the closest example or a minimal public-API scene. Preserve
   supplied assets, choices, and execution limits. Reduce failures while retaining
   the symptom, then recheck the original scene after fixing it.
5. **Verify and report.** Inspect effective model and solver values, finite
   state, relevant bounds such as penetration or joint travel, and the requested
   behavior over the agreed horizon. Report sources, commands run, and measured
   results. If execution is unavailable, give the next check and mark the outcome
   unverified. Use specialized skills when they add relevant expertise.

Compatibility across Newton releases has not been validated.
