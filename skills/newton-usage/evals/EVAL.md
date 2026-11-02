# Evaluation Scope

This suite measures documentation, example, and specialized-skill routing for
the released Newton wheel. It covers explicit, implicit, contextual, negative,
and cross-skill prompts. Tasks request instructions only; they do not require a
GPU or execute simulations. These cases do not establish simulation correctness.

## Behaviors

- Distinguish command-only guidance from active environment discovery.
- For active discovery, collect the installed version, package path, and packaged
  examples with one bounded probe and use matching public documentation.
- Find packaged examples without requiring a source checkout.
- Explicitly hand focused workflows to the matching specialized Newton skill and
  make that skill the primary owner.
- Preserve environment restrictions and distinguish advice from verified results.
- Keep Newton's method questions outside the physics-simulator skill.
- Keep source-repository CI maintenance outside this wheel-consumer skill.

## Notes

Run paired trials with and without the skill in otherwise identical environments
on both Claude Code and Codex. Use the same public documentation access in both
arms. Repeat trials to measure variance. Report task correctness, routing,
total token consumption including skill loading and retries, and elapsed time.
Skill-reading assertions apply to the with-skill arm; the baseline is judged on
the task outcome and substantive behaviors without requiring skill discovery.

Use at least three attempts per case for publication evidence. Publication
requires improved task performance or efficiency without correctness regressions.
Record evaluator, agent/model, environment, elapsed time, token coverage, per-case
results, pass@1, pass@3, and the worst component score in the generated benchmark.
Also inspect total tool calls, repeated documentation URLs, and repeated environment
probes when comparing cost. Keep executable simulation and GPU evidence in the
applicable specialized skill evaluations.

Skill execution is the source of truth for whether a skill was read or activated.
Behavior assertions should judge the observable workflow and must not duplicate
activation checks that can contradict trajectory-based skill-execution evidence.
