# Worlds, Batching, Viewers, and Benchmarking

## Contents
- Building many worlds
- Memory scaling
- Per-world parameters, randomization, and resets
- Rollout and optimization workloads
- Viewers and rendering cost
- Benchmarking Newton
- Metrics and reporting

Docs: [Worlds](https://newton-physics.github.io/newton/stable/concepts/worlds.html), [Visualization](https://newton-physics.github.io/newton/stable/guide/visualization.html), [Development › Benchmarks](https://newton-physics.github.io/newton/stable/guide/development.html).

## Building many worlds

```python
template = newton.ModelBuilder()
template.add_urdf(...)                                   # or add_usd / add_mjcf / procedural
template.approximate_meshes("convex_hull")               # per-template work happens BEFORE replicate
scene = newton.ModelBuilder()
scene.replicate(template, world_count, spacing=(0.0, 0.0, 0.0))
scene.add_ground_plane()                                  # one global shape, not one per world
scene.color()                                             # if using VBD (or call template.color() before replicate)
model = scene.finalize()
```

- **Build once, replicate.** Model building is CPU Python, and importing a USD/URDF per world wastes setup time. `replicate` merges all copies in one batched pass.
- **Do template work before replication:** mesh approximation, SDF builds, and removing unneeded collision geometry. Afterwards the work, and often the memory, is repeated per world.
- **Use `spacing=(0, 0, 0)`.** Worlds don't collide with each other, so overlapping them is fine, and float32 precision stays better near the origin. Offset them visually with the viewer's world offsets.
- **Keep global entities (`world=-1`) few.** They interact with every world.
- **Validation cost:** `finalize(skip_all_validations=True)` skips model validation for large, known-good models. Use it only after the model has been validated once.
- **Fast USD import:** imports are faster when mass, inertia, and COM are fully authored, because Newton can skip computing them.
- **Custom per-world kernels:** launch 2D, `dim=(world_count, max_per_world)`, using the model's per-world start arrays, with a bounds check. Don't launch one kernel per world.

## Memory scaling

Every per-world capacity is multiplied by `world_count`:
- MuJoCo `nconmax`/`njmax`/`njmax_nnz`;
- the default NxN/SAP `shape_pairs_max` (worst case per world);
- VBD contact buffers;
- sensor buffers;
- `requires_grad` buffers.

At thousands of worlds, an over-generous per-world default becomes gigabytes. It also slows every kernel that scans capacity.

- **Size from measured peaks.** Sweep the world count under the memory budget, and check both memory and per-step time.
- **Read memory correctly.** `wp.get_mempool_used_mem_current/high` shows Warp's own usage. `nvidia-smi` and device free memory include pool reservations and other processes.
- **Remove contacts at the source for contact-free studies.** Strip collision geometry before replication and disable contacts. Don't raise constraint capacity to absorb contacts you don't need.

## Per-world parameters, randomization, and resets

- **Randomize on the GPU.** Write parameters for all worlds in one kernel with per-world seeds (`wp.rand_init(seed, world_id)`). Avoid a Python loop with an upload per world. Then call `solver.notify_model_changed(<narrow flags>)` once.
- **Use `ArticulationView`** (`newton.selection.ArticulationView`) for structured get/set by articulation:
  - `get_attribute(name, source)` launches a gather. It does not synchronize.
  - `set_attribute(name, target, values)` expects a Warp array of the right dtype. Python lists and NumPy arrays trigger an upload and allocation each call.
- **Gravity per world:** pass one per-world gravity array to `model.set_gravity(...)`. A loop of per-world calls reads back and re-uploads on each call.
- **Partial resets:**
  - `solver.reset(state, world_mask=mask)`: the mask is a `wp.array(dtype=bool)` of length `world_count + 1`; the last entry selects global entities.
  - `newton.eval_fk(model, joint_q, joint_qd, state, mask=...)` recomputes body poses for selected articulations.
  - Use a boolean mask on the device rather than a variable-length index list, so the reset can be captured or launched with a fixed size.
- **RNG semantics:** use per-world seeds or counters on the device. A shared RNG stream makes world 0's result change with batch size. A Python-side seed is frozen inside a graph.

## Rollout and optimization workloads

These lessons come from system identification, policy replay, and parameter search:

- **Keep the whole evaluation on the GPU.** Upload trajectories once and keep the time index on the device. Write targets with a kernel inside the graph. Accumulate errors per world on the device, and download one objective vector per evaluation. Moving from per-step host scoring to this structure gave 2–20× speedups in measured cases.
- **Capture everything per step.** Capturing the main step but leaving an auxiliary per-step computation eager can erase the batching gain.
- **Batch episodes as worlds, without changing the semantics:**
  - Group experiments by identical layout and `dt` rather than padding.
  - Normalize losses per world, not divided by the world count by accident.
  - Keep optimizer state independent per world.
  - Check that world 0 alone matches world 0 in the batch.
- **More worlds is not always more progress.** Throughput rises until the GPU saturates. Beyond that, latency per step grows and the per-world buffers dominate memory. For population-based optimization, changing the population size changes the search. Compare at equal population, or compare objective quality per wall-clock time.
- **Keep the guards.** Preserve NaN/instability checks when moving scoring to the device, and return finite penalties for unstable candidates, so one bad world doesn't poison the batch or the graph.

## Viewers and rendering cost

- **Render once per frame,** after `step()`. Never render or log inside the substep loop.
- **`log_state` is mostly GPU work.** Each call still has a cost, though. Some viewers and backends (USD recording, some instance types) read data back to the host. Minimize the number of models and calls logged per frame.
- **Contacts:** `log_contacts` with contacts shown reads the contact count back to the host every frame. Disable it when timing.
- **Many worlds:** with large world counts, restrict rendering with `viewer.set_visible_worlds(...)`, or use the examples' `--max-worlds`.
- **Headless runs:** use `ViewerNull` (`--viewer null`) to measure simulation. Measure rendering separately if it matters to the application.
- **`--render-fps`** throttles rendering in the examples without changing simulation timing.

## Benchmarking Newton

- **Examples:** `python -m newton.examples <name> --benchmark [SECONDS]` forces the null viewer. It warms up for a few frames, synchronizes, and reports FPS. Use `--world-count N` to scale, and `--warp-config KEY=VALUE` to try Warp config options.
- **ASV suites (optional, needs a Newton source checkout):** the Newton repository's `asv/benchmarks/` cover MuJoCo, contacts, cloth, cables, MPM, selection, sensors, and setup/compile time. They are useful when contributing to Newton or bisecting a regression; wheel users don't need them.
- **Your own scripts:**
  - Build the model, capture, and replay once untimed.
  - Synchronize, time N replays with CUDA events or synchronized wall time, and synchronize again.
  - Report setup (build, finalize, JIT, capture) separately from steady-state stepping.
- **CUDA-event timing of solver functions:** `newton.utils.EventTracer` / `event_scope`.
- **Attributing regressions:**
  - Pin Warp, the driver, and the workload, and bisect Newton (or the reverse).
  - Change one dependency at a time.
  - Record which `newton`/`warp` modules actually imported (`module.__file__`), since `PYTHONPATH` or editable installs can shadow the installed version.
  - Use ablations: collision only, solver only, no contacts.

## Metrics and reporting

- **Throughput:** world-steps per second = `frames × substeps × worlds / time`.
- **Latency:** ms per frame or per substep. Report p95 as well as the median when frame time varies with contact.
- **Real-time factor:** `simulated_time × worlds / wall_time`, or per world.
- **Memory:** Warp mempool high-water mark, measured per configuration.
- **Solver effort:** iterations used (MuJoCo exposes solver iteration counts) and contact/constraint counts vs. capacity.
- **Accuracy alongside every timing:** the metric from the solver reference, finite state, and no overflow.

State the hardware, Newton/Warp/driver versions, world count, substeps, iterations, collision cadence, and warm-up policy. State whether the time includes collision, rendering, readbacks, and resets.
