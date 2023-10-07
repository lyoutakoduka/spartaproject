#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test to execute commands in PowerShell."""

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.execute.execute_powershell import (
    execute_powershell,
    get_path_string,
    get_quoted_paths,
)


def test_write() -> None:
    """Test for Write-Output that is shown three line number."""

    expected: Strs = [str(i).zfill(3) for i in range(3)]
    command: str = "; ".join(["Write-Output " + text for text in expected])

    assert expected == execute_powershell(command)


def test_script() -> None:
    """Test for converting path to text that executable in PowerShell."""

    expected: Path = Path(__file__)
    assert expected == Path(get_path_string(expected))


def test_argument() -> None:
    """Test for converting path to text of argument
    that is executable in PowerShell.
    """
    expected: Path = Path(__file__)
    assert expected == Path(get_quoted_paths(expected).replace("'", ""))


def main() -> bool:
    """Run all tests.

    Returns:
        bool: success if get to the end of function
    """
    test_write()
    test_script()
    test_argument()
    return True
