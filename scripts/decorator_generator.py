#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps

from contexts.callable_context import CP, CR, Callable


class TransferFunc:
    def wrapper(
        self,
        function: Callable[CP, CR],
        *args: CP.args,
        **key_arguments: CP.kwargs,
    ) -> CR:
        return function(*args, **key_arguments)

    def decorator(self, function: Callable[CP, CR]) -> Callable[CP, CR]:
        @wraps(function)
        def register_function(
            *args: CP.args, **key_arguments: CP.kwargs,
        ) -> CR:
            return self.wrapper(function, *args, **key_arguments)
        return register_function
