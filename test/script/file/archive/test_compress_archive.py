#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to compress file or directory by archive format."""

from decimal import Decimal
from pathlib import Path
from shutil import unpack_archive
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.default.integer_context import Ints2
from pyspartaproj.context.extension.decimal_context import Decs
from pyspartaproj.context.extension.path_context import Paths, Paths2
from pyspartaproj.script.decimal.initialize_decimal import initialize_decimal
from pyspartaproj.script.file.archive.compress_archive import CompressArchive
from pyspartaproj.script.path.iterate_directory import walk_iterator
from pyspartaproj.script.path.modify.get_relative import get_relative_array
from pyspartaproj.script.path.status.get_statistic import (
    get_file_size,
    get_file_size_array,
)
from pyspartaproj.script.path.temporary.create_temporary_tree import (
    create_temporary_tree,
)

initialize_decimal()


def _get_input_paths(walk_paths: Paths, temporary_root: Path) -> Paths:
    inputs: Paths = []
    tree_root: Path = Path(temporary_root, "tree")

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
    extract_root: Path = Path(temporary_root, "extract")

    for archived_path in archived:
        unpack_archive(archived_path, extract_dir=extract_root)

        for path in walk_iterator(extract_root):
            outputs += [path]

    return outputs


def _compare_path_name(sorted_paths: Paths2, temporary_root: Path) -> None:
    relative_paths: Paths2 = [
        get_relative_array(paths, root_path=Path(temporary_root, directory))
        for directory, paths in zip(["tree", "extract"], sorted_paths)
    ]

    assert relative_paths[0] == relative_paths[1]


def _compare_file_size(sorted_paths: Paths2) -> None:
    file_size_pair: Ints2 = [
        get_file_size_array(paths) for paths in sorted_paths
    ]

    assert file_size_pair[0] == file_size_pair[1]


def _compare_compress_size(outputs: Paths, archived: Paths) -> None:
    file_sizes: Decs = [
        Decimal(str(sum(get_file_size_array(paths))))
        for paths in [outputs, archived]
    ]

    assert Decimal("0.05") > (file_sizes[1] / file_sizes[0])


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


def _confirm_empty_archive(archive_paths: Paths) -> None:
    _compare_archived_count(archive_paths)

    expected: int = 22
    assert expected == get_file_size(archive_paths[0])


def test_empty() -> None:
    """Test to create empty archive."""

    def individual_test(temporary_root: Path) -> None:
        _confirm_empty_archive(
            CompressArchive(Path(temporary_root, "archive")).close_archived()
        )

    _inside_temporary_directory(individual_test)


def test_file() -> None:
    """Test to compress multiple files."""

    def individual_test(temporary_root: Path) -> None:
        walk_paths: Paths = []
        compress_archive = CompressArchive(Path(temporary_root, "archive"))

        for path in walk_iterator(
            create_temporary_tree(Path(temporary_root, "tree")),
            directory=False,
            depth=1,
        ):
            compress_archive.compress_archive(path)
            walk_paths += [path]

        archived: Paths = compress_archive.close_archived()
        _common_test(archived, temporary_root, walk_paths)
        _compare_archived_count(archived)

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    """Test to compress multiple empty directories."""

    def individual_test(temporary_root: Path) -> None:
        walk_paths: Paths = []
        compress_archive = CompressArchive(Path(temporary_root, "archive"))

        for path in walk_iterator(
            create_temporary_tree(Path(temporary_root, "tree"), tree_deep=2),
            file=False,
            depth=1,
        ):
            compress_archive.compress_archive(path)
            walk_paths += [path]

        archived: Paths = compress_archive.close_archived()
        _common_test(archived, temporary_root, walk_paths)
        _compare_archived_count(archived)

    _inside_temporary_directory(individual_test)


def test_tree() -> None:
    """Test to compress multiple files and directories."""

    def individual_test(temporary_root: Path) -> None:
        tree_root: Path = create_temporary_tree(
            Path(temporary_root, "tree"), tree_deep=3
        )

        walk_paths: Paths = []
        compress_archive = CompressArchive(Path(temporary_root, "archive"))

        for path in walk_iterator(tree_root, directory=False, suffix="txt"):
            compress_archive.compress_archive(path, archive_root=tree_root)
            walk_paths += [path]

        archived: Paths = compress_archive.close_archived()
        _common_test(archived, temporary_root, walk_paths)
        _compare_archived_count(archived)

    _inside_temporary_directory(individual_test)


def test_compress() -> None:
    """Test to compress multiple files by LZMA format."""

    def individual_test(temporary_root: Path) -> None:
        walk_paths: Paths = []
        compress_archive = CompressArchive(
            Path(temporary_root, "archive"), compress=True
        )

        for path in walk_iterator(
            create_temporary_tree(Path(temporary_root, "tree"), tree_weight=4),
            directory=False,
            suffix="json",
        ):
            compress_archive.compress_archive(path)
            walk_paths += [path]

        archived: Paths = compress_archive.close_archived()
        sorted_paths: Paths2 = _common_test(
            archived,
            temporary_root,
            walk_paths,
        )
        _compare_archived_count(archived)
        _compare_compress_size(sorted_paths[-1], archived)

    _inside_temporary_directory(individual_test)


def test_id() -> None:
    """Test to compress multiple files by specific archive name."""
    archive_name: str = "test"

    def individual_test(temporary_root: Path) -> None:
        compress_archive = CompressArchive(
            Path(temporary_root, "archive"), archive_id=archive_name
        )

        for path in walk_iterator(
            create_temporary_tree(Path(temporary_root, "tree")),
            directory=False,
            depth=1,
        ):
            compress_archive.compress_archive(path)

        archived_path = compress_archive.close_archived()[0]
        assert archive_name == archived_path.stem

    _inside_temporary_directory(individual_test)


def test_limit() -> None:
    """Test to compress multiple files and directories dividedly."""

    def individual_test(temporary_root: Path) -> None:
        tree_root: Path = create_temporary_tree(
            Path(temporary_root, "tree"), tree_deep=3
        )

        walk_paths: Paths = []
        compress_archive = CompressArchive(
            Path(temporary_root, "archive"), limit_byte=256
        )
        for path in walk_iterator(tree_root, directory=False):
            compress_archive.compress_archive(path, archive_root=tree_root)
            walk_paths += [path]

        _common_test(
            compress_archive.close_archived(), temporary_root, walk_paths
        )

    _inside_temporary_directory(individual_test)


def test_heavy() -> None:
    """Test to compress multiple files larger than byte limit dividedly."""

    def individual_test(temporary_root: Path) -> None:
        tree_root: Path = create_temporary_tree(
            Path(temporary_root, "tree"), tree_deep=3, tree_weight=2
        )

        walk_paths: Paths = []
        compress_archive = CompressArchive(
            Path(temporary_root, "archive"), limit_byte=64
        )
        for path in walk_iterator(tree_root, directory=False, suffix="json"):
            compress_archive.compress_archive(path, archive_root=tree_root)
            walk_paths += [path]

        _common_test(
            compress_archive.close_archived(), temporary_root, walk_paths
        )

    _inside_temporary_directory(individual_test)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_empty()
    test_file()
    test_directory()
    test_tree()
    test_compress()
    test_id()
    test_limit()
    test_heavy()
    return True
