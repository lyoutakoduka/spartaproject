#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to execute python code on server you can use ssh connection."""

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.server.local.upload_server import UploadServer
from pyspartaproj.script.server.script_version import get_version_name


class ExecuteServer(UploadServer):
    """Class to execute python code on server.

    Inherit:
        (UploadServer): Class to upload python code to server
    """

    def _set_version(self, version: str | None) -> str:
        if version is None:
            version = "3.11.5"

        return get_version_name(version)

    def _set_version_path(self, version: str) -> None:
        self._python_path: Path = Path(
            self.get_path("python_root"), version, "bin", "python3"
        )

    def _get_error_identifier(self) -> str:
        body: str = " ".join(["most", "recent", "call", "last"])
        return "traceback".capitalize() + " " + "(" + body + ")" + ":"

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
                local path of Python code you will upload and execute

        Raises:
            ValueError:
                raise error if error raised on server by executed Python code

        Returns:
            Strs | None:
                stdout of executed Python code when execution is successful
        """
        if not self.upload(source_root):
            return None

        result: Strs = self.execute_ssh(self._get_command(source_root))

        if self._get_error_identifier() in result:
            raise ValueError

        return result

    def __init__(self, version: str | None = None) -> None:
        """Select version of Python, then ready using ssh and sftp connection.

        Args:
            version (str | None, optional): Defaults to None.
                version information of Python you want to execute
        """
        super().__init__()

        self._set_version_path(self._set_version(version))
