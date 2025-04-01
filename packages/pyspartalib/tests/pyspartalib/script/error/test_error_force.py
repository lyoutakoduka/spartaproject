#!/usr/bin/env python

from pyspartalib.context.default.string_context import Strs
from pyspartalib.script.error.error_force import ErrorForce


class _TestForce(ErrorForce):
    def __initialize_super_class(self, error_types: Strs | None) -> None:
        ErrorForce.__init__(self, error_types=error_types)

    def _outside_process(self) -> str | None:
        return "success"

    def __init__(self, error_types: Strs | None = None) -> None:
        self.__initialize_super_class(error_types)
