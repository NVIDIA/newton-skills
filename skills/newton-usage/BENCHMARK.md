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
- Tasks: 8 evaluation tasks (6 positive, 2 negative)
- Dataset digest: `sha256:18994fa6fd8f1ce31cb9947aa9ee87b34b5d6d975394275c2e9d3fe10d96bf9a` (skill-evaluator-dataset-snapshot/1)
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
| Overall | 87.1% — baseline ran, but no comparable score was available; uplift unavailable | 82.6% — baseline ran, but no comparable score was available; uplift unavailable |
| Security | 100.0% → 93.8% (-6.2 points) | 87.5% → 100.0% (+12.5 points) |
| Correctness | 82.5% → 92.5% (+10.0 points) | 80.0% → 92.5% (+12.5 points) |
| Discoverability | 87.5% — baseline ran, but no comparable score was available; uplift unavailable | 84.2% — baseline ran, but no comparable score was available; uplift unavailable |
| Effectiveness | 67.8% → 75.0% (+7.2 points) | 64.4% → 59.4% (-5.0 points) |
| Efficiency | 86.7% — baseline ran, but no comparable score was available; uplift unavailable | 76.9% — baseline ran, but no comparable score was available; uplift unavailable |

**How to read this table:** baseline is the same task attempted without the target skill. Scores are rounded to one decimal; threshold-adjacent values use additional precision so their displayed band matches the verdict. Uplift is derived from those displayed scores and shown in percentage points.

Example: `47.0% → 92.0% (+45.0 points)` means the skill-assisted run scored 92.0%, 45.0 percentage points above its 47.0% no-skill baseline.

A partial dimension was calculated from only the available configured signals; review the detailed report before relying on it.

### Comparison details

Shared-source comparisons use the same signals and weights on both conditions. They do not replace the full dimension scores above or change the publication verdict.

| Agent | Dimension | Basis | Baseline → With skill (uplift) | Explanation |
| --- | --- | --- | --- | --- |
| claude-code | Discoverability | Dimension comparison | N/A | Discoverability is not applicable to the no-skill baseline; there is no installed skill to discover. |
| claude-code | Efficiency | Token-only comparison | 98.2% → 96.4% (-1.8 points) | Only Token Efficiency is comparable; the full dimension scores use different evaluator sources. |
| codex | Discoverability | Dimension comparison | N/A | Discoverability is not applicable to the no-skill baseline; there is no installed skill to discover. |
| codex | Efficiency | Token-only comparison | 90.6% → 91.2% (+0.6 points) | Only Token Efficiency is comparable; the full dimension scores use different evaluator sources. |

## Token Usage

Actual Tier 3 execution usage is reported for every observed agent/case pair and both conditions.

| Agent | Dataset case | With skill | Without skill | Delta | Change | Coverage |
|---|---|---:|---:|---:|---:|---|
| claude-code | All cases | 1,662,031 | 975,287 | +686,744 | +70.41% | skill 8/8; base 8/8 |
| claude-code | newton-usage-context-assets | 224,800 | 184,723 | +40,077 | +21.70% | skill 1/1; base 1/1 |
| claude-code | newton-usage-context-metadata-only | 142,646 | 142,235 | +411 | +0.29% | skill 1/1; base 1/1 |
| claude-code | newton-usage-explicit-setup | 72,329 | 35,811 | +36,518 | +101.97% | skill 1/1; base 1/1 |
| claude-code | newton-usage-implicit-build | 747,728 | 183,074 | +564,654 | +308.43% | skill 1/1; base 1/1 |
| claude-code | newton-usage-implicit-debug | 185,615 | 143,583 | +42,032 | +29.27% | skill 1/1; base 1/1 |
| claude-code | newton-usage-implicit-discovery | 109,198 | 106,599 | +2,599 | +2.44% | skill 1/1; base 1/1 |
| claude-code | newton-usage-negative-contributor-ci | 144,128 | 143,725 | +403 | +0.28% | skill 1/1; base 1/1 |
| claude-code | newton-usage-negative-root-finding | 35,587 | 35,537 | +50 | +0.14% | skill 1/1; base 1/1 |
| codex | All cases | 457,324 | 502,965 | -45,641 | -9.07% | skill 8/8; base 8/8 |
| codex | newton-usage-context-assets | 109,743 | 155,284 | -45,541 | -29.33% | skill 1/1; base 1/1 |
| codex | newton-usage-context-metadata-only | 40,334 | 53,898 | -13,564 | -25.17% | skill 1/1; base 1/1 |
| codex | newton-usage-explicit-setup | 31,834 | 53,343 | -21,509 | -40.32% | skill 1/1; base 1/1 |
| codex | newton-usage-implicit-build | 54,072 | 51,953 | +2,119 | +4.08% | skill 1/1; base 1/1 |
| codex | newton-usage-implicit-debug | 72,467 | 54,865 | +17,602 | +32.08% | skill 1/1; base 1/1 |
| codex | newton-usage-implicit-discovery | 92,087 | 78,971 | +13,116 | +16.61% | skill 1/1; base 1/1 |
| codex | newton-usage-negative-contributor-ci | 43,382 | 41,324 | +2,058 | +4.98% | skill 1/1; base 1/1 |
| codex | newton-usage-negative-root-finding | 13,405 | 13,327 | +78 | +0.59% | skill 1/1; base 1/1 |
| ALL AGENTS | Dataset aggregate | 2,119,355 | 1,478,252 | +641,103 | +43.37% | skill 16/16; base 16/16 |

Prompt tokens include cached reads, so total tokens are `prompt + completion` (cached is not added twice). The Efficiency score uses `(prompt - cached) + completion`. Change is `100 * (with - without) / without`; negative means fewer tokens. N/A comparisons include their reason in the coverage column; coverage is never estimated.

## Tier Status

| Tier | Purpose | Status | Evidence |
|---|---|---|---|
| Tier 1 | Static validation | **PASSED WITH OBSERVATIONS** | 11 validator(s); 9 finding(s) |
| Tier 2 | Semantic deduplication | **PASSED** | 2 validator(s); 0 finding(s) |
| Tier 3 | Live agent evaluation | **PASS** | 2 agent(s); 8 task(s) |

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
