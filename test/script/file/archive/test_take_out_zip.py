#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to take out directory from inside of archive as archive."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.context.extension.path_context import PathPair, Paths
from pyspartaproj.context.typed.user_context import ArchiveStatus
from pyspartaproj.script.directory.create_directory import create_directory
from pyspartaproj.script.file.archive.compress_zip import CompressZip
from pyspartaproj.script.file.archive.edit_zip import EditZip
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


def _compress_test_archive(working: PathPair) -> Path:
    compress_zip = CompressZip(working["archive"], archive_id="archive")

    for target_path in walk_iterator(working["source"], depth=1):
        compress_zip.compress_archive(target_path)

    return compress_zip.close_archived()[0]


def _get_relative_paths(working: PathPair, target_paths: Paths) -> Paths:
    return get_relative_array(target_paths, root_path=working["source"])


def _get_relative_archive(archive_path: Path) -> Paths:
    edit_zip = EditZip(archive_path)
    root_path: Path = edit_zip.get_decompressed_root()

    return get_relative_array(
        list(walk_iterator(root_path)), root_path=root_path
    )


def _add_temporary_files(directory_root: Path, file_names: Strs) -> Paths:
    return [
        create_temporary_file(directory_root, file_name=file_name)
        for file_name in file_names
    ]


def _add_temporary_directory(
    directory_root: Path, directory_names: Strs
) -> Paths:
    return [
        create_directory(Path(directory_root, directory_name))
        for directory_name in directory_names
    ]


def _create_archive_shared(
    working: PathPair,
    take_paths: Paths,
    rest_paths: Paths,
) -> ArchiveStatus:
    return {
        "archive": _compress_test_archive(working),
        "take": _get_relative_paths(working, take_paths),
        "rest": _get_relative_paths(working, rest_paths),
    }


def _create_archive_compleat(working: PathPair) -> ArchiveStatus:
    return _create_archive_shared(
        working, [], [create_temporary_file(working["source"])]
    )


def _create_archive_empty(working: PathPair) -> ArchiveStatus:
    return _create_archive_shared(
        working, [], [create_directory(Path(working["source"], "directory"))]
    )


def _create_archive_single(working: PathPair) -> ArchiveStatus:
    directory_root: Path = create_directory(
        Path(working["source"], "directory")
    )

    return _create_archive_shared(
        working, [directory_root, create_temporary_file(directory_root)], []
    )


def _create_archive_multiple(working: PathPair) -> ArchiveStatus:
    directory_root: Path = create_directory(
        Path(working["source"], "directory")
    )
    file_paths: Paths = _add_temporary_files(
        directory_root, ["first", "second", "third"]
    )

    return _create_archive_shared(working, [directory_root] + file_paths, [])


def _create_archive_mix(working: PathPair) -> ArchiveStatus:
    file_root: Path = working["source"]
    directory_root: Path = create_directory(Path(file_root, "directory"))

    return _create_archive_shared(
        working,
        [directory_root, create_temporary_file(directory_root)],
        [create_temporary_file(file_root)],
    )


def _create_archive_list(working: PathPair) -> ArchiveStatus:
    file_paths: Paths = []

    for archive_path in _add_temporary_directory(
        working["source"], ["first", "second", "third"]
    ):
        file_paths += [archive_path, create_temporary_file(archive_path)]

    return _create_archive_shared(working, file_paths, [])


def _replace_path_root(archive_path: Path, archive_root: Path) -> Paths:
    return get_absolute_array(
        _get_relative_archive(archive_path), root_path=archive_root
    )


def _get_took_out(archive_path: Path) -> Paths:
    archive_root: Path = Path(archive_path.stem)
    file_paths: Paths = _replace_path_root(archive_path, archive_root)

    return [archive_root] + file_paths


def _get_took_out_list(archive_paths: Paths) -> Paths:
    file_paths: Paths = []

    for archive_path in archive_paths:
        file_paths += _get_took_out(archive_path)

    return file_paths


def _compare_path_test(left: Paths, right: Paths) -> None:
    assert 1 == len(set([str(sorted(paths)) for paths in [left, right]]))


def _compare_took_out(archive_status: ArchiveStatus) -> None:
    _compare_path_test(
        _get_took_out_list(take_out_zip(archive_status["archive"])),
        archive_status["take"],
    )


def _compare_rest(archive_status: ArchiveStatus) -> None:
    _compare_path_test(
        _get_relative_archive(archive_status["archive"]),
        archive_status["rest"],
    )


def _common_test(archive_status: ArchiveStatus) -> None:
    _compare_took_out(archive_status)
    _compare_rest(archive_status)


def test_compleat() -> None:
    """Take out directory from inside of archive as archive.

    But, directory doesn't exist in inside of archive.
    """

    def individual_test(working: PathPair) -> None:
        _common_test(_create_archive_compleat(working))

    _inside_temporary_directory(individual_test)


def test_empty() -> None:
    def individual_test(working: PathPair) -> None:
        _common_test(_create_archive_empty(working))

    _inside_temporary_directory(individual_test)


def test_single() -> None:
    def individual_test(working: PathPair) -> None:
        _common_test(_create_archive_single(working))

    _inside_temporary_directory(individual_test)


def test_multiple() -> None:
    def individual_test(working: PathPair) -> None:
        _common_test(_create_archive_multiple(working))

    _inside_temporary_directory(individual_test)


def test_mix() -> None:
    def individual_test(working: PathPair) -> None:
        _common_test(_create_archive_mix(working))

    _inside_temporary_directory(individual_test)


def test_list() -> None:
    def individual_test(working: PathPair) -> None:
        _common_test(_create_archive_list(working))

    _inside_temporary_directory(individual_test)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_compleat()
    test_empty()
    test_single()
    test_multiple()
    test_mix()
    test_list()
    return True
