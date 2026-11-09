# Evaluation Scope

This suite measures documentation and example routing, supported simulation
construction, and symptom triage for the released Newton wheel. Planning cases
permit focused documentation retrieval while preserving user execution limits.
They do not establish executable simulation correctness or a compatibility range.

## Behaviors

- Reuse known facts and identify the installed version before release-specific work.
- Find matching documentation and packaged examples without requiring a checkout.
- Define acceptance criteria before building and choose the simplest supported
  solver configuration, including a single solver before unnecessary coupling.
- Preserve assets and avoid installing dependencies without authorization.
- Check effective model state, finite values, penetration, joint travel, and task
  behavior over the required horizon instead of relying on rendered appearance.
- Respect harness permissions; permit read-only documentation lookup during planning.
- Preserve metadata when import fails and honor version-only requests that prohibit
  direct or indirect Newton imports.
- Handle ordinary construction without depending on a separate build skill.
- Keep calculus and source-repository CI maintenance outside this skill's scope.

## Comparison Protocol

Run paired trials with and without the skill on Codex and Claude Code, with at
least three attempts per case and the same environment and documentation access.
Judge outcomes independently of activation; credit equally correct alternatives.
Record evaluator revision, agent/model versions, Newton/environment versions,
per-case correctness, total tokens including loading/retries, elapsed time, and
variability. Report correctness and efficiency separately; do not infer uplift
from activation or a pipeline PASS. Preserve generated artifacts and obtain fresh
NVSkills evaluation and signing after these changes. Simulation correctness needs
separate executable task evidence; GPU claims require GPU-backed execution.
