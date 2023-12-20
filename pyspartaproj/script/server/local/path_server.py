#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to handle paths about file and directory on server."""

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.context.extension.path_context import PathPair
from pyspartaproj.script.directory.create_directory_temporary import WorkSpace
from pyspartaproj.script.directory.create_directory_working import (
    create_working_space,
)
from pyspartaproj.script.path.modify.get_relative import get_relative


class PathServer(WorkSpace):
    """Class to handle paths about file and directory on server.

    WorkSpace: Class to create temporary working directory shared in class.
    """

    def _add_path(self, key: str, child: Path, parent: str | None) -> None:
        if parent is not None:
            child = Path(self.get_path(parent), child)

        self._path_table[key] = child

    def _add_directory(
        self, table: PathPair, parent: str | None = None
    ) -> None:
        for key, name in table.items():
            self._add_path(key, Path(name), parent=parent)

    def _build_path_root(self) -> None:
        self._add_directory(
            {"private_root": Path("private"), "public_root": Path("public")}
        )

    def _build_path_private(self) -> None:
        self._add_directory(
            {"work_root": Path("work"), "develop_root": Path("develop")},
            parent="private_root",
        )

    def _build_path_develop(self) -> None:
        self._add_directory(
            {
                "internal_root": Path("internal"),
                "python_root": Path("external", "python"),
            },
            parent="develop_root",
        )

    def _build_path_table(self) -> None:
        self._path_table: PathPair = {}

        self._build_path_root()
        self._build_path_private()
        self._build_path_develop()

    def get_path_table(self) -> Strs:
        """Get keys of predefined all paths about server.

        Returns:
            Strs: All keys of path.
        """
        return list(self._path_table.keys())

    def get_path(self, path_type: str) -> Path:
        """Get path related with specific key about server.

        Args:
            path_type (str): Key of path you want to get.

        Returns:
            Path: Path related with specific key.
        """
        return self._path_table[path_type]

    def to_relative_path(self, local_full: Path) -> Path:
        """Convert full path to relative path.

        e.g.The full path is "<Python default temporary directory>/example/",
            and returned relative path is "example/".

        Args:
            local (Path): Full path.

        Returns:
            Path: Returned relative path.
        """
        return get_relative(local_full, root_path=self.get_root())

    def to_full_path(self, local_relative: Path) -> Path:
        """Convert relative path to full path.

        e.g. The relative path is "example/",
            and returned full path is
            "<Python default temporary directory>>/example/".

        Args:
            local (Path): Relative path.

        Returns:
            Path: Returned full path.
        """
        return Path(self.get_root(), local_relative)

    def create_local_working_space(
        self, override: bool = False, jst: bool = False
    ) -> Path:
        """Create temporary working space on local environment.

        The path is used when uploading file or directory to server.

        Basic path of temporary working space is follow.
        A datetime element in path is current datetime by default.

        "<Python default temporary directory>/
            private/work/<year>/<month>/<day>/<hour>/<second>/<millisecond>/"

        Args:
            override (bool, optional): Defaults to False.
                If True, the datetime element in path become follow,
                    it's commonly used for test.

                "<Python default temporary directory>/
                    private/work/2023/04/01/00/00/000000/"

            jst (bool, optional): Defaults to False.
                If True, the datetime element is represented by
                    timezone of Asia/Tokyo.

        Returns:
            Path: Path of temporary working space.
        """
        return create_working_space(
            Path(self.get_root(), self.get_path("work_root")),
            override=override,
            jst=jst,
        )

    def __init__(self) -> None:
        """Generate string path pair about server directory."""
        super().__init__()

        self._build_path_table()
