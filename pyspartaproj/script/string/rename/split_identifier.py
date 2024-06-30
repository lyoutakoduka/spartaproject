#!/usr/bin/env python
# -*- coding: utf-8 -*-


class SplitIdentifier:
    def _initialize_variables(self, identifier: str | None) -> None:
        if identifier is None:
            identifier = "_"

        self._identifier: str = identifier

    def get_identifier(self) -> str:
        return self._identifier

    def __init__(self, identifier: str | None = None) -> None:
        self._initialize_variables(identifier)
