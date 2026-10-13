# Solver Settings and Cost

## Contents
- Tuning order
- Accuracy-equivalent comparisons
- Per-solver performance notes
- Model changes: `notify_model_changed`
- Determinism
- Differentiability

Option lists, defaults, and the feature matrix are in the docs for your installed release: [Simulation tuning](https://newton-physics.github.io/newton/stable/concepts/simulation_tuning.html), [Solvers and feature matrix](https://newton-physics.github.io/newton/stable/solvers/index.html), [MuJoCo solver](https://newton-physics.github.io/newton/stable/solvers/mujoco.html), [Kamino solver](https://newton-physics.github.io/newton/stable/solvers/kamino.html), and the [solver API reference](https://newton-physics.github.io/newton/stable/api/newton_solvers.html). This file covers only how the settings affect cost and what to watch for.

## Tuning order

1. **Get the physics right first.** Units, masses and inertias, collision geometry, and stiffness that fits `dt`. A badly conditioned model needs more substeps and iterations than any tuning can save.
2. **Remove overhead.** Use graph capture, take syncs and rendering off the hot path, and size buffers correctly.
3. **Make collision cheaper.** Use simpler geometry, filtering, and cadence (see [collisions-and-contacts.md](collisions-and-contacts.md)).
4. **Tune the solver last.** Lower substeps and iterations only until accuracy metrics start to degrade.

Cost is roughly linear in `substeps × iterations × worlds`. No setting removes that scaling.

## Accuracy-equivalent comparisons

- **Pick a reference.** Run a high-accuracy configuration (many substeps and iterations) and compare candidates against it.
- **Use physical metrics**, not "it looks fine":
  - force or torque balance residual;
  - penetration depth;
  - energy drift;
  - constraint violation;
  - trajectory error over the evaluation window;
  - inverted or degenerate elements for soft bodies.
- **Validate controlled scenes with an independent measurement.** A controller reaching its target does not prove the contact forces are right. In one measured case, a servo hit its target while the support force was off by tens of newtons.
- **Substeps and iterations are not interchangeable.** Equal `substeps × iterations` does not give equal accuracy. Substeps also shrink `dt`, refresh contacts, and change controller dynamics. With stiff contact, more substeps often beat more iterations at the same cost, but not always, so sweep both.
- **Sweep iterations by doubling** (e.g. 5, 10, 20, 40). Stop when the metric improves by only a few percent.
- **Hold everything else fixed:** material, mesh, load, controller, duration, and contact settings. Changing stiffness or scale "for speed" changes the experiment.
- **Guard against invalid fast settings.** If an automatic timestep or stability guard raises substeps drastically, investigate the model; don't accept a 10–20× cost silently.

## Per-solver performance notes

### SolverMuJoCo

- **Capacities are per world.** `nconmax`, `njmax`, and `njmax_nnz` are multiplied by `world_count` in memory and in some work. Size them for the busiest world from measurement. The automatic estimate comes from the initial pose and can be too small later in a run, or wastefully large.
- **Iteration caps are upper bounds.** The solver exits early once all worlds converge, using `wp.capture_while`, so a high cap mostly costs on hard steps. Uncaptured, that loop reads its condition on the host every iteration, which is one more reason to capture.
- **Measure the alternatives** for solver type (`newton` vs. `cg`), friction cone, integrator, and dense vs. sparse Jacobian. Their costs trade off against stability and accuracy, and the best choice depends on DoF count and contact load. Check the MuJoCo solver docs for the options in your release.
- **`update_data_interval`** is a Python counter, so a captured graph freezes its pattern. See [step-loop-and-capture.md](step-loop-and-capture.md).
- **Newton vs. MuJoCo contacts:** `use_mujoco_contacts=False` uses Newton's `CollisionPipeline` (needed for SDF and hydroelastic contact); pass `contacts` to `step` accordingly. For contact-free studies, use `disable_contacts=True` and strip collision geometry before `replicate()` instead of raising `njmax`.
- **Sleeping** (`enable_sleeping`) helps scenes with many resting bodies and is slower when most DoFs stay awake. It has backend and solver restrictions (see the docs), and `notify_model_changed` wakes all worlds.
- **`use_mujoco_cpu=True`** runs MuJoCo C on the host. It is never captured or GPU-accelerated. Use it for single-world debugging or latency comparisons.
- **Throughput, not latency:** MuJoCo Warp pays off with many worlds. For one world and the lowest latency, CPU MuJoCo can be faster.
- **Overflow** is reported through MuJoCo Warp's overflow flags and warnings. Check them at episode or rollout boundaries, not every step.
- **Contact conversion** (`solver.update_contacts(contacts, state)`) is an extra kernel. Call it only when sensors or analysis need Newton `Contacts`, and size the target with `solver.get_max_contact_count()`.
- **Stiffness limit:** with MuJoCo's default `refsafe` behavior, the `solref` time constant is clamped to at least 2·`dt`. Raising gains beyond that does nothing, so check this before adding substeps "for stiffness".

### SolverXPBD

- Cost is linear in `iterations`.
- XPBD ignores some joint features (see the feature matrix), such as armature and joint friction. Don't tune them expecting an effect.
- Restitution adds extra passes. Leave it off unless restitution matters.

### SolverVBD

- **Coloring is required** (`builder.color()` before `finalize()`). Fewer colors mean fewer sequential passes per iteration, so prefer the coloring option that produces fewer colors. Coloring the template before `replicate()` works (replicate merges color groups) and is cheaper than coloring the final builder; both are valid.
- **Contact buffers are per particle or per body** and are fixed-size. Too small drops contacts; too large costs memory and time, because kernels iterate over capacity. Size them from the measured peak contact degree (the buffer-size arguments are in the solver docs).
- **Collision schedule:** VBD can own the collision pipeline (`SolverVBD(..., collision_pipeline=...)`). `set_collision_frequency(...)`, defined on `SolverBase`, takes per-`CollisionSlot` schedules: `RIGID` covers rigid-rigid and particle-shape contacts, and `SOFT_SELF_CONTACT` covers particle self-contact. Detecting less often is cheaper but can miss fast contacts. Recapture after changing the schedule.
- **Reusing contacts across substeps:** if you run `collide()` yourself less often than every substep, call `solver.set_rigid_history_update(False)` before the substeps that reuse the previous contacts. Otherwise VBD rebuilds per-body contact lists and re-initializes contact penalties every step. The flag applies to the next `step()` only, then resets to True. Never pass freshly collided contacts while it is False.
- **Construction order for capture:** `CollisionPipeline` → `contacts()` → `SolverVBD`, or run one uncaptured step before capture. VBD allocates contact history that must exist before capture.
- **Solver history** (previous positions, collision-detection positions, warm starts) must be reset together with the state, and kept consistent with the canonical buffer for odd substep counts.
- **Stiff soft bodies** converge slowly per iteration. Check force balance against a converged reference before trusting low iteration counts. More substeps usually help more than more iterations here.
- **Explicit external springs or dampers** applied as forces bypass the implicit solve and can limit the stable `dt` regardless of iterations.

### SolverFeatherstone

- **`update_mass_matrix_interval`** skips mass-matrix updates; inside a graph, use `sim_substeps` or a divisor of it.
- **Tile GEMM / fused Cholesky options** can be faster for some articulation sizes. Measure them per robot.
- Differentiable; keep `requires_grad=False` when not differentiating.

### SolverSemiImplicit

- Explicit integration: no iterations, and stability depends entirely on `dt`. Stiff contacts or springs force many small substeps, so compare its cost with an implicit solver at equal accuracy.
- Disable triangle contact when it is not needed.

### SolverImplicitMPM, SolverStyle3D, SolverKamino

- **SolverImplicitMPM:** capture the whole step only with a fixed grid, or a sparse grid configured to be rebuildable under capture (check the grid options in the docs). Run an uncaptured warm-up step first. Its examples require an even substep count for capture. Iteration caps and the strain/basis choice dominate cost; verify volume conservation and convergence when lowering them.
- **SolverStyle3D:** cost scales with `iterations` and the inner linear-solver iterations. Its examples require even substeps for capture.
- **SolverKamino** (beta): the default `"padmm"` backend and the opt-in `"dvi"` backend have different cost profiles depending on the mechanism and contact count; benchmark both at equal accuracy. Solver-info collection adds time and memory, so use it for diagnosis only.

## Model changes: `notify_model_changed`

After writing model arrays (masses, inertias, materials, gains, limits, gravity, tendons), call:

```python
solver.notify_model_changed(newton.ModelFlags.SHAPE_PROPERTIES)   # narrowest applicable flags
```

- **Pass only the flags you need** (see `newton.ModelFlags` in the API reference). Broad flags trigger expensive recomputation; in MuJoCo, inertial changes trigger constant recomputation (`set_const`). Avoid `ModelFlags.ALL` in loops.
- **Call it outside the graph, then keep replaying.** The graph reads the updated arrays. Recapture only if buffers were reallocated or Python-level schedules changed.
- **Batch your changes.** Randomize all worlds' parameters in one kernel launch, then notify once. Don't loop per world.
- **Sleeping wakes up.** With MuJoCo sleeping enabled, any notify wakes every world.
- **Some changes are not notifications.** Structural changes (topology, element stiffness layout in VBD) require rebuilding the solver.

## Determinism

Deterministic options give reproducible results at extra cost. `CollisionPipeline(deterministic=True)` takes a bool; the solvers take `deterministic=wp.DeterministicMode.RUN_TO_RUN` (or `GPU_TO_GPU`), and `wp.config.deterministic` is also a `wp.DeterministicMode`, not a bool. The cost comes from:
- sorting or ordering passes;
- deterministic atomics, which cost extra time and memory.

Enable them only when reproducibility is a requirement. Benchmark deterministic and non-deterministic configurations separately. Repeatability on one GPU does not prove equality across GPU architectures.

## Differentiability

- **Supported solvers:** check the feature matrix. In Newton 1.6.1 only `SolverFeatherstone` and `SolverSemiImplicit` have (basic) differentiability.
- **Where cost goes:**
  - one `State` per substep (memory grows with rollout length);
  - backward kernels;
  - `requires_grad` buffers everywhere.
- **Capture:** capture the forward pass plus `tape.backward()` in one graph, and call `tape.zero()` each iteration.
- **Contact gradients:** narrow-phase collision is not differentiated. Gradients through contacts use approximations, so validate gradients with finite differences on the actual rollout.
- **Non-differentiable solvers:** for expensive solvers with no gradients, compare population or finite-difference methods against a surrogate at equal solution quality, not equal iteration count.
