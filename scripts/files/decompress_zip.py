#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict
from datetime import datetime
from zipfile import ZipFile, ZipInfo

from contexts.path_context import Path, Paths
from contexts.string_context import Strs
from scripts.files.export_file import byte_export
from scripts.files.import_json import json_load, Json
from scripts.paths.create_directory import path_mkdir
from scripts.paths.iterate_directory import walk_iterator
from scripts.paths.parent_directory import create_parent_dir
from scripts.times.set_timestamp import set_latest


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
        create_parent_dir(file_path)
        byte_export(file_path, zip_file.read(relative.as_posix()))

    def _restore_timestamp(self, file_path: Path, zip_info: ZipInfo) -> None:
        latest: datetime = datetime(*zip_info.date_time)

        comment: bytes = zip_info.comment
        if 0 < len(comment):
            content: Json = json_load(comment.decode('utf-8'))
            if isinstance(content, Dict):
                if 'latest' in content:
                    timestamp: Json = content['latest']
                    if isinstance(timestamp, str):
                        latest = datetime.fromisoformat(timestamp)

        set_latest(file_path, latest)

    def decompress_archive(self, decompress_target: Path) -> None:
        with ZipFile(decompress_target) as zip_file:
            for zip_info in zip_file.infolist():
                relative: Path = Path(zip_info.filename)
                file_path: Path = Path(self._output_root, relative)

                if zip_info.is_dir():
                    path_mkdir(file_path)
                else:
                    self._decompress_file(file_path, relative, zip_file)
                    self._restore_timestamp(file_path, zip_info)
