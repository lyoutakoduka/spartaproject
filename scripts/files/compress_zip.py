#!/usr/bin/env python
# -*- coding: utf-8 -*-

from zipfile import ZipFile, ZIP_LZMA, ZIP_STORED

from contexts.decimal_context import Decimal, set_decimal_context
from contexts.string_context import Strs
from contexts.path_context import Path, Paths
from scripts.paths.get_relative import path_relative
from scripts.paths.create_directory import path_mkdir
from scripts.paths.iterate_directory import walk_iterator

set_decimal_context()


def _default() -> int:
    limit_byte: int = 1
    for _ in range(3):
        limit_byte *= (2**10)
    return limit_byte * 4


class ArchiveZip:
    def __init__(
            self, output_root: Path,
            archive_id: str = '',
            limit_byte: int = _default(),
            compress: bool = False,
    ) -> None:
        self._output_root: Path = output_root

        self._limit_byte: Decimal = Decimal(str(limit_byte))
        self._compress: bool = compress

        self._init_archive_id(archive_id)
        self._init_walk_history()
        self._init_archive_byte()

    def _init_archive_id(self, archive_id: str) -> None:
        if 0 == len(archive_id):
            archive_id = self._output_root.name
        self._archive_id = archive_id

    def _init_walk_history(self) -> None:
        self._walk_directories: Paths = []
        self._walk_files: Paths = []
        self._archived: Paths = []

    def _init_archive_byte(self) -> None:
        self._output_index: int = 0
        self._reset_archive_byte()

    def close_archived(self) -> Paths:
        self._file_zip.close()
        return self._archived

    def _get_archive_path(self) -> Path:
        file_names: Strs = [self._archive_id]

        if 0 < self._output_index:
            file_names += [str(self._output_index).zfill(4)]
        self._output_index += 1

        return Path(self._output_root, '_'.join(file_names)).with_suffix('.zip')

    def _reset_archive_byte(self) -> None:
        self._archive_byte: Decimal = Decimal('0')

        path_mkdir(self._output_root)
        self._archived += [self._get_archive_path()]

        self._file_zip = ZipFile(
            self._archived[-1],
            mode='w',
            compression=ZIP_LZMA if self._compress else ZIP_STORED,
        )

    def _add_file_to_archive(self, is_dir: bool, target: Path, root: Path) -> None:
        relative_path: str = str(path_relative(target, root_path=root))
        if is_dir:
            self._file_zip.mkdir(relative_path)
        else:
            with open(target, 'rb') as file_read:
                self._file_zip.writestr(relative_path, file_read.read())

    def _update_archive_byte(self, target: Path, root: Path) -> None:
        target_byte: Decimal = Decimal(str(target.stat().st_size))

        if self._limit_byte < target_byte:
            ...
        else:
            next_byte: Decimal = self._archive_byte + target_byte

            if self._limit_byte < next_byte:
                self._reset_archive_byte()
            self._archive_byte += target_byte

            self._add_file_to_archive(False, target, root)

    def _not_still_archived(self, is_dir: bool, target: Path) -> bool:
        archived: Paths = self._walk_directories if is_dir else self._walk_files

        not_still: bool = target not in archived
        if not_still:
            archived += [target]

        return not_still

    def _add_archive_child(self, target: Path, root: Path) -> None:
        if target.is_dir():
            if self._not_still_archived(True, target):
                self._add_file_to_archive(True, target, root)

                for path in walk_iterator(target):
                    self._add_archive_child(path, root)
        else:
            if self._not_still_archived(False, target):
                self._update_archive_byte(target, root)

    def add_archive(self, archive_target: Path, archive_root: Path = Path('')) -> None:
        if archive_target.is_relative_to(archive_root):
            self._add_archive_child(archive_target, archive_root)
        else:
            self._add_archive_child(archive_target, archive_target.parent)
