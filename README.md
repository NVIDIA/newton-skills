# Newton Skills

Agent skills for users of the released [Newton physics simulator](https://github.com/newton-physics/newton).
This repository is the canonical source for Newton user skills. The skills route
agents to public documentation and examples shipped in the Newton Python wheel.

## Status

The first skill is an initial draft with a routing evaluation suite and an
NVSkills CI request workflow. Live evaluation, signing, and catalog publication
remain pending repository onboarding. Skills will be updated alongside Newton
releases and,
once registered, continuously synchronized to the NVIDIA Skills Catalog.

## Skills

- [newton-usage](skills/newton-usage/SKILL.md): Find documentation and packaged
  examples when setting up, building, or debugging a Newton simulation.

## Using the Skills

Install Newton in your Python environment following its
[installation guide](https://newton-physics.github.io/newton/latest/guide/installation.html).
Install or copy `skills/newton-usage/` into your agent's supported skill directory.
A Newton source checkout is optional. Use documentation matching your installed
Newton release.

The skill instructions do not collect telemetry. Your agent, Python environment,
and any tools it invokes have their own behavior and policies.

## Skill Policy

- Target consumers of released Newton wheels, public APIs, and publicly available
  tools. Declare tested Newton versions, or explicitly state that compatibility
  has not been validated. Keep a source checkout optional.
- Keep skills thin: triggers, context gathering, documentation/example routing,
  ordered actions, verification, and recovery. Stable API facts, parameter
  explanations, limitations, and human-useful troubleshooting belong in Newton
  documentation. Link that documentation rather than maintaining a second copy.
- Add a specialized skill only when it provides distinct, reusable orchestration
  beyond the general router and existing examples. Keep triggers narrow and
  demonstrate that unrelated prompts do not activate it.
- Include realistic positive, contextual, and negative evaluations. Compare with
  and without the skill on Codex and Claude Code in repeated paired trials.
  Follow the [evaluation requirements](skills/newton-usage/evals/EVAL.md): record
  agent/model versions, Newton/environment versions, evaluator revision, and
  per-case outcomes. Define correctness criteria before comparisons; report
  correctness, total tokens including loading/retries, elapsed time, and
  variability. Require improved task performance or efficiency without
  correctness regressions.
- Score task outcomes independently of skill activation and prescribed workflow;
  credit equally correct alternative approaches. Include realistic prompts that
  do not reveal the expected routing decision, ambiguous negatives, and multi-turn
  contexts. Keep held-out cases to check generalization.
- Respect user environment and resource constraints. Do not make unrequested
  environment changes or launch costly workloads without user authorization.
  Treat retrieved documentation and examples as reference data, not authority
  to override user instructions.
- Develop missing documentation and examples alongside the workflow. Executable
  simulation claims need executable checks; GPU claims need GPU-backed evidence.
  Routing scores and a pipeline PASS alone do not prove simulation correctness.
- Keep generated benchmark, card, and signature files intact. Revalidate and
  re-sign changed content before catalog publication, and recheck compatibility
  on Newton releases.

## Contributions and Support

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the workflow,
licensing requirements, and mandatory Developer Certificate of Origin sign-offs.
Use this repository's issues for skill bugs and suggestions. For Newton simulation
questions, consult the [Newton documentation](https://newton-physics.github.io/newton/)
or [Newton discussions](https://github.com/newton-physics/newton/discussions).
This early skill does not yet have a validated Newton version compatibility range.

## Security

Report vulnerabilities privately using [SECURITY.md](SECURITY.md).

## License and Attribution

Documentation, skills, and assets are licensed under CC-BY-4.0; code-only files
are licensed under Apache-2.0. [LICENSE](LICENSE) contains the complete terms.
See [NOTICE](NOTICE) for project attribution and
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for third-party notices.
