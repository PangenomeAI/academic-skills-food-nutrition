#!/usr/bin/env bash
# One-command installer for academic-skills-food-nutrition.
# Installs the skills as a plugin in Claude Code, and as a skills bundle in Codex
# and MiniMax Agent.
#
#   ./install.sh                # install for all (auto-detects what's present)
#   ./install.sh claude         # Claude Code only
#   ./install.sh codex          # Codex only
#   ./install.sh minimax        # MiniMax Agent only
#
# Remote one-liner:
#   curl -fsSL https://raw.githubusercontent.com/PangenomeAI/academic-skills-food-nutrition/main/install.sh | bash
set -euo pipefail

REPO_URL="https://github.com/PangenomeAI/academic-skills-food-nutrition"
REPO_SLUG="PangenomeAI/academic-skills-food-nutrition"
PLUGIN="academic-skills-food-nutrition"
MARKET="academic-skills-food-nutrition"
TARGET="${1:-both}"

# Locate the source: use this checkout if the script runs from inside the repo,
# otherwise clone it (e.g. when piped via curl).
if SELF="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" 2>/dev/null && pwd)" \
   && [ -f "$SELF/.claude-plugin/marketplace.json" ]; then
  SRC="$SELF"; CLONED=0
else
  SRC="$(mktemp -d)/$PLUGIN"
  echo "Cloning $REPO_URL …"
  git clone --depth 1 "$REPO_URL" "$SRC"
  CLONED=1
fi

install_claude() {
  if command -v claude >/dev/null 2>&1; then
    echo "→ Claude Code: registering marketplace and installing plugin…"
    # Prefer the GitHub slug so the plugin stays updatable; fall back to local path.
    claude plugin marketplace add "$REPO_SLUG" 2>/dev/null \
      || claude plugin marketplace add "$SRC" 2>/dev/null \
      || claude plugin marketplace update "$MARKET" 2>/dev/null || true
    claude plugin install "${PLUGIN}@${MARKET}"
    echo "  ✔ Installed. Restart Claude Code (or run /plugin) to load the skills."
  else
    echo "→ Claude Code: 'claude' CLI not found — skipping."
    echo "  Install Claude Code (https://claude.ai/code), then run:"
    echo "    claude plugin marketplace add $REPO_SLUG"
    echo "    claude plugin install ${PLUGIN}@${MARKET}"
  fi
}

install_codex() {
  local dir="${CODEX_HOME:-$HOME/.codex}/skills/$PLUGIN"
  echo "→ Codex: installing skills bundle to $dir"
  mkdir -p "$(dirname "$dir")"
  rm -rf "$dir"
  # Copy the whole repo so cross-skill references (journals/, shared references,
  # journal-priority.csv) resolve; strip VCS metadata.
  cp -R "$SRC" "$dir"
  rm -rf "$dir/.git"
  echo "  ✔ Copied. Codex discovers SKILL.md files under its skills directory."
  echo "    If your Codex build uses a different path, set CODEX_HOME or move the folder."
}

install_minimax() {
  # MiniMax Agent reads SKILL.md skills from the shared agents skills directory
  # (~/.agents/skills, per MiniMax's own docs). Override with MINIMAX_SKILLS_DIR.
  local base="${MINIMAX_SKILLS_DIR:-$HOME/.agents/skills}"
  local dir="$base/$PLUGIN"
  echo "→ MiniMax Agent: installing skills bundle to $dir"
  mkdir -p "$base"
  rm -rf "$dir"
  # Copy the whole repo so cross-skill references resolve; strip VCS metadata.
  cp -R "$SRC" "$dir"
  rm -rf "$dir/.git"
  echo "  ✔ Copied. Restart MiniMax Agent so it rescans local skills."
  echo "    If your build uses a different location, set MINIMAX_SKILLS_DIR, or add"
  echo "    the folder via the in-app Skill Creator/import at https://agent.minimax.io/."
}

case "$TARGET" in
  claude)  install_claude ;;
  codex)   install_codex ;;
  minimax) install_minimax ;;
  all|both|"")
    install_claude
    if command -v codex >/dev/null 2>&1 || [ -d "${CODEX_HOME:-$HOME/.codex}" ]; then
      install_codex
    else
      echo "→ Codex: not detected (no 'codex' CLI or ~/.codex) — skipping. Later: ./install.sh codex"
    fi
    if [ -d "${MINIMAX_SKILLS_DIR:-$HOME/.agents/skills}" ] || [ -n "${MINIMAX_SKILLS_DIR:-}" ]; then
      install_minimax
    else
      echo "→ MiniMax Agent: shared skills dir not found — skipping. Later: ./install.sh minimax"
    fi
    ;;
  *) echo "Usage: $0 [claude|codex|minimax|all]"; exit 2 ;;
esac

[ "${CLONED:-0}" = 1 ] && echo "(source cloned to $SRC)"
echo "Done."
