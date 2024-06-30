#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.string.rename.grouped_characters import (
    GroupedCharacters,
)


class SplitIdentifier:
    def _initialize_identifier(self, identifier: str | None) -> None:
        if identifier is None:
            identifier = "_"

        self._identifier: str = identifier

    def _initialize_variables(self, identifier: str | None) -> None:
        self._initialize_identifier(identifier)

        self._other_table: Strs = GroupedCharacters().get_table()["other"]

    def _replace_other(self, single: str) -> str:
        return self.get_identifier() if single in self._other_table else single

    def get_identifier(self) -> str:
        return self._identifier

    def convert_strip(self, text: str) -> str:
        return text.strip(self.get_identifier())

    def __init__(self, identifier: str | None = None) -> None:
        self._initialize_variables(identifier)
