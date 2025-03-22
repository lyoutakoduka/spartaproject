#!/usr/bin/env python

"""Module to raise errors, and it's used through method overriding."""

from collections.abc import Container, Sized
from pathlib import Path

from pyspartalib.context.custom.type_context import Type


class ErrorBase:
    """Class to raise errors together with the error identifier."""

    def _error_base(
        self,
        match: str,
        error: type[Exception] = ValueError,
    ) -> None:
        raise error(match)

    def error_value(self, match: str) -> None:
        """Raise ValueError together with the error identifier.

        Args:
            match (str):
                The error identifier for correct error handling.
                Assign a unique string.

        """
        self._error_base(match)

    def error_not_found(self, match: str) -> None:
        """Raise FileNotFoundError together with the error identifier.

        Args:
            match (str):
                The error identifier for correct error handling.
                Assign a unique string.

        """
        self._error_base(match, error=FileNotFoundError)


class _ErrorShare(ErrorBase):
    def _invert(self, result: bool, invert: bool) -> bool:
        return result ^ invert

    def raise_not_found(self, result: bool, match: str, invert: bool) -> None:
        if self._invert(result, invert):
            self.error_not_found(match)

    def raise_value(self, result: bool, match: str, invert: bool) -> None:
        if self._invert(result, invert):
            self.error_value(match)


class ErrorFail(_ErrorShare):
    """Class to raise error if the input value is False."""

    def __confirm(self, result: bool) -> bool:
        return not result

    def error_fail(
        self,
        result: bool,
        match: str,
        invert: bool = False,
    ) -> None:
        """Raise raise error if the input value is False.

        Args:
            result (bool): The boolean value you want to to check.

            match (str):
                The error identifier for correct error handling.
                Assign a unique string.

            invert (bool, optional): Defaults to False.
                If True, the condition to raise the error is inverted.

        """
        self.raise_value(self.__confirm(result), match, invert)


class ErrorNone(_ErrorShare):
    """Class to raise error if the input value is None."""

    def __confirm(self, result: object) -> bool:
        return result is None

    def error_none(
        self,
        result: object | None,
        match: str,
        invert: bool = False,
    ) -> None:
        """Raise error if the input value is None.

        Args:
            result (object | None): The value you want to to verify.

            match (str):
                The error identifier for correct error handling.
                Assign a unique string.

            invert (bool, optional): Defaults to False.
                If True, the condition to raise the error is inverted.

        """
        self.raise_value(self.__confirm(result), match, invert)

    def error_none_walrus(
        self,
        result: Type | None,
        match: str,
        invert: bool = False,
    ) -> Type | None:
        """Raise error if the input value is None.

        Args:
            result (object | None): The value you want to to verify.

            match (str):
                The error identifier for correct error handling.
                Assign a unique string.

            invert (bool, optional): Defaults to False.
                If True, the condition to raise the error is inverted.

        Returns:
            Type | None: Return the input argument "result" if no error occurs.

        """
        self.error_none(result, match, invert=invert)
        return result


class ErrorNoExists(_ErrorShare):
    """Class to raise error if the input path doesn't exist."""

    def __confirm(self, result: Path) -> bool:
        return not result.exists()

    def error_no_exists(
        self,
        result: Path,
        match: str,
        invert: bool = False,
    ) -> None:
        """Raise error if the input path doesn't exist.

        Args:
            result (Path): The path you want to to verify.

            match (str):
                The error identifier for correct error handling.
                Assign a unique string.

            invert (bool, optional): Defaults to False.
                If True, the condition to raise the error is inverted.

        """
        self.raise_not_found(self.__confirm(result), match, invert)


class ErrorContain(_ErrorShare):
    """Class to raise error if the input value is not in the container."""

    def __confirm(self, result: Container[Type], expected: object) -> bool:
        return expected not in result

    def error_contain(
        self,
        result: Container[Type],
        expected: Type,
        match: str,
        invert: bool = False,
    ) -> None:
        """Raise error if the input value is not in the container.

        Args:
            result (Container[Type]):
                The container you want to verify that the value is include.

            expected (Type): The value to be verified within the container.

            match (str):
                The error identifier for correct error handling.
                Assign a unique string.

            invert (bool, optional): Defaults to False.
                If True, the condition to raise the error is inverted.

        """
        self.raise_value(self.__confirm(result, expected), match, invert)


class ErrorLength(_ErrorShare):
    """Class to raise error if the length of Sized type isn't as expected."""

    def __confirm(self, result: Sized, expected: int) -> bool:
        return len(result) != expected

    def error_length(
        self,
        result: Sized,
        expected: int,
        match: str,
        invert: bool = False,
    ) -> None:
        """Raise error if the length of Sized type isn't as expected.

        Args:
            result (Sized): The Sized type you want to verify the length.

            expected (int): The expected length of the Sized type.

            match (str):
                The error identifier for correct error handling.
                Assign a unique string.

            invert (bool, optional): Defaults to False.
                If True, the condition to raise the error is inverted.

        """
        self.raise_value(self.__confirm(result, expected), match, invert)


class ErrorDifference(_ErrorShare):
    """Class to raise error if input the two values are different."""

    def __confirm(self, result: Type, expected: Type) -> bool:
        return result != expected

    def error_difference(
        self,
        result: Type,
        expected: Type,
        match: str,
        invert: bool = False,
    ) -> None:
        """Raise error if input the two values are different.

        Args:
            result (Type):
                For example, it's recommended to assign
                    such as the computed result.

            expected (Type):
                For example, it's recommended to assign
                    the expected value for comparison with the computed result.

            match (str):
                The error identifier for correct error handling.
                Assign a unique string.

            invert (bool, optional): Defaults to False.
                If True, the condition to raise the error is inverted.

        """
        self.raise_value(self.__confirm(result, expected), match, invert)
