#!/usr/bin/env python

from pyspartalib.context.default.string_context import Strs


class ErrorForce:
    def _set_fail_types(self, error_types: Strs | None) -> Strs:
        if error_types is None:
            return []

        return error_types
