#!/usr/bin/env python
# -*- coding: utf-8 -*-

from context.extension.path_context import Path
from script.directory.create_directory_parent import create_directory_parent
from script.path.modify.get_relative import get_relative
from script.path.safe.safe_rename import SafeRename


class SafeTrash(SafeRename):
    def _move_file(self, target: Path, root: Path) -> None:
        if target.exists():
            trash_path: Path = Path(
                self.history_path, get_relative(target, root_path=root)
            )
            create_directory_parent(trash_path)
            self.rename(target, trash_path, override=True)

    def throw_away_trash(
        self, trash_path: Path, trash_root: Path = Path()
    ) -> None:
        has_initial: bool = '.' != str(trash_root)

        if has_initial and trash_path.is_relative_to(trash_root):
            self._move_file(trash_path, trash_root)
        else:
            self._move_file(trash_path, trash_path.parent)
