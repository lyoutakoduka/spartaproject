#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test to execute Python corresponding to platform."""

from pathlib import Path
from platform import uname

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.path.modify.get_resource import get_resource
from pyspartaproj.script.shell.execute_python import (
    execute_python,
    get_script_string,
)
from pyspartaproj.script.string.temporary_text import temporary_text


def _get_script_text(script_text: str) -> str:
    return get_script_string(get_resource(local_path=Path(script_text)))


def test_path() -> None:
    """Test to convert path to the format for executing script in Python."""
    path_elements: Strs = ["A", "B", "C"]
    identifier: str = "/" if "Linux" == uname().system else "\\"

    assert identifier.join(path_elements) == get_script_string(
        Path(*path_elements)
    )


def test_command() -> None:
    """Test to execute simple Python script."""
    assert temporary_text(3, 3) == list(
        execute_python([_get_script_text("indices.py")])
    )


def test_platform() -> None:
    """Test to execute Python script for all executable platform."""
    expected: Strs = ["linux", "windows"]

    assert expected == [
        result.lower()
        for platform in expected
        for result in execute_python(
            [_get_script_text("execute_platform.py")],
            platform=platform,
        )
    ]


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_path()
    test_command()
    test_platform()
    return True
