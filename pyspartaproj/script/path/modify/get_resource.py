#! /usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.stack_frame import current_frame


def get_resource(children: Strs) -> Path:
    return Path(current_frame(offset=1)["file"].parent, "resource", *children)
