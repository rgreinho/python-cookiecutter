#!/bin/bash
set -euo pipefail

# Save the current branch.
PREVIOUS_BRANCH=$(git rev-parse --abbrev-ref HEAD)

# Return to the previous branch.
function previous_branch {
  git checkout "${PREVIOUS_BRANCH}"
}

# Go back to the root of the project
GROOT=$(git rev-parse --show-toplevel)
cd "${GROOT}"

# Checkout gh-pages.
git checkout -b gh-pages origin/gh-pages 2>/dev/null || git checkout gh-pages

# Copy the new version of the documentation
cp -r ${GROOT}/docs/build/html/* .

# Add the new packages.
git add .
FILES=$(git status -s)
git commit -am "Publish documentation" -m "${FILES}"

# Push the branch.
git push origin gh-pages

# Return to the previous branch.
previous_branch
