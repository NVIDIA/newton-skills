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

1. Establish the claim, intended use, solver, acceptance criteria, and evidence
   needed. Follow user and harness permissions; planning can include read-only
   documentation lookup, while measurements require authorized execution.
   Reuse supplied environment facts; otherwise first collect metadata with
   `python -c "import sys; from importlib.metadata import version; print(sys.executable, flush=True); print(version('newton'), flush=True)"`.
   Only if imports are permitted, separately run
   `python -c "import newton; print(newton.__file__)"` and retain any import
   error alongside the metadata. Keep both commands in the task's existing
   environment, preserving wrapper-provided variables and project context. Use
   its verified interpreter directly only when those settings are preserved;
   otherwise retain the required wrapper. Before either probe, confirm that it
   selects that
   exact environment; existence alone does not establish selection. With uv, use
   the intended project explicitly, or `--active` when the active environment is
   intended. Use `uv run --no-sync --frozen` only with that confirmed existing
   environment. Do not use probe options that create an
   environment, sync dependencies, install extras, or update a lockfile. If no
   non-mutating execution path is available, report the blocker and obtain any
   needed setup authorization before proceeding; do not probe another environment.
   Ask for the interpreter or wrapper if unknown.
   Inspect the device only when it affects the claim. For construction, use
   `newton-usage`; for root-cause correction, use `newton-debug-simulation`; for
   migration, use `newton-migrate-simulation`; for speed, use `newton-performance`.
   Follow the relevant skill only when installed. Otherwise continue the requested
   task using matching public documentation instead of stopping at a missing
   handoff or requiring another skill to be installed. Derive physical bounds
   from the task or reference, never defaults.
2. Use documentation matching the installed release. The links below are
   moving `latest` entrypoints and may differ from the installed release;
   select matching release documentation before relying on a parameter. Select the
   relevant route for each claim or check:
   [conventions](https://newton-physics.github.io/newton/latest/concepts/conventions.html)
   for units, frames, and spatial quantities; [mass and inertia](https://newton-physics.github.io/newton/latest/concepts/mass_inertia.html)
   for physical properties; [articulations](https://newton-physics.github.io/newton/latest/concepts/articulations.html)
   for state and joints; [collisions](https://newton-physics.github.io/newton/latest/concepts/collisions.html)
   for contact evidence; [actuators](https://newton-physics.github.io/newton/latest/concepts/actuators.html)
   for actuator models and limits; [solver observables](https://newton-physics.github.io/newton/latest/concepts/solver_observables.html)
   for diagnostic outputs; or [solver capabilities](https://newton-physics.github.io/newton/latest/solvers/index.html)
   for backend support. Prefer matching bundled documentation when available.
   Follow focused guides and API entries for every required check; a claim
   involving both travel limits and penetration needs both relevant routes. When
   the user only needs a documentation location, copy the URL without opening it. Use browser or
   documentation tools for retrieval; never use shell network commands such as
   `curl` or `wget`. Do not open the overview or search unrelated sections first.
   Check units, frames, model structure, geometry, and initialization first.
3. Select the smallest checks that can falsify the claim: finite states, invariants,
   contact onset and penetration, constraints, actuator/travel limits, timestep or
   substep sensitivity, determinism, repeated seeds, and reference comparisons as
   applicable. Inspect the relevant trajectory and exercise checks with known-valid,
   invalid, and misleading-output controls. For a plan, provide this minimal matrix
   and label the checks as proposed. Require external references only for
   claims that need a comparison; finite-state and authored-bound checks can use
   supplied trajectories and model requirements alone. If evidence required by
   the selected claim is missing, inspect its expected location once. In a plan,
   report the gap and describe collection without executing it. When evidence
   collection is explicitly requested and authorized, run the existing rollout
   to obtain the missing trajectory if it is available. Otherwise report the
   missing input and leave the claim unverified, without a broad search or
   inventing measurements. Building a missing simulation belongs to newton-usage.
4. Report passed, failed, and unverified claims separately, but include only the
   version/environment, selected route, horizon, bounds, commands, evidence, and
   one blocker if present. Prefer state and independent checks over
   a conflicting success flag. Import, stable rollout, reward, and hardware transfer
   are separate claims; simulation evidence alone cannot establish real-world transfer.

Newton compatibility has not been validated across releases. Verify matching
interfaces, backend behavior, and evidence before a version-specific conclusion.
