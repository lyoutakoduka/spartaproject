#!/usr/bin/env python
# -*- coding: utf-8 -*-

from spartaproject.context.default.string_context import Strs
from spartaproject.context.extension.path_context import Path, PathPair
from spartaproject.script.directory.create_directory_working import \
    create_working_space
from spartaproject.script.path.modify.get_absolute import get_absolute
from spartaproject.script.path.modify.get_relative import get_relative
from spartaproject.script.server.context_server import ContextServer


class PathServer(ContextServer):
    def _add_path(self, type: str, child: Path, parent: str = '') -> None:
        if 0 < len(parent):
            child = Path(self.get_path(parent), child)

        self._path_table[type] = child

    def _add_directory(self, table: PathPair, parent: str = '') -> None:
        for type, name in table.items():
            self._add_path(type, Path(name), parent=parent)

    def _build_path_root(self) -> None:
        self._add_directory(
            {'private_root': Path('private'), 'public_root': Path('public')}
        )

    def _build_path_private(self) -> None:
        self._add_directory(
            {'work_root': Path('work'), 'develop_root': Path('develop')},
            parent='private_root'
        )

    def _build_path_develop(self) -> None:
        self._add_directory(
            {
                'internal_root': Path('internal'),
                'python_root': Path('external', 'python')
            },
            parent='develop_root'
        )

    def _build_path_table(self) -> None:
        self._path_table: PathPair = {}

        self._build_path_root()
        self._build_path_private()
        self._build_path_develop()

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

    def _get_local_absolute(self) -> Path:
        return get_absolute(self.get_path('local_root'))

    def get_working_space(self) -> Path:
        return create_working_space(
            get_absolute(
                Path(self._get_local_absolute(), self.get_path('work_root'))
            ),
            jst=True
        )

    def to_remote_path(self, local: Path) -> Path:
        return get_relative(local, root_path=self._get_local_absolute())

    def to_local_path(self, local: Path) -> Path:
        return Path(self._get_local_absolute(), local)
