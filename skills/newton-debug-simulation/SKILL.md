---
name: newton-debug-simulation
description: Diagnose a reproducible Newton motion, contact, stability, import, controller, coupling, CUDA, or runtime failure. Not for tuning a correct workload or independently validating a result.
metadata:
  author: Anthony Angeles <aangeles@nvidia.com>
  tags:
    - newton
    - physics-simulation
    - debugging
---

# Debugging a Newton Simulation

Isolate an observable Newton failure and make the smallest evidence-supported
correction without changing the intended physical model.

1. Choose the request mode before using tools. For a diagnostic plan, name the
   direct documentation route and next discriminating check without executing the
   reproducer or opening documentation. For hands-on diagnosis, reuse supplied
   facts and otherwise run this probe once: `python -c "import sys, newton; from importlib.metadata import version; print(sys.executable); print(version('newton')); print(newton.__file__)"`.
   Inspect the device only when
   it affects the failure. Collect missing reproducer facts once. Route a correct
   workload's performance request to `newton-optimize-simulation` and claim
   assessment to `newton-verify-simulation`. Stop this workflow, state that the
   selected skill owns the task, and follow it. Record the solver,
   simulation/control cadence, and expected versus observed behavior.
2. For Newton 1.7.0, route the symptom directly to [simulation tuning](https://newton-physics.github.io/newton/1.7.0/concepts/simulation_tuning.html)
   for instability or poor physical response, [collisions](https://newton-physics.github.io/newton/1.7.0/concepts/collisions.html)
   for missing or incorrect contacts, [solver observables](https://newton-physics.github.io/newton/1.7.0/concepts/solver_observables.html)
   for backend diagnostics, [viewers and debugging](https://newton-physics.github.io/newton/1.7.0/guide/visualization.html)
   for visual or recorded inspection, [solver guidance](https://newton-physics.github.io/newton/1.7.0/solvers/index.html)
   for backend behavior, or [compatibility](https://newton-physics.github.io/newton/1.7.0/guide/compatibility.html)
   for platform and CUDA failures. Open at most one symptom route, plus its linked
   API entry only to confirm an exact parameter or supported observable. When the
   user only needs a documentation location, copy the URL without opening it. Use
   browser or documentation tools for retrieval; never use shell network commands
   such as `curl` or `wget`. Do not search the site first.
   Reproduce and reduce the failure without losing it; for late failures, retain
   the first invalid state, preceding state, and inputs. Verify that the active
   backend consumes any parameter under consideration.
3. Separate initialization/model, control, contact generation or capacity, solver
   response, and environment causes with one discriminating check at a time. For a
   plan, name the next check, what it separates, and its stop condition; do not run
   the simulation or search exhaustively. If the reproducer or required assets are
   absent, inspect the expected location once, report what is missing, and stop
   without scanning other environments or repositories. Leave the cause unverified
   when evidence is missing, and never mask invalid physics by filtering or clamping.
4. Re-run the reduced and original cases over the required horizon and compare
   state with fixed acceptance bounds. Report only the version/environment,
   documentation route, reproduction command, cause, before/after evidence,
   smallest supported fix, and one blocker or unverified claim if present. CPU,
   short-run, or visual evidence does not prove a GPU, long-run, or state-level fix.

Supported Newton version: 1.7.0 only. For another version, warn and stop before a
version-specific fix until matching interfaces and behavior are verified.
