#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to standardize string for key of dictionary."""

from pyspartaproj.script.string.rename.split_identifier import SplitIdentifier


class StandardizeText(SplitIdentifier):
    def _initialize_variables_standardize(
        self, strip: bool, under: bool, lower: bool
    ) -> None:
        self._strip: bool = strip
        self._under: bool = under
        self._lower: bool = lower

    def _convert_lower(self, text: str) -> str:
        return text.lower()

    def standardize_text(self, text: str) -> str:
        """Function to standardize string for key of dictionary.

        Args:
            text (str): Text you want to standardize.

        Returns:
            str: Standardize text.
        """
        if self._lower:
            text = self._convert_lower(text)

        if self._under:
            text = self.convert_under(text)

        if self._strip:
            text = self.convert_strip(text)

        return text

    def __init__(
        self,
        identifier: str | None = None,
        strip: bool = False,
        under: bool = False,
        lower: bool = False,
    ) -> None:
        super().__init__(identifier=identifier)

        self._initialize_variables_standardize(strip, under, lower)
