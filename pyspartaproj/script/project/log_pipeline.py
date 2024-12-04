#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to handle I/O functionalities of any script called pipeline."""

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.time.count.log_timer import LogTimer


class LogPipeline(LogTimer):
    """Class to handle I/O functionalities of any script called pipeline."""

    def __initialize_super_class(self) -> None:
        super().__init__()

    def __initialize_variables(self, disable_shown: bool) -> None:
        self._disable_shown: bool = disable_shown
        self._log: Strs = []

    def _show_message(self, message: str) -> None:
        if self._disable_shown:
            self._log += [message]
        else:
            print(message)

    def _build_log(self, message_timer: str, messages: Strs) -> str:
        return message_timer + ": " + " ".join(messages)

    def _log_with_timer(self, messages: Strs, force: bool) -> None:
        if message_timer := self.get_readable_time(force=force):
            self._show_message(self._build_log(message_timer, messages))

    def _force_log(self, message: str) -> None:
        self.show_log([message], force=True)

    def get_log(self) -> Strs | None:
        """Get recorded log message.

        The log is recorded to instance inside
            if you set option to disable showing log.

        You can get the recorded log messages all together from this method.

        Returns:
            Strs | None: Recorded log message.
        """
        if 0 == len(self._log):
            return None

        log: Strs = self._log[:]
        self._log.clear()

        return log

    def show_log(self, messages: Strs, force: bool = False) -> None:
        """Show log message to stdout.

        Args:
            messages (Strs): Message list which will merged by space character.

            force (bool, optional): Defaults to False.
                Timer count is forcibly returned if it's True.
                It's used for argument "force" of
                    method "get_readable_time" in class "LogTimer".
        """
        self._log_with_timer(messages, force)

    def __del__(self) -> None:
        self._force_log("end")

    def __init__(self, disable_shown: bool = False) -> None:
        """Initialize super class and variables."""
        self.__initialize_super_class()
        self.__initialize_variables(disable_shown)

        self._force_log("begin")
