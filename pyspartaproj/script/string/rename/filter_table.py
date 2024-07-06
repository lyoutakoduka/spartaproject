#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pyspartaproj.script.string.rename.grouped_characters import (
    GroupedCharacters,
)


class FilterTable(GroupedCharacters):
    def __init__(self, multiple: bool = False) -> None:
        super().__init__(multiple=multiple)
