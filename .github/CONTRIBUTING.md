# Contributing

## Guidelines

* We are interested in various different kinds of improvement for this cookiecutter; please feel free to raise an [Issue](https://github.com/rgreinho/python-cookiecutter/issues) if you would like to work on something major to ensure efficient collaboration and avoid duplicate effort.
* Use the provided templates to file an [Issue](https://github.com/rgreinho/python-cookiecutter/issues) or a [Pull Request](https://github.com/rgreinho/python-cookiecutter/pulls).
* Create a topic branch from where you want to base your work.
* Make sure you have added tests for your changes.
* Run all the tests to ensure nothing else was accidentally broken.
* Reformat the code by following the formatting section below.
* Submit a pull request.

## Tests

### Prerequisites

In order to run the tests, you will need to install [Docker](https://docs.docker.com/engine/understanding-docker/).

### Run the tests

To ensure the cookiecutter is still functional after you cnahged something, use the `ci-test` target of the `Makefile`:
```
make ci-tests
```
