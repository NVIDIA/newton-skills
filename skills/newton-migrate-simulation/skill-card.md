## Description: <br>
Migrate existing simulator assets, controllers, or behavior to Newton with explicit convention, feature, and parity checks; not for a new scene with no source assets or simulator. <br>

This skill is ready for commercial/non-commercial use. <br>

## Owner
NVIDIA <br>

### License/Terms of Use: <br>
CC-BY-4.0 AND Apache 2.0 <br>
## Use Case: <br>
Developers and engineers use this skill to port the smallest representative scene from an existing simulator (for example, MuJoCo) to Newton 1.7.0, inventorying units, frames, assets, joints, drives, limits, contacts, and controller semantics, mapping only documented features, and comparing source and target behavior with fixed bounds before claiming parity. <br>

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
- [Newton documentation](https://newton-physics.github.io/newton/) <br>
- [Newton physics simulator (GitHub)](https://github.com/newton-physics/newton) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Code, Shell commands] <br>
**Output Format:** [Markdown with feature mappings, commands, and parity evidence] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports retained, remapped, unsupported, and intentionally changed features; warns and stops for Newton versions other than 1.7.0; leaves parity unverified without a source reference and does not claim real-world validation.] <br>

## Evaluation Agents Used: <br>
- Claude Code (`aws/anthropic/bedrock-claude-opus-4-8`) <br>
- Codex (`openai/openai/gpt-5.5`) <br>



## Evaluation Tasks: <br>
3 evaluation tasks (2 positive, 1 negative), 1 attempt per task, each run in an isolated `k8s-sandbox` pod; Tier 1 static validation passed with observations (11 validators, 7 findings), Tier 2 semantic deduplication passed (2 validators, 0 findings), and Tier 3 live agent evaluation passed (2 agents, 3 tasks). <br>

## Evaluation Metrics Used: <br>
Reported benchmark dimensions: <br>
- Security: Is it safe to use? Scored from the `security` signal. <br>
- Correctness: Is the answer correct? Scored from the `accuracy` signal. <br>
- Discoverability: Was the right skill loaded when needed? Scored from the `skill_execution` signal. <br>
- Effectiveness: Did the skill help complete the task? Equal-weight mean of `goal_accuracy` and `behavior_check`. <br>
- Efficiency: Did it avoid wasted tool calls and token usage? Equal-weight mean of `skill_efficiency` and `token_efficiency`. <br>

Underlying evaluation signals used in this run: <br>
- `security`: Unsafe operations, secret leakage, and unauthorized access. <br>
- `skill_execution`: Whether the expected skill was selected, decoys were avoided, and the workflow executed. <br>
- `skill_efficiency`: Tool-call productivity (legacy wire id; routing is scored under Discoverability). <br>
- `accuracy`: Final-answer correctness against the reference answer. <br>
- `goal_accuracy`: Whether the user's goal was achieved. <br>
- `behavior_check`: Whether the expected workflow behavior was followed. <br>
- `token_efficiency`: Actual uncached prompt plus completion usage (50% of Efficiency). <br>



## Evaluation Results: <br>
| Measure | Claude Code (Baseline → Skill Uplift) | Codex (Baseline → Skill Uplift) |
|---|---:|---:|
| Overall | 99.7% — baseline ran, but no comparable score was available; uplift unavailable | 97.9% — baseline ran, but no comparable score was available; uplift unavailable |
| Security | 100.0% → 100.0% (±0.0 points) | 100.0% → 100.0% (±0.0 points) |
| Correctness | 66.7% → 100.0% (+33.3 points) | 93.3% → 100.0% (+6.7 points) |
| Discoverability | 100.0% — baseline ran, but no comparable score was available; uplift unavailable | 95.0% — baseline ran, but no comparable score was available; uplift unavailable |
| Effectiveness | 75.0% → 100.0% (+25.0 points) | 87.5% → 95.8% (+8.3 points) |
| Efficiency | 98.5% — baseline ran, but no comparable score was available; uplift unavailable | 98.7% — baseline ran, but no comparable score was available; uplift unavailable |

## Skill Version(s): <br>
a47aa6b (source: git SHA, committed 2026-10-15) <br>

## Ethical Considerations: <br>
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their internal team to ensure this skill meets requirements for the relevant industry and use case and addresses unforeseen product misuse. <br>

(For Release on NVIDIA Platforms Only) <br>
Please report quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://app.intigriti.com/programs/nvidia/nvidiavdp/detail). <br>
