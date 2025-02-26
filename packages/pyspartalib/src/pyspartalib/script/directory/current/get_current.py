#!/usr/bin/env python

"""Module to get current working directory."""

from pathlib import Path


def _from_python() -> Path:
    return Path().cwd()


def get_current() -> Path:
    """Get current working directory.

    Note that symbolic link is not support.

    Returns:
        Path: Current working directory.

    """
    return _from_python()
