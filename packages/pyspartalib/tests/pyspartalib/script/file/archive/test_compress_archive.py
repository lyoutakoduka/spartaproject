#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to compress file or directory by archive format."""

from decimal import Decimal
from pathlib import Path
from shutil import unpack_archive
from tempfile import TemporaryDirectory

from pyspartalib.context.default.integer_context import Ints2
from pyspartalib.context.default.string_context import StrPair
from pyspartalib.context.extension.decimal_context import Decs
from pyspartalib.context.extension.path_context import PathFunc, Paths, Paths2
from pyspartalib.script.decimal.initialize_decimal import initialize_decimal
from pyspartalib.script.directory.create_parent import create_parent
from pyspartalib.script.file.archive.compress_archive import CompressArchive
from pyspartalib.script.file.json.convert_from_json import (
    string_pair_from_json,
)
from pyspartalib.script.file.json.convert_to_json import multiple_to_json
from pyspartalib.script.file.json.export_json import json_export
from pyspartalib.script.file.json.import_json import json_import
from pyspartalib.script.path.iterate_directory import walk_iterator
from pyspartalib.script.path.modify.current.get_relative import (
    get_relative_array,
)
from pyspartalib.script.path.status.get_statistic import (
    get_file_size,
    get_file_size_array,
)
from pyspartalib.script.path.temporary.create_temporary_tree import (
    create_temporary_tree,
)

initialize_decimal()


def _get_multiple() -> str:
    return "\u3042"


def _get_multiple_path(tree_root: Path) -> Path:
    multiple: str = _get_multiple()
    return Path(tree_root, multiple, multiple).with_suffix(".json")


def _get_multiple_data() -> StrPair:
    return {"multiple": _get_multiple()}


def _get_tree_root(temporary_root: Path) -> Path:
    return Path(temporary_root, "tree")


def _get_extract_root(temporary_root: Path) -> Path:
    return Path(temporary_root, "extract")


def _get_archive_root(temporary_root: Path) -> Path:
    return Path(temporary_root, "archive")


def _get_input_paths(walk_paths: Paths, temporary_root: Path) -> Paths:
    inputs: Paths = []
    tree_root: Path = _get_tree_root(temporary_root)

    for walk_path in walk_paths:
        inputs += [walk_path]
        parent_path: Path = walk_path.parent

        if tree_root != parent_path:
            inputs += [parent_path]

        if walk_path.is_dir():
            for path in walk_iterator(walk_path):
                inputs += [path]

    return inputs


def _get_output_paths(archive_paths: Paths, temporary_root: Path) -> Paths:
    outputs: Paths = []
    extract_root: Path = _get_extract_root(temporary_root)

    for archive_path in archive_paths:
        unpack_archive(archive_path, extract_dir=extract_root)

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


def _compare_compress_size(outputs: Paths, archive_paths: Paths) -> None:
    file_sizes: Decs = [
        Decimal(str(sum(get_file_size_array(paths))))
        for paths in [outputs, archive_paths]
    ]

    assert Decimal("0.05") > (file_sizes[1] / file_sizes[0])


def _compare_archived_count(archive_paths: Paths) -> None:
    assert 1 == len(archive_paths)


def _get_sorted_paths(
    walk_paths: Paths, archive_paths: Paths, temporary_root: Path
) -> Paths2:
    inputs: Paths = _get_input_paths(walk_paths, temporary_root)
    outputs: Paths = _get_output_paths(archive_paths, temporary_root)

    return [sorted(list(set(paths))) for paths in [inputs, outputs]]


def _compare_archive(
    archive_paths: Paths, temporary_root: Path, walk_paths: Paths
) -> Paths2:
    sorted_paths: Paths2 = _get_sorted_paths(
        walk_paths, archive_paths, temporary_root
    )

    _compare_path_name(sorted_paths, temporary_root)
    _compare_file_size(sorted_paths)

    return sorted_paths


def _common_test(
    archive_paths: Paths, temporary_root: Path, walk_paths: Paths
) -> None:
    _compare_archive(archive_paths, temporary_root, walk_paths)
    _compare_archived_count(archive_paths)


