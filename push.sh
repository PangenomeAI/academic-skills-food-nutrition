#!/usr/bin/env bash
# Publish this repo to github.com/PangenomeAI/academic-skills-food-nutrition.
# Run from a shell authenticated as PangeZAU with push access to PangenomeAI.
set -euo pipefail

ORG="PangenomeAI"
REPO="academic-skills-food-nutrition"
REMOTE_URL="https://github.com/${ORG}/${REPO}.git"

cd "$(dirname "$0")"

# Ensure we have a commit to push.
if ! git rev-parse HEAD >/dev/null 2>&1; then
  echo "No commits found. Run: git add -A && git commit -m 'Initial commit' first." >&2
  exit 1
fi

git branch -M main

if command -v gh >/dev/null 2>&1; then
  echo "gh found — creating ${ORG}/${REPO} and pushing…"
  # Creates the repo under the org, sets 'origin', and pushes main.
  gh repo create "${ORG}/${REPO}" --public --source=. --remote=origin --push
  echo "Done: ${REMOTE_URL}"
else
  echo "gh (GitHub CLI) not installed. Manual steps:"
  echo "  1. Create an empty repo at https://github.com/organizations/${ORG}/repositories/new"
  echo "     name: ${REPO}  (do NOT initialize with README/license)"
  echo "  2. Then run:"
  echo "     git remote add origin ${REMOTE_URL}"
  echo "     git push -u origin main"
  echo ""
  echo "Attempting to add the remote for you (edit if it already exists)…"
  git remote add origin "${REMOTE_URL}" 2>/dev/null || git remote set-url origin "${REMOTE_URL}"
  echo "Remote 'origin' set to ${REMOTE_URL}. After creating the repo on GitHub, run:"
  echo "     git push -u origin main"
fi
