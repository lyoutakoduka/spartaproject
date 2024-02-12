#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get current working directory."""

from pathlib import Path


def get_current() -> Path:
    """Get current working directory.

    Call from symbolic link on Linux is not support

    Returns:
        Path: Current working directory.
    """
    return Path().cwd()
