#!/usr/bin/env python

"""Module to send the signal to raise an errors forcibly."""

from pyspartalib.context.default.string_context import Strs


class ErrorForce:
    """Class to send the signal to raise ana errors forcibly."""

    def __initialize_variables(self, error_types: Strs | None) -> None:
        self._error_types: Strs = self._set_fail_types(error_types)

    def _set_fail_types(self, error_types: Strs | None) -> Strs:
        if error_types is None:
            return []

        return error_types

    def send_signal(self, error_type: str) -> bool:
        """Send the signal to raise an errors forcibly.

        Args:
            error_type (str): The error type you raise forcibly.

        Returns:
            bool: True if the candidates include the error type.

        """
        return error_type in self._error_types

    def __init__(self, error_types: Strs | None = None) -> None:
        """Initialize class variables.

        Args:
            error_types (Strs | None, optional): Defaults to None.
                The candidates of error type you raise forcibly.

        """
        self.__initialize_variables(error_types)
