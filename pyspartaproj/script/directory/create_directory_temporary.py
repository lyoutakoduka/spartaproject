#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from shutil import rmtree
from tempfile import mkdtemp


class WorkSpace:
    def __init__(self) -> None:
        self._work_space_root = Path(mkdtemp())

    def __del__(self) -> None:
        rmtree(str(self._work_space_root))

    def get_root(self) -> Path:
        return self._work_space_root
