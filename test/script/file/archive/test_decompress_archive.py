#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to decompress file or directory by archive format."""

from itertools import chain
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.default.integer_context import Ints2
from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.context.extension.path_context import Paths, Paths2
from pyspartaproj.context.extension.time_context import Times, Times2, datetime
from pyspartaproj.script.file.archive.compress_archive import CompressArchive
from pyspartaproj.script.file.archive.decompress_archive import (
    DecompressArchive,
)
from pyspartaproj.script.path.iterate_directory import walk_iterator
from pyspartaproj.script.path.modify.get_relative import get_relative_array
from pyspartaproj.script.path.safe.safe_trash import SafeTrash
from pyspartaproj.script.path.status.get_statistic import get_file_size_array
from pyspartaproj.script.path.temporary.create_temporary_tree import (
    create_temporary_tree,
)
from pyspartaproj.script.time.stamp.get_timestamp import get_latest
from pyspartaproj.script.time.stamp.set_timestamp import set_latest


def _get_types() -> Strs:
    return ["tree", "extract"]


def _get_tree_root(temporary_root: Path) -> Path:
    return Path(temporary_root, "tree")


def _get_extract_root(temporary_root: Path) -> Path:
    return Path(temporary_root, "extract")


def _get_archive_root(temporary_root: Path) -> Path:
    return Path(temporary_root, "archive")


def _get_expected_stamp() -> datetime:
    return datetime.fromisoformat("2023-04-15T20:09:30.936886+00:00")


def _get_times_pair(sorted_paths: Paths2) -> Times2:
    return [
        [get_latest(path) for path in paths if path.is_file()]
        for paths in sorted_paths
    ]


def _get_times(times_pair: Times2) -> Times:
    return list(set(chain(*times_pair)))


def _compare_timestamp(sorted_paths: Paths2, expected: datetime) -> None:
    times_pair: Times2 = _get_times_pair(sorted_paths)
    assert times_pair[0] == times_pair[1]

    times = _get_times(times_pair)
    assert 1 == len(times)

    assert expected == times[0]


def _compare_path_pair(left: Paths, right: Paths) -> None:
    assert 1 == len(set([str(sorted(paths)) for paths in [left, right]]))


def _get_relative_paths(sorted_paths: Paths2, temporary_root: Path) -> Paths2:
    return [
        get_relative_array(paths, root_path=Path(temporary_root, directory))
        for directory, paths in zip(_get_types(), sorted_paths)
    ]


def _compare_path_name(sorted_paths: Paths2, temporary_root: Path) -> None:
    relative_paths: Paths2 = _get_relative_paths(sorted_paths, temporary_root)
    assert relative_paths[0] == relative_paths[1]


def _get_file_size_pair(sorted_paths: Paths2) -> Ints2:
    return [get_file_size_array(paths) for paths in sorted_paths]


def _compare_file_size(sorted_paths: Paths2) -> None:
    file_size_pair: Ints2 = _get_file_size_pair(sorted_paths)
    assert file_size_pair[0] == file_size_pair[1]


def _get_sorted_paths(temporary_root: Path) -> Paths2:
    return [
        sorted(list(walk_iterator(Path(temporary_root, directory))))
        for directory in _get_types()
    ]


def _common_test(temporary_root: Path) -> Paths2:
    sorted_paths: Paths2 = _get_sorted_paths(temporary_root)

    _compare_path_name(sorted_paths, temporary_root)
    _compare_file_size(sorted_paths)

    return sorted_paths


def _type_test(temporary_root: Path, same_type: bool) -> None:
    _common_test(temporary_root)
    assert not same_type


def _sequential_test(
    temporary_root: Path, archive_paths: Paths, sequential: Paths
) -> None:
    _common_test(temporary_root)
    _compare_path_pair(archive_paths, sequential)


def _timestamp_test(temporary_root: Path) -> None:
    _compare_timestamp(_common_test(temporary_root), _get_expected_stamp())


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def _set_file_latest(paths: Paths) -> None:
    latest: datetime = _get_expected_stamp()
    for path in paths:
        if path.is_file():
            set_latest(path, latest)


def _find_unused(paths: Paths) -> Paths:
    return [
        path for path in paths if 0 == len(list(walk_iterator(path, depth=1)))
    ]


def _remove_unused(paths: Paths) -> None:
    SafeTrash().trash_at_once(paths)


def _create_tree(temporary_root: Path) -> Path:
    return create_temporary_tree(_get_tree_root(temporary_root))


def _create_tree_file(temporary_root: Path) -> Path:
    return create_temporary_tree(_get_tree_root(temporary_root), tree_deep=2)


def _create_tree_directory(temporary_root: Path) -> Path:
    return create_temporary_tree(_get_tree_root(temporary_root), tree_deep=3)


def _create_tree_sequential(temporary_root: Path) -> Path:
    return create_temporary_tree(_get_tree_root(temporary_root), tree_deep=5)


def _get_tree_paths(path: Path) -> Paths:
    return list(walk_iterator(path))


def _get_tree_paths_file(path: Path) -> Paths:
    return list(walk_iterator(path, file=False))


def _get_tree_paths_directory(path: Path) -> Paths:
    return list(walk_iterator(path, directory=False))


