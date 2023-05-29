#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from zipfile import ZipFile, ZipInfo

from context.default.string_context import Strs, StrPair
from context.path_context import Path, Paths
from script.directories.create_directory import create_directory
from script.directories.create_directory_parent import create_directory_parent
from script.files.export_file import byte_export
from script.files.jsons.convert_from_json import string_pair_from_json
from script.files.jsons.import_json import json_load
from script.paths.iterate_directory import walk_iterator
from script.times.set_timestamp import set_latest


class DecompressZip:
    def __init__(self, output_root: Path) -> None:
        self._output_root: Path = output_root

    def _is_sequential_archive(self, path: Path) -> bool:
        names: Strs = path.stem.split('#')
        if 1 < len(names):
            try:
                int(names[-1])
                return True
            except BaseException:
                pass

        return False

    def sequential_archives(self, source_archive: Path) -> Paths:
        sequential: Paths = [source_archive]

        for path in walk_iterator(
            source_archive.parent, directory=False, depth=1, suffix='zip'
        ):
            if source_archive != path:
                if self._is_sequential_archive(path):
                    sequential += [path]

        return sequential

    def _decompress_file(
        self, file_path: Path, relative: Path, zip_file: ZipFile,
    ) -> None:
        create_directory_parent(file_path)
        byte_export(file_path, zip_file.read(relative.as_posix()))

    def _restore_timestamp(
        self, file_path: Path, information: ZipInfo,
    ) -> None:
        latest: datetime = datetime(*information.date_time)

        comment: bytes = information.comment
        if 0 < len(comment):
            content: StrPair = string_pair_from_json(
                json_load(comment.decode('utf-8'))
            )
            if 'latest' in content:
                latest = datetime.fromisoformat(content['latest'])

        set_latest(file_path, latest)

    def decompress_archive(self, decompress_target: Path) -> None:
        with ZipFile(decompress_target) as zip_file:
            for information in zip_file.infolist():
                relative: Path = Path(information.filename)
                file_path: Path = Path(self._output_root, relative)

                if information.is_dir():
                    create_directory(file_path)
                else:
                    self._decompress_file(file_path, relative, zip_file)
                    self._restore_timestamp(file_path, information)
