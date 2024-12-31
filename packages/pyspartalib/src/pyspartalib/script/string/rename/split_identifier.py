#!/usr/bin/env python

"""Module to convert string by using the split identifier."""

from pyspartalib.context.default.string_context import Strs
from pyspartalib.script.string.rename.grouped_characters import (
    GroupedCharacters,
)


class SplitIdentifier:
    """Class to convert string by using the split identifier."""

    def _initialize_identifier(self, identifier: str | None) -> str:
        if identifier is None:
            return "_"

        return identifier

    def _get_other_table(self) -> Strs:
        return GroupedCharacters().get_table()["other"]

    def __initialize_variables(self, identifier: str | None) -> None:
        self._identifier: str = self._initialize_identifier(identifier)
        self._other_table: Strs = self._get_other_table()

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

    def replace_identifier(self, text: str) -> str:
        """Replace one or more consecutive split identifier.

        Args:
            text (str): String you want to replace the split identifier.

        Returns:
            str: Replaced string.

        """
        identifier: str = self.get_identifier()
        return identifier.join(
            [line for line in text.split(identifier) if len(line) > 0],
        )

    def switch_identifier(self, text: str, identifier: str) -> str:
        """Switch the split identifier to specific character.

        Args:
            text (str): String you want to switch the split identifier.


            identifier (str):
                Character which is used instead of the split identifier.

        Returns:
            str: String that the split identifier is switched.

        """
        return text.replace(self.get_identifier(), identifier)

    def __init__(self, identifier: str | None = None) -> None:
        """Initialize variables and the split identifier.

        Args:
            identifier (str | None, optional): Defaults to None.
                You can specify the split identifier by argument "identifier",
                    and default split identifier is character "_".

        """
        self.__initialize_variables(identifier)
