#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from scripts.paths.get_relative import get_relative
from scripts.paths.working_space import current_working_space


def test_pass() -> None:
    NAME: str = '.trash'
    EXPECTED: Path = Path(
        NAME, '2023', '04', '01', '00', '00', '00', '000000'
    )

    time_path: Path = current_working_space(Path(NAME), override=True)

    assert time_path.exists()
    assert EXPECTED == get_relative(time_path)


def main() -> bool:
    test_pass()
    return True
