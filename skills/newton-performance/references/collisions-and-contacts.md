# Collisions and Contacts in Newton

## Contents
- Pipeline construction
- Buffer sizing and overflow
- Collision cadence
- Broad phase and filtering
- Geometry cost: primitives, meshes, SDFs, hydroelastic
- Gap, speculative contacts, determinism
- Reading contacts without stalling
- Gather vs. scatter and dense contact

Collision detection often costs as much as the solver, or more. Fix it first.

The [Collisions](https://newton-physics.github.io/newton/stable/concepts/collisions.html) docs and the [`CollisionPipeline` API](https://newton-physics.github.io/newton/stable/api/_generated/newton.CollisionPipeline.html) for your release describe every option and default. This file covers cost and pitfalls.

## Pipeline construction

```python
pipeline = newton.CollisionPipeline(
    model,
    broad_phase="explicit",        # or "sap" / "nxn"; see below
    rigid_contact_max=...,         # measured peak + headroom (total across worlds)
    shape_pairs_max=...,           # nxn/sap only: measured peak pair count + headroom
    verify_buffers=True,           # set False in the hot loop once sizes are proven
)
contacts = pipeline.contacts()     # allocate once; collide() clears counters each call
```

- **Use an explicit `CollisionPipeline`.** `Model.collide()` and `Model.contacts()` are deprecated convenience paths. An explicit pipeline lets you set capacities and reuse the object.
- **Construct the pipeline and contacts before the solver and before graph capture.** VBD looks at the pipeline/contacts when allocating contact history.
- **Reuse one `Contacts` object** across steps. `collide()` resets the counts, and the reset is fused into an existing kernel. Do not allocate a new `Contacts` per frame.

## Buffer sizing and overflow

Capacities cost memory and time even when they are empty: sorts, scans, compaction and clears scale with capacity, not with active count. Capacities that are too small silently drop contacts.

- **`rigid_contact_max`** is resolved in this order: the explicit argument, then `model.rigid_contact_max`, then an automatic estimate. The estimate is not a worst-case bound. Newton warns when the estimated buffer is large. Measure the peak contact count in a representative and worst-case scene, then set capacity to that peak plus about 25%.
- **`shape_pairs_max`** (NxN/SAP only): the default is the worst case, `N*(N-1)/2` pairs per world. It is often 10–100× larger than what is ever emitted, and it can mean multi-GB allocations at high world counts. Size it from a measured peak.
- **Mesh and heightfield pairs:** `max_triangle_pairs` and `contact_reduction_hashtable_size_factor` bound the mesh-triangle work buffers.
- **Overflow detection:** with `verify_buffers=True` (the default), collision prints a device warning when a buffer overflows. When counting overflows yourself, remember that the count can exceed the capacity; the excess contacts were dropped. Check it occasionally on the host:

  ```python
  n = int(contacts.rigid_contact_count.numpy()[0])  # sync: debug/occasional only
  assert n <= contacts.rigid_contact_max, "contact overflow: physics is truncated"
  ```

- **Turn verification off for production.** Once sizes are proven on the worst case, `verify_buffers=False` removes an extra kernel per collide. Keep an overflow test in CI.
- **Never accept truncation as a "memory optimization".** An overflowed run is a different simulation. Re-check force and pressure, contact counts and trajectories after any capacity change.

## Collision cadence

Calling `pipeline.collide(...)` every substep is the most robust option and the most expensive. Options:

```python
for i in range(sim_substeps):
    if i % collide_every_n == 0:            # n=sim_substeps -> once per frame
        pipeline.collide(state_0, contacts)
    solver.step(state_0, state_1, control, contacts, sim_dt)
    ...
```

- **Start at every substep while you get the scene right,** then increase the interval. Pick the largest interval that preserves penetration, grasp stability, sliding and the contact forces you need. Validate it against the every-substep run.
- **Fast-moving or thin objects need more frequent collision.** Speculative contacts can help here; see the gap section below.
- **Not every contact follows this cadence.** It does not apply to MuJoCo's internal contacts (`use_mujoco_contacts=True`, which MuJoCo computes inside `step`), nor to VBD particle self-contact, which uses its own detection interval and collision-frequency settings.
- **With VBD, tell the solver when contacts are reused.** Call `solver.set_rigid_history_update(False)` before each substep that reuses the previous `collide()` result; it resets to True after every step. Leave it True on substeps right after a fresh `collide()`. Alternatively, let VBD own the pipeline and schedule the `RIGID` collision slot via `set_collision_frequency` (see [solvers.md](solvers.md)).
- **The cadence is frozen by graph capture.** It is a Python `if` evaluated at capture time, so change it and then recapture.

## Broad phase and filtering

- **`"explicit"`:** pairs fixed at finalize. Cheapest when the candidate pair set is small and static.
- **`"sap"`:** scales as O(N log N); suits many spatially coherent shapes per world.
- **`"nxn"`:** O(N²) with a simple, predictable cost; suits small scenes. The crossover with SAP depends on the scene, so measure both.

To reduce the number of candidate pairs:
- **Separate worlds:** give each parallel environment its own world index. Shapes in different worlds never collide.
- **Minimize global shapes:** `world=-1` shapes are tested against every world. Keep them few and simple, for example one ground plane.
- **Use collision groups.** Group 0 disables collision for a shape. Positive groups restrict which shapes are tested against each other.
- **Disable flags you don't need:** turn off shape collision or particle collision on shapes that should not take part in those contact types.
- **Filter explicitly:** `shape_pairs_filtered` (pipeline argument) and builder-level collision filters remove known-irrelevant pairs, such as adjacent links.

## Geometry cost: primitives, meshes, SDFs, hydroelastic

From cheapest to most expensive: analytic primitives, then convex hulls, then meshes with SDFs, then meshes without SDFs, then hydroelastic.

- **Don't collide with visual meshes.** Use `builder.approximate_meshes(...)` (see its docstring for the available methods) and keep the visual shapes for rendering. Call it on the template builder **before** `replicate()`. Approximating afterwards repeats the work and allocates once per world.
- **Give every mesh that can touch another mesh an SDF:** `mesh.build_sdf(max_resolution=..., cache_dir=...)`. Without one, mesh-mesh falls back to BVH distance queries, which are much slower. Pass `cache_dir` so SDF baking is not repeated each launch.
- **Opt shapes into hydroelastic contact individually.** Both shapes in a pair must opt in. Use it only where pressure distributions are actually needed. Its cost scales with SDF resolution and contact area. Hydroelastic buffers are sized by a configurable fraction (see the collision docs); lower it to save memory and raise it if overflow warnings appear. Keep contact reduction on unless you need the dense field.
- **Don't let contact reduction discard the field you analyze.** Dense contact fields (hydroelastic, full-surface) and the representative contacts handed to the solver are different things. If downstream analysis needs the dense field, validate that field, not just the reduced contact count.

## Gap, speculative contacts, determinism

- **Default gap (`builder.rigid_gap`, 0.1 m in Newton 1.6.1):** shapes with `gap=None` inherit it. A nonzero gap generates force-free speculative contacts ahead of impact. They use buffer space and narrow-phase time. Set `gap=0.0` (or a small value) on shapes that don't need early contacts. This also shrinks MuJoCo's required `nconmax`.
- **Speculative contacts (`speculative_contact_gap_max`, opt-in)** enlarge the gap by velocity to catch fast objects. They require passing `dt` to `collide()`, and that value is frozen in a captured graph.
- **`deterministic=True`** adds a sort-and-gather pass for reproducible contact ordering. It can be captured and its cost is usually small. It disables hydroelastic pre-pruning, so it can change the contact set. Contact matching (`contact_matching="latest"/"sticky"`) implies deterministic mode.
- **Compare like with like.** Bit-repeatability is a separate requirement from accuracy. Don't benchmark deterministic and non-deterministic configurations as if they were the same workload.

## Reading contacts without stalling

- **Contact counts are device scalars.** Reading them (`.numpy()`) synchronizes and cannot be captured. Never read them to size a launch. Launch over capacity with a device-side `if tid >= count[0]: return` guard, or use a grid-stride loop.
- **`viewer.log_contacts(...)` reads the count every frame** when contacts are shown. Disable contact drawing while benchmarking.
- **MuJoCo contacts:** with `use_mujoco_contacts=True`, contacts live inside MuJoCo. Converting them to Newton `Contacts` (`solver.update_contacts(...)`) is an extra kernel. Do it only when a sensor or analysis consumes the contacts, and size the target `Contacts` from `solver.get_max_contact_count()`.
- **Extended contact attributes cost every step.** Contact sensors and requested contact attributes (for example, forces) make the solver compute and store extra data, even on frames when you don't read them. Request them only when needed.

## Gather vs. scatter and dense contact

Collision-to-solver data flow can be written two ways:
- **Scatter:** each contact atomically adds to its bodies or particles.
- **Gather:** each body or particle loops over its contact list.

Neither wins universally:
- **Scatter** suffers when many contacts hit the same destination, because atomics contend.
- **Gather** suffers with large per-entity lists, scattered memory reads, and capacity-sized loops over mostly-empty lists.
- Rewrites between the two have produced both several-fold wins and several-fold regressions, depending on scene.

Before adopting a new contact-processing path, sweep:
- contact density (sparse vs. dense full-surface contact);
- active/capacity ratio;
- world count;
- mixed vs. single material models.

Measure the complete collision-plus-solver step, not the isolated kernel.
