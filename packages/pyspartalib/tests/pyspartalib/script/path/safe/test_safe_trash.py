#!/usr/bin/env python

"""Test module to remove file or directory and log history."""

from collections.abc import Sized
from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.default.bool_context import BoolPair, Bools
from pyspartalib.context.default.string_context import Strs
from pyspartalib.context.extension.path_context import (
    PathFunc,
    PathPair,
    PathPair2,
    Paths,
)
from pyspartalib.context.type_context import Type
from pyspartalib.script.bool.same_value import bool_same_array
from pyspartalib.script.directory.create_directory import create_directory
from pyspartalib.script.path.iterate_directory import walk_iterator
from pyspartalib.script.path.modify.current.get_relative import (
    get_relative,
    is_relative,
)
from pyspartalib.script.path.safe.safe_trash import SafeTrash
from pyspartalib.script.path.status.check_exists import check_exists_pair
from pyspartalib.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartalib.script.path.temporary.create_temporary_tree import (
    create_temporary_tree,
)
from pyspartalib.script.time.directory.get_time_path import (
    get_initial_time_path,
)


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _none_error(result: Type | None) -> Type:
    if result is None:
        raise ValueError

    return result


def _length_error(result: Sized, expected: int) -> None:
    if len(result) == expected:
        raise ValueError


def _fail_error(status: bool) -> None:
    if not status:
        raise ValueError


def _success_error(status: bool) -> None:
    if status:
        raise ValueError


