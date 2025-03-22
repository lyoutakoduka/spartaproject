#!/usr/bin/env python

from pyspartalib.script.error.error_catch import ErrorCatch
from pyspartalib.script.error.error_raise import ErrorRaise


class TestValue(ErrorCatch, ErrorRaise):
    def _get_match(self) -> str:
        return "value"
