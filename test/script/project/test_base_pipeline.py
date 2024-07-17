#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.path.modify.get_resource import get_resource


def _get_config_file() -> Path:
    return get_resource(local_path=Path("base_pipeline", "forward.json"))
