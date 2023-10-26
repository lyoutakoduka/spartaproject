#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test to execute Python according to OS."""


from pyspartaproj.script.path.modify.get_resource import get_resource
from pyspartaproj.script.shell.execute_python import (
    execute_python,
    get_script_string,
)


def test_command() -> None:
    """Test to execute Python script that return version of interpreter."""
    assert [str(i).zfill(3) for i in range(3)] == list(
        execute_python([get_script_string(get_resource(["indices.py"]))])
    )


def main() -> bool:
    """Run all tests.

    Returns:
        bool: success if get to the end of function
    """
    test_command()
    return True
