#!/usr/bin/env sh

# Initialize the git repository.
git init
git add .
git commit -a -m "Initial Cookiecutter Commit."
git tag -f -a 0.1.0 -m 0.1.0

# Create gh-pages branch.
git symbolic-ref HEAD refs/heads/gh-pages
rm .git/index
git clean -fdx
touch .nojekyll
git checkout main .gitignore
git add .
git commit -m "Initialize gh-pages"
git checkout main
