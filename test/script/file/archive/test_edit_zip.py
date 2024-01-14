#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to edit internal of zip archive file."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.default.string_context import StrPair
from pyspartaproj.context.extension.path_context import PathPair, Paths
from pyspartaproj.interface.pytest import fail
from pyspartaproj.script.bool.compare_json import is_same_json
from pyspartaproj.script.file.archive.compress_zip import CompressZip
from pyspartaproj.script.file.archive.decompress_zip import DecompressZip
from pyspartaproj.script.file.archive.edit_zip import EditZip
from pyspartaproj.script.file.json.convert_to_json import multiple_to_json
from pyspartaproj.script.path.iterate_directory import walk_iterator
from pyspartaproj.script.path.modify.get_relative import get_relative
from pyspartaproj.script.path.safe.safe_rename import SafeRename
from pyspartaproj.script.path.safe.safe_trash import SafeTrash
from pyspartaproj.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartaproj.script.path.temporary.create_temporary_tree import (
    create_temporary_tree,
)
from pyspartaproj.script.time.stamp.get_timestamp import get_directory_latest


def _add_archive(temporary_root: Path, compress_zip: CompressZip) -> Path:
    for path in walk_iterator(Path(temporary_root, "before")):
        compress_zip.compress_archive(path)

    return compress_zip.close_archived()[0]


def _get_stamp_key(path_text: str, stamp_root: Path) -> str:
    return str(get_relative(Path(path_text), root_path=stamp_root))


def _get_stamp_value(path_text: str, time: str) -> str:
    return "directory" if Path(path_text).is_dir() else time


def _get_archive_stamp(stamp_root: Path) -> StrPair:
    latest_times: StrPair = get_directory_latest(walk_iterator(stamp_root))

    return {
        _get_stamp_key(key, stamp_root): _get_stamp_value(key, time)
        for key, time in latest_times.items()
    }


def _get_archive_stamp_before(temporary_root: Path) -> StrPair:
    return _get_archive_stamp(Path(temporary_root, "before"))


def _get_archive_stamp_after(temporary_root: Path) -> StrPair:
    return _get_archive_stamp(Path(temporary_root, "after"))


def _create_archive(temporary_root: Path) -> None:
    create_temporary_tree(Path(temporary_root, "before"))


def _initialize_archive(temporary_root: Path) -> StrPair:
    _create_archive(temporary_root)
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
    decompress_zip = DecompressZip(after_root)

    for archived_path in archived:
        decompress_zip.decompress_archive(archived_path)


def _remove_stamp_after(path_text: str, stamp_after: StrPair) -> None:
    del stamp_after[path_text]


def _remove_time_stamp(edit_history: PathPair, stamp_after: StrPair) -> None:
    _remove_stamp_after(str(edit_history["add"]), stamp_after)


def _add_stamp_after(
    edit_type: str,
    edit_history: PathPair,
    stamp_before: StrPair,
    stamp_after: StrPair,
) -> None:
    path_text: str = str(edit_history[edit_type])
    stamp_after[path_text] = stamp_before[path_text]


def _add_time_stamp(
    edit_history: PathPair, stamp_before: StrPair, stamp_after: StrPair
) -> None:
    _add_stamp_after("remove", edit_history, stamp_before, stamp_after)


def _update_time_stamp(
    edit_history: PathPair, stamp_before: StrPair, stamp_after: StrPair
) -> None:
    _remove_stamp_after("rename", stamp_after)
    _add_stamp_after("update", edit_history, stamp_before, stamp_after)


def _edit_time_stamp(
    edit_history: PathPair, stamp_before: StrPair, stamp_after: StrPair
) -> None:
    _remove_time_stamp(edit_history, stamp_after)
    _add_time_stamp(edit_history, stamp_before, stamp_after)
    _update_time_stamp(edit_history, stamp_before, stamp_after)


def _compare_time_stamp(stamp_before: StrPair, stamp_after: StrPair) -> bool:
    return is_same_json(
        *[multiple_to_json(stamp) for stamp in [stamp_before, stamp_after]]
    )


def _get_stamp_after(
    temporary_root: Path,
    stamp_before: StrPair,
    edit_history: PathPair,
    archived: Paths,
) -> StrPair:
    _decompress_archive(Path(temporary_root, "after"), archived)

    stamp_after: StrPair = _get_archive_stamp_after(temporary_root)
    _edit_time_stamp(edit_history, stamp_before, stamp_after)

    return stamp_after


def _get_edit_history(edit_zip: EditZip) -> PathPair:
    return _edit_to_archived(edit_zip.get_decompressed_root())


def _get_archive_size(archive_path: Path) -> int:
    return archive_path.stat().st_size


def _common_test(
    temporary_root: Path, stamp_before: StrPair, edit_zip: EditZip
) -> None:
    edit_history: PathPair = _get_edit_history(edit_zip)

    if archived := edit_zip.close_archive():
        assert _compare_time_stamp(
            stamp_before,
            _get_stamp_after(
                temporary_root, stamp_before, edit_history, archived
            ),
        )
    else:
        fail()


def test_single() -> None:
    """Test to edit edit internal of single zip archive file."""

    def individual_test(temporary_root: Path) -> None:
        stamp_before: StrPair = _initialize_archive(temporary_root)

        compress_zip = CompressZip(Path(temporary_root, "archive"))
        edit_zip = EditZip(_add_archive(temporary_root, compress_zip))

        _common_test(temporary_root, stamp_before, edit_zip)

    _inside_temporary_directory(individual_test)


def test_multiple() -> None:
    """Test to edit edit internal of multiple zip archive files."""
    limit_byte: int = 50

    def individual_test(temporary_root: Path) -> None:
        stamp_before: StrPair = _initialize_archive(temporary_root)

        compress_zip = CompressZip(
            Path(temporary_root, "archive"), limit_byte=limit_byte
        )
        edit_zip = EditZip(
            _add_archive(temporary_root, compress_zip),
            limit_byte=limit_byte,
        )

        _common_test(temporary_root, stamp_before, edit_zip)

    _inside_temporary_directory(individual_test)


def test_compress() -> None:
    """Test to compare size fo zip archive files."""

    def individual_test(temporary_root: Path) -> None:
        create_temporary_tree(Path(temporary_root, "before"), tree_weight=3)

        archive_path = _add_archive(
            temporary_root,
            CompressZip(Path(temporary_root, "archive")),
        )
        archive_size_before = _get_archive_size(archive_path)

        if EditZip(archive_path, compress=True).close_archive():
            assert archive_size_before > _get_archive_size(archive_path)
        else:
            fail()

    _inside_temporary_directory(individual_test)


def main() -> bool:
    """All test of feature flags module.

    Returns:
        bool: Success if get to the end of function.
    """
    test_single()
    test_multiple()
    test_compress()
    return True
