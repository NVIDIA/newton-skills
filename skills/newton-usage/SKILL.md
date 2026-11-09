---
name: newton-usage
description: Set up, build, or debug physics simulations with the released Newton Python package. Use when choosing supported simulation components, finding documentation and examples, adapting a scene, or diagnosing simulation and runtime problems.
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
source checkout is optional. Preserve supplied assets, conventions, environment,
and explicit choices.

1. Establish the requested behavior or observed failure. Before building, define
   acceptance criteria: the trajectory or command to exercise, simulation horizon,
   observable state, and task-specific physical bounds. Reuse supplied environment
   facts; otherwise identify the installed version and package with
   `python -c "import sys, newton; from importlib.metadata import version; print(sys.executable); print(version('newton')); print(newton.__file__)"`.
   Establish the solver and CPU/GPU environment when relevant. Follow the harness
   and user's execution permissions; a planning request may still need read-only
   documentation lookup to establish supported configurations. Distinguish
   proposed commands and checks from executed ones.
2. Select documentation matching the installed release from the
   [Newton documentation](https://newton-physics.github.io/newton/). Flag any
   mismatch before relying on an interface or feature. If the installed wheel
   provides `python -m newton.docs`, use its matching snapshot; older wheels may
   require hosted documentation. A supplied matching checkout's `docs/` is also
   usable without requiring a clone. Read only relevant sections and follow
   linked guidance when needed to resolve a concrete question:
   - Setup and modeling: installation, tutorials, conventions, solver guides,
     and the API reference.
   - Debugging: FAQ, simulation tuning, collisions and contacts, solver
     observables, and viewers and debugging; follow solver-specific guidance.
   - Asset reuse: importer documentation, conventions, articulations, and the
     solver's feature support. Use the legacy Warp migration guide only for
     Warp's former simulation module. Distinguish successful import from
     supported behavior and behavioral parity with a source reference.
3. Start with the simplest documented solver configuration that supports the
   required components and interactions. Consider coupled solvers only when one
   solver cannot represent the required interaction. State unsupported needs.
   Discover packaged examples with `python -m newton.examples --list` and inspect
   a relevant example with `python -m newton.examples <example_name> --help`.
   Adapt the closest suitable example or the documented minimal simulation.
   Do not install dependencies or extras without authorization; report missing
   requirements and preserve the user's Newton version and source assets.
4. Build the smallest representative scene or reduce a failure while retaining
   its symptom. Use documented public APIs, inspect effective model and solver
   values, and make a focused change. Check finite state, physical bounds such as
   penetration and joint travel, and the requested behavior over the agreed
   horizon; rendered appearance or successful execution alone is insufficient.
   Recheck the original scene after a reduced case succeeds. If a specialized
   Newton skill is installed and provides relevant additional diagnosis,
   optimization, or independent verification, use it without requiring that skill
   for ordinary setup and construction.
5. Report the documentation used, commands supplied or executed, measured results
   against the acceptance criteria, and material limitations. If execution is not
   permitted or required assets are unavailable, give the next concrete check and
   leave the outcome unverified.

Newton compatibility has not been validated across releases. Verify the installed
release's documented interfaces and behavior before claiming support.
