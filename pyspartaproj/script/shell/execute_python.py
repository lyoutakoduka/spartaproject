#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to execute Python corresponding to platform."""

from pathlib import Path

from pyspartaproj.context.default.string_context import StrGene, Strs, Strs2
from pyspartaproj.context.extension.path_context import Paths
from pyspartaproj.script.project.project_context import ProjectContext
from pyspartaproj.script.shell.execute_command import execute_multiple


def get_interpreter_path(
    platform: str | None = None, forward: Path | None = None
) -> Path:
    """Function to get interpreter path of Python corresponding to platform.

    Args:
        platform (str | None, optional): Defaults to None.
            You can select an execution platform from "linux" or "windows".
            Current execution platform is selected if argument is None.

    Raises:
        FileNotFoundError:
            Throw an exception if interpreter path you selected isn't exists.

    Returns:
        Path: Relative path of Python interpreter.
    """
    project = ProjectContext(platform=platform, forward=forward)
    interpreter_path: Path = project.merge_platform_path(
        "project", ["working", "platform"], file_type="interpreter"
    )

    if not interpreter_path.exists():
        raise FileNotFoundError()

    return interpreter_path


def get_script_string(path: Path) -> str:
    """Convert to the format which is necessary for executing script in Python.

    Args:
        path (Path): Path you want to convert.

    Returns:
        str: Convert path which can executed in Python.
    """
    return str(path)  # Not as_posix()


def _get_environment() -> str:
    return "pythonpath".upper()


def _get_system_path_value(python_paths: Paths) -> str:
    path_texts: Strs = [str(python_path) for python_path in python_paths]
    return ":".join(path_texts + ["$" + _get_environment()])


def _get_python_system_path(python_paths: Paths) -> Strs:
    return [
        "export",
        _get_environment() + "=" + _get_system_path_value(python_paths),
    ]


def _get_python_command(commands: Strs, platform: str | None) -> Strs:
    return [get_script_string(get_interpreter_path(platform))] + commands


def execute_python(
    commands: Strs,
    python_paths: Paths | None = None,
    platform: str | None = None,
) -> StrGene:
    """Execute Python corresponding to platform.

    Args:
        commands (Strs): Script you want execute and arguments of itself.

        python_paths (Paths | None, optional): Defaults to None.
            Paths you want to add to Python system path before execute Python.

        platform (str | None, optional): Defaults to None.
            You can select an execution platform from "linux" or "windows".
            Current execution platform is selected if argument is None.

    Returns:
        StrGene: Generator for getting stdout of the script you want execute.
    """
    command_multiple: Strs2 = []

    if python_paths is not None and 0 < len(python_paths):
        command_multiple += [_get_python_system_path(python_paths)]

    command_multiple += [_get_python_command(commands, platform)]

    return execute_multiple(command_multiple)
