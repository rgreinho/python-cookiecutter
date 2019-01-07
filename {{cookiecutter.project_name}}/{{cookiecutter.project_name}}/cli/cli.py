"""Define the top-level cli command."""
import logging
import os
import sys

import click
from loguru import logger

from {{ cookiecutter.project_name }} import config
from {{ cookiecutter.project_name }}.cli.base import AbstractCommand
from {{ cookiecutter.project_name }}.core.version import detect_from_metadata

# Set the project name.
APP_NAME = '{{ cookiecutter.project_name }}'

# Retrieve the project version from packaging.
__version__ = detect_from_metadata(APP_NAME)


# pylint: disable=unused-argument
#   The arguments are used via the `self.args` dict of the `AbstractCommand` class.
@click.group()
@click.version_option(version=__version__)
@click.option('-v', '--verbose', count=True, help='defines the log level')
@click.pass_context
def cli(ctx, verbose):
    """Manage CLI commands."""
    ctx.obj = {**ctx.params}
    ctx.auto_envvar_prefix = '{{ cookiecutter.prefix|upper }}'

    # Load defaults from configuration file if any.
    cfg_path = os.path.join(click.get_app_dir(APP_NAME), APP_NAME + '.conf')
    cfg = cfg_path if os.path.exists(cfg_path) else None
    ctx.default_map = config.load(cfg, with_defaults=True, validate=True)

    # Configure logger.
    # The log level gets adjusted by adding/removing `-v` flags:
    #   None    : Initial log level is WARNING.
    #   -v      : INFO
    #   -vv     : DEBUG
    #   -vvv    : TRACE
    # For 2 `-v` and more, the log format also changes from compact to verbose.
    INITIAL_LOG_LEVEL = logging.WARNING
    LOG_FORMAT_COMPACT = "<level>{message}</level>"
    LOG_FORMAT_VERBOSE = "<level>{time:YYYY-MM-DDTHH:mm:ssZZ} {name}:{line:<4} {message}</level>"
    log_level = max(INITIAL_LOG_LEVEL - verbose * 10, 0)
    log_format = LOG_FORMAT_VERBOSE if log_level < logging.INFO else LOG_FORMAT_COMPACT

    # Remove any predefined logger.
    logger.remove()

    # Set the log colors.
    logger.level('ERROR', color='<red><bold>')
    logger.level('WARNING', color='<yellow>')
    logger.level('SUCCESS', color='<green>')
    logger.level('INFO', color='<cyan>')
    logger.level('DEBUG', color='<blue>')
    logger.level('TRACE', color='<magenta>')

    # Add the logger.
    logger.add(sys.stdout, format=log_format, level=log_level, colorize=True)


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

    def _execute(self):
        """Define the internal execution of the command."""
        click.echo('Hey {}!'.format(self.args['name']))


cli.add_command(hello)
cli.add_command(hello_world)
