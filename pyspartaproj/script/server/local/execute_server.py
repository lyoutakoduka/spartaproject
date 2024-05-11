#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to execute python code on server you can use ssh connection."""

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.server.local.upload_server import UploadServer
from pyspartaproj.script.server.script_version import get_version_name


class ExecuteServer(UploadServer):
    """Class to execute python code on server."""

    def _set_version(self, version: str | None) -> str:
        if version is None:
            version = "3.11.5"

        return get_version_name(version)

    def _set_version_path(self, version: str) -> None:
        self._python_path: Path = Path(
            self.get_path("python_root"), version, "bin", "python3"
        )

    def _get_filter_head(self) -> str:
        return "traceback".capitalize()

    def _get_filter_inside(self) -> str:
        return " ".join(["most", "recent", "call", "last"])

    def _get_filter_body(self) -> str:
        return "(" + self._get_filter_inside() + ")"

    def _get_error_identifier(self) -> str:
        return self._get_filter_head() + " " + self._get_filter_body() + ":"

    def _get_command(self, source_root: Path) -> Strs:
        return [
            path.as_posix()
            for path in [
                self._python_path,
                self.to_relative_path(source_root),
            ]
        ]

    def execute(self, source_root: Path) -> Strs | None:
        """Execute Python code you selected.

        Args:
            source_root (Path):
                Local path of Python code you will upload and execute.

        Raises:
            ValueError: Throw an exception
                if throw an exception on server by executed Python code.

        Returns:
            Strs | None:
                Stdout of executed Python code when execution is successful.
        """
        if not self.upload(source_root):
            return None

        result: Strs = self.execute_ssh(self._get_command(source_root))

        if self._get_error_identifier() in result:
            raise ValueError

        return result

    def __init__(
        self,
        version: str | None = None,
        local_root: Path | None = None,
        override: bool = False,
        jst: bool = False,
    ) -> None:
        """Select version of Python, then ready using ssh and sftp connection.

        Args:
            version (str | None, optional): Defaults to None.
                Version information of Python you want to execute.

            local_root (Path | None, optional): Defaults to None.
                User defined path of local working space which is used.
                It's used for argument "local_root" of class "UploadServer".

            override (bool, optional): Defaults to False.
                Override initial time count to "2023/4/1:12:00:00-00 (AM)".
                It's used for argument "override" of class "UploadServer".

            jst (bool, optional): Defaults to False.
                If True, you can get datetime object as JST time zone.
                It's used for argument "jst" of class "UploadServer".
        """
        super().__init__(local_root=local_root, override=override, jst=jst)

        self._set_version_path(self._set_version(version))
