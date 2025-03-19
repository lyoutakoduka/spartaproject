#!/usr/bin/env python

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.custom.callable_context import BoolFunc


class WorkingDirectory:
    def _set_working_root(self, working_root: Path) -> None:
        self._working_root = working_root

    def _execute_function(
        self,
        function: BoolFunc,
        working_root: Path,
    ) -> bool:
        self._set_working_root(working_root)
        return function()

    def get_working_root(self) -> Path:
        return self._working_root

    def inside_working(self, function: BoolFunc) -> bool:
        with TemporaryDirectory() as working_path:
            return self._execute_function(function, Path(working_path))
