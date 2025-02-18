#!/usr/bin/env python

"""Module to get current working directory."""

from collections.abc import Sized
from pathlib import Path

from pyspartalib.context.default.string_context import Strs
from pyspartalib.script.platform.terminal_status import get_terminal
from pyspartalib.script.shell.execute_command import execute_single


def _from_python() -> Path:
    return Path().cwd()


def get_current() -> Path:
    """Get current working directory.

    Call from symbolic link on Linux is not support

    Returns:
        Path: Current working directory.

    """
    return _from_python()
