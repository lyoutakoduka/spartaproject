#!/usr/bin/env python

"""Module to execute Python corresponding to platform."""

from pathlib import Path

from pyspartalib.context.default.string_context import StrGene, Strs, Strs2
from pyspartalib.context.extension.path_context import Paths
from pyspartalib.script.project.project_context import ProjectContext
from pyspartalib.script.shell.execute_command import execute_multiple


def _merge_context_path(project: ProjectContext) -> Path:
    return project.merge_paths(
        "interpreter",
        ["working", "virtual", "runtime"],
    )


def _get_environment() -> str:
    return "pythonpath".upper()


def _get_path_texts(python_paths: Paths) -> Strs:
    return [str(python_path) for python_path in python_paths]


def _get_system_path_value(python_paths: Paths) -> str:
    return ":".join([*_get_path_texts(python_paths), "$" + _get_environment()])


def _get_environment_pair(python_paths: Paths) -> str:
    return _get_environment() + "=" + _get_system_path_value(python_paths)


def _get_system_path(python_paths: Paths) -> Strs:
    return ["export", _get_environment_pair(python_paths)]


def _filter_system_path(python_paths: Paths | None) -> bool:
    return python_paths is not None and len(python_paths) > 0


def _get_python_command(
    commands: Strs,
    platform: str | None,
    forward: Path | None,
) -> Strs:
    return [
        get_script_string(
            get_runtime_path(platform=platform, forward=forward),
        ),
        *commands,
    ]


def get_runtime_path(
    platform: str | None = None,
    forward: Path | None = None,
) -> Path:
    """Get interpreter path of Python corresponding to platform.

    Args:
        platform (str | None, optional): Defaults to None.
            You can select an execution platform from "linux" or "windows".
            Current execution platform is selected if argument is None.

        forward (Path | None, optional): Defaults to None.
            Path of setting file in order to place
                project context file to any place.
            It's used for argument "forward" of class "ProjectContext".

    Raises:
        FileNotFoundError:
            Throw an exception if interpreter path you selected isn't exists.

    Returns:
        Path: Relative path of Python interpreter.

    """
    return _merge_context_path(
        ProjectContext(platform=platform, forward=forward),
    )


def get_script_string(path: Path) -> str:
    """Convert to the format which is necessary for executing script in Python.

    Args:
        path (Path): Path you want to convert.

    Returns:
        str: Convert path which can executed in Python.

    """
    return str(path)  # Not as_posix()


def execute_python(
    commands: Strs,
    python_paths: Paths | None = None,
    platform: str | None = None,
    forward: Path | None = None,
) -> StrGene:
    """Execute Python corresponding to platform.

    Args:
        commands (Strs): Script you want execute and arguments of itself.

        python_paths (Paths | None, optional): Defaults to None.
            Paths you want to add to Python system path before execute Python.

        platform (str | None, optional): Defaults to None.
            You can select an execution platform from "linux" or "windows".
            Current execution platform is selected if argument is None.
            It's used for argument "platform" of class "ProjectContext".

        forward (Path | None, optional): Defaults to None.
            Path of setting file in order to place
                project context file to any place.
            It's used for argument "forward" of class "ProjectContext".

    Returns:
        StrGene: Generator for getting stdout of the script you want execute.

    """
    command_multiple: Strs2 = []

    if filtered_paths := python_paths:
        command_multiple += [_get_system_path(filtered_paths)]

    command_multiple += [_get_python_command(commands, platform, forward)]

    return execute_multiple(command_multiple)
