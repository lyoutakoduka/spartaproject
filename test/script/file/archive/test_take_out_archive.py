#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to take out directory from inside of archive."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.context.extension.path_context import PathPair, Paths
from pyspartaproj.context.typed.user_context import ArchiveStatus
from pyspartaproj.interface.pytest import fail, raises
from pyspartaproj.script.directory.create_directory import create_directory
from pyspartaproj.script.file.archive.compress_archive import CompressArchive
from pyspartaproj.script.file.archive.edit_archive import EditArchive
from pyspartaproj.script.file.archive.take_out_archive import TakeOutArchive
from pyspartaproj.script.path.iterate_directory import walk_iterator
from pyspartaproj.script.path.modify.get_absolute import get_absolute_array
from pyspartaproj.script.path.modify.get_relative import (
    get_relative_array,
    is_relative_array,
)
from pyspartaproj.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)


def _get_empty() -> Paths:
    return []


def _get_types() -> Strs:
    return ["first", "second", "third"]


def _get_directory_names() -> Strs:
    return ["source", "archive"]


def _create_working_directory(temporary_root: Path, names: Strs) -> PathPair:
    return {
        name: create_directory(Path(temporary_root, name)) for name in names
    }


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def _compress_test_archive(working: PathPair) -> Path:
    compress_archive = CompressArchive(
        working["archive"], archive_id="archive"
    )

    compress_archive.compress_at_once(
        list(walk_iterator(working["source"], depth=1))
    )
    return compress_archive.close_archived()[0]


def _get_relative_paths(
    working: PathPair, target_paths: Paths, group: str
) -> Paths:
    return get_relative_array(target_paths, root_path=working[group])


def _get_relative_source(working: PathPair, target_paths: Paths) -> Paths:
    return _get_relative_paths(working, target_paths, "source")


def _find_relative_paths(path: Path) -> Paths:
    return get_relative_array(list(walk_iterator(path)), root_path=path)


def _get_relative_archive(archive_path: Path) -> Paths:
    edit_archive = EditArchive()
    edit_archive.open_archive(archive_path=archive_path)

    return _find_relative_paths(edit_archive.get_edit_root())


def _add_temporary_files(directory_root: Path, file_names: Strs) -> Paths:
    return [
        create_temporary_file(directory_root, file_name=file_name)
        for file_name in file_names
    ]


def _add_directories_test(working: PathPair) -> Paths:
    return list(
        _create_working_directory(working["source"], _get_types()).values()
    )


def _create_archive_shared(
    working: PathPair, taka_paths: Paths, keep_paths: Paths
) -> ArchiveStatus:
    return {
        "archive": _compress_test_archive(working),
        "take": taka_paths,
        "keep": keep_paths,
    }


def _add_test_tree(file_root: Path, name: str) -> Paths:
    file_root = create_directory(Path(file_root, name))
    return [file_root, create_temporary_file(file_root)]


def _add_test_tree_simple(working: PathPair) -> Paths:
    return _add_test_tree(working["source"], "directory")


def _create_archive_compleat(working: PathPair) -> ArchiveStatus:
    return _create_archive_shared(
        working,
        _get_empty(),
        _get_relative_source(
            working, [create_temporary_file(working["source"])]
        ),
    )


def _create_archive_empty(working: PathPair) -> ArchiveStatus:
    return _create_archive_shared(
        working,
        _get_empty(),
        _get_relative_source(
            working, [create_directory(Path(working["source"], "directory"))]
        ),
    )


def _create_archive_single(working: PathPair) -> ArchiveStatus:
    return _create_archive_shared(
        working,
        _get_relative_source(working, _add_test_tree_simple(working)),
        _get_empty(),
    )


def _get_take_out_multiple(working: PathPair) -> Paths:
    directory_root: Path = create_directory(
        Path(working["source"], "directory")
    )

    return [
        directory_root,
        *_add_temporary_files(directory_root, _get_types()),
    ]


