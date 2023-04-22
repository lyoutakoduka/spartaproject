#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from contextlib import redirect_stdout
from tempfile import TemporaryDirectory
from typing import Callable, TypeVar, ParamSpec

from scripts.deco_generator import TransferFunc

_R = TypeVar('_R')
_P = ParamSpec('_P')


class StdoutText(TransferFunc):
    def wrapper(self, func: Callable[_P, _R], *args: _P.args, **kwargs: _P.kwargs) -> _R:
        def _execute_func() -> _R:
            return func(*args, **kwargs)

        with TemporaryDirectory() as tmp_directory:
            tmp_file_path: str = os.path.join(tmp_directory, 'tmp')

            with open(tmp_file_path, 'w') as file:
                with redirect_stdout(file):
                    result: _R = _execute_func()

            with open(tmp_file_path, 'r') as file:
                self.stdout = file.read()

        return result

    def show(self) -> str:
        return self.stdout
