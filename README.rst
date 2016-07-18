===================
cookiecutter-python
===================

Cookiecutter template for a python project. See https://github.com/audreyr/cookiecutter. This is inspired from the openstack cookiecutter (https://git.openstack.org/openstack-dev/cookiecutter.git).

* Free software: MIT license
* DocOpt_: CLI made nice and easy
* pbr_: Set up to use Python Build Reasonableness
* TestTools_: Better unit testing
* Tox_ testing: Setup to easily test for Python 2.7, 3.5
* Sphinx_ docs: Documentation ready for generation and publication

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

.. _DocOpt: http://docopt.org/
.. _pbr: http://docs.openstack.org/developer/pbr
.. _TestTools: http://testtools.readthedocs.org/en/latest/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
