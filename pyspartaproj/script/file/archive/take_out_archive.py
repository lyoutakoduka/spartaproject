#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to take out directory from inside of archive."""

from pathlib import Path

from pyspartaproj.context.extension.path_context import Paths, PathsPair
from pyspartaproj.script.file.archive.archive_format import rename_format
from pyspartaproj.script.file.archive.compress_archive import CompressArchive
from pyspartaproj.script.file.archive.edit_archive import EditArchive
from pyspartaproj.script.path.iterate_directory import walk_iterator
from pyspartaproj.script.path.modify.avoid_duplication import get_avoid_path
from pyspartaproj.script.path.safe.safe_trash import SafeTrash


class TakeOutArchive(EditArchive):
    def _initialize_variables_take(
        self, archive_path: Path, took_out_root: Path | None
    ) -> None:
        if took_out_root is None:
            took_out_root = archive_path.parent

        self._took_out_root: Path = took_out_root

    def _get_archive_name(self, took_out_root: Path, archive_id: str) -> str:
        archive_path: Path = get_avoid_path(
            rename_format(Path(took_out_root, archive_id))
        )
        return archive_path.stem

    def _take_out_archive(
        self, took_out_root: Path, file_paths: Paths, archive_id: str
    ) -> Path:
        compress_archive = CompressArchive(
            took_out_root,
            archive_id=self._get_archive_name(took_out_root, archive_id),
        )

        compress_archive.compress_at_once(file_paths)
        return compress_archive.close_archived()[0]

    def _take_out_archives(
        self, took_out_root: Path, inside_directory: PathsPair
    ) -> Paths:
        return [
            self._take_out_archive(
                took_out_root, file_paths, Path(directory_text).name
            )
            for directory_text, file_paths in inside_directory.items()
        ]

    def _get_take_out(self, directory_root: Path) -> Paths | None:
        file_paths: Paths = []

        for path in walk_iterator(directory_root):
            if path.is_dir():
                return None

            file_paths += [path]

        return None if 0 == len(file_paths) else file_paths

    def _get_inside_directory(self, decompressed_root: Path) -> PathsPair:
        return {
            str(directory_root): file_paths
            for directory_root in walk_iterator(decompressed_root, file=False)
            if (file_paths := self._get_take_out(directory_root))
        }

    def _remove_unused(self, remove_root: Path | None, paths: Paths) -> None:
        SafeTrash(remove_root=remove_root).trash_at_once(paths)

    def _remove_took_out(
        self, remove_root: Path | None, inside_directory: PathsPair
    ) -> None:
        self._remove_unused(
            remove_root, [Path(text) for text in inside_directory.keys()]
        )

    def _took_out_cycle(
        self,
        took_out_root: Path,
        remove_root: Path | None,
        decompressed_root: Path,
        archive_paths: Paths,
    ) -> None:
        inside_directory: PathsPair = self._get_inside_directory(
            decompressed_root
        )

        if 0 < len(inside_directory):
            archive_paths += self._take_out_archives(
                took_out_root, inside_directory
            )
            self._remove_took_out(remove_root, inside_directory)
            self._took_out_cycle(
                took_out_root, remove_root, decompressed_root, archive_paths
            )

    def _get_took_out(
        self,
        took_out_root: Path,
        remove_root: Path | None,
        decompressed_root: Path,
    ) -> Paths:
        archive_paths: Paths = []
        self._took_out_cycle(
            took_out_root, remove_root, decompressed_root, archive_paths
        )
        return archive_paths

    def get_took_out_root(self) -> Path:
        return self._took_out_root

    def take_out(
        self,
        archive_path: Path,
        took_out_root: Path | None = None,
        remove_root: Path | None = None,
        protected: bool = False,
    ) -> Paths:
        """Take out directory from inside of archive.

        Behavior of take out process is generally split into following 3 pattern.

        Pattern 1: Do Nothing if archive is applicable to following 2 pattern.

        root/
        |--archive.zip
            |--file

        root/
        |--archive.zip
            |--directory/

        Pattern 2: Take out end of directories
            if the archive is applicable to following 3 types.

        Type 1: Single directory.

        root/ # Before.
        |--archive.zip
            |--directory/
                |--file

        root/ # After.
        |--directory.zip
            |--file
        |--archive.zip

        Type 2: List of directories.

        root/ # Before.
        |--archive.zip
            |--directory_A/
                |--file_A
            |--directory_B/
                |--file_B

        Type 3: Nested directories.

        root/ # Before.
        |--archive.zip
            |--directory_A/
                |--file_A
                |--directory_B/
                    |--file_B

        Result of Type 2 and 3 is same.

        root/
        |--directory_A.zip
            |--file_A
        |--directory_B.zip
            |--file_B
        |--archive.zip

        Pattern 3: Avoid override path.

        root/ # Before.
        |--archive.zip
            |--directory_A/
                |--directory_same/
                    |--file_A
            |--directory_B/
                |--directory_same/
                    |--file_B

        root/ # After.
        |--directory_same.zip
            |--file_A
        |--directory_same_.zip
            |--file_B
        |--archive.zip
            |--directory_A/
            |--directory_B/

        Args:
            archive_path (Path): Path of archive you want to take out.

            took_out_root (Path | None, optional): Defaults to None.
                Destination directory that took out directories in archive.

            remove_root (Path | None, optional): Defaults to None.
                Path of directory used as trash box.
                It's used for argument "remove_root" of class "SafeTrash".

            protected (bool, optional): Defaults to False.
                True if you don't want to update original archive.
                It's used for argument "protected" of class "EditArchive".

        Returns:
            Paths: List of directory path which is took out.
        """
        if took_out_root is None:
            took_out_root = archive_path.parent

        edit_archive = EditArchive(archive_path, protected=protected)
        return self._get_took_out(
            took_out_root, remove_root, edit_archive.get_decompress_root()
        )
