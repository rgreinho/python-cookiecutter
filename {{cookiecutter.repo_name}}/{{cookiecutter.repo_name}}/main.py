"""
{{cookiecutter.project_short_description}}

Usage:
    {{cookiecutter.repo_name}} [-hv] <command>


Options:
    -h, --help                  shows the help screen
    -v, --version               shows the version
"""

from docopt import docopt
from docopt import DocoptExit

from {{cookiecutter.repo_name}} import commands


def main():
    args = docopt(__doc__, version='0.1.0', options_first=True)

    # Retrieve the command to execute.
    command_name = args.pop('<command>').capitalize()

    # Retrieve the command arguments.
    command_args = args.pop('<args>')
    if command_args is None:
        command_args = {}

    # After 'poping' '<command>' and '<args>', what is left in the args dictionary are the global arguments.

    # Initialize the logger.
    logging.basicConfig(format='[%(levelname).4s] %(asctime)s %(message)s', datefmt='%Y/%m/%d %H:%M:%S')

    # Retrieve the class from the 'commands' module.
    try:
        command_class = getattr(commands, command_name)
    except AttributeError:
        print('Unknown command.')
        raise DocoptExit()

    # Create an instance of the command.
    command = command_class(command_args, args)

    # Execute the command.
    command.execute()


if __name__ == '__main__':
    main()
