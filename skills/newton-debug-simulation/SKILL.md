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

1. Establish the expected symptom and the permitted actions. Follow harness and
   user execution permissions; planning may still require read-only documentation
   retrieval. For hands-on diagnosis, reuse supplied facts and otherwise run this
   probe once: `python -c "import sys, newton; from importlib.metadata import version; print(sys.executable); print(version('newton')); print(newton.__file__)"`.
   Inspect the device only when
   it affects the failure. Collect missing reproducer facts once. Route a correct
   workload's performance request to `newton-optimize-simulation` and claim
   assessment to `newton-verify-simulation` when those skills are available;
   otherwise use the applicable public documentation. Stop diagnosis when the
   request has no reproducible failure. Record the solver,
   simulation/control cadence, and expected versus observed behavior.
2. Select documentation matching the installed release. The links below are
   documentation entrypoints; verify their version before relying on a parameter.
   Route the symptom directly to [simulation tuning](https://newton-physics.github.io/newton/latest/concepts/simulation_tuning.html)
   for instability or poor physical response, [collisions](https://newton-physics.github.io/newton/latest/concepts/collisions.html)
   for missing or incorrect contacts, [solver observables](https://newton-physics.github.io/newton/latest/concepts/solver_observables.html)
   for backend diagnostics, [viewers and debugging](https://newton-physics.github.io/newton/latest/guide/visualization.html)
   for visual or recorded inspection, [solver guidance](https://newton-physics.github.io/newton/latest/solvers/index.html)
   for backend behavior, or [compatibility](https://newton-physics.github.io/newton/latest/guide/compatibility.html)
   for platform and CUDA failures. For import errors, follow
   [USD parsing](https://newton-physics.github.io/newton/latest/concepts/usd_parsing.html)
   or the applicable public importer API; for control or joint limits, consult
   [articulations](https://newton-physics.github.io/newton/latest/concepts/articulations.html)
   and solver feature support; for multi-solver interaction, consult
   [coupling](https://newton-physics.github.io/newton/latest/concepts/coupling.html).
   Start with the relevant section and follow additional guides or API entries
   when a discriminating check needs them or evidence changes the hypothesis.
   Stop retrieval once the diagnostic question is resolved; avoid unrelated surveys.
   Prefer matching bundled documentation when available. Human-useful diagnostic
   knowledge belongs in Newton documentation; report missing public guidance
   rather than adding a second troubleshooting manual to the skill.
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
   state with acceptance bounds fixed before the repair. Record all attempted
   changes, including discarded or unnecessary ones. Report the version/environment,
   documentation route, reproduction command, cause, before/after evidence,
   smallest supported fix, and one blocker or unverified claim if present. CPU,
   short-run, or visual evidence does not prove a GPU, long-run, or state-level fix.

Newton compatibility has not been validated across releases. Verify matching
interfaces and backend behavior before applying a version-specific fix.
