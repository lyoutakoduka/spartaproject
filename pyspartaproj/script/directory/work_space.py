#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to create temporary working space shared in class."""

from pathlib import Path
from shutil import rmtree
from tempfile import mkdtemp

from pyspartaproj.script.directory.create_directory import create_directory
from pyspartaproj.script.directory.date_time_space import create_working_space


class WorkSpace:
    """Class to create temporary working space shared in class."""

    def _initialize_variables(self, working_root: Path | None) -> None:
        self._root_specified: bool = False

        if working_root is None:
            self._root_specified = True
            working_root = Path(mkdtemp())

        self._working_root: Path = working_root

    def create_date_time_space(
        self, sub_root: Path, override: bool = False, jst: bool = False
    ) -> Path:
        """Create temporary working space that path include date time string.

        Args:
            sub_root (str): Path of directory
                that temporary working space will placed.

            override (bool, optional): Defaults to False.
                Override initial time count to "2023/4/1:12:00:00-00 (AM)".
                It's used for argument "override" of
                    function "create_working_space".

            jst (bool, optional): Defaults to False.
                If True, you can get datetime object as JST time zone.
                It's used for argument "jst" of
                    function "create_working_space".

        Returns:
            Path: Path of created temporary working space.
        """
        return create_working_space(
            Path(self.get_working_root(), sub_root), override=override, jst=jst
        )

    def create_sub_directory(self, sub_root: Path) -> Path:
        """Create sub directory in temporary working space.

        Args:
            sub_root (str): Path of directory you want to create.

        Returns:
            Path: Path of created sub directory.
        """
        return create_directory(Path(self._working_root, sub_root))

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
                Path of temporary working space you specified.
        """
        self._initialize_variables(working_root)
