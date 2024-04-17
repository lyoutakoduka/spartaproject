#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to edit internal of archive file."""

from pathlib import Path

from pyspartaproj.context.extension.path_context import Paths
from pyspartaproj.context.extension.time_context import TimePair
from pyspartaproj.script.directory.create_directory_temporary import WorkSpace
from pyspartaproj.script.file.archive.compress_archive import CompressArchive
from pyspartaproj.script.file.archive.decompress_archive import (
    DecompressArchive,
)
from pyspartaproj.script.path.iterate_directory import walk_iterator
from pyspartaproj.script.path.safe.safe_trash import SafeTrash
from pyspartaproj.script.time.stamp.get_timestamp import (
    get_directory_latest,
    is_same_stamp,
)


class EditArchive(WorkSpace):
    """Class to edit internal of archive file."""

    def _initialize_variables(
        self,
        archive_path: Path,
        limit_byte: int,
        compress: bool,
        protected: bool,
        remove_root: Path | None,
    ) -> None:
        self._still_removed: bool = False
        self._archive_path: Path = archive_path
        self._limit_byte: int = limit_byte
        self._is_lzma_after: bool = compress
        self._protected: bool = protected
        self._remove_root: Path | None = remove_root

    def _get_archive_stamp(self) -> TimePair:
        return get_directory_latest(walk_iterator(self.get_root()))

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

    def _remove_unused(self, paths: Paths) -> None:
        SafeTrash(remove_root=self._remove_root).trash_at_once(paths)

    def _cleanup_before_override(self) -> None:
        self._remove_unused(self._decompressed)

    def _compress_archive(self, archive_stamp: TimePair) -> Paths:
        self._cleanup_before_override()

        compress_archive = CompressArchive(
            self._archive_path.parent,
            limit_byte=self._limit_byte,
            compress=self._is_lzma_after,
            archive_id=self._archive_path.stem,
        )

        compress_archive.compress_at_once(
            [Path(path_text) for path_text in archive_stamp.keys()],
            archive_root=self.get_root(),
        )

        return compress_archive.close_archived()

    def _decompress_archive(
        self, decompress_archive: DecompressArchive
    ) -> None:
        self._decompressed: Paths = decompress_archive.sequential_archives(
            self._archive_path
        )
        decompress_archive.decompress_at_once(self._decompressed)

    def _record_compress_type(
        self, decompress_archive: DecompressArchive
    ) -> None:
        self._is_lzma_before: bool = decompress_archive.is_lzma_archive(
            self._archive_path
        )

    def _initialize_archive(self) -> None:
        decompress_archive = DecompressArchive(self.get_root())

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

    def get_decompressed_root(self) -> Path:
        """Get path of temporary working directory.

        The directory is used for placing decompressed contents of archive.

        Returns:
            Path: Path of temporary working directory.
        """
        return self.get_root()

    def close_archive(self) -> Paths | None:
        """Compress the contents of temporary working directory to archive.

        Returns:
            Paths | None: Path of compressed archive.
                Return "None" if the archive you want to edit isn't changed.
        """
        if self._still_removed:
            return None

        self._still_removed = True

        return self._finalize_archive()

    def __del__(self) -> None:
        """Close and recompress archive you want to edit automatically."""
        self.close_archive()

    def __init__(
        self,
        archive_path: Path,
        limit_byte: int = 0,
        compress: bool = False,
        protected: bool = False,
        remove_root: Path | None = None,
    ) -> None:
        """Initialize variables and decompress archive you selected.

        Args:
            archive_path (Path): Path of archive you want to edit.

            limit_byte (int, optional): Defaults to 0.
                If it's not 0, archive are dividedly compressed.
                It's used for argument "limit_byte" of class "CompressArchive".

            compress (bool, optional): Defaults to False.
                If it's True, you can compress archive by LZMA format.
                It's used for argument "compress" of class "CompressArchive".

            protected (bool, optional): Defaults to False.
                True if you don't want to update original archive.
        """
        super().__init__()

        self._initialize_variables(
            archive_path, limit_byte, compress, protected, remove_root
        )
        self._initialize_archive()
