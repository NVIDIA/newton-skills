# Evaluation Scope

Measure diagnosis and verified repair of observable Newton failures, rather than
only diagnostic advice. Run the supplied failures in a released-wheel environment
with NumPy and Warp (Newton dependencies); a source checkout is optional. Newton
1.7.0 is the local fixture test version, not a skill compatibility restriction.

## Behaviors

- Keep metadata probes in the existing task environment without syncing
  dependencies, creating environments, installing extras, or updating locks.

- Record version, device, solver, cadence, expected behavior, and reproduction.
- Use the reproducer interpreter and wrapper, collect metadata before importing,
  and verify pre-simulation failures with the failing probe before requiring a rollout.
- Reduce while retaining the symptom; preserve the first invalid state and input.
- Distinguish model, control, contact generation, solver, and environment causes.
- Allow focused follow-up documentation retrieval when evidence changes the route.
- Verify the reduced and original cases over the required horizon with fixed bounds.
- Record every attempted correction, including unnecessary and discarded changes.
- Test natural boundaries for construction, profiling, migration, validation-only,
  and contributor work without announcing which skill should apply.

## Executable Cases

The evaluator copies `fixtures/contact.py` and `fixtures/controller.py` into a
fresh agent workspace under those basenames. Supply the files and task prompt
in both comparison arms. If using the prompts' fixture-directory fallback, expose
the same read-only input directory in both arms without requiring skill activation
in the baseline. A missing fixture or missing Newton environment is a setup
failure, not a diagnosis or repair result. Keep `grade.py`, acceptance bounds,
and a pristine fixture copy outside the writable agent workspace. Run the independent grader
against the pristine fixture before the trial and the candidate after it:

```bash
python grade.py --case contact --candidate /trial/contact.py --output-dir /evidence/contact
python grade.py --case controller --candidate /trial/controller.py --output-dir /evidence/controller
```

Run each command with the same environment and `--device` before and after repair.
Use unique output directories for each arm, attempt, and before/after run.
Run `python test_grade.py` to verify that empty, truncated, or non-numeric scene
traces are reported as failures while the remaining scene is graded and a report
is written.
`WARP_CACHE_PATH` can point to a writable compiler cache. Baselines must exit 1
because of the intended physics checks, not import or execution errors. Each
candidate must complete both `--scene reduced` and `--scene original` and exit 0.
Preserve commands, logs, exit statuses, numerical traces, reports, and the diff.
Review the execution trajectory to record unnecessary changes attempted; the
numerical grader alone cannot determine what the agent tried or establish that
traces are honest. Do not allow edits to the grader or evidence fabrication.

- Contact: 720 steps at 1/240 s, radius 0.1 m, one sphere in the reduced scene and
  three in the original. Require finite poses/velocities, initial fall, minimum
  center height at least 0.095 m, and settling within 0.01 m of 0.1 m over the final
  120 samples. Preserve geometry, timestep, solver, initial state, and duration.
- Controller: 3600 steps at 0.001 s, one body in the reduced scene and three in
  the original. Require finite state through the full horizon, unchanged command
  schedule, and position within 0.02 m of the independent force/mass integration
  reference. Check transverse scene coordinates. A frozen or clipped trajectory
  fails even when finite. Record the first invalid sample and preceding command.

These cases exercise a contact-generation failure and a late controller failure;
they do not establish general solver, importer, coupling, or training coverage.
Add held-out failures before making broader claims. GPU claims require matching
GPU-backed execution; the CPU fixture smoke run establishes only CPU behavior.

## Public Documentation Coverage

Select the installed release before using these current documentation entrypoints:

| Diagnostic question | Public Newton documentation | Coverage or remaining gap |
| --- | --- | --- |
| Penetration and false success | [Simulation tuning](https://newton-physics.github.io/newton/latest/concepts/simulation_tuning.html#diagnose-before-tuning), [contacts](https://newton-physics.github.io/newton/latest/concepts/collisions.html) | Geometry, task metrics, contact generation, and capacity are covered. A consolidated false-success checklist for reward, overtravel, and penetration has not been established for the target release; record this as a documentation gap. |
| Late invalid rollout | [Tuning guardrails](https://newton-physics.github.io/newton/latest/concepts/simulation_tuning.html#tuning-order), [observables](https://newton-physics.github.io/newton/latest/concepts/solver_observables.html) | Existing guardrails cover non-finite state. A public first-invalid-transition and full-horizon replay procedure has not been established for the target release; record this as a documentation gap. |
| Model import errors | [USD parsing](https://newton-physics.github.io/newton/latest/concepts/usd_parsing.html), [articulations](https://newton-physics.github.io/newton/latest/concepts/articulations.html), applicable importer API | Verify the actual format's importer, schema resolution, imported properties, and backend support; USD guidance alone does not cover every importer. |
| Controller and coupling configuration | [Tuning classification](https://newton-physics.github.io/newton/latest/concepts/simulation_tuning.html#diagnose-before-tuning), [coupled solvers](https://newton-physics.github.io/newton/latest/concepts/coupling.html), [solver capabilities](https://newton-physics.github.io/newton/latest/solvers/index.html) | Control/model causes, ownership, and backend state synchronization are covered. Verify each link against the installed release; do not infer a complete late-failure troubleshooting procedure from these separate references. |

This PR identifies existing public coverage and records the remaining gaps; it
does not supply or depend on a companion PR in another repository. Those gaps
remain unresolved and must be reported as such when assessing documentation
completeness. The executable fixtures demonstrate only the specific failures
and repairs described above.

Keep durable diagnostic explanations in Newton, not in the skill instructions.

## Comparison Protocol

Run paired Codex and Claude Code trials with and without the skill, at least
three attempts per case, with identical fixtures, environment, and documentation
access. Judge task outcomes independently of activation and credit alternative
correct repairs. Record evaluator revision, agent/model versions, Newton and
environment versions, per-case correctness, total tokens including loading and
retries, elapsed time, variability, and unnecessary changes attempted. No paired
agent results are claimed by fixture smoke checks. Obtain fresh NVSkills evaluation
and signing after skill or evaluation changes; preserve generated artifacts.

## Local Fixture Smoke Check

On 2026-11-09 with the released Newton 1.7.0 wheel on CPU, the independent
grader rejected both pristine failures and accepted minimal reference repairs
in both scene sizes. The contact failure reached -43.2063 m; refreshed-contact
reference runs had a minimum height of 0.09999995 m and settled at 0.1 m. The
controller first became invalid at sample 2401; the guarded-normalization
reference runs completed all 3600 steps with maximum position error below
0.000074 m. Frozen trajectories were independently rejected for both cases and
scene sizes. These are evaluator smoke results, not paired agent performance
results or GPU evidence.
