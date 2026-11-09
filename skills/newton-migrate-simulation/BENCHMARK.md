# Skill Benchmark: newton-migrate-simulation

> ✅ **Overall verdict: PASS — Recommended for publication**

## Publication Recommendation

Recommended for publication based on the completed evaluation evidence in this report.

## Evaluation Metadata

- Skill: `newton-migrate-simulation`
- Validation status: `passed`
- Evaluation date: 2026-11-09
- Evaluator version: `1.6.9`
- Agents: Claude Code (`aws/anthropic/bedrock-claude-opus-5-5`), Codex (`openai/openai/gpt-6.1-sol`)
- Tasks: 7 evaluation tasks (5 positive, 2 negative)
- Dataset digest: `sha256:6ef8e81cadf422973d1e5386ca49be8b2bf76aed8d177469ac76e5fa387256dd` (skill-evaluator-dataset-snapshot/1)
- Attempts per task: 1
- Environment: `k8s-sandbox`
- Tier 2 evidence: required for publication
- Tier 3 evidence: required for publication

Each task attempt ran in its own isolated sandbox pod.

## Tier 1 LLM Provenance

SkillSpector provider, model, analyzer revision, and determinism evidence retained for this scan.

| Skill | Provider | Adapter | Analyzer | Model | Revision | Determinism |
| --- | --- | --- | --- | --- | --- | --- |
| newton-migrate-simulation | nv_inference | openai | mcp_tool_poisoning | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.4` | nondeterministic / provider_defaults |
| newton-migrate-simulation | nv_inference | openai | semantic_developer_intent | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.4` | nondeterministic / provider_defaults |
| newton-migrate-simulation | nv_inference | openai | semantic_quality_policy | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.4` | nondeterministic / provider_defaults |
| newton-migrate-simulation | nv_inference | openai | semantic_security_discovery | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.4` | nondeterministic / provider_defaults |
| newton-migrate-simulation | nv_inference | openai | meta_analyzer | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.4` | nondeterministic / provider_defaults |

- Controls for `newton-migrate-simulation`: temperature=not set (source=provider_default, forwarded=no); seed=not set (source=unset, forwarded=no); reasoning_effort=not set (source=provider_default, forwarded=no)

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
| Overall | 97.9% — baseline ran, but no comparable score was available; uplift unavailable | 86.1% — baseline ran, but no comparable score was available; uplift unavailable |
| Security | 92.9% → 100.0% (+7.1 points) | 100.0% → 100.0% (±0.0 points) |
| Correctness | 97.1% → 100.0% (+2.9 points) | 97.1% → 94.3% (-2.8 points) |
| Discoverability | 100.0% — baseline ran, but no comparable score was available; uplift unavailable | 76.0% — baseline ran, but no comparable score was available; uplift unavailable |
| Effectiveness | 85.7% → 98.2% (+12.5 points) | 92.9% → 100.0% (+7.1 points) |
| Efficiency | 91.2% — baseline ran, but no comparable score was available; uplift unavailable | 60.2% — baseline ran, but no comparable score was available; uplift unavailable |

**How to read this table:** baseline is the same task attempted without the target skill. Scores are rounded to one decimal; threshold-adjacent values use additional precision so their displayed band matches the verdict. Uplift is derived from those displayed scores and shown in percentage points.

Example: `47.0% → 92.0% (+45.0 points)` means the skill-assisted run scored 92.0%, 45.0 percentage points above its 47.0% no-skill baseline.

A partial dimension was calculated from only the available configured signals; review the detailed report before relying on it.

### Comparison details

Shared-source comparisons use the same signals and weights on both conditions. They do not replace the full dimension scores above or change the publication verdict.

| Agent | Dimension | Basis | Baseline → With skill (uplift) | Explanation |
| --- | --- | --- | --- | --- |
| claude-code | Discoverability | Dimension comparison | N/A | Discoverability is not applicable to the no-skill baseline; there is no installed skill to discover. |
| claude-code | Efficiency | Token-only comparison | 96.2% → 97.4% (+1.2 points) | Only Token Efficiency is comparable; the full dimension scores use different evaluator sources. |
| codex | Discoverability | Dimension comparison | N/A | Discoverability is not applicable to the no-skill baseline; there is no installed skill to discover. |
| codex | Efficiency | Token-only comparison | 86.9% → 89.1% (+2.2 points) | Only Token Efficiency is comparable; the full dimension scores use different evaluator sources. |

## Token Usage

Actual Tier 3 execution usage is reported for every observed agent/case pair and both conditions.

| Agent | Dataset case | With skill | Without skill | Delta | Change | Coverage |
|---|---|---:|---:|---:|---:|---|
| claude-code | All cases | 663,954 | 846,059 | -182,105 | -21.52% | skill 7/7; base 7/7 |
| claude-code | newton-migrate-context-reuse-without-reference | 74,577 | 73,116 | +1,461 | +2.00% | skill 1/1; base 1/1 |
| claude-code | newton-migrate-context-target-before-install | 151,564 | 378,025 | -226,461 | -59.91% | skill 1/1; base 1/1 |
| claude-code | newton-migrate-context-target-mismatch | 73,518 | 70,695 | +2,823 | +3.99% | skill 1/1; base 1/1 |
| claude-code | newton-migrate-explicit-mujoco | 74,898 | 109,152 | -34,254 | -31.38% | skill 1/1; base 1/1 |
| claude-code | newton-migrate-implicit-controller | 74,531 | 37,225 | +37,306 | +100.22% | skill 1/1; base 1/1 |
| claude-code | newton-migrate-negative-data-schema | 107,740 | 107,019 | +721 | +0.67% | skill 1/1; base 1/1 |
| claude-code | newton-migrate-negative-other-target | 107,126 | 70,827 | +36,299 | +51.25% | skill 1/1; base 1/1 |
| codex | All cases | 257,539 | 312,195 | -54,656 | -17.51% | skill 7/7; base 7/7 |
| codex | newton-migrate-context-reuse-without-reference | 32,999 | 31,207 | +1,792 | +5.74% | skill 1/1; base 1/1 |
| codex | newton-migrate-context-target-before-install | 62,556 | 56,415 | +6,141 | +10.89% | skill 1/1; base 1/1 |
| codex | newton-migrate-context-target-mismatch | 13,693 | 13,410 | +283 | +2.11% | skill 1/1; base 1/1 |
| codex | newton-migrate-explicit-mujoco | 50,350 | 76,241 | -25,891 | -33.96% | skill 1/1; base 1/1 |
| codex | newton-migrate-implicit-controller | 41,113 | 38,936 | +2,177 | +5.59% | skill 1/1; base 1/1 |
| codex | newton-migrate-negative-data-schema | 13,389 | 40,804 | -27,415 | -67.19% | skill 1/1; base 1/1 |
| codex | newton-migrate-negative-other-target | 43,439 | 55,182 | -11,743 | -21.28% | skill 1/1; base 1/1 |
| ALL AGENTS | Dataset aggregate | 921,493 | 1,158,254 | -236,761 | -20.44% | skill 14/14; base 14/14 |

Prompt tokens include cached reads, so total tokens are `prompt + completion` (cached is not added twice). The Efficiency score uses `(prompt - cached) + completion`. Change is `100 * (with - without) / without`; negative means fewer tokens. N/A comparisons include their reason in the coverage column; coverage is never estimated.

## Tier Status

| Tier | Purpose | Status | Evidence |
|---|---|---|---|
| Tier 1 | Static validation | **PASSED WITH OBSERVATIONS** | 11 validator(s); 8 finding(s) |
| Tier 2 | Semantic deduplication | **PASSED** | 2 validator(s); 0 finding(s) |
| Tier 3 | Live agent evaluation | **PASS** | 2 agent(s); 7 task(s) |

## Findings and Observations

<details>
<summary>Show detailed findings and successful checks</summary>

- **MEDIUM** SCHEMA/body_recommended_section: Missing recommended section: '## Instructions' (`skills/newton-migrate-simulation/SKILL.md`)
- **MEDIUM** SCHEMA/body_recommended_section: Missing recommended section: '## Examples' (`skills/newton-migrate-simulation/SKILL.md`)
- **LOW** QUALITY/quality_correctness: No examples provided (`skills/newton-migrate-simulation/SKILL.md`)
- **LOW** QUALITY/quality_discoverability: No '## Purpose' section (`skills/newton-migrate-simulation/SKILL.md`)
- **LOW** QUALITY/quality_reliability: No prerequisites/requirements documented (`skills/newton-migrate-simulation/SKILL.md`)
- 3 additional finding(s) are available in the full evaluation artifacts.

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
