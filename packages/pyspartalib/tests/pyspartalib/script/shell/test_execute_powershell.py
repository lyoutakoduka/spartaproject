#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to execute specific commands in PowerShell."""

from pathlib import Path

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


def test_script() -> None:
    """Test to convert script part of command string on PowerShell."""
    path_elements: Strs = _get_path_elements()

    assert "/".join(path_elements) == get_script_string(Path(*path_elements))


def test_path() -> None:
    """Test to convert argument part of command string on PowerShell."""
    path_elements: Strs = _get_path_elements()

    assert _get_formatted_path(path_elements) == get_path_string(
        Path(*path_elements)
    )


def test_argument() -> None:
    """Test to get path surrounded by quotation for executing on PowerShell."""
    path_elements: Strs = _get_path_elements()
    expected: str = _get_formatted_path(path_elements).join(["'"] * 2)

    assert expected == get_quoted_path(get_path_string(Path(*path_elements)))


def test_all() -> None:
    """Test to convert command part of command string on PowerShell."""
    expected: Strs = [_print_command(), "Test"]

    assert expected == get_double_quoted_command(expected).replace(
        '"', ""
    ).split(" ")


def test_write() -> None:
    """Test for executing simple command on PowerShell."""
    expected: Strs = temporary_text(3, 3)
    commands: Strs = [
        "; ".join([_print_command() + " " + text for text in expected])
    ]

    assert expected == _execute_powershell(
        [get_double_quoted_command(commands)]
    )


def test_command() -> None:
    """Test for executing simple script on PowerShell.

    Execute simple Write-Output script
        that takes the path you want to print as argument.
    """
    expected: Path = get_resource(local_path=Path("tools", "command.ps1"))

    assert [get_path_string(expected)] == _execute_powershell(
        [
            get_script_string(expected),
            get_double_quoted_command(
                [get_quoted_path(get_path_string(expected))] * 2
            ),
        ]
    )
