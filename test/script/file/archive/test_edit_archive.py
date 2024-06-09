#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to edit internal of archive file."""

from datetime import datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.extension.path_context import PathPair, Paths, Paths2
from pyspartaproj.context.extension.time_context import TimePair
from pyspartaproj.interface.pytest import fail
from pyspartaproj.script.directory.create_directory import create_directory
from pyspartaproj.script.file.archive.compress_archive import CompressArchive
from pyspartaproj.script.file.archive.decompress_archive import (
    DecompressArchive,
)
from pyspartaproj.script.file.archive.edit_archive import EditArchive
from pyspartaproj.script.path.iterate_directory import walk_iterator
from pyspartaproj.script.path.modify.get_relative import (
    get_relative,
    is_relative,
)
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


def _get_name() -> str:
    return "temporary"


def _get_root_before(temporary_root: Path) -> Path:
    return Path(temporary_root, "before")


def _get_root_after(temporary_root: Path) -> Path:
    return Path(temporary_root, "after")


def _get_root_archive(temporary_root: Path) -> Path:
    return Path(temporary_root, "archive")


def _get_root_edit(temporary_root: Path) -> Path:
    return Path(temporary_root, "edit")


def _get_date_time_root(jst: bool = False) -> Path:
    time_utc: Path = Path("2023", "04", "01", "00", "00", "00", "000000")
    time_jst: Path = Path("2023", "04", "01", "09", "00", "00", "000000")

    return time_jst if jst else time_utc


def _add_archive(
    temporary_root: Path, compress_archive: CompressArchive
) -> Paths:
    compress_archive.compress_at_once(
        list(walk_iterator(_get_root_before(temporary_root)))
    )

    return compress_archive.close_archived()


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


def _decompress_archive(after_root: Path, archive_paths: Paths) -> None:
    DecompressArchive(after_root).decompress_at_once(archive_paths)


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


def _get_decompress_stamp(
    temporary_root: Path, archive_paths: Paths
) -> TimePair:
    _decompress_archive(_get_root_after(temporary_root), archive_paths)
    return _get_archive_stamp_after(temporary_root)


def _get_stamp_after(
    temporary_root: Path,
    stamp_before: TimePair,
    edit_history: PathPair,
    archive_paths: Paths,
) -> TimePair:
    stamp_after: TimePair = _get_decompress_stamp(
        temporary_root, archive_paths
    )
    _edit_time_stamp(edit_history, stamp_before, stamp_after)

    return stamp_after


def _find_decompress_root(temporary_root: Path, remove_root: Path) -> TimePair:
    return _get_decompress_stamp(
        temporary_root, list(walk_iterator(remove_root, directory=False))
    )


def _get_edit_history(edit_archive: EditArchive) -> PathPair:
    return _edit_to_archived(edit_archive.get_edit_root())


def _close_archive(edit_archive: EditArchive) -> Paths:
    if archive_paths := edit_archive.close_archive():
        return archive_paths
    else:
        fail()


def _compare_path(result: Path, expected: Path) -> None:
    assert result.exists()
    assert result == expected


def _close_archive_fail(edit_archive: EditArchive) -> None:
    assert edit_archive.close_archive() is None


def _stamp_test(stamp_before: TimePair, stamp_after: TimePair) -> None:
    assert is_same_stamp(stamp_before, stamp_after)


def _compare_not_relative(full_path: Path, root_path: Path) -> None:
    assert not is_relative(full_path, root_path=root_path)


def _common_test(
    temporary_root: Path, stamp_before: TimePair, edit_archive: EditArchive
) -> None:
    _stamp_test(
        stamp_before,
        _get_stamp_after(
            temporary_root,
            stamp_before,
            _get_edit_history(edit_archive),
            _close_archive(edit_archive),
        ),
    )


def _protect_test(
    temporary_root: Path, stamp_before: TimePair, edit_archive: EditArchive
) -> None:
    _get_edit_history(edit_archive)
    _close_archive_fail(edit_archive)

    _stamp_test(
        stamp_before,
        _find_decompress_root(
            temporary_root, _get_root_archive(temporary_root)
        ),
    )


def _remove_test(
    temporary_root: Path,
    stamp_before: TimePair,
    edit_archive: EditArchive,
) -> None:
    _get_edit_history(edit_archive)
    _close_archive(edit_archive)

    _stamp_test(
        stamp_before,
        _find_decompress_root(temporary_root, edit_archive.get_trash_root()),
    )


def _get_sorted_paths(before_paths: Paths, after_paths: Paths) -> Paths2:
    return [sorted(paths) for paths in [before_paths, after_paths]]


def _name_test(before_path: Path, edit_archive: EditArchive) -> None:
    _get_edit_history(edit_archive)

    assert before_path == _close_archive(edit_archive)[0]
    assert before_path.stem == _get_name()


def _limit_test(before_paths: Paths, edit_archive: EditArchive) -> None:
    _get_edit_history(edit_archive)
    after_paths: Paths = _close_archive(edit_archive)

    before_paths, after_paths = _get_sorted_paths(before_paths, after_paths)
    assert before_paths == after_paths


