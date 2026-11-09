# Skill Benchmark: newton-debug-simulation

> ✅ **Overall verdict: PASS — Recommended for publication**

## Publication Recommendation

Recommended for publication based on the completed evaluation evidence in this report.

## Evaluation Metadata

- Skill: `newton-debug-simulation`
- Validation status: `passed`
- Evaluation date: 2026-11-09
- Evaluator version: `1.6.9`
- Agents: Claude Code (`aws/anthropic/bedrock-claude-opus-5-5`), Codex (`openai/openai/gpt-6.1-sol`)
- Tasks: 9 evaluation tasks (4 positive, 5 negative)
- Dataset digest: `sha256:1e4fcdd6db09f19d0f7335a9754719962f451819f2c8bc45d3e796e1b057120f` (skill-evaluator-dataset-snapshot/1)
- Attempts per task: 1
- Environment: `k8s-sandbox`
- Tier 2 evidence: required for publication
- Tier 3 evidence: required for publication

Each task attempt ran in its own isolated sandbox pod.

## Tier 1 LLM Provenance

SkillSpector provider, model, analyzer revision, and determinism evidence retained for this scan.

| Skill | Provider | Adapter | Analyzer | Model | Revision | Determinism |
| --- | --- | --- | --- | --- | --- | --- |
| newton-debug-simulation | nv_inference | openai | mcp_tool_poisoning | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.4` | nondeterministic / provider_defaults |
| newton-debug-simulation | nv_inference | openai | semantic_developer_intent | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.4` | nondeterministic / provider_defaults |
| newton-debug-simulation | nv_inference | openai | semantic_quality_policy | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.4` | nondeterministic / provider_defaults |
| newton-debug-simulation | nv_inference | openai | semantic_security_discovery | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.4` | nondeterministic / provider_defaults |
| newton-debug-simulation | nv_inference | openai | meta_analyzer | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.4` | nondeterministic / provider_defaults |

- Controls for `newton-debug-simulation`: temperature=not set (source=provider_default, forwarded=no); seed=not set (source=unset, forwarded=no); reasoning_effort=not set (source=provider_default, forwarded=no)

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
| Overall | 89.3% — baseline ran, but no comparable score was available; uplift unavailable | 82.9% — baseline ran, but no comparable score was available; uplift unavailable |
| Security | 88.9% → 100.0% (+11.1 points) | 77.8% → 88.9% (+11.1 points) |
| Correctness | 71.1% → 82.2% (+11.1 points) | 68.9% → 86.7% (+17.8 points) |
| Discoverability | 98.8% — baseline ran, but no comparable score was available; uplift unavailable | 92.5% — baseline ran, but no comparable score was available; uplift unavailable |
| Effectiveness | 63.9% → 72.2% (+8.3 points) | 67.6% → 77.8% (+10.2 points) |
| Efficiency | 93.4% — baseline ran, but no comparable score was available; uplift unavailable | 68.9% — baseline ran, but no comparable score was available; uplift unavailable |

**How to read this table:** baseline is the same task attempted without the target skill. Scores are rounded to one decimal; threshold-adjacent values use additional precision so their displayed band matches the verdict. Uplift is derived from those displayed scores and shown in percentage points.

Example: `47.0% → 92.0% (+45.0 points)` means the skill-assisted run scored 92.0%, 45.0 percentage points above its 47.0% no-skill baseline.

A partial dimension was calculated from only the available configured signals; review the detailed report before relying on it.

### Comparison details

Shared-source comparisons use the same signals and weights on both conditions. They do not replace the full dimension scores above or change the publication verdict.

| Agent | Dimension | Basis | Baseline → With skill (uplift) | Explanation |
| --- | --- | --- | --- | --- |
| claude-code | Discoverability | Dimension comparison | N/A | Discoverability is not applicable to the no-skill baseline; there is no installed skill to discover. |
| claude-code | Efficiency | Token-only comparison | 96.4% → 95.2% (-1.2 points) | Only Token Efficiency is comparable; the full dimension scores use different evaluator sources. |
| codex | Discoverability | Dimension comparison | N/A | Discoverability is not applicable to the no-skill baseline; there is no installed skill to discover. |
| codex | Efficiency | Token-only comparison | 89.4% → 89.4% (±0.0 points) | Only Token Efficiency is comparable; the full dimension scores use different evaluator sources. |

## Token Usage

Actual Tier 3 execution usage is reported for every observed agent/case pair and both conditions.

| Agent | Dataset case | With skill | Without skill | Delta | Change | Coverage |
|---|---|---:|---:|---:|---:|---|
| claude-code | All cases | 2,457,895 | 2,227,096 | +230,799 | +10.36% | skill 9/9; base 9/9 |
| claude-code | newton-debug-executable-contact | 186,071 | 220,951 | -34,880 | -15.79% | skill 1/1; base 1/1 |
| claude-code | newton-debug-executable-late-controller | 224,355 | 182,251 | +42,104 | +23.10% | skill 1/1; base 1/1 |
| claude-code | newton-debug-explicit-tunneling | 149,783 | 72,176 | +77,607 | +107.52% | skill 1/1; base 1/1 |
| claude-code | newton-debug-implicit-late-instability | 73,866 | 71,759 | +2,107 | +2.94% | skill 1/1; base 1/1 |
| claude-code | newton-debug-negative-construction | 1,238,810 | 998,442 | +240,368 | +24.07% | skill 1/1; base 1/1 |
| claude-code | newton-debug-negative-contributor-test | 144,591 | 178,024 | -33,433 | -18.78% | skill 1/1; base 1/1 |
| claude-code | newton-debug-negative-migration | 143,831 | 215,335 | -71,504 | -33.21% | skill 1/1; base 1/1 |
| claude-code | newton-debug-negative-profiling | 145,392 | 144,878 | +514 | +0.35% | skill 1/1; base 1/1 |
| claude-code | newton-debug-negative-validation | 151,196 | 143,280 | +7,916 | +5.52% | skill 1/1; base 1/1 |
| codex | All cases | 1,830,758 | 2,395,671 | -564,913 | -23.58% | skill 9/9; base 9/9 |
| codex | newton-debug-executable-contact | 89,682 | 88,725 | +957 | +1.08% | skill 1/1; base 1/1 |
| codex | newton-debug-executable-late-controller | 111,204 | 73,094 | +38,110 | +52.14% | skill 1/1; base 1/1 |
| codex | newton-debug-explicit-tunneling | 36,783 | 54,571 | -17,788 | -32.60% | skill 1/1; base 1/1 |
| codex | newton-debug-implicit-late-instability | 36,705 | 18,124 | +18,581 | +102.52% | skill 1/1; base 1/1 |
| codex | newton-debug-negative-construction | 1,361,846 | 1,970,575 | -608,729 | -30.89% | skill 1/1; base 1/1 |
| codex | newton-debug-negative-contributor-test | 55,587 | 54,552 | +1,035 | +1.90% | skill 1/1; base 1/1 |
| codex | newton-debug-negative-migration | 42,902 | 40,641 | +2,261 | +5.56% | skill 1/1; base 1/1 |
| codex | newton-debug-negative-profiling | 55,180 | 54,795 | +385 | +0.70% | skill 1/1; base 1/1 |
| codex | newton-debug-negative-validation | 40,869 | 40,594 | +275 | +0.68% | skill 1/1; base 1/1 |
| ALL AGENTS | Dataset aggregate | 4,288,653 | 4,622,767 | -334,114 | -7.23% | skill 18/18; base 18/18 |

Prompt tokens include cached reads, so total tokens are `prompt + completion` (cached is not added twice). The Efficiency score uses `(prompt - cached) + completion`. Change is `100 * (with - without) / without`; negative means fewer tokens. N/A comparisons include their reason in the coverage column; coverage is never estimated.

## Tier Status

| Tier | Purpose | Status | Evidence |
|---|---|---|---|
| Tier 1 | Static validation | **PASSED WITH OBSERVATIONS** | 11 validator(s); 8 finding(s) |
| Tier 2 | Semantic deduplication | **PASSED** | 2 validator(s); 0 finding(s) |
| Tier 3 | Live agent evaluation | **PASS** | 2 agent(s); 9 task(s) |

## Findings and Observations

<details>
<summary>Show detailed findings and successful checks</summary>

- **MEDIUM** SCHEMA/body_recommended_section: Missing recommended section: '## Instructions' (`skills/newton-debug-simulation/SKILL.md`)
- **MEDIUM** SCHEMA/body_recommended_section: Missing recommended section: '## Examples' (`skills/newton-debug-simulation/SKILL.md`)
- **LOW** QUALITY/quality_correctness: No examples provided (`skills/newton-debug-simulation/SKILL.md`)
- **LOW** QUALITY/quality_discoverability: No '## Purpose' section (`skills/newton-debug-simulation/SKILL.md`)
- **LOW** QUALITY/quality_reliability: No prerequisites/requirements documented (`skills/newton-debug-simulation/SKILL.md`)
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
