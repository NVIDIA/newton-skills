---
name: newton-debug-simulation
description: Diagnose incorrect motion, contact failures, instability, import errors, or runtime failures in an existing Newton simulation.
metadata:
  target-newton-version: "1.6.0"
  validation-status: "early-v2; behavioral validation pending; not for release"
---

Resolve the observable failure with the smallest evidence-supported correction.
Preserve the intended physical model. A correct simulation may need no change.

Capture version, backend/device, reproducer, solver and relevant simulation,
collision and controller cadences. Establish expected behavior and a measurable
failure before editing. Reduce the scene while retaining the symptom; for a
late failure preserve the first invalid state, reset history and commands.

Use the installed Newton release and matching public documentation and packaged
examples. This candidate targets 1.6.0 for evaluation; no supported version range
has been validated. Warn on other versions and check interfaces before proceeding.
Read the applicable versioned documentation directly when known. Otherwise use
https://newton-physics.github.io/newton/1.6.0/genindex.html to locate the relevant
API, concept or packaged example. Read the needed section, not the whole site.
If search fails, use index/navigation and installed public signatures. No source
checkout or other skill is required.

Route physical symptoms through the release's Simulation Tuning guidance;
route import, controller, coupling and runtime failures to their specific docs.
Distinguish initialization/model, control, contact generation/capacity, solver
response and environment causes with a discriminating measurement before tuning.
A parameter existing does not prove that the active backend consumes it.

Change one causal factor when possible and discard ineffective edits. Re-run
the reduced and original cases against the agreed bounds and verification
horizon. Compare actual solver states with reported trajectories; filtering or
clamping reported data does not repair physics. Preserve acceptance bounds and
required physics while testing a fix. Task reward alone is insufficient. Report cause,
before/after evidence, reproduction command and what remains unverified. Do not
claim GPU resolution from CPU execution or long-run resolution from a short run.
