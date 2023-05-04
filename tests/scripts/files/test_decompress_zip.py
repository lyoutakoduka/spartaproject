#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shutil import make_archive
from typing import Callable
from tempfile import TemporaryDirectory
from itertools import chain

from contexts.integer_context import Ints2
from contexts.path_context import Path, Paths, Paths2
from contexts.time_context import datetime, Times2
from scripts.files.compress_zip import CompressZip
from scripts.files.decompress_zip import DecompressZip
from scripts.paths.get_relative import path_array_relative
from scripts.paths.create_tmp_tree import create_tree
from scripts.paths.iterate_directory import walk_iterator
from scripts.times.get_timestamp import get_latest
from scripts.times.set_timestamp import set_latest


def _compare_timestamp(sorted_paths: Paths2, expected: datetime) -> None:
    times_pair: Times2 = [
        [get_latest(path) for path in paths if path.is_file()]
        for paths in sorted_paths
    ]
    assert times_pair[0] == times_pair[1]

    times = list(set(chain(*times_pair)))
    assert 1 == len(times)

    assert expected == times[0]


def _compare_path_name(sorted_paths: Paths2, tmp_root: Path) -> None:
    relative_paths: Paths2 = [
        path_array_relative(paths, root_path=Path(tmp_root, directory))
        for directory, paths in zip(['tree', 'extract'], sorted_paths)
    ]

    assert relative_paths[0] == relative_paths[1]


def _compare_file_size(sorted_paths: Paths2) -> None:
    file_size_pair: Ints2 = [
        [path.stat().st_size for path in paths if path.is_file()]
        for paths in sorted_paths
    ]

    assert file_size_pair[0] == file_size_pair[1]


def _get_sorted_paths(tmp_root: Path) -> Paths2:
    return [
        sorted(list(walk_iterator(Path(tmp_root, directory))))
        for directory in ['tree', 'extract']
    ]


def _common_test(tmp_root: Path) -> Paths2:
    sorted_paths: Paths2 = _get_sorted_paths(tmp_root)

    _compare_path_name(sorted_paths, tmp_root)
    _compare_file_size(sorted_paths)

    return sorted_paths


def _inside_tmp_directory(func: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as tmp_path:
        create_tree(Path(tmp_path, 'tree'), tree_deep=3, tree_weight=3)
        func(Path(tmp_path))


def test_outside() -> None:
    def individual_test(tmp_root: Path) -> None:
        archived: Path = Path(make_archive(
            str(Path(tmp_root, *['archive'] * 2)),
            format='zip',
            root_dir=str(Path(tmp_root, 'tree'))
        ))

        decompress_zip = DecompressZip(Path(tmp_root, 'extract'))
        decompress_zip.decompress_archive(archived)

        _common_test(tmp_root)

    _inside_tmp_directory(individual_test)


def test_timestamp() -> None:
    EXPECTED: str = '2023-04-15T20:09:30.936886+00:00'
    expected: datetime = datetime.fromisoformat(EXPECTED)

    def individual_test(tmp_root: Path) -> None:
        walk_paths: Paths = list(walk_iterator(Path(tmp_root, 'tree')))

        for path in walk_paths:
            if path.is_file():
                set_latest(path, expected)

        compress_zip = CompressZip(Path(tmp_root, 'archive'), compress=True)
        for path in walk_paths:
            compress_zip.add_archive(path)

        decompress_zip = DecompressZip(Path(tmp_root, 'extract'))
        for path in compress_zip.close_archived():
            decompress_zip.decompress_archive(path)

        sorted_paths: Paths2 = _common_test(tmp_root)
        _compare_timestamp(sorted_paths, expected)

    _inside_tmp_directory(individual_test)


def main() -> bool:
    test_outside()
    test_timestamp()
    return True
