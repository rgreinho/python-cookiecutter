"""Define the top-level cli command."""
import click
from pbr import version

from {{ cookiecutter.repo_name }}.cli.base import AbstractCommand

# Retrieve the project version from PBR.
try:
    version_info = version.VersionInfo('processor-cli')
    __version__ = version_info.release_string()
except AttributeError:
    __version__ = None


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


@click.command()
def hello_world():
    """Greet the world."""
    click.echo('Hello World!')


@click.command()
@click.argument('name', default='you')
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
