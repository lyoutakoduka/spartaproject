#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to create temporary working directory shared in class."""

from pathlib import Path
from shutil import rmtree
from tempfile import mkdtemp


class WorkSpace:
    """Class to create temporary working directory shared in class."""

    def get_root(self) -> Path:
        """Get root path of temporary working directory."""
        return self._work_space_root

    def __del__(self) -> None:
        """Remove temporary working directory."""
        rmtree(str(self._work_space_root))

    def __init__(self) -> None:
        """Create temporary working directory."""
        self._work_space_root = Path(mkdtemp())
