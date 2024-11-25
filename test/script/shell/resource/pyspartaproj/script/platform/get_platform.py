#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get current executed platform."""

from platform import uname


def get_platform() -> str:
    """Get current executed platform.

    Returns:
        str: Executed platform.
    """
    return uname().system.lower()
