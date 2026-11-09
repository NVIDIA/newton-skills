# Evaluation Scope

This candidate suite measures migration to Newton from a source simulator or
existing assets. It does not yet establish a distinct PhysX migration workflow.
The PhysX-to-Newton investigation requested in PR #11 must supply concrete
findings and reference cases before that coverage can be claimed; otherwise
fold useful guidance into `newton-usage`.

## Behaviors

- Identify source and installed target versions and the intended reuse/parity goal.
- Keep planning checks proposed when assets are not supplied; require executed
  verification only for authorized implementation. Allow a public-documentation
  fallback when the general usage skill is absent.
- Inventory assets, conventions, controls, contacts, limits, and reference runs.
- Select matching documentation without pinning the skill to a particular release.
- Before installation, use the stated target for planning documentation; verify
  the actual installed release before implementation and flag target mismatches.
- Prefer matching installed documentation when available; allow focused follow-up
  retrieval for each feature in the source inventory.
- Map documented features and inspect effective imported properties and backend support.
- Compare source and target behavior with fixed bounds when parity is requested
  and reference runs are available; reuse-only tasks do not require a parity goal.
- Report all material unsupported or intentionally changed features. Without a
  source reference, leave behavioral parity unverified.
- Require a Newton target; source assets alone do not activate this skill for a
  migration to another simulator. Route new construction to `newton-usage`.

## Notes

Run paired Codex and Claude Code trials with and without the skill, at least
three attempts per case. Record evaluator revision, agent/model versions,
Newton/environment versions, per-case correctness, total tokens including
loading/retries, elapsed time, and variability. Executable parity cases need
source and target fixtures plus independent comparisons. No compatibility range,
PhysX migration correctness, or real-world transfer is established by these
planning cases. Preserve generated artifacts and obtain fresh NVSkills evaluation
and signing after the changes.
