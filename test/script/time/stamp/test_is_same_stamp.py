#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to get latest date time of file or directory as time object."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.extension.time_context import TimePair, TimePair2
from pyspartaproj.script.path.iterate_directory import walk_iterator
from pyspartaproj.script.path.modify.get_relative import get_relative
from pyspartaproj.script.path.temporary.create_temporary_tree import (
    create_temporary_tree,
)
from pyspartaproj.script.time.path.get_timestamp import get_directory_latest
from pyspartaproj.script.time.stamp.is_same_stamp import is_same_stamp


def _get_directory_latest(path: Path, access: bool) -> TimePair:
    return get_directory_latest(walk_iterator(path), access=access)


def _get_relative_text(path_text: str, root_path: Path) -> str:
    return str(get_relative(Path(path_text), root_path=root_path))


def _get_relative_latest(path: Path, access: bool = False) -> TimePair:
    return {
        _get_relative_text(path_text, path): time
        for path_text, time in _get_directory_latest(path, access).items()
    }


def _is_access(group: str) -> bool:
    return "access" == group


def _get_stamp_pair(stamp_root: Path) -> TimePair2:
    return {
        group: _get_relative_latest(stamp_root, access=_is_access(group))
        for group in ["update", "access"]
    }


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_same() -> None:
    """Test to compare 2 dictionaries about latest date time you got."""

    def individual_test(temporary_root: Path) -> None:
        stamp_pair: TimePair2 = _get_stamp_pair(
            create_temporary_tree(Path(temporary_root, "tree"))
        )

        assert is_same_stamp(stamp_pair["update"], stamp_pair["access"])

    _inside_temporary_directory(individual_test)
