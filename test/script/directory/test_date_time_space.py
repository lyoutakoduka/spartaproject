#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to create temporary working space including date time string."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartaproj.script.directory.date_time_space import (
    create_working_space,
    get_working_space,
)
from pyspartaproj.script.path.modify.get_relative import get_relative


def test_name() -> None:
    """Test to get path including string of current date time."""
    expected: Path = Path("2023", "04", "01", "00", "00", "00", "000000")

    assert expected == get_working_space(override=True)


def test_create() -> None:
    """Test to create temporary working space including date time string."""
    expected: Path = Path("2023", "04", "01", "00", "00", "00", "000000")

    with TemporaryDirectory() as temporary_directory:
        temporary_path: Path = Path(temporary_directory)
        time_path: Path = create_working_space(temporary_path, override=True)

        assert time_path.exists()
        assert expected == get_relative(time_path, root_path=temporary_path)
