#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get current working directory that allow symbolic link."""

from os import environ
from pathlib import Path

from pyspartaproj.script.execute.execute_command import execute_command


def get_current() -> Path:
    """Get current working directory that allow symbolic link.

    Not Path.cwd() or os.getcwd()

    Returns:
        Path: current working directory
    """
    key: str = "PWD"

    if key not in environ:
        environ[key] = execute_command(["pwd"])[0]

    return Path(environ[key])
