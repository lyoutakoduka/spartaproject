#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test to execute Python corresponding to platform."""

from pathlib import Path
from platform import uname

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.context.extension.path_context import PathPair, Paths
from pyspartaproj.script.path.modify.current.get_relative import (
    get_relative,
    is_relative,
)
from pyspartaproj.script.path.modify.get_absolute import get_absolute
from pyspartaproj.script.path.modify.get_resource import get_resource
from pyspartaproj.script.shell.execute_python import (
    execute_python,
    get_interpreter_path,
    get_script_string,
)
from pyspartaproj.script.string.temporary_text import temporary_text


def _get_config_file() -> Path:
    return get_resource(local_path=Path("execute_python", "forward.json"))


def _execute_python(commands: Strs) -> Strs:
    return list(execute_python(commands, forward=_get_config_file()))


def _execute_python_path(commands: Strs, python_paths: Paths) -> Strs:
    return list(
        execute_python(
            commands, python_paths=python_paths, forward=_get_config_file()
        )
    )


def _execute_python_platform(commands: Strs, platform: str) -> Strs:
    return list(
        execute_python(commands, platform=platform, forward=_get_config_file())
    )


def _get_script_text(script_text: str) -> str:
    return get_script_string(get_resource(local_path=Path(script_text)))


def _get_system_paths(expected: Paths, first_root: Path) -> Paths:
    system_paths: Paths = []

    for result in _execute_python_path(
        [_get_script_text("local_import.py")], expected
    ):
        path: Path = Path(result)

        if is_relative(path, root_path=get_absolute(first_root)):
            system_paths += [get_relative(path)]

    return system_paths


def _compare_system_paths(expected: Paths, results: Paths) -> None:
    assert 1 == len(set([str(sorted(paths)) for paths in [expected, results]]))


def test_path() -> None:
    """Test to convert path to the format for executing script in Python."""
    path_elements: Strs = ["A", "B", "C"]
    identifier: str = "/" if "Linux" == uname().system else "\\"

    assert identifier.join(path_elements) == get_script_string(
        Path(*path_elements)
    )


def test_interpreter() -> None:
    """Test to get interpreter path of Python corresponding to platform."""
    platforms: Strs = ["linux", "windows"]

    interpreter_paths: PathPair = {
        "linux": Path("bin", "python"),
        "windows": Path("Scripts", "python.exe"),
    }

    for platform in platforms:
        interpreter_path: Path = get_interpreter_path(
            platform=platform, forward=_get_config_file()
        )
        expected: Path = Path(
            "poetry", platform, ".venv", interpreter_paths[platform]
        )
        assert expected == Path(*interpreter_path.parts[-5:])


def test_command() -> None:
    """Test to execute simple Python script."""
    assert temporary_text(3, 3) == list(
        _execute_python([_get_script_text("indices.py")])
    )


def test_platform() -> None:
    """Test to execute Python script for all executable platform."""
    expected: Strs = ["linux", "windows"]

    assert expected == [
        result.lower()
        for platform in expected
        for result in _execute_python_platform(
            [_get_script_text("execute_platform.py")],
            platform,
        )
    ]


def test_system() -> None:
    """Test to add Python system path before execute Python."""
    first_root: Path = Path(get_resource(), "local_import", "directory_first")
    expected: Paths = [first_root, Path(first_root, "directory_second")]

    _compare_system_paths(expected, _get_system_paths(expected, first_root))
