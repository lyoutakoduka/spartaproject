#!/usr/bin/env python

from decimal import FloatOperation

import pytest
from pyspartalib.context.custom.callable_context import Func


class ErrorCatch:
    def _catch_base(
        self,
        function: Func,
        error: type[Exception] = ValueError,
        match: str | None = None,
    ) -> None:
        with pytest.raises(error, match=match):
            function()

    def catch_value(self, function: Func, match: str) -> None:
        self._catch_base(function, match=match)

    def catch_not_found(self, function: Func, match: str) -> None:
        self._catch_base(function, error=FileNotFoundError, match=match)

    def catch_float(self, function: Func) -> None:
        self._catch_base(function, error=FloatOperation)
