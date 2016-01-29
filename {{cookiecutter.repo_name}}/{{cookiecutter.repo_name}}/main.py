"""
{{cookiecutter.project_short_description}}.

Usage:
    {{cookiecutter.repo_name}} action
"""

from docopt import docopt


def main():
    pass


if __name__ == '__main__':
    args = docopt(__doc__version={{cookiecutter.version}})
    main()
