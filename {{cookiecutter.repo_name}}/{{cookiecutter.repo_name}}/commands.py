import logging
import sys

from docopt import docopt
from tabulate import tabulate


def getLogLevel(level):
    """
    Returns a Loglevel matching a string.

    If no level matches, logging.NOTSET is returned.

    :param str level: string representing the log level
    :returns: a log level.
    """
    levels = {'CRITICAL': logging.CRITICAL,
              'ERROR': logging.ERROR,
              'WARNING': logging.WARNING,
              'INFO': logging.INFO,
              'DEBUG': logging.DEBUG,
              'NOTSET': logging.NOTSET}

    return levels.get(level.upper(), logging.NOTSET)


class AbstractCommand(object):
    """Base class for the commands"""

    def __init__(self, command_args, global_args):
        """
        Initialize the commands.

        :param command_args: arguments of the command
        :param global_args: arguments of the program
        """
        # Store the global arguments.
        self.global_args = global_args

        # Parse the command arguments.
        self.args = docopt(self.__doc__, argv=command_args)

        # Retrieve the the logger.
        self.logger = logging.getLogger(__name__)
        level = getLogLevel(self.global_args['-l'])
        self.logger.setLevel(level)

        # Set display parameters.
        self.data = []
        self.headers = []

    def execute(self):
        # Execute the command.
        try:
            self.execute_internal()
        except Exception as e:
            self.logger.error(e)
            self.logger.exception(e)
            sys.exit(1)

        # Leave the application.
        sys.exit(0)

    def execute_internal(self):
        """Execute the commands"""
        raise NotImplementedError

    def display_tabular_data(self):
        """
        Shows the results on the screen.

        If not header is defined, only the data is displayed, otherwise, the results will be shown in a table.
        """
        # Nothing to display if there is no data.
        if not self.data:
            return

        # Define the table format based on the headers content.
        table_format = "simple" if self.headers else "plain"

        # Print the results.
        print(tabulate(self.data, self.headers, tablefmt=table_format))
