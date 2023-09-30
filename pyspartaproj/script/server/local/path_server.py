#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.context.extension.path_context import PathPair
from pyspartaproj.script.directory.create_directory_temporary import WorkSpace
from pyspartaproj.script.directory.create_directory_working import (
    create_working_space,
)
from pyspartaproj.script.path.modify.get_relative import get_relative
from pyspartaproj.script.server.local.context_server import ContextServer


class PathServer(ContextServer, WorkSpace):
    def _add_path(self, type: str, child: Path, parent: str | None) -> None:
        if parent is not None:
            child = Path(self.get_path(parent), child)

        self._path_table[type] = child

    def _add_directory(
        self, table: PathPair, parent: str | None = None
    ) -> None:
        for type, name in table.items():
            self._add_path(type, Path(name), parent=parent)

    def _build_path_root(self) -> None:
        self._add_directory(
            {"private_root": Path("private"), "public_root": Path("public")}
        )

    def _build_path_private(self) -> None:
        self._add_directory(
            {"work_root": Path("work"), "develop_root": Path("develop")},
            parent="private_root",
        )

    def _build_path_develop(self) -> None:
        self._add_directory(
            {
                "internal_root": Path("internal"),
                "python_root": Path("external", "python"),
            },
            parent="develop_root",
        )

    def _build_path_table(self) -> None:
        self._path_table: PathPair = {}

        self._build_path_root()
        self._build_path_private()
        self._build_path_develop()

    def _initialize_multiple_inheritance(self) -> None:
        ContextServer.__init__(self)
        WorkSpace.__init__(self)

    def __init__(self) -> None:
        self._initialize_multiple_inheritance()
        self._build_path_table()

    def get_path_table(self) -> Strs:
        return list(self._path_table.keys())

    def get_path(self, type: str) -> Path:
        if type in self.get_path_table():
            return super().get_path_context(type)

        return self._path_table[type]

    def get_working_space(
        self, override: bool = False, jst: bool = False
    ) -> Path:
        return create_working_space(
            Path(self.get_root(), self.get_path("work_root")),
            override=override,
            jst=jst,
        )

    def to_remote_path(self, local: Path) -> Path:
        return get_relative(local, root_path=self.get_root())

    def to_local_path(self, local: Path) -> Path:
        return Path(self.get_root(), local)
