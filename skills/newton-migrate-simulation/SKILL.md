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
   running importers or opening documentation. For implementation, reuse supplied
   facts and otherwise run this probe once: `python -c "import sys, newton; from importlib.metadata import version; print(sys.executable); print(version('newton')); print(newton.__file__)"`.
   Inspect the device only when
   it affects the port. Collect missing source facts once. If no source simulator
   or source assets exist, stop this workflow, state that `newton-build-simulation`
   owns the task, and follow it. Record whether the goal is asset reuse, controller
   reuse, or behavioral parity. Inventory
   units, frames, assets, joints, drives, limits, contacts, collision geometry,
   controller semantics, used features, and available reference runs.
2. For Newton 1.7.0, use the [legacy Warp migration map](https://newton-physics.github.io/newton/1.7.0/migration.html)
   only for a source built with Warp's former simulation module. For other sources,
   route directly to
   [conventions](https://newton-physics.github.io/newton/1.7.0/concepts/conventions.html),
   [USD parsing](https://newton-physics.github.io/newton/1.7.0/concepts/usd_parsing.html),
   [articulations](https://newton-physics.github.io/newton/1.7.0/concepts/articulations.html),
   [collisions](https://newton-physics.github.io/newton/1.7.0/concepts/collisions.html),
   and the [solver capability guide](https://newton-physics.github.io/newton/1.7.0/solvers/index.html)
   only as required by the source inventory. Open at most one concept or guide
   page, plus the relevant public API entry only for an importer or symbol being
   mapped. When the user only needs a documentation location, copy the URL without
   opening it. Use browser or documentation tools for retrieval; never use shell
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
   selected route, commands, mappings, evidence, and one unresolved difference
   if present. Asset/controller reuse needs no parity
   objective; without a source reference, parity remains unverified.

Supported Newton version: 1.7.0 only. For another version, warn and stop before
version-specific mappings are applied. Loading is not parity, and simulator parity
is not real-world validation.
