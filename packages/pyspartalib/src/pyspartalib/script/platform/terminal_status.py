#!/usr/bin/env python

"""Module to get the current executing terminal."""

from os import getenv


def _get_environment(key: str) -> bool:
    return getenv(key.upper()) is not None


def get_terminal() -> str:
    """Get the current executing terminal.

    Returns:
        str: Three type of terminals on this module are considered.

            1. VSCode test explorer
                Return "test".

            2. VSCode integrated terminal
                Return "vscode".

            3. Other terminals
                Return "terminal".

    """
    if _get_environment("vscode_cwd"):
        return "test"

    if _get_environment("term_program"):
        return "vscode"

    return "terminal"
