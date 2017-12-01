"""Define the top-level cli command."""
import os

import click
from pbr import version

from {{ cookiecutter.repo_name }}.cli.base import AbstractCommand
from {{ cookiecutter.repo_name }} import config

# Retrieve the project version from packaging.
try:
    try:
        version_info = version.VersionInfo('{{ cookiecutter.repo_name }}')
        __version__ = version_info.release_string()
    except pkg_resources.DistributionNotFound:
        distribution_info = pkg_resources.get_distribution('pip')
        __version__ = distribution_info.version
except Exception:
    __version__ = None


APP_NAME = '{{ cookiecutter.repo_name }}'

@click.group()
@click.version_option(version=__version__)
@click.option(
    '--log-level',
    '-l',
    default='NOTSET',
    type=click.Choice(['NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']),
    help='defines the log level',
    show_default=True)
@click.pass_context
def cli(ctx, log_level):
    """Manage CLI commands."""
    ctx.obj = {**ctx.params}
    ctx.auto_envvar_prefix = '{{ cookiecutter.prefix|upper }}'

    # Load defaults from configuration file if any.
    cfg_path = os.path.join(click.get_app_dir(APP_NAME), APP_NAME+'.conf')
    cfg = cfg_path if os.path.exists(cfg_path) else None
    ctx.default_map = config.load(cfg, with_defaults=True, validate=True)


@click.command()
def hello_world():
    """Greet the world."""
    click.echo('Hello World!')


@click.command()
@click.option('--name')
@click.pass_context
def hello(ctx, name):
    """Greet somebody."""
    command = Hello(ctx.params, ctx.obj)
    command.execute()


class Hello(AbstractCommand):
    """Greet somebody."""

    def __init__(self, command_args, global_args):
        """
        Initialize the command.

        :param command_args: arguments of the command
        :param global_args: arguments of the program
        """
        super(Hello, self).__init__(command_args, global_args)

    def _execute(self):
        """Define the internal execution of the command."""
        click.echo('Hey {}!'.format(self.args['name']))


cli.add_command(hello)
cli.add_command(hello_world)
