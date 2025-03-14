#!/usr/bin/env python

"""Test module to create temporary working space including date time string."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.custom.type_context import Type
from pyspartalib.script.directory.working.working_date_time import (
    create_working_space,
)
from pyspartalib.script.path.modify.current.get_relative import get_relative
from pyspartalib.script.time.directory.get_time_path import (
    get_initial_time_path,
)


def _difference_error(result: Type, expected: Type) -> None:
    if expected != result:
        raise ValueError


def _no_exists_error(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError


def _compare_time_path(result: Path) -> None:
    _difference_error(get_initial_time_path(), result)


def test_create() -> None:
    """Test to create temporary working space including date time string."""
    with TemporaryDirectory() as temporary_directory:
        temporary_path: Path = Path(temporary_directory)
        time_path: Path = create_working_space(temporary_path, override=True)

        _no_exists_error(time_path)
        _compare_time_path(get_relative(time_path, root_path=temporary_path))
