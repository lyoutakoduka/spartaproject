#!/usr/bin/env python

"""Module to get the platform of current executing script."""

from platform import uname


def get_platform() -> str:
    """Get the platform of current executing script.

    Returns:
        str: Platform information.

    """
    return uname().system.lower()


def is_platform_linux() -> bool:
    """Confirm that the platform of current executing script is Linux.

    Returns:
        bool: True if the platform is Linux.

    """
    return "linux" == get_platform()
