#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from script.directory.create_directory_working import create_working_space
from script.path.modify.get_relative import get_relative


def test_create() -> None:
    NAME: str = '.trash'
    EXPECTED: Path = Path(
        NAME, '2023', '04', '01', '00', '00', '00', '000000'
    )

    time_path: Path = create_working_space(Path(NAME), override=True)

    assert time_path.exists()
    assert EXPECTED == get_relative(time_path)


def main() -> bool:
    test_create()
    return True
