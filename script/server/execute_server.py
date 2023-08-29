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

    def execute(self, source_root: Path) -> Strs | None:
        DESTINATION: Path = Path('private', 'work', 'execute')
        destination_root: Path = Path(DESTINATION, source_root.name)

        if not self.upload(source_root, destination_root):
            return None

        return self.execute_ssh(['python', destination_root.as_posix()])
