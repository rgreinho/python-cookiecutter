cookiecutter-python
===================

Cookiecutter template for a python project. See https://github.com/audreyr/cookiecutter.

* Free software: MIT license
* All the administrative tasks are defined in the `Makefile`
* Anyconfig_: Read and validate configuration file
* CircleCI_: Continuous Integration for your project
* Click_: Create beautiful command line interfaces
* coala_: Implement static analyzers through the use of
  * Git Commit format checker
  * Pin Requirements checker
  * Pycodestyle
  * PyDocStyle
  * PyFlakes
  * PyLint
* Docker_: Containerize the project
* EditorConfig_: Maintain consistent coding styles between different editors
* PBR_: Set up to use Python Build Reasonableness
* Pytest_: Better unit testing
* Sphinx_: Documentation ready for generation and publication
* Tox_: Easily setup tests for Python 3.6

Usage
-----

Generate a Python package project::

    cookiecutter https://github.com/rgreinho/python-cookiecutter

A working git repo for pbr to work, on newer versions of cookiecutter (>= 0.7.0 released 2013-11-09) this inital commit will be done automatically. Otherwise you will need to init a repo and commit to it before doing anything else::

    cd $repo_name
    git init
    git add .
    git commit -a

Then:

* Check that the versions in the requirements match your needs. They might be a bit old by the time you use this cookiecutter.
* Add the project to your GitHub account.

.. _Anyconfig: https://github.com/ssato/python-anyconfig
.. _CircleCI: https://circleci.com/
.. _Click: http://click.pocoo.org/6/
.. _coala: https://coala.io/
.. _Docker: https://www.docker.com/
.. _EditorConfig: http://editorconfig.org/
.. _PBR: http://docs.openstack.org/developer/pbr
.. _Pytest: https://docs.pytest.org/en/latest/
.. _Sphinx: http://sphinx-doc.org/
.. _Tox: http://testrun.org/tox/
