#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get path in local resource directory."""

from pathlib import Path

from pyspartaproj.script.stack_frame import current_frame


def get_resource(local_path: Path | None = None) -> Path:
    """Function to get path in local resource directory.

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
    resource: Path = Path(current_frame(offset=1)["file"].parent, "resource")

    if local_path is None:
        return resource

    return Path(resource, local_path)
