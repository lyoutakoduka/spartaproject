#!/usr/bin/env python

from collections.abc import Callable
from functools import wraps

from pyspartalib.context.callable_context import CP, CR


class TransferFunction:
    def wrapper(
        self,
        function: Callable[CP, CR],
        *arguments: CP.args,
        **key_arguments: CP.kwargs,
    ) -> CR:
        return function(*arguments, **key_arguments)

    def decorator(self, function: Callable[CP, CR]) -> Callable[CP, CR]:
        @wraps(function)
        def register_function(
            *arguments: CP.args,
            **key_arguments: CP.kwargs,
        ) -> CR:
            return self.wrapper(function, *arguments, **key_arguments)

        return register_function
