#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to standardize string for key of dictionary."""


class StandardizeText:
    def _convert_lower(self, text: str) -> str:
        return text.lower()

    def _convert_under(self, text: str) -> str:
        for identifier in [" ", ".", "-"]:
            text = text.replace(identifier, "_")

        return text

    def _convert_strip(self, text: str) -> str:
        return text.strip("_")

    def standardize_text(self, text: str) -> str:
        """Function to standardize string for key of dictionary.

        Args:
            text (str): Text you want to standardize.

        Returns:
            str: Standardize text.
        """
        return _convert_strip(_convert_under(_convert_lower(text)))
