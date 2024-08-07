#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to execute specific commands in PowerShell."""

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.path.modify.get_resource import get_resource
from pyspartaproj.script.shell.execute_powershell import (
    convert_mount_path,
    execute_powershell,
    get_double_quoted_command,
    get_path_string,
    get_quoted_path,
    get_script_string,
)
from pyspartaproj.script.string.temporary_text import temporary_text


def _get_formatted_path(path_elements: Strs) -> str:
    return "\\".join(path_elements)


def _get_config_file() -> Path:
    return get_resource(local_path=Path("execute_powershell", "forward.json"))


def _execute_powershell(commands: Strs) -> Strs:
    return list(execute_powershell(commands, forward=_get_config_file()))


def test_script() -> None:
    """Test to convert script part of command string on PowerShell."""
    path_elements: Strs = ["A", "B", "C"]
    assert "/".join(path_elements) == get_script_string(Path(*path_elements))


def test_path() -> None:
    """Test to convert argument part of command string on PowerShell."""
    path_elements: Strs = ["A", "B", "C"]
    assert _get_formatted_path(path_elements) == get_path_string(
        Path(*path_elements)
    )


def test_argument() -> None:
    """Test to get path surrounded by quotation for executing on PowerShell."""
    path_elements: Strs = ["A", "B", "C"]
    expected: str = _get_formatted_path(path_elements).join(["'"] * 2)
    assert expected == get_quoted_path(get_path_string(Path(*path_elements)))


def test_all() -> None:
    """Test to convert command part of command string on PowerShell."""
    expected: Strs = ["Write-Output", "Test"]
    assert expected == get_double_quoted_command(expected).replace(
        '"', ""
    ).split(" ")


def test_write() -> None:
    """Test for executing simple command on PowerShell."""
    expected: Strs = temporary_text(3, 3)
    commands: Strs = ["; ".join(["Write-Output " + text for text in expected])]

    assert expected == _execute_powershell(
        [get_double_quoted_command(commands)]
    )


def test_command() -> None:
    """Test for executing simple script on PowerShell.

    Execute simple Write-Output script
        that takes the path you want to print as argument.
    """
    expected: Path = get_resource(local_path=Path("command.ps1"))

    assert [get_path_string(expected)] == _execute_powershell(
        [
            get_script_string(expected),
            get_double_quoted_command(
                [get_quoted_path(get_path_string(expected))] * 2
            ),
        ]
    )


def test_mount() -> None:
    """Test to convert shared path between Linux and Windows."""
    path_elements: Strs = ["A", "B", "C"]
    expected: Path = Path("C:/", *path_elements)

    for path in [Path("/", "mnt", "c", *path_elements), expected]:
        assert expected == convert_mount_path(path)
