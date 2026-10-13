# Solver Settings and Cost

## Contents
- Tuning order
- Accuracy-equivalent comparisons
- SolverMuJoCo
- SolverXPBD
- SolverVBD
- SolverFeatherstone
- SolverSemiImplicit
- SolverImplicitMPM, SolverStyle3D, SolverKamino
- Model changes: `notify_model_changed`
- Determinism
- Differentiability

Docs: [Simulation tuning](https://newton-physics.github.io/newton/stable/concepts/simulation_tuning.html), [Solver tuning](https://newton-physics.github.io/newton/stable/concepts/simulation_tuning_solvers.html), [MuJoCo tuning](https://newton-physics.github.io/newton/stable/concepts/simulation_tuning_mujoco.html), [Solver feature matrix](https://newton-physics.github.io/newton/stable/solvers/index.html).

Defaults below are from Newton 1.6.1. Confirm them in the installed solver's docstring.

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

## SolverMuJoCo

MuJoCo Warp (GPU) backend. Settings from the constructor apply to all worlds. Per-world values can come from `model.mujoco.<option>` custom attributes.

| Option | Default | Performance notes |
|---|---|---|
| `nconmax`, `njmax`, `njmax_nnz` | estimated | **Per world.** Memory and some work scale with them × `world_count`. Size them for the busiest world, from measurement. The estimate comes from the initial pose and can be too small later in a run or wastefully large. |
| `iterations` / `ls_iterations` | 100 / 50 (MuJoCo defaults) | Upper bounds. The solver exits early when all worlds converge (via `wp.capture_while`), so a high cap costs only on hard steps. Lowering them helps when worlds rarely converge. Uncaptured, that loop reads the condition on the host every iteration, which is one more reason to capture. |
| `solver` | `"newton"` | `"cg"` is cheaper per iteration but needs more iterations. Measure both. |
| `cone` | `"pyramidal"` | `"elliptic"` resists slip better but costs more. |
| `integrator` | `"implicitfast"` | `"euler"` is cheapest but less stable with damping. RK4 is the most expensive. |
| `jacobian` | auto | Sparse Jacobians save memory and time for large DoF counts (roughly 60+). |
| `use_mujoco_contacts` | `True` | `False` uses Newton's `CollisionPipeline`, which is needed for SDF and hydroelastic contacts. Pass `contacts` to `step` accordingly. |
| `disable_contacts` | `False` | Use it for contact-free studies such as system identification of a fixed-base arm. Also strip collision geometry before `replicate()`. |
| `update_data_interval` | 1 | A Python-counter decision, so it is frozen inside a captured graph. See the step-loop reference. |
| `enable_sleeping`, `nvmax` | off | Helps scenes with many resting bodies, and is slower when most DoFs stay awake. Requires the GPU backend, the `"newton"` solver, MuJoCo contacts, and a non-RK4 integrator. `notify_model_changed` wakes all worlds. |
| `use_mujoco_cpu` | `False` | Runs MuJoCo C on the host. It is not captured or accelerated, and contact conversion APIs are unavailable. Use it only for single-world debugging or latency comparisons. |

Other notes:
- **Throughput, not latency:** MuJoCo Warp pays off with many worlds. For one world and lowest latency, CPU MuJoCo can be faster.
- **Overflow:** constraint and contact overflow are reported through the MuJoCo Warp data overflow flags and warnings. Check them at episode or rollout boundaries, not per step.
- **Contact conversion:** `solver.update_contacts(contacts, state)` converts MuJoCo contacts to Newton `Contacts`. It costs an extra kernel, so call it only when sensors or analysis need it. Size the target with `solver.get_max_contact_count()`.
- **Stiffness limit:** with MuJoCo's default `refsafe` behavior, the `solref` time constant is clamped to at least 2·`dt`. Raising gains beyond that does nothing, so don't add substeps "for stiffness" without checking this.

## SolverXPBD

- **Settings:** `iterations=2` by default, plus relaxation and compliance settings. Cost is linear in iterations.
- **Unsupported joint features:** XPBD ignores armature, joint friction, effort limits, and velocity limits. Don't tune those expecting an effect.
- **Restitution:** `enable_restitution=True` adds restitution passes (`rigid_contact_restitution_iterations`). Leave it off unless restitution matters.

## SolverVBD

- **Iterations:** `iterations=10` by default.
- **Coloring:** VBD requires graph coloring: call `builder.color()` before `finalize()`. Fewer colors mean fewer sequential passes per iteration. Coloring the template before `replicate` works (replicate merges color groups) and is cheaper than coloring the final builder; Newton's examples color the final builder, which also works. Prefer the coloring algorithm that produces fewer colors.
- **Contact buffers:**
  - Particle buffers: `particle_vertex_contact_buffer_size=32` and `particle_edge_contact_buffer_size=64`.
  - Rigid buffers: `rigid_body_contact_buffer_size=64` and `rigid_body_particle_contact_buffer_size=256`.
  - Too small drops contacts. Too large costs memory and time, because kernels iterate over capacity.
  - Size them from measured peak per-entity contact degree.
- **Tile solve:** `particle_enable_tile_solve=True` is the default. Keep it unless profiling shows otherwise.
- **Collision schedule:** VBD can own the collision pipeline (`SolverVBD(..., collision_pipeline=...)`). `collision_frequency` / `set_collision_frequency(...)` (defined on `SolverBase`) takes per-`CollisionSlot` schedules: `RIGID` covers rigid-rigid and particle-shape contacts, and `SOFT_SELF_CONTACT` covers particle self-contact. Detecting less often is cheaper but can miss fast contacts. Recapture after changing the schedule.
- **Reusing contacts across substeps:** if you run `collide()` yourself less often than every substep, call `solver.set_rigid_history_update(False)` before the substeps that reuse the previous contacts. Otherwise VBD rebuilds per-body contact lists and re-initializes contact penalties every step. The flag applies to the next `step()` only, then resets to True. Never pass freshly collided contacts while it is False.
- **Construction order for capture:** `CollisionPipeline` → `contacts()` → `SolverVBD`, or run one uncaptured step before capture. VBD allocates contact history that must exist before capture.
- **Solver history:** VBD keeps history (previous positions, collision-detection positions, warm starts). Reset it together with the state, and keep the canonical-buffer discipline for odd substep counts.
- **Stiff soft bodies:** high stiffness ratios converge slowly per iteration. Check force balance against a converged reference before trusting low iteration counts. More substeps usually help more than more iterations here.
- **Explicit external springs:** springs or dampers applied as external forces bypass the implicit solve and can limit stable `dt` regardless of iterations.

## SolverFeatherstone

- **`update_mass_matrix_interval=1`:** raising it skips mass-matrix updates. Inside a graph, use `sim_substeps` or a divisor of it.
- **`use_tile_gemm=False`, `fuse_cholesky=True`:** the tile path can be faster for some articulation sizes. Measure it per robot.
- **Differentiability:** one of the two differentiable solvers. Keep `requires_grad=False` when not differentiating.

## SolverSemiImplicit

- **Explicit integration:** no iterations; stability depends entirely on `dt`. Stiff contacts or springs force many small substeps, so compare cost against an implicit solver at equal accuracy.
- **`enable_tri_contact=True`** can be disabled when triangle contact is not needed.

## SolverImplicitMPM, SolverStyle3D, SolverKamino

- **SolverImplicitMPM:**
  - Capture the whole step only with `grid_type="fixed"`, or a sparse grid configured to be rebuildable under capture. The default is `"sparse"`.
  - Run an uncaptured warm-up step first.
  - Examples require an even substep count for capture.
  - Iteration caps and the strain/basis choice dominate cost. Verify volume conservation and convergence when lowering them.
- **SolverStyle3D:** cost scales with `iterations` and inner linear-solver iterations. Examples require even substeps for capture.
- **SolverKamino:**
  - `dynamics_solver="padmm"` (the default) uses proximal ADMM; `"dvi"` (opt-in) uses projected iterations with a direct bilateral solve. Their relative cost depends on the mechanism and contact count, so benchmark both at equal accuracy. Kamino is in beta.
  - `collect_solver_info=True` adds time and memory. Use it for diagnosis only.

## Model changes: `notify_model_changed`

After writing model arrays (masses, inertias, materials, gains, limits, gravity, tendons), call:

```python
solver.notify_model_changed(newton.ModelFlags.SHAPE_PROPERTIES)   # narrowest applicable flags
```

- **Pass only the flags you need.** Flags: `JOINT_PROPERTIES`, `JOINT_DOF_PROPERTIES`, `BODY_PROPERTIES`, `BODY_INERTIAL_PROPERTIES`, `SHAPE_PROPERTIES`, `MODEL_PROPERTIES`, `CONSTRAINT_PROPERTIES`, `TENDON_PROPERTIES`, `ACTUATOR_PROPERTIES`, and `ALL`. In MuJoCo, inertial changes trigger constant recomputation (`set_const`), which is expensive. Avoid `ALL` in loops.
- **Call it outside the graph, then keep replaying.** The graph reads the updated arrays. Recapture only if buffers were reallocated or Python-level schedules changed.
- **Batch your changes.** Randomize all worlds' parameters in one kernel launch, then notify once. Don't loop per world.
- **Sleeping wakes up.** With MuJoCo sleeping enabled, any notify wakes every world.
- **Some changes are not notifications.** Structural changes (topology, element stiffness layout in VBD) require rebuilding the solver.

## Determinism

`deterministic=` options give reproducible results, at extra cost. `CollisionPipeline(deterministic=True)` takes a bool; the solvers take `deterministic=wp.DeterministicMode.RUN_TO_RUN` (or `GPU_TO_GPU`), and `wp.config.deterministic` is also a `wp.DeterministicMode`, not a bool. The cost comes from:
- sorting or ordering passes;
- deterministic atomics, which cost extra time and memory.

Enable them only when reproducibility is a requirement. Benchmark deterministic and non-deterministic configurations separately. Repeatability on one GPU does not prove equality across GPU architectures.

## Differentiability

- **Supported solvers:** only `SolverFeatherstone` and `SolverSemiImplicit` have (basic) differentiability. XPBD, VBD, MuJoCo, MPM, Style3D, and Kamino do not. Check the feature matrix before planning gradient-based optimization.
- **Where cost goes:**
  - one `State` per substep (memory grows with rollout length);
  - backward kernels;
  - `requires_grad` buffers everywhere.
- **Capture:** capture the forward pass plus `tape.backward()` in one graph, and call `tape.zero()` each iteration.
- **Contact gradients:** narrow-phase collision is not differentiated. Gradients through contacts use approximations, so validate gradients with finite differences on the actual rollout.
- **Non-differentiable solvers:** for expensive solvers with no gradients, compare population or finite-difference methods against a surrogate at equal solution quality, not equal iteration count.
