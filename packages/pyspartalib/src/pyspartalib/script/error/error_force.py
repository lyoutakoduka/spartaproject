#!/usr/bin/env python

from pyspartalib.context.default.string_context import Strs


class ErrorForce:
    def __initialize_variables(self, error_types: Strs | None) -> None:
        self._error_types: Strs = self._set_fail_types(error_types)

    def _set_fail_types(self, error_types: Strs | None) -> Strs:
        if error_types is None:
            return []

        return error_types

    def __init__(self, error_types: Strs | None = None) -> None:
        self.__initialize_variables(error_types)
