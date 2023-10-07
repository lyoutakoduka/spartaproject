#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.execute.execute_powershell import execute_powershell


def test_write() -> None:
    expected: Strs = [str(i).zfill(3) for i in range(3)]
    command: str = "; ".join(["Write-Output " + text for text in expected])

    assert expected == execute_powershell(command)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: success if get to the end of function
    """
    test_write()
    return True
