===================
cookiecutter-python
===================

Cookiecutter template for a python project. See https://github.com/audreyr/cookiecutter. This is inspired from the openstack cookiecutter (https://git.openstack.org/openstack-dev/cookiecutter.git).

* Free software: Apache license
* pbr_: Set up to use Python Build Reasonableness
* Tox_ testing: Setup to easily test for Python 2.6, 2.7, 3.3, 3.4
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

* Add the project to your GitHub account.


.. _pbr: http://docs.openstack.org/developer/pbr
.. _OpenStack-Infra: http://docs.openstack.org/infra/system-config
.. _testrepository: https://testrepository.readthedocs.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _hacking: https://git.openstack.org/cgit/openstack-dev/hacking/plain/HACKING.rst
