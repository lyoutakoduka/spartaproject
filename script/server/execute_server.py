#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from context.default.integer_context import Ints
from context.default.string_context import Strs
from script.server.upload_server import UploadServer


class ExecuteServer(UploadServer):
    def _set_version(self, versions: Ints) -> str:
        if 0 == len(versions):
            versions = [3, 11, 3]

        return '.'.join([str(i) for i in versions])

    def _get_version_root(self, version: str) -> Path:
        language: str = 'python'

        return Path(
            self.get_path('python_root'),
            '-'.join([language.capitalize(), version])
        )

    def __init__(self) -> None:
        super().__init__()

    def __del__(self) -> None:
        super().__del__()

    def _get_error_identifier(self) -> str:
        body: str = ' '.join(['most', 'recent', 'call', 'last'])
        return ' '.join(['traceback'.capitalize(), '(' + body + ')']) + ':'

    def execute(self, source_root: Path) -> Strs | None:
        if not self.upload(source_root):
            return None

        destination_root: Path = self.to_remote_path(source_root)
        result: Strs = self.execute_ssh(
            ['python', destination_root.as_posix()]
        )

        if self._get_error_identifier() in result:
            raise ValueError

        return result
