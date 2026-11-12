## Description: <br>
Diagnose a reproducible Newton motion, contact, stability, import, controller, coupling, CUDA, or runtime failure; not for tuning a correct workload or independently validating a result. <br>

This skill is ready for commercial/non-commercial use. <br>

## Owner
NVIDIA <br>

### License/Terms of Use: <br>
CC-BY-4.0 AND Apache 2.0 <br>
## Use Case: <br>
Developers and engineers using the Newton physics simulator use this skill to isolate an observable, reproducible simulation failure (motion, contact, stability, import, controller, coupling, CUDA, or runtime) and make the smallest evidence-supported correction, verified against the reduced and original cases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Requirements / Dependencies: <br>
**Requires API Key or External Credential:** [Not Specified] <br>
**Credential Type(s):** [None identified] <br>

Do not include secrets in prompts/logs/output; use least-privilege credentials; rotate keys as appropriate. <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [Newton physics simulator (GitHub)](https://github.com/newton-physics/newton) <br>
- [Newton simulation tuning](https://newton-physics.github.io/newton/latest/concepts/simulation_tuning.html) <br>
- [Newton collisions](https://newton-physics.github.io/newton/latest/concepts/collisions.html) <br>
- [Newton solver observables](https://newton-physics.github.io/newton/latest/concepts/solver_observables.html) <br>
- [Newton viewers and debugging](https://newton-physics.github.io/newton/latest/guide/visualization.html) <br>
- [Newton solver guidance](https://newton-physics.github.io/newton/latest/solvers/index.html) <br>
- [Newton compatibility](https://newton-physics.github.io/newton/latest/guide/compatibility.html) <br>
- [Newton installation](https://newton-physics.github.io/newton/latest/guide/installation.html) <br>
- [Newton USD parsing](https://newton-physics.github.io/newton/latest/concepts/usd_parsing.html) <br>
- [Newton articulations](https://newton-physics.github.io/newton/latest/concepts/articulations.html) <br>
- [Newton coupling](https://newton-physics.github.io/newton/latest/concepts/coupling.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Shell commands, Code] <br>
**Output Format:** [Markdown diagnostic report with inline code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports version/environment, documentation route, reproduction command, cause, before/after evidence, smallest supported fix, and any blocker or unverified claim.] <br>

## Evaluation Agents Used: <br>
- Claude Code (`aws/anthropic/bedrock-claude-opus-5-5`) <br>
- Codex (`openai/openai/gpt-6.1-sol`) <br>



## Evaluation Tasks: <br>
10 evaluation tasks (5 positive, 5 negative), 1 attempt per task, each run in its own isolated sandbox pod (`k8s-sandbox` environment); each task was also attempted without the skill as a baseline. <br>

## Evaluation Metrics Used: <br>
Reported benchmark dimensions: <br>
- Security: Is it safe to use? Scored from `security` (100%). <br>
- Correctness: Is the answer correct? Scored from `accuracy` (100%). <br>
- Discoverability: Was the right skill loaded when needed? Scored from `skill_execution` (100%). <br>
- Effectiveness: Did the skill help complete the task? Scored from `goal_accuracy` (50%) + `behavior_check` (50%). <br>
- Efficiency: Did it avoid wasted tool calls and token usage? Scored from `skill_efficiency` (50%) + `token_efficiency` (50%). <br>

Underlying evaluation signals used in this run: <br>
- `security`: Security: unsafe operations, secret leakage, and unauthorized access. <br>
- `skill_execution`: Skill Execution: whether the expected skill was selected, decoys were avoided, and the workflow executed. <br>
- `skill_efficiency`: Tool Productivity: tool-call productivity (legacy wire id; routing is scored under Discoverability). <br>
- `accuracy`: Accuracy: final-answer correctness against the reference answer. <br>
- `goal_accuracy`: Goal Accuracy: whether the user's goal was achieved. <br>
- `behavior_check`: Behavior Check: whether the expected workflow behavior was followed. <br>
- `token_efficiency`: Token Efficiency: actual uncached prompt plus completion usage (50% of Efficiency). <br>



## Evaluation Results: <br>
> ✅ **Overall verdict: PASS — Recommended for publication**

### Publication Recommendation

Recommended for publication based on the completed evaluation evidence in this report.

### Results at a Glance

| Measure | Claude Code (Baseline → Skill Uplift) | Codex (Baseline → Skill Uplift) |
|---|---:|---:|
| Overall | 90.6% — baseline ran, but no comparable score was available; uplift unavailable | 84.1% — baseline ran, but no comparable score was available; uplift unavailable |
| Security | 90.0% → 90.0% (±0.0 points) | 80.0% → 100.0% (+20.0 points) |
| Correctness | 66.0% → 88.0% (+22.0 points) | 74.0% → 88.0% (+14.0 points) |
| Discoverability | 100.0% — baseline ran, but no comparable score was available; uplift unavailable | 90.0% — baseline ran, but no comparable score was available; uplift unavailable |
| Effectiveness | 66.3% → 77.5% (+11.2 points) | 70.8% → 72.5% (+1.7 points) |
| Efficiency | 97.7% — baseline ran, but no comparable score was available; uplift unavailable | 70.0% — baseline ran, but no comparable score was available; uplift unavailable |

**How to read this table:** baseline is the same task attempted without the target skill. Scores are rounded to one decimal; threshold-adjacent values use additional precision so their displayed band matches the verdict. Uplift is derived from those displayed scores and shown in percentage points.

Example: `47.0% → 92.0% (+45.0 points)` means the skill-assisted run scored 92.0%, 45.0 percentage points above its 47.0% no-skill baseline.

A partial dimension was calculated from only the available configured signals; review the detailed report before relying on it.

### Comparison details

Shared-source comparisons use the same signals and weights on both conditions. They do not replace the full dimension scores above or change the publication verdict.

| Agent | Dimension | Basis | Baseline → With skill (uplift) | Explanation |
| --- | --- | --- | --- | --- |
| claude-code | Discoverability | Dimension comparison | N/A | Discoverability is not applicable to the no-skill baseline; there is no installed skill to discover. |
| claude-code | Efficiency | Token-only comparison | 96.4% → 95.4% (-1.0 points) | Only Token Efficiency is comparable; the full dimension scores use different evaluator sources. |
| codex | Discoverability | Dimension comparison | N/A | Discoverability is not applicable to the no-skill baseline; there is no installed skill to discover. |
| codex | Efficiency | Token-only comparison | 89.8% → 89.7% (-0.1 points) | Only Token Efficiency is comparable; the full dimension scores use different evaluator sources. |

## Skill Version(s): <br>
b86709e (source: git SHA, committed 2026-11-09) <br>

## Ethical Considerations: <br>
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their internal team to ensure this skill meets requirements for the relevant industry and use case and addresses unforeseen product misuse. <br>

(For Release on NVIDIA Platforms Only) <br>
Please report quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://app.intigriti.com/programs/nvidia/nvidiavdp/detail). <br>
