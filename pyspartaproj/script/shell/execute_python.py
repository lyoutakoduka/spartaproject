#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to execute Python depends on OS."""

from pathlib import Path
from platform import uname

from pyspartaproj.context.default.string_context import StrGene, Strs
from pyspartaproj.context.extension.path_context import PathPair
from pyspartaproj.script.path.modify.get_absolute import get_absolute
from pyspartaproj.script.shell.execute_command import execute_command


def get_interpreter_path() -> Path:
    platform: str = uname().system

    platform_pythons: PathPair = {
        "Linux": Path("poetry", "linux", ".venv", "bin", "python"),
        "Windows": Path("poetry", "windows", ".venv", "Scripts", "python.exe"),
    }

    if platform in platform_pythons:
        return get_absolute(platform_pythons[platform])
    else:
        raise FileNotFoundError


def execute_python(commands: Strs) -> StrGene:
    """Execute Python depends on OS.

    Args:
        commands (Strs): Script you want execute and arguments of itself

    Returns:
        Strs: Stdout of Script path you want execute
    """
    return execute_command([get_interpreter_path().as_posix()] + commands)
