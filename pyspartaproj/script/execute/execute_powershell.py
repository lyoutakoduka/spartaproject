#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import system
from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.file.text.import_file import text_import


def execute_powershell(command: str) -> Strs:
    shell_commands: Strs = ["powershell", command]

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
