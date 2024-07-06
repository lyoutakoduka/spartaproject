#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to confirm that characters in selected string.

Each character should be included in user defined character tables.
"""

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.string.rename.grouped_characters import (
    GroupedCharacters,
)


class FilterTable(GroupedCharacters):
    """Class to confirm that characters in selected string.

    Each character should be included in user defined character tables.
    """

    def _serialize_tables(self) -> Strs:
        serialized: Strs = []

        for table in self.get_merged_tables():
            serialized += table

        return serialized

    def _initialize_variables_filter(self) -> None:
        self._serialized: Strs = self._serialize_tables()

    def contain(self, text: str) -> bool:
        """Confirm that characters in selected string.

        Each character should be included in user defined character tables.

        Args:
            text (str): String you want to confirm.

        Returns:
            bool: True if all characters are exists in character tables.
        """
        for single in text:
            if single not in self._serialized:
                return False

        return True

    def __init__(self, multiple: bool = False) -> None:
        """Initialize super class and variables.

        Args:
            multiple (bool, optional): Defaults to False.
                True if you want to select character tables
                    which is constructed by multiple byte.
                It's used for argument "multiple" of class "GroupedCharacters".
        """
        super().__init__(multiple=multiple)

        self._initialize_variables_filter()
