#!/usr/bin/env python

"""Module to create and manage the temporary working directory."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.custom.callable_context import BoolFunc


class WorkingDirectory:
    """Class to create and manage the temporary working directory."""

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
        """Get the root path of temporary working directory.

        Returns:
            Path: The root path of temporary working directory.

        """
        return self._working_root

    def inside_working(self, function: BoolFunc) -> bool:
        """Create the temporary working directory.

        Args:
            function (BoolFunc):
                Execute the specified function after create the directory.

        Returns:
            bool: True if the function is successfully executed.

        """
        with TemporaryDirectory() as working_path:
            return self._execute_function(function, Path(working_path))
