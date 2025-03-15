#!/usr/bin/env python

"""Module to iterate contents in a directory like walk module."""

from pyspartalib.context.default.string_context import Strs
from pyspartalib.script.pipeline.log_pipeline import LogPipeline


class WalkPipeline(LogPipeline):
    """Class to iterate contents in a directory like walk module."""

    def __initialize_super_class(self, enable_shown: bool) -> None:
        super().__init__(enable_shown=enable_shown)

    def _initialize_walk(self, interrupt: int) -> None:
        self._interrupt = interrupt

    def _force_logs(self, messages: Strs) -> None:
        self.show_log(messages, force=True)

    def _break_loop(self, index: int) -> bool:
        if index < self._interrupt:
            return False

        self._force_logs(["break"])

        return True

    def launch_override(self) -> None:
        pass

    def launch_pipeline(self, interrupt: int = 1) -> None:
        """Provide an entry point of class as overridable method."""
        self._initialize_walk(interrupt)
        self.launch_override()

    def __init__(self, enable_shown: bool) -> None:
        """Initialize super class and variables.

        Args:
            enable_shown (bool, optional):
                Log messages are shown if True.
                It's used for argument "enable_shown" of class "LogPipeline".

        """
        self.__initialize_super_class(enable_shown)
