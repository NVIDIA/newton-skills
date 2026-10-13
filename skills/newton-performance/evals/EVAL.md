# Evaluation Scope

This smoke suite measures routing and the core guidance of the performance skill
for the Newton wheel. It covers explicit, implicit, contextual, and negative
prompts. Tasks request reviews or instructions only; they do not require a GPU
or execute simulations. These cases do not establish measured speedups or a
supported Newton version range.

## Behaviors

- Detect the odd-substep state-swap trap in captured step loops and apply the
  documented fix.
- Recognize host syncs and Python state that a CUDA graph freezes.
- Size collision and solver buffers correctly: pipeline capacities are totals
  across worlds, MuJoCo capacities are per world.
- Distinguish advice from verified results and avoid claiming measurements.
- Leave general setup and example discovery to `newton-usage`.

## Notes

Run paired trials with and without the skill in otherwise identical environments
on both Claude Code and Codex. Use the same public documentation access in both
arms. Repeat trials to measure variance. Report task correctness, routing,
total token consumption including skill loading and retries, and elapsed time.
Skill-reading assertions apply to the with-skill arm; the baseline is judged on
the task outcome and substantive behaviors without requiring skill discovery.

The skill's code snippets and the odd-substep behavior were checked manually on
a GPU against Newton 1.6.1 and Warp 1.18.0; those checks are not part of this
suite. No live trial results exist yet. Keep larger executable performance
evaluations separate from this routing suite.
