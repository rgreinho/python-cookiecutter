{{ cookiecutter.repo_name }}
================

{{ cookiecutter.project_short_description }}

Quickstart
----------

Install `docker`_.

Setup the full environment::

  make

Setup a local dev environment::

  make venv
  source venv/bin/activate
  python setup.py develop

Use `make help` to see all the available make targets.

.. _`docker`: https://docs.docker.com/engine/understanding-docker/
