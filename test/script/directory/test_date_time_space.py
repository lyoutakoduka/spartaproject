#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to create temporary working space including date time string."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartaproj.script.directory.date_time_space import create_working_space
from pyspartaproj.script.path.modify.get_relative import get_relative
from pyspartaproj.script.time.path.get_time_path import get_initial_time_path


def _compare_time_path(result: Path) -> None:
    assert get_initial_time_path() == result


def test_create() -> None:
    """Test to create temporary working space including date time string."""
    with TemporaryDirectory() as temporary_directory:
        temporary_path: Path = Path(temporary_directory)
        time_path: Path = create_working_space(temporary_path, override=True)

        assert time_path.exists()

        _compare_time_path(get_relative(time_path, root_path=temporary_path))
