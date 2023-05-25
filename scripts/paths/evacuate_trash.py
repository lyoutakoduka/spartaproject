#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shutil import move

from contexts.path_context import Path, Paths
from scripts.paths.get_relative import get_relative
from scripts.paths.create_directory_parent import create_parent_directory
from scripts.paths.working_space import current_working_space


class TrashBox:
    def __init__(self, trash_path: Path = Path()) -> None:
        self._evacuated: Paths = []
        self._init_trash_path(trash_path)

    def _init_trash_path(self, path: Path) -> None:
        if '.' == str(path):
            path = current_working_space(Path('.trash'), jst=True)
        self._trash_path: Path = path

    def pop_evacuated(self) -> Paths:
        evacuated: Paths = self._evacuated[:]
        self._evacuated.clear()
        return evacuated

    def _move_file(self, target: Path, root: Path) -> None:
        if target.exists():
            trash_path: Path = Path(
                self._trash_path, get_relative(target, root_path=root)
            )

            create_parent_directory(trash_path)
            move(target, trash_path)

            self._evacuated += [trash_path]

    def throw_away_trash(
        self, trash_path: Path, trash_root: Path = Path(),
    ) -> None:
        has_initial: bool = '.' != str(trash_root)

        if has_initial and trash_path.is_relative_to(trash_root):
            self._move_file(trash_path, trash_root)
        else:
            self._move_file(trash_path, trash_path.parent)
