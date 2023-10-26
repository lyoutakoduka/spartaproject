#! /usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.stack_frame import current_frame


def get_resource(resource_path: Path) -> Path:
    return Path(
        current_frame(offset=1)["file"].parent, "resource", resource_path
    )
