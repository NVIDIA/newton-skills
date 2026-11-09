# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import argparse

import newton
import numpy as np
import warp as wp


def command_force(command):
    """Compute the force for a scheduled controller command."""
    return command / np.linalg.norm(command)


def simulate(scene, device):
    """Simulate the selected scene and return sampled state."""
    builder = newton.ModelBuilder(gravity=wp.vec3(0.0))
    for index in range(1 if scene == "reduced" else 3):
        body = builder.add_body(
            xform=wp.transform(wp.vec3(0.0, index, 0.0), wp.quat_identity()), mass=1.0
        )
        builder.add_shape_sphere(body, radius=0.1, cfg=builder.ShapeConfig(density=0.0))
    model = builder.finalize(device=device)
    solver = newton.solvers.SolverXPBD(model)
    state_0, state_1 = model.state(), model.state()
    control = model.control()
    forces = np.zeros((model.body_count, 6), dtype=np.float32)
    poses, velocities, commands = (
        [state_0.body_q.numpy().copy()],
        [state_0.body_qd.numpy().copy()],
        [],
    )
    for step in range(3600):
        command = np.array([1.0, 0.0, 0.0]) if step < 2400 else np.zeros(3)
        state_0.clear_forces()
        forces[:, :3] = command_force(command)
        state_0.body_f.assign(forces)
        solver.step(state_0, state_1, control, None, 0.001)
        state_0, state_1 = state_1, state_0
        poses.append(state_0.body_q.numpy().copy())
        velocities.append(state_0.body_qd.numpy().copy())
        commands.append(command)
    return np.array(poses), np.array(velocities), np.array(commands)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--scene", choices=("reduced", "original"), required=True)
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    poses, velocities, commands = simulate(args.scene, args.device)
    np.savez(args.output, poses=poses, velocities=velocities, commands=commands)
