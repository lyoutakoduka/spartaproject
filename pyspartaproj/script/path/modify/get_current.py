#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get current working directory that allow symbolic link."""

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.shell.execute_command import execute_command


def get_current() -> Path:
    """Get current working directory that allow symbolic link.

    Not Path.cwd() or os.getcwd()

    Returns:
        Path: current working directory
    """
    results: Strs = execute_command(["pwd"])

    if 1 == len(results):
        return Path(results[0])

    raise ValueError
