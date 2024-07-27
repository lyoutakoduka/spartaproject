#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to standardize string for key of dictionary."""

from pyspartaproj.script.string.rename.split_identifier import SplitIdentifier


class StandardizeText(SplitIdentifier):
    """Class to standardize string for key of dictionary."""

    def _convert_lower(self, text: str) -> str:
        return text.lower()

    def standardize(
        self,
        text: str,
        lower: bool = False,
        under: bool = False,
        strip: bool = False,
        replace: bool = False,
    ) -> str:
        """Function to standardize string for key of dictionary.

        Args:
            text (str): Text you want to standardize.

            lower (bool, optional): Defaults to False.
                Convert upper case letter to lower case letter.

            under (bool, optional): Defaults to False.
                Convert characters to the split identifier,
                    candidates are characters other than alphabets and numbers.
                It's executed from class "SplitIdentifier".

            strip (bool, optional): Defaults to False.
                Remove the split identifier of the both ends of string.
                It's executed from class "SplitIdentifier".

        Returns:
            str: Standardize text.
        """
        if lower:
            text = self._convert_lower(text)

        if under:
            text = self.convert_under(text)

        if strip:
            text = self.convert_strip(text)

        if replace:
            text = self.replace_identifier(text)

        return text

    def __init__(
        self,
        identifier: str | None = None,
    ) -> None:
        """Initialize variables and super class.

        Args:
            identifier (str | None, optional): Defaults to None.
                You can specify the split identifier by argument "identifier".
                It's used for argument "identifier" of class "SplitIdentifier".
        """
        super().__init__(identifier=identifier)
