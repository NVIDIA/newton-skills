# Evaluation Scope

This suite measures diagnosis of observable Newton failures. It tests whether the
agent reproduces and classifies the symptom, uses documented discriminating
checks, makes a minimal correction, and verifies the original case.

## Behaviors

- Capture version, backend/device, solver, cadence, reproducer, and expected behavior.
- Preserve the symptom while reducing the scene and collecting evidence.
- Distinguish model, control, contact, solver, and environment causes.
- Verify the reduced and original cases and separate proven from unverified claims.
- Avoid activating for initial construction, pure profiling, migration, or validation-only work.

## Notes

Run paired Codex and Claude Code trials with at least three attempts per case.
Add a deterministic executable contact or stability grader before publication.
GPU-dependent claims require project-owned GPU-backed evidence in addition to
the NVCARPS report.
