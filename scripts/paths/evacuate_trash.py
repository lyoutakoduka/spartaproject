#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shutil import move
from datetime import datetime

from contexts.integer_context import Ints2
from contexts.string_context import Strs
from contexts.path_context import Path, Paths
from scripts.paths.get_relative import path_relative
from scripts.paths.get_absolute import path_absolute
from scripts.paths.create_directory import path_mkdir
from scripts.times.current_datetime import get_current_time


def _default() -> Path:
    TRASH_BOX: Strs = ['.trash']
    return path_absolute(Path(*TRASH_BOX))


class TrashBox:
    def __init__(self, trash_path: Path = _default()) -> None:
        self._trash_path = trash_path
        self._evacuated: Paths = []
        self._trash_box_root: Path = self._get_trash_path()

    def pop_evacuated(self) -> Paths:
        evacuated: Paths = self._evacuated[:]
        self._evacuated.clear()
        return evacuated

    def _get_time_data(self, time: datetime) -> Ints2:
        return [
            [4, time.year],
            [2, time.month],
            [2, time.day],
            [2, time.hour],
            [2, time.minute],
            [2, time.second],
            [6, time.microsecond],
        ]

    def _get_trash_path(self) -> Path:
        time: datetime = get_current_time(jst=True)
        time_counts: Ints2 = self._get_time_data(time)

        time_texts: Strs = [
            str(time_count).zfill(order)
            for order, time_count in time_counts
        ]

        return Path(self._trash_path, *time_texts)

    def _move_file(self, target: Path, root: Path) -> None:
        if target.exists():
            relative: Path = path_relative(target, root_path=root)
            trash_path: Path = Path(self._trash_box_root, relative)

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
