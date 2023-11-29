#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.directory.create_directory_parent import (
    create_directory_parent,
)
from pyspartaproj.script.path.modify.get_relative import get_relative
from pyspartaproj.script.path.safe.safe_rename import SafeRename


class SafeTrash(SafeRename):
    def _move_file(self, target: Path, root: Path) -> None:
        if target.exists():
            trash_path: Path = Path(
                self.history_path, get_relative(target, root_path=root)
            )
            create_directory_parent(trash_path)
            self.rename(target, trash_path, override=True)

    def trash(self, trash_path: Path, trash_root: Path | None = None) -> None:
        parent_root: Path = trash_path.parent

        if trash_root is None:
            self._move_file(trash_path, parent_root)
        elif trash_path.is_relative_to(trash_root):
            self._move_file(trash_path, trash_root)
        else:
            self._move_file(trash_path, parent_root)
