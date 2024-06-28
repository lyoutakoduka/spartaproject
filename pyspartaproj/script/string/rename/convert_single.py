#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to convert multiple byte characters to single byte characters."""

from pyspartaproj.context.default.string_context import (
    StrPair,
    Strs2,
    Strs3,
    Trans,
)
from pyspartaproj.context.typed.user_context import CharacterTable
from pyspartaproj.script.string.rename.grouped_characters import (
    GroupedCharacters,
)


class ConvertSingle:
    """Class to convert multiple byte characters to single byte."""

    def _get_merged_tables(self, table: CharacterTable) -> Strs2:
        return [table["big"], table["small"], table["number"], table["other"]]

    def _get_tables_pair(self) -> Strs3:
        return [
            self._get_merged_tables(
                GroupedCharacters(multiple=(0 == i)).get_table()
            )
            for i in range(2)
        ]

    def _get_link_table(self, tables_pair: Strs3) -> StrPair:
        return {
            big: small
            for big_table, small_table in zip(tables_pair[0], tables_pair[1])
            for big, small in zip(big_table, small_table)
        }

    def convert(self, text: str) -> str:
        """Convert multiple byte characters to single byte characters.

        Args:
            text (str): String which might include multiple byte characters.

        Returns:
            str: Converted single byte characters.
        """
        # Type Trans is necessary.
        translated: Trans = str.maketrans(
            self._get_link_table(self._get_tables_pair())
        )
        return text.translate(translated)
