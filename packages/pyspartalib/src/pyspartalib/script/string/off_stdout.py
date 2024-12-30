#!/usr/bin/env python

"""Module to redirect stdout to string variable forcibly."""

from contextlib import redirect_stdout
from io import StringIO
from typing import Callable

from pyspartalib.context.callable_context import CP, CR
from pyspartalib.script.decorator_generator import TransferFunction


class StdoutText(TransferFunction):
    """Class to redirect stdout to string variable forcibly."""

    def wrapper(
        self,
        function: Callable[CP, CR],
        *arguments: CP.args,
        **key_arguments: CP.kwargs,
    ) -> CR:
        """Override the method from super class.

        Define a process in front and back of the function
            designated by decorator generated from this class.

        If you want to redirect stdout of following function "message".

            def message() -> None:
                print("test")

        Use decorator generated from this class as below.

            stdout_text = StdoutText()

            @stdout_text.decorator
            def message() -> None:
                print("test")

        Args:
            function (Callable[CP, CR]): The function to be decorated.

            *arguments (CP.args): Variable size arguments.

            **key_arguments (bool, optional): Variable size keyword arguments.

        Returns:
            CR: Return value of the function designated by decorator.
                Value is automatically stored when executing the function.

        """

        def _execute_function() -> CR:
            return function(*arguments, **key_arguments)

        file = StringIO()

        with redirect_stdout(file):
            result: CR = _execute_function()

        self.stdout: str = file.getvalue()

        return result

    def show(self) -> str:
        """Get string generated from stdout.

        Returns:
            str: String generated from stdout.

        """
        return self.stdout
