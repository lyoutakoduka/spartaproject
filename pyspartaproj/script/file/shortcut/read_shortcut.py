#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to read Windows shortcut information from PowerShell."""

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.path.modify.get_resource import get_resource
from pyspartaproj.script.path.modify.mount.convert_to_linux import (
    convert_to_linux,
)
from pyspartaproj.script.platform.platform_status import is_platform_linux
from pyspartaproj.script.shell.execute_powershell import (
    execute_powershell,
    get_double_quoted_command,
    get_path_string,
    get_quoted_path,
    get_script_string,
)


def _convert_to_linux(path: Path) -> Path:
    if is_platform_linux():
        return convert_to_linux(path)

    return path


def _convert_to_path(path_text: str) -> Path:
    return Path(path_text.replace("\\", "/"))


def _get_shortcut_command(shortcut_path: Path) -> str:
    return get_double_quoted_command(
        [
            get_script_string(get_resource(local_path=Path("read.ps1"))),
            get_quoted_path(get_path_string(shortcut_path)),
        ]
    )


def _execute_script(
    shortcut_path: Path, platform: str | None, forward: Path | None
) -> Strs:
    return list(
        execute_powershell(
            [_get_shortcut_command(shortcut_path)],
            platform=platform,
            forward=forward,
        )
    )


def _check_shortcut_exists(shortcut_path: Path) -> None:
    if not shortcut_path.exists():
        raise FileNotFoundError()


def _cleanup_result(result: Strs) -> Path | None:
    if 1 == len(result):
        return _convert_to_linux(_convert_to_path(result[0]))

    return None


def read_shortcut(
    shortcut_path: Path,
    platform: str | None = None,
    forward: Path | None = None,
) -> Path | None:
    """Read Windows shortcut information from PowerShell.

    Args:
        shortcut_path (Path): Path of shortcut you want to read inside.

        platform (str | None, optional): Defaults to None.
            You can select an execution platform from "linux" or "windows".
            Current execution platform is selected if argument is None.
            It's used for argument "platform" of function "execute_powershell".

        forward (Path | None, optional): Defaults to None.
            Path of setting file in order to place
                project context file to any place.
            It's used for argument "forward" of function "execute_powershell".

    Returns:
        Path | None: Path which is a link destination of shortcut.
    """
    _check_shortcut_exists(shortcut_path)

    return _cleanup_result(_execute_script(shortcut_path, platform, forward))
