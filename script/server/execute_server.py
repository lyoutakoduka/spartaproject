#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from context.default.string_context import Strs
from script.server.upload_server import UploadServer


class ExecuteServer(UploadServer):
    def __init__(self) -> None:
        super().__init__()

    def __del__(self) -> None:
        super().__del__()

    def _get_error_identifier(self) -> str:
        body: str = ' '.join(['most', 'recent', 'call', 'last'])
        return ' '.join(['traceback'.capitalize(), '(' + body + ')']) + ':'

    def execute(self, source_root: Path) -> Strs | None:
        DESTINATION: Path = Path('private', 'work', 'execute')
        destination_root: Path = Path(DESTINATION, source_root.name)

        if not self.upload(source_root, destination_root):
            return None

        result: Strs = self.execute_ssh(
            ['python', destination_root.as_posix()]
        )

        if self._get_error_identifier() in result:
            raise ValueError

        return result
