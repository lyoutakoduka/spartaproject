#!/usr/bin/env python
# -*- coding: utf-8 -*-

from context.extension.path_context import Path
from script.server.context_server import ContextServer


class PathServer(ContextServer):
    def __init__(self) -> None:
        super().__init__()

    def get_path(self, type: str) -> Path:
        return super().get_path(type)

    def get_path_string(self, type: str) -> str:
        path: Path = self.get_path(type)
        return path.as_posix()
