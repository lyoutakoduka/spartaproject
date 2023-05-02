#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shutil import move
from datetime import datetime

from contexts.integer_context import Ints2
from contexts.string_context import Strs
from contexts.path_context import Path, Paths
from scripts.paths.get_absolute import path_absolute
from scripts.paths.create_directory import path_mkdir
from scripts.times.current_datetime import get_current_time


def _default() -> Path:
    TRASH_BOX: Strs = ['.trash']
    return path_absolute(Path(*TRASH_BOX))


class TrashBox:
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

    def move_file(self, trash_root: Path, target_path: Path) -> Path:
        trash_path: Path = Path(trash_root, target_path.name)
        move(target_path, trash_path)
        return trash_path

    def throw_away(self, target_paths: Paths) -> Paths:
        evacuated_paths: Paths = []

        if 0 < len(target_paths):
            trash_root: Path = self._get_trash_path()
            path_mkdir(trash_root)

            for target_path in target_paths:
                evacuated_paths += [self.move_file(trash_root, target_path)]

        return evacuated_paths

    def __init__(self, trash_path: Path = _default()) -> None:
        self._trash_path = trash_path
