#!/usr/bin/env python

"""Module to edit internal of archive file."""

from pathlib import Path
from typing import NoReturn

from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.extension.path_context import Paths
from pyspartalib.context.extension.time_context import TimePair
from pyspartalib.script.file.archive.compress_archive import CompressArchive
from pyspartalib.script.file.archive.decompress_archive import (
    DecompressArchive,
)
from pyspartalib.script.path.iterate_directory import walk_iterator
from pyspartalib.script.path.safe.safe_trash import SafeTrash
from pyspartalib.script.time.path.get_timestamp import get_directory_latest
from pyspartalib.script.time.stamp.is_same_stamp import is_same_stamp


def _raise_error(message: str) -> NoReturn:
    raise ValueError(message)


def _none_error(result: Type | None, message: str) -> Type:
    if result is None:
        _raise_error(message)

    return result


class EditArchive(SafeTrash):
    """Class to edit internal of archive file."""

    def __initialize_super_class(
        self,
        working_root: Path | None,
        history_root: Path | None,
        trash_root: Path | None,
        override: bool,
        jst: bool,
    ) -> None:
        super().__init__(
            working_root=working_root,
            history_root=history_root,
            trash_root=trash_root,
            override=override,
            jst=jst,
        )

    def __finalize_super_class(self) -> None:
        super().__del__()

    def __initialize_variables(
        self,
        edit_root: Path | None,
        override: bool,
        jst: bool,
    ) -> None:
        self._disable_archive: bool = True
        self._is_lzma_before: bool = False
        self._archive_path: Path | None = None
        self._edit_root: Path = self.create_date_time_space(
            body_root=edit_root,
            override=override,
            jst=jst,
        )

    def _initialize_archive_open(self) -> None:
        self._disable_archive = False

    def _initialize_archive_element(
        self,
        archive_path: Path | None,
        limit_byte: int,
        compress: bool,
        protected: bool,
    ) -> None:
        self._archive_path = archive_path
        self._limit_byte: int = limit_byte
        self._is_lzma_after: bool = compress
        self._protected: bool = protected

    def _get_archive_stamp(self) -> TimePair:
        return get_directory_latest(walk_iterator(self.get_edit_root()))

    def _is_difference_archive_stamp(self, archive_stamp: TimePair) -> bool:
        return not is_same_stamp(self._archive_stamp, archive_stamp)

    def _is_difference_compress_type(self) -> bool:
        return self._is_lzma_before != self._is_lzma_after

    def _is_difference_archive(self) -> TimePair | None:
        archive_stamp: TimePair = self._get_archive_stamp()

        if self._is_difference_compress_type():
            return archive_stamp

        if self._is_difference_archive_stamp(archive_stamp):
            return archive_stamp

        return None

    def _cleanup_before_override(self) -> None:
        self.trash_at_once(self._decompressed)

    def _compress_archive(self, archive_stamp: TimePair) -> Paths:
        self._cleanup_before_override()

        archive_path: Path = self.get_archive_path()

        compress_archive = CompressArchive(
            archive_path.parent,
            limit_byte=self._limit_byte,
            compress=self._is_lzma_after,
            archive_id=archive_path.stem,
        )

        compress_archive.compress_at_once(
            [Path(path_text) for path_text in archive_stamp],
            archive_root=self.get_edit_root(),
        )

        return compress_archive.close_archived()

    def _decompress_archive(
        self,
        decompress_archive: DecompressArchive,
    ) -> None:
        self._decompressed: Paths = decompress_archive.sequential_archives(
            self.get_archive_path(),
        )
        decompress_archive.decompress_at_once(self._decompressed)

    def _record_compress_type(
        self,
        decompress_archive: DecompressArchive,
    ) -> None:
        self._is_lzma_before = decompress_archive.is_lzma_archive(
            self.get_archive_path(),
        )

    def _get_decompress_stamp(self) -> None:
        decompress_archive = DecompressArchive(self.get_edit_root())

        self._decompress_archive(decompress_archive)
        self._record_compress_type(decompress_archive)

        self._archive_stamp: TimePair = self._get_archive_stamp()

    def _filter_time_stamp(self) -> Paths | None:
        if self._protected:
            return None

        archive_stamp: TimePair | None = self._is_difference_archive()

        if archive_stamp is None:  # Can't using: if value := func()
            return None

        return self._compress_archive(archive_stamp)

    def _finalize_archive(self) -> Paths | None:
        archived: Paths | None = self._filter_time_stamp()

        self.__finalize_super_class()

        return archived

    def is_disable_archive(self) -> bool:
        """Confirm statue of archive.

        Returns:
            bool: True if the archive is opened.

        """
        return self._disable_archive

    def get_archive_path(self) -> Path:
        """Get path of archive you will edit.

        Returns:
            Path: Path of archive.

        """
        return _none_error(self._archive_path, "edit")

    def get_edit_root(self) -> Path:
        """Get path of temporary working space.

        The directory is used for placing decompressed contents of archive.

        Returns:
            Path: Path of temporary working space.

        """
        return self._edit_root

    def close_archive(self) -> Paths | None:
        """Compress the contents of temporary working space to archive.

        Returns:
            Paths | None: Path of compressed archive.
                Return "None" if the archive you want to edit isn't changed.

        """
        if self.is_disable_archive():
            return None

        self._disable_archive = True

        return self._finalize_archive()

    def open_archive(
        self,
        archive_path: Path | None = None,
        limit_byte: int = 0,
        compress: bool = False,
        protected: bool = False,
    ) -> Path | None:
        """Initialize variables about archive and decompress it.

        Args:
            archive_path (Path | None, optional): Defaults to None.
                Path of archive you want to edit.

            limit_byte (int, optional): Defaults to 0.
                If it's not 0, archive are dividedly compressed.
                It's used for argument "limit_byte" of class "CompressArchive".

            compress (bool, optional): Defaults to False.
                If it's True, you can compress archive by LZMA format.
                It's used for argument "compress" of class "CompressArchive".

            protected (bool, optional): Defaults to False.
                True if you don't want to update original archive.

        Returns:
            Path | None: Return archive path which is argument "archive_path".

        """
        if archive_path is None:
            return None

        self._initialize_archive_open()
        self._initialize_archive_element(
            archive_path,
            limit_byte,
            compress,
            protected,
        )

        self._get_decompress_stamp()

        return archive_path

    def __del__(self) -> None:
        """Close and recompress archive you want to edit automatically."""
        self.close_archive()

    def __init__(
        self,
        working_root: Path | None = None,
        history_root: Path | None = None,
        trash_root: Path | None = None,
        override: bool = False,
        jst: bool = False,
        edit_root: Path | None = None,
    ) -> None:
        """Initialize super class and variables about temporary work space.

        Args:
            working_root (Path | None, optional): Defaults to None.
                User defined temporary working space.
                It's mainly used for test.
                It's used for argument "working_root" of class "SafeTrash".

            history_root (Path | None, optional): Defaults to None.
                User defined path of temporary working space
                    including date time string.
                It's used for argument "history_root" of class "SafeTrash".

            trash_root (Path | None, optional): Defaults to None.
                User defined path of trash box including date time string.
                It's used for argument "trash_root" of class "SafeTrash".

            override (bool, optional): Defaults to False.
                Override initial time count to "2023/4/1:12:00:00-00 (AM)".
                It's used for argument "override" of class "SafeTrash"
                    and function "create_date_time_space".

            jst (bool, optional): Defaults to False.
                If True, you can get datetime object as JST time zone.
                It's used for argument "jst" of class "SafeTrash"
                    and function "create_date_time_space".

            edit_root (Path | None, optional): Defaults to None.
                User defined path of temporary working space
                    including date time string to edit archive.
                It's used for argument "body_root" of
                    function "create_date_time_space".

        """
        self.__initialize_super_class(
            working_root,
            history_root,
            trash_root,
            override,
            jst,
        )
        self.__initialize_variables(edit_root, override, jst)
