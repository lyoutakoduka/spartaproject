#!/usr/bin/env python

"""Test module to execute specific commands in PowerShell."""

from pathlib import Path

from pyspartalib.context.callable_context import Type
from pyspartalib.context.default.string_context import Strs
from pyspartalib.script.path.modify.get_resource import get_resource
from pyspartalib.script.shell.execute_powershell import (
    execute_powershell,
    get_double_quoted_command,
    get_path_string,
    get_quoted_path,
    get_script_string,
)
from pyspartalib.script.string.temporary_text import temporary_text


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _print_command() -> str:
    return "Write-Output"


def _get_path_elements() -> Strs:
    return ["A", "B", "C"]


def _get_formatted_path(path_elements: Strs) -> str:
    return "\\".join(path_elements)


def _get_config_file() -> Path:
    return get_resource(local_path=Path("forward.json"))


def _execute_powershell(commands: Strs) -> Strs:
    return list(execute_powershell(commands, forward=_get_config_file()))


def _get_result_all(expected: Strs) -> Strs:
    return get_double_quoted_command(expected).replace('"', "").split(" ")


def _get_result_write(expected: Strs) -> Strs:
    return _execute_powershell(
        [get_double_quoted_command(_get_commands_write(expected))],
    )


def _get_commands_write(expected: Strs) -> Strs:
    return ["; ".join([_print_command() + " " + text for text in expected])]


def _get_result_command(expected: Path) -> Strs:
    return _execute_powershell(
        [
            get_script_string(expected),
            get_double_quoted_command(
                [get_quoted_path(get_path_string(expected))] * 2,
            ),
        ],
    )


def test_script() -> None:
    """Test to convert script part of command string on PowerShell."""
    path_elements: Strs = _get_path_elements()

    _difference_error(
        get_script_string(Path(*path_elements)),
        "/".join(path_elements),
    )


def test_path() -> None:
    """Test to convert argument part of command string on PowerShell."""
    path_elements: Strs = _get_path_elements()

    _difference_error(
        get_path_string(Path(*path_elements)),
        _get_formatted_path(path_elements),
    )


def test_argument() -> None:
    """Test to get path surrounded by quotation for executing on PowerShell."""
    path_elements: Strs = _get_path_elements()

    _difference_error(
        get_quoted_path(get_path_string(Path(*path_elements))),
        _get_formatted_path(path_elements).join(["'"] * 2),
    )


def test_grouped_all() -> None:
    """Test to convert command part of command string on PowerShell."""
    expected: Strs = [_print_command(), "Test"]

    _difference_error(_get_result_all(expected), expected)


def test_write() -> None:
    """Test for executing simple command on PowerShell."""
    expected: Strs = temporary_text(3, 3)

    _difference_error(_get_result_write(expected), expected)


def test_command() -> None:
    """Test for executing simple script on PowerShell.

    Execute simple Write-Output script
        that takes the path you want to print as argument.
    """
    expected: Path = get_resource(local_path=Path("tools", "command.ps1"))

    _difference_error(
        _get_result_command(expected),
        [get_path_string(expected)],
    )
