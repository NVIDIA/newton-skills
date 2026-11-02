# Newton Skills

Agent skills for users of the released [Newton physics simulator](https://github.com/newton-physics/newton).
This repository is the canonical source for Newton user skills. The skills route
agents to public documentation and examples shipped in the Newton Python wheel.

## Status

The first skill is an initial draft with a routing evaluation suite. NVSkills CI
is configured for evaluation and signing; catalog publication is pending. Skills
will be updated alongside Newton releases and, once registered, continuously
synchronized to the NVIDIA Skills Catalog. Repository checks validate the
skill/evaluation contract and the installed Newton wheel.

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

These are minimum contribution requirements. Maintainers also review usefulness,
correctness, and overall quality before accepting changes.

### Skill Design

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
- Develop missing documentation and examples alongside the workflow.

### Validation and Review

- Match validation to the change. Documentation-only corrections need relevant
  link or command checks; changes to triggers or workflow behavior need relevant
  behavioral evaluations. Report checks performed and validation limitations.
- Use realistic positive, contextual, and negative prompts near the skill's scope
  boundary. Do not rely solely on prompts that name the skill or explicitly state
  whether it should apply. Add ambiguous negatives and multi-turn cases where
  relevant; use held-out cases when assessing generalization.
- Claims of improved quality or efficiency require repeated paired comparisons
  with and without the skill on Codex and Claude Code. Follow the
  [comparison protocol](skills/newton-usage/evals/EVAL.md): define correctness
  criteria first; record agent/model versions, Newton/environment versions,
  evaluator revision, and per-case outcomes. Report correctness, total tokens
  including loading/retries, elapsed time, and variability. Demonstrate the
  claimed improvement without correctness regressions.
- Judge task outcomes independently of skill activation and prescribed workflow;
  credit equally correct alternative approaches. CI establishes only the results
  of its configured checks. Maintainers separately assess task usefulness,
  correctness, and claimed improvements. Executable simulation claims need
  executable checks; GPU claims need GPU-backed evidence.
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

### NVSkills Validation

For PRs changing `skills/`, a repository maintainer or admin must post a new
`/nvskills-ci` comment to start evaluation and signing. Post it again after further
skill or evaluation changes. Opening or updating a PR only checks validation
status; it does not start evaluation. Changes outside the watched paths
(`skills/` and `team-skills/`) do not require a new evaluation.

Wait for successful NVSkills CI validation and inspect the generated benchmark,
card, and signature commit before merging. Do not edit generated artifacts by
hand. If the validation-status check failed before validation started, rerun that
failed check after validation succeeds; rerunning the check alone does not start
evaluation.

For fork PRs, the signing service account `svc-nvskills-signing` needs write access
to the fork to commit generated artifacts. A maintainer or admin of this repository
must still post the command. See the
[shared request workflow](https://github.com/NVIDIA/skills/blob/main/.github/workflows/team-request.yml).

## Security

Report vulnerabilities privately using [SECURITY.md](SECURITY.md).

## License and Attribution

Documentation, skills, and assets are licensed under CC-BY-4.0; code-only files
are licensed under Apache-2.0. [LICENSE](LICENSE) contains the complete terms.
See [NOTICE](NOTICE) for project attribution and
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for third-party notices.
