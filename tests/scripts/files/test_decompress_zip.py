#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import chain
from shutil import make_archive
from tempfile import TemporaryDirectory
from typing import Callable

from contexts.integer_context import Ints2
from contexts.path_context import Path, Paths, Paths2
from contexts.time_context import datetime, Times2
from scripts.files.compress_zip import CompressZip
from scripts.files.decompress_zip import DecompressZip
from scripts.paths.create_temporary_tree import create_tree
from scripts.paths.evacuate_trash import TrashBox
from scripts.paths.get_relative import get_relative_array
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
        get_relative_array(paths, root_path=Path(tmp_root, directory))
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


def _compress_to_decompress(tmp_root: Path) -> None:
    tree_root: Path = Path(tmp_root, 'tree')
    archived: Path = Path(make_archive(
        str(Path(tmp_root, *['archive'] * 2)),
        format='zip',
        root_dir=str(tree_root)
    ))

    decompress_zip = DecompressZip(Path(tmp_root, 'extract'))
    decompress_zip.decompress_archive(archived)


def _inside_tmp_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as tmp_path:
        function(Path(tmp_path))


def test_directory() -> None:
    def individual_test(tmp_root: Path) -> None:
        tree_root: Path = Path(tmp_root, 'tree')
        create_tree(tree_root, tree_deep=3)

        trash_box = TrashBox()
        for path in walk_iterator(tree_root, directory=False):
            trash_box.throw_away_trash(path)

        _compress_to_decompress(tmp_root)
        _common_test(tmp_root)

    _inside_tmp_directory(individual_test)


def test_tree() -> None:
    def individual_test(tmp_root: Path) -> None:
        tree_root: Path = Path(tmp_root, 'tree')
        create_tree(tree_root, tree_deep=2)

        trash_box = TrashBox()
        for path in walk_iterator(tree_root, file=False):
            if 0 == len(list(walk_iterator(path, depth=1))):
                trash_box.throw_away_trash(path)

        _compress_to_decompress(tmp_root)
        _common_test(tmp_root)

    _inside_tmp_directory(individual_test)


def test_limit() -> None:
    def individual_test(tmp_root: Path) -> None:
        tree_root: Path = Path(tmp_root, 'tree')
        create_tree(tree_root, tree_deep=5)

        compress_zip = CompressZip(Path(tmp_root, 'archive'), limit_byte=200)
        for path in walk_iterator(tree_root):
            compress_zip.compress_archive(path)

        archived_paths: Paths = compress_zip.close_archived()
        decompress_zip = DecompressZip(Path(tmp_root, 'extract'))
        for path in decompress_zip.sequential_archives(archived_paths[0]):
            decompress_zip.decompress_archive(path)

        _common_test(tmp_root)

    _inside_tmp_directory(individual_test)


def test_timestamp() -> None:
    EXPECTED: str = '2023-04-15T20:09:30.936886+00:00'
    expected: datetime = datetime.fromisoformat(EXPECTED)

    def individual_test(tmp_root: Path) -> None:
        tree_root: Path = Path(tmp_root, 'tree')
        create_tree(tree_root)

        compress_zip = CompressZip(Path(tmp_root, 'archive'))
        for path in walk_iterator(tree_root):
            if path.is_file():
                set_latest(path, expected)
            compress_zip.compress_archive(path)

        decompress_zip = DecompressZip(Path(tmp_root, 'extract'))
        for path in compress_zip.close_archived():
            decompress_zip.decompress_archive(path)

        sorted_paths: Paths2 = _common_test(tmp_root)
        _compare_timestamp(sorted_paths, expected)

    _inside_tmp_directory(individual_test)


def main() -> bool:
    test_directory()
    test_tree()
    test_limit()
    test_timestamp()
    return True
