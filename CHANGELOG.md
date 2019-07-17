# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [[1.5.0]] - 2019-07-17

## Changed

- Replace `Makefiles` with [Invoke](https://github.com/pyinvoke/invoke) and [Nox](https://nox.thea.codes) scripts.
- Remove `Tox`.
- Update CircleCI configurations for 2.1.
- Update the dependecies

## [[1.4.0]] - 2019-02-03

### Added

- Add a `CHANGELOG.md` file.
- Setup `loguru` for logging.
- Add a hook to initialize the `gh-pages` branch.
- Add a script and a `Makefile` target to update the documentation in the `gh-pages` branch.
- Add support for pytest-xdist to run tests in a distributed fashion

### Changed

- Rename the Makefile targets.
- Fix the Makefile target dependencies.
- Update the dependencies.
  - Adjust pytest version do work with `pytest-socket`.
- Adjust the CircleCI configuration.
  - Use Python 3.7.0
  - Update the workflow to publish the documentation to GitHub pages automatically.
- Move the tests directory to the root of the project.
- Restructure the documentation in a more sensible way.
- Use the [aiohttp](https://github.com/aio-libs/aiohttp-theme) theme for the documentation.
- Use a custom CSS file to emphasize keywords in the reference documentation and keywords between backticks.

### Fixed

- Fix the `Makefile` to prevent the `venv` target to run unnecessarily.

### Removed

- Remove the `bootstrap-theme` support for Sphinx

[//]: # (Release links)
[1.4.0]: https://github.com/rgreinho/python-cookiecutter/releases/tag/1.4.0
[1.5.0]: https://github.com/rgreinho/python-cookiecutter/releases/tag/1.5.0

[//]: # (Issue/PR links)
