#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to handling I/O functionality of any script called pipeline."""

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.project.project_context import ProjectContext
from pyspartaproj.script.time.count.log_timer import LogTimer


class BasePipeline(ProjectContext, LogTimer):
    """Class to handling I/O functionality of any script called pipeline."""

    def _initialize_super_class(
        self, platform: str | None, forward: Path | None
    ) -> None:
        ProjectContext.__init__(self, platform=platform, forward=forward)
        LogTimer.__init__(self)

    def _show_message(self, message: str) -> None:
        print(message)

    def _log_with_timer(self, message: str) -> None:
        if message_timer := self.get_readable_time(force=True):
            self._show_message(message_timer + ": " + message)

    def show_log(self, messages: Strs) -> None:
        """Show message as log to stdout.

        Args:
            messages (Strs): Message list which will merged by space character.
        """
        self._log_with_timer(" ".join(messages))

    def __init__(
        self, platform: str | None = None, forward: Path | None = None
    ) -> None:
        """Initialize super class and variables.

        Args:
            platform (str | None, optional): Defaults to None.
                You can select an execution platform from "linux" or "windows".
                Current execution platform is selected if argument is None.
                It's used for argument "platform" of class "ProjectContext".

            forward (Path | None, optional): Defaults to None.
                Path of setting file in order to place
                    project context file to any place.
                It's used for argument "forward" of class "ProjectContext".
        """
        self._initialize_super_class(platform, forward)
