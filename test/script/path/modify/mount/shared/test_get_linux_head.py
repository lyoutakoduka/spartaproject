#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to get the path of a mount point of Linux."""

from pyspartaproj.script.path.modify.mount.shared.get_linux_head import (
    get_linux_head,
)


def test_mount() -> None:
    """Test to get the path of a mount point of Linux."""
    assert "/mnt" == str(get_linux_head())
