#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from spartaproject.script.directory.create_directory_working import (
    create_working_space, get_working_space)
from spartaproject.script.path.modify.get_relative import get_relative


def test_name() -> None:
    EXPECTED: Path = Path('2023', '04', '01', '00', '00', '00', '000000')

    assert EXPECTED == get_working_space(override=True)


def test_create() -> None:
    NAME: str = '.trash'
    EXPECTED: Path = Path(
        NAME, '2023', '04', '01', '00', '00', '00', '000000'
    )

    time_path: Path = create_working_space(Path(NAME), override=True)

    assert time_path.exists()
    assert EXPECTED == get_relative(time_path)


def main() -> bool:
    test_name()
    test_create()
    return True
