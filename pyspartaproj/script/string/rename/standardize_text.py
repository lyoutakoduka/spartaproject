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
        return self.convert_strip(self.convert_under(_convert_lower(text)))
