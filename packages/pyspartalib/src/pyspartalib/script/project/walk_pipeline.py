#!/usr/bin/env python

"""Module to iterate contents in a directory like walk module."""

from pyspartalib.script.project.log_pipeline import LogPipeline


class WalkPipeline(LogPipeline):
    """Class to iterate contents in a directory like walk module."""

    def __initialize_super_class(self, enable_shown: bool) -> None:
        super().__init__(enable_shown=enable_shown)

    def launch_pipeline(self) -> None:
        pass

    def __init__(self, enable_shown: bool) -> None:
        """Initialize super class and variables.

        Args:
            enable_shown (bool, optional):
                Log messages are shown if True.
                It's used for argument "enable_shown" of class "LogPipeline".

        """
        self.__initialize_super_class(enable_shown)
