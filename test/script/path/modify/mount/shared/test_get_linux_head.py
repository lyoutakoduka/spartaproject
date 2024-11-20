#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test Module to get a path that drive of Windows will be mounted."""

from pyspartaproj.script.path.modify.mount.shared.get_linux_head import (
    get_linux_head,
)


def test_mount() -> None:
    """Test to get a path that drive of Windows will be mounted."""
    assert "/mnt" == str(get_linux_head())
