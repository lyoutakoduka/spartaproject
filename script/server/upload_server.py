#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import stat_result
from paramiko import SFTPAttributes

from context.default.string_context import Strs
from context.extension.path_context import Path, Paths
from script.path.modify.get_relative import get_relative
from script.server.connect_server import ConnectServer


class UploadServer(ConnectServer):
    def __init__(self) -> None:
        super().__init__()

    def __del__(self) -> None:
        super().__del__()

    def _get_upload_tree(self, path: Path) -> Paths:
        remote: Path = Path(self.get_type_text('remotePath'))

        tree: Paths = []

        for parent in path.parents:
            if not parent.is_relative_to(remote):
                continue

            if '.' != str(get_relative(parent, root_path=remote)):
                tree += [parent]

        return tree

    def _create_upload_tree(self, tree: Paths) -> None:
        if sftp := self.get_sftp():
            for path in reversed(tree):
                if path.name in sftp.listdir(path.parent.as_posix()):
                    continue

                sftp.mkdir(path.as_posix())

    def upload(self, source_path: Path, destination_local: Path) -> bool:
        destination_path = Path(
            self.get_type_text('remotePath'), destination_local
        )

        self._create_upload_tree(self._get_upload_tree(destination_path))

        status: stat_result = source_path.stat()
        paths: Strs = [
            path.as_posix() for path in [source_path, destination_path]
        ]

        if sftp := self.get_sftp():
            result: SFTPAttributes = sftp.put(paths[0], paths[1])
            return status.st_size == result.st_size

        return False
