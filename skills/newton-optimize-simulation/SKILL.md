---
name: newton-optimize-simulation
description: Measure or improve Newton runtime, startup, memory, or training throughput for a correct workload while preserving physical checks. Not for diagnosing invalid or unstable simulation behavior.
metadata:
  author: Anthony Angeles <aangeles@nvidia.com>
  tags:
    - newton
    - physics-simulation
    - performance
---

# Optimizing a Newton Simulation

Improve a measured workload without invalidating the simulation or comparing
different timing scopes.

1. Choose the request mode before using tools. For a profiling or optimization
   plan, provide the direct documentation route and one bounded experiment without
   running profilers or opening documentation. For measurement or implementation,
   reuse supplied facts and otherwise run this probe once: `python -c "import sys, newton; from importlib.metadata import version; print(sys.executable); print(version('newton')); print(version('warp-lang')); print(newton.__file__)"`.
   Inspect GPU availability only when it affects the experiment. Collect missing
   workload facts once. Route instability, invalid states, or unexplained physics
   to `newton-debug-simulation`. Stop this workflow, state that the debugging skill
   owns the task, and follow it. Record the workload, objective, timing boundary,
   and fixed fidelity checks. Separate startup/compilation, warm stepping,
   rendering, transfers, memory, and training.
2. For Newton 1.7.0, route directly to [simulation tuning](https://newton-physics.github.io/newton/1.7.0/concepts/simulation_tuning.html)
   for fidelity/performance tradeoffs, [solver capabilities](https://newton-physics.github.io/newton/1.7.0/solvers/index.html)
   for backend costs, [collisions](https://newton-physics.github.io/newton/1.7.0/concepts/collisions.html)
   for contact representation and capacity, and the [tutorials](https://newton-physics.github.io/newton/1.7.0/guide/tutorials.html)
   for Newton graph-capture usage. For instrumentation, use the profiling guide
   matching the installed Warp release: [Warp 1.17](https://nvidia.github.io/warp/v1.17/user_guide/execution_and_performance/profiling.html)
   or [Warp 1.18](https://nvidia.github.io/warp/v1.18/user_guide/execution_and_performance/profiling.html).
   Open at most one Newton route, plus the matching Warp profiling page only when
   instrumentation details are required. When the user only needs a documentation
   location, copy the URL without opening it. Use browser or documentation tools
   for retrieval; never use shell network commands such as `curl` or `wget`. Do
   not search either documentation root. Choose instrumentation for eager Python
   or captured GPU execution and account for warm-up, synchronization, profiler
   overhead, and privileges.
3. If the workload or profiler prerequisite is absent, inspect its expected
   location once, report what is missing, and stop. For a plan, define one bounded
   experiment and stop without running a profiler.
   For execution, measure a baseline only until one actionable bottleneck is found,
   then change one documented factor or a bounded coupled set. Never apply universal
   tuning values. Keep allocations and unintended synchronization outside timing.
4. Repeat comparable before/after measurements and re-run simulation-validity
   checks. Revert a change that misses the objective or violates fidelity. Report
   only version/environment, selected route, workload and boundary, change,
   variance, fidelity evidence, and one remaining cost or blocker. If elevated
   privileges are needed, provide the exact user-run command and stop. CPU evidence
   or source inspection does not establish a GPU speedup.

Supported Newton version: 1.7.0 only. For another version, warn and stop before
version-specific changes until profiler and runtime interfaces are verified.
