"""Define the anyconfig configuration."""
import anyconfig

CONFIGURATION_DEFAULTS = {'hello': {'name': 'stranger'}}

CONFIGURATION_SCHEMA = {
    'type': 'object',
    'properties': {
        'hello': {
            'type': 'object',
            'properties': {
                'name': {
                    'type': 'string'
                }
            }
        }
    }
}


def load(path=None, with_defaults=False, validate=False):
    """
    Load the configuration.

    :param str path: configuration file path. If set to `None`, it makes the configuration file optional, meaning
        that either only the defaults will be loaded or that the configuration will be empty. Otherwise the
        loading will fail if the file is not found.
    :param bool with_defaults: if `True`, loads the default values when they are not specified in the configuration file
    :param bool validate: if `True`, validates the configuration. If an error is detected, a `SyntaxError`
        will be raised. The error message should indicate which part of the configuration file was invalid.
    :returns: (dict) A dictionary representing the configuration.
    """
    # Prepare the configuration dictionary, with the default values if requested.
    conf = CONFIGURATION_DEFAULTS if with_defaults else {}

    # Load the configuration file if specified.
    conf_from_file = {} if path is None else anyconfig.load(path)

    # Merge the configuration into the dictionary containing the defaults.
    # If `with_defaults` is False, this step simply loads the configuration file.
    anyconfig.merge(conf, conf_from_file)

    # Validate the configuration.
    if validate:
        (rc, err) = anyconfig.validate(conf, CONFIGURATION_SCHEMA)
        if not rc:
            raise SyntaxError(err)

    return conf
