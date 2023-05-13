#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shutil import move

from contexts.path_context import Path, Paths
from scripts.paths.get_relative import path_relative
from scripts.paths.working_space import current_working_space
from scripts.paths.create_directory import path_mkdir


def _default() -> Path:
    return current_working_space(Path('.trash'), jst=True)


class TrashBox:
    def __init__(self, trash_path: Path = _default()) -> None:
        self._trash_path: Path = trash_path
        self._evacuated: Paths = []

    def pop_evacuated(self) -> Paths:
        evacuated: Paths = self._evacuated[:]
        self._evacuated.clear()
        return evacuated

    def _move_file(self, target: Path, root: Path) -> None:
        if target.exists():
            relative: Path = path_relative(target, root_path=root)
            trash_path: Path = Path(self._trash_path, relative)

            parent_path: Path = trash_path.parent
            if not parent_path.exists():
                path_mkdir(parent_path)

            move(target, trash_path)
            self._evacuated += [trash_path]

    def throw_away_trash(self, trash_path: Path, trash_root: Path = Path('')) -> None:
        if trash_path.is_relative_to(trash_root):
            self._move_file(trash_path, trash_root)
        else:
            self._move_file(trash_path, trash_path.parent)
