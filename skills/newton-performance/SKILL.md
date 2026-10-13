---
name: newton-performance
description: Write, review, and speed up NVIDIA Newton physics simulations without breaking the physics. Use when building or optimizing a Newton step loop, capturing it in a CUDA graph, choosing substeps/iterations/collision cadence, sizing contact and constraint buffers, batching many worlds, picking solver settings, or diagnosing slow or silently wrong Newton runs. Covers the odd-substep graph-capture trap, frozen Python state inside graphs, host syncs from viewers/sensors/contact counts, notify_model_changed, and benchmarking at equal accuracy. Warp performance guidance also applies; use Warp skills or docs for kernel-level work.
---

# Newton Performance

Newton is built on NVIDIA Warp, so Warp's performance guidance applies to everything here. This skill covers the Newton layer: the step loop, collisions, solvers, worlds, and how to measure them. For kernel-level work (custom kernels, memory access, atomics, tiles, compile time, Nsight profiling), also consult:
- any installed Warp skills, including those published in the [Warp repository](https://github.com/NVIDIA/warp/tree/main/skills);
- the Warp docs on [performance and execution](https://nvidia.github.io/warp/stable/user_guide/execution_and_performance.html), [profiling](https://nvidia.github.io/warp/stable/user_guide/execution_and_performance/profiling.html), and the [CUDA C++ Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/), most of which carries over to Warp kernels.

Written against the released Newton 1.6.1 and Warp 1.18.0. APIs move quickly, so confirm signatures in the installed version (`python -c "import newton, warp; print(newton.__version__, warp.__version__)"`) before relying on any argument named here.

## Ground rules

1. **Measure before and after, at equal accuracy.** A faster run that drops contacts, inverts elements, slows the motion, or drifts from the reference is not an optimization. Before reading any timing, check:
   - the state is finite;
   - contact and constraint counts are below their capacities;
   - the trajectory matches an eager or converged reference.
2. **Find the dominant cost before tuning.** In order, it is usually one of:
   - host launch overhead (missing graph);
   - host syncs;
   - collision detection;
   - solver iterations or substeps;
   - oversized buffers multiplied by the world count;
   - rendering.
3. **Change one thing at a time** and keep the numbers.

## The highest-value practices

### 1. Capture the whole frame in one CUDA graph

Newton's own examples typically do this: build everything once, then capture `simulate()`, which contains all substeps, the collision pass, and force clearing. Replay it once per frame. Frames made of many small launches (small scenes, few worlds) often get several times faster this way. GPU-bound workloads gain little, so measure.

```python
# build once (all allocations happen here, before capture)
self.state_0, self.state_1 = model.state(), model.state()
self.control = model.control()
self.pipeline = newton.CollisionPipeline(model)       # before the solver for VBD
self.contacts = self.pipeline.contacts()
self.solver = newton.solvers.SolverXPBD(model)

self.simulate()                     # warm-up: JIT, lazy solver buffers
# ...restore initial state here if the warm-up must not count...
with wp.ScopedCapture() as cap:     # guard with device.is_cuda if CPU must also work
    self.simulate()
self.graph = cap.graph

def step(self):
    wp.capture_launch(self.graph) if self.graph else self.simulate()
```

Capture includes collision, control preparation, and scoring/metric kernels. Keep all of them inside one graph rather than one graph per substep.

### 2. Handle odd substep counts. They silently corrupt graph replay.

The usual `state_0, state_1 = state_1, state_0` swap is Python. It runs once, at capture time, and only rebinds names; the graph records fixed buffer addresses. With an **odd** number of substeps, each replay starts from the buffer that holds the result of substep N‑1, not substep N. The simulation advances N‑1 substeps per frame while paying for N. It runs in slow motion with no error.

The fix is documented on `State.assign`: on the last odd substep, copy instead of swapping, so every replay starts and ends in `state_0`.

```python
def simulate(self):
    for i in range(self.sim_substeps):
        self.state_0.clear_forces()
        self.pipeline.collide(self.state_0, self.contacts)
        self.solver.step(self.state_0, self.state_1, self.control, self.contacts, self.sim_dt)
        if self.sim_substeps % 2 == 1 and i == self.sim_substeps - 1:
            self.state_0.assign(self.state_1)          # canonical buffer for replay
        else:
            self.state_0, self.state_1 = self.state_1, self.state_0
```

Alternatives:
- Force an even count (`if substeps % 2: substeps += 1`). Note that this changes `dt`.
- Raise an error on odd counts.
- Alternate two graphs with opposite bindings. This saves one copy per frame, but callers must pick the right graph and the right readable state every frame.

The same rule applies to double-buffered actuator state. Some solvers (MPM, Style3D, some cloth/cable setups) require even counts for capture. Any test that compares eager and captured runs must include an odd count.

### 3. Remember that only buffer *contents* change between replays

A captured graph freezes all of the following:
- array pointers;
- launch dimensions;
- Python scalars (`dt`, indices, flags);
- every Python `if`/`%` decision made during capture.

Inside Newton this means:
- `SolverMuJoCo(update_data_interval=k)` and `SolverFeatherstone(update_mass_matrix_interval=k)` decide in Python. Make the substeps per graph a multiple of `k` (examples pass `update_mass_matrix_interval=sim_substeps`). Otherwise the branch pattern seen at capture time repeats forever.
- `set_collision_frequency(...)`, VBD history-update toggles, and the speculative-contact `dt` passed to `collide()` all require **recapture** after they change.
- Write controls, targets, and resets **into** the existing arrays, with a kernel, `wp.copy`, `array.assign`, or `ArticulationView.set_attribute` given a Warp array. Never do `control.joint_target_q = wp.array(...)` after capture: the graph keeps reading the old buffer.
- Put any per-frame counter or sample index into a 1-element device array and advance it with a kernel.
- Run one uncaptured step before capture when a solver or controller allocates lazily (ONNX policies, VBD contact history, MPM inner graphs). Allocation inside capture needs the CUDA mempool and does not do what eager code does. For example, a lazily allocated `wp.zeros` becomes a fill that wipes warm-start history on every replay.

### 4. Keep the frame free of host syncs

Each of the following stalls the CPU until the GPU drains, and none of them can be captured:
- `.numpy()`, `.list()`, `print(array)`, `float(tensor)`, `tensor.item()`;
- reading contact counts to size launches;
- `Model.set_gravity(..., world=i)` in a loop. It reads back and re-uploads on every call; pass one per-world array instead.

To stay sync-free:
- Accumulate metrics, errors, and validity on the device. Download once per episode or evaluation.
- Upload trajectories and parameter tables once. Scatter per-world values with a kernel instead of looping in Python.
- Render once per frame, never per substep. `viewer.log_contacts` with contacts shown reads the contact count back every frame.
- Several `log_state` calls for separate models multiply the cost. Use one combined model or fewer calls.
- For timing, use `--viewer null` or `--benchmark`. Use `viewer.set_visible_worlds(...)` when many worlds are visible.
- Check overflow (`contacts.rigid_contact_count.numpy()[0] > contacts.rigid_contact_max`) occasionally or at the end of a run, not every step.

### 5. Size buffers from measured demand

Oversized buffers cost memory and time in sorts, clears, and scans. Undersized buffers silently drop contacts and change the physics.

- `CollisionPipeline(rigid_contact_max=..., shape_pairs_max=...)` are **totals across all worlds**. Size them from the measured peak at the target world count, plus about 25% headroom. The automatic estimate is not a worst-case bound, and the NxN/SAP pair default is the worst case, `N*(N-1)/2` per world.
- After the sizes are known to be adequate, set `verify_buffers=False` in hot loops.
- MuJoCo: `nconmax`, `njmax`, and `njmax_nnz` are **per world** and get multiplied by the world count. Size them for the busiest world. VBD's contact buffer sizes are per particle or body. Contact-free studies should disable contacts and remove collision geometry **before** `replicate()` rather than inflating `njmax`.
- The default `rigid_gap` is 0.1 m, which generates speculative contacts that cost buffer space and time. Set `gap=0.0` on shapes that do not need it.

### 6. Make collision cheaper before making the solver cheaper

- **Cadence:** collide once per frame or every N substeps when the motion allows it. Validate this against per-substep collision. MuJoCo's internal contacts and VBD's own collision slots have separate controls. With VBD, call `solver.set_rigid_history_update(False)` before substeps that reuse the previous contacts (it resets to True after each step), and never leave it False right after a fresh `collide()` into the same buffer.
- **Geometry:**
  - Use primitives or convex hulls instead of visual meshes: `builder.approximate_meshes(...)`.
  - Call `mesh.build_sdf(...)` on every mesh that collides with another mesh, and cache it with `cache_dir`.
  - Approximate **before** `replicate()`.
- **Filtering:**
  - Choose the broad phase per scene: explicit pairs for few pairs, SAP for many spatially coherent shapes, NxN for small scenes.
  - Use world indices and collision groups.
  - Keep global (`world=-1`) shapes to a minimum, because they are tested against every world.
- **Expensive contact models** (hydroelastic, dense SDF): enable them only on the shapes that need them, and tune their buffer fractions. Deterministic collision mode adds a sort pass and disables hydroelastic pre-pruning, so it produces a different contact set.

### 7. Disable gradients unless you differentiate

- `builder.finalize(requires_grad=False)` is the default; keep it. With gradients on, every state/control array gets a grad buffer, the collision pipeline allocates differentiable contact arrays, and `eval_fk` falls back from its fast tile kernel to the generic one.
- Newton's own forward-only kernels already disable backward codegen. For your own forward-only kernels, use `@wp.kernel(enable_backward=False)` or per-module options. Avoid the global `wp.config.enable_backward = False`: Newton's `IKSolver` defaults to `jacobian_mode=IKJacobianType.AUTODIFF`, which uses a tape internally. With the global off it raises no error; the joints just never move. If you need the global switch, use `IKJacobianType.ANALYTIC`.
- Only some solvers are differentiable (currently Featherstone and SemiImplicit). Check the solver table in the docs before planning gradients through XPBD, VBD, or MuJoCo.

### 8. Tune the solver last, against a converged reference

- Cost scales roughly linearly with substeps × iterations × worlds. Reduce collision cost and other overhead first.
- Compare candidate settings against a high-accuracy reference using a physical metric: force balance, penetration, energy, or trajectory error. Do not rely on "the controller reached its target".
- Equal `substeps × iterations` does not mean equal accuracy. Substeps also change `dt` and contact refresh, and with stiff contact they often beat iterations at equal cost.
- Model changes such as mass, materials, gains, or gravity need `solver.notify_model_changed(newton.ModelFlags.<narrowest flag>)`. Call it outside the graph; recapture is not needed, because the graph reads the updated arrays.
- Per-solver settings are in [references/solvers.md](references/solvers.md).

### 9. Batch worlds to the useful size, not the biggest size

- Build one template, then `ModelBuilder.replicate(template, world_count)`.
- Do the expensive per-template work, such as mesh approximation and SDFs, once on the template. VBD coloring works either on the template (`replicate` merges color groups, which is cheaper) or on the final builder.
- Throughput (world-steps/s) rises with world count until the GPU saturates; latency per step rises too. Sweep world counts.
- For optimization workloads, more worlds do not mean more useful progress, and changing the population size changes the experiment.

## Pitfall checklist (review mode)

- [ ] Python loop of substeps launched every frame without a graph.
- [ ] Odd `sim_substeps` with a plain swap inside a captured `simulate()`.
- [ ] Control, target, or state arrays reassigned after capture, instead of written in place.
- [ ] A Python counter, `dt`, index, or interval branch that is expected to change across replays.
- [ ] `.numpy()`, `print`, `float(...)`, or a contact-count read inside the step or substep loop.
- [ ] Rendering or logging per substep; multiple `log_state` calls; contacts drawn while benchmarking.
- [ ] `requires_grad=True`, or backward codegen enabled, in a forward-only program.
- [ ] Default or huge `rigid_contact_max`, `shape_pairs_max`, or `njmax`/`nconmax` multiplied by thousands of worlds. Overflow never checked.
- [ ] Visual meshes used as colliders, or mesh-mesh pairs without an SDF. Mesh approximation done after `replicate()`.
- [ ] Collision every substep when once per frame would preserve the required behavior, or the reverse, untested.
- [ ] `notify_model_changed(ALL)` every frame, or parameters changed without any notify.
- [ ] `use_mujoco_cpu=True` expected to be captured or accelerated. It runs on the host.
- [ ] Timing that includes JIT, capture, or the first replay, or that is unsynchronized.
- [ ] Speedup claimed after cutting iterations, substeps, or contacts without an accuracy check.

## References: load only what the task needs

- [references/step-loop-and-capture.md](references/step-loop-and-capture.md): the canonical loop, odd/even handling, frozen state, warm-up, resets, controls, actuators, and eager/graph parity tests.
- [references/collisions-and-contacts.md](references/collisions-and-contacts.md): pipeline construction, buffer sizing and overflow, broad phase, filtering, SDF/mesh/hydroelastic costs, cadence, and contact readback.
- [references/solvers.md](references/solvers.md): per-solver knobs (MuJoCo, XPBD, VBD, Featherstone, SemiImplicit, MPM, Kamino), `notify_model_changed` cost, and determinism.
- [references/worlds-and-benchmarking.md](references/worlds-and-benchmarking.md): replication, per-world parameters and resets, memory scaling, viewers, examples' `--benchmark`, ASV, metrics, and reporting.