def _compress_test(
    archive_paths: Paths, temporary_root: Path, walk_paths: Paths
) -> None:
    sorted_paths: Paths2 = _compare_archive(
        archive_paths,
        temporary_root,
        walk_paths,
    )

    _compare_archived_count(archive_paths)
    _compare_compress_size(sorted_paths[-1], archive_paths)


def _name_test(archive_name: str, archive_paths: Paths) -> None:
    assert archive_name == archive_paths[0].stem


def _import_multiple(config_path: Path) -> StrPair:
    return string_pair_from_json(json_import(config_path))


def _compare_archive_text(config_path: Path, expected: StrPair) -> None:
    assert expected == _import_multiple(config_path)


def _find_config_path(sorted_paths: Paths2) -> Path:
    return sorted_paths[-1][-1]


def _multiple_test(
    archive_paths: Paths,
    temporary_root: Path,
    walk_paths: Paths,
    expected: StrPair,
) -> None:
    _compare_archive_text(
        _find_config_path(
            _compare_archive(archive_paths, temporary_root, walk_paths)
        ),
        expected,
    )


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def _confirm_empty_archive(archive_paths: Paths) -> None:
    _compare_archived_count(archive_paths)

    expected: int = 22
    assert expected == get_file_size(archive_paths[0])


def _finalize_archive(
    tree_root: Path, paths: Paths, compress_archive: CompressArchive
) -> Paths:
    compress_archive.compress_at_once(paths, archive_root=tree_root)
    return compress_archive.close_archived()


def _create_tree(temporary_root: Path) -> Path:
    return create_temporary_tree(_get_tree_root(temporary_root))


def _create_tree_directory(temporary_root: Path) -> Path:
    return create_temporary_tree(_get_tree_root(temporary_root), tree_deep=2)


def _create_tree_tree(temporary_root: Path) -> Path:
    return create_temporary_tree(_get_tree_root(temporary_root), tree_deep=3)


def _create_tree_compress(temporary_root: Path) -> Path:
    return create_temporary_tree(_get_tree_root(temporary_root), tree_weight=4)


def _create_tree_limit(temporary_root: Path) -> Path:
    return create_temporary_tree(_get_tree_root(temporary_root), tree_deep=3)


def _create_tree_heavy(temporary_root: Path) -> Path:
    return create_temporary_tree(
        _get_tree_root(temporary_root), tree_deep=3, tree_weight=2
    )


def _get_archive(temporary_root: Path) -> CompressArchive:
    return CompressArchive(_get_archive_root(temporary_root))


def _get_archive_compress(temporary_root: Path) -> CompressArchive:
    return CompressArchive(_get_archive_root(temporary_root), compress=True)


def _get_archive_name(
    temporary_root: Path, archive_name: str
) -> CompressArchive:
    return CompressArchive(
        _get_archive_root(temporary_root), archive_id=archive_name
    )


def _get_archive_limit(temporary_root: Path) -> CompressArchive:
    return CompressArchive(_get_archive_root(temporary_root), limit_byte=256)


def _get_archive_heavy(temporary_root: Path) -> CompressArchive:
    return CompressArchive(_get_archive_root(temporary_root), limit_byte=64)


def _get_walk_paths(tree_root: Path) -> Paths:
    return list(walk_iterator(tree_root, directory=False, depth=1))


def _get_walk_paths_directory(tree_root: Path) -> Paths:
    return list(walk_iterator(tree_root, file=False, depth=1))


def _get_walk_paths_tree(tree_root: Path) -> Paths:
    return list(walk_iterator(tree_root, directory=False, suffix="txt"))


def _get_walk_paths_compress(tree_root: Path) -> Paths:
    return list(walk_iterator(tree_root, directory=False, suffix="json"))


def _get_walk_paths_limit(tree_root: Path) -> Paths:
    return list(walk_iterator(tree_root, directory=False))


def _get_walk_paths_heavy(tree_root: Path) -> Paths:
    return list(walk_iterator(tree_root, directory=False, suffix="json"))


def _export_multiple(config_path: Path, config_data: StrPair) -> None:
    create_parent(config_path)
    json_export(config_path, multiple_to_json(config_data))


