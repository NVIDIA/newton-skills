---
name: newton-performance
description: Measure or improve the runtime, startup time, memory use, or throughput of a Newton simulation that already behaves correctly, or review a Newton step loop for performance problems such as CUDA graph capture mistakes and host synchronization. Not for setting up simulations, general solver or API questions, debugging unstable or incorrect physics without a performance goal, or optimizing Warp code that does not use Newton.
---

# Newton Performance

Make a correct Newton workload faster without changing its results. Newton's
documentation holds the technical guidance; this skill orders the work and
defines what counts as evidence.

## 1. Scope the request

- If the simulation is unstable, produces invalid states, or the user's goal is
  correctness rather than speed, use `newton-usage` instead and stop here.
- Decide the mode. A **plan** request (how should I profile or optimize this?)
  gets a documentation route and one bounded experiment; do not run tools. A
  **review** request (is this loop correct and fast?) gets findings against the
  documentation; do not run tools unless asked. A **measure** or **implement**
  request runs the workflow below.
- Record the workload, the objective, and the timing scope. Keep these scopes
  separate, because they have different causes: startup (import, model build,
  kernel compilation), warm stepping, rendering, host/device transfers, memory,
  and training throughput.
- Record the fidelity checks that must still pass after a change, for example
  finite state, no contact overflow, and a trajectory or force metric against a
  reference run.

## 2. Gather context once

Reuse facts the user already gave. Otherwise run once:

```
python -c "import sys, newton; from importlib.metadata import version; print(sys.executable, version('newton'), version('warp-lang'), newton.__file__)"
```

Check GPU availability only when the experiment depends on it. If the workload,
a required profiler, or required permissions are missing, report exactly what
is missing and stop. If elevated privileges are needed (for example GPU
performance counters), give the exact command for the user to run and stop.

## 3. Route to the documentation

Use the Newton documentation for the installed release,
`https://newton-physics.github.io/newton/<version>/`, and flag a mismatch
before relying on an API or default. Open only the page the task needs:

- [Performance](https://newton-physics.github.io/newton/latest/guide/performance.html):
  CUDA graph capture, odd substep counts, host synchronization, buffer
  capacity, multiple worlds, and benchmarking. If the installed release does
  not have this page, use `latest` and verify each API against the installed
  version's API reference.
- [Simulation tuning](https://newton-physics.github.io/newton/latest/concepts/simulation_tuning.html):
  trading substeps, iterations, and contact settings against accuracy.
- [Collisions](https://newton-physics.github.io/newton/latest/concepts/collisions.html):
  broad phase, geometry, contact capacity, and collision frequency.
- [Solvers](https://newton-physics.github.io/newton/latest/solvers/index.html)
  and the API reference: solver options, capacities, and `ModelFlags`.
- [Warp profiling](https://nvidia.github.io/warp/stable/user_guide/execution_and_performance/profiling.html)
  for instrumentation, using the page for the installed Warp version.

When the user only needs a documentation location, give the URL without
opening it.

## 4. Measure, change, verify

1. Choose instrumentation that fits the execution: eager Python stepping and
   captured graph replay need different tools and timing boundaries. Exclude
   warm-up, compilation, and the first graph launch from steady-state timing,
   synchronize at the timing boundaries, and account for profiler overhead so
   the before and after runs measure the same work.
2. Measure a baseline until one actionable cost is identified. Do not start
   from universal tuning values.
3. Change one factor at a time. When settings interact (for example collision
   frequency, contact model, mesh resolution, and gap), run a small bounded
   sweep over the coupled set instead.
4. Repeat comparable before and after measurements to estimate variance, and
   re-run the fidelity checks from step 1.
5. Keep a change only if it meets the objective and passes the fidelity
   checks; otherwise revert it.

## 5. Review checks

When reviewing a Newton step loop, check these against the Performance guide
and cite the section:

- the whole frame, including collision, is captured in one graph and warmed up
  before capture;
- an odd substep count with a plain state swap inside a captured frame;
- arrays replaced instead of written in place after capture, or Python values
  expected to change between replays;
- host reads (`.numpy()`, contact counts, printing) inside the frame;
- capacities sized from defaults rather than measured peaks, and overflow never
  checked;
- rendering or logging inside the substep loop, or included in simulation
  timings.

Credit any correct fix the documentation supports, not only the first one
listed there.

## 6. Report

Report the Newton and Warp versions, the environment, the documentation used,
the workload and timing scope, the change, the before and after measurements
with variance, the fidelity evidence, and the largest remaining cost or
blocker. Label proposed experiments separately from measurements actually
collected. CPU measurements or source inspection do not establish a GPU
speedup.

Compatibility with specific Newton releases has not been validated.
