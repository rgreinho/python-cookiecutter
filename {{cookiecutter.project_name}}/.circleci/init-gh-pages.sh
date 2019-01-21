#!/bin/bash
set -euo pipefail

git symbolic-ref HEAD refs/heads/gh-pages
rm .git/index
git clean -fdx
touch .nojekyll
git checkout master .gitignore
git add .
git commit -m "Initialize gh-pages"
git checkout master
