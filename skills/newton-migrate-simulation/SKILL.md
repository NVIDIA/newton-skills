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

1. Choose the request mode before using tools. For a migration plan, provide the
   direct documentation route, next representative port, and comparisons without
   running importers; consult documentation when needed to establish support. For
   implementation, reuse supplied facts and otherwise run this probe once: `python -c "import sys, newton; from importlib.metadata import version; print(sys.executable); print(version('newton')); print(newton.__file__)"`.
   Inspect the device only when
   it affects the port. Collect missing source facts once. If no source simulator
   or source assets exist, stop this workflow, state that `newton-usage`
   owns the task, and follow it. Record whether the goal is asset reuse, controller
   reuse, or behavioral parity. Inventory
   units, frames, assets, joints, drives, limits, contacts, collision geometry,
   controller semantics, used features, and available reference runs.
2. Select documentation matching the installed Newton release. Use the [legacy Warp migration map](https://newton-physics.github.io/newton/latest/migration.html)
   only for a source built with Warp's former simulation module. For other sources,
   route directly to
   [conventions](https://newton-physics.github.io/newton/latest/concepts/conventions.html),
   [USD parsing](https://newton-physics.github.io/newton/latest/concepts/usd_parsing.html),
   [articulations](https://newton-physics.github.io/newton/latest/concepts/articulations.html),
   [collisions](https://newton-physics.github.io/newton/latest/concepts/collisions.html),
   and the [solver capability guide](https://newton-physics.github.io/newton/latest/solvers/index.html)
   only as required by the source inventory. Prefer the installed wheel
   documentation when available; otherwise select matching hosted documentation.
   The links above are entrypoints, not a claim about the installed version. Read
   the sections and public API entries needed to resolve each feature mapping;
   follow focused references when the inventory requires additional guidance. When
   the user only needs a documentation location, copy the URL without opening it. Use browser or documentation tools for retrieval; never use shell
   network commands such as `curl` or `wget`. Do not browse generic migration
   material first. Map only documented features and distinguish successful loading
   from properties the backend consumes.
3. For a plan, return only the next minimal port and its comparisons; do not run
   imports or broad searches. For implementation, port a representative scene,
   inspect effective values and warnings, and record retained, remapped,
   unsupported, and intentionally changed features instead of copying defaults.
   If source assets or a reference run are absent, inspect the expected location
   once, report what is missing, and stop without a broad search.
4. Compare structure, conventions, uncontrolled motion, a simple command, and
   relevant contacts with fixed task bounds. Require an additional meaningful
   asset configuration only when parity is claimed. Report only versions/environment,
   selected route, commands, mappings, evidence, and all material unresolved
   differences. Asset/controller reuse needs no parity objective; without a source
   reference, parity remains unverified.

Newton compatibility has not been validated across releases. Verify documented
interfaces and backend behavior for the installed release before applying mappings.
Loading is not parity, and simulator parity is not real-world validation.
