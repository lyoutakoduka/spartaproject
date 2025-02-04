#!/usr/bin/env python

from os import getenv


def _get_environment(key: str) -> bool:
    return getenv(key.upper()) is not None


def get_terminal() -> str:
    if _get_environment("vscode_cwd"):
        return "test"

    if _get_environment("term_program"):
        return "vscode"

    return "terminal"
