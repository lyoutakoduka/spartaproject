#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get the platform of current executing script."""

from platform import uname


def get_platform() -> str:
    """Get the platform of current executing script.

    Returns:
        str: Platform information.
    """
    return uname().system.lower()
