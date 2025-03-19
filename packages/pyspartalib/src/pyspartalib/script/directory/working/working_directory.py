#!/usr/bin/env python

from pathlib import Path

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
