# Evaluation Scope

This suite measures documentation and example routing, supported simulation
construction, and symptom triage for the released Newton wheel. Planning cases
permit focused documentation retrieval while preserving user execution limits.
They do not establish executable simulation correctness or a compatibility range.

## Behaviors

- Keep metadata probes in the existing task environment without syncing
  dependencies, creating environments, installing extras, or updating locks.
- Reuse known facts and identify the installed version before release-specific work.
- Find matching documentation and packaged examples without requiring a checkout.
- Reuse the selected interpreter or verified non-syncing wrapper for example
  listing, help, and launch, even when the project environment is not activated.
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

## Compare revisions

To measure a revision's incremental value, run the same frozen task set with
the base and proposed skills. Include a no-skill arm when claiming a benefit
over the unaided agent. Keep fixtures and permissions identical, start fresh
sessions, and apply the same repetition and reporting rules above. Include
simple setup and discovery tasks so they expose any added context cost.

## Executable construction case

Run this case outside the catalog's planning and routing suite. Use the same
preinstalled Newton 1.8.0 wheel and CPU device in every arm. Give the agent an
empty writable directory and this prompt, then grade its output separately.

> Create `scene.py` using the installed Newton package on CPU. Drop a dynamic
> sphere of radius 0.2 m from rest at a center height of 1 m onto a flat ground
> plane at z=0 under ordinary gravity. Simulate two seconds without a viewer.
> Expose a parameterless `simulate()` that runs the scene and returns the
> sphere's world-space center heights at 120 Hz, including the initial sample.
> Run it and report evidence that the sphere fell, settled on the ground, and
> did not penetrate it by more than 3 cm.

From the attempt's working directory, run
`python <evals-directory>/check_sphere_drop.py scene.py` with the same
interpreter. The checker calls the submitted simulation and checks its initial
height, descent, maximum sampled penetration, and settling. Check that the
submission actually steps Newton and samples its state. A missing script or
failed check fails the case.
