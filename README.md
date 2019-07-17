# python-cookiecutter

This is an opinionated [cookiecutter](https://github.com/audreyr/cookiecutter) template for a quickly creating command line utilities in python.

It comes with the following features:

* Free software: MIT license
* All the administrative tasks are defined in the `invoke` and `nox` scripts
* [Anyconfig](https://github.com/ssato/python-anyconfig): Read and validate configuration file
* [CircleCI](https://circleci.com/): Continuous Integration for your project
  * Check the formating
  * Build the documentation
  * Lint the code and docstrings
  * Test the code
  * Publish the documentation when tagging your code
  * Upload a package to PyPI when tagging your code
* [Click](http://click.pocoo.org/6/): Create beautiful command line interfaces
  * TAB completion support
* [Docker](https://www.docker.com/): Containerize the project
* [EditorConfig](http://editorconfig.org/): Maintain consistent coding styles between different editors
* [Github templates](https://github.com/blog/2111-issue-and-pull-request-templates): Create consistent [Issues](https://help.github.com/articles/creating-an-issue-template-for-your-repository/) and [Pull Requests](https://help.github.com/articles/creating-a-pull-request-template-for-your-repository/)
* [Github pages](https://pages.github.com/): Enable GitHub pages and add a CircleCI job to automatically publish the documentation when tagging the project
* [Loguru](https://github.com/Delgan/loguru): Logging made (stupidly) simple
* [Mergify](https://mergify.io/): Automatically merge your PRs
* [PBR](http://docs.openstack.org/developer/pbr): To easily package your application
* [Pytest](https://docs.pytest.org/en/latest/): Better unit testing
  * [coverage](https://github.com/pytest-dev/pytest-cov): plugin that produces coverage reports
  * [mock](https://github.com/pytest-dev/pytest-mock): plugin that installs a mocker fixture
  * [rerunfailures](https://github.com/pytest-dev/pytest-rerunfailures): plugin that re-runs failed tests up to -n times to eliminate flakey failures
  * [socket](https://github.com/miketheman/pytest-socket): plugin that disables or restricts socket calls to ensure network calls are prevented.
  * [xdist](https://github.com/pytest-dev/pytest-xdist): distributed testing plugin
* [Sphinx](http://sphinx-doc.org/): Documentation ready for generation and publication
  * [aiohttp heme](https://github.com/aio-libs/aiohttp-theme) to get a nice look and feel
  * badges support for PyPI, CircleCI and Coveralls.io
  * [markdown](https://www.sphinx-doc.org/en/master/usage/markdown.html) support in addition to reStructured
  * [sphinx click](https://github.com/click-contrib/sphinx-click) to automatically generate the CLI documentation
* [Twine](https://github.com/pypa/twine): Easily publish your package on PyPI
* [YAPF](https://github.com/google/yapf): Automatic code formatting

## Usage

### Setup

Install the latest Cookiecutter if you haven't installed it yet:

```bash
pip install cookiecutter invoke nox
```

Generate a Python project:

```bash
cookiecutter https://github.com/rgreinho/python-cookiecutter
```

Congratulations! Now that your project is fully generated, you have access to a lot of features, mostly using `Invoke` and `Nox`.

To run the initial setup, run:

```bash
inv
```

### Pushing to Github

[Create a new repository on Github](https://help.github.com/articles/creating-a-new-repository/) and [add the remote](https://help.github.com/articles/adding-a-remote/) to this repository

```bash
git remote add origin https://github.com/<user>/<repo.git>
git push -u origin master
git push --tags
```

### Enabling CircleCI

This cookiecutter comes with a pre-defined configuration for [CircleCI](https://circleci.com/). All you have to do is to add the repository of your project to [CircleCI](https://circleci.com/).

### Formatting the code

To end all holy wars about formatting, you should use a formatter. [YAPF](https://github.com/google/yapf) makes this task easy for you.

To check whether you code is formatted correctly, run:

```bash
inv lint-format
```

And to reformat the entire project use the following:

```bash
inv format
```

### Creating a virtual environment for the project

This is not really necessary as the project will be fully containerized using Docker, but in some cases you might want to setup a local virtual environment for your project.

```bash
inv venv
```

### Running all the tests

```bash
inv ci
```

### Generating the documentation

The documentation is generated using [Sphinx](http://sphinx-doc.org/). All your documentation must be put into the `docs` directory.

To generate the documentation run:

```bash
inv docs
```

### Packaging the application

To create a wheel package of the application:

```bash
inv dist
```

#### setup.cfg

The application is packaged using [PBR](http://docs.openstack.org/developer/pbr). The packaging configuration is located in the `setup.cfg` file. For detailed explanations about the various options, please refer to the [official documentation](https://docs.openstack.org/pbr/latest/user/index.html).

The dependencies of the application are located in the `requirements.txt` file. Modify that file if you need to add or update dependencies. The other dependencies - tests, lint, docs - are located in the `setup.cfg` file.

### Cleaning up

```bash
inv clean
```
