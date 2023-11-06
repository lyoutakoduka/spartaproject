#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get version information of Python interpreter."""

from pathlib import Path

from pyspartaproj.script.shell.execute_command import execute_single


def get_version_name(version: str) -> str:
    """Function to convert version string as default directory name.

    Args:
        version (str): version information formatted like "3.12.0"

    Returns:
        str: formatted version string like "Python-3.12.0"
    """
    return "python".capitalize() + "-" + version


def get_interpreter_version(executable: Path) -> str:
    """Function to get version information of specific interpreter.

    Args:
        executable (Path): interpreter path you want to get version

    Returns:
        str: version information formatted like "3.12.0"
    """
    return list(execute_single([str(executable), "-V"]))[0].split(" ")[-1]
