#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to confirm that characters in selected string.

Each character should be included in user defined character tables.
"""

from pyspartalib.context.default.string_context import Strs
from pyspartalib.script.string.rename.grouped_characters import (
    GroupedCharacters,
)


class FilterTable(GroupedCharacters):
    """Class to confirm that characters in selected string.

    Each character should be included in user defined character tables.
    """

    def __initialize_super_class(self, multiple: bool) -> None:
        super().__init__(multiple=multiple)

    def _serialize_tables(self) -> Strs:
        serialized: Strs = []

        for table in self.get_merged_tables():
            serialized += table

        return serialized

    def __initialize_variables(self) -> None:
        self._serialized: Strs = self._serialize_tables()

    def contain(self, text: str) -> bool:
        """Confirm that characters in selected string.

        Each character should be included in user defined character tables.

        e.g., return False if argument "text" is "ābc",
            because character "ā" is not included in character tables.

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

        Character tables used for confirming are defined in super class.

        Args:
            multiple (bool, optional): Defaults to False.
                True if you want to select character tables
                    which is constructed by multiple byte.
                It's used for argument "multiple" of class "GroupedCharacters".
        """
        self.__initialize_super_class(multiple)
        self.__initialize_variables()
