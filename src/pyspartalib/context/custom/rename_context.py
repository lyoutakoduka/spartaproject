#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""User defined types using class SafeRename."""

from pathlib import Path
from typing import Callable

from pyspartalib.script.path.safe.safe_rename import SafeRename

RenamePathFunc = Callable[[SafeRename, Path], None]
