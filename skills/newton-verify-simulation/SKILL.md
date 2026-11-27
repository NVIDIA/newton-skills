---
name: newton-verify-simulation
description: Verify claims about a Newton simulation using trajectory evidence, physical bounds, sensitivity checks, or reference measurements. Use when assessing simulation fidelity, task success, or sim-to-real evidence.
metadata:
  author: Anthony Angeles <aangeles@nvidia.com>
  tags:
    - newton
    - physics-simulation
    - verification
---

# Verify a Newton simulation

1. Define the claim and intended use. Identify the observable, units, time horizon,
   and what would count as failure. Fix acceptance criteria from the task requirements
   or reference before comparing runs. If a bound is unknown, report the measurement
   and leave the corresponding claim unverified.
2. Use the [Newton documentation](https://newton-physics.github.io/newton/) for the
   installed release to identify supported checks and observables. Run the checks
   that could falsify the claim on the actual simulation or its recorded trajectory.
   For example, check units, scales and invariants, inspect collision geometry
   independently of visual geometry, or compare contact onset, penetration,
   tunneling, constraint error and controller tracking against relevant references.
   For numerical claims, test convergence under timestep or substep refinement,
   repeat identical conditions for determinism, or vary uncertain inputs for sensitivity.
3. In long-running rollouts, monitor the task's motion, travel and force bounds
   before awarding success. Record the first violation and terminate the invalid
   episode. When auditing recorded runs, apply the same checks over the trajectory.
   Count invalid episodes as failed attempts even if they end in a plausible pose.
4. Report each claim as **passed**, **failed**, or **unverified**, with the measured
   evidence, criterion, and relevant uncertainty or missing input. Across seeds,
   report valid successes out of all attempts, the invalid count, and variability.
   State what an analytic check establishes about solver behavior, what the task
   measurements establish about fidelity, and what a comparison with another
   simulator establishes about agreement. Hardware transfer requires corresponding
   experimental or real-robot evidence for the intended use.

Compatibility across Newton releases has not been validated.
