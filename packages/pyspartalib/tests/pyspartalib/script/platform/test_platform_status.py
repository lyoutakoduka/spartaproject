#!/usr/bin/env python

"""Test module to get the platform of current executing script."""

from platform import uname

from pyspartalib.script.platform.platform_status import (
    get_platform,
    is_platform_linux,
)


def _status_error(status: bool) -> None:
    if not status:
        raise ValueError


def _get_platform() -> str:
    return uname().system.lower()


def _valid_platform(platform: str) -> str | None:
    if platform in ["linux", "windows"]:
        return platform

    return None


def test_name() -> None:
    """Test to get the platform of current executing script."""
    _status_error(_valid_platform(_get_platform()) == get_platform())


def test_linux() -> None:
    """Test to confirm that the platform of executing script is Linux."""
    if _get_platform() == "linux":
        _status_error(is_platform_linux())
