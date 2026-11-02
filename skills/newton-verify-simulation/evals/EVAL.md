# Evaluation Scope

This suite measures independent verification of Newton simulation claims. It
checks acceptance criteria, falsifying tests, trajectory/state evidence,
sensitivity or reference comparisons, and calibrated passed/failed/unverified
conclusions.

## Behaviors

- Separate solver execution, simulation fidelity, parity, and real-world validity.
- Derive task-specific bounds from requirements or references.
- Inspect actual model/state evidence over the relevant horizon.
- Validate checks with known-valid, invalid, and misleading-output controls.
- Avoid activating when the primary task is building, debugging, or optimization.

## Notes

Run paired Codex and Claude Code trials with at least three attempts per case.
Use deterministic executable graders for numerical checks where practical.
GPU and real-world claims require evidence from the corresponding environment.
The DisplayPort case evaluates rejection of physically invalid successes and
claim boundaries; numerical thresholds remain owned by the project workload.
