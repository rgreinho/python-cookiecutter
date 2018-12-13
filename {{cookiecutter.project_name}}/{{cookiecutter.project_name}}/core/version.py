"""Define a set of utility functions for managing versions."""
from pbr import version
import pkg_resources


def detect_from_metadata(package):
    """
    Detect a package version number from the metadata.

    If the version number cannot be detected, the function returns 0.

    :param str package: package name
    :returns str: the package version number.
    """
    try:
        try:
            version_info = version.VersionInfo(package)
            package_version = version_info.release_string()
        except (ModuleNotFoundError, pkg_resources.DistributionNotFound):
            distribution_info = pkg_resources.get_distribution(package)
            package_version = distribution_info.version
    except Exception:
        package_version = 0

    return package_version
