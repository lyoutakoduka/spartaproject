#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to get the path of a mount point of Linux."""

from pyspartaproj.script.path.modify.mount.build_linux_path import (
    get_mount_point,
)


def test_mount() -> None:
    """Test to get the path of a mount point of Linux."""
    assert "/mnt" == str(get_mount_point())
