# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import argparse

import newton
import numpy as np
import warp as wp


def simulate(scene, device):
    """Simulate the selected scene and return sampled state."""
    builder = newton.ModelBuilder()
    builder.add_ground_plane()
    for index in range(1 if scene == "reduced" else 3):
        body = builder.add_body(
            xform=wp.transform(
                wp.vec3(index, 0.0, 1.0 + 0.2 * index), wp.quat_identity()
            )
        )
        builder.add_shape_sphere(body, radius=0.1)
    model = builder.finalize(device=device)
    solver = newton.solvers.SolverXPBD(model, iterations=8)
    state_0, state_1 = model.state(), model.state()
    control = model.control()
    contacts = model.contacts()
    model.collide(state_0, contacts)
    poses, velocities = (
        [state_0.body_q.numpy().copy()],
        [state_0.body_qd.numpy().copy()],
    )
    for _ in range(720):
        state_0.clear_forces()
        solver.step(state_0, state_1, control, contacts, 1.0 / 240.0)
        state_0, state_1 = state_1, state_0
        poses.append(state_0.body_q.numpy().copy())
        velocities.append(state_0.body_qd.numpy().copy())
    return np.array(poses), np.array(velocities)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--scene", choices=("reduced", "original"), required=True)
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    poses, velocities = simulate(args.scene, args.device)
    np.savez(args.output, poses=poses, velocities=velocities)
