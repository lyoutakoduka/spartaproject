#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to convert string by using the split identifier."""

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.string.rename.grouped_characters import (
    GroupedCharacters,
)


class SplitIdentifier:
    """Class to convert string by using the split identifier."""

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
        """Get selected the split identifier.

        Returns:
            str: The split identifier, default is under bar.
        """
        return self._identifier

    def convert_strip(self, text: str) -> str:
        """Remove the split identifier of the both ends of string.

        You can get string "sample",
            if argument "text" is "_sample_" and identifier is "_".

        Args:
            text (str): String you want to remove the split identifier.

        Returns:
            str: String with the split identifier removed.
        """
        return text.strip(self.get_identifier())

    def convert_under(self, text: str) -> str:
        """Convert characters to the split identifier.

        Candidates are characters other than alphabets and numbers.

        You can get string "sample_domain_com",
            if argument "text" is "sample@domain.com" and identifier is "_".

        Args:
            text (str): String you want to convert to the split identifier.

        Returns:
            str: Converted string.
        """
        return "".join([self._replace_other(single) for single in text])

    def __init__(self, identifier: str | None = None) -> None:
        """Initialize variables and the split identifier.

        Args:
            identifier (str | None, optional): Defaults to None.
                You can specify the split identifier by argument "identifier",
                    and default split identifier is character "_".
        """
        self._initialize_variables(identifier)
