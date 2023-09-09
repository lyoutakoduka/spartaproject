#!/usr/bin/env python
# -*- coding: utf-8 -*-

from context.default.string_context import Strs
from context.extension.path_context import Path, PathPair
from script.server.context_server import ContextServer


class PathServer(ContextServer):
    def _add_path(self, type: str, child: Path, parent: str = '') -> None:
        if 0 < len(parent):
            child = Path(self.get_path(parent), child)

        self._path_table[type] = child

    def _build_path_table(self) -> None:
        self._path_table: PathPair = {
            '_'.join([type, 'root']): Path(type)
            for type in ['private', 'public']
        }

    def __init__(self) -> None:
        super().__init__()

        self._build_path_table()

    def get_path_table(self) -> Strs:
        return list(self._path_table.keys())

    def get_path(self, type: str) -> Path:
        if type in self.get_context_table('path'):
            return super().get_path(type)

        return self._path_table[type]

    def get_path_string(self, type: str) -> str:
        path: Path = self.get_path(type)
        return path.as_posix()
