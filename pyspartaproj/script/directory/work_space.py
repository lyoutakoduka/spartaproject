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

    def get_selected_root(self, selected_root: Path | None) -> Path:
        """Get temporary working space.

        Return Python default temporary working space
            if argument "selected_root" is None.

        Or user defined temporary working space is returned if Not None.

        Args:
            selected_root (Path | None):
                Path of temporary working space you want to specified.

        Returns:
            Path: Path of selected temporary working space.
        """
        return (
            self.get_working_root() if selected_root is None else selected_root
        )

    def create_date_time_space(
        self,
        head_root: Path | None = None,
        body_root: Path | None = None,
        foot_root: Path | None = None,
        override: bool = False,
        jst: bool = False,
    ) -> Path:
        """Create temporary working space that path include date time string.

        Define of words.

        Working Root: Python temporary working space in default.
            You can specify other directory by argument "body_root".

        Date Time Root: Directory tree that path include date time string.
            It's created on Working Root.

            e.g., following directory tree is created
                if you use this function at "2023/4/1:00:00:00-00".

            "<Working Root>/2023/04/01/00/00/00/000000"

        Head Root: Directory tree which is placed to Working Root.
            In addition, Date Time Root is placed to Head Root.

            e.g., following directory tree is created
                if argument "head_root" is "main/sub".

            "<Working Root>/main/sub/<Date Time Root>"

        Foot Root: Directory tree which is placed to Date Time Root.

            e.g., following directory tree is created
                if argument "foot_root" is "main/sub".

            "<Working Root>/<Date Time Root>/main/sub"

        Args:
            head_root (Path | None, optional): Defaults to None.
                You can specify Head Root here.

            body_root (Path | None, optional): Defaults to None.
                You can specify unique Working Root here.

            foot_root (Path | None, optional): Defaults to None.
                You can specify Foot Root here.

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
        selected_root: Path = self.get_selected_root(body_root)

        if head_root is not None:
            selected_root = Path(selected_root, head_root)

        working_root: Path = create_working_space(
            selected_root, override=override, jst=jst
        )

        if foot_root is None:
            return working_root

        return self.create_sub_directory(foot_root, selected_root=working_root)

    def create_sub_directory(
        self, sub_root: Path, selected_root: Path | None = None
    ) -> Path:
        """Create sub directory in selected temporary working space.

        In default, directory is created to Python temporary working space.

        If argument "sub_root" is "main/sub",
            and "selected_root" is "root/directory",
            path "root/directory/main/sub" is crated and returned.

        Args:
            sub_root (Path): Relative path of sub directory.

            selected_root (Path | None, optional): Defaults to None.
                Path of directory you want to create sub directory.

        Returns:
            Path: Path of created sub directory.
        """
        return create_directory(
            Path(self.get_selected_root(selected_root), sub_root)
        )

    def get_working_root(self) -> Path:
        """Get path of default temporary working space.

        Returns:
            Path: Path of default temporary working space.
        """
        return self._working_root

    def __del__(self) -> None:
        """Remove default temporary working space."""
        if self._root_specified:
            rmtree(str(self._working_root))

    def __init__(self, working_root: Path | None = None) -> None:
        """Create default temporary working space.

        Args:
            working_root (Path | None, optional): Defaults to None.
                User defined temporary working space.
                It's mainly used for test.
        """
        self._initialize_variables(working_root)