def _compress_archive(temporary_root: Path) -> CompressArchive:
    return CompressArchive(_get_archive_root(temporary_root))


def _compress_archive_sequential(temporary_root: Path) -> CompressArchive:
    return CompressArchive(_get_archive_root(temporary_root), limit_byte=200)


def _decompress_archive(temporary_root: Path) -> DecompressArchive:
    return DecompressArchive(_get_extract_root(temporary_root))


def _compress_at_once(
    tree_path: Path, paths: Paths, compress_archive: CompressArchive
) -> None:
    compress_archive.compress_at_once(paths, archive_root=tree_path)


def _from_compress_single(
    temporary_root: Path, tree_path: Path, add_paths: Paths
) -> CompressArchive:
    compress_archive: CompressArchive = _compress_archive(temporary_root)
    _compress_at_once(tree_path, add_paths, compress_archive)
    return compress_archive


def _from_compress_sequential(
    temporary_root: Path, tree_path: Path, add_paths: Paths
) -> CompressArchive:
    compress_archive: CompressArchive = _compress_archive_sequential(
        temporary_root
    )
    _compress_at_once(tree_path, add_paths, compress_archive)
    return compress_archive


def _decompress_single(
    archive_paths: Paths, decompress_archive: DecompressArchive
) -> None:
    decompress_archive.decompress_archive(archive_paths[0])


def _decompress_type(
    archive_paths: Paths, decompress_archive: DecompressArchive
) -> bool:
    return decompress_archive.is_lzma_archive(archive_paths[0])


def _decompress_sequential(
    archive_paths: Paths, decompress_archive: DecompressArchive
) -> Paths:
    sequential: Paths = decompress_archive.sequential_archives(
        archive_paths[0]
    )
    decompress_archive.decompress_at_once(sequential)
    return sequential


def _to_decompress_single(
    temporary_root: Path, archive_paths: Paths
) -> DecompressArchive:
    decompress_archive: DecompressArchive = _decompress_archive(temporary_root)
    _decompress_single(archive_paths, decompress_archive)
    return decompress_archive


def _finalize_compress_single(
    temporary_root: Path, tree_path: Path, add_paths: Paths
) -> Paths:
    compress_archive: CompressArchive = _from_compress_single(
        temporary_root, tree_path, add_paths
    )
    return compress_archive.close_archived()


def _finalize_compress_sequential(
    temporary_root: Path, tree_path: Path, add_paths: Paths
) -> Paths:
    compress_archive: CompressArchive = _from_compress_sequential(
        temporary_root, tree_path, add_paths
    )
    return compress_archive.close_archived()


def _compress_to_decompress(
    temporary_root: Path, tree_path: Path, add_paths: Paths
) -> None:
    _to_decompress_single(
        temporary_root,
        _finalize_compress_single(temporary_root, tree_path, add_paths),
    )


def _remove_unused_file(tree_path: Path) -> None:
    _remove_unused(_find_unused(_get_tree_paths_file(tree_path)))


def _remove_unused_directory(tree_path: Path) -> None:
    _remove_unused(_get_tree_paths_directory(tree_path))


def test_file() -> None:
    """Test to decompress archive including only files."""

    def individual_test(temporary_root: Path) -> None:
        tree_path: Path = _create_tree_file(temporary_root)

        _remove_unused_file(tree_path)
        _compress_to_decompress(
            temporary_root, tree_path, _get_tree_paths(tree_path)
        )

        _common_test(temporary_root)

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    """Test to decompress archive including only directories."""

    def individual_test(temporary_root: Path) -> None:
        tree_path: Path = _create_tree_directory(temporary_root)

        _remove_unused_directory(tree_path)
        _compress_to_decompress(
            temporary_root, tree_path, _get_tree_paths(tree_path)
        )

        _common_test(temporary_root)

    _inside_temporary_directory(individual_test)


def test_type() -> None:
    """Test to get type of compression format from archive."""

    def individual_test(temporary_root: Path) -> None:
        tree_path: Path = _create_tree(temporary_root)

        archive_paths: Paths = _finalize_compress_single(
            temporary_root, tree_path, _get_tree_paths(tree_path)
        )
        same_type: bool = _decompress_type(
            archive_paths, _to_decompress_single(temporary_root, archive_paths)
        )

        _type_test(temporary_root, same_type)

    _inside_temporary_directory(individual_test)


def test_sequential() -> None:
    """Test to decompress sequential archives."""

    def individual_test(temporary_root: Path) -> None:
        tree_path: Path = _create_tree_sequential(temporary_root)

        archive_paths: Paths = _finalize_compress_sequential(
            temporary_root, tree_path, _get_tree_paths(tree_path)
        )
        sequential: Paths = _decompress_sequential(
            archive_paths, _decompress_archive(temporary_root)
        )

        _sequential_test(temporary_root, archive_paths, sequential)

    _inside_temporary_directory(individual_test)


def test_timestamp() -> None:
    """Test for timestamp consistency of contents in archive."""

    def individual_test(temporary_root: Path) -> None:
        tree_path: Path = _create_tree(temporary_root)

        add_paths: Paths = _get_tree_paths(tree_path)
        _set_file_latest(add_paths)
        _compress_to_decompress(temporary_root, tree_path, add_paths)

        _timestamp_test(temporary_root)

    _inside_temporary_directory(individual_test)
