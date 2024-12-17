#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to remove file or directory and log history."""

from pathlib import Path

from pyspartalib.context.extension.path_context import Paths
from pyspartalib.script.directory.create_parent import create_parent
from pyspartalib.script.path.modify.current.get_relative import (
    get_relative,
    is_relative,
)
from pyspartalib.script.path.safe.safe_rename import SafeRename


class SafeTrash(SafeRename):
    """Class to remove file or directory and log history."""

    def __initialize_super_class(
        self,
        working_root: Path | None,
        history_root: Path | None,
        override: bool,
        jst: bool,
    ) -> None:
        super().__init__(
            working_root=working_root,
            history_root=history_root,
            override=override,
            jst=jst,
        )

    def __initialize_variables(
        self, trash_root: Path | None, override: bool, jst: bool
    ) -> None:
        self._trash_root: Path = self.create_date_time_space(
            body_root=trash_root, override=override, jst=jst
        )

    def _move_file(self, target: Path, root: Path) -> None:
        if target.exists():
            trash_path: Path = Path(
                self.get_trash_root(), get_relative(target, root_path=root)
            )
            create_parent(trash_path)
            self.rename(target, trash_path, override=True)

    def get_trash_root(self) -> Path:
        """Get path of internal trash box at current date time.

        Returns:
            Path: Path of internal trash box.
        """
        return self._trash_root

    def trash(
        self, trash_path: Path, relative_root: Path | None = None
    ) -> Path:
        """Remove file or directory and log history.

        Args:
            trash_path (Path): Path you want to remove.

            relative_root (Path | None, optional): Defaults to None.
                Path of directory used as trash box.

        Returns:
            Path: "trash_path" is returned.
        """
        parent_root: Path = trash_path.parent

        if relative_root is None:
            self._move_file(trash_path, parent_root)

        elif is_relative(trash_path, root_path=relative_root):
            self._move_file(trash_path, relative_root)
        else:
            self._move_file(trash_path, parent_root)

        return trash_path

    def trash_at_once(
        self, trash_paths: Paths, relative_root: Path | None = None
    ) -> Paths:
        """Remove files or directories at once, and log history.

        Args:
            trash_paths (Paths): Paths you want to remove.

            relative_root (Path | None, optional): Defaults to None.
                Path of directory used as trash box.
                It's used for argument "trash_root" of method "trash".

        Returns:
            Paths: "trash_paths" is returned.
        """
        for trash_path in trash_paths:
            self.trash(trash_path, relative_root=relative_root)

        return trash_paths

    def __init__(
        self,
        working_root: Path | None = None,
        history_root: Path | None = None,
        override: bool = False,
        jst: bool = False,
        trash_root: Path | None = None,
    ) -> None:
        """Initialize variables and super class.

        Args:
            working_root (Path | None, optional): Defaults to None.
                User defined temporary working space.
                It's mainly used for test.
                It's used for argument "working_root" of class "FileHistory".

            history_root (Path | None, optional): Defaults to None.
                User defined path of temporary working space
                    including date time string.
                It's used for argument "history_root" of class "FileHistory".

            override (bool, optional): Defaults to False.
                Override initial time count to "2023/4/1:12:00:00-00 (AM)".
                It's used for argument "override" of class "FileHistory"
                    and function "create_date_time_space".

            jst (bool, optional): Defaults to False.
                If True, you can get datetime object as JST time zone.
                It's used for argument "jst" of class "FileHistory"
                    and function "create_date_time_space".

            trash_root (Path | None, optional): Defaults to None.
                User defined path of trash box including date time string.
                It's used for argument "body_root" of
                    function "create_date_time_space".
        """
        self.__initialize_super_class(
            working_root, history_root, override, jst
        )
        self.__initialize_variables(trash_root, override, jst)
