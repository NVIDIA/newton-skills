# Skill Benchmark: newton-usage

> ✅ **Overall verdict: PASS — Recommended for publication**

## Publication Recommendation

Recommended for publication based on the completed evaluation evidence in this report.

## Evaluation Metadata

- Skill: `newton-usage`
- Validation status: `passed`
- Evaluation date: 2026-11-09
- Evaluator version: `1.6.9`
- Agents: Claude Code (`aws/anthropic/bedrock-claude-opus-5-5`), Codex (`openai/openai/gpt-6.1-sol`)
- Tasks: 11 evaluation tasks (9 positive, 2 negative)
- Dataset digest: `sha256:dbc72a5a6d33d9bc3e226ef96c3c3654198f4ea0b811a92a50419b77fbd2a303` (skill-evaluator-dataset-snapshot/1)
- Attempts per task: 1
- Environment: `k8s-sandbox`
- Tier 2 evidence: required for publication
- Tier 3 evidence: required for publication

Each task attempt ran in its own isolated sandbox pod.

## Tier 1 LLM Provenance

SkillSpector provider, model, analyzer revision, and determinism evidence retained for this scan.

| Skill | Provider | Adapter | Analyzer | Model | Revision | Determinism |
| --- | --- | --- | --- | --- | --- | --- |
| newton-usage | nv_inference | openai | mcp_tool_poisoning | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.4` | nondeterministic / provider_defaults |
| newton-usage | nv_inference | openai | semantic_developer_intent | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.4` | nondeterministic / provider_defaults |
| newton-usage | nv_inference | openai | semantic_quality_policy | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.4` | nondeterministic / provider_defaults |
| newton-usage | nv_inference | openai | semantic_security_discovery | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.4` | nondeterministic / provider_defaults |
| newton-usage | nv_inference | openai | meta_analyzer | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.4` | nondeterministic / provider_defaults |

- Controls for `newton-usage`: temperature=not set (source=provider_default, forwarded=no); seed=not set (source=unset, forwarded=no); reasoning_effort=not set (source=provider_default, forwarded=no)

## What This Report Answers

The three-tier evaluation checks whether the skill:

- is safe to use;
- produces correct answers;
- is discovered and activated when needed;
- helps the agent complete the user's goal and expected workflow; and
- avoids wasted skill and tool usage.

## Results at a Glance

| Measure | Claude Code (Baseline → Skill Uplift) | Codex (Baseline → Skill Uplift) |
|---|---:|---:|
| Overall | 84.0% — baseline ran, but no comparable score was available; uplift unavailable | 80.7% — baseline ran, but no comparable score was available; uplift unavailable |
| Security | 100.0% → 100.0% (±0.0 points) | 90.9% → 90.9% (±0.0 points) |
| Correctness | 85.5% → 90.9% (+5.4 points) | 83.6% → 89.1% (+5.5 points) |
| Discoverability | 70.6% — baseline ran, but no comparable score was available; uplift unavailable | 71.1% — baseline ran, but no comparable score was available; uplift unavailable |
| Effectiveness | 70.7% → 73.5% (+2.8 points) | 70.9% → 73.5% (+2.6 points) |
| Efficiency | 85.3% — baseline ran, but no comparable score was available; uplift unavailable | 78.8% — baseline ran, but no comparable score was available; uplift unavailable |

**How to read this table:** baseline is the same task attempted without the target skill. Scores are rounded to one decimal; threshold-adjacent values use additional precision so their displayed band matches the verdict. Uplift is derived from those displayed scores and shown in percentage points.

Example: `47.0% → 92.0% (+45.0 points)` means the skill-assisted run scored 92.0%, 45.0 percentage points above its 47.0% no-skill baseline.

A partial dimension was calculated from only the available configured signals; review the detailed report before relying on it.

### Comparison details

Shared-source comparisons use the same signals and weights on both conditions. They do not replace the full dimension scores above or change the publication verdict.

| Agent | Dimension | Basis | Baseline → With skill (uplift) | Explanation |
| --- | --- | --- | --- | --- |
| claude-code | Discoverability | Dimension comparison | N/A | Discoverability is not applicable to the no-skill baseline; there is no installed skill to discover. |
| claude-code | Efficiency | Token-only comparison | 98.5% → 97.9% (-0.6 points) | Only Token Efficiency is comparable; the full dimension scores use different evaluator sources. |
| codex | Discoverability | Dimension comparison | N/A | Discoverability is not applicable to the no-skill baseline; there is no installed skill to discover. |
| codex | Efficiency | Token-only comparison | 90.7% → 91.3% (+0.6 points) | Only Token Efficiency is comparable; the full dimension scores use different evaluator sources. |

## Token Usage

Actual Tier 3 execution usage is reported for every observed agent/case pair and both conditions.

| Agent | Dataset case | With skill | Without skill | Delta | Change | Coverage |
|---|---|---:|---:|---:|---:|---|
| claude-code | All cases | 1,251,002 | 1,149,570 | +101,432 | +8.82% | skill 11/11; base 11/11 |
| claude-code | newton-usage-context-active-project-selection | 35,614 | 35,383 | +231 | +0.65% | skill 1/1; base 1/1 |
| claude-code | newton-usage-context-assets | 187,137 | 144,727 | +42,410 | +29.30% | skill 1/1; base 1/1 |
| claude-code | newton-usage-context-example-environment | 73,529 | 36,102 | +37,427 | +103.67% | skill 1/1; base 1/1 |
| claude-code | newton-usage-context-metadata-only | 142,535 | 142,023 | +512 | +0.36% | skill 1/1; base 1/1 |
| claude-code | newton-usage-context-preserve-project | 35,735 | 35,512 | +223 | +0.63% | skill 1/1; base 1/1 |
| claude-code | newton-usage-explicit-setup | 72,632 | 36,111 | +36,521 | +101.14% | skill 1/1; base 1/1 |
| claude-code | newton-usage-implicit-build | 188,222 | 182,199 | +6,023 | +3.31% | skill 1/1; base 1/1 |
| claude-code | newton-usage-implicit-debug | 187,507 | 143,524 | +43,983 | +30.65% | skill 1/1; base 1/1 |
| claude-code | newton-usage-implicit-discovery | 147,860 | 178,953 | -31,093 | -17.37% | skill 1/1; base 1/1 |
| claude-code | newton-usage-negative-contributor-ci | 144,661 | 179,695 | -35,034 | -19.50% | skill 1/1; base 1/1 |
| claude-code | newton-usage-negative-root-finding | 35,570 | 35,341 | +229 | +0.65% | skill 1/1; base 1/1 |
| codex | All cases | 485,147 | 514,279 | -29,132 | -5.66% | skill 11/11; base 11/11 |
| codex | newton-usage-context-active-project-selection | 28,306 | 13,391 | +14,915 | +111.38% | skill 1/1; base 1/1 |
| codex | newton-usage-context-assets | 97,587 | 112,903 | -15,316 | -13.57% | skill 1/1; base 1/1 |
| codex | newton-usage-context-example-environment | 18,019 | 17,806 | +213 | +1.20% | skill 1/1; base 1/1 |
| codex | newton-usage-context-metadata-only | 40,328 | 54,020 | -13,692 | -25.35% | skill 1/1; base 1/1 |
| codex | newton-usage-context-preserve-project | 13,417 | 13,389 | +28 | +0.21% | skill 1/1; base 1/1 |
| codex | newton-usage-explicit-setup | 32,045 | 54,777 | -22,732 | -41.50% | skill 1/1; base 1/1 |
| codex | newton-usage-implicit-build | 55,111 | 47,965 | +7,146 | +14.90% | skill 1/1; base 1/1 |
| codex | newton-usage-implicit-debug | 43,180 | 55,599 | -12,419 | -22.34% | skill 1/1; base 1/1 |
| codex | newton-usage-implicit-discovery | 89,844 | 89,882 | -38 | -0.04% | skill 1/1; base 1/1 |
| codex | newton-usage-negative-contributor-ci | 53,919 | 41,200 | +12,719 | +30.87% | skill 1/1; base 1/1 |
| codex | newton-usage-negative-root-finding | 13,391 | 13,347 | +44 | +0.33% | skill 1/1; base 1/1 |
| ALL AGENTS | Dataset aggregate | 1,736,149 | 1,663,849 | +72,300 | +4.35% | skill 22/22; base 22/22 |

Prompt tokens include cached reads, so total tokens are `prompt + completion` (cached is not added twice). The Efficiency score uses `(prompt - cached) + completion`. Change is `100 * (with - without) / without`; negative means fewer tokens. N/A comparisons include their reason in the coverage column; coverage is never estimated.

## Tier Status

| Tier | Purpose | Status | Evidence |
|---|---|---|---|
| Tier 1 | Static validation | **PASSED WITH OBSERVATIONS** | 11 validator(s); 9 finding(s) |
| Tier 2 | Semantic deduplication | **PASSED** | 2 validator(s); 0 finding(s) |
| Tier 3 | Live agent evaluation | **PASS** | 2 agent(s); 11 task(s) |

## Findings and Observations

<details>
<summary>Show detailed findings and successful checks</summary>

- **MEDIUM** SCHEMA/body_recommended_section: Missing recommended section: '## Instructions' (`skills/newton-usage/SKILL.md`)
- **MEDIUM** SCHEMA/body_recommended_section: Missing recommended section: '## Examples' (`skills/newton-usage/SKILL.md`)
- **LOW** QUALITY/quality_correctness: No examples provided (`skills/newton-usage/SKILL.md`)
- **LOW** QUALITY/quality_discoverability: Description very long (236 chars, recommend 50-150) (`skills/newton-usage/SKILL.md`)
- **LOW** QUALITY/quality_discoverability: No '## Purpose' section (`skills/newton-usage/SKILL.md`)
- 4 additional finding(s) are available in the full evaluation artifacts.

</details>

## Scoring Methodology

<details>
<summary>Show dimension definitions, source signals, and thresholds</summary>

| Dimension | Question | Scored signals |
|---|---|---|
| Security | Is it safe to use? | `security` (100%) |
| Correctness | Is the answer correct? | `accuracy` (100%) |
| Discoverability | Was the right skill loaded when needed? | `skill_execution` (100%) |
| Effectiveness | Did the skill help complete the task? | `goal_accuracy` (50%) + `behavior_check` (50%) |
| Efficiency | Did it avoid wasted tool calls and token usage? | `skill_efficiency` (50%) + `token_efficiency` (50%) |

- Dimension bands: PASS at 50% or above; NEUTRAL from 40% to below 50%; FAIL below 40%.
- Overall Tier 3 lift: PASS at +5 points or more; FAIL at -10 points or less; values between those bands are NEUTRAL.
- Overall verdict: PASS only when every configured dimension passes for at least one supported agent. Lift is reported as diagnostic evidence and does not override this gate.
- The 50% attempt pass threshold is a separate per-task gate; it is not the dimension pass threshold.
- Effectiveness is the equal-weight mean of goal completion (`goal_accuracy`) and expected workflow adherence (`behavior_check`).
- Efficiency is 50% tool-call productivity (the backward-compatible `skill_efficiency` wire id) and 50% `token_efficiency`. Positive-case skill routing is scored under Discoverability, not Efficiency; a negative case without a routing target is N/A. N/A sources are omitted, remaining weights are renormalized, and the dimension is marked partial.

Signals present in this run:

- `security` (Security): unsafe operations, secret leakage, and unauthorized access.
- `skill_execution` (Skill Execution): whether the expected skill was selected, decoys were avoided, and the workflow executed.
- `skill_efficiency` (Tool Productivity): tool-call productivity (legacy wire id; routing is scored under Discoverability).
- `accuracy` (Accuracy): final-answer correctness against the reference answer.
- `goal_accuracy` (Goal Accuracy): whether the user's goal was achieved.
- `behavior_check` (Behavior Check): whether the expected workflow behavior was followed.
- `token_efficiency` (Token Efficiency): actual uncached prompt plus completion usage (50% of Efficiency).

</details>

## Freshness

Regenerate this benchmark when the skill, evaluation dataset, target agent/model, evaluator version, environment, or scoring policy changes.
