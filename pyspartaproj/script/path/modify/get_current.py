#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get current working directory that allow symbolic link."""

from os import environ
from pathlib import Path


def get_current() -> Path:
    """Get current working directory that allow symbolic link.

    Not Path.cwd() or os.getcwd()

    Returns:
        Path: current working directory
    """
    return Path(environ["PWD"])
