#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test to execute commands in PowerShell."""

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.shell.execute_powershell import (
    convert_mount_path,
    execute_powershell,
    get_path_string,
    get_quoted_paths,
    get_script_executable,
    get_script_string,
)


def _get_resource_path(current: str, target: str) -> Path:
    return Path(Path(current).parent, "resource", target)


def _get_formatted_path(path_elements: Strs) -> str:
    return "\\".join(path_elements)


def test_script() -> None:
    path_elements: Strs = ["A", "B", "C"]
    assert "/".join(path_elements) == get_script_string(Path(*path_elements))


def test_path() -> None:
    """Test for converting path to text that executable in PowerShell."""
    path_elements: Strs = ["A", "B", "C"]
    assert _get_formatted_path(path_elements) == get_path_string(
        Path(*path_elements)
    )


def test_argument() -> None:
    """Test for converting path to text of argument.

    It's executable in PowerShell.
    """
    path_elements: Strs = ["A", "B", "C"]
    expected: str = _get_formatted_path(path_elements).join(["'"] * 2)
    assert expected == get_quoted_paths(Path(*path_elements))


def test_all() -> None:
    expected: Strs = ["Write-Output", "Test"]
    assert expected == get_script_executable(expected).replace('"', "").split(
        " "
    )


def test_write() -> None:
    """Test for Write-Output that is shown three line number."""
    expected: Strs = [str(i).zfill(3) for i in range(3)]
    commands: Strs = ["; ".join(["Write-Output " + text for text in expected])]

    assert expected == list(
        execute_powershell([get_script_executable(commands)])
    )


def test_command() -> None:
    """Test to get string that is executable in PowerShell.

    Execute simple Write-Output script
    that takes the path you want to print as argument.
    """
    expected: Path = _get_resource_path(__file__, "command.ps1")

    assert [get_path_string(expected)] == list(
        execute_powershell(
            [
                get_script_string(expected),
                get_script_executable([get_quoted_paths(expected)] * 2),
            ]
        )
    )


def test_mount() -> None:
    name: str = "test"
    expected: Path = Path("C:/", name)

    assert expected == convert_mount_path(Path("/", "mnt", "c", name))
    assert expected == convert_mount_path(expected)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: success if get to the end of function
    """
    test_script()
    test_path()
    test_argument()
    test_all()
    test_write()
    test_command()
    test_mount()
    return True
