#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to execute Python corresponding to platform."""

from pathlib import Path

from pyspartaproj.context.default.string_context import StrGene, Strs
from pyspartaproj.context.extension.path_context import Paths
from pyspartaproj.script.project.project_context import ProjectContext
from pyspartaproj.script.shell.execute_command import execute_single


def _get_interpreter_path(platform: str | None) -> Path:
    project = ProjectContext(platform=platform)
    return project.merge_platform_path(
        "project", ["working", "platform"], file_type="interpreter"
    )


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


def execute_python(
    commands: Strs,
    python_paths: Paths | None = None,
    platform: str | None = None,
) -> StrGene:
    """Execute Python corresponding to platform.

    Args:
        commands (Strs): Script you want execute and arguments of itself.

        platform (str | None, optional): Defaults to None.
            You can select execution platform of from "linux" or "windows".

    Returns:
        StrGene: Generator for getting stdout of the script you want execute.
    """
    return execute_single(
        [get_script_string(_get_interpreter_path(platform))] + commands
    )
