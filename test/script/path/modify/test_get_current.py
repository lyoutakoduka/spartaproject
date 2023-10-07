#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.execute.execute_command import execute_command
from pyspartaproj.script.path.modify.get_current import get_current


def test_current() -> None:
    result: Path = get_current()
    assert result == Path(execute_command(["pwd"])[0])


def main() -> bool:
    test_current()
    return True
