"""{{cookiecutter.project_short_description}}."""
from {{ cookiecutter.project_name }}.cli.cli import cli

# pylint: disable=no-value-for-parameter
if __name__ == '__main__':
    cli()
