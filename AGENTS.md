# AGENTS.md — instructions for collaborators and their coding agents

This file is the contract for anyone (human or AI coding agent — Claude Code,
Codex, Cursor, etc.) contributing to **academic-skills-food-nutrition**. Read it
fully before making changes. It is written to be machine-actionable: follow the
rules literally.

## What this project is
A Claude Code / Codex **skill suite** for food & nutrition science research:
multi-subagent skills (`food-research`, `deep-research`, `food-paper`,
`food-review`, `food-pipeline`, `food-figure`), a `journal-selector`, and
publisher-tiered journal author-guideline skills under `journals/`. MIT-licensed,
original work.

## GOLDEN RULE — branching
**Never push to `main`.** `main` is protected and release-only.

1. Do all work on the **`development`** branch (or a feature branch off it).
2. Push your commits to `development` (or your feature branch).
3. Open a **pull request** on GitHub to merge `development` → `main`.
4. `main` changes **only** through a reviewed, merged pull request.

```bash
git checkout development
git pull origin development
# … make changes …
git add -A && git commit -m "…"
git push origin development
gh pr create --base main --head development --title "…" --body "…"
```

Do not merge your own PR without review unless you are the maintainer and the
checks below pass.

## ALWAYS keep docs current (required in the same change)
Every change that adds/removes/renames a skill, subagent, reference, or command,
or changes behavior, MUST in the same PR:
- Update **`README.md`** to reflect the new state.
- Add a dated entry to **`CHANGELOG.md`** (newest on top) describing the change.
- Bump the `version` in **both** `.claude-plugin/plugin.json` and
  `.claude-plugin/marketplace.json` (semver: patch = fix, minor = new capability,
  major = breaking).

A PR that changes skills but not README/CHANGELOG will be rejected.

## Verification — run before opening a PR (all must pass)
```bash
# 1. Journal coverage maps resolve (food 60, nutrition list)
python3 scripts/check_journal_coverage.py

# 2. food-figure scripts self-test
python3 food-figure/scripts/analyze_data.py --selftest
python3 food-figure/scripts/backend_pref.py --selftest

# 3. Manifests are valid JSON (and, if you have Claude Code, validate the plugin)
python3 -c "import json;[json.load(open(p)) for p in ['.claude-plugin/plugin.json','.claude-plugin/marketplace.json']];print('json ok')"
claude plugin validate .    # optional, if claude CLI is installed

# 4. Every SKILL.md 'name' matches its folder; every frontmatter reference resolves
#    (see the checks in the PR template / repo scripts)

# 5. English only — no CJK or other non-Latin scripts in tracked files
```

## Content rules
- **Original text only.** This project is MIT. Do NOT copy text from CC-BY-NC or
  other non-permissive sources (e.g. the upstream `academic-research-skills`).
  Workflow *ideas* are fine; the wording must be your own. Permissive sources
  (MIT/Apache-2.0) may be drawn on with acknowledgement in the README.
- **English only — all project files.** Every file in the repository (skills,
  subagents, references, docs, scripts and their comments, manifests) must be in
  English, including all `description` and trigger text. If you create a file in
  another language, you MUST also create an English version and make the
  **English copy the main/canonical document**; the non-English file is a
  secondary translation, named with a language suffix (e.g. `SKILL.zh.md`,
  `README.zh-CN.md`) and never the primary. Reviewers will reject a PR whose
  primary document is not in English.
- **Food & nutrition specific.** Keep domain conventions correct (units as SI,
  g/100 g with basis, log CFU/g, biological vs analytical n, validated methods,
  ethics/food-safety).

## Structure conventions
- A skill is a folder containing `SKILL.md` whose frontmatter `name` **equals the
  folder name**. Subagents go in `<skill>/agents/*.md`; references in
  `<skill>/references/*.md`; the frontmatter lists them.
- New top-level skills and new `journals/<name>` skills must be registered in
  `.claude-plugin/marketplace.json` (`skills` array).
- New journals: add a row to `journals/_coverage.md` (food) or
  `journals/_coverage_nutrition.md` (nutrition), mapping to a publisher-format
  skill folder; keep `journals/references/journal-priority.csv` consistent.
- Cross-skill references use repo-root-relative paths (e.g. a skill may point to
  `food-paper/references/apa7-quickref.md`); keep the whole repo together.

## Commit & PR conventions
- Small, focused commits; imperative subject lines.
- PR description: what changed, why, and the verification output.
- Link the issue if one exists.

## Where to look
- Skill catalog and install: `README.md`.
- Change history: `CHANGELOG.md`.
- License: `LICENSE` (MIT).
- Acknowledgements / provenance: `README.md` (Acknowledgements) and `NOTICE`/attribution.