def _no_exists_error(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError


def _get_trash_root(temporary_root: Path) -> Path:
    return Path(temporary_root, "trash")


def _get_group() -> Strs:
    return [group + ".path" for group in ["source", "destination"]]


def _get_path_pair(source: Path, destination: Path) -> PathPair:
    return dict(zip(_get_group(), [source, destination], strict=True))


def _convert_path_pair(source: Path, safe_trash: SafeTrash) -> PathPair:
    return _get_path_pair(source, safe_trash.get_trash_root())


def _compare_path(result: Path, expected: Path) -> None:
    _no_exists_error(result)
    _difference_error(result, expected)


def _compare_size(history_size: int, history: PathPair2 | None) -> PathPair2:
    filtered: PathPair2 = _none_error(history)

    _length_error(filtered, history_size)

    return filtered


def _compare_not_relative(full_path: Path, root_path: Path) -> None:
    _success_error(is_relative(full_path, root_path=root_path))


def _compare_root(trash_root: Path, safe_trash: SafeTrash) -> None:
    _compare_path(
        safe_trash.get_trash_root(),
        Path(trash_root, get_initial_time_path()),
    )


def _check_exists_pair(path_pair: PathPair) -> BoolPair:
    return check_exists_pair(path_pair)  # To avoid a circular reference.


def _filter_exists_pair(exists_pair: BoolPair) -> Bools:
    return [exists_pair[group] for group in _get_group()]


def _check_path_exists(path_pair: PathPair) -> None:
    exists_array: Bools = _filter_exists_pair(_check_exists_pair(path_pair))

    _fail_error(bool_same_array([not exists_array[0], exists_array[1]]))


def _get_relative_pair(path_pair: PathPair, root_pair: PathPair) -> Paths:
    return [
        get_relative(path_pair[group], root_path=root_pair[group])
        for group in _get_group()
    ]


def _check_path_relative(path_pair: PathPair, root_pair: PathPair) -> None:
    _length_error(set(_get_relative_pair(path_pair, root_pair)), 1)


def _common_test(
    history_size: int,
    history: PathPair2 | None,
    root_pair: PathPair,
) -> None:
    for path_pair in _compare_size(history_size, history).values():
        _check_path_exists(path_pair)
        _check_path_relative(path_pair, root_pair)


def _single_test(history: PathPair2 | None, root_pair: PathPair) -> None:
    _common_test(1, history, root_pair)


def _multiple_test(
    remove_paths: Paths,
    history: PathPair2 | None,
    root_pair: PathPair,
) -> None:
    _common_test(len(remove_paths), history, root_pair)


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def _get_history(safe_trash: SafeTrash) -> PathPair2 | None:
    return safe_trash.get_history()


def _finalize_single(path: Path, safe_trash: SafeTrash) -> PathPair2 | None:
    safe_trash.trash(path)
    return _get_history(safe_trash)


def _finalize_single_relative(
    path: Path,
    relative_root: Path,
    safe_trash: SafeTrash,
) -> PathPair2 | None:
    safe_trash.trash(path, relative_root=relative_root)
    return _get_history(safe_trash)


def _finalize_array(paths: Paths, safe_trash: SafeTrash) -> PathPair2 | None:
    safe_trash.trash_at_once(paths)
    return _get_history(safe_trash)


def _finalize_array_relative(
    paths: Paths,
    relative_root: Path,
    safe_trash: SafeTrash,
) -> PathPair2 | None:
    safe_trash.trash_at_once(paths, relative_root=relative_root)
    return _get_history(safe_trash)


def _get_removal_array(path: Path) -> Paths:
    return list(walk_iterator(path, depth=1))


def _get_remove() -> SafeTrash:
    return SafeTrash()


def _get_remove_work(working_root: Path) -> SafeTrash:
    return SafeTrash(working_root=working_root, override=True)


def _get_remove_trash(trash_root: Path) -> SafeTrash:
    return SafeTrash(trash_root=trash_root, override=True)


def test_work() -> None:
    """Test to compare user defined temporary working space."""

    def individual_test(temporary_root: Path) -> None:
        _compare_root(temporary_root, _get_remove_work(temporary_root))

    _inside_temporary_directory(individual_test)


def test_different() -> None:
    """Test to compare 2 type of temporary working spaces."""

    def individual_test(temporary_root: Path) -> None:
        safe_trash: SafeTrash = _get_remove_trash(temporary_root)
        _compare_not_relative(
            safe_trash.get_trash_root(),
            safe_trash.get_working_root(),
        )

    _inside_temporary_directory(individual_test)


def test_remove() -> None:
    """Test to get temporary working spaces used by trash box."""

    def individual_test(temporary_root: Path) -> None:
        trash_root: Path = _get_trash_root(temporary_root)
        _compare_root(trash_root, _get_remove_trash(trash_root))

    _inside_temporary_directory(individual_test)


def test_file() -> None:
    """Test to remove file, and log history."""

    def individual_test(temporary_root: Path) -> None:
        safe_trash: SafeTrash = _get_remove()

        _single_test(
            _finalize_single(
                create_temporary_file(temporary_root),
                safe_trash,
            ),
            _convert_path_pair(temporary_root, safe_trash),
        )

    _inside_temporary_directory(individual_test)


def test_relative() -> None:
    """Test to remove file which is based on specific root directory."""

    def individual_test(temporary_root: Path) -> None:
        safe_trash: SafeTrash = _get_remove()

        _single_test(
            _finalize_single_relative(
                create_temporary_file(
                    create_directory(_get_trash_root(temporary_root)),
                ),
                temporary_root,
                safe_trash,
            ),
            _convert_path_pair(temporary_root, safe_trash),
        )

    _inside_temporary_directory(individual_test)


def test_exists() -> None:
    """Test to remove same files at twice."""

    def individual_test(temporary_root: Path) -> None:
        safe_trash: SafeTrash = _get_remove()
        temporary_file: Path = create_temporary_file(temporary_root)

        _single_test(
            _finalize_array([temporary_file] * 2, safe_trash),
            _convert_path_pair(temporary_root, safe_trash),
        )

    _inside_temporary_directory(individual_test)


def test_tree() -> None:
    """Test to remove files and directories, and log history."""

    def individual_test(temporary_root: Path) -> None:
        create_temporary_tree(temporary_root, tree_deep=3)
        remove_paths: Paths = _get_removal_array(temporary_root)
        safe_trash: SafeTrash = _get_remove()

        _multiple_test(
            remove_paths,
            _finalize_array_relative(remove_paths, temporary_root, safe_trash),
            _convert_path_pair(temporary_root, safe_trash),
        )

    _inside_temporary_directory(individual_test)


def test_select() -> None:
    """Test to remove file, and using specific trash box path."""

    def individual_test(temporary_root: Path) -> None:
        create_temporary_tree(temporary_root)

        remove_paths: Paths = _get_removal_array(temporary_root)
        safe_trash: SafeTrash = _get_remove_trash(
            _get_trash_root(temporary_root),
        )

        _multiple_test(
            remove_paths,
            _finalize_array(remove_paths, safe_trash),
            _convert_path_pair(temporary_root, safe_trash),
        )

    _inside_temporary_directory(individual_test)
