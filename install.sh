#!/usr/bin/env bash
# One-command installer for academic-skills-food-nutrition.
#
# Claude Code: installed as a plugin (the whole repo is the plugin).
# Codex & MiniMax Agent (Mavis): each skill is installed FLAT into the agent's
#   skills directory (…/skills/<name>/SKILL.md) so the agent discovers it, PLUS
#   the shared `journals/` and `scripts/` directories so cross-skill references
#   (e.g. journal-selector -> journals/…, scripts/verify_citations.py) resolve.
#
#   ./install.sh            # all (auto-detects what's installed)
#   ./install.sh claude     # Claude Code only
#   ./install.sh codex      # Codex only
#   ./install.sh minimax    # MiniMax Agent / Mavis only  (alias: mavis)
#
# Remote one-liner:
#   curl -fsSL https://raw.githubusercontent.com/PangenomeAI/academic-skills-food-nutrition/main/install.sh | bash
set -euo pipefail

REPO_URL="https://github.com/PangenomeAI/academic-skills-food-nutrition"
REPO_SLUG="PangenomeAI/academic-skills-food-nutrition"
PLUGIN="academic-skills-food-nutrition"
MARKET="academic-skills-food-nutrition"
TARGET="${1:-all}"

# Top-level skills (each holds a SKILL.md) + shared dirs the skills reference.
SKILLS="food-deep-research food-research food-paper food-pipeline food-review food-figure journal-selector"
SHARED="journals scripts"

# Locate the source: this checkout if run from inside the repo, else clone it.
if SELF="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" 2>/dev/null && pwd)" \
   && [ -f "$SELF/.claude-plugin/marketplace.json" ]; then
  SRC="$SELF"; CLONED=0
else
  SRC="$(mktemp -d)/$PLUGIN"
  echo "Cloning $REPO_URL …"
  git clone --depth 1 "$REPO_URL" "$SRC"
  CLONED=1
fi

# Install each skill flat into <dir>/<name>/, plus shared journals/ and scripts/,
# so agents that discover skills one level deep pick up every SKILL.md and the
# cross-skill paths (food-paper/references/…, journals/…, scripts/…) resolve.
install_bundle() {
  local dir="$1"
  mkdir -p "$dir"
  for d in $SKILLS $SHARED; do
    rm -rf "$dir/$d"
    cp -R "$SRC/$d" "$dir/$d"
  done
  echo "  ✔ Installed 7 skills (+ journals/, scripts/) into $dir/"
}

install_claude() {
  if command -v claude >/dev/null 2>&1; then
    echo "→ Claude Code: registering marketplace and installing plugin…"
    claude plugin marketplace add "$REPO_SLUG" 2>/dev/null \
      || claude plugin marketplace add "$SRC" 2>/dev/null \
      || claude plugin marketplace update "$MARKET" 2>/dev/null || true
    claude plugin install "${PLUGIN}@${MARKET}"
    echo "  ✔ Installed. Restart Claude Code (or run /plugin) to load the skills."
  else
    echo "→ Claude Code: 'claude' CLI not found — skipping."
    echo "    claude plugin marketplace add $REPO_SLUG"
    echo "    claude plugin install ${PLUGIN}@${MARKET}"
  fi
}

install_codex() {
  local dir="${CODEX_HOME:-$HOME/.codex}/skills"
  echo "→ Codex: installing skills to $dir"
  install_bundle "$dir"
  echo "    Restart Codex to discover the skills. (Override the dir with CODEX_HOME.)"
}

install_minimax() {
  # MiniMax Agent / Mavis Code reads SKILL.md skills from ~/.mavis/skills (global).
  local dir="${MAVIS_SKILLS_DIR:-$HOME/.mavis/skills}"
  echo "→ MiniMax Agent (Mavis): installing skills to $dir"
  install_bundle "$dir"
  echo "    Restart MiniMax Agent to load the skills. (Override with MAVIS_SKILLS_DIR,"
  echo "    or add via the in-app Skill Creator/import at https://agent.minimax.io/.)"
}

case "$TARGET" in
  claude)        install_claude ;;
  codex)         install_codex ;;
  minimax|mavis) install_minimax ;;
  all|both|"")
    install_claude
    if command -v codex >/dev/null 2>&1 || [ -d "${CODEX_HOME:-$HOME/.codex}" ]; then
      install_codex
    else
      echo "→ Codex: not detected (no 'codex' CLI or ~/.codex) — skipping. Later: ./install.sh codex"
    fi
    if [ -d "${MAVIS_SKILLS_DIR:-$HOME/.mavis}" ] || [ -n "${MAVIS_SKILLS_DIR:-}" ]; then
      install_minimax
    else
      echo "→ MiniMax Agent (Mavis): not detected (no ~/.mavis) — skipping. Later: ./install.sh minimax"
    fi
    ;;
  *) echo "Usage: $0 [claude|codex|minimax|all]"; exit 2 ;;
esac

[ "${CLONED:-0}" = 1 ] && echo "(source cloned to $SRC)"
echo "Done."
