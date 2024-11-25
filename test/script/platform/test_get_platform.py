#!/usr/bin/env python
# -*- coding: utf-8 -*-

from platform import uname

from pyspartaproj.script.platform.get_platform import (
    get_platform,
    is_platform_linux,
)


def _get_platform() -> str:
    return uname().system.lower()


def _valid_platform(platform: str) -> str | None:
    if platform in ["linux", "windows"]:
        return platform

    return None


def test_name() -> None:
    assert _valid_platform(_get_platform()) == get_platform()


def test_linux() -> None:
    if "Linux" == _get_platform():
        assert is_platform_linux()
