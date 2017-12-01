# Makefile variables.
SHELL = /bin/bash

# Misc.
TOPDIR = $(shell git rev-parse --show-toplevel)
YAPF_EXCLUDE=*.tox/*,*venv/*

# Docker.
DOCKER_IMAGE = {{ cookiecutter.repo_name }}
DOCKER_IMAGE_VERSION ?= $$(git describe)
DOCKER_IMAGE_FULL = $(DOCKER_IMAGE):$(DOCKER_IMAGE_VERSION)

# External images.
DOCKER_IMAGE_COALA = coala/base:0.11

# Docker run command.
DOCKER_RUN_CMD = docker run -t -v=$$(pwd):/code --rm $(DOCKER_IMAGE_FULL)

default: setup

help: # Display help
	@awk -F ':|##' \
		'/^[^\t].+?:.*?##/ {\
			printf "\033[36m%-30s\033[0m %s\n", $$1, $$NF \
		}' $(MAKEFILE_LIST) | sort

ci-linters: ## Run the static analyzers
	@docker pull $(DOCKER_IMAGE_COALA)
	@docker run -t -v=$$(pwd):/app --workdir=/app --rm $(DOCKER_IMAGE_COALA) coala --ci

ci-docs: ## Ensure the documentation builds
	$(DOCKER_RUN_CMD) tox -e docs

ci-tests: ## Run the unit tests
	$(DOCKER_RUN_CMD) tox

clean: ## Remove unwanted files in project (!DESTRUCTIVE!)
	cd $(TOPDIR); git clean -ffdx && git reset --hard

conda: conda-venv/bin/activate ## Setup a conda environment

conda-venv/bin/activate:
	@conda env create --prefix=conda-venv python=3

docker-build: Dockerfile ## Build a docker development image
	@docker build -t $(DOCKER_IMAGE_FULL) .

docker-clean: ## Remove all docker images built for this project (!DESTRUCTIVE!)
	@docker image rm -f $$(docker image ls --filter reference=$(DOCKER_IMAGE) -q)

docs: ## Build documentation
	$(DOCKER_RUN_CMD) sphinx-build -W -b html -d docs/build/doctrees docs/source/ docs/build/html

format: ## Format the codebase using YAPF
	$(DOCKER_RUN_CMD) yapf -r -i -e{$(YAPF_EXCLUDE)} .

format-check: ## Check the code formatting using YAPF
	$(DOCKER_RUN_CMD) yapf -r -d -e{$(YAPF_EXCLUDE)} .

setup: docker-build ## Setup the full environment (default)

venv: venv/bin/activate ## Setup local venv

venv/bin/activate: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate && pip install -U pip setuptools && pip install -r requirements.txt
	. venv/bin/activate && pip install -e .[docs,local,testing]

venv-check-deps: venv ## Check whether the dependencies are up to date
	@{ \
		. venv/bin/activate && OUTDATED_PKGS=$$(pip list -o --format=columns); \
		if [ -n "$${OUTDATED_PKGS}" ]; then \
			echo "$${OUTDATED_PKGS}"; \
			exit 1; \
		fi \
	}

wheel: docker-build ## Build a wheel package
	$(DOCKER_RUN_CMD) python setup.py bdist_wheel

.PHONY: ci-coala ci-docs ci-tests clean docker-build docker-clean docs format format-check service-api setup wheel venv-check
