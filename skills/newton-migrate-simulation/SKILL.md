---
name: newton-migrate-simulation
description: Migrate existing simulator assets, controllers, or behavior to Newton with explicit convention, feature, and parity checks. Not for a new scene with no source assets or simulator.
metadata:
  author: Anthony Angeles <aangeles@nvidia.com>
  tags:
    - newton
    - physics-simulation
    - migration
---

# Migrating a Simulation to Newton

Port the smallest representative scene while preserving source assets and making
intentional differences explicit.

1. Establish the requested reuse or parity goal and follow user and harness
   execution permissions. Planning can use read-only documentation to establish
   support; describe proposed imports and comparisons without executing them.
   For implementation, reuse supplied facts; otherwise collect metadata with
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
   Inspect the device only when
   it affects the port. Collect missing source facts once. If neither a source
   simulator nor source assets are available, stop this workflow and use
   `newton-usage` for new construction when available; otherwise provide setup
   and modeling guidance from release-matched public documentation. Record
   whether the goal is asset reuse, controller reuse, or behavioral parity.
   Inventory units, frames, assets, joints, drives, limits, contacts, collision geometry,
   controller semantics, used features, and available reference runs.
2. For planning before installation, select documentation for the user's stated
   target release. If the target is unknown, clarify it or keep the plan
   version-neutral and label that assumption. Before implementation, verify the
   installed release. If it differs from the requested target, stop before
   version-specific implementation until the target environment is supplied or
   the user explicitly approves changing the target. Do not silently retarget the
   port. Select documentation matching the confirmed target. Use the
   [legacy Warp migration map](https://newton-physics.github.io/newton/latest/migration.html)
   only for a source built with Warp's former simulation module. For other sources,
   route directly to
   [conventions](https://newton-physics.github.io/newton/latest/concepts/conventions.html),
   [USD parsing](https://newton-physics.github.io/newton/latest/concepts/usd_parsing.html),
   [articulations](https://newton-physics.github.io/newton/latest/concepts/articulations.html),
   [collisions](https://newton-physics.github.io/newton/latest/concepts/collisions.html),
   and the [solver capability guide](https://newton-physics.github.io/newton/latest/solvers/index.html)
   only as required by the source inventory. Prefer the installed wheel
   documentation when available; otherwise select matching hosted documentation.
   The links above are moving `latest` entrypoints, not a claim about the
   planned or installed version. Read
   the sections and public API entries needed to resolve each feature mapping;
   follow focused references when the inventory requires additional guidance. When
   the user only needs a documentation location, copy the URL without opening it.
   Use browser or documentation tools for retrieval; never use shell
   network commands such as `curl` or `wget`. Do not browse generic migration
   material first. Map only documented features and distinguish successful loading
   from properties the backend consumes.
3. For a plan, return only the next minimal port and its comparisons; do not run
   imports or broad searches. For implementation, port a representative scene,
   inspect effective values and warnings, and record retained, remapped,
   unsupported, and intentionally changed features instead of copying defaults.
   During implementation, if required source assets are absent, inspect their
   expected location once, report what is missing, and stop without a broad search. A missing source
   reference blocks a behavioral-parity claim, not asset or controller reuse;
   continue the requested reuse checks and leave parity unverified.
4. For a plan, describe the structure, convention, control, and contact checks
   to perform, plus source comparisons only when parity is requested. Do not
   present proposed checks as results. During authorized implementation, verify
   imported structure, conventions, controls, and contacts against the reuse
   criteria. When parity is requested and a source reference is available,
   compare uncontrolled motion, a simple command, and relevant contacts with
   fixed task bounds, including another meaningful asset configuration.
   Report versions/environment,
   selected route, commands, mappings, evidence, and all material unresolved
   differences. Asset/controller reuse needs no parity objective; without a source
   reference, parity remains unverified.

Newton compatibility has not been validated across releases. Verify documented
interfaces and backend behavior for the installed release before applying mappings.
Loading is not parity, and simulator parity is not real-world validation.
