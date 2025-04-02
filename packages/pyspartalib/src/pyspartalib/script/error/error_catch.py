#!/usr/bin/env python

"""Module to catch errors, and it is used through method overriding."""

from decimal import FloatOperation

import pytest
from pyspartalib.context.custom.callable_context import Func


class ErrorCatch:
    """Class to raise errors together with the error identifier."""

    def _catch_base(
        self,
        function: Func,
        error: type[Exception] = ValueError,
        match: str | None = None,
    ) -> None:
        with pytest.raises(error, match=match):
            function()

    def catch_value(self, function: Func, match: str) -> None:
        """Catch ValueError together with the error identifier.

        Args:
            function (Func):
                The function executed within the method to catch errors.

            match (str):
                The error identifier for correct error handling.
                Assign a unique string.

        """
        self._catch_base(function, match=match)

    def catch_not_found(self, function: Func, match: str) -> None:
        """Catch FileNotFoundError together with the error identifier.

        Args:
            function (Func):
                The function executed within the method to catch errors.

            match (str):
                The error identifier for correct error handling.
                Assign a unique string.

        """
        self._catch_base(function, error=FileNotFoundError, match=match)

    def catch_float(self, function: Func) -> None:
        """Catch FloatOperation for a test.

        Args:
            function (Func):
                The function executed within the method to catch errors.

        """
        self._catch_base(function, error=FloatOperation)
