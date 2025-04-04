#!/usr/bin/env python

"""Module to compress file or directory by archive format."""

from datetime import datetime
from decimal import Decimal
from pathlib import Path
from zipfile import ZIP_LZMA, ZIP_STORED, ZipFile, ZipInfo

from pyspartalib.context.default.integer_context import Ints
from pyspartalib.context.default.string_context import StrPair, Strs
from pyspartalib.context.extension.path_context import Paths
from pyspartalib.script.decimal.initialize_decimal import initialize_decimal
from pyspartalib.script.directory.create_directory import create_directory
from pyspartalib.script.file.archive.archive_format import rename_format
from pyspartalib.script.file.archive.context.archive_context import Archives
from pyspartalib.script.file.json.convert_to_json import multiple_to_json
from pyspartalib.script.file.json.export_json import json_dump
from pyspartalib.script.file.text.import_file import byte_import
from pyspartalib.script.path.iterate_directory import walk_iterator
from pyspartalib.script.path.modify.current.get_relative import (
    get_relative,
    is_relative,
)
from pyspartalib.script.path.status.get_statistic import get_file_size
from pyspartalib.script.string.encoding.set_encoding import set_encoding
from pyspartalib.script.time.path.get_timestamp import get_latest
from pyspartalib.script.time.stamp.current_datetime import get_current_time

initialize_decimal()


class CompressArchive:
    """Class to compress file or directory by archive format."""

    def _init_variables(self, output_root: Path, compress: bool) -> None:
        self._output_root: Path = output_root
        self._compress: bool = compress
        self._archive_file: ZipFile | None = None

    def _get_archive_file(self) -> ZipFile | None:
        return self._archive_file

    def _init_limit_byte(self, byte: int) -> None:
        if byte == 0:
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

    def _has_archived(self) -> bool:
        return self._output_index > 0

    def _get_archive_path(self) -> Path:
        file_names: Strs = [self._archive_id]

        if self._has_archived():
            file_names += [str(self._output_index).zfill(4)]

        self._output_index += 1

        return rename_format(Path(self._output_root, "#".join(file_names)))

    def _reset_archive_byte(self) -> None:
        self._archived += [self._get_archive_path()]
        self._archive_file = ZipFile(self._archived[-1], mode="w")

    def _convert_comment(self, attribute: StrPair) -> bytes:
        comment: str = json_dump(multiple_to_json(attribute), compress=True)
        return set_encoding(comment)

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

    def _get_archive_timestamp(self, target: Path) -> datetime:
        if latest := get_latest(target):
            return latest

        return get_current_time()

    def _get_archive_information(
        self,
        target: Path,
        relative: Path,
    ) -> ZipInfo:
        information: ZipInfo = ZipInfo(filename=str(relative))

        information.compress_type = ZIP_LZMA if self._compress else ZIP_STORED
        latest: datetime = self._get_archive_timestamp(target)

        self._store_timestamp(latest, information)
        information.comment = self._store_timestamp_detail(latest)

        return information

    def _make_directory(self, path: Path) -> None:
        if archive_file := self._get_archive_file():
            archive_file.mkdir(str(path))

    def _write_string(self, path: Path, target_path: Path) -> None:
        if archive_file := self._get_archive_file():
            archive_file.writestr(
                self._get_archive_information(target_path, path),
                byte_import(target_path),
            )

    def _get_information_list(self) -> Archives:
        if archive_file := self._get_archive_file():
            return archive_file.infolist()

        return []

    def _close_archive(self) -> None:
        if archive_file := self._get_archive_file():
            archive_file.close()

    def _add_file_to_archive(
        self,
        is_dir: bool,
        reset: bool,
        target: Path,
        root: Path,
    ) -> None:
        if reset:
            self._reset_archive_byte()

        relative: Path = get_relative(target, root_path=root)

        if is_dir:
            self._make_directory(relative)
        else:
            self._write_string(relative, target)

    def _within_allowance(self, target_byte: Decimal) -> bool:
        return self._limit_byte >= target_byte

    def _get_decimal_size(self, path: Path) -> Decimal:
        return Decimal(str(get_file_size(path)))

    def _archive_outside_byte(self) -> Decimal:
        return self._get_decimal_size(self._archived[-1])

    def _get_file_size(self) -> Ints:
        return [
            information.file_size
            for information in self._get_information_list()
        ]

    def _archive_inside_byte(self) -> Decimal:
        return Decimal(str(sum(self._get_file_size())))

    def _archive_include_files(self) -> bool:
        return self._archive_inside_byte() > 0

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
            source_byte: Decimal = self._get_decimal_size(target)
            include_files: bool = self._archive_include_files()

            if include_files:
                source_byte = self._estimate_compressed_size(source_byte)

            if self._within_allowance(source_byte):
                if include_files and (
                    not self._within_allowance(
                        self._estimate_archived_size(source_byte),
                    )
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
        elif self._not_still_archived(False, target):
            self._update_archive_byte(target, root)

    def close_archived(self) -> Paths:
        """Close archive and return archived list.

        Returns:
            Paths: List of archives.

            If archives isn't divided, following list is returned.

                [<export directory>/<archive name>.<archive format>]

            If archive is divided by three, following list is returned.

                [
                    <export directory>/<archive name>.<archive format>,
                    <export directory>/<archive name>#0001.<archive format>,
                    <export directory>/<archive name>#0002.<archive format>
                ]

        """
        self._close_archive()
        return self._archived

    def compress_archive(
        self,
        archive_target: Path,
        archive_root: Path | None = None,
    ) -> None:
        """Compress file or directory you selected.

        Args:
            archive_target (Path): Path of compress target.

            archive_root (Path | None, optional): Defaults to None.
                Root directory which is used for generating relative path
                    in the inner of archive.

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
        elif is_relative(archive_target, root_path=archive_root):
            self._compress_child(archive_target, archive_root)
        else:
            self._compress_child(archive_target, parent_root)

    def compress_at_once(
        self,
        paths: Paths,
        archive_root: Path | None = None,
    ) -> None:
        """Compress list of file or directory at once.

        Args:
            paths (Paths): List of path of compress target.

            archive_root (Path | None, optional): Defaults to None.
                Root directory which is used for generating relative path
                    in the inner of archive.
                It's used for argument "archive_root"
                    of method "compress_archive".

        """
        for path in paths:
            self.compress_archive(path, archive_root=archive_root)

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
                        |--target.<archive format> (file1.txt + file2.txt)
                        |--target#0001.<archive format> (file3.txt)

                e.g., second sample to explain divided archive is follow.

                    target/
                        |--file1.txt (12 byte)
                        |--file2.txt (4 byte)
                        |--file3.txt (4 byte)

                Archives of first sample are compressed as follow.

                    output_root/
                        |--target.<archive format> (file1.txt)
                        |--target#0001.<archive format> (file2.txt + file3.txt)

                e.g., third sample to explain divided archive is follow.

                    target/
                        |--file1.txt (10 byte)
                        |--file2.txt (10 byte)
                        |--file3.txt (10 byte)

                Archives of first sample are compressed as follow.

                    output_root/
                        |--target.<archive format> (file1.txt)
                        |--target#0001.<archive format> (file2.txt)
                        |--target#0002.<archive format> (file3.txt)

            compress (bool, optional): Defaults to False.
                If it's True, you can compress archive by LZMA format.
                Default is no compressed.

        """
        self._init_variables(output_root, compress)
        self._init_limit_byte(limit_byte)
        self._init_archive_id(archive_id)
        self._init_walk_history()
        self._init_archive_output()
        self._reset_archive_byte()
