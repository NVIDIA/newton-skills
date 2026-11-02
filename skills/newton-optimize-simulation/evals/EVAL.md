# Evaluation Scope

This suite measures optimization of a correct, reproducible Newton workload. It
checks baseline definition, appropriate instrumentation, bottleneck attribution,
comparable before/after measurement, and preservation of physical validity.

## Behaviors

- Separate startup, warm stepping, rendering, transfers, memory, and training.
- Account for warm-up, synchronization, profiler overhead, and privileges.
- Choose documented changes from measured bottlenecks.
- Compare repeated equivalent runs and recheck simulation validity.
- Avoid activating for correctness failures or unmeasured tuning requests.

## Notes

Run paired Codex and Claude Code trials with at least three attempts per case.
Executable CPU cases may use deterministic timing-boundary checks, but GPU
speedup claims require team-owned GPU-backed measurements.
The DisplayPort case evaluates the measurement plan and acceptance logic; it is
not a substitute for running the project-owned workload on the target GPU.
