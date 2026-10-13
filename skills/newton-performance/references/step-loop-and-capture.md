# Step Loop and CUDA Graph Capture in Newton

## Contents
- Canonical structure
- What a graph freezes
- Odd substep counts
- Warm-up and lazy allocation
- Controls, resets, and parameters during replay
- Python-side counters in solvers
- Stateful actuators and controllers
- Eager/graph parity tests
- When capture does not help

## Canonical structure

Newton examples use a single shape for the step loop:

```python
class Sim:
    def __init__(self, model, device):
        self.fps, self.sim_substeps = 60, 8
        self.frame_dt = 1.0 / self.fps
        self.sim_dt = self.frame_dt / self.sim_substeps

        self.state_0 = model.state()
        self.state_1 = model.state()
        self.control = model.control()
        self.pipeline = newton.CollisionPipeline(model, rigid_contact_max=...)
        self.contacts = self.pipeline.contacts()
        self.solver = ...                     # construct after the pipeline (VBD needs this)

        self.graph = None
        if device.is_cuda:                    # mempool needed if capture allocates
            self.simulate()                   # warm-up, then restore state if required
            with wp.ScopedCapture(device=device) as cap:
                self.simulate()
            self.graph = cap.graph

    def simulate(self):
        self.pipeline.collide(self.state_0, self.contacts)      # once per frame, or per substep
        for i in range(self.sim_substeps):
            self.state_0.clear_forces()
            self.solver.step(self.state_0, self.state_1, self.control, self.contacts, self.sim_dt)
            if self.sim_substeps % 2 == 1 and i == self.sim_substeps - 1:
                self.state_0.assign(self.state_1)
            else:
                self.state_0, self.state_1 = self.state_1, self.state_0

    def step(self):
        if self.graph:
            wp.capture_launch(self.graph)
        else:
            self.simulate()
```

Rules that follow from this structure:

- **Allocate everything before capture.** This includes states, control, contacts, the pipeline, the solver, sensors, and metric buffers.
- **Keep every object the graph references alive** for as long as the graph replays. Graphs hold raw pointers. Replacing `self.contacts` or `self.state_1` leaves the graph pointing at freed memory.
- **Use `wp.ScopedCapture` on CUDA** (guard with `device.is_cuda`). Warp's CPU capture is experimental and not validated for Newton solver steps, so run eagerly on CPU. If the captured region allocates, capture only when the device mempool is enabled (`device.is_mempool_enabled`); otherwise run eagerly.
- **Rebuild the graph when topology, buffer sizes, or bound arrays change.** For example, rebuild after re-finalizing the model, resizing contacts, or reassigning a state attribute.

## What a graph freezes

A graph freezes, at capture time:

- Buffer addresses.
- Launch dimensions, including ones derived from Python ints such as `len(...)` or a host-read count.
- Scalar kernel arguments such as `dt`, `world_id`, `iteration`, and flags.
- All Python control flow: swaps, `if step % k == 0`, `if self._dirty`, and attribute toggles.

Only the contents of captured buffers change between replays. Treat anything else that must change per replay as device data. Examples are a counter, a selected sample, or a phase flag: put each in a 1-element `wp.array` and update it with a kernel inside the graph.

## Odd substep counts

The swap `state_0, state_1 = state_1, state_0` rebinds Python names. It runs once, during capture.

| substeps | Buffers during capture | Replay result |
|---|---|---|
| even (e.g. 4) | A→B→A→B→A; ends in A | Next replay reads A: **correct**. |
| odd (e.g. 5) | A→B→A→B→A→B; ends in B | Python `state_0` now names B, but the graph always reads A, which holds substep 4. Each frame advances only 4 substeps of physics: **slow motion, no error**. |

Example: a free-falling box in Newton 1.6.1 with 5 substeps, after 20 frames:

| Execution | `SolverSemiImplicit` / `SolverFeatherstone` | `SolverXPBD` |
|---|---|---|
| Eager | z = 0.450 | z = 0.450 |
| Graph, plain swap | **z = 0.638** (slow motion) | z = 0.450 |
| Graph, copy fix | z = 0.450 | z = 0.450 |

Some solvers happen to hide the bug in some scenes, as XPBD does here. That depends on what the solver writes back into its input state. Don't rely on it: apply the fix whenever substeps can be odd.

Fixes, in order of preference:

1. **Copy on the last odd substep** (`state_0.assign(state_1)`). This costs one state copy per frame. It keeps a single readable `state_0` for rendering, sensors, and resets, and eager and captured execution behave identically. This is the documented pattern on `State.assign`.
2. **Use an even substep count.** Adjust it at configuration time and recompute `sim_dt`.
3. **Alternate two graphs** (captured from A→B and from B→A) and pick the graph by which buffer is current. This avoids the copy, but every consumer must know which buffer is readable. Use it only when the copy is measurably material.

