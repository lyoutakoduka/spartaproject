#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shutil import unpack_archive
from tempfile import TemporaryDirectory
from typing import Callable

from context.default.integer_context import Ints2
from context.extension.decimal_context import (
    Decimal, Decs, set_decimal_context
)
from context.extension.path_context import Path, Paths, Paths2
from script.file.archive.compress_zip import CompressZip
from script.path.iterate_directory import walk_iterator
from script.path.modify.get_relative import get_relative_array
from script.path.temporary.create_temporary_tree import create_temporary_tree

set_decimal_context()


def _get_input_paths(walk_paths: Paths, temporary_root: Path) -> Paths:
    inputs: Paths = []
    tree_root: Path = Path(temporary_root, 'tree')

    for walk_path in walk_paths:
        inputs += [walk_path]
        parent_path: Path = walk_path.parent

        if tree_root != parent_path:
            inputs += [parent_path]

        if walk_path.is_dir():
            for path in walk_iterator(walk_path):
                inputs += [path]

    return inputs


def _get_output_paths(archived: Paths, temporary_root: Path) -> Paths:
    outputs: Paths = []
    extract_root: Path = Path(temporary_root, 'extract')

    for archived_path in archived:
        unpack_archive(archived_path, extract_dir=extract_root)

        for path in walk_iterator(extract_root):
            outputs += [path]

    return outputs


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


def _compare_compress_size(outputs: Paths, archived: Paths) -> None:
    file_sizes: Decs = [
        Decimal(str(sum([
            path.stat().st_size for path in paths if path.is_file()
        ])))
        for paths in [outputs, archived]
    ]

    assert Decimal('0.05') > (file_sizes[1] / file_sizes[0])


def _compare_archived_count(archived: Paths) -> None:
    assert 1 == len(archived)


def _get_sorted_paths(
    walk_paths: Paths, archived: Paths, temporary_root: Path
) -> Paths2:
    inputs: Paths = _get_input_paths(walk_paths, temporary_root)
    outputs: Paths = _get_output_paths(archived, temporary_root)

    return [sorted(list(set(paths))) for paths in [inputs, outputs]]


def _common_test(
    archived: Paths, temporary_root: Path, walk_paths: Paths
) -> Paths2:
    sorted_paths: Paths2 = _get_sorted_paths(
        walk_paths, archived, temporary_root
    )

    _compare_path_name(sorted_paths, temporary_root)
    _compare_file_size(sorted_paths)

    return sorted_paths


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_pass() -> None:
    def individual_test(temporary_root: Path) -> None:
        tree_root: Path = Path(temporary_root, 'tree')
        create_temporary_tree(tree_root)

        walk_paths: Paths = []
        compress_zip = CompressZip(Path(temporary_root, 'archive'))
        for path in walk_iterator(tree_root, directory=False, depth=1):
            compress_zip.compress_archive(path)
            walk_paths += [path]

        archived: Paths = compress_zip.close_archived()
        _common_test(archived, temporary_root, walk_paths)
        _compare_archived_count(archived)

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    def individual_test(temporary_root: Path) -> None:
        tree_root: Path = Path(temporary_root, 'tree')
        create_temporary_tree(tree_root, tree_deep=2)

        walk_paths: Paths = []
        compress_zip = CompressZip(Path(temporary_root, 'archive'))
        for path in walk_iterator(tree_root, file=False, depth=1):
            compress_zip.compress_archive(path)
            walk_paths += [path]

        archived: Paths = compress_zip.close_archived()
        _common_test(archived, temporary_root, walk_paths)
        _compare_archived_count(archived)

    _inside_temporary_directory(individual_test)


def test_tree() -> None:
    def individual_test(temporary_root: Path) -> None:
        tree_root: Path = Path(temporary_root, 'tree')
        create_temporary_tree(tree_root, tree_deep=3)

        walk_paths: Paths = []
        compress_zip = CompressZip(Path(temporary_root, 'archive'))
        for path in walk_iterator(tree_root, directory=False, suffix='txt'):
            compress_zip.compress_archive(path, archive_root=tree_root)
            walk_paths += [path]

        archived: Paths = compress_zip.close_archived()
        _common_test(archived, temporary_root, walk_paths)
        _compare_archived_count(archived)

    _inside_temporary_directory(individual_test)


def test_compress() -> None:
    def individual_test(temporary_root: Path) -> None:
        tree_root: Path = Path(temporary_root, 'tree')
        create_temporary_tree(tree_root, tree_weight=4)

        walk_paths: Paths = []
        compress_zip = CompressZip(
            Path(temporary_root, 'archive'), compress=True
        )
        for path in walk_iterator(tree_root, directory=False, suffix='json'):
            compress_zip.compress_archive(path)
            walk_paths += [path]

        archived: Paths = compress_zip.close_archived()
        sorted_paths: Paths2 = _common_test(
            archived, temporary_root, walk_paths,
        )
        _compare_archived_count(archived)
        _compare_compress_size(sorted_paths[-1], archived)

    _inside_temporary_directory(individual_test)


def test_id() -> None:
    ARCHIVE_NAME: str = 'test'

    def individual_test(temporary_root: Path) -> None:
        tree_root: Path = Path(temporary_root, 'tree')
        create_temporary_tree(tree_root)

        compress_zip = CompressZip(
            Path(temporary_root, 'archive'), archive_id=ARCHIVE_NAME
        )

        for path in walk_iterator(tree_root, directory=False, depth=1):
            compress_zip.compress_archive(path)

        archived: Paths = compress_zip.close_archived()
        archived_path = archived[0]
        assert ARCHIVE_NAME == archived_path.stem

    _inside_temporary_directory(individual_test)


def test_limit() -> None:
    def individual_test(temporary_root: Path) -> None:
        tree_root: Path = Path(temporary_root, 'tree')
        create_temporary_tree(tree_root, tree_deep=3)

        walk_paths: Paths = []
        compress_zip = CompressZip(
            Path(
                temporary_root,
                'archive'),
            limit_byte=256)
        for path in walk_iterator(tree_root, directory=False):
            compress_zip.compress_archive(path, archive_root=tree_root)
            walk_paths += [path]

        archived: Paths = compress_zip.close_archived()
        _common_test(archived, temporary_root, walk_paths)

    _inside_temporary_directory(individual_test)


def test_heavy() -> None:
    def individual_test(temporary_root: Path) -> None:
        tree_root: Path = Path(temporary_root, 'tree')
        create_temporary_tree(tree_root, tree_deep=3, tree_weight=2)

        walk_paths: Paths = []
        compress_zip = CompressZip(
            Path(
                temporary_root,
                'archive'),
            limit_byte=64)
        for path in walk_iterator(tree_root, directory=False, suffix='json'):
            compress_zip.compress_archive(path, archive_root=tree_root)
            walk_paths += [path]

        archived: Paths = compress_zip.close_archived()
        _common_test(archived, temporary_root, walk_paths)

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_pass()
    test_directory()
    test_tree()
    test_compress()
    test_id()
    test_limit()
    test_heavy()
    return True
