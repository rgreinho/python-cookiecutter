Contributing
============

Guidelines
----------

* We are interested in various different kinds of improvement for {{ cookiecutter.repo_name }}; please feel free to raise an `Issue`_ if you would like to work on something major to ensure efficient collaboration and avoid duplicate effort.
* Use the provided templates to file an `Issue`_ or a `Pull Request`_.
* Create a topic branch from where you want to base your work.
* Make sure you have added tests for your changes.
* Run all the tests to ensure nothing else was accidentally broken.
* Reformat the code by following the formatting section below.
* Submit a pull request.

Formatting your code
--------------------

For formatting the files properly, please use `YAPF`_.

In the root directory of the project, run the following command:

.. code-block:: bash

  yapf -r -i .

or

.. code-block:: bash

  make format

There is also a lot of YAPF plugins available for different editors. Here are a few:

  * `atom.io <https://atom.io/packages/python-yapf>`_
  * `emacs <https://github.com/paetzke/py-yapf.el>`_
  * `sublime text <https://github.com/jason-kane/PyYapf>`_
  * `vim <https://github.com/google/yapf/blob/master/plugins/yapf.vim>`_

.. _`Issue`: https://github.com/{{ cookiecutter.author }}/{{ cookiecutter.repo_name }}/issues
.. _`Pull Request`: https://github.com/{{ cookiecutter.author }}/{{ cookiecutter.repo_name }}/pulls
.. _`YAPF`: https://github.com/google/yapf
