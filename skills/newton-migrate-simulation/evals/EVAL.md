# Evaluation Scope

This suite measures evidence-driven migration from a named source simulator to
Newton. It checks convention and feature mapping, minimal-scene porting,
behavioral comparison, and explicit unsupported differences.

## Behaviors

- Identify source and target versions and the intended migration outcome.
- Inventory assets, conventions, controls, contacts, limits, and reference runs.
- Map only documented features and inspect effective imported properties.
- Compare representative source and target behavior with fixed acceptance bounds.
- Avoid activating only when there is no source simulator and no source assets to migrate; asset reuse and controller reuse do not require a parity objective.

## Notes

Run paired Codex and Claude Code trials with at least three attempts per case.
Executable parity cases need source and target fixtures plus deterministic
comparisons. Real-world transfer remains unverified without hardware evidence.
