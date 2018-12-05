Contributing
============

We are interested in various different kinds of improvement for {{ cookiecutter.project_name }}; please feel free to
raise an `Issue`_ if you would like to work on something major to ensure efficient collaboration and avoid duplicate
effort.

Guidelines
----------

Use the provided templates to file an `Issue`_ or a `Pull Request`_.

Create a topic branch from where you want to base your work.

For formatting the files properly, please use `YAPF`_.In the root directory of the project, run the following command:

.. code-block:: bash

  make format

Make sure you added tests to validate your changes.

Run all the tests to ensure nothing else was accidentally broken.

Commit messages must start with a capitalized and short summary (max. 50 chars) written in the imperative, followed by
an optional, more detailed explanatory text which is separated from the summary by an empty line.

Commit messages should follow best practices, including explaining the context of the problem and how it was solved,
including in caveats or follow up changes required. They should tell the story of the change and provide readers
understanding of what led to it. Please refer to `How to Write a Git Commit Message`_ for more details.

Formatting your code
--------------------

There is also a lot of YAPF plugins available for different editors. Here are a few:

  * `atom.io <https://atom.io/packages/python-yapf>`_
  * `emacs <https://github.com/paetzke/py-yapf.el>`_
  * `sublime text <https://github.com/jason-kane/PyYapf>`_
  * `vim <https://github.com/google/yapf/blob/master/plugins/yapf.vim>`_

.. _`Issue`: https://github.com/{{ cookiecutter.author }}/{{ cookiecutter.project_name }}/issues
.. _`Pull Request`: https://github.com/{{ cookiecutter.author }}/{{ cookiecutter.project_name }}/pulls
.. _`YAPF`: https://github.com/google/yapf
.. _`How to Write a Git Commit Message`: http://chris.beams.io/posts/git-commit
