#!/usr/bin/env python

"""Module to handle paths about file and directory on server."""

from pathlib import Path

from pyspartalib.context.default.string_context import Strs
from pyspartalib.context.extension.path_context import PathPair
from pyspartalib.script.directory.working.working_space import WorkSpace
from pyspartalib.script.path.modify.current.get_relative import get_relative


class PathServer(WorkSpace):
    """Class to handle paths about file and directory on server."""

    def __initialize_super_class(self, working_root: Path | None) -> None:
        super().__init__(working_root=working_root)

    def _add_path(self, key: str, child: Path, parent: str | None) -> None:
        if parent is not None:
            child = Path(self.get_path(parent), child)

        self._path_table[key] = child

    def _add_directory(
        self,
        table: PathPair,
        parent: str | None = None,
    ) -> None:
        for key, name in table.items():
            self._add_path(key, Path(name), parent=parent)

    def _build_path_root(self) -> None:
        self._add_directory(
            {"private_root": Path("private"), "public_root": Path("public")},
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

    def _initialize_paths(
        self,
        local_root: Path | None,
        override: bool,
        jst: bool,
    ) -> None:
        self._local_root: Path = self.get_selected_root(local_root)
        self._date_time_root: Path = self.create_date_time_space(
            body_root=local_root,
            head_root=self.get_path("work_root"),
            override=override,
            jst=jst,
        )

    def __initialize_variables(
        self,
        local_root: Path | None,
        override: bool,
        jst: bool,
    ) -> None:
        self._build_path_table()
        self._initialize_paths(local_root, override, jst)

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

    def get_local_root(self) -> Path:
        """Get path of local working space used when connecting server.

        Returns:
            Path: Path of local working space.

        """
        return self._local_root

    def get_date_time_root(self) -> Path:
        """Get path of local temporary working space.

        Path include string of current date time.

        Returns:
            Path: Path of local temporary working space.

        """
        return self._date_time_root

    def to_relative_path(self, local_full: Path) -> Path:
        """Convert full path on local working space to relative.

        Args:
            local_full (Path): Full path you want to convert.

        Returns:
            Path: Converted relative path.

        """
        return get_relative(local_full, root_path=self._local_root)

    def to_full_path(self, local_relative: Path) -> Path:
        """Convert to full path on local working space from relative.

        Args:
            local_relative (Path): Relative path you want to convert.

        Returns:
            Path: Converted full path.

        """
        return Path(self._local_root, local_relative)

    def __init__(
        self,
        working_root: Path | None = None,
        local_root: Path | None = None,
        override: bool = False,
        jst: bool = False,
    ) -> None:
        """Generate string path pair about server directory.

        Args:
            working_root (Path | None, optional): Defaults to None.
                User defined temporary working space.
                It's mainly used for test.
                It's used for argument "working_root" of class "WorkSpace".

            local_root (Path | None, optional): Defaults to None.
                User defined path of local directory
                    which is synchronized with directory tree on server.

            override (bool, optional): Defaults to False.
                Override initial time count to "2023/4/1:12:00:00-00 (AM)".
                It's used for argument "override" of
                    function "create_date_time_space".

            jst (bool, optional): Defaults to False.
                If True, you can get datetime object as JST time zone.
                It's used for argument "jst" of
                    function "create_date_time_space".

        """
        self.__initialize_super_class(working_root)
        self.__initialize_variables(local_root, override, jst)
