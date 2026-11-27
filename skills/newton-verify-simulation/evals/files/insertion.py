# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""Write the insertion-axis rollout to a CSV file using Newton on CPU."""

import csv
import sys

import newton
import warp as wp


def rollout(initial_speed, force):
    builder = newton.ModelBuilder(gravity=(0.0, 0.0, 0.0))
    slider = builder.add_link()
    builder.add_shape_box(slider, hx=0.05, hy=0.05, hz=0.05, cfg=builder.ShapeConfig(density=1000.0))
    joint = builder.add_joint_prismatic(parent=-1, child=slider, axis=newton.Axis.X)
    builder.add_articulation([joint])
    builder.joint_qd[0] = initial_speed
    model = builder.finalize(device="cpu")
    solver = newton.solvers.SolverFeatherstone(model)
    state, next_state = model.state(), model.state()
    newton.eval_fk(model, model.joint_q, model.joint_qd, state)
    control = model.control()
    control.joint_f.fill_(force)
    yield 0.0
    for _ in range(4):
        state.clear_forces()
        solver.step(state, next_state, control, None, 0.01)
        state, next_state = next_state, state
        yield float(state.joint_q.numpy()[0]) * 1000  # m to mm


if __name__ == "__main__":
    wp.init()
    with open(sys.argv[1], "w", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(("episode", "step", "travel_mm", "task_success"))
        for episode, speed, force in (("A", 0.2, 0.0), ("B", 0.7, -20.0)):
            samples = list(rollout(speed, force))
            for step, travel in enumerate(samples):
                final = step == len(samples) - 1
                success = int(7.9 <= travel <= 8.1) if final else ""
                writer.writerow((episode, step, f"{travel:.4f}", success))
