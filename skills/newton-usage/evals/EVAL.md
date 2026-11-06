# Evaluation Scope

This smoke suite measures documentation and example routing for the Newton
wheel. It covers explicit, implicit, contextual, and negative prompts. Tasks
request instructions only; they do not require a GPU or execute simulations.
These cases do not establish simulation correctness or a supported Newton
version range.

## Behaviors

- Discover the installed version and prefer its bundled documentation when
  available; use matching hosted docs for older wheels and report offline gaps.
- Locate relevant local guides and API pages through targeted search, the
  generated index, or object/symbol lookup without requiring Sphinx, a source
  checkout, network access, or a simulation run. Index reading is optional;
  accept installed introspection for simple signature/docstring questions.
- Find packaged examples without requiring a source checkout.
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

Publication requires improved task performance or efficiency without correctness
regressions. Record the evaluator revision, agent/model versions, run conditions,
and per-case results in the generated benchmark. Revalidate changed workflow
content rather than treating an earlier benchmark as evidence for the update.
Keep larger executable simulation evaluations separate from this routing suite.
