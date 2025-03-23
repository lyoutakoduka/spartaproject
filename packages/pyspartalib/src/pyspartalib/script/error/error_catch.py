#!/usr/bin/env python

import pytest
from pyspartalib.context.custom.callable_context import Func


class ErrorCatch:
    def catch_value(
        self,
        function: Func,
        error: type[Exception] = ValueError,
        match: str | None = None,
    ) -> None:
        with pytest.raises(error, match=match):
            function()

    def catch_not_found(self, function: Func, match: str) -> None:
        self.catch_value(function, match, error=FileNotFoundError)
