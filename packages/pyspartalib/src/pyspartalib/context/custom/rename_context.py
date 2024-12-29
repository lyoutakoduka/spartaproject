#!/usr/bin/env python

"""User defined types using class SafeRename."""

from collections.abc import Callable
from pathlib import Path

from pyspartalib.script.path.safe.safe_rename import SafeRename

RenamePathFunc = Callable[[SafeRename, Path], None]
