---
name: newton-verify-simulation
description: Independently verify a Newton simulation claim with bounds, invariants, sensitivity tests, or references. Not for finding and fixing the root cause of an existing failure.
metadata:
  author: Anthony Angeles <aangeles@nvidia.com>
  tags:
    - newton
    - physics-simulation
    - verification
---

# Verifying a Newton Simulation

Determine what a Newton result establishes while separating solver execution,
simulation fidelity, simulator parity, and real-world validity.

1. Choose the request mode before using tools. For a verification plan, provide
   the direct documentation route and smallest falsification matrix without running
   the simulation or opening documentation. For evidence collection, reuse supplied
   facts and otherwise run this probe once: `python -c "import sys, newton; from importlib.metadata import version; print(sys.executable); print(version('newton')); print(newton.__file__)"`.
   Inspect the device only when
   it affects the claim. Collect missing claim and reference facts once. Route
   construction to `newton-build-simulation`, root-cause correction to
   `newton-debug-simulation`, migration work to `newton-migrate-simulation`, and
   speed work to `newton-optimize-simulation`. Stop this workflow, state that the
   selected skill owns the task, and follow it. Record the intended use, solver,
   acceptance criteria, and available analytic, simulator, experimental, or
   hardware reference. Derive bounds from the task or reference, never defaults.
2. For Newton 1.7.0, open only the route needed by the claim:
   [conventions](https://newton-physics.github.io/newton/1.7.0/concepts/conventions.html)
   for units, frames, and spatial quantities; [mass and inertia](https://newton-physics.github.io/newton/1.7.0/concepts/mass_inertia.html)
   for physical properties; [articulations](https://newton-physics.github.io/newton/1.7.0/concepts/articulations.html)
   for state and joints; [collisions](https://newton-physics.github.io/newton/1.7.0/concepts/collisions.html)
   for contact evidence; [solver observables](https://newton-physics.github.io/newton/1.7.0/concepts/solver_observables.html)
   for diagnostic outputs; or [solver capabilities](https://newton-physics.github.io/newton/1.7.0/solvers/index.html)
   for backend support. Open at most one concept or solver route, plus its linked
   API entry only when the claim depends on an exact symbol. When the user only
   needs a documentation location, copy the URL without opening it. Use browser or
   documentation tools for retrieval; never use shell network commands such as
   `curl` or `wget`. Do not open the overview or search unrelated sections first.
   Check units, frames, model structure, geometry, and initialization first.
3. Select the smallest checks that can falsify the claim: finite states, invariants,
   contact onset and penetration, constraints, actuator/travel limits, timestep or
   substep sensitivity, determinism, repeated seeds, and reference comparisons as
   applicable. Inspect the relevant trajectory and exercise checks with known-valid,
   invalid, and misleading-output controls. For a plan, provide this minimal matrix
   and stop; do not execute or retrieve evidence the user did not request. If the
   trajectory or reference is absent, inspect its expected location once, report
   what is missing, and stop without a broad search.
4. Report passed, failed, and unverified claims separately, but include only the
   version/environment, selected route, horizon, bounds, commands, evidence, and
   one blocker if present. Prefer state and independent checks over
   a conflicting success flag. Import, stable rollout, reward, and hardware transfer
   are separate claims; simulation evidence alone cannot establish real-world transfer.

Supported Newton version: 1.7.0 only. For another version, warn and stop before
version-specific conclusions until interfaces and evidence are revalidated.