def _create_archive_multiple(working: PathPair) -> ArchiveStatus:
    return _create_archive_shared(
        working,
        _get_relative_source(working, _get_take_out_multiple(working)),
        _get_empty(),
    )


def _get_keep_mix(working: PathPair) -> Paths:
    return [create_temporary_file(working["source"])]


def _create_archive_mix(working: PathPair) -> ArchiveStatus:
    return _create_archive_shared(
        working,
        _get_relative_source(working, _add_test_tree_simple(working)),
        _get_relative_source(working, _get_keep_mix(working)),
    )


def _get_take_out_list(working: PathPair) -> Paths:
    file_paths: Paths = []

    for file_root in _add_directories_test(working):
        file_paths += [file_root, create_temporary_file(file_root)]

    return file_paths


def _create_archive_list(working: PathPair) -> ArchiveStatus:
    return _create_archive_shared(
        working,
        _get_relative_source(working, _get_take_out_list(working)),
        _get_empty(),
    )


def _get_take_out_nest(working: PathPair) -> Paths:
    file_root: Path = working["source"]
    take_paths: Paths = []

    for name in _get_types():
        added_paths: Paths = _add_test_tree(file_root, name)
        take_paths += get_relative_array(added_paths, root_path=file_root)
        file_root = added_paths[0]

    return take_paths


def _create_archive_nest(working: PathPair) -> ArchiveStatus:
    return _create_archive_shared(
        working, _get_take_out_nest(working), _get_empty()
    )


def _replace_path_override(index: int, path: Path) -> Path:
    names: Strs = list(path.parts)
    names[0] += "_" * index
    return Path(*names)


def _replace_paths_override(index: int, paths: Paths) -> Paths:
    return [_replace_path_override(index, path) for path in paths]


def _add_archive_override(file_root: Path) -> Paths:
    return get_relative_array(
        _add_test_tree(file_root, "directory"), root_path=file_root
    )


def _get_take_out_override(working: PathPair) -> Paths:
    take_paths: Paths = []

    for i, file_root in enumerate(_add_directories_test(working)):
        take_paths += _replace_paths_override(
            i, _add_archive_override(file_root)
        )

    return take_paths


def _get_keep_override() -> Paths:
    return [Path(name) for name in _get_types()]


def _create_archive_override(working: PathPair) -> ArchiveStatus:
    return _create_archive_shared(
        working, _get_take_out_override(working), _get_keep_override()
    )


def _get_take_out_specific(working: PathPair) -> Paths:
    return _add_test_tree(working["source"], "directory")


def _create_archive_specific(working: PathPair) -> ArchiveStatus:
    return _create_archive_shared(
        working,
        _get_relative_source(working, _get_take_out_specific(working)),
        _get_empty(),
    )


def _create_archive_protect(working: PathPair) -> ArchiveStatus:
    taka_paths: Paths = _get_relative_source(
        working, _add_test_tree_simple(working)
    )
    return _create_archive_shared(working, taka_paths, taka_paths)


def _replace_path_root(archive_path: Path, archive_root: Path) -> Paths:
    return get_absolute_array(
        _get_relative_archive(archive_path), root_path=archive_root
    )


def _get_took_out(archive_path: Path) -> Paths:
    archive_root: Path = Path(archive_path.stem)
    return [archive_root] + _replace_path_root(archive_path, archive_root)


def _get_took_out_list(archive_paths: Paths) -> Paths:
    file_paths: Paths = []

    for archive_path in archive_paths:
        file_paths += _get_took_out(archive_path)

    return file_paths


def _compare_path_test(left: Paths, right: Paths) -> None:
    assert 1 == len(set([str(sorted(paths)) for paths in [left, right]]))


def _compare_took_out(
    archive_status: ArchiveStatus, archive_paths: Paths
) -> None:
    _compare_path_test(
        _get_took_out_list(archive_paths), archive_status["take"]
    )


def _compare_keep(archive_status: ArchiveStatus) -> None:
    _compare_path_test(
        _get_relative_archive(archive_status["archive"]),
        archive_status["keep"],
    )


