"""
{{cookiecutter.project_short_description}}

Usage:
    {{cookiecutter.repo_name}} [-hv] <command>


Options:
    -h, --help                  shows the help screen
    -v, --version               shows the version
"""

from docopt import docopt


def main():
    pass


if __name__ == '__main__':
    args = docopt(__doc__, version='{{cookiecutter.version}}')
    main()
