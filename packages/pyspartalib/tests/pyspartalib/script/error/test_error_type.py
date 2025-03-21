#!/usr/bin/env python

import pytest
from pyspartalib.context.custom.callable_context import Func


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