def _took_out_and_keep(
    archive_paths: Paths, archive_status: ArchiveStatus
) -> None:
    _compare_took_out(archive_status, archive_paths)
    _compare_keep(archive_status)


def _compare_path(result: Path, expected: Path) -> None:
    assert result.exists()
    assert result == expected


def _compare_relative(working: PathPair, archive_paths: Paths) -> None:
    assert False not in is_relative_array(
        archive_paths, root_path=working["specific"]
    )


def _get_remove_expected(archive_status: ArchiveStatus) -> Paths:
    return archive_status["take"] + [Path(archive_status["archive"].name)]


def _compare_remove(trash_root: Path, archive_status: ArchiveStatus) -> None:
    _compare_path_test(
        _find_relative_paths(trash_root), _get_remove_expected(archive_status)
    )


def _filter_paths(paths: Paths | None) -> Paths:
    if paths is None:
        fail()

    return paths


def _open_archive(
    archive_status: ArchiveStatus, take_out_archive: TakeOutArchive
) -> None:
    take_out_archive.open_archive(archive_path=archive_status["archive"])


def _get_take_out(archive_status: ArchiveStatus) -> TakeOutArchive:
    take_out_archive = TakeOutArchive()
    _open_archive(archive_status, take_out_archive)
    return take_out_archive


def _get_take_out_protect(archive_status: ArchiveStatus) -> TakeOutArchive:
    take_out_archive = TakeOutArchive()
    take_out_archive.open_archive(
        archive_path=archive_status["archive"], protected=True
    )
    return take_out_archive


def _get_take_out_remove(
    working: PathPair, archive_status: ArchiveStatus
) -> TakeOutArchive:
    take_out_archive = TakeOutArchive(trash_root=working["remove"])
    _open_archive(archive_status, take_out_archive)
    return take_out_archive


def _close_archive(
    took_out_paths: Paths | None, take_out_archive: TakeOutArchive
) -> Paths:
    archive_paths: Paths = _filter_paths(took_out_paths)
    take_out_archive.close_archive()
    return archive_paths


def _take_out_close(take_out_archive: TakeOutArchive) -> Paths:
    return _close_archive(take_out_archive.take_out(), take_out_archive)


def _take_out_close_specific(
    working: PathPair, take_out_archive: TakeOutArchive
) -> Paths:
    return _close_archive(
        take_out_archive.take_out(took_out_root=working["specific"]),
        take_out_archive,
    )


def _default_test(archive_status: ArchiveStatus) -> None:
    _took_out_and_keep(
        _take_out_close(_get_take_out(archive_status)), archive_status
    )


def _take_test(working: PathPair, archive_status: ArchiveStatus) -> None:
    take_out_archive: TakeOutArchive = _get_take_out(archive_status)
    _take_out_close_specific(working, take_out_archive)

    _compare_path(take_out_archive.get_took_out_root(), working["specific"])


def _specific_test(working: PathPair, archive_status: ArchiveStatus) -> None:
    archive_paths: Paths = _take_out_close_specific(
        working, _get_take_out(archive_status)
    )

    _took_out_and_keep(archive_paths, archive_status)
    _compare_relative(working, archive_paths)


def _protect_test(archive_status: ArchiveStatus) -> None:
    _took_out_and_keep(
        _take_out_close(_get_take_out_protect(archive_status)), archive_status
    )


def _remove_test(working: PathPair, archive_status: ArchiveStatus) -> None:
    take_out_archive: TakeOutArchive = _get_take_out_remove(
        working, archive_status
    )

    _took_out_and_keep(_take_out_close(take_out_archive), archive_status)
    _compare_remove(take_out_archive.get_trash_root(), archive_status)


def _create_directory_default(temporary_root: Path) -> PathPair:
    return _create_working_directory(temporary_root, _get_directory_names())


def _create_directory_specific(temporary_root: Path) -> PathPair:
    return _create_working_directory(
        temporary_root, _get_directory_names() + ["specific"]
    )


