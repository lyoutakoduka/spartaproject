#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to decompress archive which is zip format."""

from itertools import chain
from pathlib import Path
from shutil import make_archive
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.default.integer_context import Ints2
from pyspartaproj.context.extension.path_context import Paths2
from pyspartaproj.context.extension.time_context import Times2, datetime
from pyspartaproj.script.file.archive.compress_zip import CompressZip
from pyspartaproj.script.file.archive.decompress_zip import DecompressZip
from pyspartaproj.script.path.iterate_directory import walk_iterator
from pyspartaproj.script.path.modify.get_relative import get_relative_array
from pyspartaproj.script.path.safe.safe_trash import SafeTrash
from pyspartaproj.script.path.temporary.create_temporary_tree import (
    create_temporary_tree,
)
from pyspartaproj.script.time.stamp.get_timestamp import get_latest
from pyspartaproj.script.time.stamp.set_timestamp import set_latest


def _compare_timestamp(sorted_paths: Paths2, expected: datetime) -> None:
    times_pair: Times2 = [
        [get_latest(path) for path in paths if path.is_file()]
        for paths in sorted_paths
    ]
    assert times_pair[0] == times_pair[1]

    times = list(set(chain(*times_pair)))
    assert 1 == len(times)

    assert expected == times[0]


def _compare_path_name(sorted_paths: Paths2, temporary_root: Path) -> None:
    relative_paths: Paths2 = [
        get_relative_array(paths, root_path=Path(temporary_root, directory))
        for directory, paths in zip(["tree", "extract"], sorted_paths)
    ]

    assert relative_paths[0] == relative_paths[1]


def _compare_file_size(sorted_paths: Paths2) -> None:
    file_size_pair: Ints2 = [
        [path.stat().st_size for path in paths if path.is_file()]
        for paths in sorted_paths
    ]

    assert file_size_pair[0] == file_size_pair[1]


def _get_sorted_paths(temporary_root: Path) -> Paths2:
    return [
        sorted(list(walk_iterator(Path(temporary_root, directory))))
        for directory in ["tree", "extract"]
    ]


def _common_test(temporary_root: Path) -> Paths2:
    sorted_paths: Paths2 = _get_sorted_paths(temporary_root)

    _compare_path_name(sorted_paths, temporary_root)
    _compare_file_size(sorted_paths)

    return sorted_paths


def _create_archive(temporary_root: Path, tree_root: Path) -> Path:
    return Path(
        make_archive(
            str(Path(temporary_root, *["archive"] * 2)),
            format="zip",
            root_dir=str(tree_root),
        )
    )


def _compress_to_decompress(temporary_root: Path, tree_root: Path) -> None:
    DecompressZip(Path(temporary_root, "extract")).decompress_archive(
        _create_archive(temporary_root, tree_root)
    )


def _inside_temporary_directory(
    function: Callable[[Path, Path], None]
) -> None:
    with TemporaryDirectory() as temporary_path:
        temporary_root: Path = Path(temporary_path)
        function(temporary_root, Path(temporary_root, "tree"))


def test_file() -> None:
    """Test to decompress archive including only files."""

    def individual_test(temporary_root: Path, tree_root: Path) -> None:
        safe_trash = SafeTrash()

        for path in walk_iterator(
            create_temporary_tree(Path(temporary_root, "tree"), tree_deep=2),
            file=False,
        ):
            if 0 == len(list(walk_iterator(path, depth=1))):
                safe_trash.trash(path)

        _compress_to_decompress(temporary_root, tree_root)
        _common_test(temporary_root)

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    """Test to decompress archive including only directories."""

    def individual_test(temporary_root: Path, tree_root: Path) -> None:
        safe_trash = SafeTrash()

        for path in walk_iterator(
            create_temporary_tree(tree_root, tree_deep=3),
            directory=False,
        ):
            safe_trash.trash(path)

        _compress_to_decompress(temporary_root, tree_root)
        _common_test(temporary_root)

    _inside_temporary_directory(individual_test)


def test_status() -> None:
    """Test to get status of compression format from archive."""

    def individual_test(temporary_root: Path, tree_root: Path) -> None:
        create_temporary_tree(tree_root)

        assert not DecompressZip(temporary_root).is_lzma_archive(
            _create_archive(temporary_root, tree_root)
        )

    _inside_temporary_directory(individual_test)


def test_limit() -> None:
    """Test to decompress sequential archives."""

    def individual_test(temporary_root: Path, tree_root: Path) -> None:
        compress_zip = CompressZip(
            Path(temporary_root, "archive"), limit_byte=200
        )

        for path in walk_iterator(
            create_temporary_tree(tree_root, tree_deep=5)
        ):
            compress_zip.compress_archive(path)

        decompress_zip = DecompressZip(Path(temporary_root, "extract"))

        for path in decompress_zip.sequential_archives(
            compress_zip.close_archived()[0]
        ):
            decompress_zip.decompress_archive(path)

        _common_test(temporary_root)

    _inside_temporary_directory(individual_test)


def test_timestamp() -> None:
    """Test for timestamp consistency of contents in archive."""
    expected: datetime = datetime.fromisoformat(
        "2023-04-15T20:09:30.936886+00:00"
    )

    def individual_test(temporary_root: Path, tree_root: Path) -> None:
        compress_zip = CompressZip(Path(temporary_root, "archive"))

        for path in walk_iterator(create_temporary_tree(tree_root)):
            if path.is_file():
                set_latest(path, expected)

            compress_zip.compress_archive(path)

        decompress_zip = DecompressZip(Path(temporary_root, "extract"))

        for path in compress_zip.close_archived():
            decompress_zip.decompress_archive(path)

        _compare_timestamp(_common_test(temporary_root), expected)

    _inside_temporary_directory(individual_test)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_file()
    test_directory()
    test_status()
    test_limit()
    test_timestamp()
    return True
