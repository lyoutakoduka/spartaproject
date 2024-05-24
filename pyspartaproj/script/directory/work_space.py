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

    def _initialize_variables(self) -> None:
        self._working_root: Path = Path(mkdtemp())

    def _get_selected_root(self, selected_root: Path | None) -> Path:
        return (
            self.get_working_root() if selected_root is None else selected_root
        )

    def create_date_time_space(
        self, selected_root: Path, override: bool = False, jst: bool = False
    ) -> Path:
        """Create temporary working space that path include date time string.

        Args:
            selected_root (Path | None, optional): Defaults to None.
                Path of directory that temporary working space will placed.

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
            self._get_selected_root(selected_root), override=override, jst=jst
        )

    def create_sub_directory(self, selected_root: Path) -> Path:
        """Create sub directory in selected temporary working space.

        Args:
            selected_root (Path | None, optional): Defaults to None.
                Path of directory you want to create.

        Returns:
            Path: Path of created sub directory.
        """
        return create_directory(self._get_selected_root(selected_root))

    def get_working_root(self) -> Path:
        """Get path of temporary working space.

        Returns:
            Path: Path of temporary working space.
        """
        return self._working_root

    def __del__(self) -> None:
        """Remove temporary working space."""
        rmtree(str(self._working_root))

    def __init__(self) -> None:
        """Create default temporary working space."""
        self._initialize_variables()
