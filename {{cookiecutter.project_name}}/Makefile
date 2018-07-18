# Project configuration.
PROJECT_NAME = {{ cookiecutter.project_name }}

# Makefile variables.
SHELL = /bin/bash

# Makefile parameters.
RUN ?= local
SUFFIX ?=
TAG ?= $(shell git describe)$(SUFFIX)

# Misc.
TOPDIR = $(shell git rev-parse --show-toplevel)
YAPF_EXCLUDE=*.tox/*,*venv/*

# Docker.
DOCKERFILE = Dockerfile$(SUFFIX)
DOCKER_ORG = requestyoracks
DOCKER_REPO = $(DOCKER_ORG)/$(PROJECT_NAME)
DOCKER_IMG = $(DOCKER_REPO):$(TAG)
DOCKER_IMG_COALA = coala/base:0.11

# Run commands.
DOCKER_RUN_CMD = docker run --rm -t -v=$$(pwd):/usr/src/app $(DOCKER_IMG)
LOCAL_RUN_CMD = source venv/bin/activate &&

# Determine whether running the command in a container or locally.
ifeq ($(RUN),docker)
  RUN_CMD = $(DOCKER_RUN_CMD)
else
  RUN_CMD = $(LOCAL_RUN_CMD)
endif

default: setup

.PHONY: help
help: # Display help
	@awk -F ':|##' \
		'/^[^\t].+?:.*?##/ {\
			printf "\033[36m%-30s\033[0m %s\n", $$1, $$NF \
		}' $(MAKEFILE_LIST) | sort

.PHONY: ci
ci: ci-format ci-linters ci-tests

.PHONY: ci-docs
ci-docs: ## Ensure the documentation builds
	$(RUN_CMD) tox -e docs

.PHONY: ci-format
ci-format: ## Check the code formatting using YAPF
	$(RUN_CMD) yapf -r -d -e{$(YAPF_EXCLUDE)} .

.PHONY: ci-linters
ci-linters: ## Run the static analyzers
	@docker pull $(DOCKER_IMAGE_COALA)
	@docker run -t -v=$$(pwd):/app --workdir=/app --rm $(DOCKER_IMAGE_COALA) coala --ci

.PHONY: ci-tests
ci-tests: ## Run the unit tests
	$(RUN_CMD) tox

.PHONY: clean
clean: ## Remove unwanted files in project (!DESTRUCTIVE!)
	cd $(TOPDIR) && git clean -ffdx && git reset --hard

.PHONY: docker-build
docker-build: Dockerfile ## Build a docker development image
	@docker build -t $(DOCKER_IMAGE_FULL) .

.PHONY: docker-clean
docker-clean: ## Remove all docker images built for this project (!DESTRUCTIVE!)
	@docker image rm -f $$(docker image ls --filter reference=$(DOCKER_IMAGE) -q)

.PHONY: docs
docs: ## Build documentation
	$(RUN_CMD) python setup.py build_sphinx

.PHONY: format
format: ## Format the codebase using YAPF
	$(RUN_CMD) yapf -r -i -e{$(YAPF_EXCLUDE)} .

setup: venv ## Setup the full environment (default)

venv: venv/bin/activate ## Setup local venv

venv/bin/activate: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate && pip install -U pip setuptools
	. venv/bin/activate && pip install -e .[docs,local,testing]

.PHONY: wheel
wheel: ## Build a wheel package
	$(RUN_CMD) python setup.py bdist_wheel
