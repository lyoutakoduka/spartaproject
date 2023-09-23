#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.directory.create_directory_temporary import WorkSpace


class TemporaryWorkSpace(WorkSpace):
    pass


def test_create() -> None:
    work_space = TemporaryWorkSpace()
    work_space_root: Path = work_space.get_root()
    assert work_space_root.exists()


def main() -> bool:
    test_create()
    return True
