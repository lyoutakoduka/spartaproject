#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.context.typed.user_context import BaseName
from pyspartaproj.script.string.base_name_elements import BaseNameElements


def _compare_elements(name: str, index: int, name_elements: BaseName) -> None:
    assert name == name_elements["name"]
    assert index == name_elements["index"]


def test_single() -> None:
    identifier: str = "_"
    name: str = "file"
    index: int = 1

    name_elements: BaseName = BaseNameElements().split_name(
        identifier.join([name, str(index).zfill(4)])
    )
    _compare_elements(name, index, name_elements)


def main() -> bool:
    test_single()
    return True
