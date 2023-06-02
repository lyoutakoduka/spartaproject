#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import chain
from shutil import make_archive
from tempfile import TemporaryDirectory
from typing import Callable

from context.default.integer_context import Ints2
from context.extension.path_context import Path, Paths, Paths2
from context.extension.time_context import datetime, Times2
from script.file.archive.compress_zip import CompressZip
from script.file.archive.decompress_zip import DecompressZip
from script.path.iterate_directory import walk_iterator
from script.path.modify.get_relative import get_relative_array
from script.path.safe.safe_trash import SafeTrash
from script.path.temporary.create_temporary_tree import create_temporary_tree
from script.time.stamp.get_timestamp import get_latest
from script.time.stamp.set_timestamp import set_latest


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
        for directory, paths in zip(['tree', 'extract'], sorted_paths)
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
        for directory in ['tree', 'extract']
    ]


def _common_test(temporary_root: Path) -> Paths2:
    sorted_paths: Paths2 = _get_sorted_paths(temporary_root)

    _compare_path_name(sorted_paths, temporary_root)
    _compare_file_size(sorted_paths)

    return sorted_paths


def _compress_to_decompress(temporary_root: Path) -> None:
    tree_root: Path = Path(temporary_root, 'tree')
    archived: Path = Path(make_archive(
        str(Path(temporary_root, *['archive'] * 2)),
        format='zip',
        root_dir=str(tree_root)
    ))

    decompress_zip = DecompressZip(Path(temporary_root, 'extract'))
    decompress_zip.decompress_archive(archived)


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_directory() -> None:
    def individual_test(temporary_root: Path) -> None:
        tree_root: Path = Path(temporary_root, 'tree')
        create_temporary_tree(tree_root, tree_deep=3)

        trash_box = SafeTrash()
        for path in walk_iterator(tree_root, directory=False):
            trash_box.throw_away_trash(path)

        _compress_to_decompress(temporary_root)
        _common_test(temporary_root)

    _inside_temporary_directory(individual_test)


def test_tree() -> None:
    def individual_test(temporary_root: Path) -> None:
        tree_root: Path = Path(temporary_root, 'tree')
        create_temporary_tree(tree_root, tree_deep=2)

        trash_box = SafeTrash()
        for path in walk_iterator(tree_root, file=False):
            if 0 == len(list(walk_iterator(path, depth=1))):
                trash_box.throw_away_trash(path)

        _compress_to_decompress(temporary_root)
        _common_test(temporary_root)

    _inside_temporary_directory(individual_test)


def test_limit() -> None:
    def individual_test(temporary_root: Path) -> None:
        tree_root: Path = Path(temporary_root, 'tree')
        create_temporary_tree(tree_root, tree_deep=5)

        compress_zip = CompressZip(
            Path(temporary_root, 'archive'), limit_byte=200
        )
        for path in walk_iterator(tree_root):
            compress_zip.compress_archive(path)

        archived_paths: Paths = compress_zip.close_archived()
        decompress_zip = DecompressZip(Path(temporary_root, 'extract'))
        for path in decompress_zip.sequential_archives(archived_paths[0]):
            decompress_zip.decompress_archive(path)

        _common_test(temporary_root)

    _inside_temporary_directory(individual_test)


def test_timestamp() -> None:
    EXPECTED: str = '2023-04-15T20:09:30.936886+00:00'
    expected: datetime = datetime.fromisoformat(EXPECTED)

    def individual_test(temporary_root: Path) -> None:
        tree_root: Path = Path(temporary_root, 'tree')
        create_temporary_tree(tree_root)

        compress_zip = CompressZip(Path(temporary_root, 'archive'))
        for path in walk_iterator(tree_root):
            if path.is_file():
                set_latest(path, expected)
            compress_zip.compress_archive(path)

        decompress_zip = DecompressZip(Path(temporary_root, 'extract'))
        for path in compress_zip.close_archived():
            decompress_zip.decompress_archive(path)

        sorted_paths: Paths2 = _common_test(temporary_root)
        _compare_timestamp(sorted_paths, expected)

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_directory()
    test_tree()
    test_limit()
    test_timestamp()
    return True
