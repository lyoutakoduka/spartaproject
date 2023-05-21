#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory

from contexts.callable_context import CP, CR, Callable
from scripts.deco_generator import TransferFunc
from scripts.files.import_file import text_import


class StdoutText(TransferFunc):
    def wrapper(
        self, func: Callable[CP, CR], *args: CP.args, **kwargs: CP.kwargs,
    ) -> CR:
        def _execute_func() -> CR:
            return func(*args, **kwargs)

        with TemporaryDirectory() as tmp_directory:
            tmp_path: Path = Path(tmp_directory, 'tmp')

            with open(tmp_path, 'w') as file:
                with redirect_stdout(file):
                    result: CR = _execute_func()

            self.stdout = text_import(tmp_path)

        return result

    def show(self) -> str:
        return self.stdout
