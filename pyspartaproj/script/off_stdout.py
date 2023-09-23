#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartaproj.context.callable_context import CP, CR, Callable
from pyspartaproj.script.decorator_generator import TransferFunction
from pyspartaproj.script.file.text.import_file import text_import


class StdoutText(TransferFunction):
    def wrapper(
        self,
        function: Callable[CP, CR],
        *arguments: CP.args,
        **key_arguments: CP.kwargs
    ) -> CR:
        def _execute_function() -> CR:
            return function(*arguments, **key_arguments)

        with TemporaryDirectory() as temporary_directory:
            temporary_path: Path = Path(temporary_directory, 'temporary')

            with open(temporary_path, 'w') as file:
                with redirect_stdout(file):
                    result: CR = _execute_function()

            self.stdout = text_import(temporary_path)

        return result

    def show(self) -> str:
        return self.stdout
