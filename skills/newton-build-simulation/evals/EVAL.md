# Evaluation Scope

This suite measures whether an agent turns a stated workload into a supported,
minimal Newton simulation while keeping debugging, migration, optimization, and
independent validation outside this skill's scope.

## Behaviors

- Confirm the Newton version, environment, assets, conventions, and acceptance behavior.
- Cite the direct stable Newton 1.7 documentation route for a plan; open it only
  when exact API confirmation or implementation requires its contents.
- Rank supported choices and implement the smallest suitable configuration.
- Inspect effective model and solver state and report unsupported requirements.
- Avoid activating for an existing failure, migration, profiling, or validation-only task.

## Notes

Run paired trials with and without the skill on Codex and Claude Code with at
least three attempts per case. Use the same pinned Newton wheel and public
documentation in both arms. Executable build cases should run in a clean
PyPI-only environment and use deterministic checks where practical.
