#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to edit internal of archive file."""

from datetime import datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.extension.path_context import PathPair, Paths
from pyspartaproj.context.extension.time_context import TimePair
from pyspartaproj.interface.pytest import fail
from pyspartaproj.script.file.archive.compress_archive import CompressArchive
from pyspartaproj.script.file.archive.decompress_archive import (
    DecompressArchive,
)
from pyspartaproj.script.file.archive.edit_archive import EditArchive
from pyspartaproj.script.path.iterate_directory import walk_iterator
from pyspartaproj.script.path.modify.get_relative import get_relative
from pyspartaproj.script.path.safe.safe_rename import SafeRename
from pyspartaproj.script.path.safe.safe_trash import SafeTrash
from pyspartaproj.script.path.status.get_statistic import get_file_size
from pyspartaproj.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartaproj.script.path.temporary.create_temporary_tree import (
    create_temporary_tree,
)
from pyspartaproj.script.time.stamp.get_timestamp import (
    get_directory_latest,
    get_invalid_time,
    is_same_stamp,
)


def _get_root_before(temporary_root: Path) -> Path:
    return Path(temporary_root, "before")


def _get_root_after(temporary_root: Path) -> Path:
    return Path(temporary_root, "after")


def _get_root_archive(temporary_root: Path) -> Path:
    return Path(temporary_root, "archive")


def _add_archive(
    temporary_root: Path, compress_archive: CompressArchive
) -> Path:
    for path in walk_iterator(_get_root_before(temporary_root)):
        compress_archive.compress_archive(path)

    return compress_archive.close_archived()[0]


def _get_stamp_key(path_text: str, stamp_root: Path) -> str:
    return str(get_relative(Path(path_text), root_path=stamp_root))


def _get_stamp_value(path_text: str, time: datetime) -> datetime:
    return get_invalid_time() if Path(path_text).is_dir() else time


def _get_archive_stamp(stamp_root: Path) -> TimePair:
    latest_times: TimePair = get_directory_latest(walk_iterator(stamp_root))
    return {
        _get_stamp_key(key, stamp_root): _get_stamp_value(key, time)
        for key, time in latest_times.items()
    }


def _get_archive_stamp_before(temporary_root: Path) -> TimePair:
    return _get_archive_stamp(_get_root_before(temporary_root))


def _get_archive_stamp_after(temporary_root: Path) -> TimePair:
    return _get_archive_stamp(_get_root_after(temporary_root))


def _create_source(temporary_root: Path) -> None:
    create_temporary_tree(_get_root_before(temporary_root))


def _create_source_compress(temporary_root: Path) -> None:
    create_temporary_tree(_get_root_before(temporary_root), tree_weight=3)


def _initialize_archive(temporary_root: Path) -> TimePair:
    _create_source(temporary_root)
    return _get_archive_stamp_before(temporary_root)


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def _add_to_archived(archive_root: Path) -> Path:
    return create_temporary_file(archive_root)


def _remove_from_archived(archive_root: Path) -> Path:
    return SafeTrash().trash(Path(archive_root, "file.txt"))


def _update_to_archived(archive_root: Path) -> Path:
    rename_path: Path = Path(archive_root, "file.ini")

    safe_rename = SafeRename()
    safe_rename.rename(rename_path, rename_path.with_name("rename"))

    return rename_path


def _edit_to_archived(archive_root: Path) -> PathPair:
    edit_history: PathPair = {
        "add": _add_to_archived(archive_root),
        "remove": _remove_from_archived(archive_root),
        "update": _update_to_archived(archive_root),
    }

    return {
        key: get_relative(path, root_path=archive_root)
        for key, path in edit_history.items()
    }


def _decompress_archive(after_root: Path, archived: Paths) -> None:
    decompress_archive = DecompressArchive(after_root)

    for archived_path in archived:
        decompress_archive.decompress_archive(archived_path)


def _remove_stamp_after(path_text: str, stamp_after: TimePair) -> None:
    del stamp_after[path_text]


def _remove_time_stamp(edit_history: PathPair, stamp_after: TimePair) -> None:
    _remove_stamp_after(str(edit_history["add"]), stamp_after)


def _add_stamp_after(
    edit_type: str,
    edit_history: PathPair,
    stamp_before: TimePair,
    stamp_after: TimePair,
) -> None:
    path_text: str = str(edit_history[edit_type])
    stamp_after[path_text] = stamp_before[path_text]


def _add_time_stamp(
    edit_history: PathPair, stamp_before: TimePair, stamp_after: TimePair
) -> None:
    _add_stamp_after("remove", edit_history, stamp_before, stamp_after)


