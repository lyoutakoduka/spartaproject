#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to decompress file or directory by archive format."""

from datetime import datetime
from pathlib import Path
from zipfile import ZIP_LZMA, ZipFile, ZipInfo

from pyspartaproj.context.default.string_context import StrPair, Strs
from pyspartaproj.context.extension.path_context import Paths
from pyspartaproj.script.directory.create_directory import create_directory
from pyspartaproj.script.directory.create_directory_parent import (
    create_directory_parent,
)
from pyspartaproj.script.file.archive.archive_format import get_format
from pyspartaproj.script.file.json.convert_from_json import (
    string_pair_from_json,
)
from pyspartaproj.script.file.json.import_json import json_load
from pyspartaproj.script.file.text.export_file import byte_export
from pyspartaproj.script.path.iterate_directory import walk_iterator
from pyspartaproj.script.time.stamp.set_timestamp import set_latest


class DecompressArchive:
    """Class to decompress file or directory by archive format."""

    def _initialize_paths(self, output_root: Path) -> None:
        self._output_root: Path = output_root

    def _is_sequential_archive(self, path: Path) -> bool:
        names: Strs = path.stem.split("#")

        if 1 < len(names):
            try:
                int(names[-1])
                return True
            except BaseException:
                pass

        return False

    def _decompress_file(
        self, file_path: Path, relative: Path, archive_file: ZipFile
    ) -> None:
        create_directory_parent(file_path)
        byte_export(file_path, archive_file.read(relative.as_posix()))

    def _restore_timestamp(
        self, file_path: Path, information: ZipInfo
    ) -> None:
        latest: datetime = datetime(*information.date_time)
        comment: bytes = information.comment

        if 0 < len(comment):
            content: StrPair = string_pair_from_json(
                json_load(comment.decode())
            )

            if "latest" in content:
                latest = datetime.fromisoformat(content["latest"])

        set_latest(file_path, latest)

    def sequential_archives(self, source_archive: Path) -> Paths:
        """Get list of archives which is compressed dividedly.

        Args:
            source_archive (Path): The head path of sequential archives.

        Returns:
            Paths: List of paths of sequential archives you got.

        e.g., sequential archives dividedly to three are represented to follow.

        root/
            |--archive.<archive format>
            |--archive#0001.<archive format>
            |--archive#0002.<archive format>

        If you select path "source_archive" is "root/archive.<archive format>",
            following list is returned.

        [
            root/archive.<archive format>,
            root/archive#0001.<archive format>,
            root/archive#0002.<archive format>
        ]

        Name format of sequential archives are follow.

        Index 0:    <archive name>.<archive format>
        Index 1~:   <archive name>#<string index>.<archive format>

        <archive name> of all indices must be same.
        <string index> must filled by zero, and digit is optional.
        """
        sequential: Paths = [source_archive]

        for path in walk_iterator(
            source_archive.parent,
            directory=False,
            depth=1,
            suffix=get_format(),
        ):
            if source_archive != path:
                if self._is_sequential_archive(path):
                    sequential += [path]

        return sequential

    def decompress_archive(self, decompress_target: Path) -> None:
        """Decompress file or directory by archive format.

        Args:
            decompress_target (Path): Path of archive you want to decompress.
        """
        with ZipFile(decompress_target) as archive_file:
            for information in archive_file.infolist():
                relative: Path = Path(information.filename)
                file_path: Path = Path(self._output_root, relative)

                if information.is_dir():
                    create_directory(file_path)
                else:
                    self._decompress_file(file_path, relative, archive_file)
                    self._restore_timestamp(file_path, information)

    def is_lzma_archive(self, decompress_target: Path) -> bool:
        """Method to get status of compression format.

        Args:
            decompress_target (Path): Path of archive
                which you want to get status of compression format.

        Returns:
            bool: Return True if archive is compressed by LZMA.
        """
        with ZipFile(decompress_target) as archive_file:
            for information in archive_file.infolist():
                if ZIP_LZMA == information.compress_type:
                    return True

        return False

    def __init__(self, output_root: Path) -> None:
        """Initialize decompress directory.

        Args:
            output_root (Path): Path of decompress directory.
        """
        self._initialize_paths(output_root)
