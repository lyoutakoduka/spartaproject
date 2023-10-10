#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get current working directory that allow symbolic link."""

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.shell.execute_command import execute_command


def get_current_symbolic() -> Path:
    """Get current working directory including symbolic link.

    Raises:
        ValueError: when fail to get path

    Returns:
        Path: current working directory as symbolic link
    """
    results: Strs = execute_command(["pwd"])

    if 1 == len(results):
        return Path(results[0])

    raise ValueError


def get_current() -> Path:
    """Get current working directory.

    Returns:
        Path: current working directory
    """
    return Path.cwd()
