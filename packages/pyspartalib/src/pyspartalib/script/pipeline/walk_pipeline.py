#!/usr/bin/env python

"""Module that iterates through a directory like "os.walk" module."""

from pyspartalib.context.default.string_context import Strs
from pyspartalib.context.extension.path_context import (
    PathBoolFunc,
    PathGeneFunc,
)
from pyspartalib.script.pipeline.log_pipeline import LogPipeline


class WalkPipeline(LogPipeline):
    """Class to iterates through a directory like walk module."""

    def __initialize_super_class(self, enable_shown: bool) -> None:
        super().__init__(enable_shown=enable_shown)

    def _initialize_walk(self, break_count: int) -> None:
        self._break_count = break_count

    def _force_logs(self, messages: Strs) -> None:
        self.show_log(messages, force=True)

    def _break_loop(self, count: int) -> bool:
        if count < self._break_count:
            return False

        self._force_logs(["break"])

        return True

    def walk_directory(
        self,
        generator: PathGeneFunc,
        iteration: PathBoolFunc,
    ) -> None:
        """Iterate through a directory.

        You can break iteration after a specific count.

        Args:
            generator (PathGeneFunc):
                Iterate through a directory using a user-defined path filter.

            iteration (PathBoolFunc):
                The function that is called in each iteration.
                If the function returns True,
                    the count for breaking the iteration is incremented.

        """
        count: int = 0

        for path in generator():
            if self._break_loop(count):
                break

            self._force_logs(["find", f"[{count}]", str(path)])

            if iteration(path):
                count += 1

    def launch_override(self) -> None:
        """Run just after launch super class.

        It's only used for method overriding.
        """

    def launch_pipeline(self, break_count: int = 1) -> None:
        """Provide an entry point of class as overridable method.

        Args:
            break_count (int, optional): Defaults to 1.
                The count that is condition for breaking the iteration.

        """
        self._initialize_walk(break_count)
        self.launch_override()

    def __init__(self, enable_shown: bool) -> None:
        """Initialize super class and variables.

        Args:
            enable_shown (bool, optional):
                Log messages are shown if True.
                It's used for argument "enable_shown" of class "LogPipeline".

        """
        self.__initialize_super_class(enable_shown)
