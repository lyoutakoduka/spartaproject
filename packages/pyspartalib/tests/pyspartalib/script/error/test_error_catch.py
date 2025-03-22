#!/usr/bin/env python

from pyspartalib.script.error.error_catch import ErrorCatch
from pyspartalib.script.error.error_raise import ErrorRaise


class TestValue(ErrorCatch, ErrorRaise):
    def _get_match(self) -> str:
        return "value"

    def _error_value(self) -> None:
        self.error_value(self._get_match())

    def test_value(self) -> None:
        self.catch_value(self._error_value, self._get_match())
