# Skill Benchmark: newton-usage

> ✅ **Overall verdict: PASS — Recommended for publication**

## Publication Recommendation

Recommended for publication based on the completed evaluation evidence in this report.

## Evaluation Metadata

- Skill: `newton-usage`
- Validation status: `passed`
- Evaluation date: 2026-11-27
- Evaluator version: `1.6.10`
- Agents: Claude Code (`aws/anthropic/bedrock-claude-opus-5-5`), Codex (`openai/openai/gpt-6.1-sol`)
- Tasks: 11 evaluation tasks (9 positive, 2 negative)
- Dataset digest: `sha256:f31e6fb6c33a9af3b5d985a99024365051c66767aca55f6d1a179b17c743a926` (skill-evaluator-dataset-snapshot/1)
- Attempts per task: 1
- Environment: `k8s-sandbox`
- Tier 2 evidence: required for publication
- Tier 3 evidence: required for publication

Each task attempt ran in its own isolated sandbox pod.

## Tier 1 LLM Provenance

SkillSpector provider, model, analyzer revision, and determinism evidence retained for this scan.

| Skill | Provider | Adapter | Analyzer | Model | Revision | Determinism |
| --- | --- | --- | --- | --- | --- | --- |
| newton-usage | nv_inference | openai | mcp_tool_poisoning | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.5` | nondeterministic / provider_defaults |
| newton-usage | nv_inference | openai | semantic_developer_intent | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.5` | nondeterministic / provider_defaults |
| newton-usage | nv_inference | openai | semantic_quality_policy | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.5` | nondeterministic / provider_defaults |
| newton-usage | nv_inference | openai | semantic_security_discovery | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.5` | nondeterministic / provider_defaults |
| newton-usage | nv_inference | openai | meta_analyzer | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.5` | nondeterministic / provider_defaults |

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
| Overall | 89.5% — baseline ran, but no comparable score was available; uplift unavailable | 86.3% — baseline ran, but no comparable score was available; uplift unavailable |
| Security | 100.0% → 100.0% (±0.0 points) | 77.3% → 90.9% (+13.6 points) |
| Correctness | 89.1% → 98.2% (+9.1 points) | 90.9% → 98.2% (+7.3 points) |
| Discoverability | 78.3% — baseline ran, but no comparable score was available; uplift unavailable | 82.8% — baseline ran, but no comparable score was available; uplift unavailable |
| Effectiveness | 69.3% → 82.6% (+13.3 points) | 84.1% → 79.5% (-4.6 points) |
| Efficiency | 88.2% — baseline ran, but no comparable score was available; uplift unavailable | 79.8% — baseline ran, but no comparable score was available; uplift unavailable |

**How to read this table:** baseline is the same task attempted without the target skill. Scores are rounded to one decimal; threshold-adjacent values use additional precision so their displayed band matches the verdict. Uplift is derived from those displayed scores and shown in percentage points.

Example: `47.0% → 92.0% (+45.0 points)` means the skill-assisted run scored 92.0%, 45.0 percentage points above its 47.0% no-skill baseline.

A partial dimension was calculated from only the available configured signals; review the detailed report before relying on it.

### Comparison details

Shared-source comparisons use the same signals and weights on both conditions. They do not replace the full dimension scores above or change the publication verdict.

| Agent | Dimension | Basis | Baseline → With skill (uplift) | Explanation |
| --- | --- | --- | --- | --- |
| claude-code | Discoverability | Dimension comparison | N/A | Discoverability is not applicable to the no-skill baseline; there is no installed skill to discover. |
| claude-code | Efficiency | Token-only comparison | 98.5% → 97.6% (-0.9 points) | Only Token Efficiency is comparable; the full dimension scores use different evaluator sources. |
| codex | Discoverability | Dimension comparison | N/A | Discoverability is not applicable to the no-skill baseline; there is no installed skill to discover. |
| codex | Efficiency | Token-only comparison | 91.3% → 91.2% (-0.1 points) | Only Token Efficiency is comparable; the full dimension scores use different evaluator sources. |

## Token Usage

Actual Tier 3 execution usage is reported for every observed agent/case pair and both conditions.

| Agent | Dataset case | With skill | Without skill | Delta | Change | Coverage |
|---|---|---:|---:|---:|---:|---|
| claude-code | All cases | 1,949,770 | 1,396,132 | +553,638 | +39.66% | skill 11/11; base 11/11 |
| claude-code | newton-usage-context-active-project-selection | 71,542 | 35,686 | +35,856 | +100.48% | skill 1/1; base 1/1 |
| claude-code | newton-usage-context-assets | 263,422 | 260,069 | +3,353 | +1.29% | skill 1/1; base 1/1 |
| claude-code | newton-usage-context-example-environment | 108,418 | 35,984 | +72,434 | +201.30% | skill 1/1; base 1/1 |
| claude-code | newton-usage-context-metadata-only | 142,256 | 141,342 | +914 | +0.65% | skill 1/1; base 1/1 |
| claude-code | newton-usage-context-preserve-project | 35,671 | 35,394 | +277 | +0.78% | skill 1/1; base 1/1 |
| claude-code | newton-usage-explicit-setup | 72,060 | 36,513 | +35,547 | +97.35% | skill 1/1; base 1/1 |
| claude-code | newton-usage-implicit-build | 596,677 | 347,381 | +249,296 | +71.76% | skill 1/1; base 1/1 |
| claude-code | newton-usage-implicit-debug | 184,459 | 181,388 | +3,071 | +1.69% | skill 1/1; base 1/1 |
| claude-code | newton-usage-implicit-discovery | 258,454 | 142,381 | +116,073 | +81.52% | skill 1/1; base 1/1 |
| claude-code | newton-usage-negative-contributor-ci | 181,354 | 144,458 | +36,896 | +25.54% | skill 1/1; base 1/1 |
| claude-code | newton-usage-negative-root-finding | 35,457 | 35,536 | -79 | -0.22% | skill 1/1; base 1/1 |
| codex | All cases | 603,294 | 452,177 | +151,117 | +33.42% | skill 11/11; base 11/11 |
| codex | newton-usage-context-active-project-selection | 27,217 | 13,348 | +13,869 | +103.90% | skill 1/1; base 1/1 |
| codex | newton-usage-context-assets | 130,446 | 107,101 | +23,345 | +21.80% | skill 1/1; base 1/1 |
| codex | newton-usage-context-example-environment | 27,460 | 17,837 | +9,623 | +53.95% | skill 1/1; base 1/1 |
| codex | newton-usage-context-metadata-only | 70,227 | 40,017 | +30,210 | +75.49% | skill 1/1; base 1/1 |
| codex | newton-usage-context-preserve-project | 13,381 | 13,393 | -12 | -0.09% | skill 1/1; base 1/1 |
| codex | newton-usage-explicit-setup | 31,555 | 26,236 | +5,319 | +20.27% | skill 1/1; base 1/1 |
| codex | newton-usage-implicit-build | 61,076 | 39,286 | +21,790 | +55.47% | skill 1/1; base 1/1 |
| codex | newton-usage-implicit-debug | 102,538 | 41,926 | +60,612 | +144.57% | skill 1/1; base 1/1 |
| codex | newton-usage-implicit-discovery | 65,623 | 83,240 | -17,617 | -21.16% | skill 1/1; base 1/1 |
| codex | newton-usage-negative-contributor-ci | 60,394 | 56,460 | +3,934 | +6.97% | skill 1/1; base 1/1 |
| codex | newton-usage-negative-root-finding | 13,377 | 13,333 | +44 | +0.33% | skill 1/1; base 1/1 |
| ALL AGENTS | Dataset aggregate | 2,553,064 | 1,848,309 | +704,755 | +38.13% | skill 22/22; base 22/22 |

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

- **MEDIUM** QUALITY/quality_correctness: SKILL_SPEC recommended field missing: 'metadata.tags' (`skills/newton-usage/SKILL.md`)
- **MEDIUM** SCHEMA/body_recommended_section: Missing recommended section: '## Instructions' (`skills/newton-usage/SKILL.md`)
- **MEDIUM** SCHEMA/body_recommended_section: Missing recommended section: '## Examples' (`skills/newton-usage/SKILL.md`)
- **LOW** QUALITY/quality_correctness: No examples provided (`skills/newton-usage/SKILL.md`)
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
