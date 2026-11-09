## Description: <br>
Diagnose a reproducible Newton motion, contact, stability, import, controller, coupling, CUDA, or runtime failure; not for tuning a correct workload or independently validating a result. <br>

This skill is ready for commercial/non-commercial use. <br>

## Owner
NVIDIA <br>

### License/Terms of Use: <br>
CC-BY-4.0 AND Apache 2.0 <br>
## Use Case: <br>
Developers and engineers using the released Newton physics simulator use this skill to reproduce, isolate, and minimally repair observable simulation failures (motion, contact, stability, import, controller, coupling, CUDA, or runtime) and report before/after evidence. <br>

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
- [Newton physics simulator](https://github.com/newton-physics/newton) <br>
- [Simulation tuning](https://newton-physics.github.io/newton/latest/concepts/simulation_tuning.html) <br>
- [Collisions](https://newton-physics.github.io/newton/latest/concepts/collisions.html) <br>
- [Solver observables](https://newton-physics.github.io/newton/latest/concepts/solver_observables.html) <br>
- [Viewers and debugging](https://newton-physics.github.io/newton/latest/guide/visualization.html) <br>
- [Solver guidance](https://newton-physics.github.io/newton/latest/solvers/index.html) <br>
- [Compatibility](https://newton-physics.github.io/newton/latest/guide/compatibility.html) <br>
- [USD parsing](https://newton-physics.github.io/newton/latest/concepts/usd_parsing.html) <br>
- [Articulations](https://newton-physics.github.io/newton/latest/concepts/articulations.html) <br>
- [Coupling](https://newton-physics.github.io/newton/latest/concepts/coupling.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Shell commands, Code] <br>
**Output Format:** [Markdown with inline Python and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Evaluation Agents Used: <br>
- Claude Code (`aws/anthropic/bedrock-claude-opus-5-5`) <br>
- Codex (`openai/openai/gpt-6.1-sol`) <br>



## Evaluation Tasks: <br>
9 evaluation tasks (4 positive, 5 negative), 1 attempt per task, each run in its own isolated sandbox pod (`k8s-sandbox`), with and without the skill. <br>

## Evaluation Metrics Used: <br>
Reported benchmark dimensions: <br>
- Security: Is it safe to use? Scored from `security` (100%). <br>
- Correctness: Is the answer correct? Scored from `accuracy` (100%). <br>
- Discoverability: Was the right skill loaded when needed? Scored from `skill_execution` (100%). <br>
- Effectiveness: Did the skill help complete the task? Scored from `goal_accuracy` (50%) + `behavior_check` (50%). <br>
- Efficiency: Did it avoid wasted tool calls and token usage? Scored from `skill_efficiency` (50%) + `token_efficiency` (50%). <br>

Underlying evaluation signals used in this run: <br>
- `security`: Unsafe operations, secret leakage, and unauthorized access. <br>
- `skill_execution`: Whether the expected skill was selected, decoys were avoided, and the workflow executed. <br>
- `skill_efficiency`: Tool-call productivity (legacy wire id; routing is scored under Discoverability). <br>
- `accuracy`: Final-answer correctness against the reference answer. <br>
- `goal_accuracy`: Whether the user's goal was achieved. <br>
- `behavior_check`: Whether the expected workflow behavior was followed. <br>
- `token_efficiency`: Actual uncached prompt plus completion usage (50% of Efficiency). <br>



## Evaluation Results: <br>
**Overall verdict: PASS — Recommended for publication**

**Publication Recommendation:** Recommended for publication based on the completed evaluation evidence in this report.

### Results at a Glance

| Measure | Claude Code (Baseline → Skill Uplift) | Codex (Baseline → Skill Uplift) |
|---|---:|---:|
| Overall | 89.3% — baseline ran, but no comparable score was available; uplift unavailable | 82.9% — baseline ran, but no comparable score was available; uplift unavailable |
| Security | 88.9% → 100.0% (+11.1 points) | 77.8% → 88.9% (+11.1 points) |
| Correctness | 71.1% → 82.2% (+11.1 points) | 68.9% → 86.7% (+17.8 points) |
| Discoverability | 98.8% — baseline ran, but no comparable score was available; uplift unavailable | 92.5% — baseline ran, but no comparable score was available; uplift unavailable |
| Effectiveness | 63.9% → 72.2% (+8.3 points) | 67.6% → 77.8% (+10.2 points) |
| Efficiency | 93.4% — baseline ran, but no comparable score was available; uplift unavailable | 68.9% — baseline ran, but no comparable score was available; uplift unavailable |

**How to read this table:** baseline is the same task attempted without the target skill. Scores are rounded to one decimal; threshold-adjacent values use additional precision so their displayed band matches the verdict. Uplift is derived from those displayed scores and shown in percentage points.

A partial dimension was calculated from only the available configured signals; review the detailed report before relying on it.

### Comparison details

Shared-source comparisons use the same signals and weights on both conditions. They do not replace the full dimension scores above or change the publication verdict.

| Agent | Dimension | Basis | Baseline → With skill (uplift) | Explanation |
| --- | --- | --- | --- | --- |
| claude-code | Discoverability | Dimension comparison | N/A | Discoverability is not applicable to the no-skill baseline; there is no installed skill to discover. |
| claude-code | Efficiency | Token-only comparison | 96.4% → 95.2% (-1.2 points) | Only Token Efficiency is comparable; the full dimension scores use different evaluator sources. |
| codex | Discoverability | Dimension comparison | N/A | Discoverability is not applicable to the no-skill baseline; there is no installed skill to discover. |
| codex | Efficiency | Token-only comparison | 89.4% → 89.4% (±0.0 points) | Only Token Efficiency is comparable; the full dimension scores use different evaluator sources. |

## Skill Version(s): <br>
f1758c4 (source: git SHA, committed 2026-11-09) <br>

## Ethical Considerations: <br>
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their internal team to ensure this skill meets requirements for the relevant industry and use case and addresses unforeseen product misuse. <br>

(For Release on NVIDIA Platforms Only) <br>
Please report quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://app.intigriti.com/programs/nvidia/nvidiavdp/detail). <br>
