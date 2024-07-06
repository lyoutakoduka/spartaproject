#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.string.rename.grouped_characters import (
    GroupedCharacters,
)


class FilterTable(GroupedCharacters):
    def _serialize_tables(self) -> Strs:
        serialized: Strs = []

        for table in self.get_merged_tables():
            serialized += table

        return serialized

    def __init__(self, multiple: bool = False) -> None:
        super().__init__(multiple=multiple)
