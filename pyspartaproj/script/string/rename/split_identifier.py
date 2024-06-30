#!/usr/bin/env python
# -*- coding: utf-8 -*-


class SplitIdentifier:
    def _initialize_identifier(self, identifier: str | None) -> None:
        if identifier is None:
            identifier = "_"

        self._identifier: str = identifier

    def _initialize_variables(self, identifier: str | None) -> None:
        self._initialize_identifier(identifier)

    def get_identifier(self) -> str:
        return self._identifier

    def convert_strip(self, text: str) -> str:
        return text.strip(self.get_identifier())

    def __init__(self, identifier: str | None = None) -> None:
        self._initialize_variables(identifier)
