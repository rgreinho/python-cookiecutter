{{ cookiecutter.repo_name }}
============================

{{ cookiecutter.project_short_description}}

Install
-------

Using pip::

    $ pip install {{ cookiecutter.repo_name }}

Read the docs
-------------

The latest documentation is published on Read the Docs: http://{{ cookiecutter.repo_name }}.readthedocs.org.

Build the docs
--------------

To build the documentation::

    $ pip install -r docs-requirements.txt
    $ python setup.py build_sphinx

And then browse to doc/build/html/index.html

Contribute
----------

The repository is located on Github: {{ cookiecutter.repo_name }}.

Formatting
^^^^^^^^^^

For formating the files properly, please use YAPF (https://github.com/google/yapf).

In the root directory of the project, run the following command:

.. code-block:: bash

    yapf -r -i {{ cookiecutter.repo_name }}/
