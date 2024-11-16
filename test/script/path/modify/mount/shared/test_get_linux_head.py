#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.script.path.modify.mount.shared.get_linux_head import (
    get_linux_head,
)


def test_mount() -> None:
    assert "/mnt" == str(get_linux_head())
