---
name: newton-build-simulation
description: Build or extend a Newton simulation with supported models, solvers, controllers, collision, or coupling. Not for diagnosing an existing failure, migration, profiling, or independent validation.
metadata:
  author: Anthony Angeles <aangeles@nvidia.com>
  tags:
    - newton
    - physics-simulation
    - modeling
---

# Building a Newton Simulation

Build the smallest supported simulation that expresses the requested behavior.
Preserve the user's assets, conventions, environment, and explicit choices; a
Newton source checkout is optional.

1. Choose the request mode before using tools. For a plan or instruction-only
   request, provide the direct documentation route, minimal build sequence, and
   proposed checks without executing commands or opening documentation. The
   routes and workflow below are sufficient for a plan: after reading this skill,
   do not call another tool, search the web or workspace, verify URLs, or substitute
   `latest` or raw source pages. A runnable verification plan means the proposed
   execution command, observables, bounds, and stop condition; it does not require
   source code or exact API signatures. For an
   implementation request, reuse supplied facts and otherwise run this probe once:
   `python -c "import sys, newton; from importlib.metadata import version; print(sys.executable); print(version('newton')); print(newton.__file__)"`.
   Inspect the device only when it affects the build. Collect missing model facts
   once. Route an existing failure to `newton-debug-simulation`, a source-simulator
   port to `newton-migrate-simulation`, a measured speed request to
   `newton-optimize-simulation`, and a claim check to `newton-verify-simulation`.
   Stop this workflow, state that the selected skill owns the task, and follow it.
   Identify bodies/assets, units, frames, contacts, controls, and acceptance behavior.
2. For Newton 1.7.0, start with one canonical stable route: [quick start](https://newton-physics.github.io/newton/stable/guide/installation.html#quick-start)
   for the simulation loop, [tutorials](https://newton-physics.github.io/newton/stable/guide/tutorials.html)
   for a walkthrough, [worlds](https://newton-physics.github.io/newton/stable/concepts/worlds.html)
   for replicated environments, [articulations](https://newton-physics.github.io/newton/stable/concepts/articulations.html)
   for joints and state layout, [deformables](https://newton-physics.github.io/newton/stable/concepts/deformable_objects.html),
   [collisions](https://newton-physics.github.io/newton/stable/concepts/collisions.html),
   [actuators](https://newton-physics.github.io/newton/stable/concepts/actuators.html),
   [coupled solvers](https://newton-physics.github.io/newton/stable/concepts/coupling.html),
   or the [solver guide](https://newton-physics.github.io/newton/stable/solvers/index.html).
   Consult [conventions](https://newton-physics.github.io/newton/stable/concepts/conventions.html)
   when frames or spatial quantities matter. Open at most one concept or guide
   page, plus its linked API entry, only when implementation requires an exact
   symbol. Confirm that the stable API reports 1.7.0 before relying on a signature;
   otherwise stop for matching release documentation. Use browser or documentation
   tools for retrieval, never shell network commands such as `curl` or `wget`.
   Do not browse the overview or unrelated sections first.
   Rank supported options by required fidelity and hardware, starting with the
   simplest. State unsupported needs.
3. For a plan, use this compact public workflow: build or import the smallest model,
   finalize it, create state, control, contacts, collision pipeline, and one suitable
   solver, then clear forces, collide, step, and advance successive simulation
   states. For rigid plus deformable work, consider one solver that supports every
   required component before coupled
   solvers; require coupling only when the needed interaction cannot be represented
   by one supported solver. Provide the shortest proposed command and checks without
   installing, executing, or writing unverified code. For implementation, use a packaged example only when its documented
   extras are already available: list examples with `python -m newton.examples
   --list` and inspect one with `--help`. Otherwise use the version-matched quick
   start and public APIs. Do not install extras unless asked.
4. For implementation, run a short representative trajectory, inspect effective
   model and solver state, and check task-specific bounds rather than rendered
   output alone. For a plan, describe that trajectory and its checks without
   executing them. If required assets are absent, inspect their expected location
   once, report what is missing, and stop without a broad search. Report only the
   version/environment, selected route and components, command or proposed command,
   verification evidence, and one blocker if present. Stop when the minimal model
   passes; do not imply parity, optimality, or real-world validity.

Supported Newton version: 1.7.0 only. For another version, warn and stop before
version-specific implementation until matching documentation and interfaces are
verified. Preserve the command, exit status, and output for any failure.