def _compress_test(archive_path: Path, edit_archive: EditArchive) -> None:
    archive_size_before: int = get_file_size(archive_path)
    _close_archive(edit_archive)

    assert archive_size_before > get_file_size(archive_path)


def _get_archive(temporary_root: Path) -> CompressArchive:
    return CompressArchive(_get_root_archive(temporary_root))


def _get_archive_name(temporary_root: Path) -> CompressArchive:
    return CompressArchive(
        _get_root_archive(temporary_root), archive_id=_get_name()
    )


def _get_archive_limit(
    temporary_root: Path, limit_byte: int
) -> CompressArchive:
    return CompressArchive(
        _get_root_archive(temporary_root), limit_byte=limit_byte
    )


def _get_archive_path(temporary_root: Path) -> Path:
    return _add_archive(temporary_root, _get_archive(temporary_root))[0]


def _get_archive_path_name(temporary_root: Path) -> Paths:
    return _add_archive(temporary_root, _get_archive_name(temporary_root))


def _get_archive_path_limit(temporary_root: Path, limit_byte: int) -> Paths:
    return _add_archive(
        temporary_root, _get_archive_limit(temporary_root, limit_byte)
    )


def _get_edit_archive(archive_path: Path) -> EditArchive:
    return EditArchive(archive_path)


def _get_edit_archive_work(working_root: Path) -> EditArchive:
    return EditArchive(working_root=working_root, override=True)


def _get_edit_archive_edit(working_root: Path) -> EditArchive:
    return EditArchive(edit_root=working_root, override=True)


def _get_edit_archive_limit(
    archive_path: Path, limit_byte: int
) -> EditArchive:
    return EditArchive(archive_path, limit_byte=limit_byte)


def _get_edit_archive_compress(archive_path: Path) -> EditArchive:
    return EditArchive(archive_path, compress=True)


def _get_edit_archive_protect(archive_path: Path) -> EditArchive:
    return EditArchive(archive_path, protected=True)


def _get_edit_archive_remove(
    archive_path: Path, remove_root: Path
) -> EditArchive:
    return EditArchive(archive_path, trash_root=remove_root)


def test_work() -> None:
    def individual_test(temporary_root: Path) -> None:
        edit_archive: EditArchive = _get_edit_archive_work(temporary_root)

        _compare_path(
            edit_archive.get_edit_root(),
            Path(temporary_root, _get_date_time_root()),
        )

    _inside_temporary_directory(individual_test)


def test_single() -> None:
    """Test to compare internal of single archive file."""

    def individual_test(temporary_root: Path) -> None:
        stamp_before: TimePair = _initialize_archive(temporary_root)

        _common_test(
            temporary_root,
            stamp_before,
            _get_edit_archive(_get_archive_path(temporary_root)),
        )

    _inside_temporary_directory(individual_test)


def test_name() -> None:
    """Test to compare name of archive before edit and after."""

    def individual_test(temporary_root: Path) -> None:
        _create_source(temporary_root)

        archive_path: Path = _get_archive_path_name(temporary_root)[0]
        _name_test(archive_path, _get_edit_archive(archive_path))

    _inside_temporary_directory(individual_test)


def test_limit() -> None:
    """Test to compare archive paths before edit and after."""
    limit_byte: int = 100

    def individual_test(temporary_root: Path) -> None:
        _create_source(temporary_root)

        archive_paths: Paths = _get_archive_path_limit(
            temporary_root, limit_byte
        )
        _limit_test(
            archive_paths,
            _get_edit_archive_limit(archive_paths[0], limit_byte),
        )

    _inside_temporary_directory(individual_test)


def test_compress() -> None:
    """Test to compare size of archive files."""

    def individual_test(temporary_root: Path) -> None:
        _create_source_compress(temporary_root)

        archive_path: Path = _get_archive_path(temporary_root)
        _compress_test(archive_path, _get_edit_archive_compress(archive_path))

    _inside_temporary_directory(individual_test)


def test_protect() -> None:
    """Test to take out directory from protected archive."""

    def individual_test(temporary_root: Path) -> None:
        stamp_before: TimePair = _initialize_archive(temporary_root)

        _protect_test(
            temporary_root,
            stamp_before,
            _get_edit_archive_protect(_get_archive_path(temporary_root)),
        )

    _inside_temporary_directory(individual_test)


def test_remove() -> None:
    """Test of directory used for removing process when archive is edited."""

    def individual_test(temporary_root: Path) -> None:
        stamp_before: TimePair = _initialize_archive(temporary_root)
        remove_root: Path = create_directory(_get_root_edit(temporary_root))

        _remove_test(
            temporary_root,
            stamp_before,
            _get_edit_archive_remove(
                _get_archive_path(temporary_root), remove_root
            ),
        )

    _inside_temporary_directory(individual_test)


def main() -> bool:
    """All test of feature flags module.

    Returns:
        bool: Success if get to the end of function.
    """
    test_work()
    test_single()
    test_name()
    test_limit()
    test_compress()
    test_protect()
    test_remove()
    return True
