#!/usr/bin/env python

"""Module to get current working directory."""

from collections.abc import Sized
from pathlib import Path

from pyspartalib.context.default.string_context import Strs
from pyspartalib.script.platform.terminal_status import get_terminal
from pyspartalib.script.shell.execute_command import execute_single


def _length_error(result: Sized, expected: int) -> None:
    if len(result) != expected:
        raise ValueError


def _from_python() -> Path:
    return Path().cwd()


def _get_shell_current() -> Strs:
    return list(execute_single(["pwd"]))


def _from_shell() -> Path:
    result: Strs = _get_shell_current()

    _length_error(result, 1)

    return Path(result[0])


def _confirm_symbolic() -> Path:
    if get_terminal() == "test":
        raise FileNotFoundError

    return _from_shell()


def get_current(symbolic: bool = False) -> Path:
    """Get current working directory.

    Call from symbolic link on Linux is not support

    Returns:
        Path: Current working directory.

    """
    if symbolic is True:
        return _confirm_symbolic()

    return _from_python()
