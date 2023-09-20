#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from spartaproject.context.default.integer_context import Ints
from spartaproject.context.default.string_context import Strs
from spartaproject.script.execute.script_version import version_to_string
from spartaproject.script.server.upload_server import UploadServer


class ExecuteServer(UploadServer):
    def _set_version(self, versions: Ints) -> str:
        if 0 == len(versions):
            versions = [3, 11, 5]

        return version_to_string(versions)

    def _get_version_root(self, version: str) -> Path:
        language: str = 'python'

        return Path(
            self.get_path('python_root'),
            language.capitalize() + '-' + version
        )

    def _set_version_path(self, version_root: Path) -> None:
        self._python_path: Path = Path(
            version_root, 'local', 'python', 'bin', 'python3'
        )

    def __init__(self, versions: Ints = []) -> None:
        super().__init__()

        self._set_version_path(
            self._get_version_root(self._set_version(versions))
        )

    def _get_error_identifier(self) -> str:
        body: str = ' '.join(['most', 'recent', 'call', 'last'])
        return 'traceback'.capitalize() + ' ' + '(' + body + ')' + ':'

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
