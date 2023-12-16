#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to compress file or directory by zip format."""

from datetime import datetime
from decimal import Decimal
from pathlib import Path
from zipfile import ZIP_LZMA, ZIP_STORED, ZipFile, ZipInfo

from pyspartaproj.context.default.string_context import StrPair, Strs
from pyspartaproj.context.extension.path_context import Paths
from pyspartaproj.script.decimal.initialize_decimal import initialize_decimal
from pyspartaproj.script.directory.create_directory import create_directory
from pyspartaproj.script.file.json.convert_to_json import multiple_to_json
from pyspartaproj.script.file.json.export_json import json_dump
from pyspartaproj.script.file.text.import_file import byte_import
from pyspartaproj.script.path.iterate_directory import walk_iterator
from pyspartaproj.script.path.modify.get_relative import get_relative
from pyspartaproj.script.time.stamp.get_timestamp import get_latest

initialize_decimal()


class CompressZip:
    """Class to compress file or directory by zip format."""

    def __init__(
        self,
        output_root: Path,
        archive_id: str | None = None,
        limit_byte: int = 0,
        compress: bool = False,
    ) -> None:
        """Initialize compress conditions and exporting directory.

        Args:
            output_root (Path): Path you want to export archives.

            archive_id (str | None, optional): Defaults to None.
                Name of archive you create.
                If it's None, file or directory name of path "output_root"
                    is used for archive name.

            limit_byte (int, optional): Defaults to 0.
                If it's not 0, archive are dividedly compressed.
                The value of "limit_byte" is represented by byte unit.

                Suppose "limit_byte" is 10 byte.

                e.g., first sample to explain divided archive is follow.

                target/
                    |--file1.txt (4 byte)
                    |--file2.txt (4 byte)
                    |--file3.txt (4 byte)

                Archives of first sample are compressed as follow.

                output_root/
                    |--target.zip (file1.txt + file2.txt)
                    |--target#0001.zip (file3.txt)

                e.g., second sample to explain divided archive is follow.

                target/
                    |--file1.txt (12 byte)
                    |--file2.txt (4 byte)
                    |--file3.txt (4 byte)

                Archives of first sample are compressed as follow.

                output_root/
                    |--target.zip (file1.txt)
                    |--target#0001.zip (file2.txt + file3.txt)

                e.g., third sample to explain divided archive is follow.

                target/
                    |--file1.txt (10 byte)
                    |--file2.txt (10 byte)
                    |--file3.txt (10 byte)

                Archives of first sample are compressed as follow.

                output_root/
                    |--target.zip (file1.txt)
                    |--target#0001.zip (file2.txt)
                    |--target#0002.zip (file3.txt)

            compress (bool, optional): Defaults to False.
                If it's True, you can compress archive by LZMA format.
                Default is no compressed.
        """
        self._output_root: Path = output_root
        self._compress: bool = compress

        self._init_limit_byte(limit_byte)
        self._init_archive_id(archive_id)
        self._init_walk_history()
        self._init_archive_output()

    def _init_limit_byte(self, byte: int) -> None:
        if 0 == byte:
            byte = 1
            for _ in range(3):
                byte *= 2**10
            byte *= 4  # 4GB

        self._limit_byte: Decimal = Decimal(str(byte))

    def _init_archive_id(self, archive_id: str | None) -> None:
        if archive_id is None:
            archive_id = self._output_root.name
        self._archive_id = archive_id

    def _init_walk_history(self) -> None:
        self._walk_directories: Paths = []
        self._walk_files: Paths = []
        self._archived: Paths = []

    def _init_archive_output(self) -> None:
        self._output_index: int = 0
        create_directory(self._output_root)

    def close_archived(self) -> Paths:
        """Close archive and return archived list.

        Returns:
            Paths: list of archives.

            If archives isn't divided, following list is returned.

            [<export directory>/<archive name>.zip]

            If archive is divided by three, following list is returned.

            [
                <export directory>/<archive name>.zip,
                <export directory>/<archive name>#0001.zip,
                <export directory>/<archive name>#0002.zip
            ]
        """
        self._file_zip.close()
        return self._archived

    def _has_archived(self) -> bool:
        return 0 < self._output_index

    def _get_archive_path(self) -> Path:
        file_names: Strs = [self._archive_id]

        if self._has_archived():
            file_names += [str(self._output_index).zfill(4)]
        self._output_index += 1

        archived_path: Path = Path(self._output_root, "#".join(file_names))
        return archived_path.with_suffix(".zip")

    def _reset_archive_byte(self) -> None:
        self._archived += [self._get_archive_path()]
        self._file_zip = ZipFile(self._archived[-1], mode="w")

    def _convert_comment(self, attribute: StrPair) -> bytes:
        comment: str = json_dump(multiple_to_json(attribute), compress=True)
        return comment.encode("utf-8")

    def _store_timestamp_detail(self, time: datetime) -> bytes:
        return self._convert_comment({"latest": time.isoformat()})

    def _store_timestamp(self, time: datetime, information: ZipInfo) -> None:
        information.date_time = (
            time.year,
            time.month,
            time.day,
            time.hour,
            time.minute,
            time.second,
        )

    def _get_zip_information(self, target: Path, relative: Path) -> ZipInfo:
        information: ZipInfo = ZipInfo(filename=str(relative))

        information.compress_type = ZIP_LZMA if self._compress else ZIP_STORED
        latest: datetime = get_latest(target)
        self._store_timestamp(latest, information)
        information.comment = self._store_timestamp_detail(latest)

        return information

    def _add_file_to_archive(
        self, is_dir: bool, reset: bool, target: Path, root: Path
    ) -> None:
        if reset:
            self._reset_archive_byte()

        relative: Path = get_relative(target, root_path=root)
        if is_dir:
            self._file_zip.mkdir(str(relative))
        else:
            self._file_zip.writestr(
                self._get_zip_information(target, relative),
                byte_import(target),
            )

    def _within_allowance(self, target_byte: Decimal) -> bool:
        return self._limit_byte >= target_byte

    def _archive_outside_byte(self) -> Decimal:
        current_archive: Path = self._archived[-1]
        return Decimal(str(current_archive.stat().st_size))

    def _archive_inside_byte(self) -> Decimal:
        return Decimal(
            str(
                sum(
                    [
                        information.file_size
                        for information in self._file_zip.infolist()
                    ]
                )
            )
        )

    def _archive_include_files(self) -> bool:
        return 0 < self._archive_inside_byte()

    def _estimate_compressed_size(self, source_byte: Decimal) -> Decimal:
        outside_byte: Decimal = self._archive_outside_byte()
        inside_byte: Decimal = self._archive_inside_byte()

        return source_byte * (outside_byte / inside_byte)

    def _estimate_archived_size(self, source_byte: Decimal) -> Decimal:
        outside_byte: Decimal = self._archive_outside_byte()
        return source_byte + outside_byte

    def _update_archive_byte(self, target: Path, root: Path) -> None:
        archive_reset: bool = False

        if self._has_archived():
            source_byte: Decimal = Decimal(str(target.stat().st_size))
            include_files: bool = self._archive_include_files()

            if include_files:
                source_byte = self._estimate_compressed_size(source_byte)

            if self._within_allowance(source_byte):
                if include_files:
                    if not self._within_allowance(
                        self._estimate_archived_size(source_byte)
                    ):
                        archive_reset = True
            elif include_files:
                archive_reset = True
        else:
            archive_reset = True

        self._add_file_to_archive(False, archive_reset, target, root)

    def _not_still_archived(self, is_dir: bool, target: Path) -> bool:
        archived: Paths = (
            self._walk_directories if is_dir else self._walk_files
        )

        not_still: bool = target not in archived
        if not_still:
            archived += [target]

        return not_still

    def _compress_child(self, target: Path, root: Path) -> None:
        if target.is_dir():
            if self._not_still_archived(True, target):
                archive_reset: bool = not self._has_archived()
                self._add_file_to_archive(True, archive_reset, target, root)

                for path in walk_iterator(target):
                    self._compress_child(path, root)
        else:
            if self._not_still_archived(False, target):
                self._update_archive_byte(target, root)

    def compress_archive(
        self, archive_target: Path, archive_root: Path | None = None
    ) -> None:
        """Compress file or directory you selected.

        Args:
            archive_target (Path): Path of compress target.

            archive_root (Path | None, optional): Defaults to None.
                Root directory of compress target
                    which is use to record relative path.

            e.g., if contents of archive target is follow,
                and archive_root is "root/group/".

            root/
                |--group/
                    |--file1.txt
                    |--type/
                        |--file2.txt

            Compressed archive will contain following file and directory
                as relative path.

            |--file1.txt
            |--type/
                |--file2.txt
        """
        parent_root: Path = archive_target.parent

        if archive_root is None:
            self._compress_child(archive_target, parent_root)
        elif archive_target.is_relative_to(archive_root):
            self._compress_child(archive_target, archive_root)
        else:
            self._compress_child(archive_target, parent_root)
