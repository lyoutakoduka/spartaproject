#! /usr/bin/env python

"""Module to get path in local resource directory."""

from pathlib import Path

from pyspartalib.script.frame.context.frame_context import StackFrame
from pyspartalib.script.frame.current_frame import CurrentFrame


def _get_current() -> StackFrame:
    return CurrentFrame().get_frame(offset=2)


def _get_parent(frame: StackFrame) -> Path:
    return frame["file"].parent


def get_resource(local_path: Path | None = None) -> Path:
    """Get path in local resource directory.

    Resource directory is directory named "resource"
        which is placed on same hierarchy as some script.

    e.g., the script including resource directory is follow.

    script_root/
        |--resource/
            |--directory/
                |--file
        |--script

    Args:
        local_path (Path | None, optional): Defaults to None.
            Path you want to get in resource directory as relative path.

        If you want to get "resource/directory/file",
            local_path is "directory/file".

    Returns:
        Path: Path based on resource directory.

    """
    resource: Path = Path(_get_parent(_get_current()), "resource")

    if local_path is None:
        return resource

    return Path(resource, local_path)
