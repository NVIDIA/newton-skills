---
name: newton-build-simulation
description: Set up a Newton user simulation and select supported models, solvers, controllers or coupling for a stated workload.
metadata:
  target-newton-version: "1.6.0"
  validation-status: "early-v2; behavioral validation pending; not for release"
---

Build the smallest runnable simulation that meets the user's intended behavior.
Inventory reusable assets/code, hardware, units, frames, control inputs and
required physics. Clarify missing information only when it changes the design;
state reversible assumptions and proceed otherwise.

Use the installed Newton release and matching public documentation and packaged
examples. This candidate targets 1.6.0 for evaluation; no supported version range
has been validated. Warn on other versions and check interfaces before proceeding.
Read the applicable versioned documentation directly when known. Otherwise use
https://newton-physics.github.io/newton/1.6.0/genindex.html to locate the relevant
API, concept or packaged example. Read the needed section, not the whole site.
If search fails, use index/navigation and installed public signatures. No source
checkout or other skill is required.

Find the nearest packaged example and capability/solver documentation. Rank only
options relevant to the workload, explaining the deciding support or fidelity
tradeoff. Start with the simplest supported configuration; add coupling only
when the required behavior needs it. Do not infer compatibility from shared API
signatures or promise unsupported features.

Adapt the example through public APIs, retaining the user's model semantics.
Check import/build structure, initialization, a short trajectory and task-specific
physical bounds on the actual device. Inspect effective model properties and
solver states, not only rendered or returned output. Preserve required features;
an omitted constraint is not a successful setup. Keep visualization optional when the
task is headless. Report a runnable command, assumptions, selected components,
measured checks and unsupported needs. Reuse the user's working environment;
do not install extra stacks or create a checkout without a demonstrated need.
