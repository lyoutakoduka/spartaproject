#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.context.default.integer_context import Ints
from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.server.local.upload_server import UploadServer
from pyspartaproj.script.server.script_version import get_version_name


class ExecuteServer(UploadServer):
    def _set_version(self, versions: Ints | None) -> str:
        if versions is None:
            versions = [3, 11, 5]

        return get_version_name(versions)

    def _set_version_path(self, version: str) -> None:
        self._python_path: Path = Path(
            self.get_path("python_root"), version, "bin", "python3"
        )

    def __init__(self, versions: Ints | None = None) -> None:
        super().__init__()

        self._set_version_path(self._set_version(versions))

    def _get_error_identifier(self) -> str:
        body: str = " ".join(["most", "recent", "call", "last"])
        return "traceback".capitalize() + " " + "(" + body + ")" + ":"

    def _get_command(self, source_root: Path) -> Strs:
        return [
            path.as_posix()
            for path in [self._python_path, self.to_remote_path(source_root)]
        ]

    def execute(self, source_root: Path) -> Strs | None:
        if not self.upload(source_root):
            return None

        result: Strs = self.execute_ssh(self._get_command(source_root))

        if self._get_error_identifier() in result:
            raise ValueError

        return result
