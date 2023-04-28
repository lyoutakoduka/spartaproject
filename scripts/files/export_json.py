#!/usr/bin/env python
# -*- coding: utf-8 -*-

from json import dumps

from contexts.path_context import Path
from contexts.json_context import TypeJson


def _export_text(path: Path, content: str) -> None:
    with open(path, 'w') as file:
        file.write(content)


def json_dump(content: TypeJson) -> str:
    return dumps(content, indent=2, ensure_ascii=False, sort_keys=True)


def json_export(export_path: Path, content: TypeJson) -> None:
    _export_text(export_path, json_dump(content))
