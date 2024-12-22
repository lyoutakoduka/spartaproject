#!/usr/bin/env python

"""Test to execute Python corresponding to platform."""

from pathlib import Path

from pyspartalib.context.default.string_context import StrGene, Strs
from pyspartalib.context.extension.path_context import PathPair, Paths
from pyspartalib.script.path.modify.current.get_absolute import get_absolute
from pyspartalib.script.path.modify.current.get_relative import (
    get_relative,
    is_relative,
)
from pyspartalib.script.path.modify.get_resource import get_resource
from pyspartalib.script.platform.platform_status import (
    get_platform,
    is_platform_linux,
)
from pyspartalib.script.shell.execute_python import (
    execute_python,
    get_runtime_path,
    get_script_string,
)


def _get_config_file() -> Path:
    return get_resource(local_path=Path("forward.json"))


def _execute_python(commands: Strs) -> StrGene:
    return execute_python(commands, forward=_get_config_file())


def _execute_python_path(commands: Strs, python_paths: Paths) -> StrGene:
    return execute_python(
        commands,
        forward=_get_config_file(),
        python_paths=python_paths,
    )


def _execute_python_platform(commands: Strs, platform: str) -> StrGene:
    return execute_python(
        commands,
        forward=_get_config_file(),
        platform=platform,
    )


def _get_script_text(script_text: str) -> str:
    return get_script_string(
        get_resource(local_path=Path("tools", script_text)),
    )


def _get_script_texts(script_name: str) -> Strs:
    return [_get_script_text(script_name + ".py")]


def _get_system_paths(expected: Paths, first_root: Path) -> Paths:
    system_paths: Paths = []

    for result in _execute_python_path(_get_script_texts("system"), expected):
        path: Path = Path(result)

        if is_relative(path, root_path=get_absolute(first_root)):
            system_paths += [get_relative(path)]

    return system_paths


def _compare_system_paths(expected: Paths, results: Paths) -> None:
    if len({str(sorted(paths)) for paths in [expected, results]}) != 1:
        raise ValueError


def _get_result_platform(platform: str) -> StrGene:
    return _execute_python_platform(
        _get_script_texts("find_platform"),
        platform,
    )


def _get_result_command(expected: str) -> StrGene:
    return _execute_python(_get_script_texts(expected))


def _get_platform_interpreters() -> PathPair:
    virtual: str = ".venv"

    return {
        "linux": Path(virtual, "bin", "python"),
        "windows": Path(".venvs", "windows", virtual, "Scripts", "python.exe"),
    }


def _get_interpreter_path(platform: str) -> Path:
    return get_runtime_path(platform=platform, forward=_get_config_file())


def _get_result_interpreter(platform: str, expected: Path) -> Path:
    return Path(*_get_interpreter_path(platform).parts[-len(expected.parts) :])


def test_path() -> None:
    """Test to convert path to the format for executing script in Python."""
    path_elements: Strs = ["A", "B", "C"]
    identifier: str = "/" if is_platform_linux() else "\\"

    if identifier.join(path_elements) != get_script_string(
        Path(*path_elements),
    ):
        raise ValueError


def test_interpreter() -> None:
    """Test to get interpreter path of Python corresponding to platform."""
    platform: str = get_platform()
    expected: Path = _get_platform_interpreters()[platform]

    if expected != _get_result_interpreter(platform, expected):
        raise ValueError


def test_command() -> None:
    """Test to execute simple Python script."""
    expected: str = "simple"

    if [expected] != list(_get_result_command(expected)):
        raise ValueError


def test_platform() -> None:
    """Test to execute Python script for all executable platform."""
    expected: str = get_platform()

    if [expected] != list(_get_result_platform(expected)):
        raise ValueError


def test_system() -> None:
    """Test to add Python system path before execute Python."""
    first_root: Path = Path(get_resource(), "local_import", "directory_first")
    expected: Paths = [first_root, Path(first_root, "directory_second")]

    _compare_system_paths(expected, _get_system_paths(expected, first_root))
