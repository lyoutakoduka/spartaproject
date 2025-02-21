#!/usr/bin/env python

"""Module to set current working directory."""

from os import chdir
from pathlib import Path

from pyspartalib.script.directory.current.get_current import get_current
from pyspartalib.script.inherit.inherit_with import InheritWith


class SetCurrent(InheritWith):
    def __initialize_variables(self) -> None:
        self._backup_current_root = get_current()

    def _set_current(self, path: Path) -> None:
        chdir(path)

    def exit(self) -> None:
        self._set_current(self._backup_current_root)

    def __init__(self, current_root: Path) -> None:
        self.__initialize_variables()
        self._set_current(current_root)


def set_current(path: Path) -> None:
    """Set current working directory.

    Args:
        path (Path): Current working directory you want to set.

    """
    chdir(path)
