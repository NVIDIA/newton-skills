---
name: newton-migrate-simulation
description: Port assets or simulation behavior from another simulator to Newton, checking mappings, supported features and behavioral parity.
metadata:
  target-newton-version: "1.6.0"
  validation-status: "early-v2; behavioral validation pending; not for release"
---

Identify source simulator/version, target Newton release and migration intent:
asset reuse, controller reuse or behavioral parity. Inventory referenced assets,
used physics features, units, frames, drives, limits, collision representation
and source reference runs. Preserve originals and record intentional changes.

Use the installed Newton release and matching public documentation and packaged
examples. This candidate targets 1.6.0 for evaluation; no supported version range
has been validated. Warn on other versions and check interfaces before proceeding.
Read the applicable versioned documentation directly when known. Otherwise use
https://newton-physics.github.io/newton/1.6.0/genindex.html to locate the relevant
API, concept or packaged example. Read the needed section, not the whole site.
If search fails, use index/navigation and installed public signatures. No source
checkout or other skill is required.

Use source-specific migration guidance, Newton USD/import documentation and the
nearest packaged example. Distinguish geometry successfully loading from physics
properties being applied. Inspect effective imported values and warnings;
schema resolution and backend consumption must both support the intended feature.
Do not assume one-to-one defaults or transplant gains/contact settings blindly.

Port the smallest representative scene first. Compare structure and conventions,
then uncontrolled motion, a simple control command and relevant contact behavior.
Use task-specific acceptance bounds and comparable source/target runs. Inspect
effective model/state data and test a second meaningful asset configuration to
reject a fixture-specific mapping. Record changed or dropped features; successful
loading alone cannot establish parity. Where a
feature is unsupported, explain the effect and available documented alternatives
without silently changing the problem.

For an observed failure, reproduce and isolate it before changing mappings or
solver settings. Report retained, remapped, unsupported and intentionally changed
behavior, runnable commands and evidence. Without a source reference, leave parity
unverified; without hardware evidence, leave real-world transfer unverified.
