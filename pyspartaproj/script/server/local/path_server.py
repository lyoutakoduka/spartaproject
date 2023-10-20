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
    """Class to handle paths about file and directory on server."""

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

    def __init__(self) -> None:
        """Generate string path pair about server directory."""
        super().__init__()

        self._build_path_table()

    def get_path_table(self) -> Strs:
        """Get keys of predefined all paths about server.

        Returns:
            Strs: all path keys
        """
        return list(self._path_table.keys())

    def get_path(self, path_type: str) -> Path:
        """Get path related with specific key about server.

        Args:
            path_type (str): key of path you want to get

        Returns:
            Path: path related with specific key
        """
        return self._path_table[path_type]

    def get_working_space(
        self, override: bool = False, jst: bool = False
    ) -> Path:
        """Get a path of temporary working space on server.

        the path is used when uploading file or directory to server

        basic path of temporary working space is follow
        a datetime element in path is current datetime by default

        "<project root directory>/
            private/work/<year>/<month>/<day>/<hour>/<second>/<millisecond>/"

        Args:
            override (bool, optional): Defaults to False.
                if True, the datetime element in path become follow,
                    it's commonly used for test.

                "<project root directory>/
                    private/work/2023/04/01/00/00/000000/"

            jst (bool, optional): Defaults to False.
                if True, the datetime element is represented
                    by timezone of Asia/Tokyo

        Returns:
            Path: path of temporary working space
        """
        return create_working_space(
            Path(self.get_root(), self.get_path("work_root")),
            override=override,
            jst=jst,
        )

    def to_remote_relative(self, local: Path) -> Path:
        """Convert full path based on project root directory to relative path.

        e.g. full path based on project root directory is
            "<project root directory>/example/",
            then returned relative path is "example/"

        Args:
            local (Path): full path

        Returns:
            Path: returned relative path
        """
        return get_relative(local, root_path=self.get_root())

    def to_remote_full(self, local: Path) -> Path:
        """Convert relative path to full path based on project root directory.

        e.g. relative path is "example/",
            then returned full path based on project root directory is
            "<project root directory>/example/"

        Args:
            local (Path): relative path

        Returns:
            Path: returned full path
        """
        return Path(self.get_root(), local)
