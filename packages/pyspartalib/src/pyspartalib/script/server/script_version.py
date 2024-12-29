#!/usr/bin/env python

"""Module to get version information of Python interpreter."""

from pathlib import Path

from pyspartalib.script.shell.execute_command import execute_single


def get_version_name(version: str) -> str:
    """Convert version string as default directory name.

    Args:
        version (str): Version information formatted like "3.12.0".

    Returns:
        str: Formatted version string like "Python-3.12.0".

    """
    return "python".capitalize() + "-" + version


def get_interpreter_version(executable: Path) -> str:
    """Get version information of specific interpreter.

    Args:
        executable (Path): Interpreter path you want to get version.

    Returns:
        str: Version information formatted like "3.12.0".

    """
    return list(execute_single([str(executable), "-V"]))[0].split(" ")[-1]
