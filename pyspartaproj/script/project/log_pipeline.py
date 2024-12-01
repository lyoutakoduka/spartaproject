#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to handling I/O functionalities of any script called pipeline."""

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.time.count.log_timer import LogTimer


class LogPipeline(LogTimer):
    """Class to handling I/O functionalities of any script called pipeline."""

    def __initialize_super_class(self) -> None:
        super().__init__()

    def _show_message(self, message: str) -> None:
        print(message)

    def _log_with_timer(self, message: str, force: bool) -> None:
        if message_timer := self.get_readable_time(force=force):
            self._show_message(message_timer + ": " + message)

    def show_log(self, messages: Strs, force: bool = False) -> None:
        """Show message as log to stdout.

        Args:
            messages (Strs): Message list which will merged by space character.

            force (bool, optional): Defaults to False.
                Timer count is forcibly returned if it's True.
                It's used for argument "force" of
                    method "get_readable_time" in class "LogTimer".
        """
        self._log_with_timer(" ".join(messages), force)

    def __init__(self) -> None:
        """Initialize super class and variables."""
        self.__initialize_super_class()
