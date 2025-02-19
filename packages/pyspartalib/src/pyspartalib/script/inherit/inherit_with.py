#!/usr/bin/env python

from types import TracebackType
from typing import Self


class InheritWith:
    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exception_type: type[BaseException] | None = None,
        exception_value: BaseException | None = None,
        traceback_type: TracebackType | None = None,
    ) -> None:
        return

    def __init__(self) -> None:
        return
