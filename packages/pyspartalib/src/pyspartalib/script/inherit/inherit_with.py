#!/usr/bin/env python

"""Module to use With statement by using custom class."""

from types import TracebackType
from typing import Self


class InheritWith:
    """Class to use With statement by using custom class."""

    def exit(self) -> None:
        return

    def __enter__(self) -> Self:
        """Return instance of itself from As statement.

        Returns:
            Self: Instance of the class.

        """
        return self

    def __exit__(
        self,
        exception_type: type[BaseException] | None = None,
        exception_value: BaseException | None = None,
        traceback_type: TracebackType | None = None,
    ) -> None:
        """Call custom method when leaving from With statement.

        Args:
            exception_type (type[BaseException] | None, optional):
                Defaults to None.
                Exception type used for context manager.

            exception_value (BaseException | None, optional): Defaults to None.
                Exception used for context manager.

            traceback_type (TracebackType | None, optional): Defaults to None.
                Traceback type used for context manager.

        """
        self.exit()

    def __init__(self) -> None:
        return
