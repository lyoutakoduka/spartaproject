#!/usr/bin/env python

"""Module to get current working directory."""

from pathlib import Path

from pyspartalib.context.default.string_context import Strs
from pyspartalib.script.shell.execute_command import execute_single


def _from_python() -> Path:
    return Path().cwd()


def _get_shell_current() -> Strs:
    return list(execute_single(["pwd"]))


def get_current() -> Path:
    """Get current working directory.

    Call from symbolic link on Linux is not support

    Returns:
        Path: Current working directory.

    """
    return _from_python()
