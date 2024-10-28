#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to edit internal of archive file."""

from pathlib import Path

from pyspartaproj.context.extension.path_context import Paths
from pyspartaproj.context.extension.time_context import TimePair
from pyspartaproj.script.file.archive.compress_archive import CompressArchive
from pyspartaproj.script.file.archive.decompress_archive import (
    DecompressArchive,
)
from pyspartaproj.script.path.iterate_directory import walk_iterator
from pyspartaproj.script.path.safe.safe_trash import SafeTrash
from pyspartaproj.script.time.path.get_timestamp import get_directory_latest
from pyspartaproj.script.time.stamp.is_same_stamp import is_same_stamp


class EditArchive(SafeTrash):
    """Class to edit internal of archive file."""

    def _set_disable_archive(self, status: bool) -> None:
        self._disable_archive: bool = status

    def _initialize_variables_edit(
        self,
        edit_root: Path | None,
        override: bool,
        jst: bool,
    ) -> None:
        self._is_lzma_before: bool = False
        self._archive_path: Path | None = None
        self._still_removed: bool = False
        self._edit_root: Path = self.create_date_time_space(
            body_root=edit_root, override=override, jst=jst
        )

        self._set_disable_archive(False)

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
            [Path(path_text) for path_text in archive_stamp.keys()],
            archive_root=self.get_edit_root(),
        )

        return compress_archive.close_archived()

    def _decompress_archive(
        self, decompress_archive: DecompressArchive
    ) -> None:
        self._decompressed: Paths = decompress_archive.sequential_archives(
            self.get_archive_path()
        )
        decompress_archive.decompress_at_once(self._decompressed)

    def _record_compress_type(
        self, decompress_archive: DecompressArchive
    ) -> None:
        self._is_lzma_before = decompress_archive.is_lzma_archive(
            self.get_archive_path()
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

        super().__del__()

        return archived

    def is_disable_archive(self) -> bool:
        """Confirm path of archive is undefined.

        Returns:
            bool: True if archive is undefined.
        """
        return self._disable_archive

    def get_archive_path(self) -> Path:
        """Get path of archive you will edit.

        Raises:
            ValueError: Raise error if you don't set path information.

        Returns:
            Path: Path of archive.
        """
        if archive_path := self._archive_path:
            return archive_path

        raise ValueError

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

        if self._still_removed:
            return None

        self._still_removed = True
        self._set_disable_archive(True)

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
        self._initialize_archive_element(
            archive_path, limit_byte, compress, protected
        )

        if self.is_disable_archive():
            return None

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
        super().__init__(
            working_root=working_root,
            history_root=history_root,
            trash_root=trash_root,
            override=override,
            jst=jst,
        )

        self._initialize_variables_edit(edit_root, override, jst)
