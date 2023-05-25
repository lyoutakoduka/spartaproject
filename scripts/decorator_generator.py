#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps

from contexts.callable_context import CP, CR, Callable


class TransferFunc:
    def wrapper(
        self, func: Callable[CP, CR], *args: CP.args, **kwargs: CP.kwargs,
    ) -> CR:
        return func(*args, **kwargs)

    def decorator(self, func: Callable[CP, CR]) -> Callable[CP, CR]:
        @wraps(func)
        def register_func(*args: CP.args, **kwargs: CP.kwargs) -> CR:
            return self.wrapper(func, *args, **kwargs)
        return register_func
