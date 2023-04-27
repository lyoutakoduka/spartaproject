#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contextlib import redirect_stdout
from tempfile import TemporaryDirectory

from contexts.callable_context import CP, CR, Callable
from contexts.path_context import Path
from scripts.deco_generator import TransferFunc


class StdoutText(TransferFunc):
    def wrapper(self, func: Callable[CP, CR], *args: CP.args, **kwargs: CP.kwargs) -> CR:
        def _execute_func() -> CR:
            return func(*args, **kwargs)

        with TemporaryDirectory() as tmp_directory:
            tmp_file_path: Path = Path(tmp_directory, 'tmp')

            with open(tmp_file_path, 'w') as file:
                with redirect_stdout(file):
                    result: CR = _execute_func()

            with open(tmp_file_path, 'r') as file:
                self.stdout = file.read()

        return result

    def show(self) -> str:
        return self.stdout
