#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.context.typed.user_context import BaseName


class BaseNameElements:
    def _initialize_variables(self) -> None:
        self._split_identifier = "_"

    def _get_name_elements(self, name: str, index: int) -> BaseName:
        return {
            "name": name,
            "index": index,
        }

    def _get_index(self, index_text: str) -> int:
        return int(index_text)

    def split_name(self, name: str) -> BaseName:
        identifier: str = self._split_identifier
        names: Strs = name.split(identifier)

        return self._get_name_elements(names[0], self._get_index(names[-1]))

    def __init__(self) -> None:
        self._initialize_variables()
