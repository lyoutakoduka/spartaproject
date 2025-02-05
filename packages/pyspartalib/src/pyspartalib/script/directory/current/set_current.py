#!/usr/bin/env python

"""Module to set current working directory."""

from os import chdir
from pathlib import Path


def set_current(path: Path) -> None:
    """Set current working directory.

    Args:
        path (Path): Current working directory you want to set.

    """
    chdir(path)
