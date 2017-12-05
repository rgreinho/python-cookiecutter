# Makefile variables.
SHELL = /bin/bash

# Misc.
TOPDIR = $(shell git rev-parse --show-toplevel)
TESTDIR = test-output

default: setup

help: # Display help
	@awk -F ':|##' \
		'/^[^\t].+?:.*?##/ {\
			printf "\033[36m%-30s\033[0m %s\n", $$1, $$NF \
		}' $(MAKEFILE_LIST) | sort

ci-prep-env: venv # Prep the test environment
	mkdir -p test-output
	. venv/bin/activate && cd test-output && cookiecutter --no-input --overwrite-if-exists ../
	cd $(TESTDIR)/project && make

ci-tests: ci-prep-env ## Run the unit tests
	cd $(TESTDIR)/project && make ci-linters ci-docs ci-tests

clean: ## Remove unwanted files in project (!DESTRUCTIVE!)
	cd $(TOPDIR); git clean -ffdx && git reset --hard

setup: venv ## Setup the full environment (default)

venv: venv/bin/activate ## Setup local venv

venv/bin/activate:
	test -d venv || python3 -m venv venv
	. venv/bin/activate && pip install -U pip setuptools cookiecutter==1.6.0

.PHONY: ci-prep-env ci-tests clean setup
