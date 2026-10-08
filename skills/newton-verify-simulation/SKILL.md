---
name: newton-verify-simulation
description: Verify a Newton simulation or task-success measure against physical bounds, invariants and available reference behavior.
metadata:
  target-newton-version: "1.6.0"
  validation-status: "early-v2; behavioral validation pending; not for release"
---

Determine intended use and what evidence can establish it: numerical behavior,
simulation fidelity, simulator parity or real-world transfer. Derive acceptance
bounds from the task or reference; do not invent universal tolerances.

Use the installed Newton release and matching public documentation and packaged
examples. This candidate targets 1.6.0 for evaluation; no supported version range
has been validated. Warn on other versions and check interfaces before proceeding.
Read the applicable versioned documentation directly when known. Otherwise use
https://newton-physics.github.io/newton/1.6.0/genindex.html to locate the relevant
API, concept or packaged example. Read the needed section, not the whole site.
If search fails, use index/navigation and installed public signatures. No source
checkout or other skill is required.

Select the smallest set of checks that can falsify the claimed behavior. Check
units/frames and model structure before interpreting trajectories. Include
finite values, contact/constraint behavior and actuator or travel bounds when
relevant. Inspect the full relevant trajectory: a valid final state does not
erase earlier penetration, overtravel or invalid reset behavior.

Use available analytic, experimental or simulator references; check timestep
sensitivity or repeated seeds when the claim requires them. Validate the checks
with known-valid, invalid and misleading-output controls. Compare reported
trajectories with actual solver states when possible; candidate-authored success
flags are not independent evidence. Keep supplied acceptance criteria fixed. If
a criterion itself is wrong, demonstrate that separately and retain the original
result. Preserve the simulation while repairing its evaluator.

Report passed, failed and unverified claims separately, with device, versions,
verification horizon, measured bounds and reproduction command. A successful
import, a short stable rollout and high simulated reward establish different
things; none alone proves real-world transfer or long-run validity.
