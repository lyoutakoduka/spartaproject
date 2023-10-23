#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test to execute commands in PowerShell."""

from pathlib import Path
from platform import uname
from tempfile import TemporaryDirectory

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.file.text.export_file import text_export
from pyspartaproj.script.shell.execute_powershell import (
    execute_powershell,
    get_path_string,
    get_quoted_paths,
    get_script_executable,
)


def _get_resource_path(current: str, target: str) -> Path:
    return Path(Path(current).parent, "resource", target)


def test_script() -> None:
    """Test for converting path to text that executable in PowerShell."""
    expected: Path = Path(__file__)
    assert expected == Path(get_path_string(expected))


def test_argument() -> None:
    """Test for converting path to text of argument.

    It's executable in PowerShell.
    """
    expected: Path = Path(__file__)
    assert expected == Path(get_quoted_paths(expected).replace("'", ""))


def test_all() -> None:
    expected: Strs = ["Write-Output", "Test"]
    assert expected == get_script_executable(expected).replace('"', "").split(
        " "
    )


def test_write() -> None:
    """Test for Write-Output that is shown three line number."""
    expected: Strs = [str(i).zfill(3) for i in range(3)]

    assert expected == execute_powershell(
        [
            get_script_executable(
                ["; ".join(["Write-Output " + text for text in expected])]
            )
        ]
    )


def test_command() -> None:
    """Test to get string that is executable in PowerShell.

    Execute simple Write-Output script
    that takes the path you want to print as argument.
    """
    expected: Path = Path(__file__)
    script_text: str = "\n".join(
        ["Param([String]$text)", "Write-Output $text"]
    )

    with TemporaryDirectory() as temporary_path:
        stdout_path: Path = Path(temporary_path, "temporary.ps1")
        text_export(stdout_path, script_text)
        executable_test: str = get_script_executable(
            [get_path_string(stdout_path), get_quoted_paths(expected)]
        )

        if "Windows" == uname().system:
            result: Strs = execute_powershell(executable_test)

            assert 1 == len(result)
            assert expected == Path(result[0])


def main() -> bool:
    """Run all tests.

    Returns:
        bool: success if get to the end of function
    """
    test_script()
    test_argument()
    test_all()
    test_write()
    test_command()
    return True
