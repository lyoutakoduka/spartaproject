#!/usr/bin/env python

"""Module to redirect stdout to string variable forcibly."""

from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartalib.context.callable_context import CP, CR
from pyspartalib.script.decorator_generator import TransferFunction
from pyspartalib.script.file.text.import_file import text_import


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

        '''
        def message() -> None:
            print("test")
        '''

        Use decorator generated from this class as below.

        '''
        stdout_text = StdoutText()

        @stdout_text.decorator
        def message() -> None:
            print("test")
        '''

        Args:
            function (Callable[CP, CR]):
                Arguments of the function designated by decorator.
                Value of argument is automatically assigned when created.

        Returns:
            CR: Return value of the function designated by decorator.
                Value is automatically stored when executing the function.
        """

        def _execute_function() -> CR:
            return function(*arguments, **key_arguments)

        with TemporaryDirectory() as temporary_directory:
            temporary_path: Path = Path(temporary_directory, "temporary")

            with open(temporary_path, "w") as file:
                with redirect_stdout(file):
                    result: CR = _execute_function()

            self.stdout: str = text_import(temporary_path)

        return result

    def show(self) -> str:
        """Get string generated from stdout.

        Returns:
            str: String generated from stdout.
        """
        return self.stdout
