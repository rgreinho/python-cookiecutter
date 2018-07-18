"""Base class for all the `processor-cli` commands."""
import abc
import logging
import sys

from tabulate import tabulate


def getLogLevel(level):
    """
    Return a Loglevel matching a string.

    If no level matches, logging.NOTSET is returned.

    :param str level: string representing the log level
    :returns: a log level.
    """
    levels = {
        'CRITICAL': logging.CRITICAL,
        'ERROR': logging.ERROR,
        'WARNING': logging.WARNING,
        'INFO': logging.INFO,
        'DEBUG': logging.DEBUG,
        'NOTSET': logging.NOTSET
    }

    if not level:
        return logging.NOTSET
    return levels.get(level.upper(), logging.NOTSET)


class AbstractCommand:
    """Base class for the commands."""

    __metaclass__ = abc.ABCMeta

    def __init__(self, command_args=None, global_args=None):
        """
        Initialize the commands.

        :param command_args: arguments of the command
        :param global_args: arguments of the program
        """
        # Store the global arguments.
        self.global_args = global_args or {}

        # Store the command arguments.
        self.args = command_args or {}

        # Retrieve the the logger.
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(format='[%(levelname).4s] %(asctime)s - %(message)s', datefmt='%Y/%m/%d %I:%M:%S %p')
        level = getLogLevel(self.global_args.get('log_level'))
        self.logger.setLevel(level)

        # Set display parameters.
        self.data = []
        self.headers = []

    def execute(self):
        """Execute the command."""
        try:
            sys.exit(self._execute())
        except Exception as e:
            self.logger.error(e)
            self.logger.exception(e)
            sys.exit(1)

    @abc.abstractmethod
    def _execute(self):
        """Define the internal execution of the command."""
        raise NotImplementedError

    def display_tabular_data(self):
        """
        Show the results in a table on the screen.

        If not header is defined, only the data is displayed, otherwise, the results will be shown in a table.
        """
        # Nothing to display if there is no data.
        if not self.data:
            return

        # Define the table format based on the headers content.
        table_format = "simple" if self.headers else "plain"

        # Print the results.
        print(tabulate(self.data, self.headers, tablefmt=table_format))

    def placeholder_dict(self):
        """
        Convert the set of placeholders to a dictionary.

        Placeholders are a set of key/value pairs. Their format is `key=value`. During the convertion, the `key`
        becomes the key of the entry in the dictionary, the `value` becomes the value of the entry.

        :param set placeholder: the placeholder to convert
        :return dict: a dictionary representing the placeholder set.
        """
        placeholders = self.args.get('placeholder', [])
        kvp_list = [kvp.split('=', 1) for kvp in placeholders if '=' in kvp]
        return dict(kvp_list)