def _create_directory_remove(temporary_root: Path) -> PathPair:
    return _create_working_directory(
        temporary_root, _get_directory_names() + ["remove"]
    )


def test_error() -> None:
    """Test to confirm that path used for take out archives is undefined."""
    take_out_archive = TakeOutArchive()

    with raises(ValueError):
        take_out_archive.get_took_out_root()


def test_compleat() -> None:
    """Test to take out directory from inside of archive.

    But, directory doesn't exist in inside of archive.
    """

    def individual_test(temporary_root: Path) -> None:
        _default_test(
            _create_archive_compleat(_create_directory_default(temporary_root))
        )

    _inside_temporary_directory(individual_test)


def test_empty() -> None:
    """Test to take out directory from inside of archive.

    But, only empty directory is exist in inside of archive.
    """

    def individual_test(temporary_root: Path) -> None:
        _default_test(
            _create_archive_empty(_create_directory_default(temporary_root))
        )

    _inside_temporary_directory(individual_test)


def test_single() -> None:
    """Test to take out directory from inside of archive.

    Archive include single directory with single file.
    """

    def individual_test(temporary_root: Path) -> None:
        _default_test(
            _create_archive_single(_create_directory_default(temporary_root))
        )

    _inside_temporary_directory(individual_test)


def test_multiple() -> None:
    """Test to take out directory from inside of archive.

    Archive include single directory with multiple file.
    """

    def individual_test(temporary_root: Path) -> None:
        _default_test(
            _create_archive_multiple(_create_directory_default(temporary_root))
        )

    _inside_temporary_directory(individual_test)


def test_mix() -> None:
    """Test to take out directory from inside of archive.

    Archive include single file and single directory with single file.
    """

    def individual_test(temporary_root: Path) -> None:
        _default_test(
            _create_archive_mix(_create_directory_default(temporary_root))
        )

    _inside_temporary_directory(individual_test)


def test_list() -> None:
    """Test to take out directory from inside of archive.

    Archive include multiple directories with single file.
    """

    def individual_test(temporary_root: Path) -> None:
        _default_test(
            _create_archive_list(_create_directory_default(temporary_root))
        )

    _inside_temporary_directory(individual_test)


def test_nest() -> None:
    """Test to take out directory from inside of archive.

    Archive include nested directories with single file.
    """

    def individual_test(temporary_root: Path) -> None:
        _default_test(
            _create_archive_nest(_create_directory_default(temporary_root))
        )

    _inside_temporary_directory(individual_test)


def test_override() -> None:
    """Test to take out directory from inside of archive.

    Avoid override of path when take out directory in archive.
    """

    def individual_test(temporary_root: Path) -> None:
        _default_test(
            _create_archive_override(_create_directory_default(temporary_root))
        )

    _inside_temporary_directory(individual_test)


def test_path() -> None:
    """Test to get path of directory used for take out archives."""

    def individual_test(temporary_root: Path) -> None:
        working: PathPair = _create_directory_specific(temporary_root)
        _take_test(working, _create_archive_single(working))

    _inside_temporary_directory(individual_test)


def test_specific() -> None:
    """Test to take out directory from inside of archive.

    Take out directory from archive to specific root directory.
    """

    def individual_test(temporary_root: Path) -> None:
        working: PathPair = _create_directory_specific(temporary_root)
        _specific_test(working, _create_archive_specific(working))

    _inside_temporary_directory(individual_test)


def test_protect() -> None:
    """Test to take out directory from inside of archive.

    Take out directory from protected archive, but archive isn't updated.
    """

    def individual_test(temporary_root: Path) -> None:
        _protect_test(
            _create_archive_protect(_create_directory_default(temporary_root))
        )

    _inside_temporary_directory(individual_test)


def test_remove() -> None:
    """Test to take out directory from inside of archive.

    File or directory is removed to specific trash box in test.
    """

    def individual_test(temporary_root: Path) -> None:
        working: PathPair = _create_directory_remove(temporary_root)
        _remove_test(working, _create_archive_single(working))

    _inside_temporary_directory(individual_test)
