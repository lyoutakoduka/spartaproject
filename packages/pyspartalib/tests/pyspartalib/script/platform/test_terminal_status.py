#!/usr/bin/env python

from os import getenv
from pathlib import Path

from pyspartalib.context.custom.type_context import Type
from pyspartalib.script.platform.terminal_status import get_terminal


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _none_error(result: Type | None) -> Type:
    if result is None:
        raise ValueError

    return result


def _get_environment(key: str) -> str:
    return _none_error(getenv(key.upper()))


def _confirm_test_explorer() -> None:
    _difference_error(
        Path(_get_environment("vscode_cwd")).name,
        "Microsoft VS Code",
    )


def _confirm_vscode_terminal() -> None:
    _difference_error(_get_environment("term_program"), get_terminal())
