#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import system
from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.file.json.project_context import ProjectContext
from pyspartaproj.script.file.text.import_file import text_import


def _get_powershell_path() -> str:
    project = ProjectContext()
    return project.get_path_context("runtime")[
        project.get_platform_key(["powershell"]) + ".path"
    ].as_posix()


def execute_powershell(command: str) -> Strs:
    shell_commands: Strs = [_get_powershell_path(), command]

    with TemporaryDirectory() as temporary_directory:
        stdout_path: Path = Path(temporary_directory, "stdout.txt")
        shell_commands += [">", stdout_path.as_posix()]

        system(" ".join(shell_commands))

        return text_import(stdout_path).splitlines()


def get_path_string(path: Path) -> str:
    return str(path)  # Not as_posix()


def get_quoted_paths(path: Path) -> str:
    return get_path_string(path).join(["'"] * 2)


def get_script_executable(commands_execute: Strs) -> str:
    return " ".join(commands_execute).join(['"'] * 2)
