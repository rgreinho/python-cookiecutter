# python-cookiecutter

This is a [cookiecutter](https://github.com/audreyr/cookiecutter) template for a quickly creating command line utilities in python.

It comes with the following features:

* Free software: MIT license
* All the administrative tasks are defined in the `Makefile`
* [Anyconfig](https://github.com/ssato/python-anyconfig): Read and validate configuration file
* [CircleCI](https://circleci.com/): Continuous Integration for your project
* [Click](http://click.pocoo.org/6/): Create beautiful command line interfaces

  * TAB completion support
* [coala](https://coala.io/): Implement static analyzers through the use of:

  * Git Commit format checker
  * Pin Requirements checker
  * Pycodestyle
  * PyDocStyle
  * PyFlakes
  * PyLint

* [Conda](https://conda.io/docs/index.html): Support for conda package manager
* [Docker](https://www.docker.com/): Containerize the project
* [EditorConfig](http://editorconfig.org/): Maintain consistent coding styles between different editors
* [Github templates](https://github.com/blog/2111-issue-and-pull-request-templates): Create consistent [Issues](https://help.github.com/articles/creating-an-issue-template-for-your-repository/) and [Pull Requests](https://help.github.com/articles/creating-a-pull-request-template-for-your-repository/)
* [PBR](http://docs.openstack.org/developer/pbr): To easily package your application
* [Pytest](https://docs.pytest.org/en/latest/): Better unit testing
* [Sphinx](http://sphinx-doc.org/): Documentation ready for generation and publication
* [Tox](http://testrun.org/tox/): Easily setup tests for Python 3.6
* [YAPF](https://github.com/google/yapf): Automatic code formatting

## Usage

### Setup

Install the latest Cookiecutter if you haven't installed it yet:
```
pip install -U cookiecutter
```

Generate a Python project:
```
cookiecutter https://github.com/rgreinho/python-cookiecutter
```

Congratulations! Now that your project is fully generated, you have access to a lot of features, mostly using the `Makefile`.

To run the initial setup, run:
```
make
```

### Pushing to Github

[Create a new repository on Github](https://help.github.com/articles/creating-a-new-repository/) and [add the remote](https://help.github.com/articles/adding-a-remote/) to this repository
```
git remote add origin https://github.com/<user>/<repo.git>
git push -u origin master
git push --tags
```

### Enabling CircleCI

This cookiecutter comes with a pre-defined configuration for [CircleCI](https://circleci.com/). All you have to do is to add the repository of your project to [CircleCI](https://circleci.com/).

### Formatting the code

To end all holy wars about formatting, you should use a formatter. [YAPF](https://github.com/google/yapf) makes this task easy for you.

To check whether you code is formatted correctly, run:
```
make format check
```

And to reformat the entire project use the following:
```
make format
```

### Creating a virtual environment for the project

This is not really necessary as the project will be fully containerized using Docker, but in some cases you might want to setup a local virtual environment for your project.

```
make venv
```

### Running the tests

```
make ci-linters ci-docs ci-tests
```

### Generating the documentation

The documentation is generated using [Sphinx](http://sphinx-doc.org/). All your documentation must be put into the `docs` directory.

To generate the documentation run:
```
make docs
```

### Packaging the application

To create a wheel package of the application:
```
make dist
```

#### setup.cfg

The application is packaged using [PBR](http://docs.openstack.org/developer/pbr). The packaging configuration is located in the `setup.cfg` file. For detailed explanations about the various options, please refer to the [official documentation](https://docs.openstack.org/pbr/latest/user/index.html).

The dependencies of the application are located in the `requirements.txt` file. Modify that file if you need to add or update dependencies. The other dependencies - tests, lint, docs - are located in the `setup.cfg` file.

### Cleaning up

```
make clean docker-clean
```
