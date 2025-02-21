#!/usr/bin/env python

"""Module to set current working directory."""

from os import chdir
from pathlib import Path

from pyspartalib.script.directory.current.get_current import get_current
from pyspartalib.script.inherit.inherit_with import InheritWith


class SetCurrent(InheritWith):
    def __initialize_variables(self) -> None:
        self._backup_current_root = get_current()

    def __init__(self) -> None:
        self.__initialize_variables()


def set_current(path: Path) -> None:
    """Set current working directory.

    Args:
        path (Path): Current working directory you want to set.

    """
    chdir(path)
