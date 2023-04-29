#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shutil import unpack_archive
from typing import Callable
from tempfile import TemporaryDirectory

from contexts.integer_context import Ints, Ints2
from contexts.path_context import Path, Paths, Paths2
from scripts.files.compress_zip import ArchiveZip
from scripts.paths.get_relative import path_array_relative
from scripts.paths.create_tmp_tree import create_tree
from scripts.paths.iterate_directory import walk_iterator


def _get_input_paths(walk_paths: Paths) -> Paths:
    inputs: Paths = []

    for walk_path in walk_paths:
        inputs += [walk_path]
        if walk_path.is_dir():
            for path in walk_iterator(walk_path):
                inputs += [path]

    return inputs


def _get_output_paths(result_raw: Paths, tmp_path: Path) -> Paths:
    outputs: Paths = []

    extract_root: Path = Path(tmp_path, 'extract')
    for result_path in result_raw:
        unpack_archive(result_path, extract_dir=extract_root)
        for path in walk_iterator(extract_root):
            outputs += [path]

    return outputs


def _compare_path_count(inputs: Paths, outputs: Paths) -> None:
    counts: Ints = [len(paths) for paths in [inputs, outputs]]
    assert counts[0] == counts[1]


def _compare_path_name(sorted_paths: Paths2, tmp_path: Path) -> None:
    relative_paths: Paths2 = [
        path_array_relative(paths, root_path=Path(tmp_path, directory))
        for directory, paths in zip(['tree', 'extract'], sorted_paths)
    ]

    assert relative_paths[0] == relative_paths[1]


def _compare_file_size(sorted_paths: Paths2) -> None:
    file_size_pair: Ints2 = [
        [path.stat().st_size for path in paths if path.is_file()]
        for paths in sorted_paths
    ]

    assert file_size_pair[0] == file_size_pair[1]


def _check_archive_result(
    result_raw: Paths,
    tmp_path: Path,
    walk_paths: Paths,
) -> None:

    inputs: Paths = _get_input_paths(walk_paths)
    outputs: Paths = _get_output_paths(result_raw, tmp_path)
    sorted_paths: Paths2 = [sorted(paths) for paths in [inputs, outputs]]

    _compare_path_count(inputs, outputs)
    _compare_path_name(sorted_paths, tmp_path)
    _compare_file_size(sorted_paths)


def _inside_tmp_directory(func: Callable[[Path, Path, Paths], Paths]) -> None:
    with TemporaryDirectory() as tmp_path:
        tree_root: Path = Path(tmp_path, 'tree')

        archive_root: Path = Path(tmp_path, 'archive')
        walk_paths: Paths = []
        _check_archive_result(
            func(archive_root, tree_root, walk_paths),
            Path(tmp_path), walk_paths,
        )


def test_simple() -> None:
    def make_tree(archive_root: Path, tree_root: Path, walk_paths: Paths) -> Paths:
        archive_zip = ArchiveZip(archive_root)
        create_tree(tree_root)

        for path in walk_iterator(tree_root, directory=False, depth=1):
            archive_zip.add_archive(path)
            walk_paths += [path]

        return archive_zip.result()

    _inside_tmp_directory(make_tree)


def main() -> bool:
    test_simple()
    return True