Also check other double buffers that follow the same parity: actuator state, controller history, and custom per-substep ping-pong arrays. Some solvers keep internal history (previous positions, collision-detection positions, warm starts). Reset that history when resetting the state, and verify it stays consistent with the canonical buffer.

## Warm-up and lazy allocation

Run one uncaptured `simulate()` before capturing, because:

- **Warp compiles and loads modules on first launch.** Recent drivers can load modules during capture, but warming up keeps JIT time out of the graph and avoids recompiling inside the capture window.
- **Some solvers and controllers allocate on their first step.** Examples are ONNX/torch policy buffers, VBD contact history, and MPM inner graphs. If that first step happens inside capture, the allocation becomes a graph node. For example, a `wp.zeros` can become a memset that wipes warm-start data on every replay.
- **Warm-up mutates state.** Save and restore the states (and solver history) after warm-up when the run must start from the initial condition. The alternative is to run warm-up on cloned states.

The first `wp.capture_launch` instantiates the executable graph, which takes noticeable time. Do one replay before you start timing.

## Controls, resets, and parameters during replay

**Do:**

- Write controls in place, inside the graph (a policy or controller kernel that writes `control.joint_target_*`) or before each replay (`wp.copy(control.joint_target_q, src)`, `control.joint_f.assign(src)`).
- Use `ArticulationView.set_attribute(name, target, values)` with a Warp array of matching dtype. Non-Warp input triggers a host-to-device allocation on every call.
- Reset with kernels that copy from stored initial arrays, outside the graph or in a separate reset graph. Use `solver.reset(state, world_mask=...)` for per-world resets where the solver supports it, and `newton.eval_fk(model, joint_q, joint_qd, state, mask=...)` to rebuild body poses.
- After changing model arrays (masses, materials, gains, gravity), call `solver.notify_model_changed(flags)` outside the graph and keep replaying. The graph reads the updated contents.

**Don't:**

- Reassign `control.x = wp.array(...)` or `state.y = ...` after capture.
- Pass a Python scalar that you expect to vary across frames into `simulate()`.
- Read a contact count or any other device value on the host inside `simulate()`. It is a sync point, and it fails during capture.

## Python-side counters in solvers

Several solvers decide work with Python counters. Inside a graph, the decisions made during capture repeat forever:

| Setting | Python decision | Safe use with capture |
|---|---|---|
| `SolverMuJoCo(update_data_interval=k)` | `self._step % k == 0` | Use `k=1` or `k=0`, or make substeps per graph a multiple of `k`. |
| `SolverFeatherstone(update_mass_matrix_interval=k)` | `dirty or _step % k == 0` | Use `k = sim_substeps` (as the examples do) or a divisor of it. |
| `solver.set_collision_frequency(...)` | schedule chosen in Python | Recapture after changing it. |
| VBD history update toggles | Python flag | Set them before capture; recapture after changing them. |
| `pipeline.collide(..., dt=...)` (speculative contacts) | captured scalar | Keep `dt` fixed, or recapture. |

To audit a solver you have not used before, read its `step()` and look for `self._step`, `%`, `if self.`, `.numpy()`, and allocations.

## Stateful actuators and controllers

- **Double-buffered actuator state** (PID integrators, delay lines, LSTMs) has the same parity problem as `State`. Copy at the boundary with the actuator state's `assign`, or alternate graphs keyed on the current buffer.
- **Controllers that bind live state arrays at construction** (impedance and other feedback controllers) read whatever buffer they bound. Make sure that buffer is the canonical `state_0` after each replay. The odd/even copy pattern guarantees this.

## Eager/graph parity tests

Write a test that runs the same scenario eagerly and with graph replay, then compares the full state:

- odd **and** even substep counts;
- several consecutive replays, not just one;
- controls that change between frames;
- a reset in the middle;
- eager and captured calls interleaved;
- every array the solver reads, not only `body_q`/`particle_q`. Include velocities, solver history, and custom attributes.

Expect agreement to float32 tolerance, not bit equality. Graph replay can reorder independent work. Bit-identical repeatability is a separate requirement that needs deterministic modes.

## When capture does not help

Graphs remove host launch overhead. They do not speed up the kernels themselves. Expect little from capture when:

- the frame is dominated by a few large kernels, such as big solves, dense contact, or large world counts;
- most of the time is outside Warp: CPU MuJoCo (`use_mujoco_cpu=True`, which is never captured), policy inference on another framework's stream, Python data handling, or rendering.

In those cases, profile kernels with Nsight Systems and Nsight Compute (see the Warp profiling docs and any installed Warp skills) or reduce work.

Auxiliary per-step work left out of the graph can erase the gain from capturing the main step. An example is computing bias forces or dynamics terms eagerly every step for a batched replay. Capture that work as well.