def _update_time_stamp(
    edit_history: PathPair, stamp_before: TimePair, stamp_after: TimePair
) -> None:
    _remove_stamp_after("rename", stamp_after)
    _add_stamp_after("update", edit_history, stamp_before, stamp_after)


def _edit_time_stamp(
    edit_history: PathPair, stamp_before: TimePair, stamp_after: TimePair
) -> None:
    _remove_time_stamp(edit_history, stamp_after)
    _add_time_stamp(edit_history, stamp_before, stamp_after)
    _update_time_stamp(edit_history, stamp_before, stamp_after)


def _get_stamp_after(
    temporary_root: Path,
    stamp_before: TimePair,
    edit_history: PathPair,
    archived: Paths,
) -> TimePair:
    _decompress_archive(_get_root_after(temporary_root), archived)

    stamp_after: TimePair = _get_archive_stamp_after(temporary_root)
    _edit_time_stamp(edit_history, stamp_before, stamp_after)

    return stamp_after


def _get_edit_history(edit_archive: EditArchive) -> PathPair:
    return _edit_to_archived(edit_archive.get_decompressed_root())


def _close_archive(edit_archive: EditArchive) -> Paths:
    if archived := edit_archive.close_archive():
        return archived
    else:
        fail()


def _common_test(
    temporary_root: Path, stamp_before: TimePair, edit_archive: EditArchive
) -> None:
    edit_history: PathPair = _get_edit_history(edit_archive)
    archived: Paths = _close_archive(edit_archive)

    assert is_same_stamp(
        stamp_before,
        _get_stamp_after(temporary_root, stamp_before, edit_history, archived),
    )


def compress_test(archive_path: Path, edit_archive: EditArchive) -> None:
    archive_size_before: int = get_file_size(archive_path)
    _close_archive(edit_archive)

    assert archive_size_before > get_file_size(archive_path)


def _protect_test(edit_archive: EditArchive) -> None:
    if edit_archive.close_archive() is not None:
        fail()


def _get_compress_archive(temporary_root: Path) -> CompressArchive:
    return CompressArchive(_get_root_archive(temporary_root))


def _get_compress_archive_limit(
    temporary_root: Path, limit_byte: int
) -> CompressArchive:
    return CompressArchive(
        _get_root_archive(temporary_root), limit_byte=limit_byte
    )


def _get_archive_path(temporary_root: Path) -> Path:
    return _add_archive(temporary_root, _get_compress_archive(temporary_root))


def _get_archive_path_limit(temporary_root: Path, limit_byte: int) -> Path:
    return _add_archive(
        temporary_root,
        _get_compress_archive_limit(temporary_root, limit_byte),
    )


def _get_edit_archive(archive_path: Path) -> EditArchive:
    return EditArchive(archive_path)


def _get_edit_archive_limit(
    archive_path: Path, limit_byte: int
) -> EditArchive:
    return EditArchive(archive_path, limit_byte=limit_byte)


def _get_edit_archive_compress(archive_path: Path) -> EditArchive:
    return EditArchive(archive_path, compress=True)


def test_single() -> None:
    """Test to edit edit internal of single archive file."""

    def individual_test(temporary_root: Path) -> None:
        stamp_before: TimePair = _initialize_archive(temporary_root)

        _common_test(
            temporary_root,
            stamp_before,
            _get_edit_archive(_get_archive_path(temporary_root)),
        )

    _inside_temporary_directory(individual_test)


def test_multiple() -> None:
    """Test to edit edit internal of multiple archive files."""
    limit_byte: int = 50

    def individual_test(temporary_root: Path) -> None:
        stamp_before: TimePair = _initialize_archive(temporary_root)

        _common_test(
            temporary_root,
            stamp_before,
            _get_edit_archive_limit(
                _get_archive_path_limit(temporary_root, limit_byte), limit_byte
            ),
        )

    _inside_temporary_directory(individual_test)


def test_compress() -> None:
    """Test to compare size of archive files."""

    def individual_test(temporary_root: Path) -> None:
        _create_source_compress(temporary_root)

        archive_path: Path = _get_archive_path(temporary_root)
        compress_test(archive_path, _get_edit_archive_compress(archive_path))

    _inside_temporary_directory(individual_test)


def test_protect() -> None:
    def individual_test(temporary_root: Path) -> None:
        _create_source(temporary_root)

        _protect_test(_get_edit_archive(_get_archive_path(temporary_root)))

    _inside_temporary_directory(individual_test)


def main() -> bool:
    """All test of feature flags module.

    Returns:
        bool: Success if get to the end of function.
    """
    test_single()
    test_multiple()
    test_compress()
    test_protect()
    return True
