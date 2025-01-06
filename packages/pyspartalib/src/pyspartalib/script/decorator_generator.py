#!/usr/bin/env python

from collections.abc import Callable
from functools import wraps

from pyspartalib.context.type_context import Param, Type


class TransferFunction:
    def wrapper(
        self,
        function: Callable[Param, Type],
        *arguments: Param.args,
        **key_arguments: Param.kwargs,
    ) -> Type:
        return function(*arguments, **key_arguments)

    def decorator(
        self,
        function: Callable[Param, Type],
    ) -> Callable[Param, Type]:
        @wraps(function)
        def register_function(
            *arguments: Param.args,
            **key_arguments: Param.kwargs,
        ) -> Type:
            return self.wrapper(function, *arguments, **key_arguments)

        return register_function