def test_empty() -> None:
    """Test to create empty archive."""

    def individual_test(temporary_root: Path) -> None:
        _confirm_empty_archive(
            CompressArchive(_get_archive_root(temporary_root)).close_archived()
        )

    _inside_temporary_directory(individual_test)


def test_file() -> None:
    """Test to compress multiple files."""

    def individual_test(temporary_root: Path) -> None:
        tree_root: Path = _create_tree(temporary_root)
        walk_paths: Paths = _get_walk_paths(tree_root)

        _common_test(
            _finalize_archive(
                tree_root, walk_paths, _get_archive(temporary_root)
            ),
            temporary_root,
            walk_paths,
        )

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    """Test to compress multiple empty directories."""

    def individual_test(temporary_root: Path) -> None:
        tree_root: Path = _create_tree_directory(temporary_root)
        walk_paths: Paths = _get_walk_paths_directory(tree_root)

        _common_test(
            _finalize_archive(
                tree_root, walk_paths, _get_archive(temporary_root)
            ),
            temporary_root,
            walk_paths,
        )

    _inside_temporary_directory(individual_test)


def test_tree() -> None:
    """Test to compress multiple files and directories."""

    def individual_test(temporary_root: Path) -> None:
        tree_root: Path = _create_tree_tree(temporary_root)
        walk_paths: Paths = _get_walk_paths_tree(tree_root)

        _common_test(
            _finalize_archive(
                tree_root, walk_paths, _get_archive(temporary_root)
            ),
            temporary_root,
            walk_paths,
        )

    _inside_temporary_directory(individual_test)


def test_compress() -> None:
    """Test to compress multiple files by LZMA format."""

    def individual_test(temporary_root: Path) -> None:
        tree_root: Path = _create_tree_compress(temporary_root)
        walk_paths: Paths = _get_walk_paths_compress(tree_root)

        _compress_test(
            _finalize_archive(
                tree_root, walk_paths, _get_archive_compress(temporary_root)
            ),
            temporary_root,
            walk_paths,
        )

    _inside_temporary_directory(individual_test)


def test_name() -> None:
    """Test to compress multiple files by specific archive name."""
    archive_name: str = "test"

    def individual_test(temporary_root: Path) -> None:
        tree_root: Path = _create_tree(temporary_root)

        _name_test(
            archive_name,
            _finalize_archive(
                tree_root,
                _get_walk_paths(tree_root),
                _get_archive_name(temporary_root, archive_name),
            ),
        )

    _inside_temporary_directory(individual_test)


def test_limit() -> None:
    """Test to compress multiple files and directories dividedly."""

    def individual_test(temporary_root: Path) -> None:
        tree_root: Path = _create_tree_limit(temporary_root)
        walk_paths: Paths = _get_walk_paths_limit(tree_root)

        _compare_archive(
            _finalize_archive(
                tree_root, walk_paths, _get_archive_limit(temporary_root)
            ),
            temporary_root,
            walk_paths,
        )

    _inside_temporary_directory(individual_test)


def test_heavy() -> None:
    """Test to compress multiple files larger than byte limit dividedly."""

    def individual_test(temporary_root: Path) -> None:
        tree_root: Path = _create_tree_heavy(temporary_root)
        walk_paths: Paths = _get_walk_paths_heavy(tree_root)

        _compare_archive(
            _finalize_archive(
                tree_root, walk_paths, _get_archive_heavy(temporary_root)
            ),
            temporary_root,
            walk_paths,
        )

    _inside_temporary_directory(individual_test)


def test_multiple() -> None:
    """Test to compress archive including multiple byte character."""

    def individual_test(temporary_root: Path) -> None:
        tree_root: Path = _get_tree_root(temporary_root)
        config_path: Path = _get_multiple_path(tree_root)
        config_data: StrPair = _get_multiple_data()
        walk_paths: Paths = [config_path]

        _export_multiple(config_path, config_data)

        _multiple_test(
            _finalize_archive(
                tree_root, walk_paths, _get_archive(temporary_root)
            ),
            temporary_root,
            walk_paths,
            config_data,
        )

    _inside_temporary_directory(individual_test)
