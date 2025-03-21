#!/usr/bin/env python

import pytest
from pyspartalib.context.custom.callable_context import Func
from pyspartalib.context.default.integer_context import Ints


class _TestShare:
    def cache_error(
        self,
        function: Func,
        match: str,
        error: type[Exception] = ValueError,
    ) -> None:
        with pytest.raises(error, match=match):
            function()

    def cache_error_not_found(self, function: Func, match: str) -> None:
        self.cache_error(function, match, error=FileNotFoundError)

    def get_result_integer(self) -> Ints:
        return list(range(3))
