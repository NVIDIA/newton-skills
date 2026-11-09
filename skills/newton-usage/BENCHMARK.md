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
- Tasks: 9 evaluation tasks (7 positive, 2 negative)
- Dataset digest: `sha256:a8c03739c3a93435277e680e65ecd87fc3f0cf326fd4450bee8271908dcc200b` (skill-evaluator-dataset-snapshot/1)
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
| Overall | 85.4% — baseline ran, but no comparable score was available; uplift unavailable | 78.5% — baseline ran, but no comparable score was available; uplift unavailable |
| Security | 100.0% → 100.0% (±0.0 points) | 88.9% → 88.9% (±0.0 points) |
| Correctness | 84.4% → 88.9% (+4.5 points) | 82.2% → 88.9% (+6.7 points) |
| Discoverability | 87.1% — baseline ran, but no comparable score was available; uplift unavailable | 77.1% — baseline ran, but no comparable score was available; uplift unavailable |
| Effectiveness | 56.1% → 66.7% (+10.6 points) | 63.1% → 62.5% (-0.6 points) |
| Efficiency | 84.2% — baseline ran, but no comparable score was available; uplift unavailable | 74.9% — baseline ran, but no comparable score was available; uplift unavailable |

**How to read this table:** baseline is the same task attempted without the target skill. Scores are rounded to one decimal; threshold-adjacent values use additional precision so their displayed band matches the verdict. Uplift is derived from those displayed scores and shown in percentage points.

Example: `47.0% → 92.0% (+45.0 points)` means the skill-assisted run scored 92.0%, 45.0 percentage points above its 47.0% no-skill baseline.

A partial dimension was calculated from only the available configured signals; review the detailed report before relying on it.

### Comparison details

Shared-source comparisons use the same signals and weights on both conditions. They do not replace the full dimension scores above or change the publication verdict.

| Agent | Dimension | Basis | Baseline → With skill (uplift) | Explanation |
| --- | --- | --- | --- | --- |
| claude-code | Discoverability | Dimension comparison | N/A | Discoverability is not applicable to the no-skill baseline; there is no installed skill to discover. |
| claude-code | Efficiency | Token-only comparison | 96.7% → 97.5% (+0.8 points) | Only Token Efficiency is comparable; the full dimension scores use different evaluator sources. |
| codex | Discoverability | Dimension comparison | N/A | Discoverability is not applicable to the no-skill baseline; there is no installed skill to discover. |
| codex | Efficiency | Token-only comparison | 90.6% → 90.9% (+0.3 points) | Only Token Efficiency is comparable; the full dimension scores use different evaluator sources. |

## Token Usage

Actual Tier 3 execution usage is reported for every observed agent/case pair and both conditions.

| Agent | Dataset case | With skill | Without skill | Delta | Change | Coverage |
|---|---|---:|---:|---:|---:|---|
| claude-code | All cases | 1,337,731 | 1,605,583 | -267,852 | -16.68% | skill 9/9; base 9/9 |
| claude-code | newton-usage-context-assets | 187,116 | 144,799 | +42,317 | +29.22% | skill 1/1; base 1/1 |
| claude-code | newton-usage-context-metadata-only | 142,477 | 142,082 | +395 | +0.28% | skill 1/1; base 1/1 |
| claude-code | newton-usage-context-preserve-project | 72,696 | 35,437 | +37,259 | +105.14% | skill 1/1; base 1/1 |
| claude-code | newton-usage-explicit-setup | 72,534 | 35,710 | +36,824 | +103.12% | skill 1/1; base 1/1 |
| claude-code | newton-usage-implicit-build | 345,934 | 782,357 | -436,423 | -55.78% | skill 1/1; base 1/1 |
| claude-code | newton-usage-implicit-debug | 186,793 | 143,677 | +43,116 | +30.01% | skill 1/1; base 1/1 |
| claude-code | newton-usage-implicit-discovery | 147,615 | 142,999 | +4,616 | +3.23% | skill 1/1; base 1/1 |
| claude-code | newton-usage-negative-contributor-ci | 147,037 | 143,166 | +3,871 | +2.70% | skill 1/1; base 1/1 |
| claude-code | newton-usage-negative-root-finding | 35,529 | 35,356 | +173 | +0.49% | skill 1/1; base 1/1 |
| codex | All cases | 529,395 | 561,611 | -32,216 | -5.74% | skill 9/9; base 9/9 |
| codex | newton-usage-context-assets | 111,863 | 204,346 | -92,483 | -45.26% | skill 1/1; base 1/1 |
| codex | newton-usage-context-metadata-only | 54,301 | 53,952 | +349 | +0.65% | skill 1/1; base 1/1 |
| codex | newton-usage-context-preserve-project | 18,026 | 13,430 | +4,596 | +34.22% | skill 1/1; base 1/1 |
| codex | newton-usage-explicit-setup | 31,863 | 54,155 | -22,292 | -41.16% | skill 1/1; base 1/1 |
| codex | newton-usage-implicit-build | 53,927 | 38,611 | +15,316 | +39.67% | skill 1/1; base 1/1 |
| codex | newton-usage-implicit-debug | 57,861 | 41,074 | +16,787 | +40.87% | skill 1/1; base 1/1 |
| codex | newton-usage-implicit-discovery | 87,758 | 85,300 | +2,458 | +2.88% | skill 1/1; base 1/1 |
| codex | newton-usage-negative-contributor-ci | 100,397 | 57,418 | +42,979 | +74.85% | skill 1/1; base 1/1 |
| codex | newton-usage-negative-root-finding | 13,399 | 13,325 | +74 | +0.56% | skill 1/1; base 1/1 |
| ALL AGENTS | Dataset aggregate | 1,867,126 | 2,167,194 | -300,068 | -13.85% | skill 18/18; base 18/18 |

Prompt tokens include cached reads, so total tokens are `prompt + completion` (cached is not added twice). The Efficiency score uses `(prompt - cached) + completion`. Change is `100 * (with - without) / without`; negative means fewer tokens. N/A comparisons include their reason in the coverage column; coverage is never estimated.

## Tier Status

| Tier | Purpose | Status | Evidence |
|---|---|---|---|
| Tier 1 | Static validation | **PASSED WITH OBSERVATIONS** | 11 validator(s); 9 finding(s) |
| Tier 2 | Semantic deduplication | **PASSED** | 2 validator(s); 0 finding(s) |
| Tier 3 | Live agent evaluation | **PASS** | 2 agent(s); 9 task(s) |

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
