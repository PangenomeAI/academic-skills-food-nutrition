---
name: deep-research
description: "General-purpose deep research on any question: decompose it, investigate iteratively across many sources, verify the key claims, synthesize, stress-test, and deliver a sourced report. Use standalone for any complex or open-ended question, or as the deep-dive engine called by food-research for a subtopic. Runs a subagent team (scoper, planner, investigator, verifier, synthesizer, critic) with an iterate-until-saturated loop. Triggers: deep research, research this in depth, investigate, look into this thoroughly, comprehensive answer, what's the state of, give me a briefing on, dig into, deep dive."
metadata:
  version: "1.0.0"
  verified: "2026-07"
  related_skills: [food-research, food-paper, food-pipeline]
  subagents: [question_scoper, research_planner, investigator, verifier, synthesizer, critic]
---

# Deep-Research — General Iterative Research Engine

Answer hard, open-ended questions properly: break the question down, investigate
across sources, check the load-bearing claims, and write a report that shows its
work. Original work; architecture informed by open community deep-research skills
(see the repo README Acknowledgements). Usable standalone on any topic, and
callable by `food-research` for a deep dive on a subtopic.

## Modes
- **quick brief** — one investigate→synthesize pass; best sources, direct answer, key uncertainties.
- **full** — the default: full subagent team with the iterate-until-saturated loop.

## Subagent team (dispatch via the Agent tool)
1. **`question_scoper`** — clarify intent, define scope and success criteria, decompose the question into sub-questions.
2. **`research_planner`** — turn sub-questions into an investigation plan: which source types answer each, in what order, and what "enough" looks like.
3. **`investigator`** — gather evidence per sub-question across sources; run in **parallel** across independent sub-questions.
4. **`verifier`** — independently check the load-bearing claims against primary sources; flag unsupported or shaky ones.
5. **`synthesizer`** — integrate findings into a coherent, sourced answer; resolve conflicts; state confidence.
6. **`critic`** — devil's advocate: attack the conclusions, surface bias, missing angles, and overreach; send gaps back for another loop.

## Workflow (iterate)
1. **Scope** (`question_scoper`) → confirm the question, scope, and sub-questions with the user (one consolidated clarifying question if anything is ambiguous).
2. **Plan** (`research_planner`) → map sub-questions to source types and set stopping criteria.
3. **Investigate** (`investigator`, parallel) → collect evidence with provenance for every claim. Sources span the open web, literature, official data/statistics, and primary documents — pick what fits the question. Use connected MCP tools (literature, data) when available; web search otherwise.
4. **Verify** (`verifier`) → check the claims the answer depends on; downgrade or drop the unsupported.
5. **Synthesize** (`synthesizer`) → draft the answer with inline citations and explicit confidence.
6. **Critique** (`critic`) → challenge it. If it finds real gaps or weak spots, **loop back** to step 3 for those sub-questions (cap ~2–3 loops).
7. **Report** → deliver: direct answer up front, then reasoning by sub-question, evidence with sources, open questions, and a confidence statement.

## Stopping rule
Stop looping when new investigation stops changing the conclusions and the
critic raises no new material gap — or the loop cap is reached (state residual
uncertainty rather than padding).

## Principles
- **Every claim carries a source.** No source, no claim — or mark it explicitly as inference.
- **Separate fact from interpretation.** Say which is which.
- **Show disagreement.** Where sources conflict, present the conflict and weigh it; don't average it into false consensus.
- **Surface uncertainty.** A calibrated "we don't know, because…" beats false confidence.

## Handoff
When invoked by `food-research`, return the sourced synthesis for a subtopic so
it can fold into the evidence brief. Standalone, deliver the report directly.
