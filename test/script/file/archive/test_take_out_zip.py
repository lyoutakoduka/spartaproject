#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to take out directory from inside of archive as archive."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.extension.path_context import PathPair, Paths, Paths2
from pyspartaproj.context.typed.user_context import ArchiveStatus
from pyspartaproj.script.directory.create_directory import create_directory
from pyspartaproj.script.file.archive.compress_zip import CompressZip
from pyspartaproj.script.file.archive.take_out_zip import take_out_zip
from pyspartaproj.script.path.iterate_directory import walk_iterator
from pyspartaproj.script.path.modify.get_absolute import get_absolute_array
from pyspartaproj.script.path.modify.get_relative import get_relative_array
from pyspartaproj.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)


def _create_working_directory(temporary_root: Path) -> PathPair:
    return {
        name: create_directory(Path(temporary_root, name))
        for name in ["source", "archive"]
    }


def _inside_temporary_directory(function: Callable[[PathPair], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(_create_working_directory(Path(temporary_path)))


def _compress_test_archive(working: PathPair, target_paths: Paths) -> Path:
    compress_zip = CompressZip(working["archive"], archive_id="archive")

    for target_path in target_paths:
        compress_zip.compress_archive(target_path)

    return compress_zip.close_archived()[0]


def _create_compleat_archive(working: PathPair) -> ArchiveStatus:
    return {
        "archive": _compress_test_archive(
            working, [create_temporary_file(working["source"])]
        ),
        "expected": [],
    }


def _create_empty_archive(working: PathPair) -> ArchiveStatus:
    return {
        "archive": _compress_test_archive(
            working, [create_directory(Path(working["source"], "directory"))]
        ),
        "expected": [],
    }


def _get_relative_expected(working: PathPair, target_paths: Paths) -> Paths:
    return get_relative_array(target_paths, root_path=working["source"])


def _create_single_archive(working: PathPair) -> ArchiveStatus:
    directory_root: Path = create_directory(
        Path(working["source"], "directory")
    )
    file_path: Path = create_temporary_file(directory_root)

    return {
        "archive": _compress_test_archive(working, [directory_root]),
        "expected": _get_relative_expected(
            working, [directory_root, file_path]
        ),
    }


def _replace_path_root(decompressed_root: Path, archive_root: Path) -> Paths:
    return get_absolute_array(
        get_relative_array(
            list(walk_iterator(decompressed_root)),
            root_path=decompressed_root,
        ),
        root_path=archive_root,
    )


def _common_test(archive_status: ArchiveStatus) -> None:
    paths_pair: Paths2 = [
        take_out_zip(archive_status["archive"]),
        archive_status["expected"],
    ]

    assert 1 == len(set([str(sorted(paths)) for paths in paths_pair]))


def test_compleat() -> None:
    """Take out directory from inside of archive as archive.

    But, directory doesn't exist in inside of archive.
    """

    def individual_test(working: PathPair) -> None:
        _common_test(_create_compleat_archive(working))

    _inside_temporary_directory(individual_test)


def test_empty() -> None:
    def individual_test(working: PathPair) -> None:
        _common_test(_create_empty_archive(working))

    _inside_temporary_directory(individual_test)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_compleat()
    test_empty()
    return True
