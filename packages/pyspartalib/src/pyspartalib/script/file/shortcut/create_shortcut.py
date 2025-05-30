#!/usr/bin/env python

"""Module to create Windows shortcut from PowerShell."""

from pathlib import Path

from pyspartalib.context.default.string_context import StrGene, Strs
from pyspartalib.script.path.modify.get_resource import get_resource
from pyspartalib.script.path.modify.mount.convert_to_windows import (
    convert_to_windows,
)
from pyspartalib.script.path.safe.safe_trash import SafeTrash
from pyspartalib.script.platform.platform_status import is_platform_linux
from pyspartalib.script.shell.execute_powershell import (
    execute_powershell,
    get_double_quoted_command,
    get_path_string,
    get_quoted_path,
    get_script_string,
)


def _no_exists_error(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError


def _convert_to_windows(path: Path) -> Path:
    if is_platform_linux():
        return convert_to_windows(path)

    return path


def _get_quoted_command(shortcut_target: Path, shortcut_path: Path) -> Strs:
    return [
        get_quoted_path(get_path_string(_convert_to_windows(path)))
        for path in [shortcut_target, shortcut_path]
    ]


def _get_resource_script() -> str:
    return get_script_string(get_resource(local_path=Path("create.ps1")))


def _get_shortcut_command(shortcut_target: Path, shortcut_path: Path) -> str:
    commands: Strs = [_get_resource_script()]
    return get_double_quoted_command(
        commands + _get_quoted_command(shortcut_target, shortcut_path),
    )


def _execute_script(
    shortcut_target: Path,
    shortcut_path: Path,
    platform: str | None,
    forward: Path | None,
) -> StrGene:
    return execute_powershell(
        [_get_shortcut_command(shortcut_target, shortcut_path)],
        platform=platform,
        forward=forward,
    )


def _cleanup_shortcut(shortcut_path: Path, remove_root: Path | None) -> None:
    if shortcut_path.exists():
        SafeTrash(trash_root=remove_root).trash(shortcut_path)


def create_shortcut(
    shortcut_target: Path,
    shortcut_path: Path,
    remove_root: Path | None = None,
    platform: str | None = None,
    forward: Path | None = None,
) -> bool:
    """Create Windows shortcut from PowerShell.

    Args:
        shortcut_target (Path): Path which is a link destination of shortcut.

        shortcut_path (Path): Path of shortcut you want to create.
            Extension of shortcut should be ".lnk".

        remove_root (Path | None, optional): Defaults to None.
            Path of directory used as trash box.
            It's used for argument "remove_root" of class "SafeTrash".

        platform (str | None, optional): Defaults to None.
            You can select an execution platform from "linux" or "windows".
            Current execution platform is selected if argument is None.
            It's used for argument "platform" of function "execute_powershell".

        forward (Path | None, optional): Defaults to None.
            Path of setting file in order to place
                project context file to any place.
            It's used for argument "forward" of function "execute_powershell".

    Returns:
        bool: True if creating shortcut is success.

    """
    _no_exists_error(shortcut_target)
    _cleanup_shortcut(shortcut_path, remove_root)

    list(_execute_script(shortcut_target, shortcut_path, platform, forward))

    return True
