#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import stat_result
from paramiko import SFTPAttributes

from context.default.string_context import Strs
from context.extension.path_context import Path, Paths
from script.path.iterate_directory import walk_iterator
from script.path.modify.get_relative import get_relative
from script.server.connect_server import ConnectServer


class UploadServer(ConnectServer):
    def __init__(self) -> None:
        super().__init__()

    def __del__(self) -> None:
        super().__del__()

    def _get_remote_root(self) -> Path:
        if sftp := self.get_sftp():
            if root := sftp.getcwd():
                return Path(root)

        return Path('')

    def _get_upload_tree(self, path: Path) -> Paths:
        remote: Path = self._get_remote_root()
        tree: Paths = []

        for parent in path.parents:
            if not parent.is_relative_to(remote):
                continue

            if '.' != str(get_relative(parent, root_path=remote)):
                tree += [parent]

        return tree

    def _exists_directory(self, path: Path) -> bool:
        if sftp := self.get_sftp():
            if path.name in sftp.listdir(path.parent.as_posix()):
                return True

        return False

    def _create_directory(self, path: Path) -> None:
        if sftp := self.get_sftp():
            if not self._exists_directory(path):
                sftp.mkdir(path.as_posix())

    def _create_upload_tree(self, path: Path) -> None:
        for path in reversed(self._get_upload_tree(path)):
            self._create_directory(path)

    def _convert_remote_path(self, local: Path) -> Path:
        return Path(self._get_remote_root(), local)

    def _create_file(self, source_path: Path, destination_path: Path) -> bool:
        status: stat_result = source_path.stat()
        paths: Strs = [
            path.as_posix() for path in [source_path, destination_path]
        ]

        if sftp := self.get_sftp():
            result: SFTPAttributes = sftp.put(paths[0], paths[1])
            return status.st_size == result.st_size

        return False

    def _path_with_tree(self, local: Path) -> Path:
        path: Path = self._convert_remote_path(local)
        self._create_upload_tree(path)
        return path

    def _upload_file(self, source_path: Path, destination_local: Path) -> bool:
        return self._create_file(
            source_path, self._path_with_tree(destination_local)
        )

    def _upload_directory(self, local: Path) -> None:
        self._create_directory(self._path_with_tree(local))

    def _upload_tree(self, source_path: Path, destination_local: Path) -> bool:
        for source_child in walk_iterator(source_path, depth=1):
            if not self.upload(
                source_child,
                Path(
                    destination_local,
                    get_relative(source_child, root_path=source_path)
                )
            ):
                return False
        else:
            self._upload_directory(destination_local)

        return True

    def upload(self, source_path: Path, destination_local: Path) -> bool:
        if source_path.is_dir():
            return self._upload_tree(source_path, destination_local)

        return self._upload_file(source_path, destination_local)
