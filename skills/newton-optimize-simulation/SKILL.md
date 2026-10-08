---
name: newton-optimize-simulation
description: Measure and improve a Newton simulation’s runtime, startup, memory or training throughput while preserving required physical behavior.
metadata:
  target-newton-version: "1.6.0"
  validation-status: "early-v2; behavioral validation pending; not for release"
---

Establish the user's performance objective, workload, device and fidelity
constraints before changing the simulation. Separate startup/compilation,
warm steady-state stepping, rendering, transfers and end-to-end training.

Use the installed Newton release and matching public documentation and packaged
examples. This candidate targets 1.6.0 for evaluation; no supported version range
has been validated. Warn on other versions and check interfaces before proceeding.
Read the applicable versioned documentation directly when known. Otherwise use
https://newton-physics.github.io/newton/1.6.0/genindex.html to locate the relevant
API, concept or packaged example. Read the needed section, not the whole site.
If search fails, use index/navigation and installed public signatures. No source
checkout or other skill is required.

Route to applicable Warp profiling and Newton collision/solver guidance. Use
instrumentation appropriate to eager Python versus captured GPU execution.
Measure comparable work with warm-up, synchronization and profiler overhead
accounted for. Keep host waiting separate from device timing. If privileged
profiling is necessary, prepare the command for the user; do not require agent sudo.

Choose an optimization from a measured bottleneck. Avoid adding synchronization
or allocation to the timed hot path. For interacting contact/collision/solver
settings, evaluate a small justified sweep against physical checks rather than
applying a universal preset. Preserve timestep, simulated duration, control and
collision semantics unless a tradeoff is explicitly accepted.

Keep the timing boundary, workload and acceptance bounds fixed when attributing
a speedup. Retain raw observations, failed variants and workload-specific regressions;
label published measurements as external evidence, not your own results.
Compare repeated before/after measurements and re-run validity checks. Revert
changes that fail the objective or fidelity constraints. If GPU execution is
unavailable, report that limitation; source inspection alone cannot establish a
GPU speedup. Report timing scope, variance, changed factors and remaining costs.
