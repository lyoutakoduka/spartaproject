#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to create temporary working space shared in class."""

from pathlib import Path
from shutil import rmtree
from tempfile import mkdtemp

from pyspartaproj.script.directory.create_directory import create_directory


class WorkSpace:
    """Class to create temporary working space shared in class."""

    def _initialize_variables(self, working_root: Path | None) -> None:
        self._root_specified: bool = False

        if working_root is None:
            self._root_specified = True
            working_root = Path(mkdtemp())

        self._working_root: Path = working_root

    def create_sub_directory(self, group: str) -> Path:
        """Create sub directory in temporary working space.

        Args:
            group (str): Name of directory you want to create.

        Returns:
            Path: Path of created sub directory.
        """
        return create_directory(Path(self._working_root, group))

    def get_working_root(self) -> Path:
        """Get path of temporary working space.

        Returns:
            Path: Path of temporary working space.
        """
        return self._working_root

    def __del__(self) -> None:
        """Remove temporary working space."""
        if self._root_specified:
            rmtree(str(self._working_root))

    def __init__(self, working_root: Path | None = None) -> None:
        """Create temporary working space.

        Args:
            working_root (Path | None, optional): Defaults to None.
                Path for user defined temporary working space.
        """
        self._initialize_variables(working_root)
