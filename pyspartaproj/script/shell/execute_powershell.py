#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to execute specific commands in PowerShell."""

from pathlib import Path
from platform import uname

from pyspartaproj.context.default.string_context import StrGene, Strs
from pyspartaproj.script.project.project_context import ProjectContext
from pyspartaproj.script.shell.execute_command import execute_single


def _get_powershell_path() -> str:
    project = ProjectContext()
    return project.get_path_context("runtime")[
        project.get_platform_key(["powershell"]) + ".path"
    ].as_posix()


def execute_powershell(commands: Strs) -> StrGene:
    """Function to execute specific command in PowerShell.

    Args:
        commands (Strs): Elements of command which will merged by space.
            e.g., if command is "Write-Output Test",
            you can input ["Write-Output", "Test"] or ["Write-Output Test"].

    Returns:
        StrGene: Generator for getting stdout of command  you want execute.
    """
    shell_commands: Strs = [
        _get_powershell_path(),
        "-ExecutionPolicy",
        "Bypass",
    ] + commands

    return execute_single(shell_commands)


def get_script_string(path: Path) -> str:
    """Convert path string in order to execute command in PowerShell.

    e.g., simplified command for execution in PowerShell is follow.

    "powershell.exe directory/script.ps1 argument"

    The path will convert is called "script part",
        and its "directory/script.ps1" in above example.

    Args:
        path (Path): Script part path you want to convert.

    Returns:
        str: Converted script part which used "slash"
            as directory separator character.
    """
    return path.as_posix()  # Not str()


def get_path_string(path: Path) -> str:
    """Convert path string in order to execute command in PowerShell.

    e.g., simplified command for execution in PowerShell is follow.

    "powershell.exe script.ps1 directory/argument"

    The path will convert is called "argument part",
        and its "directory/argument" in above example.

    Args:
        path (Path): Argument part path you want to convert.

    Returns:
        str: Converted argument part which used "back slash"
            as directory separator character.
    """
    path_text: str = str(path)

    if "Linux" == uname().system:
        return path_text.replace("/", "\\")

    return path_text


def get_quoted_path(path: str) -> str:
    """Get path surrounded by quotation for executing command on PowerShell.

    If you select argument (path) is "root/directory/file",
        "'root/directory/file'" is returned.

    Args:
        path (str): Path you want surround by quotation.

    Returns:
        str: Path surrounded by quotation.
    """
    return path.join(["'"] * 2)


def get_double_quoted_command(commands: Strs) -> str:
    """Convert command string in order to execute command in PowerShell.

    e.g., simplified command for execution in PowerShell is follow.

    "powershell.exe script.ps1 argument"

    The path will convert is called "command part",
        and its "script.ps1 argument" in above example.

    If you select argument (commands) like ["script.ps1", "argument"],
        '"script.ps1 argument"' is returned.

    Args:
        commands (Strs): Command part path you want to convert.

    Returns:
        str: Converted command part surrounded by double quotation.
    """
    return " ".join(commands).join(['"'] * 2)


def convert_mount_path(path: Path) -> Path:
    """Convert shared path between Linux and Windows.

    e.g., if you select argument (path) like "/mnt/c/Users/user",
        "C:/Users/user" is returned.

    Args:
        path (Path): Linux path which is starts from mount string.

    Returns:
        Path: Converted Windows path which is starts from drive letter.
    """
    path_text: str = path.as_posix()
    mount: str = "/mnt/"

    if not path_text.startswith(mount):
        return path

    index: int = len(mount)
    index_right: int = index + 1

    return Path(path_text[index].capitalize() + ":" + path_text[index_right:])
